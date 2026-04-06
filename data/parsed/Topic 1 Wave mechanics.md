# Linear wave Theory

#####  Real water waves propagates in a viscous fluid over an irregular bottom of

 varying permeability.

  However the main body of the fluid is irrotational.


-----

#####  WHY ?

  Because viscous effects are usually concentrate in thin boundary layers near the

 surface and bottom.

  Since water can also be considered reasonably incompressible, a velocity

 potential & stream function should exist for wave.


-----

# BOUNDARY VALUE PROBLEMS (BVP)

#####  The formulation of BVP is simply the expression of a physical solution in

 mathematical form such that a unique solution exists.

  Steps

  Establishing a region of interest.

  Specifying a differential equation that must be satisfied within the region.


-----

#####  Selecting one or more solutions out of infinite number of solutions relevant

 to physical problem under investigation. This is done using the Boundary

 Conditions(BC), i.e rejecting those solutions that are incompatible with these

 conditions.

  In addition to spatial (geometric) BC, temporal (initial condition) BC should be

 specified.


-----

##### Under the assumption of irrotational motion and incompressible fluid a

 velocity potential exist which satisfies continuity equation

 𝛁. 𝐔= 𝟎 (1.a)

 OR 𝛁. 𝛁ϕ = 0 (1.b)

 Giving

###### 𝝏[𝟐]𝝋 𝝏[𝟐]𝝋 𝝏[𝟐]𝝋

##### 𝜵[𝟐]𝝋= (2)

###### [𝟐] [+] [𝟐] [+] [𝟐]


-----

#####  For flows that are non-divergent and irrotational Laplace equation also applies to
 stream function.


###### 𝝏𝒘
 𝝏𝒙 [−]


###### 𝝏𝒖

##### (3.a)
###### 𝝏𝒛 [=][ 0]


##### Since u= −


###### 𝝏[𝟐]𝝍
 𝝏𝒙[𝟐] [+]


###### 𝝏[𝟐]𝝍

##### (3.b)
###### 𝝏𝒛[𝟐] [= 0]


-----

##### Above equation must hold throughout the fluid.

  Question what if the flow was frictionless but rotational what could be the
 equation (3.b) look like?

  Answer

###### 𝛻[2]𝜑= 𝜔 (4)
 Vorticity


##### 


##### 


-----

#####  Velocity potential can be defined for 2D and 3D whereas the definition

 of the stream function is such that it only can defined for 2D and 3D if

 and only if the flow is symmetric about an axis i.e is mathematically

 2D.

  Laplace equation is linear i.e involves no products and thus has a

 valuable property of superposition.

  If 𝝓𝟏 𝒂𝒏𝒅𝝓𝟐 each satisfy Laplace equation then 𝝓𝟑=A𝝓𝟏+B𝝓𝟐 also

 satisfies Laplace equation.


-----

# KINEMATIC BOUNDARY CONDITIONS(KBC)

#####  At any boundary (whether fixed or free) certain physical conditions must be satisfied

 by fluid velocities. These conditions on water particle kinematics are called kinematic

 boundary conditions.

  At any surface or fluid interface there must be no flow across the interface :

 otherwise there would be no interface.

 quite obvious in case of an impermeable fixed surface like sea wall.

  Mathematical expression for KBC may be derived from the equation which

 describes the surface that constitutes the boundary.


-----

# HOW?

#####  Any moving or fixed surface is written as

 F(x, y, z, t) = 0

 Example: sphere?? (of radius a)

 F(x, y, z, t)= 𝒙[𝟐] + 𝒚[𝟐]+ 𝒛[𝟐] −𝒂[𝟐]= 0


-----

##### For such surface to represent an interface the total derivative or material derivative of the

 surface would be zero on surface.

###### 𝑫𝑭 𝝏𝑭 𝝏𝑭 𝝏𝑭 𝝏𝑭

##### (5.a)

###### 𝑫𝒕 [=] 𝝏𝒕 [+ 𝒖] 𝝏𝒙 [+ 𝒗] 𝝏𝒚 [+ 𝒘] 𝝏𝒛 [= 𝟎]

##### on F=0 (surface)
 Or

###### −𝝏𝑭

##### (5.b)
###### 𝝏𝒕 [= ഥ𝑼. 𝜵𝑭]


-----

##### If we define unit vector normal to the surface such as n=

 written as


###### 𝜵𝑭 𝜵𝑭 [Eq. (5.b) can be ]


##### U.n =


###### −𝝏𝑭

##### (5.c)
###### 𝝏𝒕 [= ഥ𝑼. 𝒏𝜵𝑭]

##### Or

###### −𝝏𝑭
 𝝏𝒕 on  F(x, y, z, t)=0 (6)
 𝜵𝑭


-----

##### here

###### 𝟐 𝟐 𝟐
 𝝏𝑭 𝝏𝑭 𝝏𝑭

##### 𝜵𝑭 = + +

###### 𝝏𝒙 𝝏𝒚 𝝏𝒛

#####  This condition requires that (u.n) fluid velocity normal to surface be related to

###### 𝝏𝑭

##### local velocity of surface (

###### 𝝏𝒕[)]

#####  If surface do not move with respect to time i.e u.n = 0 or velocity component

 normal to surface is zero.


-----

# Bottom Boundary Condition (BBC)

#####  Bottom described as z=-h(x) for 2D case where origin is located at still water level(SWL) &

 h represents depth.

  Since bottom is fixed U.n=0

  Here F(x,z) = z+h(x)=0 (7)

 &

 u.n = 0

###### U= u Ƹ𝒊+ w𝒌[෡]


###### 𝝏𝑭
 = 𝝏𝒛 [෡𝒌]


###### 𝝏(𝒛+𝒉𝒙)
 Ƹ𝒊 + 𝝏𝒙


###### 𝝏(𝒛+𝒉𝒙)
 ෡𝒌 𝝏𝒛


###### 𝜵𝑭=


###### 𝝏𝑭
 𝝏𝒙 [Ƹ𝒊+]


-----

###### 𝝏𝒉

##### 𝜵𝑭 =

###### 𝝏𝒙 [Ƹ𝒊] [+ 1. ][෡𝒌=]


###### 𝝏𝒉 𝝏𝒙 [Ƹ𝒊][+ ][෡𝒌]


##### n=


###### 𝜵𝑭 𝜵𝑭 [=]


###### 𝒅𝒉

##### u.n = u on z=-h(x) (9.a)

###### 𝒅𝒙 [+ 𝐰][=0]

 𝒅𝒉

##### Or W= -u on z=-h(x) (9.b)


##### Special case of horizontal bottom


###### 𝝏𝒉 𝝏𝒙 [= 𝟎]

 W = 0


-----

##### For sloping bottom

###### 𝒘 𝒅𝒉

##### (10)

###### 𝒖 [= −] 𝒅𝒙

#####  Question?? Could we treat bottom as a streamline?

 Yes since flow is everywhere tangential to it

  Bottom BC (Eq. 7) also applies to flows in 3D in which h is h (x,y)


-----

#####  Kinematic Free surface Boundary Condition (KFSBC)

  Free surface of wave is written as

 F(x, y, z, t) = z- η(x, y, t)=0

 Here η(x, y, t) is displacement of free surface about horizontal plane z=0


-----

###### 𝝏η
 𝝏𝒚 [Ƹ𝒋+ ෡𝒌]


###### 𝝏𝑭

##### 𝜵F=

###### 𝝏𝒙 [Ƹ𝒊+]


###### 𝝏𝑭 𝝏𝒚 [Ƹ𝒋+]


###### 𝝏𝑭
 𝝏𝒛 [෡𝒌=]


###### −𝝏η

##### Ƹ𝒊−
###### 𝝏𝒙


##### 𝜵F = 𝟏+

 U= u Ƹ𝒊 + v Ƹ𝒋 + w𝒌[෡]

###### −𝒖[𝝏][η]
 𝝏𝒙 [−𝒗][𝝏]𝝏𝒚[η]

##### u.n =


##### (11.a)
###### 𝟐


-----

##### Using eqn (6) u.n=


###### −[𝝏𝑭]
 𝝏𝒕


##### z= η(x, y, t)


-----

