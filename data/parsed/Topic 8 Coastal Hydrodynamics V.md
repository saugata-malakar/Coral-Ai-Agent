# Coastal Hydrodynamics V

###### Course : CE60222

#### Dr. Mohammad Saud Afzal

###### Associate professor
 Civil Engineering Department


-----

## Contents



######  Alongshore balance: longshore current

#####  Alongshore momentum balance (straight, parallel depth contours)

  Wave force in alongshore uniform situation

  Analytical model for alongshore wave force in the surf zone

  Quadratic friction law for bed shear stress

  Analytical model for longshore current (no lateral dispersion)

  Turbulent forces redistributing momentum


-----

## Contents



######  Roller Momentum

  Irregular Waves

  3D effects

  Eddy formation in the shadow zone of structures

  Rip currentsdue to convergence or divergence of wave energy

  Wave-induced currentsaround shoals (and submerged breakwaters)

  Wind-inducedset-up and currents


-----

### Alongshore balance: longshore current



######  In the alongshore direction, the transfer of momentum from the wave motion to the mean flow

 gives rise to a longshore current.

  The longshore current (velocity magnitude and cross-shore distribution) is an important input

 parameter in longshore sediment transport computations.


-----

### Alongshore momentum balance (straight, parallel depth contours)



######  In a 2D scenario with long-crested waves obliquely incident to an alongshore uniform coast, the

 cross-shore variation of the radiationstress shear component 𝑺𝒚𝒙 drives a longshorecurrent.

  In the cross-shoredirection, this force is balanced by a hydraulicpressure gradient.

  Along an infinitely long coastline, no alongshore pressure gradient can form, so the balancing

 force is provided by bed shear stresses,which arise only when a longshore current is generated.

  These shear stresses restrain the current, while in the cross-shore direction, bed shear stress is

 negligible compared to the pressure force.


-----

######  The alongshore component of the momentum balance for a steady state and alongshore

 uniformity can be written as:


###### 𝑭 = − 𝒚


###### 𝒅𝑺 𝒚𝒙
 𝒅𝒙 [= ത𝝉][𝒃,𝒚]



######  The balance between the drivingforce and the resistingor retardingforce is shown in Figure.


-----

### Wave force in alongshore uniform situation



######  Let us first assess 𝑭 = − 𝒚

 where,


###### 𝒅𝑺𝒚𝒙
 in deeper water, i.e. outside the breakerzone. 𝒅𝒙


###### 𝑆𝑦𝑥 = 𝐸𝑛 sin 𝜑 cos 𝜑

 and 𝜑 = the wave angle changes as a function of 𝑥, but does not vary with 𝑦.

  The latter leads to Snell’s law for regular waves :

 sin 𝜑/𝑐 = constant

  Conservation of energy requires under the present assumptions.

 𝒅
 𝒅𝒙 [𝑬𝒄][𝒈] [𝒄𝒐𝒔𝜑= −𝑫][𝒘]


-----

######  For linear waves we can now write the wave force as:


###### 𝒅
 𝒅𝒙 [𝑬𝒄][𝒈][𝒄𝒐𝒔𝝋=][ 𝑫]𝒄[𝒘]
 𝟎


###### 𝑭 = − 𝒚


###### 𝒅𝑺 𝒚𝒙
 𝒅𝒙 [= −] [𝒔𝒊𝒏𝝋]𝒄


###### 𝒔𝒊𝒏𝝋 𝟎



######  Apparentlythe alongshore drivingforce is a function of the dissipation of the wave energy.

  Outside the surf zone, the dissipation of wave energy can be neglected and hence the energy

 flux is constant.

 𝑬𝒄𝒈 = (𝑬𝒄𝒈 cos 𝜑, 𝑬𝒄𝒈 sin 𝜑) = Constant

  In the absence of dissipation:

 𝑆𝑦𝑥 is constant

 𝐹 = 0


-----

