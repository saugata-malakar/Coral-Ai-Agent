# Coastal Hydrodynamics II

#### Course : CE60222

### Dr. Mohammad Saud Afzal

#### Associate professor
 Civil Engineering Department


-----

## Content



###  Wave Skewness And Asymmetry

  Wave Orbital Velocity

  Dynamic Pressure

  Wave Boundary Layer

  Bed Shear Stress


-----

## Wave skewness and Asymmetry


##### Skewness:

  Gradual peaking of the wave crest and a flattening of the trough. This asymmetry relative to the horizontal

 axis is called skewness.

 Asymmetry:

  Relative steepening of the face until breaking occurs, resulting in a pitched-forward wave shape. This

 asymmetry relative to the vertical axis is often simply called asymmetry.


-----

#####  Waves propagating towards the shore become more and more asymmetric, until the point of wave-breaking.

 These non-linear effects cannot be described by linear theory.

  Numerous non-linear theories (Stokes theory, cnoidal wave theory, Boussinesq equations) have been developed

 to take into account these complicated non-linear processes.

  The non-linear effects are crucial in determining the magnitude of the wave-induced transport. In the following

 we will therefore subsequently consider skewness and asymmetry.

  This asymmetric profile (relative to the horizontal axis) can only be described by a sum of sinusoidal waves

 with higher harmonics (frequencies that are a multiple of the basis frequency: cos𝑆, cos 2𝑆 etc. with 𝑆= 𝜔𝑡−

 𝑘𝑥 )

  The second-order equation for the surface elevation can be written as:

 𝜼= ෝ𝜼𝟏𝒄𝒐𝒔(𝝎𝒕−𝒌𝒙) + ෝ𝜼𝟐𝒄𝒐𝒔𝟐(𝝎𝒕−𝒌𝒙)


-----

#####  The amplitude of the second-order correction is small compared to the first-order component.

  It can be seen that the resulting Stokes wave profile 𝜂1 + 𝜂2has crests which are narrower and more peaked

 than those of a cosine profile and troughs that are wider and fatter; the profile is skewed.

  The second term 𝜂2 represents the Stokes second-order wave travelling at the same speed as the first-order
 wave 𝜂1 (hence, it does not obey the linear dispersion relation).


-----

#####  The pitched-forward wave shape is the result of the fact that in shallow water the wave crest moves faster than

 the wave trough.

  The propagation speed of non-linear shallow-water waves

 𝒄= 𝒈(𝒉+ 𝜼)

  For small-amplitude shallow-water waves this reduces to 𝒄= 𝒈𝒉

  The wave crest of a harmonic wave with amplitude 𝑎 has a higher propagation velocity 𝑐𝑐𝑟𝑒𝑠𝑡 =

 𝑔(ℎ+ 𝑎) than the trough which propagates with 𝑐𝑡𝑟𝑜𝑢𝑔ℎ = 𝑔(ℎ−𝑎).


-----

#####  Closer to the surf zone, phase-shifting of the harmonic(s) leads to an increase in wave asymmetry and –

 eventually – to a decrease in wave skewness as well.

  Ultimately the pitching forward results in wave-breaking.


-----

#####  The right panel of Figure shows a time series of a pitched-forward (sawtooth-like) wave at one location, namely

 location A (x/L = 0 ) in the left panel of Figure.

  The left panel of Figure shows a rapidly rising and slowly falling surface elevation.

  The sawtooth-like wave of Figure, the phase shift between the first and the second harmonic is such that the

 asymmetry is maximum and the skewness is zero.

  The sawtooth-likewave of Figure can also be depicted as a function of 𝑆= 𝜔𝑡−𝑘𝑥 .


-----

## Wave orbital velocity



#####  Wave orbital velocity refers to the movement of water particles beneath the surface of a wave as it

 propagates through the ocean.

  As a wave travels, the water particles do not move in a straight line. Instead, they follow a circular or

 elliptical path. This motion is called "orbital" because the particles move in orbits.


-----

#####  In deep water, the orbits of the water particles are nearly circular. At a depth of about half a wavelength, the

 circular motion is reduced to about 4% of the surface value.

  In shallow water, the orbits become elliptical. The water particles still move up and down, but the motion is

 less circular and more flattened as they approach the seabed. At the bottom, the vertical movement is zero.


-----

#####  Understanding wave orbital velocity is crucial for coastal engineering, sediment transport studies, and

 predicting how waves interact with the shoreline.

  The horizontal velocity of the water particles varies with depth and is influenced by the wave's characteristics,

 such as its amplitude and wavelength.

  The velocity can be described mathematically, showing how it changes with depth.

  Now consider waves of infinitesimal amplitudes. According to linear theory, the horizontal orbital velocity

 varies harmonically with an amplitude ො𝑢 equal to:


