### Hydraulics

#### Prof. Mohammad Saud Afzal

###### Department of Civil Engineering


-----

# The Velocity Field

####  The infinitesimal particles of a fluid are tightly packed together (as is implied by

 the continuum assumption).

  Thus, at a given instant in time, a description of any fluid property (such as density,

 pressure, velocity, and acceleration) may be given as a function of the fluid’s

 location.


-----

######  This representation of fluid parameters as functions of the spatial coordinates is termed a

 field representation of the flow.

 𝑽= 𝒖𝒙, 𝒚, 𝒛, 𝒕Ƹ𝒊+ 𝒗𝒙, 𝒚, 𝒛, 𝒕 Ƹ𝒋+ 𝒘𝒙, 𝒚, 𝒛, 𝒕 𝒌[෡]

 where u, and w are the x, y, and z components of the velocity vector.

  By definition, the velocity of a particle is the time rate of change of the position vector for

 that particle.


-----

####  Shown in Fig.1, The position of particle 

 A relative to the coordinate system is

 given by its position vector, which (if the

 particle is moving) is a function of time.

  The time derivative of this position gives

###### Fig.1

#### the velocity of the particle,

 𝑑𝑟 Τ𝑑𝑡= 𝑉 .
###### 𝐴 𝐴


-----

####  By writing the velocity for all of the particles, we can obtain the field description of

 the velocity vector 𝑽= 𝑽𝒙, 𝒚, 𝒛, 𝒕.

  Since the velocity is a vector, it has both a direction and a magnitude. The magnitude

 of V, denoted 𝑽= 𝑽= 𝒖[𝟐] + 𝒗[𝟐] + 𝒘[𝟐] , is the speed of the fluid.


-----

# Eulerian Flow
#### There are two general approaches in analyzing fluid mechanics problems. The Descriptions

 first method, called the Eulerian method.

 In this case, the fluid motion is given by completely prescribing the necessary

 properties (pressure, density, velocity, etc.) as functions of space and time.

 From this method we obtain information about the flow in terms of what

 happens at fixed points in space as the fluid flows through those points.


-----

#### A typical Eulerian representation of

 the flow is shown by the figure in the

 margin which involves flow past an air

 foil at angle of attack.

  The pressure field is indicated by using

 a contour plot showing lines of

 constant pressure, with gray shading

 indicating the intensity of the

 pressure.


-----

# Lagrangian Flow Descriptions

###### The second method, called the Lagrangian method, involves following individual

 fluid particles as they move about and determining how the fluid properties

 associated with these particles change as a function of time.

 That is, the fluid particles are “tagged” or identified, and their properties

 determined as they move.

 The difference between the two methods of analyzing fluid flow problems can be

 seen in the example of smoke discharging from a chimney.


-----

# One-, Two-, and Three-Dimensional Flows

###### Generally, a fluid flow is a rather complex three-dimensional, time-dependent

 phenomenon. 𝑽= 𝑽𝒙, 𝒚, 𝒛= 𝒖Ƹ𝒊+ 𝒗Ƹ𝒋+ 𝒘𝒌[෡]

 In almost any flow situation, the velocity field actually contains all three velocity

 components(u, v, and w, for example). In many situations the three-dimensional

 flow characteristics are important in terms of the physical effects they produce. For

 these situations it is necessary to analyze the flow in its complete three-

 dimensional character.


-----

###### The flow of air past an airplane wing provides an example of a complex three-dimensional

 flow.

 In many situations one of the velocity components may be small (in some sense) relative to

 the two other components. In situations of this kind it may be reasonable to neglect the

 smaller component and assume two-dimensional flow. That is, 𝐕= 𝒖Ƹ𝒊+ 𝒗Ƹ𝒋, where u and 𝒗

 are functions of x and y (and possibly time, t).


-----

#### It is sometimes possible to further simplify a flow analysis by assuming that two of the

 velocity components are negligible, leaving the velocity field to be approximated as a

 one-dimensional flow field. That is, 𝐕= 𝒖Ƹ𝒊.


-----

# Steady and Unsteady Flows