######  So, although outside the surf zone the wave conditions change with 𝑥 (wave height due to

 shoaling; wave direction due to refraction), the radiationshear stress is constant.

  Therefore, since the alongshore forcing is only present when the waves are breaking, the

 longshore current is confined to the surf zone.


-----

### Analytical model for alongshore wave force in the surf zone



######  To simplify the alongshore wave force, a basic model for wave breaking is used, where

 wave height H is proportionalto water depth h in the surf zone.

 𝐻 = 𝛾ℎ

  An alternative would be solving the energy balance numerically. Snell’s law and the simple

 dissipation model result in:


###### 𝑭 = − [𝒔𝒊𝒏𝝋] 𝒚
 𝒄


###### 𝒅
 𝒅𝒙 [𝑬𝒄][𝒈][𝒄𝒐𝒔𝝋]


###### 𝑭 = − [𝒔𝒊𝒏𝝋][𝟎] 𝒚
 𝒄 𝟎


###### 𝒅
 𝒅𝒙 [𝟏/𝟖𝝆𝒈𝜸][𝟐][𝒉][𝟐][𝒄][𝒈][𝒄𝒐𝒔𝝋]


-----

######  In shallow water 𝑐𝑔 = 𝑐 = √𝑔ℎ and since, due to refraction, 𝜑 is small (generally around 10° to

 15°), we assume cos 𝜑 ≈1. We now have:
 𝑭 ≈− [𝒔𝒊𝒏𝝋][𝟎] 𝟏/𝟖𝝆𝒈[𝟑/𝟐]𝜸[𝟐] [𝒅] 𝒚
 𝒄 𝒅𝒙 [𝒉][𝟓/𝟐] 𝟎
 𝒔𝒊𝒏𝝋 𝟎
 𝑭 = − [𝟓] 𝝆(𝒈𝒉)[𝟑/𝟐]𝜸[𝟐] [𝒅𝒉] 𝒚
 𝟏𝟔 𝒄 𝒅𝒙
 𝟎



######  The radiation shear stress 𝑆𝑦𝑥 is constant seaward of the border of the breaker zone (thus the

 wave force is zero). It decreases inside the breaker zone to zero at the waterline.


-----

######  Radiation shear stress 𝑺𝒚𝒙 for 𝑯𝟎= 2m, 𝑇 = 7s, 𝝋𝟎= 30°, constant bottom slope 1:100 and a

 breakerindex 𝛾 = 0.8.

  For many day to day wave conditions, this gradient in 𝑺𝒚𝒙 causes alongshore stresses (forces)

 which are in the same order of magnitude as the bottom shear stress in rivers: in the order of

 1𝑵/𝒎[𝟐] to 𝟏𝟎𝑵/𝒎[𝟐].

  The cross-shore gradient in the alongshore radiation stress 𝑺 is therefore an important


-----

### Quadratic friction law for bed shear stress



######  To determining the alongshorecurrent, we need to calculate the bed shearstress.

  Turbulence from currents spreads through the whole water, while wave turbulence stays near the

 seabed and makes the bed shear stress much stronger.

  This happensbecause waves move faster and create more friction.

  To describe the longshore current's vertical profile, we use a quadratic law that combines the

 effects of both currents and waves.


-----

###### Quadraticfriction law for bed shear stress is non trivialsince:

  The quadratic friction law makes the combined effect of waves and currents non-linear, often

 resulting in a total shear stress greater than the sum of their individual stresses.

  Waves and currents can move in different directions, with waves approaching at an angle and

 currentsflowing along the coast, causing the bed-shear stress to vary based on their angle.

  Currents create turbulence throughout the water, while waves only affect the wave boundary

 layer, raising the question of which velocity to use for combined motion.

  Most models focus on time-averaged bed shear stress, ignoring short-term changes within a wave

 cycle. However, these intra-wave changes can impact sedimenttransport.

  Different models describe bed shear stress in various ways—some focus on time-averaged

 stress, others on instantaneous stress.


