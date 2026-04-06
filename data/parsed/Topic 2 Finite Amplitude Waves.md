# Finite Amplitude Waves

###### Dr. Mohammad Saud Afzal
 Associate Professor
 Department of Civil Engineering
 Indian Institute of Technology Kharagpur


-----

## Introduction

### • Finite-amplitude wave theories are generally of two types. There are
 numerical theories that employ a finite difference, finite element, or boundary integral method to solve the Laplace and boundary condition equations.

 • There are also analytical theories in which the velocity potential (and
 other parameters such as the surface amplitude and wave celerity) is written as a power series that is solved by successive approximations or by the perturbation approach.


-----

##### • For numerical theories a computer solution of the numerical equations yields
 tabulated values of the desired wave characteristics such as the surface profile, particle velocity and acceleration, dynamic pressure, energy and momentum flux, etc. as a function of selected values of wave height and period and water depth.

 • On the other hand, the analytical theories produce specific equations for the
 various wave characteristics which are given in terms of the wave height and period and the water depth.

 • Both numerical and analytical theories are not complete solutions of the wave
 boundary value problem, but infinite series solutions that must be truncated at some point (e.g., truncation of a series after the third term yields a third-order solution).


-----

### • In this chapter we briefly consider four finite-amplitude wave
 theories.

 • The Stokes theory for deep water waves and the cnoidal and solitary
 theories for shallow water waves are useful analytical theories. Dean’s stream function numerical wave theory is a commonly used numerical theory applicable to finite-amplitude waves throughout the range of relative water depths.


-----

## Stokes Waves


-----

### • As the deep water wave steepness increases improved accuracy can
 generally be achieved (at the price of more onerous equations to work with) if the Stokes theory is carried out to higher orders.

 • Various higher order approximations to the Stokes theory have been
 developed.

 • For example, see Skjelbreia (1959) for a third-order theory, Skjelbreia
 and Hendrickson (1961) for a Fifth-order theory, and Schwartz(1974) for much higher order solutions based on calculations using a powerful computer.

 • For engineering applications the second- order and possibly the fifth order theories are most commonly used.


-----

##### • For the Stokes theory second-order solution the velocity potential is given by


###### Φ = [𝑔𝐻]
 2𝜎


###### cosh 𝑘(𝑑+ 𝑧)
 sin 𝑘𝑥−𝜎𝑡+ [3𝜋𝐶𝐻] cosh 𝑘𝑑 16


###### cosh 2𝑘𝑑+ 𝑧
 sin 2 𝑘𝑥−𝜎𝑡 (1) sinh[4] 𝑘𝑑



##### • Inspection of the above equation reveals a number of important features of the
 second-order theory.

 • Comparison of above equation with the one we derived earlier for Φ shows that
 the first term on the right is the small-amplitude theory velocity potential.



##### • The magnitude of the second term on the right is dependent on the wave
 steepness, a ratio that has a numerical value that is significantly less than unity but that increases as the wave amplitude increases for a given wave period.

 • The second term on the right also has a frequency that is twice that of the small amplitude term.


-----

###### • The surface profile is given by

 𝜂= [𝐻]
 2 [cos 𝑘𝑥−𝜎𝑡+][ 𝜋𝐻]8


###### cos 2 𝑘𝑥−𝜎𝑡 2 sinh[3] 𝑘𝑑


###### for which the same comments can be made as were made above for the velocity potential.

 • The effect of the second-order term having twice the frequency of the small-amplitude
 or first-order term is that the two components of surface amplitude reinforce (i.e., are in phase) each other at the wave crest and oppose each other at the wave trough.



###### • This yields a surface profile vertical asymmetry (more peaked wave crest and flatter wave
 trough than a cosine profile given by the small-amplitude theory) that grows as the wave steepness increases.


-----

##### amplitude wave theory.

 • Thus, to the second order, waves are still period dispersive but not amplitude
 dispersive. For the Stokes third-order theory the dispersion relationship becomes


##### 𝐶[2] = [𝑔]
 𝑘 [tanh 𝑘𝑑1 +][ 𝜋𝐻]𝐿


