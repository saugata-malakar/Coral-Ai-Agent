# Coastal Hydrodynamics I

###### Course : CE60222

#### Dr. Mohammad Saud Afzal

###### Associate professor


-----

## Contents



####  Introduction

  Wave deformation

  Shoaling

  Refraction

  Diffraction

  Wave breaking


-----

## Introduction



######  Coastal hydrodynamics outlines the importance of understanding nearshore hydrodynamics for sediment
 transport.

  It highlights the following aspects:

 1. Mean and Oscillatory Water Levels: Discuss how waves, wind, and tides influence water levels and
 currents.

 2. Wave Propagation: Linear wave propagation effects, including how waves change as they approach the
 shore, such as increasing in height and decreasing in wavelength.

 3. Non-linear Wave Transformation: The transformation of wave shapes from symmetric to asymmetric
 profiles as they near breaking.

 4. Wave Boundary Layer: The effects of wave dissipation in the boundary layer on wave velocities and
 sediment transport will be explored.

 5. Wave-Induced Water Level Changes: It will address phenomena like wave set-up (the rise in water level at
 the coast) and the resulting currents, including cross-shore and longshore currents.


-----

## Wave Deformation


###### Energy balance

  When waves propagate from deep into intermediate and shallow water, the waves transform, i.e. wave

 height, length and direction change until the waves finally break and lose their energy.

  Wave transformation takes place because the waves are affected by the seabed through processes such as

 refraction, shoaling, bottom friction and wave breaking.

  Numerically (or analytically) solving the energy balance yields information on the wave transformation of

 a wave field, while the waves approach the shore.

  In the presence of a current, energy is not conserved any longer, since transfer of energy between waves

 and currents is possible.

  In that case another wave quantity, wave action 𝐸/𝜔, will be conserved and the wave action balance rather

 than the energy balance should be solved.

  In the absence of a current the wave action balance reduces to the energy balance


-----

######  Integrating over all frequencies and directions in an irregular wave field, Energy conservation can be
 composed :


###### 𝝏𝑬
 𝝏𝒕ณ
 change of energy


###### 𝝏 +
 𝝏𝒙 [𝑬𝒄][𝒈][𝒄𝒐𝒔𝜽]
 import of energy in 𝒙−direction


###### 𝝏 +
 𝝏𝒚 [𝑬𝒄][𝒈][𝒔𝒊𝒏𝜽]
 and in 𝒚−direction


###### = 𝑺−𝑫
 gain of energy


###### (1)



######  Definition of wave angles for a wave propagating along a wave ray 𝑠 is shown in Fig 1.

 where

 𝜃 = the wave direction angle with respect to the 𝑥-axis

 𝑆 = generation term

 D = Dissipation term

 Cg = wave group speed

 𝜑 = the angle of incidence with respect to

 the depth contours.

 Fig 1. Sketch showing a wave propagating along a wave ray


###### -axis


-----

######  If we assume that the wave conditions are stationary (do not change in time). The term 𝜕𝐸/𝜕𝑡 on the left-hand

 side equals zero.

  The energy balance in the coastal zone can be written as:


###### 𝒅
 𝒅𝒙 [𝑬𝒄][𝒈] [𝐜𝐨𝐬𝜽+]


###### 𝒅
 (2) 𝒅𝒚 [𝑬𝒄][𝒈] [𝒔𝒊𝒏𝜽= −𝑫][𝒇] [−𝑫][𝒘]


###### Where

 𝟐
 𝑬= [𝟏] total wave energy being propagated at the wave group speed 𝒄𝒈 in the wave
 𝟖 [𝝆𝒈𝑯][𝒓𝒎𝒔]
 propagation direction 𝜃.

 𝐷𝑤 = Wave dissipation due to wave-breaking

 𝐷𝑓 = Wave dissipation due to bottom friction

  The direction 𝜃 can change and we therefore need information on 𝜃 to find a solution.

  For simple cases (alongshore uniform coast), Snell’s law gives this information.


-----

######  Equation 2 can also be written along a wave ray 𝑠:

 𝒅
 (3) 𝒅𝒔 [𝑬𝒄][𝒈] [= −𝑫][𝒇] [−𝑫][𝒘]

  Overall, the energy balance is crucial for understanding how waves interact with the coastal environment and

 the resulting implications for sediment transport and coastal management.


-----

## Shoaling