-----

###### For the determination of the time-averaged bed shear stress in the alongshore direction,

 necessaryto compute the longshorecurrent, we take a fairlysimple approach:

  The wave motion is described by shallow-water theory (constant orbital amplitude outside the

 wave boundarylayer);

  The angle of incidence is very small, such that for the wave motion

 (𝑢, 𝑢 ) = (ො𝑢cos𝜔𝑡, 0) 𝑥 𝑦

  The bed friction vector is related to the depth-averaged velocity vector. The latter is the sum of

 the depth-averaged longshore current velocity and the wave orbital motion:

 𝑢 = (ො𝑢cos𝜔𝑡, V)


-----

######  The time-varyingbed friction is written as:

 𝝉 = 𝝆𝒄 |𝒖|𝒖 𝒃 𝒇

  The enhancement of the friction factor (compared to a current-only situation) due to the

 small height of the wave boundary layer as compared to the current boundary layer is

 not further specified.


-----

######  In the cross-shoredirection, thetime-averaged (not the instantaneous)bed shear stress is zero.

  With the above approximations, the time-averaged bed shear stress in the alongshore direction

 reads:

 ത𝝉 = 𝝆𝒄 |𝒖|𝑽= 𝝆𝒄 𝑽[𝟐] + ෝ𝒖[𝟐]𝒄𝒐𝒔[𝟐] 𝝎𝒕𝑽 𝒃,𝒚 𝒇 𝒇

  If we further assume that 𝑉≪ො𝑢, this can be simplified to:


###### ത𝝉 = [𝟐] 𝒃,𝒚
 𝝅 [𝝆𝒄][𝒇][ෝ𝒖𝑽]



######  With ො𝑢 in shallow water and with a constant ratio of wave height over water depth across the

 entire surf zone we find:

 ത𝝉 = [𝟏] 𝒃,𝒚
 𝝅 [𝝆𝒄][𝒇] [𝒈𝒉𝑯]𝒉 [𝑽]


-----

### Analytical model for longshore current (no lateral dispersion)



######  For steady conditions, the alongshore velocity follows from the balance between the driving force

 and the resisting friction force.


###### 𝑭 = − 𝒚


###### 𝒅𝑺 𝒚𝒙
 𝒅𝒙 [= ത𝝉][𝒃,𝒚]



######  This yields with Equations


###### ത𝝉 = [𝟏] 𝒃,𝒚
 𝝅 [𝝆𝒄][𝒇] [𝒈𝒉𝑯]𝒉 [𝑽]

 Now, 𝑫𝒘
 𝒄𝟎 [𝐬𝐢𝐧𝝋][𝟎] [=][ 𝟏]𝝅 [𝝆𝒄][𝒇] [𝒈𝒉] [𝑯]𝒉 [𝑽]


###### 𝝅 𝑽(𝒙) =
 𝒄 𝝆𝒈 𝒇


###### 𝒔𝒊𝒏𝝋 𝟎
 𝒄 𝟎


###### 𝑫 (𝒙) 𝒘
 𝒉(𝒙) 𝑯(𝒙)


-----

######  The magnitude of the depth-averaged longshore current velocity varies in the surf zone as a

 function of the dissipation, wave height and water depth.

  The dissipation and wave heights can be modelled using a wave model (with roller model).

  In our simple dissipation model

 𝛾 = 𝐻 /ℎ= constant

  we can write the force balance as:


###### 𝟏𝟔


###### 𝒄 𝟎

 𝑽(𝒙) = − [𝟓]
 𝟏𝟔 [𝝅𝜸]𝒄
 𝒇


###### 𝒈 [𝒔𝒊𝒏𝝋][𝟎]
 𝒄 𝟎



###### [𝒅𝒉]
 𝒅𝒙 [= 𝟏]𝝅 [𝝆𝒄][𝒇] [𝒈𝒉𝜸𝑽]


###### which leads to:


