"""
Advanced mathematical engine for coastal hydrodynamics.
Includes symbolic computation, numerical methods, and verification.
"""
import numpy as np
from scipy.optimize import brentq, fsolve, minimize_scalar
from scipy.integrate import odeint, quad, simpson
from scipy.interpolate import interp1d
import sympy as sp
from sympy import symbols, cos, sin, sqrt, pi, sinh, cosh, tanh, diff, integrate, solve, oo
from mpmath import mp, mpf, findroot
import warnings

warnings.filterwarnings('ignore')


class SymbolicCoastalMath:
    """Symbolic mathematical engine for coastal engineering."""
    
    @staticmethod
    def dispersion_relation(k=None, omega=None, h=None, g=9.81, symbolic=False):
        """
        Dispersion relation: ω² = gk·tanh(kh)
        
        Given any two parameters, solve for the third.
        
        Args:
            k: Wave number (rad/m)
            omega: Angular frequency (rad/s)
            h: Water depth (m)
            g: Gravitational acceleration (m/s²)
            symbolic: If True, return symbolic expression
            
        Returns:
            dict with solution and verification
        """
        if symbolic:
            k_sym, omega_sym, h_sym, g_sym = symbols('k omega h g', positive=True, real=True)
            relation = omega_sym**2 - g_sym * k_sym * sp.tanh(k_sym * h_sym)
            return {
                "relation": relation,
                "latex": sp.latex(relation)
            }
        
        # Solve for missing parameter
        if k is None and omega is not None and h is not None:
            # Solve: ω² = gk·tanh(kh)
            def equation(k):
                return omega**2 - g * k * np.tanh(k * h)
            
            # Use brentq for robust solution
            try:
                k = brentq(equation, 1e-6, 100)
                verification = g * k * np.tanh(k * h)
                error = abs(omega**2 - verification) / (omega**2 + 1e-10)
                return {
                    "k": k,
                    "omega": omega,
                    "h": h,
                    "verification_omega_squared": verification,
                    "relative_error": error,
                    "valid": error < 1e-10
                }
            except ValueError:
                return {"error": "No solution in valid range"}
        
        elif omega is None and k is not None and h is not None:
            # ω² = gk·tanh(kh)
            omega_squared = g * k * np.tanh(k * h)
            omega = np.sqrt(omega_squared)
            return {
                "k": k,
                "omega": omega,
                "h": h,
                "verification": g * k * np.tanh(k * h),
                "valid": True
            }
        
        elif h is None and k is not None and omega is not None:
            # Solve for h using fsolve
            def equation(h):
                return omega**2 - g * k * np.tanh(k * h)
            
            h_solution = fsolve(equation, g * omega**2 / (k**2) if k > 0 else 1)[0]
            if h_solution > 0:
                verification = g * k * np.tanh(k * h_solution)
                error = abs(omega**2 - verification) / (omega**2 + 1e-10)
                return {
                    "k": k,
                    "omega": omega,
                    "h": h_solution,
                    "verification": verification,
                    "valid": error < 1e-6
                }
            return {"error": "Invalid solution"}
        
        return {"error": "Must provide exactly two of: k, omega, h"}
    
    @staticmethod
    def wave_properties(T=None, L=None, H=None, h=None, g=9.81):
        """
        Calculate comprehensive wave properties.
        
        Args:
            T: Period (s)
            L: Wavelength (m)
            H: Wave height (m)
            h: Water depth (m)
            g: Gravitational acceleration (m/s²)
            
        Returns:
            dict with all wave parameters and relationships
        """
        result = {}
        
        # Calculate angular frequency and wave number
        if T is not None:
            omega = 2 * np.pi / T
            result["T"] = T
            result["omega"] = omega
            result["f"] = 1 / T
        else:
            return {"error": "Period T is required"}
        
        # Calculate wavelength using dispersion relation
        if L is None and h is not None:
            # Solve dispersion relation
            disp = SymbolicCoastalMath.dispersion_relation(
                omega=omega, h=h, g=g
            )
            if "error" in disp:
                return disp
            k = disp["k"]
            L = 2 * np.pi / k
            result["L"] = L
            result["k"] = k
        elif L is not None:
            k = 2 * np.pi / L
            result["L"] = L
            result["k"] = k
        else:
            return {"error": "Either L (wavelength) or h (depth) required"}
        
        # Wave properties
        result["c"] = L / T  # phase velocity
        result["cg_deep"] = result["c"] / 2  # group velocity (deep water)
        
        # Group velocity (general)
        if h is not None:
            k = result["k"]
            kh = k * h
            n = 0.5 * (1 + 2 * kh / np.sinh(2 * kh))
            result["n"] = n
            result["cg"] = n * result["c"]
            
            # Classification
            if kh > np.pi:
                result["regime"] = "Deep Water"
                result["kh"] = kh
            elif kh < np.pi / 10:
                result["regime"] = "Shallow Water"
                result["kh"] = kh
                result["cg"] = np.sqrt(g * h)
                result["c"] = result["cg"]
            else:
                result["regime"] = "Intermediate / Transitional"
                result["kh"] = kh
        
        # Wave energy
        if H is not None:
            result["H"] = H
            result["E"] = (1/8) * 1025 * g * H**2  # Energy per unit area (ρ=1025 kg/m³)
            result["E_per_m"] = result["E"] * L if L is not None else None
        
        return result
    
    @staticmethod
    def shoaling_refraction(k0=None, theta0=None, h_values=None, g=9.81):
        """
        Calculate wave shoaling and refraction.
        
        Args:
            k0: Initial wave number (deep water)
            theta0: Initial wave angle (degrees)
            h_values: Array of depth values
            g: Gravitational acceleration
            
        Returns:
            Shoaling coefficient and refracted waves
        """
        if k0 is None or h_values is None:
            return {"error": "k0 and h_values required"}
        
        results = []
        for h in np.atleast_1d(h_values):
            # Dispersion relation at depth h
            disp = SymbolicCoastalMath.dispersion_relation(omega=k0 * np.sqrt(g), h=h, g=g)
            if "error" in disp:
                continue
            
            k = disp["k"]
            L = 2 * np.pi / k
            L0 = 2 * np.pi / k0
            
            # Shoaling coefficient
            cg0 = g / (2 * k0)
            cg = g * k / np.tanh(k * h) * np.tanh(k * h) / (2 * k) if h > 0 else cg0 / 2
            Ks = np.sqrt(cg0 / cg)  # Shoaling coefficient
            
            results.append({
                "depth": h,
                "wavelength": L,
                "wave_number": k,
                "shoaling_coeff": Ks,
                "group_velocity": cg,
                "phase_velocity": k0 * np.sqrt(g) / k  # ω/k
            })
        
        return {"shoaling_profile": results}
    
    @staticmethod
    def radiation_stress(k=None, H=None, h=None, g=9.81):
        """
        Calculate radiation stress tensor components.
        
        Args:
            k: Wave number
            H: Wave height
            h: Water depth
            g: Gravitational acceleration
            
        Returns:
            Radiation stress components and setup
        """
        if any(x is None for x in [k, H, h]):
            return {"error": "k, H, and h required"}
        
        kh = k * h
        
        # Radiation stress components (normalized by ρg)
        E = (1/8) * H**2  # Energy per unit area (normalized)
        
        n = 0.5 * (1 + 2 * kh / np.sinh(2 * kh))
        
        # Radiation stress (x-direction, wave propagation)
        Rxx = E * (n * (2 * kh / np.sinh(2 * kh) + 0.5))
        
        # Radiation stress (y-direction, perpendicular)
        Ryy = E * (n - 0.5)
        
        # Wave setup
        setup = -3/8 * H**2 / h
        
        return {
            "Rxx": Rxx,
            "Ryy": Ryy,
            "energy": E,
            "wave_setup": setup,
            "setup_percent_of_depth": abs(setup) / h * 100 if h > 0 else 0
        }
    
    @staticmethod
    def dimensional_analysis(L_dim=None, T_dim=None, M_dim=None):
        """
        Dimensional analysis using Buckingham Pi theorem.
        Returns dimensionless groups for coastal quantities.
        """
        # Common dimensionless numbers in coastal engineering
        dimensionless = {
            "Froude": {"description": "u/√(gh)", "use": "River/channel flow"},
            "Reynolds": {"description": "ρuL/μ", "use": "Flow regime (laminar/turbulent)"},
            "Iribarren": {"description": "tan(β)/√(H/L)", "use": "Beach slope effect"},
            "Shields": {"description": "τ*/(ρ(ρs-ρ)gd)", "use": "Sediment motion"},
            "Strouhal": {"description": "fD/u", "use": "Cylinder wake"},
        }
        return dimensionless
    
    @staticmethod
    def verify_solution(computed, expected, tolerance=1e-6):
        """
        Verify numerical solution against expected value.
        
        Returns:
            dict with error metrics and verification status
        """
        if expected == 0:
            absolute_error = abs(computed - expected)
        else:
            absolute_error = abs(computed - expected)
            relative_error = absolute_error / abs(expected)
        
        return {
            "computed": computed,
            "expected": expected,
            "absolute_error": absolute_error,
            "relative_error": relative_error if expected != 0 else None,
            "verified": absolute_error < tolerance,
            "percent_error": (absolute_error / abs(expected) * 100) if expected != 0 else 0
        }


# Coastal Engineering Constants
COASTAL_CONSTANTS = {
    "g": 9.81,  # Gravitational acceleration (m/s²)
    "rho_water": 1025,  # Seawater density (kg/m³)
    "rho_air": 1.225,  # Air density (kg/m³)
    "nu_water": 1e-6,  # Kinematic viscosity of water (m²/s)
    "kinematic_viscosity": 1e-6,
    "dynamic_viscosity": 1.002e-3,  # Pa·s at 20°C
}


def format_with_uncertainty(value, uncertainty=None, significant_figures=4):
    """Format number with uncertainty."""
    if uncertainty is None:
        return f"{value:.{significant_figures}g}"
    
    # Round uncertainty to 1 significant figure
    exp = np.floor(np.log10(abs(uncertainty)))
    uncertainty_rounded = np.round(uncertainty / 10**exp) * 10**exp
    
    # Round value to same decimal place
    decimals = max(0, int(-exp))
    value_rounded = np.round(value, decimals)
    
    return f"{value_rounded:.{decimals}f} ± {uncertainty_rounded:.{decimals}f}"