###### 2 4 2
##### 9 + 8 cosh 𝑘𝑑−8 cosh 𝑘𝑑
 3 8 sinh[4] 𝑘𝑑



##### • Thus, to the third order, wave celerity is amplitude as well as period dispersive.

 • For the same wave period higher waves travel faster than lower waves.

 • For the limiting steepness in deep water (𝐻0 1

###### 𝐿0 [=] 7[) the third-order theory yields a]

##### wave celerity that is about 10% greater than the celerity given by the small- amplitude theory.



##### • A greater celerity for the same wave period means that the wave length would
 also be 10% larger (since 𝐿= 𝐶𝑇).


-----

###### For deep water,


###### 𝜂= [𝐻][0]
 2 [cos 𝑘𝑥−𝜎𝑡+ 𝜋𝐻]4 [0]


###### 𝐿0


###### cos 2 𝑘𝑥−𝜎𝑡 4



###### • which yields the following relationships for the amplitude of the wave crest 𝑎c and wave trough
 𝑎t :
 2 2
 𝑎𝑐 = [𝐻][0] 𝑎𝑡 = [𝐻][0] 5
 2 [+ 𝜋𝐻]4𝐿0[0] 2 [−𝜋𝐻]4𝐿0[0]

 • From Eq. (5) for the limiting wave steepness in deep water (1/7) we have 𝑎𝑐 = 0.611𝐻 and 𝑎t =
 0.389𝐻.



###### • Equation (2) shows that as a wave enters intermediate water depths the asymmetry will increase
 over its equivalent deep water value.


-----

##### g, p p p g g p j p
 water limit. Using the equations presented above, calculate the wave celerity and length. Also, determine the wave crest and trough amplitudes. Compare the results to those from the small-amplitude wave theory.


###### Solution:

 For deep water Eq. (3) reduces to
 𝑔𝐿0 𝐶0 = 1 + [𝜋𝐻]
 2𝜋 𝐿

 Inserting 𝐿0 = 𝐶0 𝑇 yields
 𝑔𝐶0𝑇 𝐶0 = 1 + [𝜋𝐻]
 2𝜋 𝐶

 which can be solved (𝑇= 7𝑠 and 𝐻0 = 6𝑚) by trial to yield

 𝐶0 = 11.54𝑚/𝑠


-----

###### For the small amplitude theory, yields 𝐶0 = 10.93𝑚/𝑠 and 𝐿0 = 76.50𝑚.

 The Stokes theory values are both 5.5% higher.

 The steepness of this wave is 6/80.78 = 0.074 or about half the limiting steepness of 1/7.


###### 𝜋(6)[2]
 𝑎𝑐 = [6]
 2 [+] 4(80.78) [= 3.35𝑚]
 𝜋(6)[2]
 𝑎𝑡 = [6]
 2 [−] 4(80.78) [= 2.65m]


-----

##### With increasing wave steepness the second order term in Eq. (2) increases in size relative to the first-order term.

 • The causes an accelerated ‘‘peaking’’ at the wave crest where the two terms are
 in phase; but at the wave trough the first- and second-order terms are out of phase, causing the trough to become increasingly flat.

 • A point is reached where the trough surface becomes horizontal.

 • Increases in wave steepness beyond this point cause a hump to form and grow at
 the wave trough.

 • This hump is not a real wave phenomenon and its appearance is an indication
 that the theory is being used beyond its appropriate limit.


-----

##### • If we set a limit of applicability at the point where the trough becomes horizontal,
 the maximum wave steepness for application of the second-order Stokes theory would be

 𝐻 sinh[3] 𝑘𝑑
 6
 𝐿 [=] 𝜋cosh 𝑘𝑑(2 + cosh 2𝑘𝑑)

 • In deep water the steepness value given by Eq. (6) is greater than 1/7 so the limit
 has no practical meaning.

 • For a relative depth (𝑑/𝐿) as small as 0.1 the limiting steepness from Eq. (6) is
 0.021.

 • This puts a significant restriction on the use of the second-order theory as the
 wave propagates into shallower water.


-----

###### The Stokes second order equations for particle velocity and acceleration follow:


###### cosh2𝑘𝑑+ 𝑧
 cos2 𝑘𝑥−𝜎𝑡 (7) sinh[4] 𝑘𝑑


###### 𝑢= [𝜋𝐻]
 𝑇


###### cosh𝑘𝑑+ 𝑧
 cos 𝑘𝑥−𝜎𝑡+ [3(𝜋𝐻)][2] sinh𝑘𝑑 4𝑇𝐿


###### sinh2𝑘𝑑+ 𝑧
 sin2 𝑘𝑥−𝜎𝑡 8 sinh[4] 𝑘𝑑

 [𝐻][2]
 cosh2𝑘𝑑+ 𝑧
 sin2 𝑘𝑥−𝜎𝑡 9
 𝐿 sinh[4]𝑘𝑑


###### 𝜋𝐻 𝑤=
 𝑇


###### sinh𝑘(𝑑+ 𝑧)
 sin(𝑘𝑥−𝜎𝑡) + [3(𝜋𝐻)][2] sinh𝑘𝑑 4𝑇𝐿


###### 2𝜋[2]𝐻 𝑎𝑥 =
 𝑇[2]

 𝑎𝑧 = − [2𝜋][2][𝐻]

 [2]


###### sinh2𝑘(𝑑+ 𝑧)
 cos2(𝑘𝑥−𝜎𝑡) 10 sinh𝑘𝑑



###### • The second-order terms in Eqs. (7) to (10) also have twice the frequency of the first-order terms,
 leading to asymmetries in the particle velocity and acceleration as a particle completes its orbit.

 • The particle velocity and acceleration are increased under the wave crest and diminished under
 the wave trough. A i th t i i th t i


-----

###### 2 sinh 𝑘𝑑 8𝐿sinh[2] 𝑘𝑑 2 sinh[2] 𝑘𝑑


###### 𝜁=

 𝜀= [𝐻]
 2


###### sinh 𝑘(𝑑+ 𝑧)
 cos 𝑘𝑥−𝜎𝑡+ [3𝜋𝐻][2] sinh 𝑘𝑑 16𝐿


###### + [𝜋𝐻][2]
 4𝐿


###### cosh 2𝑘𝑑+ 𝑧
 𝜎𝑡 (11) sinh[2] 𝑘𝑑


###### sinh 2𝑘𝑑+ 𝑧
 cos 2 𝑘𝑥−𝜎𝑡 (12) sinh[4] 𝑘𝑑



###### • Note that the last term in Eq. (11) is not periodic but continually increases with time, indicating a net
 forward transport of water particles as the wave propagates. If we divide the last term in Eq. (11) by time we have the second-order equation for the mass transport velocity


###### ᪄𝑢= [𝜋][2][𝐻][2]
 2𝑇𝐿


###### cosh 2𝑘(𝑑+ 𝑧)
 13 sinh[2](𝑘𝑑)



###### • Since the surface particle velocity at the crest of a wave in deep water is 𝜋𝐻= 𝑇 to the first order, Eq. (13)
 indicates that the surface mass transport velocity is of the order of the crest particle velocity times the wave


-----

##### p p y
 distance below the water surface level for 𝑧= 0, −0.1, −0.2, −0.3, −0.4, and −0.5 times the wave length. Compare this to the wave celerity and crest particle velocity.


###### Solution:

 For the first or second order, the wave length is given by

 𝐿0 = [9.81(7)][2] = 76.5 m
 2𝜋

 Thus, the water depth is 76.5/2 = 38.25 m and 𝑘= 2𝜋/76.5 = 0.0821. Then, the mass transport velocity, given by Eq. (13), becomes

|Col1|velocity.|Col3|
|---|---|---|
||||
||||


###### 𝜋[2](6)[2] ᪄𝑢 =
 2(7)(76.5)


###### cosh 2(0.0821)(𝑑+ 𝑧)
 = 0.0025cosh 0.164(𝑑+ 𝑧) sinh[2](𝜋)


-----

###### 0 38.25 0.665
 −7.65 30.60 0.189
 −15.30 22.95 0.053
 −22.95 15.30 0.015
 −30.60 7.65 0.004
 −38.25 0 0.002


###### Note the rapid decay in the mass transport velocity with distance below the still water level. The wave celerity is


###### 𝐶0 = [9.81(7)] = 10.93 m/s
 2𝜋


###### for both the first and second order. Using the first-order crest particle velocity as sufficient for comparison

 purposes we have

 𝑢𝑐 = [𝜋(6)] = 2.69 m/s
 7

 Thus the celerity crest particle velocity and mass transport velocity at the water surface are 10 93 𝑚/𝑠


-----

###### • The pressure field in a wave according to the Stokes second order is


###### cosh2𝑘(𝑑+ 𝑧)
 − [1] sinh[2](𝑘𝑑) 3 [cos2(𝑘𝑥−𝜎𝑡)]


###### 𝑝= 𝜌𝑔𝑧+ [𝜌𝑔𝐻]
 2


###### cosh𝑘(𝑑+ 𝑧) cos(𝑘𝑥−𝜎𝑡) + [3𝜋𝜌𝑔𝐻][2]
 cosh𝑘𝑑 4𝐿sinh2𝑘𝑑


###### 𝜋𝜌𝑔𝐻[2] − (14)
 4𝐿sinh2𝑘𝑑 [cosh2𝑘𝑑+ 𝑧−1]

 • Besides the usual higher frequency second-order term, there is a noncyclic last term on the righthand side.



###### • This noncyclic term has a zero value at the bottom which is in keeping with the requirement that if there is
 no vertical velocity component at the bottom boundary there can be no vertical momentum flux so the time average pressure must balance the time average weight of water above.

 • Away from the bottom there is a time average vertical momentum flux owing to the crest to trough
 asymmetry in the vertical velocity component.

 • This produces the above-zero time average dynamic pressure given by this last term on the right in Eq. (14).


-----

## Cnoidal Waves

###### • The applicability of Stokes theory diminishes as a wave propagates across decreasing
 intermediate/shallow water depths.



###### • Keulegan (1950) recommended a range for Stokes theory application extending from deep water
 to the point where the relative depth is approximately 0.1.

 • However, the actual Stokes theory cutoff point in intermediate water depths depends on the
 wave steepness as well as the relative depth.



###### • For steeper waves, the higher order terms in the Stokes theory begin to unrealistically distort
 results at deeper relative depths.

 • For shallower water, a finite-amplitude theory that is based on the relative depth is required.

 • Cnoidal wave theory and in very shallow water, solitary wave theory, are the analytical theories
 most commonly used for shallower water.


-----

#### Cnoidal wave theory is based on equations developed by Korteweg and de Vries (1895).

 • The resulting equations contain Jacobian elliptical functions, commonly
 designated 𝑐𝑛, so the name cnoidal is used to designate this wave theory.

 • The most commonly used versions of this theory are to the first order, but
 these theories are still capable of describing finite-amplitude waves.

 • The deep water limit of cnoidal theory is the small-amplitude wave theory
 and the shallow water limit is the solitary wave theory.

 • Owing to the extreme complexity of applying the cnoidal theory, most
 authors recommend extending the use of the small-amplitude, Stokes higher order, and solitary wave theories to cover as much as possible of the range where cnoidal theory is applicable.


-----

###### • The most commonly used presentation of the cnoidal wave theory is from Wiegel (1960), who synthesized
 the work of earlier writers and presented results in as practical a form as possible.

 • Some of the basic wave characteristics from cnoidal theory, such as the surface profile and the wave celerity,
 can be presented by diagrams that are based on two parameters, namely 𝑘[2] and 𝑈𝑟.

 • The parameter 𝑘[2] is a function of the water depth, the wave length, and the vertical distance up from the
 bottom to the water surface at the wave crest and trough.

 • It varies from 0 for the small-amplitude limit to 1.0 for the solitary wave limit as the ratio of the crest
 amplitude to wave height varies from 0 to 1.0 for the two wave theories.

 • 𝑈𝑟, which is known as the Ursell number (Ursell, 1953), is a dimensionless parameter given as 𝐿[2]𝐻/𝑑[3] that
 is also useful for defining the range of application for various wave theories.

 • From Hardy and Kraus (1987) the Stokes theory is generally applicable for 𝑈𝑟 < 10 and the cnoidal theory
 for 𝑈𝑟 > 25.

 • The theories are equally applicable in the range 𝑈= 10 to 25


-----

###### depth.

 • From Figure 1 𝑇( g/𝑑)[0.5] and 𝐻/𝑑 yield the value of 𝑘[2] which then yields (using the dashed line) a
 value for the Ursell number.



###### • The Ursell number indicates how appropriate cnoidal theory is for our application and allows the wave
 length to be calculated if the wave height and water depth are known.

 • This then gives the wave celerity from 𝐶= 𝐿/𝑇.

 • Figure 2 is a plot of the water surface amplitude with reference to the elevation of the wave trough
 −𝜂𝑡 as a function of dimensionless horizontal distance 𝑥/𝐿.

 Thus, 𝜂−−𝜂𝑡 = 𝜂+ 𝜂𝑡.



###### • From Figure 2, with the value of 𝑘[2] we can define the complete surface profile relative to the still
 water line.

 • Note that when 𝑘[2] is near zero the surface profile is nearly sinusoidal, whereas when 𝑘[2] is close to
 unity the profile has a very steep crest and a very flat trough with the ratio of crest amplitude to wave


-----

###### Figure 1. Solution for basic parameters of cnoidal wave theory. (Modified from Wiegel, 1964.)


-----

###### Figure 2. Cnoidal wave theory surface profiles. (Modified from U.S. Army Coastal Engineering Research Center, 1984.)


-----

###### 3. A wave having a period of 14 s and a height of 2 m is propagating in water 4 m deep. Using cnoidal wave theory determine the wave length and celerity and compare the results to the small-amplitude theory. Also plot the wave surface profile.


###### Solution:

 To employ Figure 1 we need

 and

 This gives

 And


###### 𝑘[2] = 1 −10[−5.3]

 𝑈𝑟 = 300


-----

###### So the cnoidal theory is quite appropriate for this wave condition. From the Ursell number the wave length is

 (4)[3]300 𝐿= = 98.0 m
 2


###### And

 𝐶= 98.0/14 = 7.0 m/s

 Since 𝑑/𝐿= 4/98 this is a shallow water wave. Using small-amplitude wave theory we have

 𝐶= 9.81(4) = 6.26 m/s

 and

 𝐿= 6.26(14) = 87.6 m


-----

###### yielding smaller values of C and L for a given 𝐻, 𝑇, 𝑎𝑛𝑑𝑑.

 • With the value of 𝑘[2] and the wave length and height, the surface profile can be determined from
 Figure 2. A plot of the surface profile (with a 10: 1 vertical scale exaggeration) is:

 • Note that the ratio of the crest amplitude to the wave height for this wave is 0.86


-----

-----

## Solitary Waves



#### • A solitary wave has a crest that is completely above the still water level,
 and no trough.

 • It is the wave that would be generated in a wave flume by a vertical paddle
 that is pushed forward and stopped without returning to the starting position.



#### • The water particles move forward as depicted in Figure 3 and then come to
 rest without returning to complete an orbit. Thus, it is a translatory rather than an oscillatory wave.

 • It has an infinite wave length and period.



#### • The surface profile is depicted by Figure 2 as the limit as 𝑘[2] approaches
 unity.


-----

###### Figure 3. Surface profile and particle paths for a solitary wave.


-----

###### As a long period oscillatory wave propagates in very shallow water of decreasing depth, the surface profile approaches the solitary wave form.

 • But the wave will break before a true solitary form is reached.

 • The cnoidal wave theory would still be most appropriate for these very long oscillatory waves in shallow water.

 • However, owing to the complexity of cnoidal theory, solitary wave theory has been used by some investigators to
 calculate wave characteristics in very shallow relative water depths.

 • Munk (1949) and Wiegel (1964) present good summaries of the most common forms of solitary wave theory.

 • As 𝑘[2] approaches unity the cnoidal theory surface profile becomes

 3𝐻 𝜂= 𝐻sech[2] 16
 4𝑑[3][ 𝑥−𝐶𝑡]

 • which defines the profile of a solitary wave. The wave celerity is commonly given by


###### 𝐶= 𝑔𝑑1 + [𝐻] 17
 2𝑑


-----

##### g q ( ) p y
 celerity.

 • Thus, at incipient wave breaking (say 𝐻/𝑑= 0.9) the solitary wave theory celerity
 will be 45% greater than the small-amplitude wave theory celerity assuming shallow water conditions.



##### • As a solitary wave approaches, water particles begin to move forward and
 upward as depicted in Figure 3.

 • As the wave crest passes the particle velocity ismhorizontal throughout the water
 column and reaches its highest value.



##### • Then the particles move downward and forward at decreasing speed until the
 wave passes.

 • The most commonly used equations for the horizontal and vertical components
 of water particle velocity in a solitary wave are from McCowan (1891).


-----

###### • They are

 𝑢= 𝑁𝐶

 𝑤= 𝑁𝐶

 • where the coefficients 𝑁 and 𝑀 are defined by


###### 1 + cos 𝑀 [𝑧+ 𝑑] cosh [𝑀𝑥]
 𝑑 𝑑
 cos 𝑀 [𝑧+ 𝑑] + cosh [𝑀𝑥]
 𝑑 𝑑


###### 18
2

###### 19
2



###### [ 𝐻] 20
 𝑑


###### 𝑁= [2]
 3 [sin][2][ 𝑀1 + 2]3


###### 𝐻
 𝑑


-----

###### water surface elevation above the still water level from 𝑥= minus to plus infinity (letting 𝑡= 0).

 • For a unit width along the wave crest this yields the following volume of water:
 1/2
 16 𝑉= 21
 3 [𝑑][3][𝐻]



###### • Since the period of a solitary wave is infinite it is not possible to determine a mass transport in terms of a
 mass per unit time.

 • Using the solitary wave theory, however, the mass transport can be estimated by dividing the water mass
 represented by Eq. (21) by the period of the wave in question.

 • A solitary wave also has its energy divided approximately half as potential energy and half as kinetic energy.

 • The total energy for a unit crest width is given by


###### 8 𝐸=
 3 3


###### 3
 𝜌𝑔(𝐻𝑑)2 22



###### • Since the length is infinite it is not possible to determine an energy density for a solitary wave.


-----

##### p (,,, )
 Using solitary wave theory calculate the wave celerity and compare it to the results from that example. Also, calculate the crest particle velocity and compare it with the results from the small-amplitude wave theory.


###### Solution:

 From Eq. (17) the wave celerity is

 𝐶= 9.81(4)(1 + 2/4(2)) = 7.8 m/s

 which compares to 6.3 m/s and 7.0 m/s for the small-amplitude and cnoidal wave theories, respectively.

 Given 𝐻= 2 m and 𝑑= 4 m, Eqs. (20) can be solved simultaneously by trial and error to yield

 𝑀= 0.88
 𝑁= 0.57

 Then, with 𝐶= 7.8 m/s, 𝑧= 2 m, 𝑥= 0 we have for the particle velocity at the wave crest

 𝑢𝑐 = 0 57(7 8) [1 + [cos(0.88)6/4]cosh(0.88)(0)/4]


-----

###### or

 𝑢𝑐 = 1.98 m/s

 for the small-amplitude wave theory in shallow water

 9.81
 𝑢𝑐 = [2] (1) = 1.6 m/s
 2 4

 Thus, in shallow water there is a significant difference between the results from the two theories. For this wave the true value lies between the two results, but is probably closer to the result given by the solitary wave theory.


-----

##### g p p y g q y
 breaking, one can derive a limiting value of H/d for wave breaking in shallow water.

 • This has produced values ranging from 0.73 to 0.83 with a most common value of
 0.78 (see Galvin, 1972).

 • Thus, neglecting the bottom slope because solitary wave theory is developed for a
 horizontal bottom, the relationship 𝐻/𝑑= 0.78 should well define shallow water breaking conditions.

 • Note that this is the limit used in Fig. 4.


-----

###### Figure 4. Recommended wave theory selection. (Based on LeMehaute, 1969.)


-----

## Stream Function Numerical Waves



##### • The foregoing finite-amplitude analytical wave theories are somewhat deficient
 in satisfactorily defining wave characteristics for waves of large steepness.

 • In addition, they are generally limited to a range of relative water depths. The use
 of numerical techniques with a computer has provided wave theories that have overcome these difficulties.



##### • Another limitation is introduced, however.

 • Rather than producing equations (however complex) that can be used to
 calculate wave characteristic for any 𝐻, 𝑇, and 𝑑 condition, the numerical theories directly produce and tabulate solutions for selected 𝐻, 𝑇, and 𝑑 values.



##### • Application of these results for conditions other than those selected by the
 practicing engineer requires interpolation between tabulated results.


-----

###### • The numerical wave theory most used in practice is the stream function theory developed by Dean (1965).

 • Dean uses the stream function 𝜓 rather than the velocity potential function to define the wave field in his numerical
 theory.

 • Wave motion is first converted to steady flow by subtracting the wave celerity from the horizontal motion in the wave.

 • Thus, the free surface profile and the bottom become steady-state stream lines and the stream function becomes constant
 along these two surfaces.

 • The boundary value problem is to seek a solution of the Laplace equation

 𝜕[2]𝜓
 23
 𝜕x[2][ + 𝜕]𝜕𝑧[2][𝜓][2][ = 0]

 • for the steady-state surface and bottom boundary conditions written in terms of the stream function. These become

 𝜕𝜓
 (24) 𝜕x [= 0][ at][ 𝑧= −𝑑]

 𝜕𝜓 𝜕𝜓
 𝜕x [=] 𝜕𝑧 [−𝐶𝜕𝜂]𝜕𝑥 [at][ 𝑧= 𝜂] (25)


###### 𝜕𝜓 +
 𝜕


###### 1 2


###### 𝜕𝜓
 −𝐶 𝜕


2


2


###### + 𝑔𝜂= 𝑄 at 𝑧= 𝜂 (26)


-----

###### where 𝑄 is the total energy with respect to the still water surface elevation, 𝑢 𝛿𝜓/𝛿𝑧, and 𝑤 𝛿𝜓/𝛿𝑥

 • The stream function for the small-amplitude wave theory is


###### 𝜓= [𝑔𝐻]
 2𝜎


###### sinh 𝑘(𝑑+ 𝑧)
 cos 𝑘𝑥−𝜎𝑡 27 cosh 𝑘𝑑



###### • which defines the streamline pattern in a wave with respect to both position and time. If a steady uniform
 horizontal flow is added we have


###### 𝜓= 𝐶𝑧+ [𝑔𝐻]
 2𝜎


###### sinh 𝑘(𝑑+ 𝑧)
 cos 𝑘𝑥 28 cosh 𝑘𝑑



###### • which is the steady flow streamline pattern.

 • Since the surface profile is a streamline, with Dean's theory the measured surface profile for a nonlinear wave can
 be used to calculate the related wave characteristics.

 • Also, the classic wave problem of calculating the wave characteristics given the wave height and period and the
 water depth can be solved.

 Th l tt h i di d i th t lid


-----

###### solution to the 𝑁th order that had the following form:

𝑁


###### 𝜓= 𝐶𝑧+ ෍

𝑛=1


###### 𝑋𝑛 sinh 𝑛𝑘𝑑+ 𝑧cos 𝑛𝑘𝑥 29



###### • for the stream line pattern in a wave. From Eq. (3.29), the streamline at the surface 𝜓𝑠 would be

𝑁

###### 𝜓𝑠 = 𝐶𝜂+ ෍ 𝑋𝑛 sinh 𝑛𝑘𝑑+ 𝜂cos 𝑛𝑘𝑥 30

𝑛=1

###### • Since the surface is a streamline, Eq. (30) exactly satisfies the Laplace equation, the BBC [Eq. (24)], and the KSBC

 [Eq. (25)].

 • The basic problem is to evaluate the coefficient 𝑋𝑛 to the order desired, the wave number 𝑘, and the value of 𝜓𝑠 so
 that they best satisfy the DSBC [Eq. (26)].

 • This is accomplished by evaluating the constant 𝑄 in the DSBC at a number of points along the wave.

 • Then, by trial, the square of the difference of each 𝑄 value from the average 𝑄 value for these points is minimized.

 Th l f t b d b l th till t l l [ i E (30)] t l b l


-----

-----

## Wave Theory Application

###### • When the various wave theories are to be applied in engineering practice two important concerns

 must be addressed.

 • The first is which theory to use for a particular application.

 • The second is how to apply one or more theories over a range of relative water depths to analyze

 the change in wave characteristics as a wave propagates from one water depth to another.


-----

-----

###### • Even if the input values of 𝐻, 𝑇, and 𝑑 are fairly precisely known, the calculated wave characteristics may
 only need to be approximately known thus the advantage of small-amplitude wave theory again.

 • However, if it were necessary to calculate the surface profile of a wave in relatively shallow water, say to
 determine the loading on the underside of a pier deck, cnoidal or stream function wave theory would be more appropriate.

 • Or, if the surface profile of a wave was being measured in a field experiment on wave forces on a pile
 structure, the stream function theory might be more appropriate for calculating the wave particle velocity and acceleration fields for that surface profile.

 • Another factor that compounds the choice of a wave theory for a particular application is that a particular
 theory may be better at defining some characteristics than others.

 • For example, in fairly shallow water, the small-amplitude wave theory does well at predicting bottom particle
 velocities, but does not do well at predicting particle velocities near the surface or the surface profile itself.


-----

###### ranges of application of the various wave theories.

 • These recommendations are based on several factors including the range of conditions for which the theory was
 derived, results of experiments on the efficacy of the various theories in predicting certain wave characteristics, ease of application of the theories, and some personal judgment.

 • Figure 4, based on a diagram originally presented by LeMehaute (1969) but with slight modification by the author,
 can be used as a starting point in selecting a wave theory for an engineering application.

 • It is a plot of wave steepness versus relative depth with breaking wave cutoff limits in deep and shallow water.

 • The general areas for use of each theory are denoted with the stream function theory application range defined by
 the cross-hatched area.

 • The application range for small-amplitude wave theory is extended as far as reasonable owing to its ease of
 application.

 • The Stokes fifth-order theory is specified where LeMehaute recommends the third- and fourth-order theories for
 increasing wave steepnesses.

 • The solitary wave theory is not shown but, depending on the wave characteristics to be calculated, it may be used
 in place of the cnoidal theory for very steep waves in shallow water.


-----

###### Shoaling Calculations


-----

###### breaking characteristics.
 (Walker and Headland,
 1982.)


-----

##### g p g p g g
 refraction and breaks on a beach slope of 1: 20. Determine the wave height and water depth just before the wave breaks.


###### Solution:

 From the small-amplitude wave theory

 So


###### 𝐿0 = [9.81(11)][2] = 188.9 m
 2𝜋


###### 𝐻o[′]
 𝐿0


###### 4
 188.9 [= 0.021]


###### Figure 5 then yields (for 𝑚= 0.05 and 𝐻o[′] /𝐿o = 0.021 )

 𝐻
 ′ [= 1.4]
 𝐻 0
 𝑑
 = 0.024
 𝐿0


-----

###### Thus, the wave height at breaking

 and the water depth at breaking


###### 𝐻𝑏 = 1.4(4) = 5.6 m

 𝑑𝑏 = 0.024(188.9) = 4.5 m


###### The solitary wave theory could then be used to estimate some of the other characteristics of this wave just before it breaks.


-----