# Dynamic Free surface Boundary Condition
 (DFSBC)

#####  BC for fixed surfaces are easy to prescribe as they are applied on known surface.

 The displacement of upper boundary in free surface problem is not known a priori

 in water wave problem.

  Fixed surface can support pressure variations across interface whereas free surface

 cannot.


-----

#####  Another BC is hence required on any free surface or interface to prescribe

 pressure distribution on the boundary. This is called Dynamic Boundary

 Condition.

  The DFSBC requires that the pressure on free surface be uniform along the wave

 form. Thus, unsteady Bernoulli’s equation is applied on free surface Z= η(x, t).


-----

###### 𝟏 𝟐 [𝒖][𝟐] [+ 𝒘][𝟐] [+]


###### 𝒑𝒏

##### (12)
###### 𝝆 [+ 𝒈𝒛= 𝒄(𝒕)]


##### −


###### 𝝏𝝓
 𝝏𝒕 [+]


##### 𝒑𝒏 is constant and usually taken as gauge pressure 𝒑𝒏 = 0

 Class problem

 If wave length are very short (order of several cm) that the surface is no

 longer “free”. Write DFSBC for this case where surface tension T is important.


###### 𝑻

##### Use σ̕=

###### 𝒍[(surface tension per unit length).]


-----

##### Solution
 consider a surface for which curvature exists as shown below

###### 𝑝𝑛 T
 p

 α
 T
 x+ Δx
 x

##### Denoting p as the pressure under the free surface a free body analysis in vertical

 direction gives
###### T −𝒔𝒊𝒏 α + 𝒔𝒊𝒏 α + (p-𝒑𝒏)Δx + terms of Δ𝒙[𝟐]=0

 x         x+Δx
 𝝏η

##### Here 

###### 𝝏𝒙 [≈𝒔𝒊𝒏𝜶]


-----

##### Expanding using Taylor series and allow Δx 0

 𝐏= 𝒑 −�̕ [𝝏][𝟐][η]
###### 𝒏

##### 𝝏𝒙[𝟐]

 Hence DFSBC becomes


###### 𝟏 𝟐


##### at z= η(x, t)
###### 𝝏𝒙[𝟐] [+ 𝒈𝒛= 𝒄(𝒕)]


##### −


###### 𝝏𝝓
 𝝏𝒕 [+]


-----

# Lateral Boundary Conditions

#####  Until now we have discussed BC for bottom and upper surfaces.

  Conditions must also be specified or remaining lateral boundaries.

  If waves are propagating in x directions  no flow in y directions is

 lateral BC.

  In x direction if motion occurs due to a paddle or wave maker then

 usual kinematic BC applied.


-----

##### Consider a vertical paddle. If displacement of paddle is described as x=s(z, t) find KBC.

###### x=s(z, t)

#####  For waves that are periodic in space and time the BC is expressed as

 φ(x,t)= φ(x+L,t) (13.a)

 φ(x,t)= φ(x,t+T) (13.b)


-----

# Velocity potential derivation assumptions

##### The assumptions in deriving the expression for the velocity potential due to

 propagating ocean waves are;

 • Flow is said to be irrotational

 • Fluid is ideal

 • Surface tension is neglected

 • Pressure at the free surface is uniform and constant

 • The seabed is rigid, horizontal and impermeable


-----

# Velocity potential derivation assumptions

##### • Wave height is small compared to its length

 • Potential flow theory is applicable

 • A velocity potential 𝝓 exists and the velocity components u and 𝒘 in


##### the x and z directions can be obtained as


###### 𝝏𝝓 𝝏𝝓
 𝝏𝒙 [and ] 𝝏𝒛 [.]


-----

# DERIVATION FOR VELOCITY POTENTIAL

##### The governing equation is the Laplace Equation given by
 𝜵[𝟐]𝝓= 𝟎 (2.1)
 The continuity equation and Bernoulli’s equations (2.2) and (2.3) are used in the solution procedure


###### 𝝏𝒖 𝝏𝒙 [+]


###### 𝝏𝒗 𝝏𝒚 [+]


###### 𝟏 𝟐 [𝒖][𝟐][+𝒗][𝟐][+𝒘][𝟐] [+]


###### 𝒑
##### (2.3)
###### 𝝆 [+ gz =0]


##### 

###### 𝝏𝝓
 𝝏𝒕 [+]


-----

##### BOUNDARY CONDITIONS:

 • The equation (2.1) is to be satisfied in the region −𝒅≤𝒛≤𝜼, −∞≤𝒙≤∞ where 𝜼

 is the water surface elevation measured from the Still Water Level (SWL).

 • The kinematic bottom boundary condition meaning, that the vertical velocity

 component at the sea bottom is zero. Since ‘z’ is negative in downward from SWL.

 • The pressure at the free surface is zero or at z= 𝜼


-----

#### −


##### Linearizing the Bernoulli’s equation results in

###### 𝝏𝝓 𝒑

#### (2.4)

###### 𝝏𝒕 [+ ]𝝆 [+ gz =0]



##### • When z= 𝜼 and taking 𝒑 = 0 using equation (2.4) we get


###### 𝝏𝝓
 𝝏𝒕𝒛=𝜼


##### 𝜼=


###### 𝟏
 𝒈



##### • This is the dynamic free surface boundary condition. Since we assume that

 amplitude of the waves are small, the above equation can be written as


-----

###### 𝝏𝝓

##### (2.5)
###### 𝝏𝒕𝒛=𝟎


##### 𝜼=


###### 𝟏
 𝒈


###### 𝑯
 𝑳[<1 .The definition]


##### This is applicable only when 𝜼 is small and valid for


###### 𝑯
 𝒅 [and]


##### sketch is given in Fig.2.2. With the above boundary conditions, the solution to

 eqn. (2.1) is solved


-----

##### Fig. 2.2 Definition sketch for wave motion


-----

# SOLUTION TO THE LAPLACE EQUATION:

###### 𝝏[𝟐]𝝓 𝝏[𝟐]𝝓

##### (2.6)

###### 𝝏𝒙[𝟐] [+] 𝝏𝒛[𝟐] [= 0]

##### • Method of separable is used to obtain the solution to Eqn. (2.6)

 • Let us assume

 𝝓𝒙, 𝒛, 𝒕 =𝑿𝒙[ഥ] 𝒁𝒛[ഥ] 𝑻𝒕[ഥ] (2.7)


-----

##### • Substituting Eq. (2.7) in Eq. (2.6) we get

 𝑿′′ [ഥ]𝒁𝑻[ഥ] + 𝑿𝒁′′[ഥ] 𝑻[ഥ] =0

 • Where each prime denotes differentiation once with respect to the

 particular independent variable.

 • Dividing both side of the above 𝑿[ഥ]𝒁[ഥ]𝑻[ഥ] gives


###### ഥ𝑿[′′]
 ഥ𝑿 [= ]


###### ഥ𝒁


-----

##### • Let this be constant = -𝒌[𝟐] ; then

 𝑿′′+𝒌[𝟐]𝑿[ഥ]=0 (2.8)

 𝒁′′ −𝒌[𝟐]𝒁[ഥ]=0 (2.9)

 ഥ 𝑿 = Acoskx + Bsinkx

 ഥ𝒁 = C𝒆[𝒌𝒛] + 𝑫𝒆[−𝒌𝒛]

 Hence 𝝓𝒙, 𝒛, 𝒕 = Acoskx + Bsinkx C𝒆[𝒌𝒛] + 𝑫𝒆[−𝒌𝒛] 𝑻𝒕[ഥ]


-----

##### • The solutions to ɸ are simple harmonic in time requiring 𝑻𝒕[ഥ] be replaced as

 𝒄𝒐𝒔𝝈𝒕 or 𝒔𝒊𝒏𝝈𝒕, thus leading to four forms of solutions to ɸ, such that

 • 𝝓𝟏 =𝑨𝟏 C𝒆[𝒌𝒛] + 𝑫𝒆[−𝒌𝒛] 𝒄𝒐𝒔𝒌𝒙. 𝒄𝒐𝒔𝝈𝒕

 • 𝝓𝟐 =𝑨𝟐 C𝒆[𝒌𝒛] + 𝑫𝒆[−𝒌𝒛] 𝐬𝒊𝒏𝒌𝒙. 𝒔𝒊𝒏𝝈𝒕

 • 𝝓𝟑=𝑨𝟑 C𝒆[𝒌𝒛] + 𝑫𝒆[−𝒌𝒛] 𝐬𝒊𝒏𝒌𝒙. 𝒄𝒐𝒔𝝈𝒕

 • 𝝓𝟒=𝑨𝟒 C𝒆[𝒌𝒛] + 𝑫𝒆[−𝒌𝒛] 𝒄𝒐𝒔𝒌𝒙. 𝐬𝒊𝒏𝝈𝒕