######  Wave shoaling is a phenomenon that occurs as ocean waves travel from deeper water into shallower areas,

 causing changes in wave height, wavelength, and wave speed.

  As waves enter shallower water, their speed decreases, leading to a reduction in wavelength and an

 increase in wave height.


-----

######  Outside the breaker zone the dissipation is approximately zero (neglecting bottom friction) and integration

 of Equation-3 yields:

 𝑼= 𝑬𝒄𝒈 = 𝑬𝒏𝒄= 𝐜𝐨𝐧𝐬𝐭𝐚𝐧𝐭 (4)

 Where, 𝑈 = wave power or energy flux per unit wave crest width J/(m s)

 𝐸 =wave energy per unit surface area J/m[2]

 c𝑔 = wave group velocity m/s

 𝑐 = wave celerity m/s

 𝑛 = ratio 𝑐𝑔 to 𝑐

 Fig 3. Normally incident waves with parallel depth contours
 (φ = θ = constant = 0).


-----

######  Wave Power: The wave energy flux is the rate at which energy is transmitted in the direction of wave

 propagation across a vertical plane perpendicular to the direction of wave advance and extending down the

 depth.

 The average flux per unit wave crest is given as,
 Deep water n=0.5, 𝑪𝒈=0.5C
 𝑷= 𝑬𝒏𝑪= 𝑬𝑪𝒈
 Shallow water n=1, 𝑪𝒈=C
 𝟏 𝟐𝒌𝒅
 where, 𝒏=
 𝟐 [𝟏+] 𝒔𝒊𝒏𝒉𝟐𝒌𝒅
 Transition water 0.5 < n < 1

 Deep water conditions
 Shallow water conditions


###### 𝟐𝒌𝒅
 𝒔𝒊𝒏𝒉𝟐𝒌𝒅 [= 𝟎𝐚𝐧𝐝𝑪][𝒈][=][𝟏]𝟐 [𝒄] [and n=][𝟏]𝟐


###### 𝒔𝒊𝒏𝒉𝟐𝒌𝒅= 𝟐𝒌𝒅𝒂𝒏𝒅𝑪𝒈=𝒏C and n=1

 𝑷= 𝑬𝑪


###### 𝑷𝟎 =


###### 𝟏 𝟐 [𝑬][𝟎][𝑪][𝟎]


-----

######  Assuming the wave propagates from deep water towards the shore and the ocean bottom slope is gradual

 and there are no undulations and has parallel bottom slope contours.

  Accordingly to the conservation of energy Equating the power in the deep waters to that in shallow waters.

 𝑷𝟎 = 𝑷


###### 𝟏 𝟐 [𝑬][𝟎][𝑪][𝒐] [= 𝑬𝒏𝑪]

 𝝆𝒈 𝟐 𝟎
 . [𝑪]
 𝟖 [𝑯][𝟎] 𝟐 [=][ 𝝆𝒈]𝟖 [𝑯][𝟐] [𝒏𝑪]


###### 𝑯[𝟐]

𝟐 [=][ 𝟏]

###### 𝑯 𝟐𝒏 [.][ 𝑪]𝑪[𝟎]
𝟎



[𝟎] **Shoaling co-efficient**

###### 𝑪 [= ][𝑲][𝒔]


-----

######  The parameter 𝑲𝒔 is called the shoaling factor.



######  In Fig. 4 it is shown as a function of


###### 𝐻
 𝐿0 [. ]



######  𝐾𝑠 is 1.0 in deep water, then decreases slightly with water depth to 0.91 and subsequently rises to infinity.

 𝐾𝑠

 Fig 4. The shoaling factor 𝐾𝑠 = [𝐻]
 𝐻0[, n and ]𝐶[𝐶]0 [=][ 𝐿]𝐿0 [as a function of ]𝐿[ℎ]0 [.]


###### 𝐾𝑠


-----

## Problem


###### A 10 s period wave having a height of 5 m propagates from deep to shallow waters. Assuming that the

 bottom contours are parallel to each other, compute the wave height at a water depth of 10 m.

 Solution- Given data, T =10 sec, d = 10m,𝐻0 = 5m

 𝐿0=1.56𝑇[2]=1.56 ×10[2]=156m   

 𝑑
 𝐿0 [= ]156[10] [= ][0.0642]