##### ෝ𝒖(𝒛) = 𝝎𝒂 [𝒄𝒐𝒔𝒉𝒌(𝒉+𝒛)]

###### 𝒔𝒊𝒏𝒉𝒌𝒉


##### where:   𝜔 = angular frequency (2𝜋/𝑇 ) rad/s

 𝑎 = wave amplitude m

 𝑘 = wavenumber (2𝜋/𝐿) rad/m

 𝐿 l th


-----

#####  The 𝑧-axis is defined positive upward with 𝑧 = 0 at the surface and 𝑧= −ℎ at the bottom.

  The velocity 𝑢 is in the wave propagation direction. Using the cosh𝑘ℎ and sinh𝑘ℎ approximations for shallow and

 deep water, the horizontal velocity profiles can be drawn schematically as in Figure.

  In shallow water (𝑘ℎ ≪ 1; in practice 𝑘ℎ< 𝜋/10 or ℎ/𝐿 > 1/20), the depth-uniform velocity amplitude is given by :
 ෝ𝐮= [𝛚𝐚] 𝐠𝐡 [𝐇]
 𝐤𝐡 [= 𝐜𝐚]𝐡 [=] 𝟐𝐡


-----

#####  The particle excursions (i.e. the horizontal and vertical displacements of the particles) are the time integrals

 of the oscillatory horizontal and vertical flow velocities respectively.

  This means that the amplitude of the horizontal particle excursion is given by:


##### ෠𝝃= [ෝ𝒖]
 𝝎


-----

## y



#####  Pressure gradients in coastal waters are mainly due to mean water level variations (hydrostatic

 pressure) and fluctuations of pressure due to waves.

  The hydrostatic pressure due to mean water level variation is 𝑝0 = −𝜌𝑔𝑧 and hence linearly

 increases from zero at the water surface 𝑧 = 0 to 𝑝0 = 𝜌𝑔ℎ at the bottom 𝑧 = −ℎ.

  In the case of waves, the total pressure is the sum of this hydrostatic pressure 𝑝0 (from 𝑧 = −ℎ to

 𝑧 = 𝜂) plus the wave-induced or dynamic pressure 𝑝wave from (from 𝑧 = −ℎto 𝑧 = 𝜂).


-----

#####  Wave-induced pressure oscillations are different under wave crest and wave trough and – in

 intermediate and deep water – reduce with depth below the free surface.

  According to linear theory, the wave-induced pressure varies harmonically (in phase with the surface

 elevation η) with amplitude:


###### 𝒄𝒐𝒔𝒉𝒌(𝒉+𝒛)

 𝒄𝒐𝒔𝒉𝒌𝒉


#### ෝ𝒑=


###### 𝝆𝒈𝑯

 𝟐


-----

#####  wave-induced pressure which reduces in shallow water to:

 ෝ𝒑= [𝝆𝒈𝑯]
 𝟐

  Hence, in shallow water the hydrostatic dynamic pressure varies linearly with the free surface elevation.

 𝑝wave = ෥𝒑= 𝜌𝑔𝜂

  The tilde indicates the purely oscillatory character.

  To derive wave-induced pressure the amplitude was assumed to be very small in order to linearize the free

 surface boundary condition.

  It is therefore not valid in the region between the trough and the crest elevation.

  We can, however, assume that the dynamic pressure is hydrostatic between wave trough and wave crest:

 ෥𝒑= 𝜌𝑔𝜂


-----

## y y



#####  Most wave theories are valid from the water level to a small

 distance from the bed, where the flow still is unaffected by the

 boundary.

  Closer to the bed, in a thin layer called the wave boundary

 layer(δ).

  vorticity (rotation) can be generated, which is not included in

 linear wave theory or in most other (irrotational) wave theories

 for that matter.

  The distance denoted as δ in Figure is the thickness of the wave

 boundary layer, the transition layer between the bed and the

 layer of ‘normal’ oscillating flow.


-----

#####  The thickness is generally between 1 cm and 10 cm for short-period waves

 (T < 10 s).

  The reason for this small thickness is that there is not sufficient time for the

 layer to grow out in the vertical direction, because the current regularly

 reverses.

  It is typical for oscillating boundary layers that the maximum flow velocity

 near the bed is somewhat larger than the so-called free stream velocity.

  The free-stream velocity amplitude ෝ𝒖𝟎 according to linear theory for

 𝑧= −ℎ