-----

# DETERMINATION OF THE CONSTANTS:

##### The constants are determined by using the dynamic free surface boundary condition

 and the kinematic bottom boundary condition.

 Considering 𝝓𝟐

 𝝓𝟐 =𝑨𝟐 C𝒆[𝒌𝒛] + 𝑫𝒆[−𝒌𝒛] 𝐬𝐢𝐧𝒌𝒙. 𝐬𝐢𝐧𝝈𝒕 (2.10)


-----

##### • Applying the kinematic bottom boundary condition

###### 𝝏𝝓

##### i.e., 

###### 𝝏𝒛 [= 0 at z = -d]

 𝝏𝝓𝟐ቚ
 𝝏𝒛 𝒛=−𝒅 [= ][𝑨][𝟐] [C][𝒌𝒆][−𝒌𝒅] [−] [𝑫𝒌𝒆][𝒌𝒅] [𝐬𝒊𝒏𝒌𝒙. 𝒔𝒊𝒏𝝈𝒕] [= 0]


##### 𝑨𝟐 ≠ 0; 𝐬𝒊𝒏𝒌𝒙. 𝒔𝒊𝒏𝝈𝒕≠ 0 [since velocity potential exists]

### ∴ 𝑪= 𝑫𝒆[𝟐𝒌𝒅]


-----

##### Substituting for C in (Eq. 2.10) and simplifying,

###### 𝒆[𝒌(𝒅+𝒛)] +𝒆[−𝒌(𝒅+𝒛)]
##### 𝝓𝟐= 2𝑨𝟐𝑫𝒆[𝒌𝒅] 𝐬𝒊𝒏𝒌𝒙. 𝒔𝒊𝒏𝝈𝒕

###### 𝟐

##### 𝝓𝟐= 2𝑨𝟐𝑫𝒆[𝒌𝒅]𝒄𝒐𝒔𝒉𝒌(𝒅+ 𝒛) 𝐬𝒊𝒏𝒌𝒙. 𝒔𝒊𝒏𝝈𝒕 (2.11)


-----

##### • 𝝏𝝓𝟐ቚ

###### 𝝏𝒕 𝒛=𝟎 [= ][𝟐𝑨][𝟐][𝑫𝝈𝒆][𝒌𝒅] [. 𝐜𝐨𝐬𝐡𝐤𝐝. 𝐬𝒊𝒏𝒌𝒙. 𝒄𝒐𝒔𝝈𝒕]

##### On assuming

 • 𝜼= 𝒂𝐬𝒊𝒏𝒌𝒙. 𝒄𝒐𝒔𝝈𝒕 where a = wave amplitude =

 surface boundary condition 𝜼= 𝟏 𝝏𝝓𝟐ቚ [we get]


###### 𝑯

##### and applying the free
###### 𝟐


-----

##### • 𝒂𝐬𝒊𝒏𝒌𝒙. 𝒄𝒐𝒔𝝈𝒕 = 𝟐𝑨𝟐𝑫𝝈𝒆[𝒌𝒅] . 𝐜𝐨𝐬𝐡𝐤𝐝. 𝐬𝒊𝒏𝒌𝒙. 𝒄𝒐𝒔𝝈𝒕

###### 𝒈

 𝒂𝒈 𝟏

##### 𝟐𝑨𝟐𝑫𝒆[𝒌𝒅] =

###### 𝝈 𝒄𝒐𝒔𝒉𝒌𝒅 [.]

##### Substituting in eq. (2.11), we get


##### 𝝓𝟐 =


##### 𝐬𝐢𝐧𝒌𝒙. 𝐬𝐢𝐧𝝈𝒕 (2.12)
###### 𝐜𝐨𝐬𝐡𝐤𝐝


##### Let us consider 𝝓𝟑


-----

##### 𝝓𝟑=𝑨𝟑 C𝒆[𝒌𝒛] + 𝑫𝒆[−𝒌𝒛] 𝐬𝒊𝒏𝒌𝒙. 𝒄𝒐𝒔𝝈𝒕 (2.13)

 • Applying the kinematic bottom boundary condition

 • 𝝏𝝓𝟑ቚ

###### 𝝏𝒛 𝒛=−𝒅 [=][𝑨][𝟑] [C][𝒌𝒆][−𝒌𝒅] [−] [𝑫𝒌𝒆][𝒌𝒅] [𝐬𝒊𝒏𝒌𝒙. 𝒄𝒐𝒔𝝈𝒕] [= 0]



##### • 𝑨𝟑 ≠ 0; 𝐬𝒊𝒏𝒌𝒙. 𝒄𝒐𝒔𝝈𝒕≠ 0

 𝑪= 𝑫𝒆[𝟐𝒌𝒅]

 • Substituting for C in eq. (2.13)


-----

##### 𝝓𝟑= 2𝑨𝟑𝑫𝒆[𝒌𝒅]𝒄𝒐𝒔𝒉𝒌(𝒅+ 𝒛) 𝐬𝒊𝒏𝒌𝒙. 𝒄𝒐𝒔𝝈𝒕 (2.14)

 And

 • 𝝏𝝓𝟑ቚ

###### 𝝏𝒕 𝒛=𝟎 [= ][−𝟐𝑨][𝟑][𝑫𝝈𝒆][𝒌𝒅] [. 𝐜𝐨𝐬𝐡𝐤𝐝. 𝐬𝒊𝒏𝒌𝒙. 𝒔𝒊𝒏𝝈𝒕]



##### • On assuming  𝜼= 𝒂𝐬𝒊𝒏𝒌𝒙. 𝒔𝒊𝒏𝝈𝒕 and applying the free surface boundary condition

 we get


##### 𝟐𝑨𝟑𝑫𝒆[𝒌𝒅] =


###### 𝝈


###### 𝒄𝒐𝒔𝒉𝒌𝒅 [.]


-----

##### Substituting in eq. (2.14), we get


###### −𝒂𝒈

##### 𝝓𝟑 =

###### 𝝈

##### Let us consider 𝝓𝟒


##### 𝐬𝒊𝒏𝒌𝒙. 𝒄𝒐𝒔𝝈𝒕 (2.15)
###### 𝒄𝒐𝒔𝒉𝒌𝒅


##### 𝝓𝟒=𝑨𝟒 C𝒆[𝒌𝒛] + 𝑫𝒆[−𝒌𝒛] 𝒄𝒐𝒔𝒌𝒙. 𝒔𝒊𝒏𝝈𝒕 (2.16)

 Applying the kinematic bottom boundary condition


###### 𝝏𝝓𝟒ቚ
 𝝏𝒛 𝒛=−𝒅 [=][𝑨][𝟒] [C][𝒌𝒆][−𝒌𝒅] [−] [𝑫𝒌𝒆][𝒌𝒅] [𝒄𝒐𝒔𝒌𝒙. 𝒔𝒊𝒏𝝈𝒕]

##### Substituting for C in eq. (2.16)


##### 𝑪= 𝑫𝒆[𝟐𝒌𝒅]


-----

##### • 𝝓𝟒= 2𝑨𝟒𝑫𝒆[𝒌𝒅]𝒄𝒐𝒔𝒉𝒌(𝒅+ 𝒛) 𝒄𝒐𝒔𝒌𝒙. 𝒔𝒊𝒏𝝈𝒕 (2.17)

 And

 • 𝝏𝝓𝟒ቚ

###### 𝝏𝒕 𝒛=𝟎 [=][𝟐𝑨][𝟒][𝑫𝒆][𝒌𝒅][𝒄𝒐𝒔𝒉𝒌(𝒅+ 𝒛) 𝒄𝒐𝒔𝒌𝒙. 𝒔𝒊𝒏𝝈𝒕]