###### 𝑑
 𝐿 [= ][0.1082 ][(from wave table)]

 𝑑 10 L =
 0.1082 [= ]0.1082 [= ][92.4m]


###### 𝐶0= [𝐿][0]
 𝑇 [= ][156]10 [= ][15.6 m/s]

 C = [𝐿] = [92.4] = 9 24 m/s


-----

###### k =

 n =


###### 2π
 L [= ][0.06523]

 1 2kd
 (as 2kd =1.31)
 2[(1+]sinh 2kd[) = ][0.88]


-----

## Refraction



######  Instead of a normally incident wave, consider now an obliquely incident linear wave approaching at a deep
 water angle 𝝋𝟎 to the shore.

  The wave is again long-crested and the bottom contours are essentially straight and parallel as shown in Fig.4.


-----

######  When a wave approaches underwater contours at an angle, it is evident that the sections of the crest in the

 deeper parts travel faster than those in the shallower sectors.

  This causes the wave crest to turn towards the depth contour. This bending effect is called Refraction.

 Fig 6. Slowing and bending of waves as they approach shore


-----

######  Construction of wave refraction diagrams

 A train of waves travels over a step where the depth instantaneously decreases from 𝒅𝟏 to 𝒅𝟐, causing the

 wave celerity 𝑪𝟏 and 𝑳𝟏 to 𝑪𝟐 and 𝑳𝟐 respectively. From figure 7, we can observe that:

 sin 𝛼1 = [𝐿][1]
 𝑥 [=][ 𝐶][1]𝑥[𝑇]
 sin 𝛼2 = [𝐿][2]
 𝑥 [=][ 𝐶]𝑥[2][𝑇]

 Dividing:

 sin 𝛼1
 = [𝐶][1] = [𝐿][1] Snell’s Law
 sin 𝛼2 𝐶2 𝐿2

 Figure-7: Definition sketch for Snell’s law


-----

######  Waves approaching at an oblique angle are refracted in

 such a way that the angle α is decreased, corresponding to

 the wave fronts that tend to become more nearly parallel

 to the shore.

  Let us consider two wave rays, defined as orthogonal or

 ray of the wavefronts, at a distance b apart at constant

 𝑑
 𝐿0 [= 0.5,]


###### cos 𝛼0 = [𝑏][0]
 𝐵𝐶

 cos𝛼= [𝑏]
 𝐵𝐶


###### 𝑏0 𝐵𝐶=
 cos 𝛼0


###### 𝑏 =
 cos 𝛼


###### Fig 8. Schematic representation of wave deformation


###### cos 𝛼0 𝑏0


-----

######  A refraction diagram is a plot showing the coordinate positions of the orthogonal for a given location with

 defined bathymetry (depth contours).

  The figure shows a typical view of the understanding of wave refraction.


-----

######  Wave energy converges in the case of convex depth contours and diverges in the case of concave depth

 contours.

  Convergence of orthogonal leads to an increase in wave heights or energy, resulting in shore erosion.

  Divergence of orthogonal leads to a reduction in wave heights or energy, resulting in accretion or

 deposition.


-----

###### Combined effect of refraction and shoaling

  In the analysis of the refraction phenomenon, it is assumed that for an advancing wave approaching the

 shore, energy flow is absent along the wave crest in the lateral direction.

  It implies that the energy transmitted remains constant between the orthogonal.

  The average power transmitted by a wave is given by

 𝑷= 𝒏𝒃𝑬𝑪
 where, 𝒏= [𝟏] 𝟐𝒌𝒅
 𝟐 [𝟏+] 𝒔𝒊𝒏𝒉𝟐𝒌𝒅

 Deep water conditions
 Shallow water conditions


###### 2𝑘𝑑 1 1
 𝑠𝑖𝑛ℎ2𝑘𝑑 [= 0 and 𝐶][𝑔][=]2 [𝑐] [and n=]2

 𝑃0 = [1]
 2 [𝑏][0][𝐸][0][𝐶][0]


###### 𝑠𝑖𝑛ℎ2𝑘𝑑= 2𝑘𝑑𝑎𝑛𝑑𝐶𝑔=𝑛C

 𝑃= 𝑛𝑏𝐸𝐶


-----

######  Since energy flow is absent along the wave crest in the lateral direction
 𝑷= 𝑷𝟎
 𝒏𝒃𝑬𝑪= [𝟏]
 𝟐 [𝒃][𝟎][𝑬][𝟎][𝑪][𝟎]