#### ෝ𝒖 =
###### 𝟎


###### 𝝎𝒂
 𝒔𝒊𝒏𝒉𝒌𝒉


-----

#####  The flow in the wave boundary layer is generally turbulent due to the presence of roughness elements on the

 bed.

  The water moving along the bed incurs a shear stress on the bed.

  This becomes clear when imagining that – as a result of viscosity and turbulence – the flow sticks to the wall

 (no-slip condition).

  Hence, the orbital velocity increases from zero at the bed to the undisturbed free-stream velocity at the top of

 the wave boundary layer 𝑧= 𝛿.

  Because of the thin boundary layer, the velocity gradients perpendicular to the bed are large and give rise to

 large stresses in the wave boundary layer.

  The friction in the wave boundary layer results in dissipation of wave energy.


-----

#####  In coastal waters, turbulent stresses – arising from turbulent fluctuations of the velocity are much larger

 than viscous stresses arising from small-scale erratic movements of molecules.

  Now think of the total horizontal velocity u and vertical velocity w to be composed of a mean, a wave and a

 turbulent part, hence


##### 𝑢 = 𝑈 + ෤𝑢+ 𝑢′

 𝑤 = 𝑊 + ෥𝒘 + 𝑤′



#####  Turbulent shear stress is defined as the stress introduced when averaging over the turbulent motion:

 𝝉(𝒛) = 𝝆𝒖[′]𝒘[′]


-----

##### For practical purposes, the following aspects of the wave boundary layer is to be consider:

  The water moving along the bed incurs a shear stress on the bed.

  The orbital motion under waves, even without the presence of a uniform current, gives a time-varying shear

 stress at the bed, which can set sediment grains into motion.

  Due to bed friction, the wave boundary layer dissipates energy from the flow above .

  The wave-induced streaming should be taken into account for net sediment transport computations.


-----

## ed s ea st ess



#####  Bed shear stress (τ) is the stress exerted by the water flow on the bed of a water body, which can vary due to

 the presence of waves and currents.

  It is crucial for understanding sediment transport.

  If we refrain from turbulence modelling, (bed) friction is a major unknown that has to be determined using

 (empirical) friction laws.

  This introduces coefficients that need to be calibrated, which makes the calibration of these models important.

  To determine the bed shear stress, Jonsson (1967) introduced the concept of a wave friction factor in

 analogy with the current friction factor.


-----

#####  The current friction factor relates the bed shear stress to the depth-averaged current velocity, whereas the

 wave friction factor relates the bed shear stress to the free stream velocity.

  For a current only, the magnitude of the bed shear stress is 𝜏𝑐 = 𝑐𝑓𝜌𝑈[2]

  The friction factor 𝑐𝑓 is a dimensionless coefficient relating the bed shear stress to the square of the velocity.

  𝑐𝑓 can be expected to depend on the bed material and bed forms (bed roughness)

  For uniform flow in a canal driven by a small slope of the mean water surface, Chezy’s derived theoretically

 a Chezy’s coefficient


##### where


##### 𝑪= 𝟏𝟖𝐥𝐨𝐠𝟏𝟐 [𝒉]

###### 𝒓[, ]

##### 𝑟 is the bottom roughness and ℎ is the water depth.


-----

#####  The Chezy’s coefficient 𝐶 relates to 𝑐𝑓 as follows:


##### 𝒄𝒇 = [𝒈]
 𝑪[𝟐]

  Under waves, the bed shear stress varies in time and reverses with the direction of the orbital velocities.

  For linear waves with a free stream velocity


##### 𝑢= ෞ𝒖𝟎 cos 𝜔𝑡



#####  Jonsson defined the friction factor 𝑓𝑤 through the following formula for the magnitude of the maximum bed

 shear stress:

###### 𝟐

##### ො𝝉𝒘 = 𝟎. 𝟓𝝆𝒇𝒘ෝ𝒖𝟎


-----

#####  For a rough bed and turbulent flow, it is not easy to determine the friction coefficient as it cannot be

 measured directly.

  The friction coefficient will generally depend on the bed material and the bed forms (e.g. ripples).

  The following variables can be found in expressions for 𝑓𝑤 for rough turbulent flow.

  the bed roughness 𝑘𝑠 (Nikuradse roughness) or 𝑟 of the wall; the bed roughness represents the size of the

 roughness elements, for instance the grains.

  the particle excursion amplitude close to the bed 𝜉[෡]𝟎 = ෞ𝒖𝟎 /𝜔 .


-----