##### Assuming 𝜼= 𝒂𝒄𝒐𝒔𝒌𝒙. 𝒄𝒐𝒔𝝈𝒕 and applying eq (2.5)


###### 𝟏
 𝒄𝒐𝒔𝒉𝒌𝒅 [.]


##### We get 𝟐𝑨𝟒𝑫𝒆[𝒌𝒅] =


###### 𝒂𝒈
 𝝈


-----

##### • Substituting in eq. (2.17), we get


##### 𝒄𝒐𝒔𝒌𝒙. 𝒔𝒊𝒏𝝈𝒕 (2.18)
###### 𝒄𝒐𝒔𝒉𝒌𝒅


##### 𝝓𝟒 =


###### 𝒂𝒈
 𝝈



##### • Let us consider 𝝓𝟏

 𝝓𝟏 =𝑨𝟏 C𝒆[𝒌𝒛] + 𝑫𝒆[−𝒌𝒛] 𝒄𝒐𝒔𝒌𝒙. 𝒄𝒐𝒔𝝈𝒕 (2.19)

 • Applying the kinematic bottom boundary condition

 • 𝝏𝝓𝟏ቚ 𝑪= 𝑫𝒆[𝟐𝒌𝒅]

###### 𝝏𝒛 𝒛=−𝒅 [=][𝟎]


-----

##### • Substituting for C in eq. (2.19)

 • 𝝓𝟏= 2𝑨𝟏𝑫𝒆[𝒌𝒅]𝒄𝒐𝒔𝒉𝒌(𝒅+ 𝒛) 𝒄𝒐𝒔𝒌𝒙. 𝒄𝒐𝒔𝝈𝒕 (2.20)

 • assuming 𝜼= 𝒂𝒄𝒐𝒔𝒌𝒙. 𝒔𝒊𝒏𝝈𝒕 and applying equation (2.5)

 We get

###### −𝒂𝒈 𝟏

##### • 𝟐𝑨𝟏𝑫𝒆[𝒌𝒅] =

###### 𝝈 𝒄𝒐𝒔𝒉𝒌𝒅 [.]

##### • Substituting in eq. (2.20), we get


###### 𝒄𝒐𝒔𝒉𝒌(𝒅+𝒛)

##### 𝒄𝒐𝒔𝒌𝒙. 𝒄𝒐𝒔𝝈𝒕 (2.21)
###### 𝒄𝒐𝒔𝒉𝒌𝒅



##### • 𝝓𝟏 =


###### −𝒂𝒈
 𝝈


-----

##### • If 𝝓[+] = 𝝓𝟐-𝝓𝟏

###### 𝒂𝒈 𝒄𝒐𝒔𝒉𝒌(𝒅+𝒛)

##### =

###### 𝝈 𝒄𝒐𝒔𝒉𝒌𝒅


##### φ =


##### . 𝒄𝒐𝒔𝒌𝒙−𝝈𝒕. (2.22)
###### 𝒄𝒐𝒔𝒉𝒌𝒅



##### • This is the expression for the velocity potential for a propagating wave in

 a constant water depth


-----

##### Since 𝜼=

 𝜼=


###### 𝟏 𝝏𝝓

##### ቚ
###### 𝒈


###### 𝟏
 𝒈


###### 𝒂𝒈


##### Hence 𝜼 =𝐚𝒔𝒊𝒏𝒌𝒙−𝝈𝒕. (2.23)

 • ‘𝜂’ is periodic in x and t. If we locate a point and traverse along the wave,

 such that, at all-time ‘t’ our position relative to the wave form remains

 fixed then the phase difference is zero or 𝒌𝒙−𝝈𝒕 = constant


-----

##### • And the speed with which we must move to accomplish this is given by 𝒌𝒙= 𝝈𝒕+ constant


##### k


###### 𝒅𝒙
 𝒅𝒕 [= 𝝈]


###### 𝒅𝒙
 𝒅𝒕 [=]


###### 𝝈
 𝒌 [=]


###### 𝟐𝝅



##### • 𝑪=


###### 𝑳
##### (2.24)
###### 𝑻 [= CELERITY or Speed of the wave]


-----

# Wave moving in negative ‘x’ direction

##### • If 𝝓[−] = 𝝓𝟐 + 𝝓𝟏

###### −𝒂𝒈 𝒄𝒐𝒔𝒉𝒌(𝒌𝒙+𝝈𝒕)

##### = . 𝒄𝒐𝒔𝒌𝒙+ 𝝈𝒕.

###### 𝝈 𝒄𝒐𝒔𝒉𝒌𝒅

 𝟏 𝝏𝝓

##### • Since 𝜼= ቚ


##### 𝜼=


###### 𝟏
 𝒈


##### 𝜼 =𝐚𝒔𝒊𝒏𝒌𝒙+ 𝝈𝒕


-----

##### To obtain the celerity of the wave we have

 𝒌𝒙+ 𝝈𝒕 = constant


###### 𝒅𝒙
 𝒅𝒕 [=]


##### (2.25)
###### 𝑻 [= −𝑪]


-----

# DISPERSION RELATIONSHIP

##### • The relationship between wavelength, period and water depth is obtained as given

 below. The main assumption while establishing the relationship is that, since, we are

 dealing with small amplitude waves, meaning that the slope of the wave profile are


##### small so that

 w . This is


###### 𝒅𝜼
 𝒅𝒕 [can be approximately said as equal to the vertical component velocity,]


###### 𝝏𝜼
 𝝏𝒕 [+]


###### 𝝏𝜼 𝝏𝒙 [.]


###### 𝝏𝒕



##### • 𝒘=


###### 𝒅𝜼
 𝒅𝒕 [=]



##### • Wave slope being small by setting,


###### 𝝏𝜼 𝝏𝒙 [= 0]


-----

###### −𝝏𝝓


##### 𝒘=


###### 𝝏𝜼
 𝝏𝒕 [but][ 𝒘=]


##### (2.26)
###### 𝝏𝒛


##### Hence


###### 𝝏𝜼
 𝝏𝒕 [=]


##### Differentiating the expression of 𝜼 we get


##### ቚ
###### 𝒈 𝝏𝒕[𝟐]
 𝒛=𝟎


##### Hence


##### 𝒄𝒐𝒔𝒉𝒌𝒅. 𝒄𝒐𝒔𝒌𝒙−𝝈𝒕. (2.27)
###### 𝒈


-----

###### 𝒈 𝝈


###### 𝟏



##### • Where 𝐀=

 𝒘=


###### 𝑯



##### • Using the relation of Eq. (2.26), equating Eq. (2.27) to Eq (2.28), we get

###### 𝑨𝝈[𝟐]
 𝒈 [𝒄𝒐𝒔𝒉𝒌𝒅. 𝒄𝒐𝒔𝒌𝒙−𝝈𝒕= 𝐀𝐤. 𝐬𝐢𝐧𝐡𝐤𝐝. 𝒄𝒐𝒔𝒌𝒙−𝝈𝒕.]


-----

###### 𝐤𝒔𝒊𝒏𝒉𝒌𝒅
 𝐜𝐨𝐬𝐡𝐤𝐝



##### •


###### 𝝈[𝟐]
 𝒈 [=]



##### • 𝝈[𝟐] = 𝒈𝒌. 𝒕𝒂𝒏𝒉𝒌𝒅 (2.29)

###### 𝟐𝝅

##### • 𝝈:Wave angular frequency =

###### 𝑻 [and k: wave number = ]

##### • The above equation can be written as


##### = 𝒈


###### 𝟐



##### •


###### 𝟐𝝅
 𝑻


###### 𝟐𝝅

##### 𝒕𝒂𝒏𝒉𝒌𝒅
###### 𝑳


-----

##### =


###### 𝑳 𝑻


###### 𝟐


###### 𝒈𝑳 𝟐𝝅 [𝒕𝒂𝒏𝒉𝒌𝒅]

 𝒈
##### (2.30)
###### 𝒌 [𝒕𝒂𝒏𝒉𝒌𝒅]


##### 𝑪 [𝟐] =