###### 𝑬
 𝑬𝟎 [=]


###### 𝟏
 𝟐𝒏


###### 𝒃𝟎
 𝒃


###### 𝑪𝟎
 (i) 𝑪

[𝟐]

###### (ii)
𝟐

[𝟎]

###### 𝒃𝟎 𝑪𝟎 Shoaling Co-efficient (𝑲𝒔)
 𝒃 𝑪

 𝑪𝟎 𝒃𝟎
 𝑪 𝒃 [= 𝑲][𝒔][𝑲][𝒓]

 Refraction Co-efficient (𝑲𝒓)


###### From Equation (i) and (ii), we found as:


-----

## Problem


###### A deep water wave of height 3.5 m and period 10 s is refracted so that the distance between the

 orthogonals is reduced by 50 % at a depth of 10 m and reduced by 20 % at 5 m water depth. What will be

 the height of the wave here, assuming no energy loss?

 Solution- Given, 𝐻0= 3.5m, T= 10s

 H in depth of 10m

 𝐻 1 C0 b0
 𝐻0[=][𝐾][𝑠][. 𝐾][𝑟] [=] 2n [.] C [.] b

 𝑏0 100 2 (as orthogonal is reduced by 50%)
 𝑏 [=] 50 [=]


###### 𝐻
 𝐻0 [=]


0

###### 𝐶 [.]


0

###### 𝑏 [=]


0 2

###### 𝐶 [.]


###### 𝐿 1 56𝑇[2] 1 56 × 10[2] 156m


-----

###### 𝑑
 𝐿0 [=]


###### 10
 156 [=][ 0.0642]


###### 𝑑
 𝐿 [=][ 0.1082 (from wave table)]

 10
 or, L = 92.42 m 𝐿 [=][0.1082]


###### 𝐶0 =


###### 𝐿0
 𝑇 [=]


###### C =

 𝑛=


###### 𝐿 92.4 𝑇 [=] 10

 1 2 [1 +]


###### k =


###### 2𝜋
 𝐿 [=][ 0.06523]


-----

###### 𝐾𝑠 = 𝐶0
 𝑐



###### [ 1]
 2𝑛 [= 0.98]


###### H in depth of 5 m


###### 𝐻
 2 𝐻0 [=][ 0.98 ×]

 H = 0.98 × 2 × 3.5

 H = 4.85m

 𝐻
 𝐻0 [=][ 𝐾][𝑠][. 𝐾][𝑟]

 𝐻 1 𝐶0 𝑏0 1 𝐶0
 𝐻0 [=] 2𝑛 [.] 𝐶 [.] 𝑏 [=] 2𝑛 [.] 𝐶 [.]

 𝐿0=1.56 𝑇[2] = 1.56 × 10[2] = 156m


-----

###### 𝑑
 𝐿0 [=]


###### 5
 156 [=][ 0.032]


###### 𝑑
 𝐿 [=][ 0.0738 (from wave table)]

 5 𝐿 [=][ 0.0738][ or,][ L = 67.75 m]

 𝐶0= [𝐿][0]
 𝑇 [=][ 156]10 [= 15.6 m/s]


###### C = [𝐿] = 6.78 m/s
 𝑇 [= 67.75]10

 𝑛= [1] 2𝑘𝑑
 2 [1 +] 𝑠𝑖𝑛ℎ2𝑘𝑑 [=0.935]


###### 𝐾𝑠 =


###### 2𝑛 [= 1.109]


-----

###### 𝐻
 𝐻0 [=][𝐾][𝑠][. 𝐾][𝑟][= 1.109 × 1.118]

 H = 1.109 × 1.118 × 3.5 = 4.34 m

  In this case, as per the given problem, H in d = 5 m is 4.34, which is greater than the breaking wave height in

 this depth of 0.78 × 5 = 3.9 m. (as maximum wave height 0.78d)

  This only suggests that the 20% reduction in 5 m water depth would not have wave of height greater than 3.9

 m.


-----

## Problem