###### CLASSIFICATION OF FLOW

  Steady Flow: Fluid flow conditions at any point do not change with time. For example

 𝜕𝑉
 𝜕𝑡 [= 0,][ 𝜕𝑝]𝜕𝑡 [= 0,][ 𝜕𝜌]𝜕𝑡 [= 0]

 In a steady flow steam line, path line and streak line are identical.

  Unsteady Flow: Flow parameters at any point change with time, e.g. [𝜕𝑉]
 𝜕𝑡 [≠0]


-----

# Uniform and Non-uniform Flows

####  Uniform Flow: The flow is defined as uniform flow when in the flow field

 the velocity and other hydrodynamic parameters do not change from point to

 point at any instant of time.

  For a uniform flow, the velocity is a function of time only, which can be expressed in

 Eulerian description as

 𝑉= 𝑉(𝑡)


-----

####  Implication:

  For a uniform flow, there will be no spatial distribution of hydrodynamic and

 other parameters.

  Any hydrodynamic parameter will have a unique value in the entire field,

 irrespective of whether it changes with time − unsteady uniform flow OR

 does not change with time − steady uniform flow.


-----

######  Non-Uniform Flow: When the velocity and other hydrodynamic parameters changes

 from one point to another the flow is defined as non-uniform.

  Important points:

  For a non-uniform flow, the changes with position may be found either in the

 direction of flow or in directions perpendicular to it.

  Non-uniformity in a direction perpendicular to the flow is always encountered

 near solid boundaries past which the fluid flows.


-----

#### Reason: All fluids possess viscosity which reduces the relative velocity (of the fluid

 w.r.t. to the wall) to zero at a solid boundary. This is known as no-slip condition.


-----

# Streamline

####  In a fluid flow, a continuous line so drawn that it is tangential to the velocity

 vector at every point is known as a streamline.

  If the velocity vector 𝑽= Ƹ𝒊𝒖+ Ƹ𝒋𝒗+ 𝒌𝒘[෡]

  Then the differential equation of a streamline is given by

 𝑑𝑥
 𝑢 [=][ 𝑑𝑦]𝑣 [=][ 𝑑𝑧]𝑤


-----

## Practice Problem

#### In a flow the velocity vector is given by V= 3xi + 4yj – 7zk. Determine the equation of the

 streamline passing through a point M= (1, 4, 5).

###### Solution:

 The equation of the streamline is

 𝑑𝑥 𝑑𝑦 𝑑𝑧
 𝑢 [=] 𝑣 [= ] 𝑤

 Here, u = 3𝑥, v = 4𝑦 and w=-7𝑧

 𝑑𝑥 𝑑𝑦 𝑑𝑧
 Hence                    
 3𝑥 [=] 4𝑦 [= ][−] 7𝑧

 Considering the equations involving 𝑥 and 𝑦, on integration


-----

###### 1
 ′ ′ Where, 𝐶1 = a constant
 3 [ln 𝑥=][ 1]4 [ln 𝑦+ ln 𝐶][1]

4
3

###### Or,    𝑦 = 𝐶1𝑥 Where 𝐶1 is another constant.

 Similarly, by considering equations with x and z and on integration

 1
 ′ ′ Where, 𝐶2 = a constant
 3 [ln 𝑥= −] 7[1] [ln 𝑧+ ln 𝐶][2]

 Z= [𝐶][2]7 Where, 𝐶2 is another constant.
 𝑥3

 4 Putting the coordinates of the point M (1, 4, 5). 𝐶1=
 (1)[4/3][ =4 and ][𝐶][2][= 5 X ][1][7/3][ =5]

 The streamline passing through M is given by

 𝒚 = 4𝒙[𝟒/𝟑] and  z = [𝟓]
 𝒙[𝟕/𝟑]


-----

# Path lines

###### A path line is the actual path traveled by an individual fluid

 particle over some time period.

 Path lines are the easiest of the flow patterns to understand.

 A path line is a Lagrangian concept in that we simply follow

 the path of an individual fluid particle as it moves around in Fig.2

 the flow field.

 Thus, a path line is the same as the fluid particle’s material position vector (x

 particle(t), y particle(t), z particle(t)), traced out over some finite time interval.