###### 𝒉 [𝒅𝒉]
 𝒅𝒙


-----

######  For a constant beach slope tan 𝛼 = −𝑑ℎ0/𝑑𝑥 and for 𝑑ℎ/𝑑𝑥 ≈ 𝑑ℎ0/𝑑𝑥, the current velocity

 is proportional to the depth with a maximum at the breaker line (where ℎ= ℎ ): 𝑏


###### 𝑽(𝒙) = [𝟓]
 𝟏𝟔 [𝝅𝑯]𝒄 [𝒃]
 𝒇

  A longshore current profile according
 to above equation is shown in Figure.

  Alongshore velocity distribution
 (regular wave field, 𝐻0 = 2 m, 𝑇 = 7 s, 𝜑0 = 30°, bottom slope 1:100, 𝛾 = 0.8, roughness height 𝑟 = 0.06 m).


###### 𝒈 [𝒔𝒊𝒏𝝋][𝟎]
 𝒄 𝟎


###### 𝒉
 𝒉 𝒃


###### 𝒕𝒂𝒏𝜶


-----

######  Larger wave heights at breaking (𝑯𝒃) increase the maximum longshore current velocity and

 widen the littoralzone, leading to greater water discharge in the surf zone.

  The beach slope (tanα) also affects the current velocity V(x): steeper slopes increase velocities

 but narrow the surf zone, keeping the total discharge roughly constant.

  For small wave angles, the longshore current velocity at a given depth becomes a linear

 function of the wave angle 𝜑0 .


-----

### Turbulent forces redistributing momentum



######  Turbulence plays a significant role in fluid dynamics by smoothing out velocity gradients through

 lateral dispersionof momentum.

  When modeling turbulence, the total velocity is often divided into mean, wave, and turbulent

 components.

  Turbulent shear stress arises from averaging over turbulent motions and is modeled using an eddy

 viscosity(𝜈𝑇 ​), which is analogous to molecularviscosity(ν) but representsturbulentfriction.

 • Molecular Viscosity (ν): Measures the fluid's resistance to flow due to internal friction.

 • Eddy Viscosity (𝜈𝑇): Represents turbulent friction and is much larger than ν in coastal waters

 (𝜈𝑇 ≫𝜈).


-----

######  The eddy viscosity depends on:

  Characteristic Velocity: Often related to wave orbital motion in coastal zones.

  Characteristic Length Scale:

 • For vertical mixing, it is the water depth.

 • For horizontal mixing, it is not limited by depth, so horizontal eddy viscosity (𝜈𝑇, H) is

 typically much larger than vertical eddy viscosity (𝜈𝑇,V​).

  The shear componentof the radiation stress 𝑆 was defined through: 𝑦𝑥

 𝜼


###### 𝑺 = න 𝒚𝒙
 −𝒉𝟎


###### 𝝆𝒖 𝒖 𝒅𝒛 𝒚 𝒙


###### where the velocity componentsare due to the orbital motion.


-----

######  In analogy with above equation,we can write for the turbulent force:


###### 𝜼
 ′ 𝑺 = න 𝒚𝒙
 −𝒌𝟎


###### 𝝆𝒖 𝒖 𝒅𝒛 𝒚[′] 𝒙[′]


###### where the overbar now representsaveraging over the turbulentmotion (indicated with primes).

  This shear stress or friction force per unit surface area, acts on a surface parallel to the coast. It can be

 modelled as:


###### ′
 𝑺 ≅𝒉𝝆𝒗 𝒚𝒙 𝑻,𝑯


###### 𝒅𝑽
 𝒅𝒙



######  The eddy viscosity 𝜈, [m[2]/s] is also referred to as horizontaldiffusivity. 𝑇 𝐻

  The momentum equation in the alongshoredirection now reads:


###### 𝑫 𝒘
 𝒄 𝟎


###### 𝒔𝒊𝒏𝝋 + [𝒅] 𝟎
 𝒅𝒙 [𝒉𝝆𝒗][𝑻,𝑯]