###### For an average deep-water wave height of 𝟏. 𝟓𝐦, 𝑻𝒂𝒗 = 𝟏𝟎𝐬 and 𝜽𝒐, av = 𝟓𝟎[∘], determine the length of

 the wave energy device if it is to be located in water depth of 𝟔𝐦 and power required is 𝟐𝟎𝟎𝐤𝐖. Assume

 that the device is aligned parallel to the wave crest.

 Solution:

 Given: 𝐻𝑜 = 1.5 m, 𝑑= 6 m, 𝜃𝑜 = 50[∘], 𝑇= 10s

 𝐿𝑜 = 1.56𝑇[2] = 1.56 × 10[2] = 156 m


###### 𝑑
 𝐿0 [=]


###### 6
 156 [= 0.0384]


###### 𝑑
 𝐿 [= 0.0810 (from wave table)]

 6 or, L = 74.07 m 𝐿 [= 0.0810]

 𝐶𝑜 = 𝐿𝑜/𝑇= 156/10 = 15.6 m/s


-----

###### From Snell s law, = 𝐶𝑜 𝐶


###### sin5015.6[∘] [= sin𝜃]7.36 [leading to][ 𝜃= 21.18][∘]

 𝐻 𝐶𝑜 cos𝜃𝑜
 =
 𝐻𝑜 2𝑛𝐶 [⋅] cos𝜃

 𝐻 15.6 cos50[∘]
 =
 𝐻𝑜 2 × 0.922 × 7.36 [⋅] cos21.18[∘] [= 0.889]

 𝐻= 0.889 × 1.5 = 1.335 m.

 𝑃= 𝛾𝐻[2]𝑊/8 ⋅𝐶𝑔

 (where 𝑊 is the width of the wave energy device)

 200,000 = 1030 × 9.81 × 1.335[2] × 𝑊/8 × (0.922 × 7.36)


-----

## Diffraction



######  Diffraction is the bending or spreading of waves when they encounter an obstacle or pass through an

 opening.

  It is dominant around natural barriers or man-made structures such as breakwaters, groins, training

 walls, etc.

 Fig 11. Typical diffraction pattern through a gap between two detached breakwaters in Pesaro, Italy


-----

###### Wave diffraction coefficient:

  If 𝑯𝒊 is the incident wave height at the end of the

 barrier and 𝑯𝒅 is the height of a wave diffracted at

 the point of interest in a sheltered area, then the

 diffraction coefficient (𝑲𝒅) could be defined as:


-----

###### Calculation of wave diffraction coefficient:

  The value of 𝐾𝑑 depends on the location behind the barrier defined by r and 𝛽, and the incident wave direction

 defined by 𝜃 ; or in the dimensionless form given by

 𝑟 𝐾𝑑 = 𝑓 𝐿 [, 𝛽, 𝜃]

 Where

 r = Distance of point of interest

 𝛽 = Diffracted wave direction from barrier

 𝜃 = Incident wave direction from barrier

 L = Wavelength in the lee of the barrier


-----

###### The two most common diffraction problems encountered in coastal engineering design are:

  Diffraction past the end of a semi-infinite barrier, and

  Diffraction through a relatively small gap in a barrier.

 Semi-infinite Barrier:

  The diffraction solution for a semi-infinite barrier is presented by Wiegel (1964).

  Penny and Price (1952) showed that the mathematical solution for the diffraction of light can be used to predict

 the wave crest pattern and height variation for these two wave diffraction problems.

  Wiegel (1962) used the Penny and Price (1952) solution to calculate and tabulate values of 𝐾𝑑 for selected

 values of 𝜃, 𝛽, and r/L.

  The values of 𝐾𝑑 against these parameters are shown in the next slide, as reported in Wiegel (1962).


-----

###### 𝒅 𝑳 [, 𝜷,]


-----

###### 𝒅 𝑳 [, 𝜷,]


-----

###### 𝒅 𝑳 [, 𝜷,]


-----

###### 𝒅 𝑳 [, 𝜷,]


-----

###### Barrier Gap: Large

  If the gap is large, compared to the wavelength of the waves

 passing through, the circular disturbances are tiny compared to

 the undisturbed wavefronts.

  A tiny disturbance at the edge of the straight wavefront leads to

 slight curving of the wavefronts at the edge and a slight spread.


-----

###### Barrier Gap: Small

  If the gap is small, the circular disturbances that get

 through are massive compared to the undisturbed

 wavefronts.

  only circular wavefronts are observed passing

 through the tiny gap in the barrier (instead of straight

 ones)


-----

## Problem