-----

# Streak lines

####  A streakline is the locus of fluid particles that have passed

 sequentially through a prescribed point in the flow.

  Streaklines are the most common flow pattern generated in a

 physical experiment. If you insert a small tube into a flow and

 introduce a continuous stream of tracer fluid (dye in a water Fig.3

 flow or smoke in an airflow), the observed pattern is a

 streakline.

  Fig. 3 shows a streakline is formed by connecting all the circles into a

 smooth curve.


-----

# Stagnation Point

######  A point of interest in the study of the kinematics of fluid

 is the occurrence of points where the fluid flow stops.

 When a stationary body is immersed in a fluid, the fluid

 is brought to a stop at the nose of the body. Such a

 point where the fluid flow is brought to rest is known as
 Fig.4

 the stagnation point.


-----

####  Thus, a stagnation point is defined as a point in the flow field where the velocity

 is identically zero.

  This means that all the components of the velocity vector 𝑽[ഥ] viz., u, v, and w are

 identically zero at the stagnation point.


-----

####  Acceleration is a vector.


# Acceleration

####  Acceleration is a vector.

  In the natural co-ordinate system, viz., along and across a streamline (Fig. 5).

###### 𝑑𝑉
 2 2

#### 𝑎= a = 𝑎 + 𝑎

###### 𝑠 𝑛 𝑑𝑡 [and]

####  In the tangential direction: 𝑎𝑠 = 𝜕𝑉𝑠 𝜕𝑉𝑠

###### 𝜕𝑡 [+ 𝑉][𝑠] 𝜕𝑠

 Fig.5


-----

######  In the normal direction : 𝑎𝑛 = [𝜕𝑉][𝑛]
 𝜕𝑡 [+][ 𝑉]𝑟[𝑠][2]

 where r = radius of curvature of the streamline at the point

 𝑉𝑠 = tangential component of the velocity V

 And 𝑉𝑛 = normal component of velocity generated due to change in direction.

  The terms [𝝏𝑽][𝒔]
 𝝏𝒕 [and ][𝝏𝑽]𝝏𝒕[𝒏] [are called ][local accelerations][.]

 Also 𝑽𝒔 𝝏𝑽𝒔
 𝝏𝒔 [= tangential convective acceleration and ][𝑽]𝒓[𝒔𝟐] [= normal convective ]

 acceleration.


-----

######  In Cartesian co-ordinates: 𝑽= Ƹ𝒊𝒖+ Ƹ𝒋𝒗+ 𝒌𝒘[෡]

  Acceleration 𝑎𝑥 , 𝑎𝑦 , and 𝑎𝑧 in the x, y, z directions respectively are:

  𝑎 = [𝜕𝑢] 𝑥
 𝜕𝑡 [+ 𝑢] [𝜕𝑢]𝜕𝑥 [+ 𝑣] [𝜕𝑢]𝜕𝑦 [+ 𝑤] [𝜕𝑢]𝜕𝑧

  𝑎 = [𝜕𝑣] 𝑦
 𝜕𝑡 [+ 𝑢] 𝜕𝑥[𝜕𝑣] [+ 𝑣] 𝜕𝑦[𝜕𝑣] [+ 𝑤] [𝜕𝑣]𝜕𝑧

  𝑎 = [𝜕𝑤] 𝑧
 𝜕𝑡 [+ 𝑢] [𝜕𝑤]𝜕𝑥 [+ 𝑣] [𝜕𝑤]𝜕𝑦 [+ 𝑤] [𝜕𝑤]𝜕𝑧


-----

# Practice Problem

###### The velocity along the centreline of a nozzle of length L is

 given by

 𝟐
 𝑽= 𝟐𝒕𝟏− [𝒙]
 𝟐𝑳

 where V= velocity in m/s, t = time in seconds from commencement of flow, x = distance

 from inlet to the nozzle. Find the convective acceleration, local acceleration and

 the total acceleration when t= 3s, x = 0.5 m and L = 0.8 m.