##### ▪ Let us consider two cases in which ෞ𝒖𝟎is the same, but 𝑇 differs.

 ▪ For the case with a large value for 𝑇, the value of 𝜉0̂ is larger than in the case with the lower value for 𝑇 .

 ▪ Assuming an equal value for r, this means that the case with the larger value for the wave period gives lower

 values for the wave friction factor.

 ▪ This can be understood by considering that the boundary layer thickness varies with time.

 ▪ In case of a larger wave period, more time is available to develop the boundary layer, which therefore

 reaches a larger maximum thickness.

 ▪ Consequently, the velocity gradients in the boundary layer are smaller, leading to a smaller maximum

 shear stress and friction factor.


-----

#####  A frequently applied formula for 𝑓𝑤 is that of Jonsson (1967), rewritten by Swart (1974) into:

###### −𝟎.𝟏𝟗𝟒

##### 𝒇𝒘 = 𝒆𝒙𝒑−𝟓. 𝟗𝟕𝟕+ 𝟓. 𝟐𝟏𝟑 ෠𝝃𝟎

###### 𝒓

 ෠

##### 𝒇𝒘 = 𝟎. 𝟑𝟎 for 𝝃𝟎 < 𝟏. 𝟓𝟗

###### 𝒓

#####  Many simpler formulas exist, such as (Soulsby, 1994):

###### −𝟎.𝟓𝟐
 ෠

##### 𝒇𝒘 = 𝟏. 𝟑𝟗 𝝃𝟎

###### 𝒓/𝟑𝟎

##### 𝒇𝒘,𝒎𝒂𝒙 = 𝟎. 𝟑

  For the roughness value 𝑟 the so-called Nikuradse roughness 𝑘𝑠 is often used, which is normally set as a

 function of the grain size.


-----

#####  As expected, the friction factor 𝑓𝑤 increases if 𝜉[෡]𝟎 /𝑟 decreases.

  The upper limit of 𝑓𝑤 has been questioned by various researchers:

 some suggest that there is no upper limit and that the friction factor
 remains proportional to 𝜉[෡]𝟎 /𝑟.

  In case of irregular waves, the near-bed orbital velocity amplitude in

 the above formulas should be based on the root-mean-square wave

 height and the wave orbital excursion parameter near the bed on the

 root-mean-square wave height and peak period.


-----

## ob e


##### Find the maximum shear stress near the bed under waves only from the linear wave theory for given parameters.

 (Water depth d = 3 m, Roughness height 𝑟 = 0.06 m, Wave height 𝐻 = 1.18 m, Wave period 𝑇 = 8 s)

 Solution : The amplitude of the velocity near the bed can be found from linear wave theory:


###### ො𝑢0 = [𝜔𝐻]
 2


###### 1
 sinh𝑘𝑑 [and][ መ][𝜉][0][ =][ ො𝑢]2𝜋[0][𝑇]


###### 𝐿𝑜 = 1.56𝑇[2] = 1.56 × 8[2] = 99.84 m

 𝑑 3
 𝐿0 [= ]99.84 [= 0.03     ]


###### 𝑑
 𝐿 [= 0.0713 (from wave table)]

 3 or, L = 42.08 m 𝐿 [=][ 0.0713]


###### 𝜔= [2𝜋]

𝑇 [=][ 2𝜋]8 [= 0.7]

2𝜋 2𝜋


-----

##### ො𝑢0 = [𝜔𝐻]
 2


##### 1 1
 ×
 sinh𝑘𝑑 [= 0.786 × 1.118]2 sinh(0.149 × 3) [= 1.003𝑚/𝑠]

 መ𝜉0 = [ො𝑢][0][𝑇] = 1.27𝑚
 2𝜋 [= 1.003 × 8]2𝜋


##### For a value of 𝜉[መ]0 /𝑟 > 1.59 the friction factor equals:

 𝑓𝑤 = exp −5.977 + 5.213 𝜉[መ]0/𝑟

 The maximum bottom shear stress follows from:


###### −0.194
##### = 0.045


###### 2 2

##### Ƹ𝜏𝑤 = [1] = 22.5N/m

###### 2 [𝜌𝑓][𝑤][ො𝑢][0]

##### Hence, for a maximum near-bed orbital velocity of 1 m/s, the bottom shear stress due to waves equals 22.5 N/m[2].


-----

##### Now consider the situation of a mean current of 1 m/s.

 Assume that the roughness height and water depth are the same as above.

 Using 𝐶 = 18 log 12d/𝑟 = 50 m[1/2]/s

 we find:

 𝜏𝑐 = 𝜌 [𝑔]

###### 𝐶[2][ 𝑈][2][ = 3.9N/m][2]


-----