###### Consider a train of 6 s period waves approaching a breakwater so that the angle of approach at the breakwater head is 60⁰. The water depth in the lee of the breakwater is 10 m. Determine the wave height at an angle of 30⁰ from the breakwater and a distance of 96.6 m from the breakwater head if the incident wave height at the head is 2.2 m.

 Solution- Given T=6 sec, 𝜃 = 60[0], 𝛽 = 30[0], r = 96.6, d = 10, 𝐻𝑖=2.2, 𝐻𝑑 = ?

 L0=1.56× T[2]=1.56 × 6[2]=56.16 m

 d 10
 L0 [=] 56.16 [=][ 0.178]


###### d L [=][ 0.2067][ (from wave table)]

 10
 L [=][ 0.2067]

 L = 48.3 m

 r 96.6


-----

###### Then, from the table, (as


###### 𝑟 𝛽 = 30[0]) 𝐿 [= 2,][ 𝜃] [=][ 60][0][,]


###### 𝐾𝑑 = 0.28


###### 𝐾𝑑 = [𝐻][𝑑]
 𝐻𝑖 [= 0.28]

 𝐻𝑑 2.2 [= 0.28]

 𝐻𝑑 = 0.28x2.2

 𝐻𝑑 = 0.62m


-----

## Wave Breaking



######  Wave breaking is the process where a wave loses its stability and collapses, dissipating its energy.

 Conditions for wave breaking:

  When horizontal particle velocity at the crest

 exceeds the celerity of the wave.

  When vertical particle acceleration is greater than

 the acceleration due to gravity.

  When the wave steepness, H/L> 0.142tanhkd.

  When the crest angle is less than 120°.

  When wave height is greater than 0.78d.


-----

######  Miche(1944) describes wave breaking (regular wave) in a surf zone when the limiting wave steepness is:

 𝑯𝒃
 𝑳𝒃 [> 𝟎. 𝟏𝟒𝐭𝐚𝐧𝒉𝒌𝒅][b]

  Munk (1949) derived several relationships from a modified Solitary Wave Theory:

 𝑯𝒃 𝟏
 Breaker Height Index

𝟏

###### 𝑯𝟎 [=]

𝟑

###### 𝟑.𝟑 [𝑯𝟎]

𝑳𝟎

###### Breaker Depth Index 𝒅𝒃 [= 𝟏. 𝟐𝟖]


###### 𝑳𝟎
 𝑯𝟎


𝟏
𝟓



######  Wave height at Breaking Point


###### 𝑯𝒃 𝑯𝟎 [= 𝟎. 𝟓]


-----

###### Effect of bed slope on breaking process:

  Depending on the wave properties and the angle of the bed slope, the process of breaking takes place in

 various different ways.

  Battjes (1974) showed that the Iribarren parameter(ξ) guides this process.

  The Iribarren parameter (ξ) represents the ratio of the slope steepness tanα and the wave steepness.

 𝐭𝐚𝐧𝜶

##### 𝝃=  Spilling Breakers: ξ < 0.5


###### Where, 𝒕𝒂𝒏𝜶 = m = steepness of the beach

 𝑯𝟎 = wave height in deep water

 𝑳𝟎 = wave length in deep water



######  Plunging Breakers: 0.5< ξ < 3.3

  Surging Breakers: 3.3< ξ < 5

  Collapsing Breakers: ξ > 5


-----

###### Types of wave breaking:

  Spilling Breakers: Waves break gradually, with foam spilling down the front. Common on gently sloping

 beaches.

  Plunging Breakers: Waves curl over and crash with significant energy. Often seen on steeper beaches.

  Surging Breakers: Waves don't break entirely but instead surge up the shore. Common on very steep beaches.

  Collapsing Breakers: A hybrid where the crest collapses, but there’s no well-defined curl.


-----

## Problem


###### For a wave with period T = 10 s, deep water wave height Ho = 3.5 m and beach slope m = 1/15. Calculate the

 breaking wave height using munk formulae . Also identify the type of breaking wave.

 Solution, T = 10s, 𝐻0 = 3.5m, m = [1]
 15 [= 0.067]

 𝐿0 = 1.56 𝑇[2] = 1.56 × 6[2] = 56.16 m


###### 𝐻𝑏 3.5 [=]


3.5
###### 3.3

56.16


1
3


###### 𝐻𝑏 = 2.675m


-----

###### ξ =

 ξ =


###### m
 H0/

 0.067


###### Therefore, Spilling Breaker


-----