###### 𝒅𝑽
 = ത𝝉 𝒃,𝒚 𝒅𝒙


-----

######  The effect of turbulent forces, smoothing the longshore

 current profile, is indicated in Figure.

  The largest velocity gradient at the breaker line causes the

 maximum transfer of horizontal momentum, reducing the

 peak velocity and shifting it landward.

  This also creates longshore currents outside the breaker

 zone.

  The cross-shore distribution of eddy viscosity (𝜈𝑇 ​) further

 influences the velocity profile.


-----

### Roller momentum



######  Wave set-up is observed to start closer to the coast than expected.

  This spatiallag was attributed to the rollermomentum, which had not been taken into account.

  Similarly longshore current velocity profiles show an onshore shift in the maximum longshore

 current velocity.

  This can be modelled by including the roller contribution in the alongshore momentum

 equation.


-----

### g



######  Until now we have only considered regular waves. In reality, of course, waves are irregular and

 there is no sharply defined breaker line.

  The effect of wave irregularity is therefore to smooth out the velocity distribution, very similar

 to the effect of turbulence, giving a wider and less sharplypeaked velocity distribution.

  This is also illustrated in Figure, which shows the output of a computation with the computer

 model Unibest-CL+.


-----

### 3D effects



######  Wave conditions can vary along the coast due to factors like wave refraction over uneven sea beds

 or wave diffraction near structures. These changes affect wave-induced forces, making terms

 like 𝜕𝑆𝑦𝑦/𝜕𝑦 and 𝜕𝑆𝑥𝑦/𝜕𝑦 may be non-zero.

  Variations in wave height along the coastline also cause differences in cross-shore wave forces and

 wave set-ups.

  Consequently, pressure gradients 𝜌𝑔ℎ 𝜕ҧ𝜂/𝜕𝑦 occur along the coast and 3D current patterns are the

 result. We will briefly discuss the following situations:

 i) Eddy formation in the shadow zone of structures;

 ii) Creation of rip currents;

 iii) 3D current patterns around shoals


-----

### Eddy formation in the shadow zone of structures



######  In the case of wave sheltering due to for instance groynes or detached breakwaters, wave set-up

 can be expected to be less in the sheltered area than in the unshelteredregion.

  This generates local nearshore currents towards the sheltered area.

  In the shadow zone of the groyne, due to set-up differences a current runs towards the groyne, until

 it i di t d t d l th t t ti dd


-----

######  In Figure set-up differences create nearshore currents towards the sheltered zone from both sides

 of the detached (emerged) breakwater.

  Therefore, a return flow will be present in deeper water, resulting in the development of two eddies.


-----

### p g g gy



######  Rip currents are strong, narrow flows moving seaward from the surf zone, fed by longshore

 currents that turn offshore.

  Longshore currents form due to wave set-up differences, flowing from high to low set-up areas.

  Variations in set-up arise from wave energy convergence/divergence due to depth refraction or

 sheltering(e.g., headlands).

  An undulating coastline focuses wave energy at peaks, creating rhythmic rip currents. This pattern

 develops mainly under near-normal wave incidence.


-----

###### stress (see Figure) will overshadow the more subtle effects of set-up differences.

  A combination of the two effects may occur for slightly oblique wave incidence.


-----

#### Wave induced currents around shoals (and submerged breakwaters)



######  In case of a complex topography with interrupted breaking, the pattern of wave-induced currents

 is more complicated.

  A still relatively simple example concernsa shoal on which waves are breaking (see figure).

  Due to refraction, thewaves will tend to converge toward the top of the shoal.

  As the waves break on the seaward slope of the shoal, they generate a dissipation-related wave


-----

