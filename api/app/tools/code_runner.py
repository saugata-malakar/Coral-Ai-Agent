"""
run_python tool: executes code using exec() with pre-loaded modules.
This is MUCH faster than subprocess since imports are cached in memory.
Plots are saved to PLOTS_DIR with a uuid filename and the path is returned.
"""
import io
import os
import sys
import traceback
import uuid
from contextlib import redirect_stdout, redirect_stderr

from langchain_core.tools import tool

from ..config import PLOTS_DIR

# Pre-import heavy modules ONCE at server startup (not per-request)
import numpy as np
from scipy.optimize import brentq, fsolve, minimize_scalar, odeint
from scipy.integrate import quad, simpson
from scipy.interpolate import interp1d
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import sympy as sp
from sympy import symbols, cos, sin, sqrt, pi, sinh, cosh, tanh, diff, solve

# Import advanced math module
from .advanced_math import (
    SymbolicCoastalMath,
    COASTAL_CONSTANTS,
    format_with_uncertainty
)

# Pre-built namespace with all imports ready
_BASE_NAMESPACE = {
    "np": np,
    "numpy": np,
    "brentq": brentq,
    "fsolve": fsolve,
    "minimize_scalar": minimize_scalar,
    "odeint": odeint,
    "quad": quad,
    "simpson": simpson,
    "interp1d": interp1d,
    "plt": plt,
    "matplotlib": matplotlib,
    "sp": sp,
    "symbols": symbols,
    "cos": cos,
    "sin": sin,
    "sqrt": sqrt,
    "pi": pi,
    "sinh": sinh,
    "cosh": cosh,
    "tanh": tanh,
    "diff": diff,
    "solve": solve,
    "SymbolicCoastalMath": SymbolicCoastalMath,
    "format_with_uncertainty": format_with_uncertainty,
    "COASTAL_CONSTANTS": COASTAL_CONSTANTS,
    "__builtins__": __builtins__,
}


def run_code(code: str, plot_path: str | None = None) -> dict:
    """
    Execute code using exec() with captured output.
    Includes advanced mathematical capabilities.
    
    Returns: {"stdout": str, "stderr": str, "plot_path": str | None}
    """
    if plot_path is None:
        plot_path = str(PLOTS_DIR / f"{uuid.uuid4().hex}.png")

    # Fresh namespace with pre-loaded imports + plot path
    namespace = _BASE_NAMESPACE.copy()
    namespace["_PLOT_PATH"] = plot_path

    stdout_capture = io.StringIO()
    stderr_capture = io.StringIO()

    try:
        with redirect_stdout(stdout_capture), redirect_stderr(stderr_capture):
            exec(code, namespace)
        
        stdout = stdout_capture.getvalue()[:5000]
        stderr = stderr_capture.getvalue()[:1000]
    except Exception:
        stdout = stdout_capture.getvalue()[:5000]
        stderr = traceback.format_exc()[:1500]

    # Clear any matplotlib figures to prevent memory leaks
    plt.close("all")

    found_plot = plot_path if os.path.exists(plot_path) else None
    return {"stdout": stdout, "stderr": stderr, "plot_path": found_plot}


def _wrap_error_with_suggestion(stderr: str) -> str:
    """Provide helpful error messages for common calculation issues."""
    suggestions = {
        "division by zero": "Check for zero denominators in your equations",
        "invalid value": "Check for NaN or infinity in calculations",
        "singular matrix": "Linear system is singular; check your equations",
        "no solution": "The numerical solver couldn't find a solution in the given range",
    }
    
    for error_type, suggestion in suggestions.items():
        if error_type in stderr.lower():
            return f"{stderr}\n\n💡 Suggestion: {suggestion}"
    
    return stderr


@tool
def run_python(code: str) -> str:
    """Execute Python code for numerical calculations or plots.

    ✓ Pre-imported modules:
      - numpy (np), scipy.optimize (brentq, fsolve, etc.)
      - matplotlib.pyplot (plt)
      - sympy (sp) for symbolic math
      - SymbolicCoastalMath for advanced coastal calculations
      - COASTAL_CONSTANTS (g, rho_water, etc.)

    ✓ Available tools:
      - SymbolicCoastalMath.dispersion_relation(k, omega, h, g, symbolic)
      - SymbolicCoastalMath.wave_properties(T, L, H, h, g)
      - SymbolicCoastalMath.shoaling_refraction(k0, theta0, h_values, g)
      - SymbolicCoastalMath.radiation_stress(k, H, h, g)
      - format_with_uncertainty(value, uncertainty, sig_figs)

    ✓ For plots: plt.savefig(_PLOT_PATH, dpi=150, bbox_inches='tight')
      Do NOT call plt.show(). _PLOT_PATH is pre-set.

    ⚠️ RULES:
    1. ALWAYS compute numerical results; NEVER compute by hand
    2. Use appropriate numerical methods (brentq for root-finding)
    3. Check solution validity and report verification status
    4. Include dimensional analysis where appropriate
    5. Format output with units and uncertainty
    6. Verify results against known solutions when possible"""
    
    r = run_code(code)
    out = r["stdout"]
    if r["stderr"]:
        out += "\nSTDERR:\n" + r["stderr"]
    if r["plot_path"]:
        out += f"\nPLOT_SAVED:{r['plot_path']}"
    return out if out.strip() else "(no output)"