-----

###### Solution:

 2
 𝜕𝑉 𝑥
 (i) Local acceleration = at t = 3 s
 𝜕𝑡 [= 2 1 −] 2𝐿

 and

 2
 𝜕𝑉 0.5 x = 0.5 m, = 0.945 m/s[2]
 𝜕𝑡 [= 2 1 −] 2×0.8

 2 3
 (ii) Convective acceleration = 𝑉 [𝜕𝑉] . 2𝑡. 2 1 − [𝑥] − [1] 1 − [𝑥]
 𝜕𝑥 [= 2𝑡1 −] 2𝐿[𝑥] 2𝐿 2𝐿 [= −] [4𝑡]𝐿[2] 2𝐿

 At 1 = 3 s and x= 0.5 m

 3
 0.5
 Convective acceleration = − [4×3][2] 1 − = −𝟏𝟒. 𝟔𝟐𝟑 m/s[2]
 0.8 2×0.8
 (iii) Total acceleration = (local + convective) acceleration = 0.945 — 14.623 = — 13.68 m/s[2]


-----

# Continuity equation

#### In One-dimensional Analysis

  In steady flow, mass rate of flow into stream tube is equal to mass rate

 of flow out of the tube

 𝜌 𝐴 𝑉 𝐴 𝑉
###### 1 1 1 = 𝜌2 2 2

####  For incompressible fluid, under steady flow (Fig. 6).

 𝐴 𝑉 𝑉
###### 1 1 = 𝐴2 2

 Fig:6


-----

####  When there is a variation of velocity across the cross section of a conduit, for an

 incompressible fluid discharge. (Fig. 7)

 𝑄= න 𝑣𝑑𝐴= න 𝑣𝑑𝐴

###### 𝐴1 𝐴2
 Fig: 7


-----

# Practice Problem

###### Fig shows a pipe network with junctions (nodes) at A, B, C, D, E, and F. The numerals in the fig indicates the

 discharges at the nodes or in the pipes as the case is and the arrows indicate the directions of flows. By

 continuity equation determine the missing discharge values and their direction in pipes AB, BC, CD, BE and EF

 at the node F.


-----

###### By continuity criterion, the flow entering into a node must be equal to the flow going out of the node. Thus by considering flow into a node as positive, the algebraic sum of discharges at a node is zero.

 Thus at node A:

 100 – 70 – Q AB = 0
 Or Q 30 and Q is from A to B. AB = AB
 At node D: 70 + 50 – Q = 0 DC

 Q 120 and Q is from D to C. DC = DC
 At node C: 120 - 80 – Q = 0 CB
 Q 40 and Q is from C to B. CB = CB
 At node B: 30 + 40 - 30 – Q -20 = 0 BE 

 Q 20 and Q is from B to E. BE = BE
 At node E: 80 + 20 – Q - 90= 0 EF


-----

###### Q 10 and Q is from E to F. EF = EF
 At node F: 20 + 10 – Q = 0 F 
 Q discharge out of node F = 30. F =
 The distribution of discharges are as in fig below.

 It can be seen now that at each node the continuity equation is satisfied.


-----

# In Differential Form

######  Cartesian co-ordinates:

 𝜕𝜌 + [𝜕(𝜌𝑣)] = 0
 𝜕𝑡 [+][ 𝜕(𝜌𝑢)]𝜕𝑥 𝜕𝑦 [+][ 𝜕(𝜌𝑤)]𝜕𝑧

  For incompressible fluid (d𝜌/dt = 0) and hence the above equation is

 simplified as

 𝜕𝑢 𝜕𝑥 [+ 𝜕𝑣]𝜕𝑦 [+ 𝜕𝑤]𝜕𝑧 [= 0]


-----

# Rotational and irrotational action

######  Consider a rectangular fluid element of sides dx and dy [(Fig. 8.(a)].

  Under the action of velocities acting on it let it undergo deformation as shown in Fig. 8.(b) in a time

 dt.

 Fig.8.a Fig.8.b


-----