######  At the top of the shoal, there is no closedboundary that requires a zero mean flow.

  Instead, the water will flow over the shoal in the direction of the force.

  The water flows over the shoal until it reaches the channel behind the shoal, where water

 level gradients will deflect it and drive it to the sides of the shoal.

  There it has room to flow seawards again, thus closingthe circulation.

  In tidal inlets systems the wave-driven currents around shoals on the outer delta can be so

 strong that they dominate the tidal residual currents


-----

###### In a similar fashion, the interruption of wave breaking can generate rip currents along a stretch

 of coast.

  Non-homogeneous wave-breaking can occur in the case of a non homogeneous alongshore bar

 system or a ( series of ) submerged breakwater(s) on which waves break, see Figure.

  Wave-breaking on the bar induces a set-up over the bar as well as an onshore flow.

  Water level gradients and continuity force the flow to deflect to the sides and return seaward in


-----

### p



######  Moving air exerts a shear stress 𝜏 on the water surface that can be modelled by, again, a quadratic

 friction law:

 𝝉 𝝆 𝑾[𝟐] wind = 𝑪𝒅 𝒂

 Where:

 𝝉 wind = wind shear stress in N/m[2]

 𝐶 = drag coefficient dependingon wind velocity: 𝑑

 𝐶 = (0.63 + 0.066𝑊 ) × 10−3 for 2 < 𝑊 < 21 (Smith & Banke, 1975) 𝑑

 𝜌 = density of air (1.25 kg/m[3]) in kg/m[3] 𝑎

 𝑊 = wind velocity at the water surface in m/s


-----

######  Windshearstress causes the upper water layers to move in the wind s direction.

  A seaward wind creates a seaward current in the upper layers, while a landward wind creates a

 landward current.

  However, the coastline blocks the landward current, so in equilibrium, the net onshore flow must be zero.

  To balance this, opposite-directed currents form in the lower water layers. Additionally, a water level

 set-up or set-down occurs near the coast to counteract the wind-inducedshear stresses.


-----

######  The equilibriumconditionis given by:


###### 𝝆𝒈𝒉 [𝒅᪄𝜼]
 𝒅𝒙 [= 𝝉][wind][,𝒙]

  Wind set-up is inversely proportional to water depth, causing water to pile up significantly in

 shallowcoastal areas (e.g., storm surges).

  When wind blows parallel to the coast, it generates a longshore current, which takes about a day

 to fully develop.

  In equilibrium, without other forces, the wind shear stress balances the bed shear stress, similar to

 wave-induced currents.


-----

######  The vertical distribution of the wind-generated current differs substantially from the current

 generated by a water level gradient (see figure).

  The highest flow velocities occur at the water surface, with usually a rapid decrease in the

 downward direction (much more than with the logarithmic velocityprofile).


-----

######  During storms, wind stress can significantly influence the residuallongshorecurrent.

  However, in the littoral zone, its effect is often negligible, and its morphological impact is limited

 due to low velocities near the seabed, where sediment concentrationsare highest.

  Wind-driven currentsare more important in areas like coastallagoons.


-----

###### A steady wind of velocity 15 m/s blows over a shallow rectangular lagoon of uniform depth 5 m and length

 20 km. The wind shear stress acting on the water surface follows the quadratic law Where drag coefficient
 𝑪𝒅 = (𝟎. 𝟔𝟑+ 𝟎. 𝟎𝟔𝟔𝑾) × 𝟏𝟎[−𝟑] and the air density is 1.25 kg/m³, steady one-dimensional flow and

 neglect bottom friction and Coriolis effects. Determine the wind shear stress?

 Solution: drag coefficient 𝐶𝑑 = 0.63 + 0.066𝑊 × 10[−3]
 𝐶𝑑 = 0.63 + 0.066 × 15 × 10[−3]
 𝐶𝑑 = 1.62 × 10[−3]
 𝜏wind = 𝐶𝑑 𝜌𝑎𝑊 [2]
 𝜏 × 1.25 × 15[2] wind = 1.62 × 10[−3]

 𝜏 wind = 0.456 𝑁/𝑚[2]


-----