##### The speed at which a wave moves in its direction of propagation as a function of water

 depth is given by Eq.(2.30)

 Since


##### 𝑪=


###### 𝑳 𝑻 [from the above equation we get]


-----

###### 𝒈𝑳

##### • 𝑪= (2.31)

###### 𝟐𝝅 [𝒕𝒂𝒏𝒉𝒌𝒅]

 𝒈𝑻[𝟐]

##### Or    𝐋= (2.32)

###### 𝟐𝝅 [𝒕𝒂𝒏𝒉𝒌𝒅]

##### • Since the unknown ‘L’ occurs on both sides (Implicit Eq.) of Eq. (2.32), it has

 to be solved by trial and error.


-----

# CELERITY IN DIFFERENT WATER DEPTH
 CONDITIONS:

##### Classification d/L 2𝜋d/L tanh(2𝜋d/L)

 Deep Waters >1/2 >𝝅 ~ 1

 Intermediate 1/20 to 1/2 𝜋/10 to 𝝅 tanh(2𝜋d/L) waters

 Shallow waters ≤1/20 0 to 𝜋/10 ~ 2𝜋d/L

 Classification of ocean waves according to water depth

|Classification|d/L|2𝜋d/L|tanh(2𝜋d/L)|
|---|---|---|---|
|Deep Waters|>1/2|>𝝅|~ 1|
|Intermediate waters|1/20 to 1/2|𝜋/10 to 𝝅|tanh(2𝜋d/L)|
|Shallow waters|≤1/20|0 to 𝜋/10|~ 2𝜋d/L|


-----

# Deep water conditions:

##### • In case of deep waters Eq (2.30) becomes

 𝒄𝟎 = 𝒈𝑳𝟎 since, tanhkd=1

###### 𝟐𝝅

##### and Eq (2.31) becomes


##### 𝒄 =
###### 𝟎

##### Or  𝑳𝟎 =


###### 𝒈𝑻
##### (2.33)
###### 𝟐𝝅

 𝒈𝑻[𝟐]

##### (2.34)
###### 𝟐𝝅


-----

##### That is when d/L ≥ 1/2, tanh(kd) approaches unity and the wave characteristics are

 independent of the water depth, d, while wave period remaining constant. Hence,


##### 𝑳 =
###### 𝟎

##### 𝑳 =
###### 𝟎


###### 𝒈𝑻[𝟐]

##### [FPS]
###### 𝟐𝝅 [= 5.12 ][𝑻][𝟐]

 𝒈𝑻[𝟐]

##### [MKS]
###### 𝟐𝝅 [= 1.56 ][𝑻][𝟐]



##### • If Eq (2.33) or(2.34) are used to compute wave celerity for shallow water conditions

 (d/L<1/20) and error of about 20% to 50% results. 


-----

# Shallow water conditions:


###### 𝝅 𝒅 𝟏

##### • When kd=

###### 𝟏𝟎 [, ] 𝑳 [≤] 𝟐𝟎

 𝒈𝑳

##### 𝑪[𝟐] =

###### 𝟐𝝅[.tanh(kd)]

##### • Hence tanh(kd)≈kd=2𝜋d/L 𝑪[𝟐] =


###### 𝟐𝝅𝒅

##### 𝑪[𝟐]= gd
###### 𝑳


##### C= 𝒈𝒅 (2.35)

 This relation shows that when a wave travels in shallow waters wave

 celerity depends only on the water depth.


-----

# Relationship between d/L and d/𝑳
#### 𝟎

##### • It can be shown by dividing the Eq.(2.31) by Eq.(2.33) and dividing Eq.

 (2.32) by Eq.(2.34) that     𝐶/𝑪𝟎 =𝐿/𝑳𝟎 =tanhkd

 Multiplying both sides by d/L, then

 𝑑/𝑳𝟎 =𝑑/𝐿tanhkd (2.36)

 The relation between 𝑑/𝐿 and 𝑑/ 𝑳𝟎 is given in the wave Tables


-----

-----

# LOCAL FLUID PARTICLE VELOCITIES AND ACCLERATION UNDER PROGRESSIVE WAVES

##### • In the evaluation of wave forces on offshore structures it is desirable to 
 know the fluid particle kinematics that is velocity and acceleration.

 We know


###### 𝒂𝒈

##### 𝝓 =

###### 𝝈


##### (2.37)
###### 𝒄𝒐𝒔𝒉𝒌𝒅 [cos(kx -σt)]



##### • The horizontal water particle velocity or orbital velocity u is given by


###### 𝒄𝒐𝒔𝒉𝒌(𝒅+𝒛)

##### (2.38)
###### 𝐜𝐨𝐬𝒉𝒌𝒅 [sin(kx -σt)]


##### u = −


###### 𝝏𝝓 𝒂𝒈
 𝝏𝒙 [= ] 𝝈 [𝒌]


-----

##### • The horizontal water particle velocity or orbital velocity, u is given by

###### 𝒂𝒈 𝒄𝒐𝒔𝒉𝒌(𝒅+𝒛)

##### = .tanhkd.sin(kx -σt)

###### 𝝈 [𝒌] 𝐬𝐢𝐧𝐡𝐤𝐝


###### 𝑯
 𝟐



##### • Substituting the relationship 𝑪[𝟐] =
 In the above expression we get


###### 𝒈 𝒌 [𝒕𝒂𝒏𝒉𝒌𝒅] [(2.30)    and a=]


##### U =


###### 𝑯
 𝟐𝝈 [𝒄][𝟐][𝒌][𝟐𝒄𝒐𝒔𝒉𝒌(𝒅+𝒛)]𝐬𝐢𝐧𝐡𝐤𝐝


-----

##### =


###### 𝑯 𝑳
 𝟐 [(]𝑻[)][𝟐𝟐𝝅/𝑳]𝟐𝝅/𝑻 [𝟐]


##### Simplifying we get,


##### U=


###### 𝝅𝑯
 𝑻


##### The vertical fluid particle velocity, w is given by


-----

###### 𝒔𝒊𝒏𝒉𝒌(𝒅+𝒛)

##### 𝐜𝐨𝐬(kx -σt) (2.40)
###### 𝐜𝐨𝐬𝒉𝒌𝒅


##### w = 
 =


###### 𝝏𝝋 −𝒂𝒈
 𝝏𝒛 [= ] 𝝈 [𝒌]


##### Using eq (2.30) we get

###### −𝝅𝑯 𝒔𝒊𝒏𝒉𝒌(𝒅+𝒛)

##### w =  𝐜𝐨𝐬(kx -σt)

###### 𝑻 𝐬𝐢𝐧𝒉𝒌𝒅

 −𝝅𝑯 𝒔𝒊𝒏𝒉𝒌(𝒅+𝒛)

##### w =  𝐜𝐨𝐬(kx -σt) (2.41)

###### 𝑻 𝐬𝐢𝐧𝐡𝐤𝐝


-----

##### The equations express the velocity components with the wave at any depth z. At a given z, all the velocities are seen to be harmonic in x and t as shown in 2.4.a

###### Z=-1m

 Z=-2m

 Z=-3m

 Z=-4 m

 Z=-n m

 Fig.2.4a shows the horizontal velocity components are the hyperbolic functions of depth


-----

##### At a given phase angle θ,(θ=kx- σt) the hyperbolic function of z (cosh and sinh) cause an exponential decay of u and w with the distance down from free surface. This is indicated schematically in fig 2.4.b for the phase angles at which the components are largest. The variation of u and w with respect to phase are shown in fig 2.5.

###### d/L > 0.5 0.5<d/L > 0.05 d/L < 0.05
 0
 0
 0

 -0.5 -0.5 w -0.5 w
 u, w


###### -1


###### -1

 Fig 2.4.b Variation of maximum u and w


-----

###### θ= π/2 U=+ve W= 0

 θ= π U=0 W= +ve

 θ= 3π/2 U= -ve W= 0

##### Fig 2.5 Variation of u and w with phase


-----

##### • The local acceleration in x and z direction are given by


##### 𝐜𝐨𝐬(kx -σt) (2.42)
###### 𝐬𝐢𝐧𝒉𝒌𝒅

 𝒔𝒊𝒏𝒉𝒌(𝒅+𝒛)