###### 𝛾1= angular velocity of element AB = [𝜕𝑣]
 𝜕𝑥

 𝛾 2 = angular velocity of element AD = [𝜕𝑢]
 𝜕𝑦

  Considering the anticlockwise rotation as positive, the average of angular

 velocities of two mutually perpendicular elements is defined as the rate

 of rotation.

  Thus rotation about z-axis

 𝝏𝒗
 𝝎𝒛 = [𝟏]
 𝟐 𝝏𝒙 [−𝝏𝒖]𝝏𝒚


-----

####  Thus for a three-dimensional fluid element, three rotational components as given in the

 following are possible:

###### 𝟏 𝝏𝒗 𝝏𝒖

#### About z axis, 𝝎𝒛 =

###### 𝟐 𝝏𝒙 [−] 𝝏𝒚

 𝟏 𝝏𝒖 𝝏𝒘

#### About y axis, 𝝎𝒚 =

###### 𝟐 𝝏𝒛 [−] 𝝏𝒙

 𝟏 𝝏𝒘 𝝏𝒗

#### About x axis, 𝝎𝒙 =

###### 𝟐 𝝏𝒚 [−] 𝝏𝒛


-----

####  Fluid motion with one or more of the terms 𝝎𝒛, 𝝎𝒚 or 𝝎𝒛 different from zero is

 termed rotational motion.

  Twice the value of rotation about any axis is called as vorticity along that axis.

###### 𝝏𝒗 𝝏𝒖

####  Thus the equation ( for vorticity along z-axis is ζ𝑧 = 2𝝎𝒛 =

###### 𝝏𝒙 [−] 𝝏𝒚

####  A flow is said to be irrotational if all the components of rotation are zero,

 viz. 𝝎𝒛 = 𝝎𝒚 = 𝝎𝒛 = 𝟎


-----

# Practice Problem

#### For the following flows, determine the components of rotation about the various axes.

 u = xy[3]z,  v = - y[2] z[2],  w = yz[2] – ( y[3] Z[2 ]/2)

 Solution: The components of rotation about the various axes are:

###### 𝜔𝑧 = [1] 𝜕𝑣
 2 𝜕𝑥 [−] [𝜕𝑢]𝜕𝑦 [=][ 1]2 [0 −3𝑥𝑦][2][𝑧= −] 𝟐[𝟑] [𝒙𝒚][𝟐][𝒛]

 𝜔𝑥 = [1] 𝜕𝑤 + 𝟐𝒚[𝟐]𝒛
 2 𝜕𝑦 [−] [𝜕𝑣]𝜕𝑧 [=][ 𝟏]𝟐 [𝒛][𝟐] [−] [𝟑𝒚]𝟐[𝟐][𝒛][𝟐]

 𝜕𝑢
 𝜔𝑦 = [1] = [1]
 2 𝜕𝑧 [−𝜕𝑤]𝜕𝑥 2 [𝑥𝑦][3][ −0 = 1]2 [𝒙𝒚][3]


-----

# Stream function

######  In a two-dimensional flow consider two streamlines S1 and S2. The flow rate (per unit depth) of

 an incompressible fluid across the two streamlines is constant and is independent of the path,

 (path a or path b from A to B in Fig. 9).

 Fig.9


-----

####  A stream function Ψ is so defined that it is constant along a streamline and the difference

 of Ψ𝑠 for the two streamlines is equal to the flow rate between them.

  Thus Ψ −Ψ = flow rate between S . The flow from left to right is taken as
###### 𝐴 𝐵 1 and S2

#### positive, in the sign convention. The velocities u and v in x and s directions are

 given by

###### 𝜕Ψ 𝜕Ψ

#### 𝑢=

###### 𝜕𝑦 [and][ v = −] 𝜕𝑥


-----

####  The stream function Ψ is defined as above for two dimensional flows only.

###### 𝝏𝒗 𝝏𝒖

####  For an irrotational flow,

###### 𝝏𝒙 [−] 𝝏𝒚 [=][ 0 and hence,]

 𝜕[2]Ψ 𝜕[2]Ψ

#### −

###### 𝜕𝑥[2][ −] 𝜕𝑦[2][ = 0]

 𝝏[𝟐]Ψ 𝝏[𝟐]Ψ

####  That is, the Laplace equation

###### 𝝏𝒙[𝟐] [+] 𝝏𝒚[𝟐] [= 𝟎]


-----

# Potential function

#####  In irrotational flows, the velocity can be written as a gradient of a scalar function ϕ

 called velocity potential.

###### 𝜕ϕ 𝜕ϕ 𝜕ϕ

##### 𝑢= and w =

###### 𝜕𝑥 [,][ v =] 𝜕𝑦 𝜕𝑧

##### Considering the equation of continuity for an incompressible fluid,

###### 𝜕𝑢 𝜕𝑣 𝜕𝑤
 𝜕𝑥 [+] 𝜕𝑦 [+] 𝜕𝑧 [= 0]

#####  And substituting the expressions for u, v and w in terms of ϕ

###### 𝜕[2]ϕ 𝜕[2]ϕ 𝜕[2]ϕ

##### 𝛻[2]ϕ =

###### 𝜕𝑥[2][ +] 𝜕𝑦[2][ +] 𝜕𝑧[2][ = 0]


-----

####  Thus the velocity potential satisfies the Laplace equation. Conversely, any function ϕ

 which satisfies he Laplace equation is a possible irrotational fluid flow case.

  Lines of constant ϕ arc called equipotential lines and it can be shown that these lines

 will form orthogonal grids with Ψ = constant lines. This fact is used in the construction

 of flow nets for fluid flow analysis.

###### [Note : Some authors define ϕ such that
 𝜕ϕ 𝜕ϕ 𝜕ϕ
 𝑢= − and w = −
 𝜕𝑥 [, ][v = −] 𝜕𝑦 𝜕𝑧 [] ]


-----

# Relation between Ψ and ϕ for 2-dimensional flow

####  ϕ exists for irrotational flow only.

######  Ψ = constant along a streamline.
 𝜕ϕ 𝜕Ψ

#### 𝑢=

###### 𝜕𝑥 [=] 𝜕𝑦

  Φ = constant along an equipotential
 v = [𝜕ϕ]
 line which is normal to streamlines.
 𝜕𝑦 [= −𝜕Ψ]𝜕𝑥

####  By continuity equation 𝜕[2]ϕ

###### 𝜕𝑥[2][ + 𝜕]𝜕𝑦[2][ϕ][2][ = 0]

####  By irrotational flow condition 𝜕[2]Ψ
 𝜕𝑥[2][ + 𝜕]𝜕𝑦[2][Ψ][2][ = 0]


-----

# Practice Problem

###### A velocity potential for a two-dimensional flow is given by ɸ = (x[2] — y[2]) + 3xy.

 Calculate (i) the stream function and (ii) the flow rate between the streamlines passing through points (1, 1) and (1, 2)

 Solution:
 ɸ = (x[2] - y[2])+ 3xy u = [𝜕𝛷] Ψ = 2xy + [3] (i)
 𝜕𝑥 [= 2𝑥+ 3𝑦=][ 𝜕𝜓]𝜕𝑦 2 [𝑦][2][ + 𝑓(𝑥)]

 𝑣= [𝜕𝛷] (ii) And from (i) − 𝜕𝜓
 𝜕𝑦 [= −2𝑦+ 3𝑥= −] [𝜕𝜓]𝜕𝑥 𝜕𝑥 [= −2𝑦−𝑓′(𝑥)]
 3
 f(x) = − Thus f'(x) = -3x and hence 2 [𝑥][2]

 3
 The required stream function is Ψ = 2xy —
 2 [(x][2][ — y][2][) ]


-----

###### At point (1, 1) Ψ1 = (2 — [3]
 2 [(1 —1)) = 2 units]

 At point (1, 2)

 Ψ [3] 2 = [2 x (1 x 2) —
 2 [(1 — 4)] = 8.5 units ]

 Flow rate between the stream lines passing through (1, 1) and (1, 2)

 Δ Ψ = Ψ2 −Ψ1 = (8.5 - 2.0) = 6.5 units


-----