##### 𝐬𝐢𝐧(kx -σt) (2.43)
###### 𝐬𝐢𝐧𝒉𝒌𝒅


##### 𝒂 =
###### 𝒙

##### 𝒂 =
###### 𝒘


###### 𝝏𝒖
 𝝏𝒕 [=]



##### • This expression for the fluid particle kinematics reported above is for the

 water surface elevation, 𝜼 being a sinus curve. The fluid particle kinematics

 for 𝜼 being a cosine curve are given below.

 The φ can be derived as


###### 𝒂𝒈

##### φ =

###### 𝝈


###### 𝒄𝒐𝒔𝒉𝒌(𝒅+𝒛)

##### . 𝐬𝒊𝒏𝒌𝒙−𝝈𝒕. (2.44)
###### 𝒄𝒐𝒔𝒉𝒌𝒅


-----

##### In which case

 𝜼= a𝐜𝐨𝐬(kx -σt) (2.45)


###### 𝒂𝒈𝒌

##### u=


##### 𝐜𝐨𝐬(kx -σt) (2.46)
###### 𝐜𝐨𝐬𝒉𝒌𝒅


##### 𝒂 = 𝒂𝒈𝒌
###### 𝒙


##### 𝐬𝐢𝐧(kx -σt) (2.47)
###### 𝐜𝐨𝐬𝒉𝒌𝒅


##### w=


##### 𝐬𝐢𝐧(kx -σt) (2.48)
###### 𝐜𝐨𝐬𝒉𝒌𝒅


##### 𝒂 = −𝒂𝒈𝒌
###### 𝒘


###### 𝒔𝒊𝒏𝒉𝒌(𝒅+𝒛)

##### 𝐜𝐨𝐬(kx -σt) (2.49)
###### 𝐜𝐨𝐬𝒉𝒌𝒅


-----

# WATER PARTICLE DISPLACEMENT UNDER PROGRESSIVE WAVE

##### • The expression for individual horizontal and vertical water particle displacements is

 Obtained as follows.


##### δ𝒙 = ׬ 𝒖𝒅𝒕=

 δ𝒛 = ׬ 𝒘𝒅𝒕=


##### cos(kx −σt) (2.50)
###### 𝐬𝐢𝐧𝒉𝒌𝒅

 𝒔𝒊𝒏𝒉𝒌(𝒅+𝒛)

##### sin(kx −σt) (2.51)
###### 𝐬𝐢𝐧𝒉𝒌𝒅


###### 𝑯

##### Let δ𝒙 = D cos(kx −σt) where D=

###### 𝟐


###### 𝒄𝒐𝒔𝒉𝒌(𝒅+𝒛)
 𝐬𝐢𝐧𝒉𝒌𝒅


-----

###### 𝑯

##### δ𝒛 = B sin(kx −σt) where B =

###### 𝟐


###### 𝒔𝒊𝒏𝒉𝒌(𝒅+𝒛)
 𝐬𝐢𝐧𝒉𝒌𝒅


###### 𝟐

##### 𝒄𝒐𝒔[𝟐] 𝒌𝒙−𝝈𝒕= [δ][𝒙] ∶𝒔𝒊𝒏[𝟐] 𝒌𝒙−𝝈𝒕=

###### 𝑫

 Since, [𝒄𝒐𝒔[𝟐] 𝒌𝒙−𝝈𝒕 + 𝒔𝒊𝒏[𝟐] 𝒌𝒙−𝝈𝒕 = 1], we have


###### 𝟐


##### This equation of an ellipse showing that the water particles moves in an elliptical orbit.

 Where, D= Semi major axis (horizontal measure of particle displacement)

 B= Semi minor axis (vertical measure of particle displacement)


-----

#####  Shallow water Condition:


###### 𝒅

##### For

###### 𝑳 [<]


###### 𝟏
 𝟐𝟎 [we have used coshk(d+z) and sinhk(d + z)]


##### Hence, D=

###### 𝟐 [.] 𝒌𝒅

 𝑯 𝒌(𝒅+𝒛) 𝑯 (𝒅+𝒛)

##### B= =

###### 𝟐 𝒌𝒅 𝟐 𝒅

##### • Hence, the water particles move in elliptical orbits (paths) in shallow and

 intermediate waters with the equation of the form


-----

##### = 1 (2.53)


#####  Deep water condition:

###### 𝒅 𝟏

##### For the case [>]


##### D=


###### 𝑯
 𝟐


##### As ‘d’ (depth of water of d/L) is very large 𝒆[−𝒌(𝒅+𝒛)] and 𝒆[−𝒌𝒅] will be very small compared to 𝒆[𝒌(𝒅+𝒛)]


-----

##### Hence D=

###### 𝑯

##### Similarly B= [𝒆][𝒌𝒛]


###### 𝒆[𝒌(𝒅+𝒛)]



##### • Thus, the particles move in circular orbits in deep waters (since D=B) with the

 equation of the form

###### 2 2

𝐻δ𝑥 + 𝐻δ𝑧 = 1 (2.54)

2[𝑒][𝑘𝑧] 2[𝑒][𝑘𝑧]

##### This shows that for deep water conditions, the water particles are circular.


-----

##### • The amplitude of the water particle

 displacement decreases exponentially

 along with the depth. The water

 particle displacements becomes small

 relative to the wave height at a depth

 equal to one half the wave length

 below the SWL. The variation of the

 water particle displacements under

 different depth conditions is

 illustrated in Fig 2.6


-----

# Solution to the Dispersion equation

##### • An approximate solution for wave number k in the dispersion relationship given by eq. (2.29)
 • For a given σ and d proposed by Hunt (1979) can be solved directly for kd.

###### 𝒚

##### (𝒌𝒅)[𝟐]= 𝒚[𝟐] + 𝟔 (2.55)

###### 𝟏+σ𝒏=𝟏 𝒅𝒏𝒀[𝒏]

 𝝈[𝟐]𝒅

##### Where y=

###### 𝒈 [= ][𝒌][𝟎][𝒅] [and]

##### 𝒅𝟏 = 0.666666666 𝒅𝟐 = 0.35555555 𝒅𝟑 = 0.160846508
 𝒅𝟒 = 0.0632098765  𝒅𝟓 = 0.0217540484 𝒅𝟔 = 0.0065407983

 The celerity can be obtained as


###### 𝑪[𝟐]
 𝒈𝒅 [= 𝒚+ 𝟏+ 𝟎. 𝟔𝟓𝟐𝟐𝒚+ 𝟎. 𝟒𝟔𝟐𝟐𝒚][𝟐] [+ 𝟎. 𝟎𝟖𝟔𝟒𝒚][𝟒] [+ 𝟎. 𝟎𝟔𝟕𝟓𝒚][𝟓−𝟏−𝟏]
 Which is accurate to 0.1% for 0<y<∞


###### (2.56)


-----

# PRESSURE DISTRIBUTION UNDER
 PROGRESSIVE WAVES:

##### • The linearized Bernoulli’s equation is given by


###### −𝝏𝝓
 𝝏𝒕 [+]


###### 𝒑 𝝆 [+ 𝒈𝒛=][ 0]



##### • Multiplying through out by ρ the total pressure is given as,


##### 𝐩= 𝝆


###### 𝝏𝝓

##### (Dynamic + Static)
###### 𝝏𝒕 [+ (−ϒ𝒛)]



##### • Substituting for φ from eq. (2.22) we get


###### 𝒄𝒐𝒔𝒉𝒌(𝒅+𝒛)
 𝐜𝐨𝐬𝒉𝒌𝒅 [sin(kx – σt)-ϒz]


##### P=


###### ϒ𝑯
 𝟐


-----

##### 𝜼=


###### 𝑯 𝒄𝒐𝒔𝒉𝒌(𝒅+𝒛)

##### = 𝑲𝒑

###### 𝟐 [𝒔𝒊𝒏𝒌𝒙−𝝈𝒕] [and let ] 𝐜𝐨𝐬𝒉𝒌𝒅


##### Where 𝑲𝒑 is the pressure response factor then,


##### Or


##### (2.57)
###### ϒ[=(][𝜼𝑲][𝒑] [- z)]


##### It is to be mentioned that p was set to zero to define the free surface boundary

 condition in the Bernoulli equation. However φ was determined by setting p=0 at

 z=0 instead of z=η [Refer Eq 2.5]. Hence eq 2.57 is valid only for negative z.


-----

##### Applying Eq (2.57)

###### 𝑷

##### Pressure at z=0,

###### ϒ

##### Pressure at z=-d, 

 η This is [


##### (2.58)
###### 𝒄𝒐𝒔𝒉𝒌𝒅 [+ d]


##### Since cosh kd is always greater than 1

 Under the trough at sea bed

 Conditions are z= - d, η= - η


###### 𝟏
 𝒄𝒐𝒔𝒉𝒌𝒅


##### Substituting 𝑲𝒑 =


###### 𝐜𝐨𝐬𝐡(𝒅−𝒅)
 𝒄𝒐𝒔𝒉𝒌𝒅 [=]


-----

##### And η= - η Hence from eq (2.57)


###### 𝑷
 ϒ [=]


###### −η

##### (2.59)
###### 𝒄𝒐𝒔𝒉𝒌𝒅 [+ d]


###### 𝑷 η
 ϒ [=][[d -] 𝒄𝒐𝒔𝒉𝒌𝒅 [] > (d- η)]

##### It is often needed to determine the surface wave height based on subsurface

 measurement of pressure. For this purpose Eq. (2.57) is represented as


##### η=


###### 𝑵(𝒑+𝝆𝒈𝒛) 1

#####, where ‘K’ is pressure response factor at the seabed given by
###### 𝝆𝒈𝑲 𝒄𝒐𝒔𝒉𝒌𝒅 [.]


##### N is the correction factor depending on the period, depth, wave amplitude etc.

 N> 1 for long period waves N<1 for short period waves

 N=1 for linear waves


-----

##### The pressure distribution under a progressive wave is given in Fig 2.7

###### d+ 𝜼 d-η

|Col1|Col2|Col3|
|---|---|---|
||||
||||


###### d+η d

𝜼

𝒄𝒐𝒔𝒉𝒌𝒅


##### Fig 2.7 Pressure distribution under a progressive wave


-----

# GROUP CELERITY:

##### • When a group of waves or a wave train travels its speed is generally not identical to the
 speed with individual waves within the group travel. If any two wave trains of the same amplitude, but slightly different wavelengths or periods, progress in the same direction, the resultant surface disturbance can be represented as the sum of the individual disturbances. For waves propagating in deep or transitional waters, the group velocity is determined as follows.

 𝜼𝑻 = 𝜼𝟏+𝜼𝟐 =a𝒔𝒊𝒏𝒌𝟏𝒙−𝝈𝟏𝒕+ a𝒔𝒊𝒏(𝒌𝟐𝒙−𝝈𝟐𝒕) (2.60)


##### 𝜼𝑻=𝟐𝒂𝒄𝒐𝒔


###### 𝟐 𝒙−
 𝟐


###### 𝟐 𝒕. 𝒔𝒊𝒏
 𝟐


###### 𝟐 𝒙−
 𝟐


###### 𝟐 𝒕
 𝟐


-----

##### • This is a form of a series of sine waves the amplitude of which varies slowly from 0 to 2a
 according to the cosine factor.

 • The points of zero amplitude(nodes) of the wave envelope 𝛈𝐓 are located by finding the
 zeros of the cosine factor.
 i.e
 𝛈𝐓𝐦𝐚𝐱= 0 occurs when

###### 𝐤𝟏−𝐤𝟐 𝐱− 𝛔𝟏−𝛔𝟐 𝐭= (2m+1)𝛑
 𝟐 𝟐 𝟐

##### • In other words the nodes will occur on ‘x’ axis at distances as follows:


###### 𝝈𝟏−𝝈𝟐 𝒌𝟏−𝒌𝟐 [𝒕]


##### 𝑿 =
###### 𝒏𝒐𝒅𝒆


###### (𝟐𝒎+𝟏)𝝅
 𝒌𝟏−𝒌𝟐 [+]


-----

##### • Since the position of all the nodes in a function of time they are not stationary. At t=0,

 there will be nodes at


###### 𝝅
 𝒌𝟏−𝒌𝟐 [,]


###### 𝟑𝝅
 𝒌𝟏−𝒌𝟐[, ]



##### • The distance between the nodes are given by


##### x =


###### 𝟐𝝅
 𝒌𝟏−𝒌𝟐 [=]



##### • The speed of propagation of the nodes and hence the speed of propagation of the
 wave group is called the ‘Group Velocity’ and is given by:


###### 𝒅𝒙𝒏𝒐𝒅𝒆
 𝒅𝒕 [= Wave group velocity ][𝑪][𝑮] [=]


###### 𝝈𝟏−𝝈𝟐 𝒌𝟏−𝒌𝟐 [=]


###### 𝒅𝝈 𝒅𝒌


-----

###### 𝑳 𝟐𝝅 𝑻[= ] 𝑻


##### But σ = K.C =

 𝑪 =
###### 𝑮


###### 𝟐𝝅
 𝑳


###### 𝒅(𝑲𝑪)


##### Since k=


###### 𝟐𝝅
 𝑳


##### 𝑪𝑮=C+

###### 𝑳.𝒅𝑳

##### 𝑪𝑮= C - 𝐋


##### Since 𝑪[𝟐] =


###### 𝒈 𝒌 [𝒕𝒂𝒏𝒉(𝒌𝒅)]


##### Substituting and on simplification we get


-----

##### (2.62) 𝒔𝒊𝒏𝒉𝟐𝒌𝒅


##### For deep waters

###### 𝒔𝒊𝒏𝒉𝟐𝒌𝒅 [is zero ]
 𝟏

##### Hence 𝑪𝑮 =

###### 𝟐 [𝑪][𝟎]

##### 𝑪 = 𝟏 𝑳𝟎 𝟏
###### 𝑮
 𝟐 𝑻 [=] 𝟐 [𝑪][𝟎]

##### (2.63)

 The Group velocity is one half of the phase velocity in deep waters. Further it should be noted that variables if associated with a suffix ‘0’ refer to deep-water conditions. For example 𝑪𝟎 is deep water celerity.


-----

## Table 2.2 Variation of Asymptotic Functions

##### Function Asymptotes

 Shallow waters Deep Waters

 Sinhkd kd 𝒆𝒌𝒅
 𝟐
 Coshkd 1 𝒆𝒌𝒅
 𝟐
 tanhkd Kd 1

 In shallow waters,
 𝑪𝑮 = 𝑪= 𝒈𝒅 (2.64) since sinh2kd = 2kd

|Function|Asymptotes|Col3|
|---|---|---|
||Shallow waters|Deep Waters|
|Sinhkd|kd|𝒆𝒌𝒅 𝟐|
|Coshkd|1|𝒆𝒌𝒅 𝟐|
|tanhkd|Kd|1|


-----

##### Hence in shallow water the group and phase velocities are same and is a function of only depth of water and in deep waters, the 𝑪𝑮is a function of wave length. Because of this, in deep waters, the longer waves (Long L) travel faster and produce the small phase differences resulting in wave groups. These waves are said to be dispersive or propagating in a dispersive medium, i.e., in a medium where their celerity is dependent on wave length.


-----

# WAVE ENERGY

##### • Total Energy = Potential energy + Kinetic Energy

 • In order to determine the total energy under progressive waves the potential

 energy of the wave above z=-d with a wave from present is determined from which

 the potential energy of the water in the absence of a wave from is subtracted. Refer

 Fig 2.8 for definitions.

 • The potential energy (with respect to z=-d) of a small column of water (d+η) high, dx
 long and 1m wide.


##### dP𝑬𝟏 = ϒ𝑨ഥ𝒙
 = ϒdx.(d+η)([d+η] = ϒ

###### 𝟐 [)]


###### (d+η)[𝟐]

##### dx (2.65)
###### 𝟐


-----

##### • The average potential energy per unit surface area (sometimes called the average potential
 energy density) is

###### 𝒕+𝑻 𝒙+𝑳

##### 𝟏 𝟏
 (2.66)
 𝑷𝑬 = [ϒ] න (𝒅+ 𝜼)[𝟐] 𝒅𝒙𝒅𝒕
###### 𝟏

##### 𝟐 𝑳 𝑻 [න]

###### 𝒕 𝒙

##### Using 𝜼=asin(kx-σt) then Eq. (2.66) becomes


##### ϒ 𝑷𝑬 =
###### 𝟏

##### 𝟐𝑳𝑻 [න]

###### 𝒕

##### On simplification


##### න (𝒅[𝟐] + 𝟐𝒂𝒅𝒔𝒊𝒏𝒌𝒙−𝝈𝒕+ 𝒂[𝟐]𝒔𝒊𝒏[𝟐](𝒌𝒙−𝝈𝒕))𝒅𝒙𝒅𝒕

###### ϒ𝒂[𝟐]

##### (2.67)
###### 𝟒


##### 𝑷𝑬 =
###### 𝟏


###### ϒ𝒅[𝟐]
 𝟐 [+]


-----

##### • Which is the average potential energy per unit surface area of all the water above z=-d

 • The potential energy in the absence of wave would be


##### 𝑷𝑬 =
###### 𝟐


##### (2.68)
###### 𝟐



##### • The average potential energy density, 𝑷𝑬 which is attributable to the presence of the

 progressive wave on the free surface, is

 𝑷𝑬= 𝑷𝑬𝟏 −𝑷𝑬𝟐= Average Potential Energy


###### 𝟒 [−]


###### 𝟐


##### =


###### 𝟐 [+]


-----

##### 𝑷𝑬=


###### ϒ𝒂[𝟐]

##### (2.69)
###### 𝟒

|= 𝟒 (2.6|Col2|Col3|
|---|---|---|
||||
|dz|w|u|
||||
||||
||||


###### dx

##### Fig.2.8 Definition sketch for potential and kinetic energy under progressive wave 


##### Kinetic Energy

 The kinetic energy, KE =


###### 𝟏 𝟐 [𝒎𝒗][𝟐][, where ‘m’ is the mass of the fluid and ‘v’ is ]


##### the resultant velocity. For 2D wave flow


-----

##### d(KE)= 𝒖[𝟐] + 𝒘[𝟐] dM

###### 𝟐

 𝟐
 𝟏

##### = 𝒖[𝟐] + 𝒘[𝟐] ρ.dz.dx

###### 𝟐

##### • The average K.E. per unit of surface area is then given by

###### 𝝆 𝒕+𝑻 𝒙+𝑳 𝜼
 𝟐 𝟐

##### 𝑲𝑬= ׬ ׬ (𝒖 + 𝒘 ) 𝒅𝒛𝒅𝒙𝒅𝒕

###### 𝟐𝑳𝑻 [׬][𝒕] 𝒙 −𝒅

##### • With η= a sin(kx-σt)


-----

###### 𝑲𝑬


###### 𝒕+𝑻
 𝝆 =
 𝟐𝑳𝑻 [න]
 𝒕


###### 𝒙+𝑳

 න

 𝒙


###### 𝜼≅𝟎

 න

 −𝒅


###### 𝝈[𝟐]𝒄𝒐𝒔𝒉[𝟐]𝒌𝒅 [(𝒄𝒐𝒔𝒉][𝟐][𝒌(𝒅+ 𝒛)𝒔𝒊𝒏][𝟐][(][kx−σt][) + 𝒔𝒊𝒏𝒉][𝟐][𝒌(𝒅+ 𝒛)𝒄𝒐𝒔][𝟐][(][kx−σt][)) 𝒅𝒛𝒅𝒙𝒅𝒕]


##### Using trigonometrical identities

###### 𝟏

##### 𝒄𝒐𝒔𝒉[𝟐]𝒌(𝒅+ 𝒛)=

###### 𝟐 [𝟏+ 𝒄𝒐𝒔𝒉𝟐𝒌(𝒅+ 𝒛)]

##### 𝒔𝒊𝒏𝒉[𝟐]𝒌𝒅+ 𝒛= [−𝟏] 𝟏−𝒄𝒐𝒔𝒉𝟐𝒌(𝒅+ 𝒛)
 𝟐

 𝒄𝒐𝒔[𝟐] kx−σt −𝒔𝒊𝒏[𝟐] kx−σt = 𝒄𝒐𝒔𝟐 kx−σt


-----

##### 𝒄𝒐𝒔[𝟐] kx−σt + 𝒔𝒊𝒏[𝟐] kx−σt = 1

 Sinh2kd= 2sinhkd.coshkd

 And 𝝈[𝟐] = 𝒈𝒌𝒕𝒂𝒏𝒉𝒌𝒅


##### It can be shown   𝑲𝑬=

 Total energy E= 𝑷𝑬+ 𝑲𝑬


##### (2.70)
###### 𝟒


##### E=


##### (2.71)
###### 𝟐


##### The average total energy per unit surface area is the sum of the average potential and kinetic energy densities often called as specific energy density.


-----

# WAVE POWER

##### • Wave energy flux is the rate at which energy is transmitted in the direction of wave

 propagation across a vertical plane perpendicular to the direction of the wave advance and

 extending down the entire depth. The average energy flux per unit wave crest width

 transmitted across a plane perpendicular to wave advance is
 ഥ𝑷=Wave power = Average energy flux per unit wave crest width

 ഥ ഥ 𝑷=𝑬𝒏𝑪= ഥ𝑬𝑪𝒈 (2.72)


###### 𝒔𝒊𝒏𝒉𝟐𝒌𝒅


##### When n=


###### 𝟏 𝟐 [𝟏+]


###### 𝟏 𝟐 [𝑪][𝟎]


##### For Deep waters


###### 𝟐𝒌𝒅
 𝒔𝒊𝒏𝒉𝟐𝒌𝒅 [= 0 and][ 𝑪][𝒈][=]


-----

###### 𝟏

##### n=

###### 𝟐

 𝟏

##### Or 𝑷𝟎= (2.73)

###### 𝟐 [ഥ𝑬𝑪][𝟎]


##### For shallow waters

 ഥ𝑷=ഥ𝑬𝑪= ഥ𝑬𝑪𝒈 (since sinh2kd=2kd)

 • Assume the wave propagates from deep waters towards the shore. The ocean
 bottom slope is gradual and there are no undulations and has parallel bottom slope contours. According to the conservation of energy, equating the power in the shallow waters (Eq. 2.72) to that in deep waters (Eq. 2.73) we get

###### ϒ𝑯[𝟐] ϒ𝑯𝟎[𝟐] . 𝑪𝟎
 𝟖 [. 𝑪][𝒈] [=] 𝟖 𝟐

##### On substituting for 𝑪𝒈 and on simplification we obtain


-----

##### =


###### 𝑯
 𝑯𝟎


###### 𝟐


###### 𝟏
 𝟐𝒌𝒅
 𝒔𝒊𝒏𝒉𝟐𝒌𝒅

 𝟏

##### [.] 𝟐𝒏 [= 𝒌][𝒔] (2.74)


###### 𝑪𝟎


##### Or


##### Where n=

###### 𝟐 [𝟏+] 𝒔𝒊𝒏𝒉𝟐𝒌𝒅

##### • The above equation giving the ratio between wave height at any depth in

 shallower waters and the deep water height. This relationship obtained

 without considering the irregular variation in the sea bottom contours is

 called as shoaling coefficient.


-----

##### The variation of the different properties of a small amplitude waves are shown in Fig.2.9

###### Fig.2.9 Properties of small amplitude waves


-----

# MASS TRANSPORT VELOCITY

##### When waves are in motion, the particles upon completion of each nearly an elliptical or

 circular motion would have advanced a short distance in the direction of propagation

 (Fig.2.10). Consequently there is a mass transport in the direction of progress of the

 wave. The mass transport velocity at any depth z below S.W.L is given as

###### 𝝅𝑯 𝟐𝑪 𝒄𝒐𝒔𝒉𝟐𝒌(𝒅+𝒛)

##### ഥ𝑼𝒛= (2.75)

###### [𝟐]


-----

##### The mass transport speed is appreciable for high steep waves and is very small for

 waves of long period.

###### ഥ𝑼𝒛 DIRECTION OF PROPAGATION

 Fig. 2.10


-----

