# BASIC COASTAL ENGINEERING


-----

# BASIC
 COASTAL
 ENGINEERING

##### Third Edition

 ROBERT M. SORENSENROBERT M. SORENSEN

###### Department of Civil and
 Environmental Engineering
 Lehigh University, Bethlehem, Pennsylvania


-----

Library of Congress Cataloging-in-Publication Data

A C.I.P. Catalogue record for this book is available
from the Library of Congress

ISBN-10: 0-387-23332-6 ISBN-10: 0-387-23333-4 (e-book)

ISBN-13: 9780387233321 ISBN-13: 978038723338

Printed on acid-free paper.

�2006 Springer ScienceþBusiness Media, Inc.
All rights reserved. This work may not be translated or copied in whole or in part
without the written permission of the publisher (Springer ScienceþBusiness Media,
Inc. 233 Spring Street, New York, NY 10013, USA), except for brief excerpts in
connection with reviews or scholarly analysis. Use in connection with any form of
information storage and retrieval, electronic adaptation, computer software, or by
similar or dissimilar methodology now known or hereafter developed is forbidden.
The use in this publication of trade names, trademarks, service marks and similar
terms, even if they are not identiWed as such, is not to be taken as an expression of
opinion as to whether or not they are subject to proprietary rights.

Printed in the United States of America

10 9 8 7 6 5 4 3 2 1 (SPI/SBA)

springeronline.com


-----

#### To
 Rita, Jon, Jenny,
 Mark, and John
 With Love


-----

### Contents

Preface xi

1. Coastal Engineering 1

1.1 The Coastal Environment 1

1.2 Coastal Engineering 3

1.3 Recent Trends 5

1.4 Coastal Engineering Literature 6

1.5 Summary 8

1.6 References 8

2. Two-Dimensional Wave Equations and Wave Characteristics 9

2.1 Surface Gravity Waves 9

2.2 Small-Amplitude Wave Theory 10

2.3 Wave Classification 15

2.4 Wave Kinematics and Pressure 18

2.5 Energy, Power, and Group Celerity 22

2.6 Radiation Stress and Wave Setup 30

2.7 Standing Waves, Wave Reflection 35

2.8 Wave Profile Asymmetry and Breaking 38

2.9 Wave Runup 44

2.10 Summary 47

2.11 References 48

2.12 Problems 49

3. Finite-Amplitude Waves 53

3.1 Finite-Amplitude Wave Theory Formulation 53

3.2 Stokes Waves 54

3.3 Cnoidal Waves 61

3.4 Solitary Waves 64

3.5 Stream Function Numerical Waves 68

3.6 Wave Theory Application 70

3.7 Summary 74

3.8 References 74

3.9 Problems 76

4. Wave Refraction, Diffraction, and Reflection 79

4.1 Three-Dimensional Wave Transformation 79

4.2 Wave Refraction 80


-----

viii / Contents

4.3 Manual Construction of Refraction Diagrams 82

4.4 Numerical Refraction Analysis 89

4.5 Refraction by Currents 91

4.6 Wave Diffraction 92

4.7 Combined Refraction and Diffraction 99

4.8 Wave Reflection 101

4.9 Vessel-Generated Waves 102

4.10 Summary 105

4.11 References 105

4.12 Problems 108

5. Coastal Water Level Fluctuations 113

5.1 Long Wave Equations 114

5.2 Astronomical Tide Generation and Characteristics 117

5.3 Tide Datums and Tide Prediction 120

5.4 Tsunamis 124

5.5 Basin Oscillations 127

5.6 Resonant Motion in Two- and Three-Dimensional Basins 130

5.7 Resonance Analysis for Complex Basins 137

5.8 Storm Surge and Design Storms 138

5.9 Numerical Analysis of Storm Surge 141

5.10 Simplified Analysis of Storm Surge 144

5.11 Long-Term Sea Level Change 150

5.12 Summary 151

5.13 References 151

5.14 Problems 154

6. Wind-Generated Waves 157

6.1 Waves at Sea 157

6.2 Wind-Wave Generation and Decay 158

6.3 Wave Record Analysis for Height and Period 161

6.4 Wave Spectral Characteristics 167

6.5 Wave Spectral Models 169

6.6 Wave Prediction—Early Methods 178

6.7 Wave Prediction—Spectral Models 183

6.8 Numerical Wave Prediction Models 185

6.9 Extreme Wave Analysis 187

6.10 Summary 190

6.11 References 190

6.12 Problems 193

7. Coastal Structures 195

7.1 Hydrodynamic Forces in Unsteady Flow 196

7.2 Piles, Pipelines, and Cables 198


-----

Contents / ix

7.3 Large Submerged Structures 209

7.4 Floating Breakwaters 211

7.5 Rubble Mound Structures 214

7.6 Rigid Vertical-Faced Structures 227

7.7 Other Loadings on Coastal Structures 233

7.8 Wave–Structure Interaction 235

7.9 Selection of Design Waves 238

7.10 Summary 241

7.11 References 241

7.12 Problems 245

8. Coastal Zone Processes 247

8.1 Beach Sediment Properties and Analysis 248

8.2 Beach Profiles and Profile Change 252

8.3 Nearshore Circulation 258

8.4 Alongshore Sediment Transport Processes and Rates 261

8.5 Shore Response to Coastal Structures 265

8.6 Numerical Models of Shoreline Change 269

8.7 Beach Nourishment and Sediment Bypassing 271

8.8 Wind Transport and Dune Stabilization 276

8.9 Sediment Budget Concept and Analysis 277

8.10 Coastal Entrances 280

8.11 Summary 282

8.12 References 282

8.13 Problems 285

9. Field and Laboratory Investigations 287

9.1 Field Investigations 288

9.2 Wind-Wave Measurements 288

9.3 Other Hydrodynamic Measurements 291

9.4 Coastal Morphology and Sedimentary Processes 293

9.5 Coastal Structures 298

9.6 Laboratory Investigations 299

9.7 Wave Investigation Facilities 300

9.8 Scaling of Laboratory Investigations 302

9.9 Common Types of Investigations 304

9.10 Summary 305

9.11 References 305

Appendices 309

A. Notation and Dimensions 309

B. Selected Conversion Factors 314

C. Glossary of Selected Terms 315

Index 321


-----

### Preface

The second edition (1997) of this text was a completely rewritten version of the

original text Basic Coastal Engineering published in 1978. This third edition
makes several corrections, improvements and additions to the second edition.

Basic Coastal Engineering is an introductory text on wave mechanics and

coastal processes along with fundamentals that underline the practice of coastal
engineering. This book was written for a senior or first postgraduate course in
coastal engineering. It is also suitable for self study by anyone having a basic
engineering or physical science background. The level of coverage does not
require a math or fluid mechanics background beyond that presented in a typical
undergraduate civil or mechanical engineering curriculum. The material presented in this text is based on the author’s lecture notes from a one-semester
course at Virginia Polytechnic Institute, Texas A&M University, and George
Washington University, and a senior elective course at Lehigh University. The
text contains examples to demonstrate the various analysis techniques that are
presented and each chapter (except the first and last) has a collection of problems
for the reader to solve that further demonstrate and expand upon the text
material.

Chapter 1 briefly describes the coastal environment and introduces the rela
tively new field of coastal engineering. Chapter 2 describes the two-dimensional
characteristics of surface waves and presents the small-amplitude wave theory to
support this description. The third chapter presents the more complex nonlinear
wave theories for two-dimensional waves, but only selected aspects of those
theories that are most likely to be of interest to practicing coastal engineers.
Wave refraction, diffraction, and reflection—the phenomena that control the
three-dimensional transformation of waves as they approach the shore—are
presented in Chapter 4. Besides the most common shorter period waves that
have periods in the range generated by the wind, there are longer period coastal
water level fluctuations that are important to coastal engineers. They are presented in Chapter 5.

Chapters 2 to 4 consider monochromatic waves—which are important for the

analysis of both wind-generated waves and many of the longer period water level
fluctuations. Chapter 6 then presents the behavior, analysis, and prediction of
the more complex wind-generated waves—the ‘‘real’’ waves that confront the
practicing coastal engineer.

The material presented in the first six chapters covers the primary controlling

environmental factors for coastal engineering analysis and design. The next two


-----

xii / Preface

chapters—which deal with coastal structures and shoreline processes—are concerned with the effects of wave action on the shore and engineering responses to
these effects. Chapter 7 focuses on determination of wave forces on coastal
structures and related coastal structure stability requirements, as well as the
interaction of waves with coastal structures and establishment of design wave
conditions for coastal structures. Chapter 8 covers beach characteristics, their
response to wave action, and the interaction of beach processes and coastal
structures, as well as the design of stable beaches. The last chapter gives an
overview of the types of field and laboratory investigations typically carried out
to support coastal engineering analysis and design. Finally, there is an appendix
that provides a tabulation of the notation used in the text, conversion factors for
common dimensions used in the text, and a glossary of selected coastal engineering terms.

I wish to acknowledge the support provided by Mrs. Cathy Miller, who typed

all of the equations in the original manuscript and Mrs. Sharon Balogh, who
drafted the figures. I am indebted to the late J.W. Johnson and R.L. Wiegel,
Emeritus Professors at the University of California at Berkeley, who introduced
me to the subject of coastal engineering.

R.M. Sorensen

Lehigh University


-----

# BASIC COASTAL ENGINEERING


-----

## 1

### Coastal Engineering

The competent coastal engineer must develop a basic understanding of the

characteristics and physical behavior of the coastal environment, as well as be
able to apply engineering principles and concepts to developing opportunities
and solving problems in this environment. Consequently, this book provides an
introduction to those physical processes that are important in the coastal zone. It
also introduces the analytical basis for and application of those methods required to support coastal engineering and design.

1.1 The Coastal Environment

We deWne the shoreline as the boundary between the land surface and the surface
of a water body such as an ocean, sea, or lake. The coastal zone is that area of
land and water that borders the shoreline and extends suYciently landward and
seaward to encompass the areas where processes important to the shore area are
active.

The land portion of most of the world’s coastal zone consists of sandy beaches.

In some places the beach is covered with coarser stones known as shingle. Where
wave and current action is relatively mild and a river provides large deposits of
sediment a delta may form and extend seaward of the general trend of the
shoreline. In some places there is a break in the shoreline to produce an estuary
or inlet to a back bay area—the estuary or inlet being maintained by river and/or
tide-induced Xow. Also, some coasts may be fronted by steep cliVs that may or
may not have a small beach at their toe. Since sandy beaches predominate and
have very dynamic and interesting characteristics, this type of coastline will
receive the greatest emphasis herein.

Waves are the dominant active phenomenon in the coastal zone. Most appar
ent and signiWcant are the waves generated by the wind. Second in importance is
the astronomical tide, which is a wave generated by the gravitational attraction
of the sun and moon. Other waves, which on the whole are less important but


-----

2 / Basic Coastal Engineering

that may have important consequences in some places, are seismically generated
surface waves (tsunamis) and waves generated by moving vessels.

The wind and related atmospheric pressure gradient will generate a storm

surge—the piling up of water along the coast when the wind blows in an onshore
direction. This raised water level can cause damage by Xooding and it allows
waves to attack the coast further inland. The wind will generate currents that
move along the coast. Coastal currents are also generated by the tide as it
propagates along the coast and alternately Xoods and ebbs through an inlet or
into an estuary. Further, the wind has direct consequences on the shore by
moving sand and causing structural damage.

Wind wave action causes the most signiWcant changes to a beach. The shore
normal beach proWle changes as sand is carried oVshore and back onshore over a
period of time. In many locations large volumes of sand are also carried along
the shore by the action of waves that obliquely approach the shore. Current
eVects often dominate at the entrances to bays and estuaries where higher Xow
velocities develop.

When structures are built along the coast their design must anticipate the

eVects of this dynamic wave and beach environment. This is important insofar as
the structures must remain stable and must not cause undesirable sand accumulation or erosion by interfering with on/oVshore and alongshore sediment transport processes.

Understanding and being able to manage the coastal environment is of critical

importance. About two-thirds of the world’s population lives on or near the coast,
and many others visit the coast periodically. This creates strong pressure for shore
development for housing and recreation and for shore protection from storminduced damage. Shore protection and stabilization problems often require regional solutions rather than a response by a single or small number of property
owners. Much of our commerce is carried by ships that must cross the coastline to
enter and exit ports. This requires the stabilization, maintenance, and protection
of coastal navigation channels. Coastal waters are also used for power plant
cooling water and as a receptacle for treated and untreated liquid wastes.

The importance of the coastal environment is demonstrated by events at Miami

Beach, Florida. In the early 1970s the beach at Miami Beach was in poor shape—a
narrow beach that was not very useful for recreation or eVective for storm surge
protection.Inthelate1970sabout15millioncubicyardsofsandwereplacedonthe
beach. Estimated annual beach attendance increased from 8 million in 1978 to 21
million in 1983 (Wiegel, 1992). This was twice the annual number of tourists who
visited Yellowstone Park, the Grand Canyon, and Yosemite Park combined
(Houston, 1995). Foreign visitors alone now spend more than 2 billion dollars a
year at Miami Beach, largely because of the improved beach conditions. The
expanded beach also has value because of the protection provided from potential
storm surge and wave damage to the coast. The capitalized cost of the project is just
3 million dollars per year (Houston, 1995).


-----

Coastal Engineering / 3

1.2 Coastal Engineering

Attempts to solve some coastal zone problems such as beach erosion and the
functional and structural design of harbors date back many centuries. Bruun
(1972) discusses early coastal erosion and Xooding control activities in Holland,
England, and Denmark in a review of coastal defense works as they have
developed since the tenth century. Inman (1974), from a study of early harbors
around the Mediterranean Sea, found that harbors demonstrating a ‘‘very
superior ‘lay’ understanding of waves and currents, which led to development
of remarkable concepts in working with natural forces’’ were constructed as
early as 1000–2000 B.C.

Coastal works have historically been the concern of civil and military engin
eers. The term ‘‘coastal engineer’’ seems to have come into general use as a
designation for a deWnable engineering Weld in 1950, with the meeting of the First
Conference on Coastal Engineering in Long Beach, California. In the preface to
the proceedings of that conference M.P. O’Brien wrote, ‘‘It (coastal engineering)
is not a new or separate branch of engineering and there is no implication
intended that a new breed of engineer, and a new society, is in the making.
Coastal Engineering is primarily a branch of Civil Engineering which leans
heavily on the sciences of oceanography, meteorology, Xuid mechanics, electronics, structural mechanics, and others.’’ Among the others one could include
geology and geomorphology, numerical and statistical analysis, chemistry, and
material science.

This deWnition is still essentially correct. However, coastal engineering has

dramatically grown in the past few decades. The Proceedings of the First
Conference on Coastal Engineering contained 35 papers; the Proceedings of
the 28th International Conference on Coastal Engineering held in 2002 contained 322 papers selected from over 600 abstracts presented to the conference.
In addition to the biannual International Conferences on Coastal Engineering
there are several specialty conferences held each year dealing with such subjects
as ports, dredging, coastal sediment, the coastal zone, coastal structures, wave
measurement and analysis, and coastal and port engineering in developing
countries. The American Society of Civil Engineers has a Waterway, Port,
Coastal, and Ocean Division which, along with magazines titled Coastal Engineering and Shore and Beach publish papers on all aspects of coastal engineering.
In addition, a growing number of general and specialized textbooks on coastal
engineering have been published.

Areas of concern to coastal engineers are demonstrated by the following list of

typical coastal engineering activities:

. Development (through measurement and hindcasts) of nearshore wave,
current, and water level design conditions


-----

4 / Basic Coastal Engineering

. Design of a variety of stable, eVective, and economic coastal structures
including breakwaters, jetties, groins, revetments, seawalls, piers, oVshore
towers, and marine pipelines

. Control of beach erosion by the design of coastal structures and/or by the
artiWcial nourishment of beaches

. Stabilization of entrances for navigation and water exchange by dredging,
construction of structures, and the mechanical bypassing of sediment
trapped at the entrances

. Prediction of inlet and estuary currents and water levels and their eVect on
channel stability and water quality

. Development of works to protect coastal areas from inundation by storm
surge and tsunamis

. Functional and structural design of harbors and marinas and their appurtenances including quays, bulkheads, dolphins, piers, and mooring systems

. Functional and structural design of oVshore islands and dredge spoil
disposal areas

. Monitoring various coastal projects through a variety of measurements in
the Weld.

A major source of support for coastal engineers is the available literature on

past coastal engineering works along with the design guidance published in textbooks; manuals from government agencies; and special studies conducted by
university, government, and consulting Wrm personnel. Additional design tools
generally fall into one of the following categories:

. Many aspects of coastal engineering analysis and design have a strong
analytical foundation. This includes theories for the prediction of individual wave characteristics and the properties of wave spectra, for the calculation of wave-induced forces on structures, for the eVect of structures on
wave propagation, and for the prediction of tide-induced currents and
water level changes.

. Many coastal engineering laboratories have two- and three-dimensional
Xumes in which monochromatic and spectral waves can be generated to
study fundamental phenomena as well as the eVects of waves in models of
prototype situations. Examples of model studies include wave propagation
toward the shore and into harbors, the stability of structures subjected to
wave attack and the amount of wave overtopping and transmission that
occurs at these structures, the response of beaches to wave attack, and the
stability and morphological changes at coastal inlets owing to tidal Xow
and waves.


-----

Coastal Engineering / 5

. Various computer models that numerically solve the basic wave, Xow, and
sediment transport equations have been developed. These include models
for wind wave prediction, for the analysis of wave transformation from
deep water to the nearshore zone, for the surge levels caused by hurricanes
and other storms, for the resonant response of harbors and other water
bodies to long period wave motion, and for the sediment transport
and resulting shoreline change caused by a given set of incident wave
conditions.

. An invaluable tool for coastal engineers is the collection of data in the Weld.
This includes measurements of wave conditions, current patterns, water
levels, shore plan and proWle changes, and wave-induced damage to structures. There is a great need for more postconstruction monitoring of the
performance of most types of coastal works. In addition, laboratory and
numerical models require prototype data so that the models can be adequately calibrated and veriWed.

The wind wave and surge levels that most coastal works are ultimately

exposed to are usually quite extreme. It is generally not economical to design
for these conditions. The design often proceeds for some lesser wave and surge
condition with the understanding that the structures will be repaired as needed.

Compared to most other areas of civil engineering (e.g., bridges, highways,

water treatment facilities), coastal engineering design is less controlled by code
requirements. This is because of the less predictable nature of the marine environment and the relative lack of an extensive experience base required to establish
codes.

1.3 Recent Trends

Some of the recent important trends in coastal engineering practice should be
noted.

With the explosion in the capabilities of computers there has been a parallel

explosion in the types and sophistication of numerical models for analysis of
coastal phenomena. In many, but not all, areas numerical models are supplementing and replacing physical models. Some areas such as storm surge prediction can
be eVectively handled only by a numerical model. On the other hand, some
problems such as wave runup and overtopping of coastal structures or the stability
of stone mound structures to wave attack are best handled in the laboratory.

There is a trend toward softer and less obtrusive coastal structures. For

example, oVshore breakwaters for shore protection and stabilization more commonly have their crest positioned just below the mean water level, where they still
have an ability to control incident wave action but where they also have less


-----

6 / Basic Coastal Engineering

negative aesthetic impact. In some coastal areas coastal structures are
discouraged.

There has been a signiWcant increase in the capability and availability of

instrumentation for Weld measurements. For example, three decades ago wave
gages commonly measured only the water surface Xuctuation at a point (i.e., the
diVerent directional components of the incident wave spectrum were not measured). Now directional spectral wave gages are commonly used in Weld studies.

Wave generation capabilities in laboratories have signiWcantly improved. Prior

to the 1960s only constant period and height (monochromatic) waves were
generated. In the 1970s one-dimensional spectral wave generators became common-place. Now directional spectral wave generators are found at many laboratories.

1.4 Coastal Engineering Literature

This text presents an introduction to coastal engineering; it is not a coastal
engineering design manual. For practical design guidance the reader should
see, for example, the design manuals published by the U.S. Army Corps of
Engineers including the Coastal Engineering Manual and the various Engineering Manuals dealing with coastal engineering topics.

A good source of detailed information on the various subjects encompassed by

coastal engineering is the broad range of reports published by many government
laboratories including the U.S. Army Coastal and Hydraulics Laboratory, the
Delft Hydraulics Laboratory (Netherlands), Hydraulics Research Limited
(Wallingford, England), the Danish Hydraulic Institute (Horsholm), and the
National Research Council (Ottawa, Canada). Several universities conduct
coastal engineering studies and publish reports on this work.

As mentioned previously, there are many general and specialty conferences

dealing with various aspects of coastal engineering. The published proceedings of
these conferences are an important source of information on the basic and
applied aspects of coastal engineering.

Many senior coastal engineers were introduced to coastal engineering by two

texts published in the 1960s: Oceanographical Engineering by R.L. Wiegel (Prentice-Hall, Englewood CliVs, NJ, 1964) and Estuary and Coastline Hydrodynamics
edited by A.T. Ippen (McGraw-Hill, New York, 1966). Since the 1960s a number
of texts on coastal engineering or a speciWc facet of coastal engineering have been
published. A selective list of these texts follows:

Abbott, M. B. and Price, W.A., Editors (1994), Coastal, Estuarial and Harbor Engineers’

Reference Book, E & FN Spon, London.


-----

Coastal Engineering / 7

Bruun, P., Editor (1985), Design and Construction of Mounds for Breakwaters and Coastal

Protection, Elsevier, Amsterdam.

Bruun, P. (1989), Port Engineering, Fourth Edition, 2 Vols., Gulf Publishing, Houston.

Dean, R.G. and Dalrymple, R.A. (1984), Water Wave Mechanics for Engineers and

Scientists, Prentice-Hall, Englewood CliVs, NJ.

Dean, R.G. and Dalrymple, R.A. (2002), Coastal Processes with Engineering Applications,

Cambridge University Press, Cambridge.

Dean, R.G. (2003) Beach Nourishment: Theory and Practice, World Scientific, Singapore.

Fredsoe´, J. and Deigaard, R. (1992), Mechanics of Coastal Sediment Transport, World

ScientiWc, Singapore.

Goda, Y. (1985), Random Seas and Design of Maritime Structures, University of Tokyo

Press, Tokyo.

Herbich, J.B., Editor (1990), Handbook of Coastal and Ocean Engineering, 3 Vols., Gulf

Publishing, Houston.

Horikawa, K., Editor, (1988), Nearshore Dynamics and Coastal Processes—Theory; Meas
urement and Predictive Models, University of Tokyo Press, Tokyo.

Hughes, S.A. (1993), Physical Models and Laboratory Techniques in Coastal Engineering,

World ScientiWc, Singapore.

Kamphius, J.W. (2000), Introduction to Coastal Engineering and Management, World

ScientiWc, Singapore.

Komar, P.D. (1998), Beach Processes and Sedimentation, Second Edition, Prentice Hall,

Englewood CliVs, NJ.

Pilarczyk, K.W., Editor (1990), Coastal Protection, A.A. Balkema, Rotterdam.

Sarpkaya, T. and Isaacson, M. (1981), Mechanics of Wave Forces on OVshore Structures,

Van Nostrand Reinhold, New York.

Sawaragi, T., Editor (1995), Coastal Engineering—Waves, Beaches, Wave-Structure Inter
actions, Elsevier, Amsterdam.

Sorensen, R.M. (1993), Basic Wave Mechanics for Coastal and Ocean Engineers, John

Wiley, New York.

Tucker, M.J. (1991), Waves in Ocean Engineering—Measurement, Analysis, Interpretation,

Ellis Horwood, New York.

Thorne, C.R., Abt, S.R., Barends, F.B.J., Maynord, S.T., and Pilarczyk, K.W., Editors

(1995), River, Coastal and Shoreline Protection, John Wiley, New York.

An increasing amount of Weld data and a number of useful publications and
software packages are becoming available over the internet. Two useful sites are
noaa.gov and bigfoot.wes.army.mil.


-----

8 / Basic Coastal Engineering

1.5 Summary

Coastal engineering is a unique branch of civil engineering that has undergone
signiWcant development in recent decades. Practitioners of this branch of engineering must be knowledgeable in a number of special subjects, one of which is the
mechanics of surface gravity waves. Basic two-dimensional wave theory and the
characteristics of these waves are the starting points for this text.

1.6 References

Bruun, P. (1972), ‘‘The History and Philosophy of Coastal Protection,’’ in Proceedings,

13th Conference on Coastal Engineering, American Society of Civil Engineers, Vancouver, pp. 33–74.

Houston, J.R. (1995), ‘‘The Economic Value of Beaches,’’ The Cercular, U.S. Army

Coastal Engineering Research Center, Vicksburg, MS, December, pp. 1–3.

Inman, D.L. (1974), ‘‘Ancient and Modern Harbors: A Repeating Phylogeny,’’ in Pro
ceedings, 14th Conference on Coastal Engineering, American Society of Civil Engineers,
Copenhagen, pp. 2049–2067.

U.S. Army Coastal Engineering Research Center (1984), Shore Protection Manual, Fourth

Edition, 2 Vols., U.S. Government Printing OYce, Washington DC.

Wiegel, R.L. (1992), ‘‘Dade County, Florida, Beach Nourishment and Hurricane Surge

Protection Project,’’ Shore and Beach, October, pp. 2–26.


-----

## 2

### Two-Dimensional Wave Equations and Wave Characteristics

A practicing coastal engineer must have a basic and relatively easy to use

theory that deWnes the important characteristics of two-dimensional waves. This
theory is required in order to analyze changes in the characteristics of a wave as it
propagates from the deep sea to the shore. Also, this theory will be used as a
building block to describe more complex sea wave spectra. Such a theory—the
small amplitude wave theory—is presented in this chapter along with related
material needed to adequately describe the characteristics and behavior of twodimensional waves.

2.1 Surface Gravity Waves

When the surface of a body of water is disturbed in the vertical direction, the
force of gravity will act to return the surface to its equilibrium position. The
returning surface water has inertia that causes it to pass its equilibrium position
and establish a surface oscillation. This oscillation disturbs the adjacent water
surface, causing the forward propagation of a wave.

A wave on the water surface is thus generated by some disturbing force which

may typically be caused by the wind, a moving vessel, a seismic disturbance of
the shallow sea Xoor, or the gravitational attraction of the sun and moon. These
forces impart energy to the wave which, in turn, transmits the energy across the
water surface until it reaches some obstacle such as a structure or the shoreline
which causes the energy to be reXected and dissipated. The wave also transmits a
signal in the form of the oscillating surface time history at a point.

As a wave propagates, the oscillatory water motion in the wave continues

because of the interaction of gravity and inertia. Since water particles in the wave
are continuously accelerating and decelerating as the wave propagates, dynamic
pressure gradients develop in the water column. These dynamic pressure gradients are superimposed on the vertical hydrostatic pressure gradient. As the wave


-----

10 / Basic Coastal Engineering

propagates energy is dissipated, primarily at the air–water boundary and, in
shallower water, at the boundary between the water and the sea Xoor.

The diVerent wave generating forces produce waves with diVerent periods.

Wind-generated waves have a range of periods from about 1 to 30 s with the dominant periods for ocean storm waves being between 5 and 15 s. Vessel-generated
waves have shorter periods, typically between 1 and 3 s. Seismically generated
waves (tsunamis) have longer periods from about 5 min to an hour and the
dominant periods of the tide are around 12 and 24 hours.

Wind waves in the ocean have a height (vertical distance crest to trough) that is

typically less than 10 ft, but it can exceed 20 ft during signiWcant storms. Vessel
waves rarely exceed 3 ft in height. At sea, tsunami waves are believed to have a
height of 2 ft or less, but as the tsunami approaches the coast heights often increase
to greater than 10 ft, depending on the nature of the nearshore topography.
Similarly, tide wave heights (tide ranges) in the deep ocean are relatively low, but
along the coast tide ranges in excess of 20 ft occur at a number of locations.

Wind-generated waves are complex, consisting of a superimposed multitude of

components having diVerent heights and periods. In this chapter we consider the
simplest theory for the characteristics and behavior of a two-dimensional monochromatic wave propagating in water of constant depth. This will be useful in
later chapters as a component of the spectrum of waves found at sea. It is also
useful for Wrst-order design calculations where the height and period of this
monochromatic wave are selected to be representative of a more complex wave
spectrum. Also, much laboratory research has used, and will continue to use,
monochromatic waves for basic studies of wave characteristics and behavior
such as the wave-induced force on a structure or the nature of breaking waves.

The simplest and often most useful theory (considering the eVort required in

its use) is the two-dimensional small-amplitude or linear wave theory Wrst presented by Airy (1845). This theory provides equations that deWne most of the
kinematic and dynamic properties of surface gravity waves and predicts these
properties within useful limits for most practical circumstances. The assumptions
required to derive the small-amplitude theory, an outline of its derivation, the
pertinent equations that result, and the important characteristics of waves described by these equations are presented in this chapter. More detail on the
small-amplitude wave theory can be found in Wiegel (1964), Ippen (1966), Dean
and Dalrymple (1984), U.S. Army Coastal Engineering Research Center (1984),
and Sorensen (1993).

2.2 Small-Amplitude Wave Theory

The small-amplitude theory for two-dimensional, freely propagating, periodic
gravity waves is developed by linearizing the equations that deWne the free
surface boundary conditions. With these and the bottom boundary condition,


-----

Two-Dimensional Wave Equations and Wave Characteristics / 11

a periodic velocity potential is sought that satisWes the requirements for irrotational Xow. This velocity potential, which is essentially valid throughout the
water column except at the thin boundary layers at the air–water interface and at
the bottom, is then used to derive the equations that deWne the various wave
characteristics (e.g., surface proWle, wave celerity, pressure Weld, and particle
kinematics). SpeciWcally, the required assumptions are:

1. The wateris homogeneous and incompressible, and surface tension forcesare

negligible. Thus, there are no internal pressure or gravity waves aVecting the
Xow, and the surface waves are longer than the length where surface tension
eVects are important (i.e., wave lengths are greater than about 3 cm).

2. Flow is irrotational. Thus there is no shear stress at the air–sea interface or

at the bottom. Waves under the eVects of wind (being generated or diminished) are not considered and the Xuid slips freely at the bottom and other
solid Wxed surfaces. Thus the velocity potential f must satisfy the Laplace
equation for two-dimensional Xow:

@[2]f

(2:1)

@x[2][ þ][ @]@[2]z[f][2][ ¼][ 0]


where x and z are the horizontal and vertical coordinates, respectively.

3. The bottom is stationary, impermeable, and horizontal. Thus, the bottom is

not adding or removing energy from the Xow or reXecting wave energy.
Waves propagating over a sloping bottom, as for example when waves
propagate toward the shore in the nearshore region, can generally be
accommodated by the assumption of a horizontal bottom if the slope is
not too steep.

4. The pressure along the air–sea interface is constant. Thus, no pressure is

exerted by the wind and the aerostatic pressure diVerence between the wave
crest and trough is negligible.

5. The wave height is small compared to the wave length and water depth.

Since particle velocities are proportional to the wave height, and wave
celerity (phase velocity) is related to the water depth and the wave length,
this requires that particle velocities be small compared to the wave celerity.
This assumption allows one to linearize the higher order free surface
boundary conditions and to apply these boundary conditions at the still
water line rather than at the water surface, to obtain an easier solution.
This assumption means that the small-amplitude wave theory is most
limited for high waves in deep water and in shallow water and near wave
breaking where the waves peak and wave crest particle velocities approach
the wave phase celerity. Given this, the small-amplitude theory is still
remarkably useful and extensively used for wave analysis.


-----

12 / Basic Coastal Engineering

z

L

H

w

u

ε

ζ

d

Particle
d + z orbit

Figure 2.1. DeWnition of progressive surface wave parameters.


x


L

_C_

H η

w

Still water

u level

ε

ζ

d

Particle
d + z orbit


Figure 2.1 depicts a monochromatic wave traveling at a phase celerity C on water
of depth d in an x, z coordinate system. The x axis is the still water position and
the bottom is at z d. The wave surface proWle is deWned by z h, where h is
¼ � ¼
a function of x and time t. The wave length L and height H are as shown in the
Wgure. Since the wave travels a distance L in one period T,

C ¼ L=T (2:2)

The arrows at the wave crest, trough, and still water positions indicate the
directions of water particle motion at the surface. As the wave propagates
from left to right these motions cause a water particle to move in a clockwise
orbit. The water particle velocities and orbit dimensions decrease in size with
increasing depth below the still water line. Particle orbits are circular only under
certain conditions as deWned in Section 2.4.

The horizontal and vertical components of the water particle velocity at any

instant are u and w, respectively. The horizontal and vertical coordinates of a
water particle at any instant are given by � and e, respectively. The coordinates
are referenced to the center of the orbital path that the particle follows. At any
instant, the water particle is located a distance d ( z) d z above the
� � ¼ þ
bottom.

The following dimensionless parameters are often used:

k ¼ 2p=L(wave number)

s ¼ 2p=T(wave angular frequency)

We also use the terms ‘‘wave steepness’’ deWned as the wave height divided by the
wave length (i.e., H/L) and ‘‘relative depth’’ deWned as the water depth divided
by the wave length (i.e., d/L) in discussions of wave conditions.


-----

Two-Dimensional Wave Equations and Wave Characteristics / 13

The small-amplitude wave theory is developed by solving Eq. (2.1) for the

domain depicted in Figure 2.1, with the appropriate boundary conditions for
the free surface (2) and the bottom (1).

At the bottom there is no Xow perpendicular to the bottom which yields the

bottom boundary condition (BBC):

w ¼ [@][f] (2:3)

@z [¼][ 0 at][ z][ ¼ �][d]

At the free surface there is a kinematic boundary condition (KSBC) that relates
the vertical component of the water particle velocity at the surface to the surface
position:


w ¼ [@][h] (2:4)

@t [þ][ u][ @]@[h]x [at][ z][ ¼][ h]

The Bernoulli equation for unsteady irrotational Xow may be written


1

(2:5)

2 [(][u][2][ þ][ w][2][)][ þ][ p]r [þ][ gz][ þ][ @]@[f]t [¼][ 0]


where g is the acceleration of gravity, p is the pressure, and r is the Xuid density.
At the surface where the pressure is zero the dynamic boundary condition
(DSBC) becomes

1

(2:6)

2 [(][u][2][ þ][ w][2][)][ þ][ gz][ þ][ @]@[f]t [¼][ 0 at][ z][ ¼][ h]

The KSBC and the DSBC have to be linearized and applied at the still water line
rather than at the a priori unknown water surface. This yields for the KSBC

w ¼ [@][h] (2:7)

@t [at][ z][ ¼][ 0]


and for the DSBC

gh þ [@][f] (2:8)

@t [¼][ 0 at][ z][ ¼][ 0]

Employing the Laplace equation, the BBC, and the linearized DSBC, we can
derive the velocity potential for the small-amplitude wave theory (see Ippen,
1966; Sorensen, 1978; or Dean and Dalrymple, 1984). The most useful form of
this velocity potential is


f [gH]
¼

2s


cosh k(d z)
þ

sin (kx � s t) (2:9)
cosh kd


-----

14 / Basic Coastal Engineering

The velocity potential demonstrates an important point. Since the wave length or
wave number (k ¼ 2p=L) depends on the wave period and water depth [see Eq.
(2.14)], when the wave height and period plus the water depth are known the
wave is fully deWned and all of its characteristics can be calculated.

We can insert the velocity potential into the linearized DSBC with z 0 to
¼

directly determine the equation for the wave surface proWle:

h ¼ [H] (2:10)

2 [cos (][kx][ �] [s][ t][)]


which can also be written


� �

h [H]
¼

2 [cos 2][p][ x]L T

[�] [t]


(2:11)


by inserting the wave number and wave angular frequency. Thus, the smallamplitude wave theory yields a cosine surface proWle. This is reasonable for lowamplitude waves, but with increasing wave amplitude the surface proWle becomes
vertically asymmetric with a more peaked wave crest and a Xatter wave trough
(as will be shown in Chapter 3).

Combining the KSBC and the DSBC by eliminating the water surface eleva
tion yields

@[2]f

@t[2][ þ][ g][ @]@[f]z [¼][ 0 at][ z][ ¼][ 0]


Then, inserting the velocity potential, diVerentiating, and rearranging we have

s[2] gk tanh kd
¼

or


C [s]
¼

k

[¼]


rffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffig

k [tanh][ kd]


and


C
¼


rffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi

gL
2p [tanh 2][p]L[d]


(2:12)


Equation (2.12) indicates that for small-amplitude waves, the wave celerity is
independent of the wave height. As the wave height increases there is a small but
growing dependence of the wave celerity on the wave height (see Chapter 3).
Equation (2.12) can also be written [by inserting Eq. (2.2)]


-----

Two-Dimensional Wave Equations and Wave Characteristics / 15


C ¼ [gT] (2:13)

2p [tanh 2][p]L[d]

L ¼ [gT] [2] (2:14)

2p [tanh 2][p]L[d]

From Eq. (2.14), if the waterdepth and the wave period are known, the wave length
can be calculated by trial and error. Then the celerity can be determined from
C ¼ L=T. Tables are available (U.S. Army Coastal Engineering Research Center,
1984) for the direct determination of L given the water depth and wave period.

Equations (2.12) to (2.14) collectively are commonly known as the dispersion

equation. For a spectrum of waves having diVerent periods (or lengths), the
longer waves will propagate at a higher celerity and move ahead while the shorter
waves will lag behind.

It can be demonstrated (see Ippen, 1966) that as a wave propagates from deep

water in to the shore, the wave period will remain constant because the number
of waves passing sequential points in a given interval of time must be constant.
Other wave characteristics including the celerity, length, height, surface proWle,
particle velocity and acceleration, pressure Weld, and energy will all vary during
passage from deep water to the nearshore area.

2.3 Wave ClassiWcation

An important classiWcation of surface waves is based on the relative depth (d/L).
When a wave propagates from deep water oVshore in to shallower water nearshore the wave length decreases [see Eq. (2.14)], but at a slower rate than that at
which the depth decreases. Thus, the relative depth decreases as a wave approaches the shore. When d/L is greater than approximately 0.5, tanh (2pd=L)
is essentially unity and Eqs. (2.12) to (2.14) reduce to


r


ffiffiffiffiffiffiffiffi
gLo

2p


Co ¼


(2:15)


Co ¼ [gT]2p (2:16)


and


Lo ¼ [gT]2p[2] (2:17)

respectively. Waves in this region are called deep water waves and this condition
is commonly denoted by the subscript zero (except for the wave period which is


-----

16 / Basic Coastal Engineering

not depth dependent and thus does not change as the relative depth decreases).
Wave particle velocities and orbit dimensions decrease with increasing distance
below the free surface. In deep water at a depth of �z=L > 0:5 the particle
velocities and orbit dimensions are close to zero. Since for d=L > 0:5 the waves
do not interact with the bottom, wave characteristics are thus independent of the
water depth [e.g., see Egs. (2.15) to (2.17)].

Example 2.3-1

A wave in water 100 m deep has a period of 10 s and a height of 2 m. Determine
the wave celerity, length, and steepness. What is the water particle speed at the
wave crest?

Solution:

Assume that this is a deep water wave. Then, from Eq. (2.17)

Lo ¼ [9][:][81(10)]2p [2] ¼ 156 m

Since the depth is greater than half of the calculated wave length, the wave is in
deep water and the wave length is 156 m. [Otherwise, Eq. (2.14) would have to be
used to calculate the wave length.] The wave celerity is from Eq. (2.2)

Co ¼ [156]10

[¼][ 15][:][6][ m][=][s]

and the steepness is

Ho

[2]
¼

Lo 156 [¼][ 0][:][013]

For deep water the particle orbits are circular having a diameter at the surface
equal to the wave height. Since a particle completes one orbit in one wave period,
the particle speed at the crest would be the orbit circumference divided by the
period or

uc ¼ [p]T[H][o] ¼ [3][:][14(2)]10 ¼ 0:63 m=s

Note that this is much less than Co.

When the relative depth is less than 0.5 the waves interact with the bottom.

Wave characteristics depend on both the water depth and the wave period, and


-----

Two-Dimensional Wave Equations and Wave Characteristics / 17

continually change as the depth decreases. The full dispersion equations must be
used to calculate wave celerity or length for any given water depth and wave
period. Dividing Eq. (2.13) by Eq. (2.16) or Eq. (2.14) by Eq. (2.17) yields


C

Co



[L]
¼

Lo


¼ tanh [2][p][d] (2:18)

L


which is a useful relationship that will be employed in a later chapter. Waves
propagating in the range of relative depths from 0.5 to 0.05 are called intermediate or transitional water waves.

When the relative depth is less than approximately 0.05, tanh (2pd=L) ap
proximately equals 2pd=L and the dispersion equation yields


ffiffiffiffiffiffi
gd


(2:19)


C
¼


p


or


T (2:20)


L
¼


pffiffiffiffiffiffi

gd


Waves in this region of relative depths are called shallow water waves. In shallow
water the small-amplitude wave theory gives a wave celerity that is independent of
wave period and dependent only on the water depth (i.e., the waves are not period
dispersive). The Wnite-amplitude wave theories presented in the next chapter show
that the shallow water wave celerity is a function of the water depth and the wave
height so that in shallow water waves are amplitude dispersive. Remember that it is
the relative depth, not the actual depth alone, that deWnes deep, intermediate, and
shallow water conditions. For example, the tide is a very long wave that behaves as
a shallow water wave in the deepest parts of the ocean.

Example 2.3-2

Consider the wave from Example 2.3-1 when it has propagated in to a nearshore
depth of 2.3 m. Calculate the wave celerity and length.

Solution:

Assuming this is a shallow water wave, Eq. (2.19) yields


¼ 4:75 m=s


C
¼


pffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi

9:81(2:3)


and Eq. (2.2) yields

L ¼ 4:75(10) ¼ 47:5 m

So d=L ¼ 2:3=47:5 ¼ 0:048 < 0:05 and the assumption of shallow water was
correct. Compare these values to the results from Example 2.3-1


-----

18 / Basic Coastal Engineering

2.4 Wave Kinematics and Pressure

Calculation of the wave conditions that will cause the initiation of bottom
sediment motion, for example, requires a method for calculating water particle
velocities in a wave. The water particle velocity and acceleration as well as the
pressure Weld in a wave are all needed to determine wave-induced forces on
various types of coastal structures.

Wave Kinematics

The horizontal and vertical components of water particle velocity (u and w,
respectively) can be determined from the velocity potential where

u ¼ [@][f] w ¼ [@][f]

@x [,] @z


This yields, after inserting the dispersion relationship and some algebraic manipulation


�cosh k(d z)�

þ

u [p][H]
¼

T sinh kd


and


�sinh k(d z)�

þ

w [p][H]
¼

T sinh kd


cos (kx � st) (2:21)

sin (kx � st) (2:22)


Equations (2.21) and (2.22) give the velocity components at the point (x, z) as
�
a function of time as diVerent water particles pass through this point.

Note that each velocity component consists of three parts: (1) the surface deep

water particle speed pH=T, (2) the term in brackets which accounts for particle
velocity variation over the vertical water column at a given location and for
particle velocity variation caused by the wave moving from deep to shallow
water, and (3) a phasing term dependent on position in the wave and time.
Note that d z is the distance measured up from the bottom as demonstrated
þ
in Figure 2.1. Also, as would be expected, the horizontal and vertical velocity
components are 908 out of phase.

The horizontal component of particle acceleration ax may be written

ax ¼ u @[@]x[u] [þ][ w][ @]@[u]z [þ][ @]@[u]t


where the Wrst two terms on the righthand side are the convective acceleration
and the third term is the local acceleration. The magnitude of the convective


-----

Two-Dimensional Wave Equations and Wave Characteristics / 19

acceleration for a small-amplitude wave is of the order of the wave steepness
(H/L) squared while the magnitude of the local acceleration is of the order of
the wave steepness. Since the wave steepness is much smaller that unity, we can
usually neglect the higher order convective acceleration term in determining the
particle acceleration. This yields


ax ¼ [2][p]T[2][2][H]


�cosh k(d z)�

þ

sin (kx � st) (2:23)

sinh kd


for the horizontal component and


az ¼ � [2][p]T[2][2][H]


�sinh k(d z)�

þ

cos (kx � st) (2:24)

sinh kd


for the vertical component of acceleration. The terms in brackets are the same
for both the particle velocity and acceleration components. The cosine/sine terms
indicate that the particle velocity components are 908 out of phase with the
acceleration components. This is easily seen by considering a particle following
a circular orbit. The velocity is tangent to the circle and the acceleration is
toward the center of the circle or normal to the velocity.

As water particles orbit around a mean position (see Figure 2.1) the horizontal

and vertical coordinates of the particle position relative to the mean position are
given by z and e, respectively. These components can be found by integrating the
particle velocity components with time. This yields


z
¼ [�][H]

2


�cosh k(d z)�

þ

sinh kd


sin (kx � st) (2:25)


and


e ¼ [H]

2


�sinh k(d z)�

þ

sinh kd


cos (kx � st) (2:26)


where H/2 is the orbit radius for a particle at the surface of a deep water wave.
The position coordinates are evaluated for the orbit of the particle that is passing
through the point x, z at that instant, but the small-amplitude assumptions
�
allow us to assume that these coordinates [given by Eqs. (2.25) and (2.26)] apply
to the orbit mean position.

As a wave propagates from deep water into shallow water, the particle orbit

geometries undergo the transformation depicted in Figure 2.2. In deep water the
orbits are circular throughout the water column but decrease in diameter with
increasing distance below the water surface, to approximately die out at a distance


-----

20 / Basic Coastal Engineering

L/2

Shallow

Deep

Figure 2.2. Deep and shallow water surface proWles and particle orbits.


SWL


L/2

Shallow


of L/2. In transitional to shallow water, the orbits reach the bottom and become
elliptical—with the ellipses becoming Xatter near the bottom. At the bottom the
particles follow a reversing horizontal path. (This is for the assumed irrotational
motion—for real conditions a bottom boundary layer develops and the horizontal
dimension of the particle orbit reduces to zero at the bottom.) Since the terms in
brackets are the same for the respective velocity, acceleration, and displacement
equations, the particle velocity and acceleration component magnitudes demonstrate the same spatial change as do the displacement coordinates.

According to the small-amplitude theory surface waves have a sinusoidal

surface proWle. This is reasonable for low steepness waves in deep water. But,
for steeper deep water waves or as waves propagate into transitional and shallow
water the surface proWle becomes trochoidal, having long Xat troughs and
shorter peaked crests (see Figure 2.2). The amplitude of the crest increases
while the amplitude of the trough decreases. In transitional and shallow water,
particles still move in essentially closed orbits. Since they must travel the same
distance forward under the crest in less time (owing to the trochoidal proWle) as
they travel back under the trough in more time, peak velocities under the wave
crest will exceed those under the trough. As with the proWle asymmetry, this
velocity asymmetry is not predicted by the small amplitude wave theory.

It is useful to consider the deep and shallow water limits for the term in

brackets in the particle velocity, acceleration, and orbit displacement equations.
At these limits we have:

Deep water: [cosh][ k][(][d][ þ][ z][)] ¼ [sinh][ k][(][d][ þ][ z][)] ¼ e[kz] (2:27)

sinh kd sinh kd


Shallow water: [cosh][ k][(][d][ þ][ z][)] ¼ [1] (2:28)

sinh (kd) kd

sinh k(d z)
þ

¼ 1 þ [z] (2:29)
sinh kd d


-----

Two-Dimensional Wave Equations and Wave Characteristics / 21

Substitution of Eq. (2.27) into Eqs. (2.21) to (2.26) indicates that, in deep water,
the particle velocity, acceleration, and orbit displacement decay exponentially
with increasing distance below the still water line. At z ¼ �L=2 they are reduced
to 4.3% of their value at the surface.

Substitution of Eqs. (2.28) and (2.29) into Eqs. (2.21) and (2.22) respectively

yields (after some algebraic manipulation) the following equations for water
particle velocity in shallow water:


rffiffiffig

u [H]
¼

2 d


cos (kx � st) (2:30)


w [p][H] �1 [z]�
¼ þ

T d


sin (kx � st) (2:31)


Equation (2.30) indicates that, in shallow water, the horizontal component of
water particle velocity is constant from the water surface to the bottom. The
vertical component of particle velocity can be seen from Eq. (2.31) to decrease
linearly from a maximum at the water surface to zero at the bottom. Similar
statements can be made for the particle acceleration and orbit dimensions.

Pressure Field

Substitution of the velocity potential into the linearized form of the equation of
motion [Eq. (2.5) without the velocity squared terms] yields the following equation for the pressure Weld in a wave:


�cosh k(d z)�

þ

p rgz [r][gH]
¼ � þ

2 cosh kd


cos (kx � st) (2:32)


The Wrst term on the right gives the normal hydrostatic pressure variation and
the second term is the dynamic pressure variation owing to the wave-induced
particle acceleration. These components are plotted in Figure 2.3 for vertical
sections through the wave crest and trough. Since particles under the crest are
accelerating downward, a downward dynamic pressure gradient is required. The
reverse is true under a wave trough. Halfway between the crest and trough the
acceleration is horizontal so the vertical pressure distribution is hydrostatic.
Equation (2.32) is not valid above the still water line owing to the linearization
of the DSBC and its application at the still water line. Above the still water line
the pressure must regularly decrease to zero at the water surface.

In deep water, the dynamic pressure reduces to near zero at z ¼ �L=2. A

pressure gage at this depth would essentially measure the static pressure for the
given depth below the still water line. A pressure gage (located above �L=2) can
be used as a wave gage. The period of the pressure Xuctuation is the wave period
which can be used to calculate the wave length from the dispersion equation. The


-----

22 / Basic Coastal Engineering

Dynamic

Static Static

Total

− z ~ L/2 ~

Figure 2.3. Deep water wave vertical pressure distributions.


SWL


Dynamic

Dynamic

Static Total Static Total


wave height can then be calculated from Eq. (2.32), assuming the position of the
gage, the wave period and length, and the water depth are known.

Note that the term in brackets diVers from the terms in brackets for the

particle velocity, acceleration, and orbit displacement equations. At the deep
and shallow water limits we have,


cosh k(d z)
þ

e[kz](deep water)
¼
cosh kd

1(shallow water)
¼


(2:33)


Thus, from the small-amplitude wave theory, in deep water there is also an
exponential decay in the dynamic pressure with distance below the still water
line. In shallow water the total pressure distribution is given by

p ¼ rg(h � z) (2:34)

2.5 Energy, Power, and Group Celerity

An important characteristic of gravity waves is that they have mechanical energy
and that this energy is transmitted forward as they propagate. It is important to
be able to quantify this energy level and the rate of energy transmission (energy
Xux or power) for a given wave height and period and water depth.

Wave Energy

The total mechanical energy in a surface gravity wave is the sum of the kinetic
and potential energies. Equations for each may be derived by considering Figure
2.4. The kinetic energy for a unit width of wave crest and for one wave length Ek


-----

Two-Dimensional Wave Equations and Wave Characteristics / 23

SWL

w

d + η u

dz

dx

Figure 2.4. DeWnition sketch for wave energy derivation.

is equal to the integral over one wave length and the water depth of one-half
times the mass of a diVerential element times the velocity of that element
squared. Thus


w

d + η u

dz

dx


o
Z

�d


Ek ¼


L
Z

o


1
2 [r][dxdz][(][u][2][ þ][ w][2][)]


where the upper limit of the vertical integral is taken as zero in accord with the
assumptions of the small-amplitude wave theory. Inserting the velocity terms

[Eqs. (2.21) and (2.22)], integrating, and performing the required algebraic
manipulation yields the kinetic energy

Ek ¼ [r][gH]16[2][L]

If we subtract the potential energy of a mass of still water (with respect to the
bottom) from the potential energy of the wave form shown in Figure 2.4 we will
have the potential energy due solely to the wave form. This gives the potential
energy per unit wave crest width and for one wave length Ep as


Ep ¼


L
Z

o


� � ��d

rg(d h) [d][ þ][ h] dx rgLd
þ �

2 2


The surface elevation as a function of x is given by Eq. (2.10) with t 0.
¼
Performing the integration and simplifying yields

Ep ¼ [r][gH]16[2][L]

Thus, the kinetic and potential energies are equal and the total energy in a wave
per unit crest width E is

E ¼ Ek þ Ep ¼ [r][gH]8 [2][L] (2:35)


-----

24 / Basic Coastal Engineering

A wave propagating through a porous structure, for example, where the water
depth is the same on both sides of the structure, will have the same period and
wave length on both sides. Thus, a reduction of wave energy because of reXection
from the structure and viscous dissipation within the structure will result in a
decrease in the wave height. A 50% reduction in wave energy would result in only
a 29% decrease in the wave height because the wave energy is proportional to the
wave height squared.

Both the kinetic and potential energies are variable from point to point along a

wave length. However, a useful concept is the average energy per unit surface
area given by

E
E� ¼ (2:36)

L(1) 8

[¼][ r][gH] [2]


This is usually known as the energy density or speciWc energy of a wave.
Equations (2.35) and (2.36) apply for deep to shallow water within the limits
of the small-amplitude wave theory.

Wave Power

Wave power P is the wave energy per unit time transmitted in the direction of
wave propagation. Wave power can be written as the product of the force acting
on a vertical plane normal to the direction of wave propagation times the particle
Xow velocity across this plane. The wave-induced force is provided by the
dynamic pressure (total pressure minus hydrostatic pressure) and the Xow velocity is the horizontal component of the particle velocity. Thus


o
Z

�d


p [1]
¼

T


T
Z

o


(p rgz)udzdt
þ


where the term in parentheses is the dynamic pressure. Inserting the dynamic
pressure from Eq. (2.32) and the horizontal component of velocity from Eq.
(2.21) and integrating leads to

P [r][gH] [2][L] �1 2kd �
¼ þ

16T sinh 2kd


or

Letting


� 2kd �

P [E] 1
¼ þ

2T sinh 2kd

� 2kd �

n [1] 1
¼ þ

2 sinh 2kd


(2:37)

(2:38)


-----

Two-Dimensional Wave Equations and Wave Characteristics / 25

Equation (2.37) becomes

P ¼ [nE] (2:39)

T

The value of n increases as a wave propagates toward the shore from 0.5 in deep
water to 1.0 in shallow water. Equation (2.39) indicates that n can be interpreted
as the fraction of the mechanical energy in a wave that is transmitted forward
each wave period.

As a train of waves propagates forward the power at one point must equal the

power at a subsequent point minus the energy added, and plus the energy
dissipated and reXected per unit time between the two points. For Wrst-order
engineering analysis of waves propagating over reasonably short distances it is
common to neglect the energy added, dissipated, or reXected, giving


�nE�

P
¼

T 1


�nE�

¼

T 2


¼ constant (2:40)


Equation (2.40) indicates that, for the assumptions made, as a two-dimensional
wave travels from deep water to the nearshore the energy in the wave train
decreases at a rate inversely proportional to the increase in n since the wave
period is constant.

As waves approach the shore at an angle and propagate over irregular hy
drography they vary three-dimensionally owing to refraction. (See Chapter 4 for
further discussion and analysis of wave refraction.) If we construct lines that are
normal or orthogonal to the wave crests as a wave advances and assume that no
energy propagates along the wave crest (i.e., across orthogonal lines) the energy
Xux between orthogonals can be assumed to be constant. If the orthogonal
spacing is denoted by B, Eq. (2.40) can be written


�BnE�


�BnE�

¼

T 2


T


1


constant
¼


Inserting the wave energy from Eq. (2.35) yields


H1
H2


¼


rnffiffiffiffiffiffiffiffiffiffi2L2rffiffiffiffiffiffiB2

n1L1 B1


(2:41)


The Wrst term on the right represents the eVects of shoaling and the second term
represents the eVects of orthogonal line convergence or divergence owing to
refraction. These are commonly called the coeYcient of shoaling Ks and the
coeYcient of refraction Kr respectively.

Equation (2.41) allows us to calculate the change in wave height as a wave

propagates from one water depth to another depth. Commonly, waves are


-----

26 / Basic Coastal Engineering

predicted for some deep water location and then must be transformed to some
intermediate or shallow water depth nearshore using Eq. (2.41). For this, Eq.
(2.41) becomes


H

Ho


¼


rffiffiffiffiffiffiffiffiffirffiffiffiffiffiffi

Lo Bo


2nL


(2:42)


or


B

ffiffiffiffiffiffi
Bo

B


H

Ho


¼ [H]0

Ho


r


where the prime denotes the change in wave height from deep water to the point
of interest considering only two-dimensional shoaling eVects.

Figure 2.5 is a plot of H=H 0 o versus d/L and d=Lo from deep to shallow water.

Initially, as a wave enters intermediate water depths the wave height decreases
because n increases at a faster rate than L decreases [see Eq. (2.42)]. H=H 0 o

reaches a minimum value of 0.913 at d=L ¼ 0:189(d=Lo ¼ 0:157). Shoreward of
this point the wave height grows at an ever-increasing rate until the wave
becomes unstable and breaks.

1.6

1.4

H

H0[9]


1.2

1.0

0.8


0


0.1 0.2 0.3 0.4 0.5 0.6 0.7

(0.056) (0.170) (0.287) (0.395) (0.498) (0.599) (0.700)

d / L (d / Lo)


Figure 2.5. Dimensionless wave height versus relative depth for two-dimensional wave

transformation.


-----

Two-Dimensional Wave Equations and Wave Characteristics / 27

Example 2.5-1

Consider the wave from Example 2.3–1 when it has propagated into a water
depth of 10 m without refracting and assuming energy gains and losses can be
ignored. Determine the wave height and the water particle velocity and pressure
at a point 1 m below the still water level under the wave crest. (Assume fresh
water.)

Solution:

From Example 2.3–1 we have Lo ¼ 156 m and Eq. (2.14) gives


which can be solved by trial to yield L ¼ 93:3 m. Then, k ¼ 2p=93:3 ¼ 0:0673 m[�][1]

and from Eq. (2.38)

� 2(0:0673)(10) �

n ¼ [1] 1 þ ¼ 0:874

2 sinh (2(0:0673)(10)

With Kr ¼ 1, Eq. (2.42) yields

sffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi

156

H ¼ 2 ¼ 1:97 m

2(0:874)(93:3)

At the crest of the wave cos (kx st) 1, and z 1, so Eq. (2.21) gives
� ¼ ¼ �

u ¼ [p][(1][:][97)] � cosh (0:0673)(9) � ¼ 1:01 m=s

10 sinh (0:0673)(10)

which is the total particle velocity since w 0 under the wave crest. Equation
¼
(2.32) gives

� cosh (0:0673)9 �

P ¼ �1000(9:81)( � 1) þ [1000(9][:][81)(1][:][97)]

2 cosh (0:0673)10

¼ 19; 113 N=m[2]

Remember, Eqs. (2.40) to (2.42) neglect energy transfer to and from waves by
surface and bottom eVects. The nature of these eVects is discussed brieXy below.
Bottom eVects, of course, require that the water depth be suYciently shallow for
a strong interaction between the wave train and the bottom.


-----

28 / Basic Coastal Engineering

Wave ReXection

If the bottom is other than horizontal, a portion of the incident wave energy will
be reXected seaward. This reXection is generally negligible for wind wave periods
on typical nearshore slopes. However, for longer period waves and steeper
bottom slopes wave reXection would not be negligible. Any sharp bottom
irregularity such as a submerged structure of suYcient size will also reXect a
signiWcant portion of the incident wave energy.

Wind EVects

Nominally, if the wind has a velocity component in the direction of wave
propagation that exceeds the wave celerity the wind will add energy to the
waves. If the velocity component is less than the wave celerity or the wind
blows opposite to the direction of wave propagation the wind will remove energy
from the waves. For typical nonstormy wind conditions and the distances from
deep water to the nearshore zone found in most coastal locations, the wind eVect
can be neglected in the analysis of wave conditions nearshore.

Bottom Friction

As the water particle motion in a wave interacts with a still bottom, an unsteady
oscillatory boundary layer develops near the bottom. For long period waves in
relatively shallow water this boundary layer can extend up through much of the
water column. But, for typical wind waves the boundary layer is quite thin
relative to the water depth, and if propagation distances are not too long and
the bottom is not too rough, bottom friction energy losses can be neglected.

Bottom Percolation

If the bottom is permeable to a suYcient depth, the wave-induced Xuctuating
pressure distribution on the bottom will cause water to percolate in and out of
the bottom and thus dissipate wave energy.

Bottom Movement

When a wave train propagates over a bottom consisting of soft viscous material
(such as the mud deposited at the Mississippi River Delta) the Xuctuating
pressure on the bottom can set the bottom in motion. Viscous stresses in the
soft bottom dissipate energy provided by the waves.

Wave Group Celerity

Consider a long constant-depth wave tank in which a small group of deep water
waves is generated. As the waves travel along the tank, waves in the front of the
group will gradually decrease in height and, if the tank is long enough, disappear


-----

Two-Dimensional Wave Equations and Wave Characteristics / 29

in sequence starting with the Wrst wave in the group. As the waves in the front
diminish in height, new waves will appear at the rear of the group and commence
to grow. One new wave will appear each wave period so the total number of
waves in the group will continually increase. This phenomenon causes the wave
group to have a celerity that is less than the celerity of the individual waves in the
group. Since the total energy in the group is constant (neglecting dissipation) the
average height of the waves in the group will continually decrease.

An explanation for this phenomenon can be found in the fact that only a

fraction [n; see Eq. (2.39)] of the wave energy goes forward with the wave as it
advances each wave length. Thus, the Wrst wave in the group is diminished in
height by the square root of n during the advance of one wave length. Waves in the
group lose energy to the wave immediately behind and gain energy from the wave
in front. The last wave in the group leaves energy behind so, relative to the group, a
new wave appears each T seconds and gains additional energy as time passes.

Apracticalconsequenceofthedeepwatergroupceleritybeinglessthanthephase

celerity of individual waves is that when waves are generated by a storm, prediction
of their arrival time at a point of interest must be based on the group celerity.

To develop an equation for calculating the group celerity Cg consider two

trains of monochromatic waves having slightly diVerent periods and propagating
in the same direction. Figure 2.6 shows the wave trains separately (above) and
superimposed (below) when propagating in the same area. The superimposition
of the two wave trains results in a beating eVect in which the waves are alternately in and out of phase. This produces the highest waves when the two
components are in phase, with heights diminishing in the forward and backward
directions to zero height where the waves are exactly out of phase. The result is a
group of waves advancing at a celerity Cg. If you follow an individual wave in the
wave group its amplitude increases to a peak and then diminishes as it passes
through the group and disappears at the front of the group.

C + dC, L + dL C, L

SWL

Cg

SWL

Figure 2.6. Two wave trains shown separately and superimposed.


C + dC, L + dL

Cg


-----

30 / Basic Coastal Engineering

Referring to Figure 2.6, the time required for the lag between the two com
ponents dL to be made up is dt, where dt equals the diVerence in component
lengths divided by dC, the diVerence in component celerities, i.e., dt ¼ dL=dC.
The group advances a distance dx in the time dt, where dx is the distance traveled
by the group in the time interval dt minus the one wave length that the peak wave
dropped back (as the in-phase wave drops back one wave length each period).
This can be written


dx �[(][C][ þ][ dC][)][ þ][ C]�
¼

2


dt � [(][L][ þ][ dL][)][ þ][ L] � Cdt � L:

2


if dL and dC are very small compared to L and C. Then,

Cg ¼ [dx]dt dt ¼ C � dt[L]

[¼][ Cdt][ �] [L]


since dt ¼ dL=dC this leads to


� �

Cg ¼ C � L [dC]dL


(2:43)


In shallow water, small-amplitude waves are not dispersive (dC=dL ¼ 0) so
Cg ¼ C. In deep water dC=dL ¼ C=2L [from Eq. (2.15)] so the group celerity
is half of the phase celerity. For a general relationship for the group celerity,
employing the dispersion relationship with Eq. (2.43) yields


� 2kd �

Cg ¼ [C]2 1 þ sinh 2kd


(2:44)


Thus, with n as deWned in Eq. (2.38)

Cg ¼ nC (2:45)

So n is also the ratio of the wave group celerity to the phase celerity. Another way
to look at this is that the wave energy is propagated forward at the group
celerity.

2.6 Radiation Stress and Wave Setup

In Xuid Xow problems, some analyses are best carried out by energy considerations (e.g., head loss along a length of pipe) and some by momentum considerations (e.g., force exerted by a water jet hitting a wall). Similarly, for waves it is


-----

Two-Dimensional Wave Equations and Wave Characteristics / 31

better to consider the Xux of momentum for some problem analyses. For wave
analyses, the Xux of momentum is commonly referred to as the wave ‘‘radiation
stress’’ which may be deWned as ‘‘the excess Xow of momentum due to the presence
of waves’’ (Longuet-Higgins and Stewart, 1964). Problems commonly addressed
by the application of radiation stress include the lowering (setdown) and raising
(setup) of the mean water level that is induced by waves as they propagate into the
nearshore zone, the interaction of waves and currents, and the alongshore current
in the surf zone induced by waves obliquely approaching the shore.

Radiation Stress

The horizontal Xux of momentum at a given location consists of the pressure
force acting on a vertical plane normal to the Xow plus the transfer of momentum through that vertical plane. The latter is the product of the momentum in
the Xow and the Xow rate across the plane. From classical Xuid mechanics, the
momentum Xux from one location to another will remain constant unless there is
a force acting on the Xuid in the Xow direction to change the Xux of momentum.

If we divide the momentum Xux by the area of the vertical plane through

which Xow passes, we have for the x direction

p ru[2]
þ

For a wave, we want the excess momentum Xux owing to the wave, so the
radiation stress Sxx for a wave propagating in the x direction becomes


ðo

�d


Sxx ¼


ðh

�d


(p ru[2])dz
þ �


rgdz (2:46)


where the subscript xx denotes the x-directed momentum Xux across a plane
deWned by x constant. In Eq. (2.46) p is the total pressure given by Eq. (2.32)
¼
so the static pressure must be subtracted to obtain the radiation stress for only
the wave. The overbar denotes that the Wrst term on the right must be averaged
over the wave period. Inserting the pressure and the particle velocity from Eq.
(2.21) leads to (Longuet-Higgins and Stewart, 1964)


� �

¼E[�] 2n � [1]

2


Sxx ¼ [r][gH]8 [2]


�1 2kd �

2 sinh 2kd

[þ]


(2:47)


For a wave traveling in the x-direction there also is a y-directed momentum Xux
across a plane deWned by y constant. This is
¼


Syy ¼ [r][gH]8 [2]


� kd �

sinh kd


¼ E[�] (n � 1=2) (2:48)


-----

32 / Basic Coastal Engineering

The radiation stress components Sxy and Syx are both zero. Note that in deep
water Eqs. (2.47) and (2.48) become


Sxx ¼

And in shallow water they become


E�
(2:49)
2 [,][ S][yy][ ¼][ 0]


Sxx ¼ [3]2 [E][ �] [,][ S][yy][ ¼]


E�
(2:50)
2


so, like wave energy, the radiation stress changes as a wave propagates through
water of changing depth (as well as when a force is applied).

If a wave is propagating in a direction that is situated at an angle to the

speciWed x direction, the radiation stress components become


Sxx ¼E n[�]� ( cos[2] u þ 1) � 1=2�

Syy ¼E n[�]� ( sin[2] u þ 1) � 1=2�

E�

Sxy ¼ 2 [n][ sin][2][ u][ ¼][ �][En][ sin][ u][ cos][ u]


(2:51)


where u is the angle between the direction of wave propagation and the speciWed
x direction.

Wave Setup

When a train of waves propagates toward the shore, at some point, depending on
the wave characteristics and nearshore bottom slope, the waves will break.
Landward of the point of wave breaking a surf zone will form where the waves
dissipate their energy as they decay across the surf zone.

As the waves approach the breaking point there will be a small progressive set

down of the mean water level below the still water level. This setdown is caused
by an increase in the radiation stress owing to the decreasing water depth as the
waves propagate toward the shore. The setdown is maximum just seaward of the
breaking point. In the surf zone, there is a decrease in radiation stress as wave
energy is dissipated. This eVect is stronger than the radiation stress increase
owing to continued decrease in the water depth. The result is a progressive
increase or setup of the mean water level above the still water level in the
direction of the shore. This surf zone setup typically is signiWcantly larger than
the setdown that occurs seaward of the breaking point.

The equations that predict the wave-induced nearshore setdown and setup can

be developed by considering the horizontal momentum balance for two-dimensional waves approaching the shore (Longuet-Higgins and Stewart, 1964). The


-----

Two-Dimensional Wave Equations and Wave Characteristics / 33

dx MWL


d9
SWL

d

Sxx

Hydrostatic

force


d9 + ∂d9/∂x dx

Sxx + (∂sxx/∂x) dx

Hydrostatic force

Hydrostatic


dx

d9 + ∂d

d9
SWL

d Sxx

xx

Hydrostatic

force


Figure 2.7. Force balance for wave-induced setup analysis.

net force caused by the cyclic bottom shear stress is reasonably neglected.
Consider Figure 2.7 which shows a shore-normal segment of length dx with a
setup d [0]. The forces and related change in the radiation stress at the boundaries
are as shown. Writing the force-momentum Xux balance for a segment of unit
width parallel to the shore yields


rg � �2

d þ d[0] þ [@][d] [0]

2 [(][d][ þ][ d] [0][)][2][ �] [r]2[g] @x [dx]


¼ [@][S][xx]

@x [dx]


where the two terms on the left are the fore and aft hydrostatic forces and the
term on the right is the resulting change in radiation stress. Assuming d � d[0] and
neglecting higher order terms this leads to

dSxx (2:52)

dx dx

[þ][ r][gd dd] [0] [¼][ 0]


Equation (2.52) basically relates the change in radiation stress (caused either by a
depth change and/or wave energy dissipation) to the resulting slope of the mean
water level. This equation applies to the regions before and after the breaking
point.

For the region just seaward of the breaking point assume that the wave power

is constant and employ Eq. (2.47) to integrate Eq. (2.52). This leads to the
setdown of the mean water level given by


d [0] ¼ � [1]

8


H [2]k

(2:53)
sinh 2kd


For deep water, Eq. (2.53) shows that the setdown is zero irrespective of the wave
height because the sinh term is very large. In shallow water, which may be used
as an estimate of the conditions just prior to breaking, d [0] ¼ �H [2]=16d.


-----

34 / Basic Coastal Engineering

In the surf zone, the rate of energy dissipation by wave breaking will depend

on the type of breaker that occurs. This rate of energy dissipation is complex and
typically nonuniform. However, to reasonably develop an equation for wave
setup, we will assume that the wave height across the surf zone is proportional to
the depth below the local mean water level, i.e., H ¼ g(d þ d[0]). A reasonable
value for g is 0.9 (see Section 2.8). Also, we will assume that shallow water wave
conditions exist so Sxx ¼ 3E=2. These assumptions lead to a solution to Eq.
(2.52) given by

dd [0] � ��1 dd

1 þ [8] (2:54)
dx 3g[2] dx

[¼]


which gives the slope of the mean water level as a function of the bottom slope in
the surf zone.

Example 2.6-1

Consider a wave that has a height of 2 m in water 2.2 m deep (below the mean
water level) as it is about to break. The nearshore bottom slope through the surf
zone is 0.02. Find the setdown at the breaker point and the setup (above the still
water line) at the still water line contour of the shore. Assume shallow water
wave conditions throughout.

Solution:

The setdown at the breaker line is

(2)[2]
d[0] ¼ �

16(2:2) [¼ �][0][:][11 m]

The slope of the rising mean water level through the surf zone is


dd[0] � 8 ��1

1
þ
dx [¼] 3(:9)[2]


(0:02) ¼ 0:0047


For a bottom slope of 0.02 the still water line at the beach will be
(2:2 þ 0:11)=(0:02) ¼ 115:5 mshorewardofthebreakerline.Atthispointthemean
water level will be �0:11 þ (115:5)(0:0047) ¼ 0:43 m above the still water level.

Equations (2.53) and (2.54) indicate that the setdown is a function of the incident
wave height but the slope of the mean water level through the surf zone is not.
However, higher incident waves will break further seaward so the same mean
water level slope will yield a higher mean water level throughout the surf zone.


-----

Two-Dimensional Wave Equations and Wave Characteristics / 35

It should be kept in mind that the development of Eqs. (2.53) and (2.54)

employed the small-amplitude wave theory, which is less accurate in the nearshore zone. However, experiments conducted by Saville (1961) in a large twodimensional wave tank yielded results that favorably agree with predictions from
these equations. Also, the equations apply to waves approaching normal to the
shore. If the waves approach obliquely to the shore, only the shore normal
component of radiation stress will induce setdown and setup.

2.7 Standing Waves, Wave ReXection

A solid structure such as a vertical wall will reXect an incident wave, the
amplitude of the reXected wave depending on the wave and wall characteristics.
When the reXected wave passes through the incident wave a standing wave will
develop. It is worthwhile to investigate the nature of wave reXection and standing
waves, particularly the resulting surface proWle and particle kinematics of the
resulting wave motion as well as the dependence of the reXected wave characteristics on the reXecting structure makeup.

Standing Waves

Consider two waves having the same height and period but propagating in
opposite (þ=�) directions along the x axis. When these two waves are superimposed the resulting motion is a standing wave as depicted in Figure 2.8a. The
water surface oscillates from one position to the other and back to the original
position in one wave period. The arrows indicate the paths of water particle
oscillation. Under a nodal point particles oscillate in a horizontal plane while
under an antinodal point they oscillate in a vertical plane. When the surface is at
one of the two envelope positions shown, water particles instantaneously come
to rest and all of the wave energy is potential. Halfway between the envelope
positions the water surface is horizontal and all wave energy in kinetic. The net
energy Xux (if the two component waves are identical) is zero.

The velocity potential for a standing wave can be obtained by adding the

velocity potentials for the two component waves that move in opposite directions. This yields


f [gH]
¼

s


�cosh k(d z)�

þ

cosh kd


cos kx sin �t (2:55)


With the velocity potential given by Eq. (2.55), we can derive the various
standing wave characteristics in the same way as for a progressive wave. This
yields a surface proWle given by


-----

36 / Basic Coastal Engineering

= O, T


Envelope of
surface motion


= T/2


SWL

SWL


surface motion

(a)

Envelope of
surface motion


(b)

Figure 2.8. Standing wave particle motion and surface proWle envelope. (a) Cr ¼ 1:0,

(b) Cr < 1:0.


h ¼ H cos kx sin st; (2:56)

horizontal and vertical velocity components given by


�cosh k(d z)�

þ

sinh kd


u [p][H]
¼

T


sin kx sin st (2:57)


and


�sinh k(d z)�

þ

sinh kd


w [p][H]
¼

T


cos kx sin st; (2:58)


a pressure Weld given by

� �

p ¼ �rgz þ �gH [cosh][ k][(][d][ þ][ z][)]

cosh kd


cos kx cos st; (2:59)


and horizontal and vertical particle displacements given by


-----

Two-Dimensional Wave Equations and Wave Characteristics / 37


� �

z H [cosh][ k][(][d][ þ][ z][)]
¼ �

sinh kd


sin kx cos st (2:60)


and


e ¼ H�[sinh][ k][(][d][ þ][ z][)]�

sinh kd


cos kx cos st (2:61)


Equations (2.56) through (2.61) demonstrate some interesting features of a
standing wave. If the component progressive wave heights are H, the standing
wave height is 2H. The terms in brackets that deWne wave decay/shoaling eVects
are the same as for the equivalent progressive wave characteristic. However, at a
given point (x, z) the horizontal and vertical velocity and displacement com�
ponents are in phase, rather than being 908 out of phase as is the case for
progressive waves. The pressure is hydrostatic under a node where particle
acceleration is horizontal; but under an antinode there is a Xuctuating vertical
component of dynamic pressure.

The energy in a standing wave per unit crest width and for one wave length is

E ¼ [r][gH][2][L] (2:62)

4

where, again, H is the height of a component progressive wave. This consists of
potential and kinetic energy components given by

Ep ¼ [r][gH]4 [2][L] cos[2] st (2:63)


and

Ek ¼ [r][gH]4 [2][L] sin[2] st (2:64)

Equations (2.63) and (2.64) demonstrate, as discussed above, that at

t ¼ 0, T=2, . . . E ¼ Ep and at T ¼ T=4, 3T=4, . . . E ¼ Ek.

Wave ReXection

In a standing wave, the particle velocity under an antinode is always vertical. If a
frictionless, rigid, vertical, impermeable wall were placed at the antinode the
water particle motion would be unaVected. Thus, we would have a standing wave
caused by the reXection of a progressive wave from the wall. The particle velocity
and the pressure distribution along the wall would be given by Eqs. (2.58) and
(2.59), respectively with cos kx 1.
¼


-----

38 / Basic Coastal Engineering

As the wall slope decreases, the wall becomes elastic and/or the wall surface

becomes rough and permeable, the reXected wave height becomes less than the
incident height. The surface proWle and the particle motion in this standing wave
are depicted in Figure 2.8b. We can deWne a reXection coeYcient Cr as


Cr ¼ [H]H[r]i


(2:65)


where Hr is the reXected wave height and Hi is the incident wave height (i.e., the
reXection coeYcient will be equal to or less than unity). Considering Figure 2.8,
as the reXection coeYcient decreases from unity to zero the particle trajectories
transition from those for a pure standing wave to those of the orbital pattern for
a pure progressive wave.

The envelope height at the antinode for a standing wave is Hi Hr and the
þ

nodal envelope height is Hi Hr (Ippen, 1966). It can also be shown the reXec�
tion coeYcient equals the diVerence between the two envelope heights divided by
the sum of the two envelope heights. When wave tank tests are being run with
monochromatic waves and a reXecting structure, the wet mark on the side of the
tank displays the upper envelope shown in Figure 2.8b and is an indicator of the
amount of wave reXection from the structure. A wave gage mounted on a
carriage and slowly moved at least one wave length along the wave tank will
measure the node and antinode envelope heights which can be used to calculate
the reXection coeYcient for a monochromatic wave.

2.8 Wave ProWle Asymmetry and Breaking

As a wave propagates into intermediate and shallow water an initial proWle
asymmetry develops around the horizontal axis as the wave crest steepens and
the wave trough Xattens. Further on an asymmetry also develops around a vertical
axis through the wave crest (neither asymmetry is deWned by the small amplitude
wave theory). These asymmetries ultimately lead to wave instability and breaking.

ProWle Asymmetry

Figure 2.9 shows a typical asymmetric wave proWle as a wave propagates
through relatively shallow water prior to breaking. Besides the vertical
asymmetry resulting in a crest amplitude that exceeds half the wave height, the
front face of the wave becomes steeper than the back face and the distance (in
the direction of wave propagation) from crest to trough is less than the distance
from trough to crest. These asymmetries increase as the wave moves into shallower and shallower water. They also contribute to increased particle velocities
at the wave crest and ultimately to crest instability and wave breaking.


-----

Two-Dimensional Wave Equations and Wave Characteristics / 39

ac

b a H
SWL

2 1

4 3

Figure 2.9. DeWnition of proWle asymmetry terms.

Wave tank experiments were conducted by Adeyemo (1968) for intermediate

depth waves shoaling on slopes from 1:18 to 1:4. These slopes are somewhat
steeper than found in most nearshore areas. He presented his data in terms of
four values deWned as follows (see Figure 2.9):

Vertical asymmetry ¼ ac=H

Slope asymmetry ¼ 0:5(slope a þ slope b)

Horizontal asymmetry (1) distance 1/distance 2
¼

Horizontal asymmetry (2) distance 3/distance 4
¼

The slopes were stated in radians with slope b being a positive value and slope a
being a negative value.

The experiments showed the vertical asymmetry continuously increased as the

wave shoaled, reaching a maximum of between 0.62 and 0.74 at breaking. In
shallower depths (d=L < 0:10) wave vertical asymmetry was greater for Xatter
slopes. Flatter slopes mean that the wave has more travel time for the asymmetry
to develop. Thus, for natural beach slopes that are Xatter than the experimental
slopes one might expect vertical asymmetries greater than the 0.62 to 0.74 values
reported. The slope and horizontal asymmetries also continuously increased as
the wave shoaled; but, as opposed to vertical asymmetries steeper bottom slopes
caused greater slope and horizontal asymmetries.

Wave Breaking

If a wave has suYcient height in any water depth it will break. In deep water, for
a given wave period, the crest particle velocity is proportional to the wave height.
From the small-amplitude wave theory, the wave celerity is independent of the
wave height. So, as the wave height increases the crest particle velocity will
eventually equal the wave celerity and the wave will break. In shallow water,
as the water depth decreases the crest particle velocity increases and the wave
celerity decreases, leading to instability and breaking.


ac

b a H

2 1

4 3


-----

40 / Basic Coastal Engineering

Miche (1944) developed a simple equation for wave breaking in any water

depth given by


�H�


¼ [1] (2:66)

7 [tanh 2][p]L[d]


L


max


This equation ignores the bottom slope which, as discussed above, aVects development of wave asymmetry and breaking as a wave shoals. As a consequence,
Eq. (2.66) gives a good indication of deep water breaking limits on wave height
but only an approximate rule of thumb for shallow water breaking conditions.
For deep water Eq. (2.66) reduces to


�Ho�


¼ [1] (2:67)

7


Lo


max


indicating that the maximum wave height in deep water is limited to one-seventh
of the wave length. In shallow water we have


�H�



[1]
¼

7


�2pd�


L


L


max


or


�H�


d


max


¼ 0:9 (2:68)


Thus, in shallow water wave heights are limited by the water depth. This is often
an important consideration in the design of structures built seaward of the
water’s edge. No matter how high the deep water wind generated waves are,
the highest wave that can reach the structure is dependent primarily on the water
depth in front of the structure. Thus, as structures are extended further seaward
they tend to be exposed to higher, more damaging waves.

Waves breaking on a beach are commonly classiWed into three categories (U.S.

Army Coastal Engineering Research Center, 1984) depicted in Figure 2.10.
These three breaker classes are:

Spilling. As breaking commences, turbulence and foam appear at the wave
crest and then spread down the front face of the wave as it propagates
toward the shore. The turbulence is steadily dissipating energy, resulting in a
relatively uniform decrease in wave height as the wave propagates forward
across the surf zone.

Plunging. The wave crest develops a tongue that curls forward over the front
face and plunges at the base of the wave face. The breaking action and


-----

Two-Dimensional Wave Equations and Wave Characteristics / 41

Spilling

Plunging

Collapsing

Surging

Figure 2.10. Wave breaker classiWcation.

energy dissipation are more conWned to the point of breaking than is the
case for a spilling wave. The plunging tongue of water may regenerate lower
more irregular waves that propagate forward and break close to the shore.

Surging. The crest and front face of the wave approximately keep their
asymmetric shape as they surge across the beach slope. This form of
breaking is a progression toward a standing or reXecting wave form.

While the above three classes are relatively distinct, for gradually changing

incident wave steepnesses and bottom slopes there is a gradual transition from
one form to the next. (Some investigators add a transitional class—collapsing
breakers—between plunging and surging.) Only spilling and plunging breakers
occur in deep water and they are the most common types of breakers in shallow
water. Spilling breakers, accompanied by ‘‘whitecapping’’ if there is a strong
wind, are most common in deep water. The type of breaker is important, for
example, to the stability of a stone mound structure exposed to breaking waves.


Spilling

Plunging

Collapsing


-----

42 / Basic Coastal Engineering

It will also aVect the amount of energy reXected from a slope and the elevation of
wave runup on a slope.

As discussed above, Eq. (2.68) only gives an approximate rule of thumb for

wave breaking in shallow water. A number of experimenters have investigated
nearshore breaking conditions in the laboratory and presented procedures for
predicting the breaking height Hb and water depth at breaking db as a function of
incident wave characteristics and bottom slope m. Figures 2.11 and 2.12, modiWed slightly from the U.S. Army Coastal Engineering Research Center (1984)
and based on studies by Goda (1970) and Weggel (1972), are commonly used for
estimating breaking conditions.

Given the beach slope, the unrefracted deep water wave height, and the wave

period one can calculate the deep water wave steepness and then determine the
breaker height from Figure 2.11. The regions for the three classes of wave
breaker types are also denoted on this Wgure. With the breaker height one can
then determine the water depth at breaking from Figure 2.12. Note the range of
db=Hb values in Figure 2.12 versus the guidance given by Eq. (2.68). If a wave
refracts as it propagates toward the shore, the equivalent unrefracted wave
height given by

3.0

2.5

m = 0.100

2.0 0.050

0.033

Hb 0.020

H09


1.5

1.0

0.5


m = 0.100

0.050

0.033

0.020


0.0004


0.0006 0.001 0.002


0.004 0.006 0.01 0.02 0.03

/gT[2]


H


**9**

0


Figure 2.11. Dimensionless breaker height and class versus bottom slope and deep water

steepness. (ModiWed from U.S. Army Coastal Engineering Research Center, 1984.)


-----

Two-Dimensional Wave Equations and Wave Characteristics / 43


db

Hb


2.0

1.8

1.6

1.4

1.2

1.0

0.8

0.6
0


m = 0 (1:∞)


0.002 0.004 0.006


0.008


0.010 0.012 0.014 0.016 0.018 0.020

Hb /gT[2]


Figure 2.12. Dimensionless breaker depth versus bottom slope and breaker steepness.

(ModiWed from U.S. Army Coastal Engineering Research Center, 1984.)

Ho0 [¼][ K][r][H][o] (2:69)


should be used in Figure 2.11.

Figures 2.11 and 2.12 do not consider the eVects of wind on wave breaking.

Douglass (1990) conducted limited laboratory tests on the eVect of inline following and opposing winds on nearshore wave breaking. He found that oVshore
directed winds retarded the growth of wave height toward the shore and consequently caused the waves to break in shallower water than for the no wind
condition. Onshore winds had the opposite eVect but to a lesser extent. However,
Hb=db was greater for oVshore winds than for onshore winds, given the same
incident wave conditions and beach slope. For the same incident waves, oVshore
winds caused plunging breakers when onshore winds caused waves to spill.

The design of some coastal structures is dependent on the higher wave that

breaks somewhat seaward of the structure and plunges forward to hit the
structure. Thus, when designing a structure for breaking wave conditions, the
critical breaking depth is some point seaward of the structure that is related to
the breaker plunge distance Xp as depicted in Figure 2.13. Smith and Kraus
(1991), based on experiments with plane slopes and slopes having a submerged


-----

44 / Basic Coastal Engineering

Xp Breaker initiation

Hb
MWL

db

m

Figure 2.13. DeWnition sketch for breaker plunge distance.

bar that trips wave breaking, found the following relationships for the plunge
distance. For plane slopes,


Xp Breaker initiation

Hb

db

m


ffiffiffiffiffiffiffiffiffiffiffiffiffiffiHo=Lo

m


Xp

Hb


¼ 3:95


p


and, for slopes with a submerged bar


!0:25

(2:70)

þ 1:81 (2:71)


!


Xp

Hb


¼ 0:63


pffiffiffiffiffiffiffiffiffiffiffiffiffiffiHo=Lo

m


For structure design one might typically use the wave that breaks at 0:5Xp
seaward of the structure.

2.9 Wave Runup

After a wave breaks, a portion of the remaining energy will energize a bore that
will run up the face of a beach or sloped shore structure. Figure 2.14 depicts this

Limit of wave

runup

R

SWL

ds

Figure 2.14. DeWnition sketch for wave runup.


runup

R

ds


-----

Two-Dimensional Wave Equations and Wave Characteristics / 45

process where the runup R is the maximum vertical elevation above the still
water level to which the water rises on the beach or structure. Prediction of the
wave runup is important, for example, for the determination of the required crest
elevation for a sloping coastal structure or to establish a beach setback line for
limiting coastal construction.

The runup depends on the incident deep water wave height and period, the

surface slope and proWle form if not planar, the depth ds fronting the slope (see
Figure 2.14), and the roughness and permeability of the slope face. Dimensional
analysis leads to


R

Ho0


� 0 �

¼ fcn a, [H]o 0

gT [2][,][ d]H[s]o


(2:72)


for a given surface shape and condition (where cot a ¼ 1=m).

Figure 2.15 is a typical plot of experimental data from a laboratory wave

runup study with monochromatic waves. These data are for a smooth, planar,
impermeable slope with ds=Ho0 [between 1 and 3. (See U.S. Army Coastal Engin-]

eering Research Center, 1984 for similar plots for other slope conditions.) Figure
2.15 indicates that, for a given structure slope, steeper waves (higher Ho0 [=][gT] [2][)]

have a lower relative runup (R=Ho0 [). Also, for most beach and revetment slopes]

(which are Xatter than 1 on 2), the wave runup increases as the slope becomes
steeper.

Table 2.1, developed from a number of laboratory experiments, gives an

indication of the eVect of slope surface condition on wave runup. The factor r
is the ratio of the runup on the given surface to that on a smooth impermeable
surface and may be multiplied by the runup determined from Wgures such as
Figure 2.15 to predict the wave runup.

Example 2.9-1

Consider the deep water wave in Example 2.3–1 propagating toward the shore
without refracting. The wave breaks and runs up on a 1:10 grass covered slope
having a toe depth of 4 m. Determine the breaking wave height and the wave
runup elevation on the grass-covered slope.

Solution:

For a deep water unrefracted wave height of 2 m and a period of 10 s we have

Ho0 2

gT [2][ ¼] (9:81)(10)[2][ ¼][ 0][:][002]


From Figure 2.11 for m ¼ 0:1


-----

46 / Basic Coastal Engineering

6.0
5.0

4.0

3.0

2.0

1.5

1.0

R

0.9

H09 0.80.7 Ho9

gT[2]

0.6
0.5 0.0003


0.4

0.3

0.2

0.15

0.1


Ho9

gT[2]

0.0003

0.0006

0.0009
0.0012
0.0016
0.0019
0.0023
0.0031

0.0047
0.0062
0.0078
0.0093
0.0124


0.6


0.8 1.0 1.5 2.0 3.0 4.0 5.0 6.0 8.0 10 15 20 30 40

cot α


50


Figure 2.15. Dimensionless runup on smooth impermeable slopes versus bottom slope

and incident deep water wave steepness; 1 < ds=Ho0 [<][ 3. (Modi][W][ed from U.S. Army]

Coastal Engineering Research Center, 1984.)

Table 2.1. Runup Factors for Various Slope Conditions

Slope facing r

Concrete slabs 0.9

Placed basalt blocks 0.85–0.9

Grass 0.85–0.9

One layer of riprap on an impermeable base 0.8

Placed stones 0.75–0.8

Round stones 0.6–0.65

Dumped stones 0.5–0.6

Two or more layers of riprap 0.5

Tetrapods, etc. 0.5

From Battjes, 1970.


-----

Two-Dimensional Wave Equations and Wave Characteristics / 47


Hb
Ho0


¼ 1:6


or

Hb ¼ 1:6(2) ¼ 3:2 m

The wave would form a plunging breaker. From Figure 2.15, since

ds=Ho0 [¼][ 4][=][2][ ¼][ 2, at cot][ a][ ¼][ 10]


R


H


0

o


¼ 0:85


or the uncorrected smooth slope runup is

R ¼ 0:85(2) ¼ 1:7 m

Using r ¼ 0:875 from Table 2.1 gives a runup of

R ¼ 0:875(1:7) ¼ 1:5 m

on the grass-covered slope.

2.10 Summary

Experiments conducted in wave tanks (Wiegel, 1950; Eagleson, 1956; LeMehaute et al., 1968) give some indication of the accuracy of small-amplitude wave
theory in predicting the transformation of monochromatic two-dimensional
waves as they travel into intermediate and shallow water depths, and of the
accuracy in predicting particle kinematics given the wave height and period and
the water depth. A summary follows:

1. For most typical bottom slopes the dispersion equation is satisfactory for

predicting the wave celerity and length up to the breaker zone.

2. For increasing beach slopes and wave steepnesses, the wave height predic
tions given by Eq. (2.42) will be lower than the real wave heights. This
discrepancy increases as the relative depth decreases. As an example, on a
1:10 slope, for a relative depth of 0.1 and a deep water wave steepness of 0.02,
the experimental wave height exceeded the calculated wave height by 15%.

3. For waves on a relatively Xat slope and having a relative depth greater than

about0.1,thesmall-amplitude theoryissatisfactoryforpredictinghorizontal


-----

48 / Basic Coastal Engineering

water particle velocities. At lesser relative depths the small-amplitude
theory still predicts reasonably good values for horizontal velocity near
the bottom, but results are poorer (up to 50% errors on the low side) near
the surface.

Limitations of the small-amplitude theory in shallow water and for high waves

in deep water suggest a need to consider nonlinear or Wnite-amplitude wave
theories for some engineering applications. The next chapter presents an overview of selected aspects of the more useful Wnite-amplitude wave theories, as well
as their application and the improved understanding of wave characteristics that
they provide.

2.11 References

Adeyemo, M.D. (1968), ‘‘EVect of Beach Slope and Shoaling on Wave Asymmetry,’’ in

Proceedings, 11th Conference on Coastal Engineering, American Society of Civil Engineers, London, pp. 145–172.

Airy, G.B. (1845), ‘‘On Tides and Waves,’’ in Encyclopedia Metropolitan, London,

pp. 241–396.

Battjes, J.A. (1970), Discussion of ‘‘The Runup of Waves on Sloping Faces—A Review of

the Present State of Knowledge,’’ by N.B. Webber and G.N. Bullock, Proceedings,
Conference on Wave Dynamics in Civil Engineering, John Wiley, New York, pp. 293–314.

Dean, R.G. and Dalrymple, R.A. (1984), Water Wave Mechanics for Engineers and

Scientists, Prentice-Hall, Englewood CliVs, NJ.

Douglass, S.L. (1990), ‘‘InXuence of Wind on Breaking Waves,’’ Journal, Waterways,

Port, Coastal and Ocean Engineering Division, American Society of Civil Engineers,
November, pp. 651–663.

Eagleson, P.S. (1956), ‘‘Properties of Shoaling Waves by Theory and Experiment,’’

Transactions, American Geophysical Union, Vol. 37, pp. 565–572.

Goda, Y. (1970), ‘‘A Synthesis of Breaker Indices,’’ Transactions, Japan Society of Civil

Engineers, Vol. 2, Tokyo, pp. 227–230.

Ippen, A.T. (1966), Estuary and Coastline Hydrodynamics, McGraw-Hill, New York.

LeMehaute, B., Divoky, D., and Lin, A. (1968), ‘‘Shallow Water Waves: A Comparison of

Theories and Experiments,’’ in Proceedings, 11th Conference on Coastal Engineering,
American Society of Civil Engineers, London, pp. 86–107.

Longuet-Higgins, M.S. and Stewart, R.W. (1964), ‘‘Radiation Stress in Water Waves: A

Physical Discussion, with Applications,’’ Deep Sea Research, Vol. 11, pp. 529–549.

Miche, M. (1944), ‘‘Movements Ondulatoires des Mers en Profondeur Constante ou

Decroissante,’’ Annales des Ponts et Chaussees, pp. 25-78, 131-164, 270–292, 369–406.

Saville, T., Jr. (1961), ‘‘Experimental Determination of Wave Setup,’’ in Proceedings, 2nd

Conference on Hurricanes, U.S. Department of Commerce National Hurricane Project,
Report 50, pp. 242–252.


-----

Two-Dimensional Wave Equations and Wave Characteristics / 49

Smith, E.R. and Kraus, N.C. (1991), ‘‘Laboratory Study of Wave Breaking Over Bars and

ArtiWcial Reefs,’’ Journal, Waterway, Port, Coastal and Ocean Engineering Division,
American Society of Civil Engineers, July/August, pp. 307–325.

Sorensen, R.M. (1978), Basic Coastal Engineering, John Wiley, New York.

Sorensen, R.M. (1993), Basic Wave Mechanics for Coastal and Ocean Engineers, John

Wiley, New York.

U.S. Army Coastal Engineering Research Center (1984), Shore Protection Manual, U.S.

Government Printing OYce, Washington, DC.

Weggel, J.R. (1972), ‘‘Maximum Breaker Height,’’ Journal, Waterway, Port, Coastal and

Ocean Engineering Division, American Society of Civil Engineers, November, pp. 529–
548.

Wiegel, R.L. (1950), ‘‘Experimental Study of Surface Waves in Shoaling Water,’’ Trans
actions, American Geophysical Union, Vol. 31, pp. 377–385.

Wiegel, R.L. (1964), Oceanographical Engineering, Prentice-Hall, Englewood CliVs, NJ.

2.12 Problems

1. A two-dimensional wavetank has a stillwater depthof 1.9 m and a1:20 plane

slope installed with its toe at the tank midpoint. The tank is 1 m wide. A wave
generator produces monochromatic waves that, when measured at a wave gage
installed before the toe of the slope, have a height of 0.5 m and a period of 2.8 s.

(a) Determine the wave length, celerity, group celerity, energy, and energy

density at the wave gage.

(b) At the instant that a wave crest passes the wave gage, determine the water

particle velocity and acceleration below the gage at mid depth.

(c) Is the wave passing the gage a deep water wave? If not, what would the

equivalent deep water length, celerity, group celerity, energy, and energy
density be? Compare these values to those in part a.

(d) Calculate the wave height as a function of distance along the slope from

the toe to the point at which the wave breaks.

2. An ocean bottom-mounted pressure sensor measures a reversing pressure

as a train of swells propagates past the sensor toward the shore. The pressure
Xuctuations have a 5.5 s period and vary from a maximum of 54:3 kN=m[2] to a
minimum of 41:2 kN=m[2].

(a) How deep is the pressure sensor (and bottom) below the still water level?
(b) Determine the wave height, celerity, group celerity, energy, and power as it

passes the sensor.

(c) As a wave crest is passing the sensor determine the water particle velocity

and acceleration at a point 1.5 m above the bottom.


-----

50 / Basic Coastal Engineering

(d) Calculate the deep water wave celerity, length, group celerity, energy, and

power if the wave propagates along a line perpendicular to the shore
without refracting.

(e) The nearshore bottom slope is 1:30. Calculate and plot the wave height as a

functionofposition fromdeepwaterinto thepointatwhichthe wavebreaks.

3. OVshore, in deep water, a wave gage measures the height and period of a

train of waves to be 2 m and 7.5 s, respectively. The wave train propagates
toward the shore in a normal direction without refracting and the nearshore
bottom slope is 1:40. It passes the outer end of a pier located in water 4.5 m deep.

(a) Determine the wave length, celerity, group celerity, energy density, and

power in deep water.

(b) Determine the wave length, height, celerity, group celerity, energy density,

and power at the end of the pier. Is this a deep, transitional or shallow
water wave at the end of the pier?

(c) At the instant that a wave crest passes the end of the pier, what is the

pressure at a point 2 m below the still water level?

(d) Calculate the horizontal components of the water particle velocity and

acceleration at this point 2 m below the still water level 1 s before the wave
crest passes the end of the pier.

(e) At what water depth will the wave break? What will the wave height be as

the wave breaks? What type of breaker will it be?

4. A wave gage mounted on the seaward end of a pier where the water depth is

6 m, measures a wave having H ¼ 2:3 m and T ¼ 7:1 s. This wave is one of a
train of waves that is traveling normal to the shore without refracting. The
bottom slope is 1:30.

(a) Determine the deep water wave height and energy.
(b) Determine the wave height and water depth where the wave breaks.
(c) What are the water particle pressure, velocity and acceleration 1.7 m

above the bottom 1.3 seconds after the wave crest passes the gage?

5. A wave has a height of 1.5 m in water 5 m deep and a wave period of 6 s.

Plot the horizontal component of velocity, the vertical component of acceleration, and the dynamic pressure at a point 2 m below the still water level versus
time for a 6-s interval. Plot the three values on the same diagram and comment
on the results.

6. Estimate the maximum height wave that can be generated in a wave tank

having water 1.8 m deep if the wave period is 1 s and if the period is 3 s.

7. A wave has a measured height of 1.4 m in water 5.6 m deep. If it shoals on

a 1:50 slope how wide will the surf zone be? Assume the wave propagates normal
to the shore without refracting.

8. A pressure gage located 1 m oV the bottom in water 10 m deep measures an

average maximum pressure of 100 kN=m[2] having an average Xuctuation period
of 12 s. Determine the height and period of the wave causing the measured
pressure Xuctuation.


-----

Two-Dimensional Wave Equations and Wave Characteristics / 51

9. Derive an equation for the horizontal component of particle convective

acceleration in a wave. Compare the horizontal components of convective and
local acceleration versus time for a time interval of one wave period, at a distance
of 2 m below the still water level and for a 1 m high 6 s wave in water 5 m deep.

10. Demonstrate, using Eq. (2.43), that Cg ¼ C=2 in deep water and Cg ¼ C

in shallow water.

11. Calculate and plot n and L nondimensionalized by dividing by the deep

water values for n and L, as a function of d/L for d/L from 0.5 to 0.05.

12. Derive the equations for the horizontal and vertical components of particle

acceleration in a standing wave, starting from the velocity potential [Eq. (2.55)].

13. As the tide enters a river and propagates upstream, the water depth at a

given location is 3.7 m. At this location the tide range is 1 m. If the dominant
tidal component has a period of 12.4 hours, estimate the peak Xood tidal Xow
velocity at this location in the river.

14. Consider the conditions given in Problem 13. At a location in the river

where the water depth is 5.1 m estimate the tide range and peak Xood tidal Xow
velocity.

15. The Wrst wave of a group of waves advancing into still water is 0.30 m

high. The water depth is 4.5 m and the wave period is 2 s. How high is this wave
8 s later?

16. Consider a 1 m high, 4 s wave in water 5 m deep. Plot suYcient velocity

potential lines to deWne their pattern and then sketch in orthogonal streamlines.

17. Consider a deep water wave having a height of 2.1 m and a period of 9 s

shoaling on a 1:50 slope without refraction. Calculate, for comparison, the crest
particle velocity in deep water, at d 20 m, and just prior to breaking. Calculate
¼
the wave celerity just prior to breaking and compare it to the crest particle
velocity. Comment on the reason for any discrepancies.

18. A 12 s, 2 m high wave in deep water shoals without refracting. Calculate

the maximum horizontal velocity component and the maximum horizontal
displacement from the mean position for a particle 5 m below the still water
level in deep water and where the water depth is 6 m.

19. As the wave given in Problem 4 propagates toward the shore determine

the mean water level setdown at the breaker line and the setup 40 m landward of
the breaker line.

20. Equation (2.56) deWnes the surface proWle as a function of time for a

standing wave. From this, derive the potential energy per wave length and the
potential energy density, both as a function of time. Realizing that at the instant
a standing wave has zero particle velocity throughout, all energy is potential
energy, determine the total and kinetic energies per wave length and the total and
kinetic energy densities.

21. For the conditions in Example 2.6-1, calculate and plot (to a 10:1 vertical

scale distortion) the bottom, still water line, and the mean water line from a point
20 m seaward of the breaker point to the shoreline.


-----

52 / Basic Coastal Engineering

22. A wave having a height of 2.4 m and a period of 8 s in deep water is

propagating toward the shore without refracting. A water particle velocity of
0.25 m/s on the bottom is required to initiate movement of the sand on the sea
Xoor. At what water depth will sand movement commence as the wave shoals?

23. Using shallow water wave equations for celerity and water particle vel
ocity and the criteria that at incipient breaking the crest particle velocity equals
the wave celerity, derive a criterion for wave breaking. Comment on the result of
this derivation.

24. To an observer moving in the direction of a monochromatic wave train at

the wave celerity, the wave motion appears to be steady. The surface particle
velocity at the wave crest Uc ¼ Co � pH=T and at the trough Ut ¼ Co þ pH=T
for a deep water wave. Apply the Bernoulli equation between these two points to
derive Eq. (2.16).

25. For a given wave height and period and water depth which of the follow
ing wave parameters depend on the water density: celerity, length, energy density, particle pressure, and particle velocity at a given depth? Explain each answer.

26. How does increased water viscosity aVect a wave train as it propagates

toward the shore?

27. Waves with a period of 10 s and a deep water height of 1 m arrive normal

to the shore without refracting. A 100-m long device that converts wave motion
to electric power is installed parallel to the shore in water 6 m deep. If the device
is 45% eYcient what power is generated?

28. Demonstrate that the velocity potential deWned by Eq. (2.9) does represent

irrotational Xow.

29. A wave with a period of 7 s propagates toward the shore from deep water.

Using the limit presented in this chapter, at what water depth does it become a
shallow water wave? If the deep water wave height is 1 m would this wave break
before reaching the shallow water depth? Assume that no refraction occurs and
that the nearshore slope is 1:30.


-----

## 3

### Finite-Amplitude Waves

The small-amplitude wave theory was formulated as a solution to the Laplace

equation with the required surface (two) and bottom (one) boundary conditions

[Eqs. (2.1), (2.3), (2.4), and (2.6)]. But the two surface boundary conditions had
to be linearized and then applied at the still water level rather than at the water
surface. This requires that H/d and H/L be small compared to unity. Consequently, the small-amplitude wave theory can be applied over the complete range
of relative water depths (d/L), but it is limited to waves of relatively small
amplitude relative to the water depth (for shallow water waves) and wave length
(for deep water waves).

There is no general solution to the Laplace equation and three gravity wave

boundary conditions. All wave theories require some form of approximation or
another. Typically, the Wnite-amplitude wave theories relax the requirement that
either H/d or H/L be small to produce a theory that is applicable for Wniteamplitude waves over some speciWc range of wave conditions. A Wnite H/d yields
a theory useful in shallow water whereas a Wnite H/L yields a theory more
appropriate for deep water.

The intent of this chapter is to provide a brief overview of selected useful Wnite
amplitude wave theories and to employ these theories to provide additional insight
into the characteristics of two-dimensional waves. A discussion of the application
of these Wnite-amplitude theories to engineering analysis will also be presented.

3.1 Finite-Amplitude Wave Theory Formulation

Finite-amplitude wave theories are generally of two types. There are numerical
theories that employ a Wnite diVerence, Wnite element, or boundary integral
method to solve the Laplace and boundary condition equations. There are also
analytical theories in which the velocity potential (and other parameters such as
the surface amplitude and wave celerity) is written as a power series that is solved
by successive approximations or by the perturbation approach.


-----

54 / Basic Coastal Engineering

For numerical theories a computer solution of the numerical equations yields

tabulated values of the desired wave characteristics such as the surface proWle,
particle velocity and acceleration, dynamic pressure, energy and momentum Xux,
etc. as a function of selected values of wave height and period and water depth.
On the other hand, the analytical theories produce speciWc equations for the
various wave characteristics which are given in terms of the wave height and
period and the water depth. Both numerical and analytical theories are not
complete solutions of the wave boundary value problem, but inWnite series
solutions that must be truncated at some point (e.g., truncation of a series
after the third term yields a third-order solution).

In this chapter we brieXy consider four Wnite-amplitude wave theories. The

Stokes theory for deep water waves and the cnoidal and solitary theories for
shallow water waves are useful analytical theories. Dean’s stream function numerical wave theory is a commonly used numerical theory applicable to Wnite-amplitude waves throughout the range of relative water depths. For a more detailed
presentation of these and other Wnite-amplitude wave theories see Wiegel (1964),
Ippen (1966), Sarpkaya and Isaacson (1981), and Dean and Dalrymple (1984).

If any of the Wnite-amplitude wave theories are to be used in practice, two

important considerations arise. The Wrst is the choice of which theory to use to
calculate wave characteristics for a given combination of wave height and period
and water depth. As indicated above, most Wnite-amplitude theories are developed for a speciWc range of relative depths and the higher order solutions for a
particular theory are often more appropriate for higher steepness waves. In some
cases, one characteristic may be best predicted by one theory and another by a
diVerent theory. The Wnite-amplitude theories are generally much more complex
and diYcult to apply than the small-amplitude theory, but generally yield better
results. Is the increased eVort justiWed given the accuracy of analysis desired and
the accuracy to which the input wave conditions are known?

A second consideration is the diYculty of employing Wnite-amplitude wave

theories to calculate wave transformations over a wide range of water depths,
since these theories are commonly developed for speciWc ranges of relative water
depth. (In practice, wave conditions are typically forecast for an oVshore deep
water location and then must be transformed to some nearshore point for coastal
design analysis.) This factor, plus the ease in applying the theory, generally induces
the coastal engineer to apply the small-amplitude wave theory for most analyses.

These two considerations are addressed further in Section 3.6.

3.2 Stokes Waves

Stokes (1847), employing perturbation techniques to solve the wave boundary
value problem, developed a theory for Wnite-amplitude waves that he carried to
the second order. In this theory all the wave characteristics (velocity potential,


-----

Finite-Amplitude Waves / 55

celerity, surface proWle, particle kinetics, etc.) are formulated in terms of a power
series in successively higher orders of the wave steepness H/L. A condition of this
theory is that H/d be small so the theory is applicable only in deep water and a
portion of the intermediate depth range.

As the deep water wave steepness increases improved accuracy can generally be

achieved (at the price of more onerous equations to work with) if the Stokes theory
is carried out to higher orders. Various higher order approximations to the Stokes
theory have been developed. For example, see Skjelbreia (1959) for a third-order
theory, Skjelbreia and Hendrickson (1961) for a Wfth-order theory, and Schwartz
(1974) for much higher order solutions based on calculations using a powerful
computer. We will present selected elements of the second-order and third-order
theories that demonstrate some of the interesting characteristics of Wnite amplitude
waves (vis-a´-vis small-amplitude waves). For engineering applications the secondorder and possibly the Wfth-order theories are most commonly used.

For the Stokes theory second-order solution the velocity potential is given by


(3:1)


F [gH]
¼

2s


cosh k(d z)
þ

sin (kx st)
�
cosh kd



[3][p][CH]
þ

16


�H� cosh 2k(d z)
þ

L sinh[4] (kd)


sin 2(kx st)
�


Inspection of Eq. (3.1) reveals a number of important features of the secondorder theory. Comparison of Eq. (3.1) with Eq. (2.9) shows that the Wrst term on
the right is the small-amplitude theory velocity potential. The magnitude of the
second term on the right is dependent on the wave steepness, a ratio that has a
numerical value that is signiWcantly less than unity but that increases as the wave
amplitude increases for a given wave period. The second term on the right also
has a frequency that is twice that of the small-amplitude term.

The surface proWle is given by


h [H]
¼

2 [cos (][kx][ �] [s][t][)]


(3:2)



[p][H]
þ

8


�H� cosh kd(2 cosh 2kd)
þ

L sinh[3] kd


cos 2(kx st)
�


for which the same comments can be made as were made above for the velocity
potential. The eVect of the second-order term having twice the frequency of the
small-amplitude or Wrst-order term is that the two components of surface amplitude reinforce (i.e., are in phase) each other at the wave crest and oppose each
other at the wave trough. This yields a surface proWle vertical asymmetry (more
peaked wave crest and Xatter wave trough than a cosine proWle given by the
small-amplitude theory) that grows as the wave steepness increases.


-----

56 / Basic Coastal Engineering

In the second-order Stokes theory, the wave celerity is the same as for the

small-amplitude wave theory [given by Eq. (2.12)]. Thus, to the second order,
waves are still period dispersive but not amplitude dispersive. For the Stokes
third-order theory the dispersion relationship becomes


" �pH�2 9 8 cosh[4] (kd) 8 cosh[2] (kd)!#

þ �

C[2] [g]
¼

k [tanh][ kd][ 1][ þ] L 8 sinh[4] (kd)


(3:3)



[It should be noted that small variations on Eq. (3.3) for the third-order celerity
have been given by various authors, e.g., see Wiegel (1964) and Ippen (1966).]
Thus, to the third order, wave celerity is amplitude as well as period dispersive.
For the same wave period higher waves travel faster than lower waves. For the
limiting steepness in deep water (H0=L0 ¼ 1=7) the third-order theory yields a
wave celerity that is about 10% greater than the celerity given by the smallamplitude theory. A greater celerity for the same wave period means that the
wave length would also be 10% larger (since L CT).
¼

For deep water, Eq. (3.2) becomes


h [H][0]
¼

2 [cos (][kx][ �] [s][t][)][ þ][ p][H]4 [0]


�H0�

L0


cos 2(kx � st) (3:4)


which yields the following relationships for the amplitude of the wave crest ac
and wave trough at:


ac ¼ [H]2[0] [þ][ p]4[H]L00[2]

at ¼ [H]2[0] [�] [p]4[H]L00[2]


(3:5)


From Eq. (3.5) for the limiting wave steepness in deep water (1/7) we have
ac ¼ 0:611H and at ¼ 0:389H. Equation (3.2) shows that as a wave enters
intermediate water depths the asymmetry will increase over its equivalent deep
water value.

Example 3.2-1

A 6 m high, 7 s period wave is propagating over a water depth that is just at the
deep water limit. Using the equations presented above, calculate the wave
celerity and length. Also, determine the wave crest and trough amplitudes.
Compare the results to those from the small-amplitude wave theory.


-----

Finite-Amplitude Waves / 57


Solution:

For deep water Eq. (3.3) reduces to


C0 ¼

Inserting Lo ¼ CoT yields


vuuffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffigL0 �pH0�2!
t 1 þ

2p L0


C0 ¼


vuugCffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi0T �pH0�2!
t 1 þ

2p C0T


which can be solved (T ¼ 7 s and Ho ¼ 6 m) by trial to yield

C0 ¼ 11:54 m=s

L0 ¼ 80:78 m

Forthesmall-amplitude theory,Eq(2.16)yields Co 10.93 m/sandEq(2.2)yields
¼
Lo 76.50 m. The Stokes theory values are both 5.5% higher. The steepness of this
¼
wave is 6/80.78 0.074 or about half the limiting steepness of 1/7.
¼

From Eq. (3.5) we have


ac ¼ [6]2 [þ] 4(80p(6):78)[2] [¼][ 3][:][35][m]

at ¼ [6]2 [�] 4(80p(6):78)[2] [¼][ 2][:][65][m]

With increasing wave steepness the second-order term in Eq. (3.2) increases in

size relative to the Wrst-order term. The causes an accelerated ‘‘peaking’’ at the
wave crest where the two terms are in phase; but at the wave trough the Wrst- and
second-order terms are out of phase, causing the trough to become increasingly
Xat. A point is reached where the trough surface becomes horizontal. Increases in
wave steepness beyond this point cause a hump to form and grow at the wave
trough. This hump is not a real wave phenomenon and its appearance is an
indication that the theory is being used beyond its appropriate limit. If we set a
limit of applicability at the point where the trough becomes horizontal, the maximum wave steepness for application of the second-order Stokes theory would be


-----

58 / Basic Coastal Engineering

H sinh[3] kd

(3:6)

L p cosh kd(2 cosh 2 kd)

[¼] þ


In deep water the steepness value given by Eq. (3.6) is greater than 1/7 so the
limit has no practical meaning. For a relative depth (d/L) as small as 0.1 the
limiting steepness from Eq. (3.6) is 0.021. This puts a signiWcant restriction on the
use of the second-order theory as the wave propagates into shallower water.

The Stokes second-order equations for particle velocity and acceleration

follow:


u [p][H]
¼

T


cosh k(d z)
þ

cos (kx st)
�
sinh kd



[3(][p][H][)][2]
þ

4TL


cosh 2k(d z)
þ

sinh[4] (kd)


cos 2(kx st)
�


w [p][H]
¼

T


sinh k(d z)
þ

sin (kx st)
�
sinh kd



[3 (][p][H][)][2]
þ

4TL


sinh 2k(d z)
þ

sinh[4] (kd)


sin 2(kx st)
�


ax ¼ [2][p]T[2][2][H]


cosh k(d z)
þ

sin (kx st)
�
sinh kd



[3][p][3][H] [2]
þ

T [2]L


cosh 2k(d z)
þ

sinh[4] kd


sin 2 (kx st)
�


(3:7)

(3:8)

(3:9)

(3:10)


az ¼ � [2][p]T[2][2][H]


sinh k(d z)
þ

cos (kx st)
�
sinh kd


� [3][p][3][H] [2]

T [2]L


sinh 2k(d z)
þ

cos 2 (kx st)
�
sinh kd


The second-order terms in Eqs. (3.7) to (3.10) also have twice the frequency of
the Wrst-order terms, leading to asymmetries in the particle velocity and acceleration as a particle completes its orbit. The particle velocity and acceleration are
increased under the wave crest and diminished under the wave trough. Again,
these asymmetries increase as the wave steepness increases.

Since the horizontal component of particle velocity is maximum at the wave

crest and trough (and zero at the still water positions), this crest/trough asymmetry in velocity causes particle orbits that are not closed and results in a small
drift of the water particles in the direction of wave propagation. This mass
transport is also evident in the second-order particle displacement equations.


-----

Finite-Amplitude Waves / 59


z
¼ � [H]

2


cosh k(d z)
þ

sin (kx st)
�
sinh kd


pH [2]
þ

8L sinh[2] (kd)


� �

1 sin 2(kx st)
� [3 cosh 2][k][(][d][ þ][ z][)] �

2 sinh[2] (kd)


(3:11)



[p][H] [2]
þ

4L


cosh 2k (d z)
þ

sinh[2] (kd)


st


: (3:12)


« [H]
¼

2


sinh k(d z)
þ

cos (kx st)
�
sinh kd



[3][p][H] [2]
þ

16L


sinh 2k(d z)
þ

sinh[4] (kd)


cos 2(kx st)
�


Note that the last term in Eq. (3.11) is not periodic but continually increases with
time, indicating a net forward transport of water particles as the wave propagates. If we divide the last term in Eq. (3.11) by time we have the second-order
equation for the mass transport velocity


u� [p][2][H] [2]
¼

2TL


cosh 2k(d z)
þ

sinh[2] (kd)


(3:13)


Since the surface particle velocity at the crest of a wave in deep water is pH=T to
the Wrst order, Eq. (3.13) indicates that the surface mass transport velocity is of
the order of the crest particle velocity times the wave steepness and thus generally
much smaller than the crest particle velocity.

Example 3.2-2

Consider the wave discussed in Example 3.2-1. Calculate the mass transport
velocity versus distance below the water surface level for z ¼ 0, � 0:1, � 0:2,
�0:3, � 0:4, and �0.5 times the wave length. Compare this to the wave celerity
and crest particle velocity.

Solution:

For the Wrst or second order, the wave length is given by Eq. (2.17) or

L0 ¼ [9][:][81(7)]2p [2] ¼ 76:5 m

Thus, the water depth is 76:5=2 ¼ 38:25 m and k ¼ 2p=76:5 ¼ 0:0821. Then, the
mass transport velocity, given by Eq. (3.13), becomes


-----

60 / Basic Coastal Engineering

p[2](6)[2]
u�
¼

2(7) (76:5)


cosh 2(0:0821) (d þ z)

sinh[2] (p)


¼ 0:0025 cosh 0:164(d þ z)

where d z is the distance up from the bottom. Proceeding with the calculations
þ
yields:

z (m) d þ z (m) u¯ (m/s)

0 38.25 0.665

�7.65 30.60 0.189

�15.30 22.95 0.053

�22.95 15.30 0.015

�30.60 7.65 0.004

�38.25 0 0.002


Note the rapid decay in the mass transport velocity with distance below the

still water level. From Eq. (2.16) the wave celerity is

C0 ¼ [9][:][81(7)]2p ¼ 10:93 m=s

for both the Wrst and second order. Using the Wrst-order crest particle velocity as
suYcient for comparison purposes we have

uc ¼ [p]7[(6)] ¼ 2:69 m=s

Thus, the celerity, crest particle velocity, and mass transport velocity at the water
surface are 10.93 m/s, 2.69 m/s and 0.665 m/s respectively for this wave.

The pressure Weld in a wave according to the Stokes second order is


p rgz [r][gH]
¼ þ

2


cosh k(d z)
þ

cos (kx st)
�
cosh kd


3prgH [2]
þ

4L sinh 2kd


�cosh 2k(d z) �

þ

� [1]

sinh[2] (kd) 3


cos 2(kx st)
�


(3:14)


prgH[2]
�

4L sinh 2kd [( cosh 2][k][(][d][ þ][ z][)][ �] [1)]

Besides the usual higher frequency second-order term, there is a noncyclic last term
onthe righthandside. This noncyclic termhas azero valueatthe bottomwhichisin
keeping with the requirement that if there is no vertical velocity component at the


-----

Finite-Amplitude Waves / 61

bottom boundary there can be no vertical momentum Xux so the time average
pressure must balance the time average weight of water above. Away from the
bottom there is a time average vertical momentum Xux owing to the crest to trough
asymmetry in the vertical velocity component. This produces the above-zero time
average dynamic pressure given by this last term on the right in Eq. (3.14).

3.3 Cnoidal Waves

The applicability of Stokes theory diminishes as a wave propagates across
decreasing intermediate/shallow water depths. Keulegan (1950) recommended a
range for Stokes theory application extending from deep water to the point
where the relative depth is approximately 0.1. However, the actual Stokes theory
cutoV point in intermediate water depths depends on the wave steepness as well
as the relative depth. For steeper waves, the higher order terms in the Stokes
theory begin to unrealistically distort results at deeper relative depths. For
shallower water, a Wnite-amplitude theory that is based on the relative depth is
required. Cnoidal wave theory and in very shallow water, solitary wave theory,
are the analytical theories most commonly used for shallower water.

Cnoidal wave theory is based on equations developed by Korteweg and de

Vries (1895). The resulting equations contain Jacobian elliptical functions, commonly designated cn, so the name cnoidal is used to designate this wave theory.
The most commonly used versions of this theory are to the Wrst order, but these
theories are still capable of describing Wnite-amplitude waves. The deep water
limit of cnoidal theory is the small-amplitude wave theory and the shallow water
limit is the solitary wave theory. Owing to the extreme complexity of applying
the cnoidal theory, most authors recommend extending the use of the smallamplitude, Stokes higher order, and solitary wave theories to cover as much as
possible of the range where cnoidal theory is applicable.

The most commonly used presentation of the cnoidal wave theory is from

Wiegel (1960), who synthesized the work of earlier writers and presented results
in as practical a form as possible. Elements of this material, including slight
modiWcations presented by the U.S. Army Coastal Engineering Research Center
(1984), are presented herein. The reader should consult Wiegel (1960, 1964) for
more detail and the information necessary to make more extensive cnoidal wave
calculations.

Some of the basic wave characteristics from cnoidal theory, such as the surface

proWle and the wave celerity, can be presented by diagrams that are based on two
parameters, namely k[2] and Ur. The parameter k[2] is a function of the water depth,
the wave length, and the vertical distance up from the bottom to the water
surface at the wave crest and trough. It varies from 0 for the small-amplitude
limit to 1.0 for the solitary wave limit as the ratio of the crest amplitude to wave
height varies from 0 to 1.0 for the two wave theories. Ur, which is known as the


-----

62 / Basic Coastal Engineering

Ursell number (Ursell, 1953), is a dimensionless parameter given as L[2]H=d[3] that
is also useful for deWning the range of application for various wave theories.
From Hardy and Kraus (1987) the Stokes theory is generally applicable for
Ur < 10 and the cnoidal theory for Ur > 25. The theories are equally applicable
in the range Ur ¼ 10 to 25.

Figures 3.1 and 3.2, which are taken from Wiegel (1960) with slight modiWca
tion, allow us to determine the cnoidal wave length, celerity, and surface proWle,
given the wave period and height and the water depth. From Figure 3.1 T(g=d)[0][:][5]

and H/d yield the value of k[2] which then yields (using the dashed line) a value for
the Ursell number. The Ursell number indicates how appropriate cnoidal theory is
for our application and allows the wave length to be calculated if the wave height
and water depth are known. This then gives the wave celerity from C ¼ L=T.

Figure 3.2 is a plot of the water surface amplitude with reference to the

elevation of the wave trough (� ht) as a function of dimensionless horizontal
distance x/L. Thus, h � (� ht) ¼ h þ ht. From Figure 3.2, with the value of k[2]

we can deWne the complete surface proWle relative to the still water line. Note
that when k[2] is near zero the surface proWle is nearly sinusoidal, whereas when k[2]

is close to unity the proWle has a very steep crest and a very Xat trough with the
ratio of crest amplitude to wave height approaching unity.

L[2]H / d [3]

10 100 1000

1-10[−][100]

1-10[−][10]

k[2]

1-10[−][1]


1-10[−][0.1]
10


100 1000

T√g/d


Figure 3.1. Solution for basic parameters of cnoidal wave theory. (ModiWed from

Wiegel, 1964.)


-----

η + η

H


1.0

0.8

0.6

0.4

0.2


0 0.1


Finite-Amplitude Waves / 63

0.2 0.3 0.4 0.5

x / L


k[2]=0

0.9

1-10[−][2]

1-10[−][5]

1-10[−][40]


Figure 3.2. Cnoidal wave theory surface proWles. (ModiWed from U.S. Army Coastal

Engineering Research Center, 1984.)

Example 3.3-1

A wave having a period of 14 s and a height of 2 m is propagating in water 4 m
deep. Using cnoidal wave theory determine the wave length and celerity and compare the results to the small-amplitude theory. Also plot the wave surface proWle.

Solution:

To employ Figure 3.1 we need

H

d 4

[¼][ 2] [¼][ 0][:][5]


and

This gives

and


k[2] 1 10[�][5][:][3]
¼ �

Ur ¼ 300


p

14
¼


ffiffiffiffiffiffiffiffiffiffiffiffiffiffi
9:81=4


¼ 21:9


T


pffiffiffiffiffiffiffiffi

g=d


So the cnoidal theory is quite appropriate for this wave condition. From the
Ursell number the wave length is


L
¼


sffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi

(4)[3]300

2


¼ 98:0 m


and


-----

64 / Basic Coastal Engineering

C ¼ 98:0=14 ¼ 7:0 m=s

Since d/L 4/98 this is a shallow water wave. Using the procedure demonstrated
¼
in Example 2.3–2 for the small-amplitude wave theory we have


¼ 6:26 m=s


C
¼


pffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi

9:81(4)


and


L ¼ 6:26(14) ¼ 87:6 m

The diVerence between the results of the two theories is 11.7% with the small
amplitude theory yielding smaller values of C and L for a given H, T, and d.

With the value of k[2] and the wave length and height, the surface proWle can be

determined from Figure 3.2. A plot of the surface proWle (with a 10:1 vertical
scale exaggeration) is:

η(m)

2 H = 2 m

T = 14 sec.
d = 4 m

1

−40 −20 20 40 x(m)
0

SWL

−1

Note that the ratio of the crest amplitude to the wave height for this wave is 0.86.

For cnoidal theory to the Wrst order the pressure distribution is essentially

hydrostatic with distance below the water surface, i.e.,

p ¼ rg (h � z) (3:15)

Equations are available to calculate the water particle velocity and acceleration
components [see Wiegel (1960,1964)] but they are very complex, involving Jacobian elliptical functions.

3.4 Solitary Waves

A solitary wave has a crest that is completely above the still water level, and no
trough. It is the wave that would be generated in a wave Xume by a vertical
paddle that is pushed forward and stopped without returning to the starting


η(m)

2 H = 2 m

T = 14 sec.
d = 4 m

1

−40 −20 20 40 x(m)
0

−1


-----

Finite-Amplitude Waves / 65

C

H

SWL

d

Figure 3.3. Surface proWle and particle paths for a solitary wave.

position. The water particles move forward as depicted in Figure 3.3 and then
come to rest without returning to complete an orbit. Thus, it is a translatory
rather than an oscillatory wave. It has an inWnite wave length and period. The
surface proWle is depicted by Figure 3.2 as the limit as k[2] approaches unity.

As a long period oscillatory wave propagates in very shallow water of decreas
ing depth, the surface proWle approaches the solitary wave form. But the wave
will break before a true solitary form is reached. The cnoidal wave theory would
still be most appropriate for these very long oscillatory waves in shallow water.
However, owing to the complexity of cnoidal theory, solitary wave theory has
been used by some investigators to calculate wave characteristics in very shallow
relative water depths. Munk (1949) and Wiegel (1964) present good summaries
of the most common forms of solitary wave theory.

As k[2] approaches unity the cnoidal theory surface proWle becomes


C

H

SWL

d


h H sech[2]
¼


"rffiffiffiffiffiffiffiffi #

3H

(x Ct)
�

4d [3]


(3:16)


which deWnes the proWle of a solitary wave. The wave celerity is commonly given by


� �

1 [H]
þ

2d


(3:17)


C
¼


pffiffiffiffiffiffi

gd


but slight variations on Eq. (3.17) have also been developed for solitary wave
celerity.

Thus, at incipient wave breaking (say H/d 0.9; see Chapter 2) the solitary
¼

wave theory celerity will be 45% greater than the small-amplitude wave theory
celerity assuming shallow water conditions.


-----

66 / Basic Coastal Engineering

As a solitary wave approaches, water particles begin to move forward and

upward as depicted in Figure 3.3. As the wave crest passes the particle velocity is
horizontal throughout the water column and reaches its highest value. Then the
particles move downward and forward at decreasing speed until the wave passes.
The most commonly used equations for the horizontal and vertical components
of water particle velocity in a solitary wave are from McCowan (1891). They are


u NC
¼

w NC
¼


� � � �

1 cos M [z][ þ][ d] cosh [Mx]
þ

d d

� � � � ��2 (3:18)

cos M [z][ þ][ d] cosh [Mx]

þ

d d

� � � �

sin M [z][ þ][ d] sinh [Mx]

d d

� � � � ��2 (3:19)

cos M [z][ þ][ d] cosh [Mx]

þ

d d


where the coeYcients N and M are deWned by

Hd M [tan 1]2 �[M][ 1]� [ þ][ H]d ��

[¼][ N]

(3:20)

N [2] � � H��
¼

3 [sin][2][ M][ 1][ þ][ 2]3 d


As a solitary wave passes a point the mass of water transported past that point is
simply the integral of the water surface elevation above the still water level from
x minus to plus inWnity (letting t 0). For a unit width along the wave crest
¼ ¼
this yields the following volume of water:


�16 �1=2

V
¼

3 [d][3][H]


(3:21)


Since the period of a solitary wave is inWnite it is not possible to determine a mass
transport in terms of a mass per unit time. Using the solitary wave theory,
however, the mass transport can be estimated by dividing the water mass
represented by Eq. (3.21) by the period of the wave in question.

A solitary wave also has its energy divided approximately half as poten
tial energy and half as kinetic energy. The total energy for a unit crest width is
given by


-----

Finite-Amplitude Waves / 67


8
E ¼ 3pffiffiffi3 rg (Hd)[3][=][2] (3:22)

Since the length is inWnite it is not possible to determine an energy density for a
solitary wave. Since all of the energy in a solitary wave moves forward with the
wave, the wave power is equal to the product of the wave energy and wave celerity.

Example 3.4-1

Consider the same wave as in Example 3.3–1 (i.e., T 14 s, H 2 m, and d
¼ ¼ ¼
4 m). Using solitary wave theory calculate the wave celerity and compare it to
the results from that example. Also, calculate the crest particle velocity and
compare it with the results from the small-amplitude wave theory.

Solution:

From Eq. (3.17) the wave celerity is

pffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi

C ¼ 9:81(4) (1 þ 2=4 (2) ) ¼ 7:8 m=s

which compares to 6.3 m/s and 7.0 m/s for the small-amplitude and cnoidal wave
theories, respectively.

Given H 2 m and d 4 m, Eqs. (3.20) can be solved simultaneously by trial
¼ ¼

and error to yield

M ¼ 0:88

N ¼ 0:57

Then, with C ¼ 7:8 m=s, z ¼ 2 m, x ¼ 0 we have for the particle velocity at the
wave crest

uc ¼ 0:57(7:8) [1][ þ][ [ cos (0][:][88)6][=][4] cosh (0][:][88) (0)][=][4]

[ cos (0:88)6=4 þ cosh (0:88) (0)=4][2]

or

uc ¼ 1:98 m=s

From Eq. (2.30), for the small-amplitude wave theory in shallow water

rffiffiffiffiffiffiffiffiffi

uc ¼ [2]2 9:481 (1) ¼ 1:6 m=s

Thus, in shallow water there is a signiWcant diVerence between the results from
the two theories. For this wave the true value lies between the two results, but is
probably closer to the result given by the solitary wave theory.


-----

68 / Basic Coastal Engineering

Using the concept of the crest particle velocity being equal to the wave celerity at
breaking, one can derive a limiting value of H/d for wave breaking in shallow
water. This has produced values ranging from 0.73 to 0.83 with a most common
value of 0.78 (see Galvin, 1972). Thus, neglecting the bottom slope because
solitary wave theory is developed for a horizontal bottom, the relationship
H=d ¼ 0:78 should well deWne shallow water breaking conditions. Note that
this is the limit used in Fig. 3.4.

3.5 Stream Function Numerical Waves

The foregoing Wnite-amplitude analytical wave theories are somewhat deWcient
in satisfactorily deWning wave characteristics for waves of large steepness. In
addition, they are generally limited to a range of relative water depths. The use of
numerical techniques with a computer has provided wave theories that have
overcome these diYculties. Another limitation is introduced, however. Rather
than producing equations (however complex) that can be used to calculate wave
characteristic for any H, T, and d condition, the numerical theories directly
produce and tabulate solutions for selected H, T, and d values. Application of


Shallow Intermediate

H0/L0=1/7

H=Hb

L[2]H/d[3]=26

Cnoidal

Small amplitude

0.001 0.005 0.01

d / gT[2]


Shallow Intermediate Deep

H0/L0=1/7

Stokes 5[th]

Stokes 2[nd]

H=Hb/4

L[2]H/d[3]=26

Cnoidal

Small amplitude


0.05


H

gT[2]


0.01

0.005

0.001

0.0005

0.0001

0.00005

0.0005


Deep

Stokes 5

[nd]

0.1


Figure 3.4. Recommended wave theory selection. (Based on LeMehaute, 1969.)


-----

Finite-Amplitude Waves / 69

these results for conditions other than those selected by the practicing engineer
requires interpolation between tabulated results.

The numerical wave theory most used in practice is the stream function theory

developed by Dean (1965). Use of this wave theory is greatly facilitated by a set of
broadly tabulated results (Dean, 1974) published by the U.S. Army Corps of
Engineers. Some other numerical theories, which employ diVerent approaches,
have been presented by Chappelear (1961), Schwartz (1974), and Williams (1985).

Dean uses the stream function c rather than the velocity potential function to

deWne the wave Weld in his numerical theory. Wave motion is Wrst converted to
steady Xow by subtracting the wave celerity from the horizontal motion in the
wave. Thus, the free surface proWle and the bottom become steady-state stream
lines and the stream function becomes constant along these two surfaces.

The boundary value problem is to seek a solution of the Laplace equation

@[2]c

(3:23)

@x[2][ þ][ @]@[2]z[c][2][ ¼][ 0]


for the steady-state surface and bottom boundary conditions written in terms of
the stream function. These become

@c

(3:24)
@x [¼][ 0][ at z][ ¼ �][d]


@c �@c � @h

(3:25)

@x [¼] @z [�] [C] @x [at][ z][ ¼][ h]


1
2


"�@c �2þ�[@][c]�2#

@z [�] [C] @x


þ gh ¼ Q at z ¼ h (3:26)


where Q is the total energy with respect to the still water surface elevation,
u ¼ dc=dz, and w ¼ dc=dx.

The stream function for the small-amplitude wave theory is


c [gH]
¼

2s


sinh k(d z)
þ

cos (kx � st) (3:27)
cosh kd


which deWnes the streamline pattern in a wave with respect to both position and
time. If a steady uniform horizontal Xow is added we have


c Cz [gH]
¼ þ

2s


sinh k(d z)
þ

cos kx (3:28)
cosh kd


which is the steady Xow streamline pattern.


-----

70 / Basic Coastal Engineering

Since the surface proWle is a streamline, with Dean’s theory the measured

surface proWle for a nonlinear wave can be used to calculate the related wave
characteristics. Also, the classic wave problem of calculating the wave characteristics given the wave height and period and the water depth can be solved. The
latter approach is discussed below.

Using the form of (Eq. 3.28) and the form of the Stokes higher order equa
tions, Dean proposed a boundary value solution to the Nth order that had the
following form:


c Cz
¼ þ


N
X

Xn sinh nk(d þ z) cos nkx (3:29)

n¼1


for the stream line pattern in a wave. From Eq. (3.29), the streamline at the
surface cs would be


cs ¼ Ch þ


N
X

Xn sinh nk(d þ h) cos nkx (3:30)

n¼1


Since the surface is a streamline, Eq. (3.30) exactly satisWes the Laplace equation,
the BBC [Eq. (3.24)], and the KSBC [Eq. (3.25)]. The basic problem is to evaluate
the coeYcient Xn to the order desired, the wave number k, and the value of cs
so that they best satisfy the DSBC [Eq. (3.26)]. This is accomplished by evaluating the constant Q in the DSBC at a number of points along the wave. Then,
by trial, the square of the diVerence of each Q value from the average Q value for
these points is minimized. The volumes of water above and below the still water
level [using Eq. (3.30)] must also be equal.

The result is a value for k that deWnes the wave length, the value of Xn that

deWnes the stream function to the desired order, and a value for cs that gives the
surface proWle using Eq. (3.30). With the stream function deWned, all the other
wave characteristics can be determined using standard potential Xow analysis.

The tabulated results presented by Dean (1974) are for 40 dimensionless com
binations of H, Lo( ¼ gT [2]=2p), and d. SpeciWcally, theseinclude 10 values of d=Lo
from deep water (2.0) to shallow water (0.002) and H=Hb ¼ 0:25, 0.50, 0.75, and
1.0 for each d=Lo value. The tabulated results include the wave length, surface
proWle, particle velocity and acceleration Welds, dynamic pressure Weld, group
celerity, energy, and momentum Xux all in dimensionless form. Interpolation is
required if the desired d=Lo and H=Hb values are not included in the 40 sets of
tabulated information.

3.6 Wave Theory Application

When the various wave theories are to be applied in engineering practice two
important concerns must be addressed. The Wrst is which theory to use for a
particular application. The second is how to apply one or more theories over a


-----

Finite-Amplitude Waves / 71

range of relative water depths to analyze the change in wave characteristics as a
wave propagates from one water depth to another.

Range of Application

Selection of the appropriate wave theory to be used for a particular coastal
engineering application depends on several factors. A general guide can be given
in terms of the wave steepness (H=gT [2]) and the relative depth (d=gT [2]), but this
must be tempered by conditions of the actual application.

If one is calculating wave characteristics for a given set of input conditions (H,

T, and d ), these input conditions may be only generally speciWed or they may be
speciWed for a range of values. This may be due to the fact that these input
conditions are only approximately known from wave hindcasts and a shoaling/
refraction analysis for a given return period storm. A very sophisticated wave
calculation may not be justiWed so the easier-to-apply small amplitude theory
may be adequate.

Even if the input values of H, T, and d are fairly precisely known, the

calculated wave characteristics may only need to be approximately known—
thus the advantage of small-amplitude wave theory again. However, if it were
necessary to calculate the surface proWle of a wave in relatively shallow water,
say to determine the loading on the underside of a pier deck, cnoidal or stream
function wave theory would be more appropriate. Or, if the surface proWle of a
wave was being measured in a Weld experiment on wave forces on a pile structure,
the stream function theory might be more appropriate for calculating the wave
particle velocity and acceleration Welds for that surface proWle.

Another factor that compounds the choice of a wave theory for a particular

application is that a particular theory may be better at deWning some characteristics than others. For example, in fairly shallow water, the small-amplitude wave
theory does well at predicting bottom particle velocities, but does not do well at
predicting particle velocities near the surface or the surface proWle itself.

A number of authors including Muir Wood (1969), LeMehaute (1969), and

Komar (1976) have recommended ranges of application of the various wave
theories. These recommendations are based on several factors including the
range of conditions for which the theory was derived, results of experiments on
the eYcacy of the various theories in predicting certain wave characteristics, ease
of application of the theories, and some personal judgment.

Figure 3.4, based on a diagram originally presented by LeMehaute (1969) but

with slight modiWcation by the author, can be used as a starting point in selecting
a wave theory for an engineering application. It is a plot of wave steepness versus
relative depth with breaking wave cutoV limits in deep and shallow water. The
general areas for use of each theory are denoted with the stream function theory
application range deWned by the cross-hatched area. The application range for
small-amplitude wave theory is extended as far as reasonable owing to its ease of


-----

72 / Basic Coastal Engineering

application. The Stokes Wfth-order theory is speciWed where LeMehaute recommends the third- and fourth-order theories for increasing wave steepnesses. The
solitary wave theory is not shown but, depending on the wave characteristics to
be calculated, it may be used in place of the cnoidal theory for very steep waves
in shallow water.

Shoaling Calculations

By equating the wave power from one depth to another Eqs. (2.41) and (2.42) were
developed from the small-amplitude wave theory to predict the resulting change in
wave height as a wave shoals. This change in wave height is dependent only on the
relative depth change, i.e., just the change in depth for a given wave period. If
the wave steepness is not too large this aVords an easy way to calculate the change
in wave height from one water depth to another. Given the new wave height
along with the known wave period and water depth, all of the other wave characteristics can be calculated from the small-amplitude or some Wnite-amplitude wave
theory.

For steeper waves the small-amplitude wave theory is generally less valid.

Finite-amplitude wave theories should be used to calculate changes in wave
height as a wave propagates from one water depth to another. However, most
Wnite-amplitude wave theories are valid only for a limited range of relative
depths. So, to carry out the analysis two theories would have to be coupled at
some intermediate point. This can cause diYculties to arise. Given the same
value of wave power at the coupling point, two diVerent Wnite-amplitude theories
often yield a diVerent value of wave height (and other characteristics) at the
intersection point. Or, if wave heights are matched at the intersection point there
would be a power discontinuity. For Wnite-amplitude wave theories the change in
wave height depends on the initial wave steepness as well as the change in relative
depth. For numerical wave theories that may be valid over a wide range of
relative depths it is not easy to relate wave power values at two depths and
calculate the resulting wave height change.

Nevertheless, a number of eVorts have been made to employ Wnite-amplitude

theories for wave shoaling analysis. See LeMehaute and Webb (1964), Koh and
LeMehaute (1966), Iwagaki (1968), Svendsen and Brink-Kjaer (1972), Svendsen
and Buhr-Hansen (1977), and LeMehaute and Wang (1980) for some of these
eVorts. Walker and Headland (1982) evaluated these various Wnite-amplitude
theory approaches to shoaling analysis along with the available experimental
data on wave shoaling and breaking to develop Figure 3.5. The lowest solid line
in this Wgure is the shoaling curve (H=Ho0 [versus][ d][=][L][o][) from the small-amplitude]

wave theory (i.e., for Ho0 [=][L][o][ near zero). The other solid lines give the shoaling]

curves for increasing deep water wave steepnesses. The dashed lines indicate the
breaker point as the waves shoal, for various beach slopes (i.e., m ¼ 0:05 is a
slope of 1:20).


-----

Finite-Amplitude Waves / 73


H

H09


3.6

3.2

2.8
H0[�]

2.4

2.0

1.6

1.2


0.8

10[-3] 2 5 10[-2] 2 5 10[-1] 2 5 1

d / L0

Figure 3.5. Wave shoaling and breaking characteristics. (Walker and Headland, 1982.)

Example 3.6-1

A wave having a deep water height of 4 m and a period of 11 s shoals with
negligible refraction and breaks on a beach slope of 1:20. Determine the wave
height and water depth just before the wave breaks.

Solution:

From the small-amplitude wave theory

L0 ¼ [9][:][81(11)]2p [2] ¼ 188:9 m


H0[�] /Lo=.001 m=0.1

.002 .05

.004

.006

.008 0.33

.01.15 .02

.02

.04

.06

.08


So


Ho0

L0


4

188:9 [¼][ 0][:][021]


Figure 3.5 then yields (for m ¼ 0:05 and Ho0 [=][L][o][ ¼][ 0][:][021)]


H

H00

d

L0


¼ 1:4

¼ 0:024


-----

74 / Basic Coastal Engineering

Thus, the wave height at breaking

Hb ¼ 1:4 (4) ¼ 5:6 m

and the water depth at breaking

db ¼ 0:024 (188:9) ¼ 4:5 m

The solitary wave theory could then be used to estimate some of the other
characteristics of this wave just before it breaks.

3.7 Summary

Chapters 2 and 3 together present the characteristics and analysis of changes in
the characteristics as a wave propagates from deep water into the point of
breaking and runup on a slope. This is done only for the two-dimensional (x,
z) plane as waves propagate along a nearshore proWle. For a complete analysis of
wave propagation to the shore the three-dimensional eVects of wave refraction,
diVraction, and reXection must also be considered.

3.8 References

Chappelear, J.E. (1961), ‘‘Direct Numerical Calculation of Wave Properties,’’ Journal of

Geophysical Research, Vol. 66, pp. 501–508.

Dean, R.G. (1965), ‘‘Stream Function Representation of Nonlinear Ocean Waves,’’

Journal of Geophysical Research, Vol. 70, pp. 4561–4572.

Dean, R.G. (1974), ‘‘Evaluation and Development of Water Wave Theories for Engin
eering Application,’’ Special Report No. 1, U.S. Army Coastal Engineering Research
Center, Ft. Belvoir, VA.

Dean, R.F. and Dalrymple, R.A. (1984), Water Wave Mechanics for Engineers and

Scientists, Prentice-Hall, Englewood CliVs, NJ.

Galvin, C.J. (1972), ‘‘Wave Breaking in Shallow Water,’’ in Waves on Beaches and

Resulting Sediment Transport (R.E. Myers, Editor) Academic Press, New York,
pp. 413–451.

Hardy, T.A. and Kraus, N.C. (1987), ‘‘A Numerical Model for Shoaling and Refraction of

Second Order Cnoidal Waves Over an Irregular Bottom,’’ Miscellaneous Paper CERC
87–9, U.S. Army Waterways Experiment Station, Vicksburg, MS.

Ippen, A.T. (1966), Estuary and Coastline Hydrodynamics, McGraw-Hill, New York.

Iwagaki, Y. (1968), ‘‘Hyperbolic Waves and Their Shoaling,’’ in Proceedings, 11th Confer
ence on Coastal Engineering, American Society of Civil Engineers, London, pp. 124–144.


-----

Finite-Amplitude Waves / 75

Keulegan, G.H. (1950), ‘‘Wave Motion,’’ in Engineering Hydraulics, (H. Rouse, Editor)

John Wiley, New York, Chapter 11.

Koh, R.C.Y. and LeMehaute, B. (1966), ‘‘Wave Shoaling,’’ Journal of Geophysical Re
search, Vol. 71, pp. 2005–2012.

Komar, P.D. (1976), Beach Processes and Sedimentation, Prentice-Hall, Englewood CliVs,

NJ.

Korteweg, D.J. and de Vries, G. (1985), ‘‘On the Change of Form of Long Waves

Advancing in a Rectangular Canal, and on a New Type of Long Stationary Waves,’’
Philosophical Magazine, Series 5, Vol. 39, pp. 422–443.

LeMehaute, B. (1969), ‘‘An Introduction to Hydrodynamics and Water Waves,’’ Tech
nical Report ERL 118-POL-3–2, U.S. Department of Commerce, Washington, DC.

LeMehaute, B. and Wang, J.D. (1980), ‘‘Transformation of Monochromatic Waves from

Deep to Shallow Water,’’ Technical Report 80–2, U.S. Army Coastal Engineering
Research Center, Ft. Belvoir, VA.

LeMehaute, B. and Webb, L.M. (1964), ‘‘Periodic Gravity Waves over a Gentle Slope at a

Third Order Approximation,’’ in Proceedings, 9th Conference on Coastal Engineering,
American Society of Civil Engineers, Lisbon, pp. 23–40.

McGowan, J. (1891), ‘‘On the Solitary Wave,’’ London, Edinburgh and Dublin Magazine

and Journal of Science, Vol. 32, pp. 45–58.

Muir Wood, A.M. (1969), Coastal Hydraulics, Gordon and Breach, New York.

Munk, H.W. (1949), ‘‘Solitary Wave and Its Application to Surf Problems,’’ Annals, New

York Academy of Science, Vol. 51, pp. 376–424.

Sarpkaya, T. and Isaacson, M. (1981), Mechanics of Wave Forces on OVshore Structures,

Van Nostrand Reinhold, New York.

Schwartz, L.W. (1974), ‘‘Computer Extension and Analytical Continuation of Stokes’

Expansion for Gravity Waves,’’ Journal of Fluid Mechanics, Vol. 62, pp. 552–578.

Skjelbreia, L. (1959), ‘‘Gravity Waves, Stokes Third Order Approximations, Tables of

Functions,’’ Council on Wave Research, Engineering Foundation, University of California, Berkeley.

Skjelbreia, L. and Hendrickson, J.A. (1961), ‘‘Fifth Order Gravity Wave Theory,’’ in

Proceedings, 7th Conference on Coastal Engineering, Council on Wave Research, Engineering Foundation, University of California, Berkeley, pp. 184–196.

Stokes, G.G. (1847), ‘‘On the Theory of Oscillatory Waves,’’ Transactions, Cambridge

Philosophical Society, Vol. 8, pp. 441–455.

Svendsen, I.A. and Brink-Kjaer, O. (1972), ‘‘Shoaling of Cnoidal Waves,’’ in Proceedings,

13th International Conference on Coastal Engineering, American Society of Civil Engineers, Vancouver, pp. 365–383.

Svendsen, I.A. and Buhr-Hansen, J. (1977), ‘‘The Wave Height Variation for Regular

Waves in Shoaling Water,’’ Coastal Engineering, Vol. 1, pp. 261–284.

Ursell, F. (1953), ‘‘The Long Wave Paradox in the Theory of Gravity Waves,’’ Proceed
ings, Cambridge Philosophical Society, Vol. 49, pp. 685–694.


-----

76 / Basic Coastal Engineering

U.S. Army Coastal Engineering Research Center (1984), Shore Protection Manual, U.S.

Government Printing OYce, Washington, DC.

Walker, J. and Headland, J. (1982), ‘‘Engineering Approach to Nonlinear Wave Shoal
ing,’’ in Proceedings, 18th International Conference on Coastal Engineering, American
Society of Civil Engineers, Cape Town, pp. 523–542.

Wiegel, R.L. (1960), ‘‘A Presentation of Cnoidal Wave Theory for Practical Application,’’

Journal of Fluid Mechanics, Vol. 7, pp. 273–286.

Wiegel, R.L. (1964), Oceanographical Engineering, Prentice-Hall, Englewood CliVs, NJ.

Williams, J.M. (1985), Tables of Progressive Gravity Waves, Pitman, London.

3.9 Problems

1. A 8.5 m high, 8 s period wave is propagating in water 30 m deep. Calculate

and plot the water surface proWle over one wave length using the small-amplitude
and Stokes second-order wave theories. Plot the two proWles superimposed and
comment on the diVerence.

2. For the wave given in Problem 1, calculate the water particle velocity at the

still water level under the wave crest using the small-amplitude and Stokes
second-order wave theories.

3. For the wave given in Problem 1, calculate and plot the mass transport

velocity as a function of position along a vertical line from the bottom up to the
still water level.

4. For the wave given in Problem 1, calculate the wave celerity employing

both the second- and the third-order Stokes theories.

5. For the wave given in Problem 1, calculate and plot the pressure distribu
tion along a vertical line under the wave crest from the bottom up to the still
water level.

6. A wave having a height of 2.4 m and a period of 5 s is propagating in water

8 m deep. Is it more appropriate to use the Stokes second-order wave theory or
the cnoidal wave theory to calculate characteristics of this wave?

7. A wave having a deep water height of 5 m and a period of 8 s propagates

toward the shore. Calculate and plot the ratio of ac to at from deep water into a
depth where Ur ¼ 10. For this plot estimate H and L from the small-amplitude
wave theory. Comment on the results.

8. A 7 s period wave having a height of 1.5 m is propagating in water 5.3 m

deep. Plot the surface proWle using the most appropriate theory.

9. A 9 s period wave having a height of 2.1 m is propagating in water 4.5 m

deep. Calculate and plot the surface proWle using the small-amplitude, Stokes
second-order, cnoidal, and solitary wave theories. Plot the four proWles superimposed and comment on the results.


-----

Finite-Amplitude Waves / 77

10. For the wave in Problem 9, calculate the wave celerity and length by each

of the four mentioned theories and comment on the results.

11. A wave has a length of 50 m and a height of 1.9 m in water 7 m deep.

Using the cnoidal wave theory determine the period of this wave. What wave
period would the small-amplitude wave theory yield?

12. Plot the surface proWle of the wave given in Problem 10, using the cnoidal

wave theory.

13. Consider a wave having a period of 12.5 s and a height of 2.1 m in water

3.8 m deep. Using the solitary wave theory calculate the wave celerity, length,
crest particle velocity, and energy. Compare these with the results given by the
small-amplitude wave theory.

14. A section of a beach has a bottom surface layer of shingle (stones with a

diameter of around 100 mm). The water depth is 1.8 m in the vicinity of the
shingle. If the required velocity to initiate movement of these shingle units is
1.5 m/s, will a 1.3 m high wave initiate movement?

15. Show that the maximum water particle velocity in a solitary wave is given

by:

CN
u
¼ � �

1 cos 1 [H]
þ þ

d


16. Demonstrate that the stream function given by Eq. (3.27) represents

irrotational Xow.

17. For the wave given in Example 3.6–1 determine the wave height when the

wave is propagating in water 6 m deep.

18. A 2.5 m high, 12 s period wave in deep water propagates toward the shore

on a 1:30 slope. Determine the wave height, length, and celerity just prior to
breaking by the best procedures available from Chapter 3. Compare the results
of this analysis to results using the small-amplitude wave theory from Chapter 2.

19. A wave having a period of 10 s and a deep water height of 3.5 m propa
gates to the shore in a normal direction. The nearshore beach proWle has a 1:20
slope. Estimate the width of the surf zone.

20. Considering the material presented in this chapter, are waves dispersive in

shallow water? Explain your answer.

21. List three signiWcant ocean wave characteristics that are demonstrated by

Wnite amplitude wave theories, but not by the small amplitude wave theory.


-----

## 4

### Wave Refraction, DiVraction, and ReXection

Consider the design of a protective breakwater for a small marina that is

located on the open coast. A typical design concern would be to predict wave
conditions at interior points in the marina (where vessels will be moored) for a
given deep water design wave height, period, and direction. There must be an
analysis of the change in wave height owing to the change in relative depth from
deep water to the marina interior (as discussed in Chapters 2 and 3). We must
also evaluate the eVects of refraction on wave height and crest orientation as
the wave propagates over the nearshore bottom contours from deep water to the
vicinity of the marina. Then the eVects of diVraction and possibly further
refraction as the wave propagates into the lee of the marina breakwater must
be evaluated. The combined eVects of shoaling, refraction, and diVraction will
yield the resulting wave height and direction of propagation pattern within the
marina. If any of the interior borders of the marina (e.g., vertical bulkheads and
quay walls) have a high reXection coeYcient, reXected waves may also be active
at the points of interest.

4.1 Three-Dimensional Wave Transformation

Wave refraction occurs in transitional and shallow water depths because wave
celerity decreases with decreasing water depths to cause the portion of the wave
crest that is in shallower water to propagate forward at a slower speed than the
portion that is in deeper water. The result is a bending of the wave crests so that
they approach the orientation of the bottom contours. Wave orthogonals, to
remain normal to the wave crest, will also bend so that orthogonals that are
parallel in deep water may converge or diverge as wave refraction occurs. This
convergence or divergence of wave orthogonals will cause local increases or
decreases in wave energy and consequently wave height.

Wave celerity relative to the Wxed sea Xoor will also depend on the possible

existence of an ocean current. If a train of waves crosses a region where there is a


-----

80 / Basic Coastal Engineering

horizontal gradient in the current velocity the waves will be refracted. This
phenomenon is common, for example, when deep water waves from the Atlantic
Ocean cross the Gulf Stream near the U.S. coastline or when waves propagating
toward the coast interact with the tide-induced ebb current at a coastal entrance.

DiVraction will occur when the height of a wave is greater at one point along a

wave crest than at an adjacent point. This causes a Xow of energy along the crest
in the direction of decreasing height and a consequent adjustment of wave height
along the crest as the wave propagates forward. This is particularly important,
for example, when a wave crest is truncated as it passes the end of a structure
that extends out into the water. DiVraction will then cause a Xow of wave energy
into the shadow region in the lee of the structure. DiVraction also occurs
whenever wave refraction causes wave height diVerences along a wave crest.
However, for many (but not all) wave refraction analyses the eVect of diVraction
on wave height changes is a second-order eVect that may be neglected. In this
chapter, we will consider refraction and diVraction separately and then look at
the techniques available to evaluate the combined eVects of refraction and
diVraction where they are important and can be evaluated.

The two-dimensional aspects of wave reXection were discussed in Section 2.7.

When the incident wave crest is not completely parallel to a reXecting structure
the reXected wave crest will have a changed orientation from that of the incident
wave.

The eVects of wave shoaling, refraction, and diVraction all depend on the

period of the wave being considered. Also, the eVects of wave refraction and
diVraction depend on the incident direction of the wave. Thus, for a spectrum of
wind-generated waves having a range of component periods and directions, the
diVerent components of the spectrum will be aVected diVerently as they propagate from deep water to the point of interest. The components of a wave
spectrum can be analyzed separately and then regrouped to approximate the
nearshore characteristics of the spectrum. An easier approach, commonly used
for many engineering analyses, is to select a single representative wave height,
period, and direction to represent the spectrum of waves and to analyze the
behavior of this wave as it propagates toward the shore.

A related phenomenon that involves the planform transformation of waves is

vessel-generated waves. The generation, resulting wave crest patterns, and behavior of vessel-generated eaves will be presented in Section 4.9.

4.2 Wave Refraction

Figure 4.1 shows a hypothetical shoreline and nearshore bottom contours.
A wave train with a deep water wave length Lo is approaching the shore with a
crest orientation in deep water that is parallel to the average shoreline position.
Bottom contour depths are given in terms of the deep water wave length. As


-----

Wave Refraction, Diffraction, and Reflection / 81

_B_ 2

Wave

breakers _d/Lo = 0.1_

0.2

1 1

0.3

0.4

0.5

Bottom contour

_Lo_ Wave

orthogonal

_Bo_ Wave crest

Figure 4.1. Wave refraction pattern.

portions of the wave crest enter the region where d=Lo < 0:5 the wave length and
celerity commence to decrease [as given by Eqs. (2.13) and (2.14)]. The result is
the refraction of the wave train with the wave crest orientations approaching the
orientation of the bottom contours as the waves propagate shoreward. If one
constructs equally spaced orthogonal lines along the deep water wave crests and
extends these lines toward the shore, being sure that they remain normal to the
wave crests, one can see the pattern of energy distribution at any point along a
wave crest. Where orthogonals converge there is an increase in the energy per
unit crest length, and vice versa.

The wave refraction diagram shown in Figure 4.1 deWnes the wave crest

orientation as the wave propagates forward and allows one to determine the
change in wave height owing to wave refraction. The convergence and divergence
of the wave orthogonals along with the eVects of wave shoaling cause the wave
height variation from deep water deWned by


_B_ 2

Wave

breakers

1 1

_Lo_

_Bo_ Wave crest


ffiffiffiffiffiffi
Bo

B


H

Ho


r


¼


rffiffiffiffiffiffiffiffiffirffiffiffiffiffiffi

Lo Bo


2nL


B


¼ [H]0

Ho


(2:42)


In Eq. (2.42), the shoaling coeYcient (Ks ¼ H=Ho0 [) is only a function of][ d][=][L][o][.]

The orthogonal spacing ratio (Bo=B ¼ Kr[2][) for a nearshore point of interest must]

be determined from a refraction analysis. The calculated change in wave height
employing Eq. (2.42) yields a wave height value that is the average over the
orthogonal spacing B. This may require the use of smaller orthogonal spacings in
deep water to suYciently deWne the wave height at a desired nearshore location,
especially if the hydrography is complex.


-----

82 / Basic Coastal Engineering

Note in Figure 4.1 that refraction causes a convergence of orthogonals over

the submerged ridge (point 1), resulting in higher waves that break further
oVshore. Over the submerged trough (point 2), wave heights are lower than
they would be over the ridge and can actually be much lower than the deep
water height if the eVect of refraction in lowering the wave height is greater than
the increase in wave height owing to shoaling.

Since wave celerity depends on the wave period, waves with diVerent periods

will refract diVerently as they approach the shore. Longer period waves begin to
feel bottom and refract in deeper water and consequently may undergo greater
refraction as they approach the shore. The resulting wave refraction pattern will
also be diVerent for each diVerent deep water approach direction. For a typical
wave analysis at a coastal site refraction patterns must be investigated for a
representative range of wave periods and deep water directions to determine the
most critical wave height/direction combinations at the site.

It should be noted that some empirical data for wave processes are presented

in terms of the unrefracted deep water wave height Ho0 [(e.g., see Figures 2.11 and]

2.15). If a wave having a deep water height Ho refracts into a nearshore location
where the refraction coeYcient is Kr then the unrefracted deep water height to be
used in these diagrams is Ho0 [¼][ K][r][H][o][.]

Refraction analyses were initially done by the manual construction of refrac
tion diagrams. Now they are mostly done by numerical/computer analysis,
except for situations that only involve a limited number of wave conditions for
a speciWc location when manual construction of a refraction diagram may
reasonably be carried out. We will present the common procedures used for
both manual and numerical refraction analysis.

4.3 Manual Construction of Refraction Diagrams

The Wrst method used for the construction of refraction diagrams is known as the
wave crest method (Johnson et al., 1948). Working on a hydrographic chart of the
study area, a wave crest having the proper orientation is constructed in deep water.
Then, points along the wave crest are advanced normal to the crest by an integral
number of wave lengths and the new crest position is drawn. This process is
continued until the crest pattern from deep water into the shore is constructed.
Given the deep water wave length and the local average water depth over which the
wave will advance, the advancing wave length (or an integral number of wave
lengths) can be calculated from Eq. (2.18). A template that graphically solves Eq.
(2.18) (see Wiegel, 1964) may be constructed to simplify the plotting of crest
positions. After all of the crest positions for the advancing wave train are drawn,
orthogonal lines are constructed normal to the wave crests at desired intervals.

The wave crest method is presented because it is of historic interest and it

provides a simple explanation of the wave refraction process. However, for


-----

Wave Refraction, Diffraction, and Reflection / 83

engineering analysis it is most important to produce an accurate depiction of the
wave orthogonal pattern, so satisfactory computation of wave height patterns
can be accomplished. The orthogonal lines also depict the local direction of wave
propagation. Thus, a procedure that directly produces the orthogonal pattern is
preferable to the wave crest method where the orthogonal lines are less accurately constructed. After the orthogonal pattern is constructed wave crests can be
drawn if so desired.

A second graphical method for constructing refraction diagrams, known as

the orthogonal method, is based on Snell’s Law which may be derived by
considering Figure 4.2. Consider a train of waves propagating over a step
where the water depth instantaneously decreases from d1 to d2 (ignore wave
reXection by the step). This causes the wave celerity and length to decrease from
C1 and L1 to C2 and L2, respectively. For an orthogonal spacing x and a time
interval T, sin a1 ¼ C1T=x and sin a2 ¼ C2T=x. Dividing yields


sin a1
sin a2



[C][1]
¼

C2



[L][1]
¼

L2


(4:1)


which is Snell’s Law for wave refraction. Applying Eq. (4.1) to wave refraction
over a gradually varying bottom slope, a1 and a2 become the angles between the
wave crest and bottom contour line at successive points along an orthogonal as a
wave propagates forward, and L1 and L2 become the wave lengths at the points
where a1 and a2 are measured.

Wave

crest

Orthogonais

x α1 _d1_

α2 _d2_

α2 _L2 = C2T_

_d1 > d2_
_C1 > C2_

_L1 > L2_

Figure 4.2. DeWnition sketch for Snell’s law derivation.


crest

Orthogonais

x α1 _d1_

α2 _d2_

α2 _L2 = C2T_

_d1 > d2_
_C1 > C2_

_L1 > L2_


-----

84 / Basic Coastal Engineering


ox d/L0=0.5

α

x

Shore

Figure 4.3. Wave refraction over straight parallel bottom contours.

When waves propagate shoreward over bottom contours that are essentially

straight and parallel as shown in Figure 4.3


αo

x

α

x

Shore


sin ao

Lo



[sin][ a] [1]
¼ ¼

L x


if we choose Bo and B so that the orthogonal lengths equal Lo and L as shown.
Then,


B
x
¼ ¼

cos a


ffiffiffiffiffiffi
Bo

B


or

where


Bo

cos ao

r

Kr ¼


(4:2)

(4:3)


r


cosffiffiffiffiffiffiffiffiffiffiffiffiffi ao

cos a


¼


� C �

a ¼ sin[�][1] sin ao

Co


Equations (4.2) and (4.3) allow one to determine the refracted wave height [also
using Eq. (2.42)] and wave crest orientation or orthogonal direction when waves
refract over essentially uniform nearshore hydrography. Note that the nearshore
bottom slope does not enter the analysis as long as the bottom contours are
essentially straight and parallel. Wiegel and Arnold (1957) conducted wave tank
tests on uniform slopes and found Snell’s Law valid for deep water incident wave
angles between 108 and 708 and bottom slopes ranging from 1:10 to vertical (step).


-----

Wave Refraction, Diffraction, and Reflection / 85

Example 4.3-1

Consider the wave from Examples 2.3-1 and 2.3-2 which has a deep water height
of 2 m and a period of 10 s. Assume the wave crests in deep water are oriented at
an angle of 358 with the shoreline and that the nearshore bottom contours are
essentially straight and parallel to the shoreline. Determine the wave height and
crest orientation with respect to the shoreline when the wave propagates into
water 2.3 m deep.

Solution:

From Examples 2.3-1 and 2.3-2 respectively, Co ¼ 15:6 m=s and at d ¼ 2:3 m,
C ¼ 4:75 m=s.

Then for an oVshore angle of 358, Eq. (4.3) yields

�4:75 �

a ¼ sin[�][1] ¼ 9:5[�]
15:6 [sin 35][�]

which is the angle between the wave crest and the shoreline at the water depth of
2.3 m.

From Eq. (4.2)

rffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi

cos 35[�]

Kr ¼ cos 9:5[�] ¼ 0:91

which is the refraction coeYcient from deep water to the 2.3 m water depth.

Since Co=C ¼ Lo=L and n ¼ 1:0 for the shallow water depth of 2.3 m, Eq.

(2.42) yields

sffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi

H 15:6

¼ ¼ 1:166

Ho 2(1)(4:75) [(0][:][91)]

or

H ¼ 2(1:166) ¼ 2:33 m

Thus, wave refraction decreases the wave height but the height increase caused
by wave shoaling is greater, so there is a net increase in the wave height from
deep water to the point where the depth is 2.3 m.

The commonly used orthogonal method for manual construction of wave refraction diagrams for irregular hydrography is based on Arthur et al. (1952).
Essentially, as one progresses shoreward it is assumed that the bottom


-----

86 / Basic Coastal Engineering

topography is horizontal from a contour line to the midpoint to the next contour
line where the bottom is stepped up to the depth represented by that next contour
line. Snell’s Law is applied at this midpoint step to predict the change in
orthogonal line direction that would gradually occur over the particular contour
interval being traversed.

To assist this graphical procedure for laying out orthogonal lines on a hydro
graphic chart, the template shown in Figure 4.4 has been developed. For practical use, a template scaled so that the distance from the turning point to the
orthogonal line is about 15 cm and printed on a transparent sheet should be
employed for refraction diagram construction on most hydrographic charts.
A pin is placed through the turning point and the ratio of the wave celerities at
the two contour lines deWning the interval being crossed controls the change in
orthogonal direction.

The procedure for constructing an orthogonal line on a hydrographic chart is

as follows:

1. Locate the depth contour represented by d=Lo ¼ 0:5 on the hydrographic

chart for the area of interest. Then label each of the shallower contours in
terms of the relative depth d=Lo. Bottom contour irregularities that are
smaller than about one wave length do not appreciably aVect wave behavior and may be smoothed out.

2. For each contour line and the one landward of it calculate the ratio of wave

celerities C1=C2 where C1 is the celerity at the deeper contour. From Eq.
(2.13)

20�

∆α

10�

Turning

point

1.2 1.1 0.9 0.8

C1/C2 C2/C1

10�

∆α

20�

Figure 4.4. Template for orthogonal refraction analysis.


20�

∆α

10�

Turning

point

1.2 1.1 0.9 0.8

C1/C2 C2/C1

10�

∆α

20�


-----

Wave Refraction, Diffraction, and Reflection / 87


C1
C2


¼


� �

tanh [2][p][d][1]

L1

� �

tanh [2][p][d][2]

L2


where d/L can be determined by trial and error from Eq. (2.18) reorganized as


d

Lo



[d] � �
¼

L [tanh 2][p]L[d]


3. Starting at the two most seaward contours, construct a line that is a

midcontour halfway between these two contours; extend the incoming
deep water orthogonal straight to the midcontour, and construct a line
tangent to the midcontour at the intersection of the midcontour and the
incoming orthogonal.

4. Lay the template (Figure 4.4) with the line marked orthogonal over the

incoming orthogonal and C1=C2 ¼ 1:0 at the intersection of the midcontour and the orthogonal.

5. Rotate the template around the turning point until the calculated value of

C1=C2 intersects the tangent to the midcontour line. The line on the template
labeled orthogonal now lies in the direction of the outgoing orthogonal.
However, it is not at the correct position for the outgoing orthogonal.

6. With a pair of triangles, move the outgoing orthogonal to a parallel

position such that the incoming and outgoing orthogonals connect and
the lengths of these two orthogonal lines are equal (thus the two orthogonals may not cross exactly at the midcontour line).

7. Repeat the above procedure at successive contour intervals to extend the

orthogonal line forward toward the shore.

8. Repeat the above procedure for additional orthogonal lines as needed.

The usual objective in constructing a refraction diagram is to evaluate wave
height and direction at a particular point or points nearshore. To do this, at least
two orthogonal lines are needed and they should arrive at the shore bracketing
the point of interest with not too large of a spread. Experience and some forethought are necessary to start the orthogonals in deep water at a point that will
lead to the desired location on shore.

Orthogonals may be constructed from shallow to deep water using the above

procedure except that C2=C1 values are used where C1 is still the wave celerity at
the deeper contour line. For example, selecting a range of seaward projecting
directions at a nearshore point and constructing orthogonals seaward from these
initial directions would demonstrate the range of oVshore directions from which
waves will reach the shoreline site.


-----

88 / Basic Coastal Engineering

To obtain suYcient accuracy, Arthur et al. (1952) recommend a contour

spacing such that the absolute value of DC=C1 < 0:2 and Da < 15[�]. If the
angle between the wave crest and the bottom contour exceeds 808, the above
procedure is not suYciently accurate. A modiWed procedure presented by the
U.S. Army Coastal Engineering Research Center (1984) should be used.

Figure 4.5 is a refraction diagram constructed by the above procedure. It

shows the orthogonal pattern for 7 s waves approaching the shore from S
308 E. Note how refraction concentrates wave energy at the breakwater dogleg
(Bo=B > 4) and spreads energy at the breakwater head (Bo=B < 1). Additional
orthogonal lines might be constructed for this wave condition to better deWne the
variation of wave height along the breakwater and the wave height and direction
of propagation at the breakwater head. The former is desirable for the structural
design of the breakwater and the latter (as will be seen later) is desirable for
predicting wave conditions in the lee of the breakwater.

Occasionally, when refraction diagrams are constructed a pair of orthogonals

will cross, forming a caustic point. As the orthogonal lines approach the caustic

−5

−10

−15

−20

−25

−30

−35

−40

Figure 4.5. Wave refraction diagram for 7 s wave from S 308 E. (Sorensen, 1993.)


−5

−10

15

40


-----

Wave Refraction, Diffraction, and Reflection / 89

point their spacing approaches zero so the wave height would approach inWnity.
In reality, before the orthogonals cross there would be wave breaking and
reformation. The wave conditions in the lee of the caustic would then not be
well deWned by the refraction diagram.

4.4 Numerical Refraction Analysis

Numerical refraction analysis by computer requires that the equations for wave
orthogonal position and spacing be developed for a wave propagating through
water of changing depth. These equations, presented by Arthur et al. (1952), are
summarized below.

Figure 4.6 depicts a wave orthogonal crossing a bottom contour where the

orthogonal position is given in an horizontal x, y coordinate system. DeWne u as
the angle between the x axis and a tangent to the wave orthogonal, and s and n as
the distances along the orthogonal and wave crest from their point of crossing.
Then, from the geometry of the system, an equation deWning the redirection of
the orthogonal is


du

ds C

[¼ �] [1]


dC

(4:4)
dn


Equation (4.4) states that the curvature of the wave orthogonal depends on the
gradient of the wave celerity normal to the direction of wave propagation (i.e.,
along the wave crest) and that the wave orthogonal bends toward the region of
lower wave celerity. This is a general statement of the wave refraction process. By
the chain rule we can write Eq. (4.4) as

y

Orthogonal

Crest

Bottom

s

contour

n θ

x

Figure 4.6. DeWnition sketch for Eq. (4.4).


Orthogonal

Crest

s

n θ


-----

90 / Basic Coastal Engineering

du � �

ds C [sin][ u][ dC]dx dy

[¼][ 1] [�] [cos][ u][ dC]


(4:5)


Equation (4.5) must be solved to deWne the progressive positions of a wave
orthogonal as the wave propagates forward. Given the incoming orthogonal
direction in the x, y coordinate system, and determining the wave celerity and x
and y component gradients of the celerity at a point in the x, y coordinate system
one can determine the change in the orthogonal direction at that point. The
celerity, from the small-amplitude wave theory, depends on the wave period and
water depth at the point of interest. The component gradients of the celerity can
be determined in Wnite diVerence form from the celerity at two adjacent points
separated by a distance x or y. The computed change in orthogonal direction at a
point (du=ds) is employed to extend the orthogonal a Wnite distance to a new
point where the new orthogonal direction change is computed, etc. This allows
the orthogonal line to be advanced in steps toward the shore. The nearshore
hydrography is set up on an x, y grid system and an interpolation scheme is
established to compute values of dC/dx, dC/dy, and C at intermediate points
reached by the extended orthogonal. Smaller grids improve accuracy at the cost
of greatly increased computer time.

See Griswold (1963), Wilson (1966), Jen (1969), Keulegan and Harrison

(1970), Crowley et al. (1982), Headland and Chiu (1984) and Oh and Grosch
(1985) for applications of these refraction analysis techniques including the use
of Wnite-amplitude wave theory, diVerent interpolation schemes, and variable
forward step distances to provide increased accuracy in shallower water. The
orthogonal spacing can be computed as two orthogonals are extended shoreward
to yield values of the refraction coeYcient along the wave orthogonals. As an
alternative, Munk and Arthur (1951) developed a set of equations that predict
the spacing of a pair of closely spaced orthogonals (and thus Kr) at any point
along a wave orthogonal. These equations can be employed along with the
computation of the path of a single orthogonal propagating toward the shore.

An alternative to the above procedure is to use the conservation of waves

equation which equates the number of waves entering and leaving a twodimensional (x, y) region. This equation can be written (see Dean and Dalrymple, 1984)

k cos u [@][u] (4:6)

@x [þ][ k][ sin][ u][ @]@y[u] [¼][ cos][ u][ @]@[k]y [�] [sin][ u][ @]@x[k]


where k is the wave number equal to 2p=L. Equation (4.6) would be solved
numerically over an x, y grid to determine values of u for the points on that grid.
Given the deep water direction of the wave orthogonal, the orthogonal can be
extended shoreward using interpolated values of u as the orthogonal is extended
forward. See Noda et al. (1974) and Perlin and Dean (1983) for examples of this


-----

Wave Refraction, Diffraction, and Reflection / 91

approach. The latter coupled their solution with a conservation of energy Xux
equation which could incorporate energy dissipation as the wave propagated
forward to more realistically calculate wave heights. Hardy and Krauss (1987)
and Cialone and Krauss (1987) used both the conservation of waves and conservation of energy Xux equations with Wnite-amplitude wave theory to carry out
wave refraction and shoaling analyses.

4.5 Refraction by Currents

When a wave train propagates in a region where there is a current of varying
velocity, the wave celerity relative to the Wxed sea Xoor will change, causing the
wave to refract. Johnson (1947) presented an analysis of this phenomenon
assuming deep water waves. A similar analysis can be carried out for intermediate and shallow water waves. The results would be similar but with much more
complex equations.

Consider Figure 4.7, which depicts a wave propagating from still water to

water having a current velocity U. The orthogonal direction relative to the
current interface changes from a to ac and the wave crest and orthogonal pattern
change as shown. From the geometry of this Wgure Johnson showed that

sin a
sin ac ¼ � �2 (4:7)

1
� [U]

C [sin][ a]


where U/C would be negative when the current opposes the wave direction and
vice versa. From the conservation of energy Xux between two orthogonals
Johnson found the following relationship for wave height change:

Crest

U

Orthogonal

αc

α

Still

water

Figure 4.7. DeWnition sketch for wave refraction by a current.


Crest

U

Orthogonal

αc

α

Still

water


-----

92 / Basic Coastal Engineering


"�1 � [U]C [sin][ a]�6#

1 þ [U]C [sin][ a]


�Hc�2

Lc


�H�2 cos a

¼

L cos ac


(4:8)


where


Lc ¼ L [sin]sin[ a] a[c]

When waves enter a navigation channel where the current is ebbing, the current
will cause the waves to decrease in length and increase in height, possibly to the
point of breaking. This can have serious negative consequences on navigation,
particularly for small vessels. Perigrine (1976) found that if the ebb current is
about 0.3 times the celerity that the approaching wave has oVshore in still water,
waves will break in the channel no matter what the approaching wave steepness
may be. For waves entering a channel with a Xood current the wave steepness is
decreased, which would have a positive eVect of vessel navigation.

The creation of an opposing current, for example by a surface water jet or by

rising air bubbles, has been used to dissipate wave energy, particularly by steepening and breaking the waves. This would be more eVective for shorter steeper waves
thanforthelongercomponentsofawavespectrum,andonewouldhavetoevaluate
the cost of the energy required to operate the system versus the eVect achieved.

4.6 Wave DiVraction

Consider a train of waves approaching a barrier as shown in Figure 4.8. The
portion of the wave that hits the barrier will be reXected and dissipated, with the
possible transmission of some wave energy through or over the barrier depending

incident

wave direction

Constant

depth

Hd

r

Point of

interest

Hi Barrier

Wave crest

Figure 4.8. DeWnition sketch for wave diVraction in the lee of a barrier.


incident

wave direction

Constant

depth

Hd

r

Point of

interest

Hi Barrier

Wave crest


-----

Wave Refraction, Diffraction, and Reflection / 93

on the cross-section geometry and composition of the barrier. The portion of the
wave passing the end of the barrier will have a lateral transfer of wave energy along
the wave crest into the lee of the barrier. The diVracted wave crests in the lee of the
barrier will form approximately concentric circular arcs with the wave height
decreasing exponentially along the crests. The shadow region out to the dashed
line will have a wave height that is less than the incident wave height at the end of
the barrier. Note that the water depth in Figure 4.8 is constant; otherwise the wave
crest pattern and wave heights would also be aVected by refraction.

If Hi is the incident wave height at the end of the barrier and Hd is the diVracted

wave height at a point of interest in the lee of the barrier, we can deWne a diVraction
coeYcient Kd Hd=Hi.Thevalueof Kd dependsonthelocationbehindthebarrier
¼
deWned by r and b,and the incidentwave direction deWned by u; or in dimensionless
form Kd ¼ f (u, b, r=L)where L isthe wavelength inthe leeofthe barrier. Sincethe
wave length is a function of the wave period and water depth, the resulting
diVraction coeYcient for each component of the wave spectrum would depend
on the incident direction and period of that component.

Water wave diVraction is analogous to the diVraction of light. The two most

common diVraction problems encountered in coastal engineering design are
diVraction past the end of a semi-inWnite barrier as depicted in Figure 4.8
and diVraction through a relatively small gap in a barrier. Penny and Price
(1952) showed that the mathematical solution for the diVraction of light can be
used to predict the wave crest pattern and height variation for these two wave
diVraction problems.

Semi-inWnite Barrier

A summary of the diVraction solution for a semi-inWnite barrier is presented by
Wiegel (1964) and by Putnam and Arthur (1948), who also conducted some wave
tank experiments to verify results. Wiegel (1962) used the Penny and Price (1952)
solution to calculate and tabulate values of Kd for selected values of u, b, and r/
L. His results are tabulated in Table 4.1. Graphic plots of the tabulated results
are also presented in Wiegel (1962, 1964) and the U.S. Army Coastal Engineering
Research Center (1984). Figure 4.9 is an example of these diagrams for the
incident wave approach angle (u) of 908. The horizontal position of the point
of interest in Figure 4.9 is given in the usual x, y coordinate system nondimensionalized by dividing by the wave length.

A curious result depicted in Figure 4.9 and common to other wave approach

directions as shown in Table 4.1 is that the value of Kd along a line extending
back from the end of the barrier in the direction of the incident wave is about 0.5.
It should also be noted in Figure 4.9 and in Table 4.1 that regions outside of the
lee of the barrier have Kd values in excess of unity. These values develop because
the theoretical solution assumes a perfectly reXecting barrier and a small portion
of the reXected wave energy diVracts to add to the energy of the incident wave in


-----

94 / Basic Coastal Engineering

Table 4.1. Kd versus u, b, r/L for Semi-InWnite Breakwater

b (Degrees)

r/L 0 15 30 45 60 75 90 105 120 135 150 165 180

u ¼ 15[�]

1/2 0.49 0.79 0.83 0.90 0.97 1.01 1.03 1.02 1.01 0.99 0.99 1.00 1.00

1 0.38 0.73 0.83 0.95 1.04 1.04 0.99 0.98 1.01 1.01 1.00 .100 1.00

2 0.21 0.68 0.86 1.05 1.03 0.97 1.02 0.99 1.00 1.00 1.00 1.00 1.00

5 0.13 0.63 0.99 1.04 1.03 1.02 0.99 0.99 1.00 1.01 1.00 1.00 1.00

10 0.35 0.58 1.10 1.05 0.98 0.99 1.01 1.00 1.00 1.00 1.00 1.00 1.00

u ¼ 30[�]

1/2 0.61 0.63 0.68 0.76 0.87 0.97 1.03 1.05 1.03 1.01 0.99 0.95 1.00

1 0.50 0.53 0.63 0.78 0.95 1.06 1.05 0.98 0.98 1.01 1.01 0.97 1.00

2 0.40 0.44 0.59 0.84 1.07 1.03 0.96 1.02 0.98 1.01 0.99 0.95 1.00

5 0.27 0.32 0.55 1.00 1.04 1.04 1.02 0.99 0.99 1.00 1.01 0.97 1.00

10 0.20 0.24 0.54 1.12 1.06 0.97 0.99 1.01 1.00 1.00 1.00 0.98 1.00

u ¼ 45[�]

1/2 0.49 0.50 0.55 0.63 0.73 0.85 0.96 1.04 1.06 1.04 1.00 0.99 1.00

1 0.38 0.40 0.47 0.59 0.76 0.95 1.07 1.06 0.98 0.97 1.01 1.01 1.00

2 0.29 0.31 0.39 0.56 0.83 1.08 1.04 0.96 1.03 0.98 1.01 1.00 1.00

5 0.18 0.20 0.29 0.54 1.01 1.04 1.05 1.03 1.00 0.99 1.01 1.00 1.00

10 0.13 0.15 0.22 0.53 1.13 1.07 0.96 0.98 1.02 0.99 1.00 1.00 1.00

10

kd=1.0 1.0 1.0 1.0

0.9 0.9

0.9 0.8

8 0.7


x
L


6

4

2

0
8


kd=1.0 1.0 1.0 1.0

0.9 0.9

0.9 0.8

0.7

0.6

0.5

0.4

0.3

0.2

0.1

�

8 6 4 2 0 2 4 6 8

Barrier


y / L


Barrier


Figure 4.9. Wave crest pattern and related Kd values for normal wave incidence. (Wiegel,

1962.)


-----

(Table 4.1. continued.)


Wave Refraction, Diffraction, and Reflection / 95

b (Degrees)


r/L 0 15 30 45 60 75 90 105 120 135 150 165 180

u ¼ 60[�]

1/2 0.40 0.41 0.45 0.52 0.60 0.72 0.85 1.13 1.04 1.06 1.03 1.01 1.00

1 0.31 0.32 0.36 0.44 0.57 0.75 0.96 1.08 1.06 0.98 0.98 1.01 1.00

2 0.22 0.23 0.28 0.37 0.55 0.83 1.08 1.04 0.96 1.03 0.98 1.01 1.00

5 0.14 0.15 0.18 0.28 0.53 1.01 1.04 1.05 1.03 0.99 0.99 1.00 1.00

10 0.10 0.11 0.13 0.21 0.52 1.14 1.07 0.96 0.98 1.01 1.00 1.00 1.00

u ¼ 75[�]

1/2 0.34 0.35 0.38 0.42 0.50 0.59 0.71 0.85 0.97 1.04 1.05 1.02 1.00

1 0.25 0.26 0.29 0.34 0.43 0.56 0.75 0.95 1.02 1.06 0.98 0.98 1.00

2 0.18 0.19 0.22 0.26 0.36 0.54 0.83 1.09 1.04 0.96 1.03 0.99 1.00

5 0.12 0.12 0.13 0.17 0.27 0.52 1.01 1.04 1.05 1.03 0.99 0.99 1.00

10 0.08 0.08 0.10 0.13 0.20 0.52 1.14 1.07 0.96 0.98 1.01 1.00 1.00

u ¼ 90[�]

1/2 0.31 0.31 0.33 0.36 0.41 0.49 0.59 0.71 0.85 0.96 1.03 1.03 1.00

1 0.22 0.23 0.24 0.28 0.33 0.42 0.56 0.75 0.96 1.07 1.05 0.99 1.00

2 0.16 0.16 0.18 0.20 0.26 0.35 0.54 0.69 1.08 1.04 0.96 1.02 1.00

5 0.10 0.10 0.11 0.13 0.16 0.27 0.53 1.01 1.04 1.05 1.02 0.99 1.00

10 0.07 0.07 0.08 0.09 0.13 0.20 0.52 1.14 1.07 0.96 0.99 1.01 1.00

u ¼ 105[�]

1/2 0.28 0.28 0.29 0.32 0.35 0.41 0.49 0.59 0.72 0.85 0.97 1.01 1.00

1 0.20 0.20 0.24 0.23 0.27 0.33 0.42 0.56 0.75 0.95 1.06 1.04 1.00

2 0.14 0.14 0.13 0.17 0.20 0.25 0.35 0.54 0.83 1.08 1.03 0.97 1.00

5 0.09 0.09 0.10 0.11 0.13 0.17 0.27 0.52 1.02 1.04 1.04 1.02 1.00

10 0.07 0.06 0.08 0.08 0.09 0.12 0.20 0.52 1.14 1.07 0.97 0.99 1.00

u ¼ 120[�]

1/2 0.25 0.26 0.27 0.28 0.31 0.35 0.41 0.50 0.60 0.73 0.87 0.97 1.00

1 0.18 0.19 0.19 0.21 0.23 0.27 0.33 0.43 0.57 0.76 0.95 1.04 1.00

2 0.13 0.13 0.14 0.14 0.17 0.20 0.26 0.16 0.55 0.83 1.07 1.03 1.00

5 0.08 0.08 0.08 0.09 0.11 0.13 0.16 0.27 0.53 1.01 1.04 1.03 1.00

10 0.06 0.06 0.06 0.07 0.07 0.09 0.13 0.20 0.52 1.13 1.06 0.98 1.00

u ¼ 135[�]

1/2 0.24 0.24 0.25 0.26 0.28 0.32 0.36 0.42 0.52 0.63 0.76 0.90 1.00

1 0.18 0.17 0.18 0.19 0.21 0.23 0.28 0.34 0.44 0.59 0.78 0.95 1.00

2 0.12 0.12 0.13 0.14 0.14 0.17 0.20 0.26 0.37 0.56 0.84 1.05 1.00

5 0.08 0.07 0.08 0.08 0.09 0.11 0.13 0.17 0.28 0.54 1.00 1.04 1.00

10 0.05 0.06 0.06 0.06 0.07 0.08 0.09 0.13 0.21 0.53 1.12 1.05 1.00

u ¼ 150[�]

1/2 0.23 0.23 0.24 0.25 0.27 0.29 0.33 0.38 0.45 0.55 0.68 0.83 1.00

1 0.16 0.17 0.17 0.18 0.19 0.22 0.24 0.29 0.36 0.47 0.63 0.83 1.00


-----

96 / Basic Coastal Engineering

(Table 4.1. continued.)

b (Degrees)

r/L 0 15 30 45 60 75 90 105 120 135 150 165 180

2 0.12 0.12 0.12 0.13 0.14 0.15 0.18 0.22 0.28 0.39 0.59 0.86 1.00

5 0.07 0.07 0.08 0.08 0.08 0.10 0.11 0.13 0.18 0.29 0.55 0.99 1.00

10 0.05 0.05 0.05 0.06 0.06 0.07 0.08 0.10 0.13 0.22 0.54 1.10 1.00

u ¼ 165[�]

1/2 0.23 0.23 0.23 0.24 0.26 0.28 0.31 0.35 0.41 0.50 0.63 0.79 1.00

1 0.16 0.16 0.17 0.17 0.19 0.20 0.23 0.26 0.32 0.40 0.53 0.73 1.00

2 0.11 0.11 0.12 0.12 0.13 0.14 0.16 0.19 0.23 0.31 0.44 0.68 1.00

5 0.07 0.07 0.07 0.07 0.08 0.09 0.10 0.12 0.15 0.20 0.32 0.63 1.00

10 0.05 0.05 0.05 0.06 0.06 0.06 0.07 0.08 0.11 0.11 0.21 0.58 1.00

u ¼ 180[�]

1/2 0.20 0.25 0.23 0.24 0.25 0.28 0.31 0.34 0.40 0.49 0.61 0.78 1.00

1 0.10 0.17 0.16 0.18 0.18 0.23 0.22 0.25 0.31 0.38 0.50 0.70 1.00

2 0.02 0.09 0.12 0.12 0.13 0.18 0.16 0.18 0.22 0.29 0.40 0.60 1.00

5 0.02 0.06 0.07 0.07 0.07 0.08 0.10 0.12 0.14 0.18 0.27 0.46 1.00

10 0.01 0.05 0.05 0.06 0.06 0.07 0.07 0.08 0.10 0.13 0.20 0.36 1.00

From Wiegel, 1962.

this region. For a real barrier with a low reXection coeYcient it is not likely that
these values in excess of unity would occur.

Example 4.6-1

Consider a train of 6 s period waves approaching a breakwater so that the angle
of approach at the breakwater head (u) is 608. The water depth in the lee of the
breakwater is 10 m. Determine the wave height at an angle (b) of 308 from
the breakwater and a distance of 96.6 m from the breakwater head if the incident
wave height at the head is 2.2 m.

Solution:

For a wave period of 6 s and a water depth of 10 m we can calculate the wave
length in the lee of the breakwater [by trial using Eq. (2.14)], L ¼ 48:3 m.

From Table 4.1 for r=L ¼ 2:0, u ¼ 60[�], and b ¼ 30[�] we have Kd ¼ 0:28.
Thus, the wave height at the point of interest is 0.28(2.2) 0.62 m. At the point
¼

of interest the wave would be propagating in the direction of the 308 radial line.

Note from Table 4.1 that a spectrum of waves all coming from the same

direction will experience a greater percentage decrease in wave height at successively lower periods (i.e., higher values of r/L for the same point). Thus, the
energy density concentration in the wave spectrum will shift toward the higher


-----

Wave Refraction, Diffraction, and Reflection / 97

Wave

crest

Figure 4.10. DiVraction in the lee of a barrier of Wnite length. (U.S. Army Coastal

Engineering Research Center, 1984.)

wave periods in the spectrum. For a spectrum of waves having a range of periods
and directions one can evaluate on a component-by-component basis the modiWed characteristics for a diVracted wave spectrum at a particular point of
interest (e.g., see Goda, 1985).

When waves approach a barrier of Wnite length and wave diVraction occurs at

both ends, a wave crest pattern similar to that shown in Figure 4.10 will
develop. It can be constructed by combining the patterns for semi-inWnite
barrier diVraction at each end. The wave crests combine along lines like the
dashed line to form the higher amplitudes which may be estimated (assuming
linear waves) by combining the heights from the two separate patterns. Harms
(1979) has presented an analytical solution for the wave weight pattern in
the lee of the barrier and performed laboratory experiments to evaluate his
analysis.

Barrier Gap

Penny and Price (1952) also presented a solution for the diVraction of waves
passing through a gap in a barrier. These solutions were in agreement with the
results of wave tank studies conducted by Blue and Johnson (1949). Johnson
(1952) presented plots of diVraction coeYcient versus nondimensional horizontal
position similar to Figure 4.11 for normally incident waves penetrating barrier
gaps having a range of dimensions from one to Wve wave lengths.

Johnson (1952) demonstrated that these diVraction diagrams could also be

used if the angle of wave approach is other than 908 by using a projected
imaginary gap width as shown in Figure 4.12. When the gap width is about
Wve times the incident wave length or greater, the diVraction zones caused by


-----

98 / Basic Coastal Engineering

2 4 6
8 [0]

6

x
L [4]


y / L

2 4 6 8 10 12 14 16 18 20
8 [0]

6

0.2

x
L [4]

0.4

2

0
1.2 1.0 0.8 0.6

(mirror image)


Figure 4.11. Kd values for the lee of a barrier gap 2.5 wave lengths wide, with normally

incident waves. (Johnson, 1952.)

Gap width


Imaginary
gap width


Figure 4.12. Oblique wave incident to a barrier gap.

the barrier on each end of the gap are essentially independent. Then,
the diVraction analyses for the two separate semi-inWnite barriers may be
combined.


Johnson (1952), using analytical results from Carr and Stelzreide (1952), also

presented a series of diVraction diagrams for a range of incident wave directions
passing through a single gap width equal to one wave length. A compilation of
all of the barrier gap diVraction diagrams discussed above is presented by the
U.S. Army Coastal Engineering Research Center (1984). Often, the barrier
geometries encountered in practice will not be the same as the speciWc geometries
for which solutions are presented. However, approximate but useful results can
still be achieved by employing these solutions with some ingenuity to approximate the eVect of the actual barrier geometry. If the project is of suYcient


-----

Wave Refraction, Diffraction, and Reflection / 99

importance, these approximate results can also be coupled with limited physical
model tests to achieve better results.

Wave Action in Harbors

A major design concern for typical marinas or small craft harbors is to limit the
wave height in the interior of the harbor at the points were vessels are docked.
This limit would be established for a given design wave condition or conditions
having a speciWed probability of occurrence. A typical criteria for marinas where
recreational vessels and small working vessels are docked is to limit the wave
height to 0.3 m under ‘‘normal’’ conditions but to allow up to a 0.6 m wave
height during ‘‘extreme storm events’’ (Cox and Clark, 1992). Normal conditions
would be a wave event that is exceeded only once a year and extreme storm
events might be an event that is exceeded once in Wfty years. It is preferable that
the waves approach a moored vessel head on; for beam seas the allowable wave
heights might be reduced. For large vessels (e.g. tankers and bulk carriers) the
allowable wave heights would be signiWcantly higher.

Typically, the water depth in a marina or harbor is dredged to one or more

constant depths so that as a wave enters the harbor, diVraction dominates in
establishing the wave height variation throughout the harbor. The design wave or
waves will typically be speciWed (height and direction) in deep water oVshore of the
harbor. Shoaling and refraction analyses (e.g. see Figure 4.5) would determine the
height and direction of the incident wave at the tip of the breakwater that protects
the harbor. This might be a single breakwater as depicted in Figures 4.5 and 4.9 or
a pair of breakwaters having a gap as depicted in Figures 4.11 and 4.12.

The harbor designer can then adjust the length of the single breakwater or the

gap width between the breakwater pair to control the wave height at points of
interest within the harbor. A minimum gap width might be dictated by other
considerations such as the width of the channel required for vessels to navigate
through the harbor entrance. The possibility that wave energy can penetrate the
harbor by wave transmission through or over the breakwater must also be
considered. Also, the wave reXection characteristics of the harbor interior
boundaries (see Section 4.8) must be considered.

4.7 Combined Refraction and DiVraction

Whenever the wave height is not constant along a wave crest wave diVraction
will occur to diminish the wave height variation. For the example depicted in
Figure 4.5 a refraction/shoaling analysis from deep water to the breakwater
would be adequate for most design purposes. One should realize, however,
that in some areas such as where the orthogonals converge at the breakwater


-----

100 / Basic Coastal Engineering

dogleg the wave height may be lower than predicted because of the lateral spread
of energy caused by wave diVraction.

Immediately in the lee of the breakwater in Figure 4.5 wave diVraction would

dominate, owing to the cutting of the wave crest by the breakwater head and to the
fact that the bottom is relatively Xat in the lee of the breakwater. As the wave moves
further shoreward to where the bottom contours commence to change signiWcantly
(i.e., inside the –10 m contour)bothrefraction and diVractionmight besigniWcant.
The signiWcance of refraction would depend both on the bottom slope and on how
large of an angle is formed between the wave crests and the bottom contours. For
cases like this, the U.S. Army Coastal Engineering Research Center (1984) recommends carrying the diVraction processforward forthree or fourwave lengths in the
lee of the breakwater and then continuing with the wave refraction analysis as a
way to account for the combined eVects of refraction and diVraction. After threeor
four wave lengths the diVractive eVects are well established so the refraction of the
wave with this wave crest pattern and height distribution can now be carried
forward. The actual number of wave lengths for which the diVraction analysis
should proceed before the refraction analysis should take over would depend on
the actual bottom conditions as discussed above.

Mobarek (1962) conducted experiments in a wave basin that had a single

barrier oriented parallel to the wave generator and extending part of the way
across the basin. There was an opening from the barrier tip to the opposite
basin wall. In the lee of the barrier there was a 1:12 sloped bottom with straight
bottom contours situated normal to the barrier. For an incident wave with
d=L ¼ 0:14 at the barrier tip the experimental wave heights on the slope
generally agreed with the heights determined by the suggested procedure,
which was applied by constructing a diVraction diagram for one wave length
in the lee of the barrier and then conducting the refraction analysis to the point
of interest on the slope.

In practice, there may be some situations where an adequate analysis cannot

be conducted by the alternate application of diVraction and refraction analyses.
Such problems may be studied by a physical model. The cost and time requirements for a physical model study may make it of limited value, particularly for
small projects or projects with time constraints on completion of the design.
Also, there are some physical constraints on combined refraction-diVraction
model studies. If the model does not require a vertical to horizontal scale
distortion then both refraction and diVraction can be studied simultaneously.
But, space limitations, viscous and surface tension scale eVects, and diYculties in
adequately measuring wave heights in a small vertical scale model may require
that the model be distorted. Then, both refraction and diVraction cannot simultaneously be modeled if intermediate depth water waves are being studied (see
Chapter 9 and Sorensen, 1993).

Recently, numerical model analyses of wave propagation where refraction and

diVraction are both important have been developed using the mild slope equation


-----

Wave Refraction, Diffraction, and Reflection / 101

Wrst presented by BerkhoV (1972). These analyses are successful where refraction/
diVraction are not strong over a large lateral extent. For example, this approach
would be useful to give a better analysis of wave height variation seaward of the
breakwater in Figure 4.5 than the classic refraction/shoaling analysis alone. For
some examples see BerkhoV et al. (1982), Ebersole (1985), Houston (1981), Kirby
and Dalrymple (1983), Lozano and Liu (1980), and Tsay and Liu (1983).

4.8 Wave ReXection

ThereXection oftwo-dimensional waves,wherea reXectioncoeYcient Cr ¼ Hr=Hi
was deWned, was covered in Section 2.7. When waves in a three-dimensional domain obliquely approach a reXecting barrier a method is required to predict the
shape and orientation of the reXected wave crests. This, along with the reXection
coeYcient allows one to determine the wave height along the reXected wave crest.

Consider Figure 4.13, which shows an incident wave crest, which may be

curved as a result of previous diVraction, and is undergoing refraction as it
approaches a reXecting barrier. To construct the reXected wave crest pattern,
Wrst construct imaginary mirror image bottom contours in the lee of the reXecting barrier. Then extend the incident wave crest into this imaginary domain,
refracting and diVracting it as necessary. Then construct a mirror image of this
wave crest that was constructed in the imaginary domain. This will be the pattern
of the reXected wave crest. The wave height at any point along the reXected wave
crest will be the wave height at the equivalent point in the imaginary domain
times the reXection coeYcient of the barrier.

An example that further demonstrates this process is depicted in Figure 4.14,

where a straight crested wave passes a barrier, diVracts into the lee of that
barrier, and then reXects oV a second barrier. The water depth is constant so
the wave only undergoes diVraction and reXection. The imaginary diVracted
wave crest pattern is carried to point A[0] where the imaginary wave height can

Imaginary refracted

crest

Hi Image

bottom contours

CrHi Actual

bottom contours

Reflected Incident

crest crest

Figure 4.13. Wave reXection analysis.


Imaginary refracted

crest

Hi

CrHi

Reflected Incident

crest crest


-----

102 / Basic Coastal Engineering

Imaginary

diffracted

wave

A[9] A

r

β

Hi

Figure 4.14. Combined wave diVraction and reXection.

be determined from the incident height and direction along with the values of r
and b as previously discussed. The reXected wave height at point A would equal
the imaginary diVracted height at point A[0] times the reXection coeYcient. Remember, the wave crests are continually moving forward, the patterns depicted
in Figures 4.13 and 4.14 are only a ‘‘snapshot’’ in time showing one view of the
advancing wave crests. The total vertical displacement of the water surface at
any point would equal the sum of the displacements of the incident wave and
reXected wave at that point and instant of time.

As the waves continue to propagate forward they may be reXected again and

again to produce complex patterns, particularly inside of harbors where most of
the boundaries have relatively high reXection coeYcients. An analysis of the
reXection patterns and related reXected wave heights may indicate potential
‘‘trouble spots’’ in a harbor. Inspection of the pattern of reXected waves will
indicate possible desired changes in the harbor boundaries (e.g., lowering the
reXection coeYcient of a segment of the harbor boundary by changing it from a
vertical bulkhead to a sloping stone revetment). Ippen (1966) discusses this in
greater detail and presents suggestions for applying these concepts to the study
of wave reXection in harbors.

4.9 Vessel-Generated Waves

In restricted areas, owing to the relatively short expanse of water over which the
wind can generate waves, the waves generated by a moving vessel often are the
dominant waves for design.



**[9]** A

r

β

Hi


-----

Wave Refraction, Diffraction, and Reflection / 103

As a vessel moves across the water surface, the Xow of water back across the

vessel hull causes a varying pressure distribution over the hull surface. The
magnitudes of these dynamic pressures depend on the vessel speed, the water
depth (if suYciently shallow), the vessel hull geometry and draft, and the channel
cross-section shape if the channel is relatively narrow. For vessels moving in a
conWned channel the resulting pressure gradients will be greater than if the vessel
is moving across a wide and deep body of water.

For common vessel hull shapes, the pressure will rise in the vicinity of the vessel

bow, fall below the free stream pressure along the midsection of the hull, and rise
again at the vessel stern. The water surface proWle along the hull responds to this
pressure variation, rising at the bow and stern and falling along the midsection.
Owing to Xow separation that is common at the vessel stern, the pressure and
resulting water surface rise will be less there than at the bow. The inertia of the
rising and falling water causes the water to lag behind its equilibrium position and
to produce a surface oscillation which, in turn, produces the pattern of free waves
that propagate out from the vessel. The amplitude of the waves will depend on the
magnitude of the pressure variation (i.e. on the vessel speed, hull geometry and
draft, andthe water depth). Theperiod (length) and directionof propagationof the
waves depends only on the vessel speed and water depth.

For some lighter vessels moving at higher speeds, the hydrodynamic forces on

the hull will lift the vessel (planning) so it ‘‘skims’’ the water surface. When a
vessel planes, the generated wave heights are lower than they otherwise would be
and do not noticeably increase with increasing vessel speed. Sorensen (1973)

Diverging

wave

Cusp locus

line

Sailing line 19°289

θ

Transverse Cusp

wave

Figure 4.15. Deep water wave crest pattern generated by the bow of a moving vessel.


Diverging

wave

Cusp locus

line

Sailing line 19°289

θ

Transverse Cusp

wave


-----

104 / Basic Coastal Engineering

gives a more thorough review of the generation and resulting characteristics of
vessel generated waves.

Figure 4.15 shows the wave crest pattern generated by the bow of a vessel

moving across deep water. Only the crests in the vicinity of the vessel are shown.
The pattern of waves would extend back from the vessel with decreasing wave
amplitudes until the wave crests are no longer discernable.

The wave pattern consists of symmetrical pairs of diverging waves that move

obliquely out from the vessel sailing line and a single set of transverse waves that
move forward in the direction of the sailing line. The transverse and diverging
waves meet to form cusps which are located along lines that are 19828’ out from
the sailing line. The largest wave amplitudes are at the cusps. A similar wave
pattern, but usually with lower amplitudes would be generated at the stern. If the
vessel speed is increased, the wave lengths would accordingly increase, but the
overall pattern (including the 19828’ angle) would retain the same form.

Since the wave pattern remains steady relative to the vessel, the celerity C of all

of the waves in the pattern must be related to the vessel speed V by

C V cos Q
¼

Where Q is the angle between the sailing line and the direction of wave propagation
as depicted in Figure 4.15. For diverging waves in deep water the theoretical value
of Q is 358 16’. Consequently, the diverging wave crests form an angle of 548 44’
with the sailing line at the cusp point (i.e. 1808 � 908 � 35816[0] ¼ 54844[0]).

Owing to wave diVraction, successive transverse and diverging waves aft of the

vessel have increasing crest lengths and commensurate energy densities and wave
amplitudes. It can be shown (Havelock, 1908) that the diverging wave heights at
the cusp points should decrease at a rate that is inversely proportional to the
cube root of the distance from the sailing line. Transverse wave heights at the
sailing line decrease at a rate that is inversely proportional to the square root of
the distance from the vessel bow. Thus, at a greater distance from the vessel, the
diverging waves become relatively higher than the transverse waves.

Note that the diverging waves are propagating away from the sailing line;

however, the wave pattern does not change if the vessel maintains a constant
speed. This apparent anomaly is explained by considering the group celerity
(Section 2.5) for deep water waves. As a diverging wave propagates forward one
wave length (refer to Figure 4.15), half of its energy remains behind. The outer
portionofthedivergingwavereceivesnoenergyfromthewaveinfrontofit,butthe
inner portion of the wave does. Thus, as the diverging waves propagate forward,
they diminish at the outer end and grow at the inner end, allowing them to remain
stationary relative to the vessel. Also, by this process, the total wave system adds
one wave at the distant point for each wave length that the vessel advances.

The total drag on a moving vessel consists of the Xuid friction and form drag

owing to Xow past the hull, plus the vessel wave drag as it is energy from the


-----

Wave Refraction, Diffraction, and Reflection / 105

vessel that produces the vessel wave system. As a vessel’s speed is increased, wave
amplitudes and wave drag increase exponentially.

Also, as the vessel speed increases causing the generated wave lengths to

increase, the waves may become long enough to ‘‘feel’’ the bottom (d=L < 0:5).
This occurs when the Froude number F (where F ¼ V=(gd)[0][:][5]) exceed approximately 0.7. As the Froude number increases from 0.7 to 1.0, the transverse wave
heights increase faster than the diverging wave heights, becoming more prominent toward F ¼ 1. Concurrently, the cusp locus locus angle increases from 198 18’
to 908 at F ¼ 1. At F ¼ 1, with the cusp locus angle equal to 908, the diverging
and transverse waves have coalesced with their crests oriented perpendicular to
the sailing line. Also, most of the energy in the wave system is concentrated in the
Wrst wave at the bow.

For Froude numbers in excess of unity, since the greatest wave celerity can

only equal (gd)[0][:][5], no transverse waves can exist. Diverging waves extend back
from the vessel and form an angle equal to arcsin (F[�][1]) with the sailing line
(similar to the Mach angle in aerodynamics).

In addition to the vessel speed and the water depth, the generated wave heights

depend on the vessel bow geometry and draft. Consequently, most wave height
prediction schemes are semi-empirical. Sorensen (1989, 1997) summarizes Weld
and laboratory vessel-generated wave height measurements, as well as most of
the available wave height prediction schemes. For the range of vessel speeds
between 5 and 15 knots the maximum wave heights generated by a vessel (near
the vessel at the cusp point) typically range between 0.2 and 0.9 m. Common
wave periods range between 1 and 2.5s.

4.10 Summary

The basic material on surface waves covered to this point can generally be
applied to the full range of wave periods from the shorter wind generated
waves to long period waves such as the astronomical tide. But the applications
of this material that were presented have focused on the characteristics and
behavior of the wind wave portion of the wide spectrum of waves that occur at
sea. Next, we must turn our attention to the longer period Xuctuations of coastal
water levels, which includes wave phenomena such as the tide and seismically
generated tsunamis as well as phenomena such as storm surge which does not
primarily involve wave action.

4.11 References

Arthur, R.S., Munk, W.H., and Isaacs, J.D. (1952), ‘‘The Direct Construction of Wave

Rays,’’ Transactions, American Geophysical Union, Vol. 33, pp. 855–865.


-----

106 / Basic Coastal Engineering

BerkhoV, J.C.W. (1972), ‘‘Computation of Combined Refraction–DiVraction,’’ in Pro
ceedings, 13th International Conference on Coastal Engineering, American Society of
Civil Engineers, Vancouver, pp. 471–490.

BerkhoV, J.C.W., Booij, N., and Radder, A.C. (1982), ‘‘VeriWcation of Numerical Wave

Propagation Models for Simple Harmonic Linear Water Waves,’’ Coastal Engineering,
Vol. 6, pp. 255–279.

Blue, F.L. and Johnson, J.W. (1949), ‘‘DiVraction of Water Waves Passing

Through a Breakwater Gap,’’ Transactions, American Geophysical Union, Vol. 33,
pp. 705–718.

Carr, J.H. and Stelzreide, M.E. (1952), ‘‘DiVraction of Water Waves by Breakwaters,’’

Gravity Waves, Circular 521, National Bureau of Standards, Washington, DC,
pp. 109–125.

Cialone, M.A. and Kraus, N.C. (1987), ‘‘A Numerical Model for Shoaling and Refraction

of Third-Order Stokes Waves Over an Irregular Bottom,’’ Miscellaneous Paper CERC
87–10, U.S. Army Waterways Experiment Station, Vicksburg, MS.

Crowley, J.B., Fleming, C.A., and Cooper, C.K. (1982), ‘‘Computer Model for the Refrac
tion of Nonlinear Waves,’’ in Proceedings, 18th International Conference on Coastal
Engineering, American Society of Civil Engineers, Cape Town, pp. 384–403.

Cox, J.C. and Clark, G.R. (1992), ‘‘Design Development of a Tandem Breakwater System

for Hammond Indiana,’’ in Proceedings, Coastal Structures and Breakwaters Conference, Thomas Telford, London, pp. 111–121.

Dean, R.G. and Dalrymple, R.A. (1984), Water Wave Mechanics for Engineers and

Scientists, Prentice-Hall, Englewood CliVs, NJ.

Ebersole, B.A. (1985), ‘‘Refraction–DiVraction Model for Linear Water Waves,’’ Journal,

Waterway, Port, Coastal and Ocean Engineering Division, American Society of Civil
Engineers, November, pp. 939–953.

Goda, Y. (1985), Random Seas and the Design of Maritime Structures, University of

Tokyo Press, Tokyo.

Griswold, G.M. (1963), ‘‘Numerical Calculation of Wave Refraction,’’ Journal of Geo
physical Research, Vol. 68, pp. 1715–1723.

Hardy, T.A. and Krauss, N.C. (1987), ‘‘A Numerical Model for Shoaling and Refraction

of Second Order Cnoidal Waves Over an Irregular Bottom,’’ Miscellaneous Paper
CERC 87–9, U.S. Army Waterways Experiment Station, Vicksburg, MS.

Harms, V.W. (1979), ‘‘DiVraction of Water Waves by Isolated Structures,’’ Journal,

Waterway, Port, Coastal and Ocean Engineering Division, American Society of Civil
Engineers, May, pp. 131–147.

Havelock, T.H. (1908), ‘‘The Propagation of Groups of Waves in Dispersive Media, with

Application to Waves on Water Produced by a Travelling Disturbance,’’ Proceedings
Royal Society of London Series A, pp. 398–430.

Headland, J.R. and Chiu, H.-L. (1984), ‘‘A Numerical Model for Refraction of Linear and

Cnoidal Waves,’’ in Proceedings, 19th International Conference on Coastal Engineering,
American Society of Civil Engineers, Houston, pp. 1118–1131.


-----

Wave Refraction, Diffraction, and Reflection / 107

Houston, J.R. (1981), ‘‘Combined Refraction and DiVraction of Short Waves Using the

Finite Element Method,’’ Applied Ocean Research, Vol. 3, pp. 163–170.

Ippen, A.T. (1966), Estuary and Coastline Hydrodynamics, McGraw-Hill, New York.

Jen, Y. (1969), ‘‘Wave Refraction Near San Pedro Bay, California,’’ Journal, Waterways

and Harbors Division, American Society of Civil Engineers, August, pp. 379–393.

Johnson, J.W. (1947), ‘‘The Refraction of Surface Waves by Currents,’’ Transactions,

American Geophysical Union, Vol. 28, pp. 867–874.

Johnson, J.W. (1952), ‘‘Generalized Wave DiVraction Diagrams,’’ in Proceedings, 2nd

Conference on Coastal Engineering, Council on Wave Research, Berkeley, pp. 6–23.

Johnson, J.W., O’Brien, M.P., and Isaacs, J.D. (1948), ‘‘Graphical Construction of Wave

Refraction Diagrams,’’ Navy Hydrographic OYce Publication Number 605, Washington, DC.

Keulegan, G.H. and Harrison, J. (1970), ‘‘Tsunami Refraction Diagrams by Digital

Computer,’’ Journal, Waterways and Harbors Division, American Society of Civil Engineers, May, pp. 219–233.

Kirby, J.T. and Dalrymple, R.A. (1983), ‘‘A Parabolic Equation for the Combined

Refraction–DiVraction of Stokes Waves by Mildly Varying Topography,’’ Journal of
Fluid Mechanics Vol. 136, pp. 453–466.

Lozano, C.J. and Liu, P.L.-F. (1980), ‘‘Refraction–DiVraction Model for Linear Surface

Water Waves,’’ Journal of Fluid Mechanics, Vol. 101, pp. 705–720.

Mobarek, I. (1962), ‘‘EVect of Bottom Slope on Wave DiVraction,’’ Report HEL 1-1,

Hydraulic Engineering Laboratory, University of California, Berkeley.

Munk, W.H. and Arthur, R.S. (1951), ‘‘Wave Intensity Along a Refracted Ray,’’ Gravity

Waves, Circular 521, National Bureau of Standards, Washington, DC, pp. 95–108.

Noda, E.K., Sonu, C.J., Rupert, V.C., and Collins, J.I. (1974), ‘‘Nearshore Circulation

Under Sea Breeze Conditions and Wave Current Interaction in the Surf Zone,’’ Tetra
Tech Report P-72–149–4, Pasadena, CA.

Oh, I.S. and Grosch, C.E. (1985), ‘‘Numerical Study of Finite Amplitude Wave Refrac
tion,’’ Journal, Waterway, Port, Coastal and Ocean Engineering Division, American
Society of Civil Engineers, January, pp. 78–95.

Penny, W.G. and A.T. Price (1952), ‘‘The DiVraction Theory of Sea Waves by Breakwa
ters and the Shelter AVorded by Breakwaters,’’ Phylosophical Transactions, Royal
Society, Series A, Vol. 244, London, pp. 236–253.

Perigrine, D.H. (1976), ‘‘Interaction of Water Waves and Currents,’’ Advances in Applied

Mathematics, Vol. 16, Academic, New York, pp. 9–117.

Perlin, M. and Dean, R.G. (1983), ‘‘An EYcient Algorithm for Wave Refraction/Shoaling

Problems,’’ in Proceedings, Coastal Structures ’83 Conference, American Society of
Civil Engineers, Arlington, VA, pp. 988–999.

Putnam, J.A. and Arthur, R.S. (1948), ‘‘DiVraction of Water Waves by Breakwaters,’’

Transactions, American Geophysical Union, Vol. 29, pp. 481–490.

Sorensen, R.M. (1973), ‘‘Ship-Generated Waves,’’ Advances in Hydroscience Academic

Press, New York, Vol.9, pp. 49–83.


-----

108 / Basic Coastal Engineering

Sorensen, R.M. (1993), Basic Wave Mechanics for Coastal and Ocean Engineers, John

Wiley, New York.

Sorensen, R.M. (1989), ‘‘Port and Channel Bank Protection from Ship Waves,’’ Proceed
ings, Ports ’89 Conference, American Society of Civil Engineers, Boston, pp. 393–401.

Sorensen, R.M. (1997), ‘‘Prediction of Vessel-Generated Waves with Reference to Vessels

Common to the Upper Mississippi River System,’’ ENV Report 4, U.S. Army Corps of
Engineers, Upper Mississippi River-Illinois Waterway System Navigation Study, Rock
Island, Illinois.

Tsay, T.-K. and Liu, P.L.-F. (1983), ‘‘A Finite Element Model for Refraction and

DiVraction,’’ Applied Ocean Research, Vol. 5, pp. 30–37.

U.S. Army Coastal Engineering Research Center (1984), Shore Protection Manual, U.S.

Government Printing OYce, Washington, DC.

Wiegel, R.L. (1962), ‘‘DiVraction of Waves by Semi-inWnite Breakwater,’’ Journal, Hy
draulics Division, American Society of Civil Engineers, January, pp. 27–44.

Wiegel, R.L. (1964), Oceanographical Engineering, Prentice-Hall, Englewood CliVs, NJ.

Wiegel, R.L. and Arnold, A.L. (1957), ‘‘Model Study of Wave Refraction,’’ Technical

Memorandum 103, U.S. Army Corps of Engineers Beach Erosion Board, Washington,
DC.

Wilson, W.S. (1966), ‘‘A Method for Calculating and Plotting Surface Wave Rays,’’

Technical Memorandum 17, U.S. Army Coastal Engineering Research Center,
Washington, DC.

4.12 Problems

1. A wave train is observed approaching a coast that has straight parallel

nearshore bottom contours that are oriented in a north–south direction. Where
the water depth is 5 m the wave crests are observed to form an angle of 98
with the shoreline (waves from the southwest) and the wave period is measured
to be 7.3 s. What is the incident wave direction in deep water? If the measured
wave height at the 5 m depth is 2.2 m, what is the deep water wave height?

2. A wave train approaches the same shore location as in Problem 1 but the

deep water wave crests form an angle with the shoreline of 508. If the wave period
is 11 s and the deep water height is 2 m what is the wave height and angle
between the wave crest and shoreline where the water depth is 8 m? At what
depth will the wave break?

3. A wave train has a period of 8.6 s and propagates toward the shore over

straight shore-parallel bottom contours. Plot the wave crest angle (with respect
to the shoreline orientation) in deep water versus the wave crest angle at a water
depth of 5 m for deep water angles ranging from zero to 808. How would this
curve diVer if the incident wave period were 6 s?


-----

Wave Refraction, Diffraction, and Reflection / 109

4. The wave refracted in Figure 4.5 has a deep water height of 2.1 m. Deter
mine its height at the breakwater dogleg and at the head of the breakwater.

5. A train of waves having a 1 s period and a height of 5 cm is generated in a

wave basin having the dimensions and water depths shown. The side walls of the
basin have a reXection coeYcient of zero and the step has a reXection coeYcient
of zero and the step has a reXection coeYcient of 0.2 (assume no energy
dissipated at the step). Construct the refraction diagram, indicate regions
where wave diVraction eVects would be signiWcant, sketch the wave crest pattern
in the diVraction region, and calculate the wave height at point A.

_45˚_

_d = 15 cm_

Wave

generator

_d = 25 cm_ _B_ 2 m 9 m

_A_

_45˚_ 1 m

3 m 3 m 6 m

6. Draw 10 parallel lines 3 cm apart and assign depths of 105, 85, 70, 58, 48,

38, 28, 18, 10, and 5 m. Construct a pair of orthogonals for a 11.5 s wave
approaching the contours at a 458 angle and determine the refraction coeYcient
at the 5 m depth. Calculate the refraction coeYcient using Eqs. (4.2) and (4.3)
and compare the result from that for the refraction diagram analysis.

7. Given the hydrography in Problem 6 construct a pair of orthogonals for a

10 s period wave train approaching with deep water wave crests forming a 408
angle with the bottom contours. If the wave has a height of 6 m in deep water,
determine the wave height, water depth, and angle between the wave crest and
bottom contours just prior to breaking.

8. The Gulf Stream Xows generally to the northeast oVshore of the eastern

seaboard of the United States. At a point where this current is Xowing directly to
the northeast at 1.8 m/s, it is approached by waves from the east having a period
of 8 s and a height of 2.1 m. Assuming the ocean east of the Gulf stream has a


_45˚_

_d = 15 cm_

Wave

generator

_d = 25 cm_ _B_ 2 m

_A_

_45˚_ 1 m

3 m 3 m 6 m


-----

110 / Basic Coastal Engineering

negligible current, what is the eVect on the celerity, height, and direction of the
approaching waves as they enter the Gulf Stream?

9. An ocean current Xows directly to the east. Describe the eVect of this

current on a train of waves approaching from still water and a northeast
direction. From still water and a northwest direction? Be speciWc.

10. Considering the eVects of wave diVraction, what is the wave height at

point B along the centerline in Problem 5?

11. Consider the L-shaped breakwater that protects a small harbor dredged

to a uniform depth of 6 m. For a 2 m high, 10 s period incident wave at the
head of the breakwater having the direction shown, what length x must the
seaward arm of the breakwater have to diminish the wave height to 0.5 m at
point A?

200m

× _A_

250m

200m

−6m

depth

60˚

x

Incident

wave direction

12. With x 300 m in Problem 11 and the same incident wave direction, what
¼

are the values of Kd at point A for a 2, 4, 6, 8 and 10 s wave? From this, discuss
the eVect of wave diVraction on a spectrum of waves all arriving from the same
direction and diVracting to the lee of a breakwater.

13. A 7 s, 2.5 m high deep water wave approaches the shore in a normal

direction. At a distance of 300 m from the shore a 700 m long breakwater is
constructed parallel to the shore and the area leeward of the breakwater is dredged
to a depth of 5 m, which is the natural depth at the breakwater. What is the
maximumwaveheightthatwilloccuratthecenterofthebreakwaterontheleeward
side?

14. If the deep water incident wave direction in Problem 13 is 308 oV a line

normal to the breakwater axis and the nearshore bottom contours are all straight
and parallel to the shore, what is the maximum wave height at the center of the


200m

× _A_

250m

200m

−6m

depth

60˚

x

Incident

wave direction


-----

Wave Refraction, Diffraction, and Reflection / 111

breakwater on the leeward side? Draw the wave crest pattern in the vicinity of
the breakwater. Assume the breakwater has a reXection coeYcient of zero.

15. In Problem 11, for the same incident wave height, period, and direction

and a breakwater length of x 400 m, what is the wave height at point A if the
¼
water depth in the lee of the breakwater decreases linearly from 6 m at the
�
oVshore arm to 2 m at point A?
�

16. In Problem 11, for the same incident wave height, period, and direction

and a breakwater length of x 300 m draw the diVracted and reXected wave
¼
crest pattern in the harbor. Assume that the shoreline is a bulkhead with a
reXection coeYcient of 0.8 and that the interior sides of the breakwater are
stone mound with a reXection coeYcient that is essentially zero. What will the
reXected wave height be at point A?

17. Consider the situation depicted in Figure 4.14 and assume the water depth

throughout is 5 m. If the incident wave height and period are 2.2 m and 4 s,
respectively, what is the reXected wave height at point A which is 20 m from each
of the barriers? The barrier that reXects the wave has a Cr ¼ 0:75.

18. The oVshore arm of the breakwater in Problem 11 has a reXection coeY
cient of 0.65 on the seaward side. Consider the incident wave period, height, and
incident direction given in Problem 11 and assume that the water depth immediately seaward of the breakwater is also 6 m. What is the reXected wave height
at a point 100 m from the head of the breakwater along a line that extends out
from the axis of the oVshore arm? Show the reXected wave crest pattern out to
this point.

19. A vessel is traveling at 10 knots over deep water. Determine the transverse

and diverging wave lengths and periods. How deep must the water be to be deep
water?


-----

## 5

### Coastal Water Level Fluctuations

This chapter is concerned with coastal water level Xuctuations caused

by waves having longer periods than those generated directly by the wind, and
other nonwave Xuctuations in coastal water levels. In particular, these may be
classiWed as:

1. Astronomical tide—periodic Xuctuations caused by the interaction of

gravitational and centrifugal forces primarily between the earth, sun, and
moon

2. Tsunamis—surface waves generated by underwater disturbances primarily

of seismic origin

3. Basin oscillations—resonant response of water bodies to long period wave

and nonwave excitations

4. Storm surge—setup and setdown of coastal water levels caused by me
teorological forces

5. Climatological/geological eVects—long-term changes in relative sea level

owing to atmospheric warming coupled with coastal uplift or subsidence.

Figure 5.1 is a schematic depiction of a common type of gage that can be used

to measure the coastal water level Xuctuations that are discussed in this chapter.
Water surface Xuctuations cause the water level and Xoat inside the stilling well
to rise and fall. The stilling well water level is recorded on a chart to provide a
time-history of the coastal water level Xuctuations. The small oriWce in the
stilling well is designed to Wlter out oscillations having periods typically smaller
than a minute or so. This is accomplished through frictional dissipation at the
oriWce and by the large ratio of stilling well cross-sectional area to oriWce area.
Gages of this type and other types of gages that make similar measurements are
located at numerous places around the coastline and in bays and estuaries. They
provide an excellent long-term record of the coastal water level conditions at a
site as well as general insight as to the nature of shorter term Xuctuations. Also,


-----

114 / Basic Coastal Engineering

Rotating chart


Time-history of local


on drum Sea level

Pulley

Moving

Float
pen

Sea level

Short period

wave
Stilling

well

Orifice

o


Figure 5.1. Float-stilling well water level gage.

our predictive procedures for most coastal water level Xuctuations require calibration data provided by these gages.

Figure 5.2 is a plot that schematically shows the spectrum of wave energy

typically found on the ocean and large bays and lakes. The actual energy level
any spectral component has will vary with location and time. Also indicated on
the Wgure are the primary generating forces for the various components of the
spectrum. The portion of the spectrum from about 1 to 30 s covers the windgenerated waves one typically sees when visiting the coast. Surf beat consists of
oscillations in the surf zone caused by wind wave induced setup and setdown (see
Section 2.6) as groups of higher and lower waves reach the coast. Tsunami waves
can have periods from 5 to 60 min while the dominant tidal periods are around
12 and 24 hours. Basin oscillations commonly occur in response to the portion of
the spectrum from surf beat up to the astronomical tide, the speciWc periods
responded to depending on the geometry of the basin and the periods of the
spectrum that are active at the basin location.

5.1 Long Wave Equations

The waves considered in this chapter have relatively long periods and thus tend to
have low d/L values so that they usually are shallow water waves even in the deeper
ocean. Employing the small-amplitude wave theory, the wave celerity would be


-----

Coastal Water Level Fluctuations / 115

Wind Storm systems Moon

Seismic activity Sun

Wind waves

Tides

Surf

Capillary

beat Tsunamis

waves

30 sec 5 min 50 min 12 24 hrs

0.1 1.0 10 10[2] 10[3] 10[4] 10[5]


Wind Storm systems Moon

Seismic activity Sun

Wind waves

Tides

Surf

Capillary

beat Tsunamis

waves

30 sec 5 min 50 min 12 24 hrs


WAVE PERIOD, sec

Figure 5.2. Typical ocean wave energy spectrum.


givenby Eq.(2.19), theparticle velocities byEqs. (2.30)and (2.31),and thepressure
distribution by Eq. (2.34). As an alternative, we can start with the known physical
characteristics of shallow water waves and directly develop the relevant form of the
equations of continuity and motion. These equations are commonly known as the
long wave equations. Owing to the typical applications of the long wave equations
for the phenomena discussed in this chapter, these equations will be presented in
three-dimensional cartesian form (x, y horizontal coordinates; z vertical coordinate) and the equations of motion will include the eVects of surface and bottom
stress as well as Coriolis acceleration. For a more thorough discussion of the long
wave equations see Dean and Dalrymple (1984) and Sorensen (1993).

In the long wave equations, vertical Xow velocities are assumed negligible.


Horizontal Xows are considered in terms of the average velocity over the vertical
water column. This is done in terms of the volumetric Xow rate per unit width of
vertical section qx and qy for the two coordinate directions. Thus


ðh

�d


ðh

�d


and


qx ¼

qy ¼


u dz

v dz


where d is the bottom depth below the still water level and h is the water surface
elevation above the still water level. Considering a mass balance where the net


-----

116 / Basic Coastal Engineering

sum of the horizontal Xow rates into and out of a control volume equals the net
change in volume per unit time of the control volume represented by a rise or fall
of the water surface leads to the equation of continuity which can be written:

@qx (5:1)

@x [þ][ @]@[q]y[y] [þ][ @]@[h]t [¼][ 0]


To present the equations of motion for the two horizontal directions we must
introduce the bottom stresses in the x and y directions (tbx and tby) and the
surface stresses in the x and y directions (tsx and tsy). These might typically
represent bottom friction and the surface stress due to wind shear on the water.
Also we must introduce the Coriolis parameter f where

f ¼ 2v sin f (5:2)

In Eq. (5.2) v is the earth’s rotational speed (7:27 � 10[�][5]rad=s) and f is the
latitude of the point on the earth’s surface where the equations are being applied.
This parameter would be zero at the equator and maximum at the poles. The
product of f times a horizontal component of the Xow velocity yields the
horizontal Coriolis force per unit mass or acceleration which acts at right angles
to that Xow velocity component (to the right in the Northern hemisphere and to
the left in the Southern hemisphere). The Coriolis acceleration is relatively small,
but can be important in some long wave analyses where large masses of water are
involved.

Integrating the equations of motion from the bottom to the water surface

yields a common form for the horizontal components of the equations of motion


�g(d þ h) [@][h]

@x [þ][ fq][y][ þ][ 1]r [(][t][sx][ �] [t][bx][)][ ¼][ @]@x

�g(d þ h) [@][h]

@y [þ][ fq][x][ þ][ 1]r [(][t][sy][ �] [t][by][)][ ¼][ @]@x


� q[2]x �

d h
þ

� qxqy �

d h
þ


þ [@]

@y

þ [@]

@y


� qxqy �

d h
þ


d h
þ


þ [@][q][x] (5:3a)

@t

þ [@][q][x] (5:3b)

@t


q[2]y


!


where r is the density of the water. In Eqs. (5.3) the Wrst term on the lefthand side
represents the gravitational force per unit mass exerted through the slope of the
water surface in that component direction; the second term is the Coriolis
acceleration component; and the last term on the left represents the net horizontal stress per unit mass in that component direction. The three terms on the right
represent the resulting convective and local acceleration components for the
water. As will be seen, in some physical situations certain terms in Eqs. (5.3)
are negligible and may be excluded. Also, if the water surface Xuctuations are
small compared to the depth, the total water depth can be represented by d. The
eVects of a pressure gradient acting across the water surface are not included in


-----

Coastal Water Level Fluctuations / 117

the force summation on the lefthand side. If this force is signiWcant in practical
problems its eVect is usually evaluated separately.

5.2 Astronomical Tide Generation and Characteristics

A coastal engineer’s ability to predict the astronomical tide at a given location is
important for a number of practical reasons. Nearshore coastal hydrographic
work from a Xoating vessel may be referenced to the instantaneous tide level.
Planning for Weld work may be keyed to the need to work at high or low tide or
related periods of ebb or Xood current at an estuary. The range of tides indicates
the range of water levels at which waves and currents will act on coastal works.
At places where the tide range is large, the importance of an impending storm
may be very dependent on whether it arrives at high or low tide. In addition,
analysis of the reversing currents and related stability of a coastal inlet is
primarily dependent on the tide characteristics at the entrance to that inlet.
Astronomical tide theory is presented in great detail in specialized texts such as
Macmillan (1966), Harris (1981), and Pugh (1987). This section concentrates on
those aspects of the tide that are of particular interest to coastal engineers.

The gravitational attraction of the sun and moon on the oceans and the equal

and opposite centrifugal forces owing to the rotation of the earth–sun–moon
system are the primary tide generating forces. Although the sun’s mass is approximately 2:7 � 10[7] times that of the moon, the closer proximity of the moon to the
earth results in the moon having about twice the sun’s gravitational force on the
oceans. The resulting tide is a long period wave generated by these gravitational
and centrifugal forces. Consequently, even in the deepest areas of the ocean the
tide is a shallow water wave. As the tide wave propagates onto the continental
shelf and into bays and estuaries it is signiWcantly aVected by nearshore hydrography, bottom friction, Coriolis acceleration, and resonant eVects.

The range of the tide and the arrival time of high or low tide at a given location

are dependent on the above mentioned factors. Converging or diverging estuary
shorelines cause the amplitude of the tide to increase or decrease respectively
owing to the concentration or spreading of the tide wave’s energy. Decreasing
water depths as a tide wave propagates up an estuary will increase the tidal
range. Bottom friction, which dissipates wave energy, will cause the tide range to
decrease at successive points along an estuary.

The tide is a wave that has a very low steepness and thus relatively high reXec
tivity. At some locations such as the Bay of Fundy, Nova Scotia, reXection causes
resonance andresulting ampliWcationof the tidalrange inthe bay.ReXectionof the
tide wave also increases the complexity of the tide in some coastal regions.

In the Northern hemisphere, Coriolis acceleration will deXect Xowing water

to the right as one looks in the direction of the Xow (left in the Southern
hemisphere). Thus, as the tide propagates up an estuary causing Xow into the


-----

118 / Basic Coastal Engineering

estuary, the water level will be relatively higher on the righthand side. On the ebb
tide, this will cause a relatively higher water level on the other side of the estuary.

Further insight into the nature of the tide can be gained from an elementary

description of the way the tide is generated. Consider an idealized earth–moon
system with the earth covered by a uniform layer of water and the two bodies
revolving around a common axis that is about 2900 miles from the earth’s axis
(Figure 5.3). The gravitational forces Fg and the centrifugal forces Fc are in
balance at the center of mass of each body. But an element of water located on
the side of the earth farthest from the moon would have Fc > Fg and a resulting
net outward force. On the half of the earth closest to the moon Fg > Fc, which
also causes a net outward force. The result is two bulges as shown or two high
and two low tides each day as the earth rotates. These bulges are the tide waves
that propagate as shallow water waves.

While the earth rotates once (relative to the position of the sun), the moon

makes 1/29.5th of a revolution (a lunar month is 29.5 solar days). Thus, the
principal lunar tidal period M2 ¼ 12:0(1 þ 1=29:5) ¼ 12:42 hours. The principal
solar tidal period S2 ¼ 12:0 hours. Since the lunar force dominates, high and low
tides progress 0.84 hours (about 50 min) each day.

The planes of the moon’s and sun’s rotation relative to the earth are not in line

and change with regard to each other as time passes. Also, the orbits of the sun
and moon are elliptical rather than circular. These plus other factors make the


N


Common axis
of revolution


of revolution

∆

2900

mi

E M

water

ω

S

_Fc > Fg_ _Fg > Fc_


Figure 5.3. Tide generation—idealized earth/moon system.


-----

Coastal Water Level Fluctuations / 119

S

29.5 days

Spring

Spring

E

E

Neap 29.5 days

Neap

E E

E

Spring

Figure 5.4. Earth, sun, and moon during a lunar month.

net tide generating force very complex. Figure 5.4 shows the approximate
orientation of the sun, moon, and earth at the quarter points of the moon’s
revolution around the earth relative to the position of the sun (29.5 days). At the
Wrst position (new moon) and third position (full moon) the solar and lunar tide
generating forces reinforce and the highest or spring tides occur. At the second
and fourth quarters the lowest or neap tides occur. Each quarter is 29:5=4 ¼ 7:4
days long, so that spring and neap tides are 14.8 days or about 2 weeks apart.
The result of these two principal forces is a water level variation that is similar to
the beating eVect shown in Figure 2.6, where the lunar component would have a
slightly longer period and a greater amplitude than the solar component.

The principal lunar and solar components are just two of over 390 active tidal

components having periods ranging from about 8 hours to 18.6 years. Each
component has a period that has been determined from astronomical analysis
and a phase angle and amplitude that depend on local conditions and are best
determined empirically. Most of the 390 components are quite small and can be
neglected for practical tide prediction. Eight major components with their common symbol, period, approximate relative strength (depending on location), and
description are listed in Table 5.1. The components combine in diVerent ways at
each coastal location and are aVected by local hydrography, bottom friction,
resonance and so on, to produce the local tide.


-----

120 / Basic Coastal Engineering

Table 5.1. Eight Major Tidal Components

Period Relative

Symbol (hours) Strength Description

M2 12.42 100.0 Main lunar semidiurnal component

S2 12.00 46.6 Main solar semidiurnal component

N2 12.66 19.1 Lunar component due to monthly variation in

moons distance from earth

K2 11.97 12.7 Soli-lunar component due to changes in declination

of sun and moon throughout their orbital cycles

K1 23.93 58.4 With O1 and P1 accounts for lunar and solar

diurnal inequalities

O1 25.82 41.5 Main lunar diurnal component

P1 24.07 19.3 Main solar diurnal component

Mf 327.86 17.2 Lunar biweekly component

The tidal record at any location can generally be classiWed as one of three

types: semidiurnal, diurnal, or mixed. They are deWned as follows:

Semidiurnal: There are two high and two low water levels each tidal day (24.84
hours) with approximately the same vertical variation for each of the two cycles.
This is the predominate tidal type throughout the world, including the east coast
of North America.

Diurnal: There is only one high and one low water level each tidal day. Diurnal
tides predominate on the Gulf coast of the United States, but some Gulf coastal
sections have mixed tides.

Mixed: There is a large inequality in the vertical range of the two daily cycles.
Typically there is a cyclic transition from mixed to semidiurnal and back, or
from mixed to diurnal and back, the former being typical of the tides on the west
coast of North America.

Semidiurnal tides occur at a site where the semidiurnal components M2 þ S2

are stronger than the diurnal components K1 þ O1. The reverse occurs where
tides are diurnal. The diVerences are not that great where tides are mixed.

5.3 Tidal Datums and Tide Prediction

Water and land elevations in the coastal zone are referenced to a variety of tidal
datums in diVerent regions of the world and for diVerent purposes. Some of these
datums are:


-----

Coastal Water Level Fluctuations / 121

Mean sea level (MSL): The average height of all tide elevations (usually on an
hourly basis) averaged over a 19-year period

National geodetic vertical datum (NGVD): Mean sea level determined from 19
years of data averaged over 26 North American coastal stations in 1929

Mean low water (MLW): The 19-year arithmetic mean of all low water levels
(i.e., low points in tidal elevation cycle). MHW is the average of the high tide
levels.

Mean lower low water (MLLW): The 19-year arithmetic mean of only the lower
of each pair of low water levels in a mixed tide. MHHW is the average of the
higher high tide levels.

Mean tide level (MTL): the level located midway between MLW and MHW.

Sea level is observed to be generally higher on the PaciWc coast than on the

Atlantic coast and higher in the north than in the south on both coasts. Also,
with the passage of time, sea level rise as well as uplift or subsidence of coastal
lands causes the true MSL to vary from location to location and as time passes.
Thus, NGVD was established as a ‘‘Wxed’’ mean sea level reference. The
contemporary MSL at any given location will likely diVer from NGVD. In
1988 NGVD was reWned further to include gravimetric and other anomalies to
produce the North American Vertical Datum (NAVD 88). MLW and MLLW
are established as datums largely for navigation and related purposes so that
depths referenced to these datums are minimums likely to be available throughout the tide cycle. Land elevations are usually referenced to NGVD while depths
on coastal hydrographic charts may be referenced to MLW or MLLW so care
must be exercised when combining topographic and hydrographic data. The
vertical distance between NGVD and say MLLW will vary with location and
time.

The mean tide ranges for a number of coastal locations in North America are

listed in Table 5.2. The mean tide range is the diVerence between MLW and
MHW for semidiurnal and diurnal tides and between MLLW and MHHW for
mixed tides.

Note the wide range of values and the relatively steady progression in values as

one moves along the coast. Two sets of values are of particular interest. Grand
Manan Island is an island at the entrance to the Bay of Fundy and Burncote
Head is located back at the head of the Bay. The relatively large range at the bay
entrance is signiWcantly ampliWed back in the bay owing to resonance. The
resonant period of the Bay of Fundy is around the dominant tidal period of 12
hours. Cape May is located at the entrance to the Delaware River while Trenton
is over 150 river miles up the river. The larger tide range at Trenton than at Cape
May indicates the signiWcant eVects of shoaling and shoreline convergence on
increasing the amplitude of the tide wave as it propagates up the river. Also note


-----

122 / Basic Coastal Engineering

Table 5.2. Selected Coastal Mean Tide Ranges

Location Mean Tide Range (m)

Grand Manan Island, New Brunswick 5.24

Burntcoat Head, Nova Scotia 11.70

Boston, MA 2.90

Provincetown, MA 2.77

Sandy Hook, NJ 1.42

Cape May, NJ 1.46

Trenton, NJ 2.46

Ocean City, MD 1.07

Duck, NC 1.00

Folly Island, SC 1.58

Savannah River Entrance, GA 2.10

Cape Canaveral, FL 1.07

Key West, FL 0.40

Pensacola, FL 0.40

Mobile, AL 0.46

Galveston, TX 0.43

La Jolla, CA 1.13

San Francisco, CA 1.25

Crescent City, CA 1.55

Columbia River Entrance, OR 1.71

Juneau, AK 4.18

Anchorage, AK 7.89

Honolulu, HI 0.40

the small tide range at Honolulu which is typical of mid-ocean ranges. This is so
because there is not a signiWcant shallow coastal section to increase the tide wave
height before it reaches the shore.

A long record, on a continuous or at least hourly basis, of the water level at a

given coastal location is required to make future predictions of the tide. Measurements of water level by a device similar to that shown in Figure 5.1 will
include short-term wind and atmospheric pressure-induced water level changes,
but if the record to be analyzed is of suYcient length these eVects can be Wltered
out. For that reason and considering the range of tidal component periods, the
ideal record length would be about 19 years. However, records as short as 370
days can be satisfactory for tide prediction.

The instantaneous tidal elevation h above a selected datum can be given by


h A
¼ þ


N
X

i¼1


� �

Ai cos [2][p][t] þ Di

Ti


(5:4)


-----

Coastal Water Level Fluctuations / 123

where A is the vertical distance from the selected datum to MSL; Ai, Ti, and Di
are the amplitude, period, and phase angle of the particular component
(e.g., M2, K1); t is the time elapsed; and N is the number of tidal components
being used. Although the eight components listed in Table 5.1 are suYcient to
analyze the tide at most locations, the U.S. National Ocean Service considers
the 37 most important components in performing this analysis. The measured
tide record at a given site is then analyzed by performing an harmonic analysis
to determine Ai and Di for each component of period Ti. Once the values of Ai
and Di for each component are determined for a given site, Eq. (5.4) can be used
to predict future tide elevations at that location. Any changes to the coastal
area that would aVect propagation of the tide wave to the location of interest
will likely aVect the empirically determined values of Ai and Di for that
location.

The National Ocean Service of the U.S. Department of Commerce annually

publishes tide predictions for numerous selected points around the coastlines of
the world. (see noaa.gov) The predicted tidal elevations are given in terms of the
elevation and time predicted daily highs and lows for a year at several key
stations. Corrections on these values are then tabulated for numerous nearby
coastal locations. Remember, these are the predicted astronomical tide levels and
do not include any meteorological eVects that my be active at the time. The
National Ocean Service also publishes tables of predicted tidal currents at key
coastal locations

The patterns and amplitudes of oceanic tide wave propagation have been

modeled using numerical solutions of the long wave equations (e.g., see Hendershott, 1977). The models are driven by a forcing function that includes the
desired number of lunar and solar components. The surface stress is omitted
and for deep ocean tides the bottom stress term is negligible. The Coriolis term is
quite signiWcant and must be included. There are two basic types of oceanic tidal
models. One type employs the boundary condition of no Xow across the coastal
boundaries and attempts to predict tide ranges around the coast and in the ocean
interior. The second uses water levels at the coast as a boundary condition and
just attempts to predict tides throughout the interior of the ocean. The logic of
the second type of model is that coastal tides are known, but there exist little data
on the tides throughout the ocean.

One could also model nearshore and river/estuary tide wave propagation using

the long wave equations. For example, Reid and Bodine (1968) calibrated a
Galveston Bay storm surge numerical model for bottom friction by Wrst modeling the tide without including the surface stress term. The forcing function was
based on conditions at the entrance to the bay. Here, the bottom stress term
would be signiWcant; but if the lateral extent of the water body is relatively small,
the Coriolis term may be neglected.


-----

124 / Basic Coastal Engineering

5.4 Tsunamis

The term ‘‘tsunami,’’ which means ‘‘harbor wave’’ in Japanese, is used to denote
the relatively long period waves generated by a variety of underwater disturbances including earthquakes, landslides, and volcanic eruptions. Although tsunami waves have a low amplitude at sea, shoaling, refraction, and resonance can
greatly increase the nearshore amplitude and runup of these waves. This has
caused severe damage and the loss of many lives in those coastal areas prone to
tsunami attack. Thorough discussions of tsunamis are given by Wiegel (1970)
and CamWeld (1980) and an informative and detailed analysis of the 1964
Alaskan earthquake and resulting tsunami is given by Wilson and Torum
(1968).

Tsunamis are generated by a rapid large-scale disturbance of a mass of ocean

water that results in the displacement of the ocean surface and the generation of a
series of waves that radiate out from the disturbance. While volcano eruptions
and underwater landslides have generated waves of local signiWcance, major
tsunami events usually are the result of earthquakes that produce signiWcant
vertical movement of the sea Xoor in suYciently shallow water. These earthquakes typically have a magnitude greater than about 6.5 on the Richter scale
and a focal depth of less than 60 kilometers (Iida, 1969). The 1964 Alaskan
tsunami was generated by an earthquake of 8.4 to 8.6 magnitude and a 20- to 50kilometer focal depth that resulted in vertical land movement over an 800kilometer front in a period of 4 to 5 min (Wilson and Torum, 1968). The sea
bed rotated around a hinge line with underwater uplift and subsidence in excess
of 8 m and 2 m, respectively. Most tsunamis are generated in the active
þ �
earthquake regions along the rim of the PaciWc Ocean (Aleutian Islands, Japan,
New Zealand, and the west coast of South America). Tsunamis have also been
generated in the Indian Ocean and the Caribbean and Mediterranean Seas.

A tsunami will typically consist of a group of waves having periods from 5 to

60 min with the most common range of periods being around 20 to 30 min.
Wave heights in the deep ocean are believed to typically be a meter or less
(Wiegel, 1970). The waves have a very low steepness (see Example 5.4–1) and
thus are highly reXective which signiWcantly increases complexity in some
coastal areas.

Example 5.4-1

One of the waves in a tsunami has a period of 20 min and a height of 0.6 m at a
point in the ocean where the depth is 3800 m (this is the mean depth of the
earth’s seas). Determine the celerity and length of this wave. Determine its
celerity, length, and height in a nearshore depth of 10 m assuming no refraction,
diVraction, or reXection eVects.


-----

Coastal Water Level Fluctuations / 125

Solution:

Assume that the wave is a shallow water wave so

pffiffiffiffiffiffi pffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi

C ¼ gd ¼ 9:81(3800) ¼ 193 m=s(695 km=h)

L ¼ CT ¼ 193(20)60 ¼ 231; 700 m

d=L ¼ 3800=231; 700 ¼ 0:016

H=L ¼ 2=231; 700 ¼ 8:6 � 10[�][6]

Thus, the wave is a shallow water wave at a depth of 3800 m (and would be a
shallow water wave in the deepest parts of the ocean). Note the large speed and
length of the wave, and its very small steepness.

Equating wave power at the two water depths [Eq. (2.40)] leads to

(H [2]L)10 ¼ (H [2]L)3800

Or, since

pffiffiffiffiffiffi

L gdT
¼

� pffiffiffi� � pffiffiffi�

H [2] d H [2] d

10 3800

[¼]

So, at a depth of 10 m

� �0:25

H ¼ 0:6 [3800] ¼ 2:65 m

10

pffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi

C ¼ 9:81(10) ¼ 9:9 m=s

L ¼ 9:9(20)60 ¼ 11; 900 m

Shoaling has increased the wave height by a factor of 2:65=0:6 ¼ 4:4 times and
refraction could cause a much greater increase.

An important concern, once a tsunami has been generated, is to forecast its
arrival time at locations that are prone to tsunami wave damage. This can be
done by consulting refraction diagrams previously constructed using the basic
techniques presented in Sections 4.3 and 4.4 [where wave celerity is given by Eq.
(2.19)]. Map projection distortion must be considered and bottom irregularities
much shorter than a wave length (see Example 5.4–1) can be smoothed out.
Keulegan and Harrison (1970) used numerical techniques to construct tsunami
refraction diagrams, including compensation techniques for the distorted picture
of the earth’s surface found on a Mercator projection, so results could be plotted


-----

126 / Basic Coastal Engineering

on a Mercator map. Refraction diagrams were constructed for tsunamis generated in Alaska; Kamchatka, Russia; and Chile and propagating to Hilo, Hawaii
and Crescent City, California. A major objective was to determine nearshore
wave crest orientations for use as input to hydraulic model studies of these sites
for proposed tsunami barrier projects.

The travel time tT of a tsunami wave from its source to a point of interest can

be predicted by summing the travel times along successive intervals along the
wave orthogonal that connects the two points. Thus


tT ¼


X DS

pffiffiffiffiffiffiffigds (5:5)


where ds is the average water depth over the interval having a length DS. For
places such as Hilo, Hawaii that are frequently attacked by tsunamis, charts of
travel time from all possible sources areas have been developed (see Zetler, 1947
and Gilmour, 1961). These charts are applicable for any tsunami since the wave
celerity depends only on the water depth.

Example 5.4-1 demonstrates how much the wave height can increase as a

tsunami wave approaches the shore. Refraction can cause wave heights to be
signiWcantly larger or smaller than this. The spread of wave orthogonals as the
waves radiate out from the origin causes a spreading of energy as tsunami waves
propagate across the ocean, so regions closer to the tsunami source are generally
likely to have higher nearshore wave heights. This will cause an initial wave
height reduction which may be reversed if local hydrography refocuses wave
energy. Measured tsunami coastal wave heights and runup elevations along an
irregular coast line will likely show similar results for diVerent tsunamis approaching the same location, but for the same tsunami results might be quite
diVerent from point to point along the coast. This demonstrates the importance
of local eVects on tsunami nearshore heights and runup elevations.

Figure 5.5 shows a tide gage record from San Francisco Bay, California taken

after the 1964 Alaskan earthquake. Tsunami waves having a period around
35 min can be seen superimposed on the tide. It appears that the tsunami set
the bay into resonant oscillation to cause noticeable oscillations which continued
for over 24 hours.

Tsunami waves still have a very low steepness when they reach the shore (see

Example 5.4-1). Primary coastal damage is caused by the surge of water as the
tsunamirunsuptheslopingcoast.Althoughrunupelevationsoftsunamiwaveswill
depend on the land slope and surface conditions as well as the actual tsunami wave
steepness,asaruleofthumb(CamWeld,1980)therunupelevationwillbeequaltoor
slightlyhigherthanthewaveheightatthecoast.Therunupmayvaryfromarapidly
rising water surface to a wave that forms a bore that runs up the coastal slope. The
former appears more likely for the longer period waves (e.g., 50 to 60 min) and the
latter for the shorter period (e.g., 10 to 20 min) waves. The runup Xow velocity can


-----

9

8
7

6

5

4

3
2

1

0


March 28-29, 1964


8 9 10 11 12 13 14 15 16 17 18


Coastal Water Level Fluctuations / 127

March 28-29, 1964

19 20 21 22 23 0 1 2 3 4 5 6


Approx. hours Greenwich Mean Time

Figure 5.5. Water level gage record, San Francisco Bay.


be signiWcant for some tsunami waves. The 1964 Alaskan tsunami overturned a
locomotive engine in nearby Seward. Calculations (Wilson and Torum, 1968)
estimated the required Xow velocity to overturn the engine to be about 7.5 m/s.
Other damage comes from Xooding and scour caused by the Xowing water.

Certain coastal areas are prone to tsunami damage because of their location


(PaciWc, Caribbean, Mediterranean) and because of their local topography/hydrography. Hilo, Hawaii for example, is at the head of a funnel-shaped embayment. In general, the best ways to deal with potential tsunami damage are:
develop a good early warning system so the damage prone areas can be evacuated, remove structures that are easily damaged by Xooding or surge from low
coastal areas, design structures that must be in damage-prone areas to withstand
the potential Xooding and surge, and build barriers that might consist of structures or groves of trees to limit surge damage in key areas.

The best tsunami warning system is the one in place around the rim of the PaciWc


Ocean and operated by the National Weather Service of the National Oceanic and
Atmospheric Administration. Pressure sensors are installed at a number of coastal
sites in deep water so that they can only sense long waves (e.g. the tide and
tsunamis). When a tsunami passes over the submerged gage its occurrence is
signaled to a Xoating device that transmits the information to a land base, which
in turn, notiWes an extensive warning system located around the rim of the PaciWc.

5.5 Basin Oscillations


There are systems that respond to a disturbing force by developing a restoring
force that returns the system to its equilibrium position. But at this equilibrium
position the system has inertia which carries the system past the equilibrium


-----

128 / Basic Coastal Engineering

position and a free oscillation at the system’s natural period or frequency is
established. (A simple example of such a system is a pendulum.) The natural
frequency of oscillation of the system depends on the geometry of the system.
(For a pendulum the oscillation period depends on the length of the arm.) It is
essentially independent of the magnitude of the disturbance, which does, however, establish the magnitude of oscillation of the system. After the initial
disturbance has occurred, free oscillations continue at the natural frequency
but with exponentially decreasing amplitude due to the eVects of friction.
These systems can also undergo forced oscillations at frequencies other than
the natural frequency owing to a cyclic input of energy at other than the natural
frequency. Continuous excitation at frequencies equal or close to the natural
frequency will usually cause an ampliWed system response, the level of ampliWcation depending on the proximity of the excitation frequency to the natural
frequency and on the frictional characteristics of the system.

An enclosed or partly open basin of water such as a lake, bay, or harbor can

be set into free oscillation at its natural frequency (and harmonic modes) or
forced oscillation as described above. The result is a surging or seiching motion
of the water mass as a wave propagates back and forth across the basin. The
speed and pattern of wave propagation, and the resulting natural frequency of
the basin, depend on the basin geometry. Typical sources of excitation energy
include:

1. Ambient wave motion if the basin has an opening to permit entry of this

energy (e.g., harbor open to the sea from which the energy comes)

2. Atmospheric pressure Xuctuations

3. Tilting of the water surface by wind stress and/or a horizontal atmospheric

pressure gradient, with subsequent release

4. Local seismic activity

5. Eddies generated by currents moving past the entrance to a harbor

Bay and harbor oscillations are usually of low amplitude and relatively long

period. Their importance is due primarily to (1) the large-scale horizontal water
motions which can adversely aVect moored vessels (mooring lines break, fender
systems are damaged, loading/unloading operations are delayed) and (2) the
strong reversible currents that can be generated at harbor entrances and other
points of Xow constriction. The second factor may have positive or negative
consequences.

A basin of water, depending on its geometry, can have a variety of resonant

modes of oscillation. A resonant mode is established when an integral number
of lengths of the wave equals the distance over which the wave is propagating as
it reXects repeatedly forward and back. Further insight into the nature of
resonance and resonant ampliWcation can be gained from Figure 5.6, a classic


-----

Coastal Water Level Fluctuations / 129

Frictionless

Increasing

friction

2 3

Tn / T


A


2

1

0


Frictionless

Increasing

friction

2 3


Figure 5.6. Resonant response of an oscillating system.

diagram that demonstrates the resonant response of one of the modes of
oscillation of a resonating system. Tn is the natural resonant period for that
mode of oscillation—the period of free oscillation that develops when the system
has a single disturbance to set up that mode of oscillation. T is the period of the
system excitation being considered; it may or may not be at the resonant period.
A is the resulting ampliWcation of the oscillating system; that is, the ratio of the
amplitude of the system response to the amplitude of excitation of the system.
Three curves are shown for the frictionless case, a case with some friction, and a
case where the system is heavily damped by friction.

If the system is excited at periods much greater than the natural period (i.e.,

Tn=T approaching zero) the system response has about the same magnitude as
the excitation force. This would be the case, for example, when a small coastal
harbor that has a large opening to the ocean responds to the rising and falling
water level of the tide. As the excitation period decreases toward the resonant
period of the system the response is ampliWed. The response comes to an
equilibrium ampliWcation where the rate at which energy is put into the system
equals the rate at which energy is dissipated by the system (A frictionless system
would ultimately reach an inWnite ampliWcation). Systems with larger rates of
dissipation undergo less ampliWcation. When the excitation period equals the
resonant period of the system, ampliWcation reaches its peak. Note that frictional eVects can slightly shift the period at which peak ampliWcation occurs. At
T > Tn the ampliWcation continually diminishes with decreasing excitation
period. If the system is excited by a single impulsive force rather than a
continuing cyclic force the system oscillates at the natural period. If the system
is excited by a spectrum of excitation forces it selectively ampliWes those periods
at and around the natural period. When the cyclic excitation force is removed,
friction causes the response amplitude to decrease exponentially with time.


-----

130 / Basic Coastal Engineering

5.6 Resonant Motion in Two- and Three-Dimensional Basins

When resonant motion is established in a basin a standing wave pattern develops
(as brieXy discussed in Section 2.7). At antinodal lines there is vertical water
particle motion while horizontal particle motion occurs at the nodal lines (see
Figure 2.8). Our concerns in analyzing basin resonance are (1) to predict the
fundamental and harmonic periods of resonance for the various resonant modes;
(2) to predict the pattern of nodal and antinodal lines in the horizontal plane for
each of these resonant modes; and (3) to predict, for each resonant mode, the
amplitudes and velocities of particle motion, particularly at the nodal lines where
motion is essentially horizontal. The Wrst two just depend on the geometry of the
basin and can be easily addressed in many cases. The third also depends on the
amplitude of the excitation forces and the magnitude of frictional dissipation in
the basin. This is diYcult to resolve in a quantitative sense.

In this section we present an analysis of resonance in basins where resonant

motion is predominantly two-dimensional and in some idealized basin geometries where resonance is three-dimensional. This provides additional insight into
the nature of resonance in most basins and provides tools to analyzes resonance
for many practical situations.

Two-Dimensional Basins

Figure 5.7 shows (in proWle view) the fundamental and Wrst two harmonic modes
of oscillation for idealized two-dimensional rectangular open and closed basins.
For the closed basin the standing wave would have lengths equal to 0.5, 1.0, and
1.5 times the length of the basin. For the basin open to a large water body the
standing wave lengths would be 0.25, 0.75, and 1.25 times the basin length. The
resonant period for a particular mode of oscillation equals the wave length for
that mode divided by the wave celerity. Since most basins of concern to coastal
engineers are broad and relatively shallow, the waves are shallow water waves
and the resonant periods are given by

2G
Tn ¼ k 1 pffiffiffiffiffiffigd (closed basin) (5:6)

ð þ Þ


and

4G
Tn ¼ (2k 1)pffiffiffiffiffiffigd (open basin) (5:7)

þ

where k depends on the oscillation mode and is equal to 0, 1, 2 etc. for the
fundamental, Wrst, and second harmonic modes etc. G is the basin length as
depicted in Figure 5.7. The fundamental mode of oscillation has the longest


-----

Coastal Water Level Fluctuations / 131

Closed Open

Water surface
envelope

d

Γ Γ

Figure 5.7. Water surface envelope proWles for oscillating two-dimensional idealized

basins.

period and the harmonic mode periods decrease by a factor of 1=(k þ 1) and
1=(2k þ 1) for closed and open basins, respectively.

For many natural basins that are long and narrow (e.g., Lake Michigan, Bay

of Fundy) well established resonance is most likely to involve wave motion along
the long axis of the basin. To determine the resonant periods for these water
bodies which would have irregular cross-sections and centerline proWles we can
rewrite Eqs. (5.6) and (5.7) as follows:


envelope

d

Γ Γ


2
Tn ¼ (k 1)

þ


N
X

i¼1


pGffiffiffiffiffiffiffigdi i (closed) (5:8)


and


4
Tn ¼ (2k 1)

þ


N
X

i¼1


pGffiffiffiffiffiffiffigdi i (open) (5:9)


-----

132 / Basic Coastal Engineering

where the basin length is broken into N segments of length Gi each having an
average depth di.

Equations for estimating the horizontal water excursion and maximum particle

velocity, which occur below nodal lines, can be easily developed from the smallamplitude wave theory for shallow water waves. Combining Eqs. (2.28) and (2.57)
for the time of peak velocity under the nodal point (sin kx sin st 1) yields
¼


umax ¼ 2[HL]dT 2d 2

[¼][ HC] [¼][ H]


rffiffiffig

d


(5:10)


where T would be the resonant period Tn and umax is essentially constant over the
vertical line extending down from the nodal point. Since water particle motion is
sinusoidal, the average particle velocity would be


��2

uavg ¼ umax p



[HL]
¼

pdT


So, the particle horizontal excursion at the nodal point X during one half period
T/2 now becomes


(5:11)


rffiffiffig

d


X ¼ uavg


��T


2



[HL]
¼

2pd 2p

[¼][ HT]


Example 5.6-1

A section of a closed basin has a depth of 8 m and a horizontal length of 1000 m.
When resonance occurs in this section at the fundamental period, the height of
the standing wave is 0.2 m. Determine the resonant period, the maximum water
particle velocity, and the horizontal particle excursion that occurs under the
nodal point.

Solution:

From Eq. (5.6) for a closed rectangular basin

Tn ¼ p[2(1000)]ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi9:81(8) ¼ 226 s(3:77 min )

Equation (5.10) then yields the maximum particle velocity


umax ¼ [0]2[:][2]


rffiffiffiffiffiffiffiffiffi

9:81

8


¼ 0:11 m=s


and Eq. (5.11) yields the horizontal particle excursion


-----

Coastal Water Level Fluctuations / 133


X [0][:][2(226)]
¼

2p


rffiffiffiffiffiffiffiffiffi

9:81

8


¼ 7:96 m


These results typify basin resonance characteristics. The relatively long resonant
period indicates that it is a shallow water wave and that the wave motion (0.2 m
rise and fall in 3.77 min) would be hardly perceptible to the eye. Water particle
velocities are commensurately small. But the horizontal water particle excursion
is relatively large. A moored vessel responding to this long period wave motion
would oscillate back and forth over a signiWcant distance, tensing and releasing
the tension on the mooring line and possible slamming the fender system every
3.77 min.

The preceding discussion assumed that each lateral boundary is either closed,
and thus an antinode, or completely open to an inWnite sea, and thus a pure
node. However, many basin boundaries have partial openings and/or are open to
a larger but not eVectively inWnite body of water. The resulting boundary
condition is more complex; it causes resonant behavior at the opening that is
somewhat between that of a node and antinode, and the basin resonant periods
are commensurately modiWed.

Three-Dimensional Basins

Basins that have widths and lengths of comparable size can develop more
complex patterns of resonant oscillation. The character of these oscillations
can be demonstrated by considering a rectangular basin (see Figure 5.8), a
form that approximates many basins encountered in practice. The long wave
equations can be applied to develop analytical expressions for the periods and
water surface oscillation patterns for the various resonant modes [see Sorensen
(1993) for more detail].

y

z

Γy

η

x

Γx d

Figure 5.8. DeWnition sketch for a rectangular basin.


z

Γy

η

x

Γx d


-----

134 / Basic Coastal Engineering

If the basin is relatively small the Coriolis term in the equations of motion

[Eqs. (5.3a and b)] can be neglected. For just the patterns of surface oscillation
and the resonant periods the surface and bottom stress can also be neglected. In
addition, a linearized small amplitude solution allows the two nonlinear convective acceleration terms to be neglected. When these simpliWed forms of the
equations of motion for the two horizontal direction are combined through the
continuity equation [Eq. (5.1)] we have


� �

gd [@][2][h]

@x[2][ þ][ @]@[2]y[h][2]


¼ [@][2][h] (5:12)

@t[2]


A solution to Eq. (5.12) for a standing wave surface form as a function of
position (x, y) and time (t) is

h ¼ H cos (kxx) cos (kyy) cos st (5:13)

where the wave numbers kx and ky give the standing wave lengths in the x and y
directions and s is the wave angular frequency in terms of the diVerent periods of
the various resonant modes. SpeciWc values of kx, ky, and s depend on the basin
geometry which establishes the lengths and periods of the standing waves in the
basin.

For the rectangular basin shown in Figure 5.8 which has a depth d and

horizontal dimensions Gx and Gy the appropriate wave numbers and angular
frequency yield


� �

h H cos [2][p][Nx]
¼

Gx


� �

cos [2][p][My]

Gy


� 2pt �

cos

TNM


(5:14)


from Eq. (5.13). In Eq. (5.14) the various resonant modes are deWned by combinations of N and M which can each have values of 0, 0:5, 1:0, 1:5 . . . and TNM is the
resonant period of the particular mode. The resonant period is given by


TNM ¼ p1ffiffiffiffiffiffigd "�GNx�2þ�[M]Gy�2#�1=2


(5:15)


Nodal lines will be located where the water surface elevation is xero at all times.
From Eq. (5.14) this would require


� �

cos [2][p][N][x]

Gx


� �

cos [2][p][My]
¼

Gy


0
¼


Thus, the coordinates of nodal lines are given by


-----

Coastal Water Level Fluctuations / 135


x [G][x]
¼

4N [, 3]4[G]N[x] [, 5]4[G]N[x] [. . .]

y [G][y]
¼

4M [, 3]4M[G][y] [, 5]4M[G][y] [. . .]


(5:16)


for each resonant mode NM. In Eq. (5.16) the number of terms would
be truncated at the number of nodal lines which is equal to 2N or 2M respectively.

Note that when N or M equal zero, Eq. (5.15) reduces to the two-dimensional

resonant condition given by Eq. (5.6) with N or M given by (k þ 1)=2.

Example 5.6–2

A basin has a square planform with side lengths G and a water depth d. For the
resonant mode having an amplitude H and N ¼ M ¼ 0:5 give the equations for
the water surface elevation as a function of position and time and the equation
for the speciWed resonant mode. Describe the behavior of the water surface as the
oscillations occur.

Solution:

For N ¼ M ¼ 0:5 Eq. (5.15) yields

G
T11 ¼ pffiffiffiffiffiffiffiffi2gd

for the period of this resonant mode as a function of the basin dimensions.

The water surface elevation, from Eq. (5.14), is given by

h H cos [p][x]
¼

G [cos][ p]G[y] [cos 2]T[p]11[t]


Since 2N 2M 1, there will be a pair of nodal lines. From Eq. (5.16), they will
¼ ¼
be at x ¼ G=2 and y ¼ G=2.

Shown below is a plot of the water surface contours at t ¼ 0, T11, 2T11 . . . The

solid lines show contours that are above the still water level, increasing from zero
at the nodal line to H at the corners x, y 0 and x, y G. The dashed lines
¼ ¼
show contours that are below the still water level. A quarter of a period later the
water surface is Xat. At t ¼ T11=2 the contours are reversed and at t ¼ 3T11=4 the
surface is Xat again. At t ¼ T11 the surface is the same as at t ¼ 0 and the cycle is
complete. The maximum standing wave height would be at the corners and
would equal 2H. Maximum horizontal Xow velocities would occur at the nodal
lines and be perpendicular to the nodal lines.


-----

136 / Basic Coastal Engineering

y

η = −H

Γ

η = H


η = H

x


η

Nodal

lines


Γ


η = −H


Equations (5.14) and (5.15) for resonance in a rectangular basin have also been

developed using a diVerent approach (Raichlen, 1966). The three-dimensional
Laplace equation is solved with the linearized DSBC [Eq. (2.8)], the BBC [Eq.
(2.3)], and the boundary conditions at the vertical side walls of the basin, namely
that the horizontal component of the Xow velocity is zero at the wall. Assuming
shallow water this yields the following velocity potential


f [Hg]
¼

s [cos 2][N]G[p]x [x]


cos [2][M][p][y]

Gy


sin st (5:17)


With Eq. (5.17), other Xow properties including the water particle velocity and
displacement patterns can be derived (see Section 2.7).

Helmholtz Resonance

In addition to the standing wave modes of oscillation discussed above, a basin
open to the sea through an inlet can resonate in a mode known as the Helmholtz
mode. Water motion is analogous to that of a Helmholtz resonator in acoustics.
The water surface in the basin uniformly rises and falls while the inlet channel
water mass oscillates in and out. For a simple somewhat prismatic basin and
channel the resonant period TH is given by (Carrier et al., 1971)


TH ¼


s(ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiLc þ L0c[)][A][b]

gAc


(5:18)


where Ab is the basin surface area, Ac is the channel cross-section area, Lc is the
channel length, and L0c [is an additional length to account for the additional mass]


-----

Coastal Water Level Fluctuations / 137

of water at each end of the channel that is involved in the resonant oscillation. L0c

is given by (adapted from Miles, 1948)


L0c [¼ �]p[W] ln�pffiffiffiffiffiffiffigdpWcTH �


(5:19)


where W and dc are the channel width and depth, respectively. The Helmholtz
mode appears to be important for the response of some ocean harbors to
tsunami excitation (Miles, 1974). It is also a signiWcant mode of oscillation for
a number of harbors on the Great Lakes (Sorensen and Seelig, 1976) that
respond to the storm-generated long wave energy spectrum on the Lakes.

5.7 Resonance Analysis for Complex Basins

Many real basins can be analyzed with suYcient accuracy using the procedures
described in the previous section. If the geometry of the basin under investigation is
too complex for these procedures to be applied, one can resort to either a physical
hydraulic model investigation or analysis by a numerical model procedure.

A hydraulic model for a study of basin resonance would be based on Froude

number similarity. If the model to prototype horizontal and vertical scale ratios
are the same (undistorted model) this leads to


ffiffiffiffiffi
Lr


(5:20)


Tr ¼


p


where Tr, the time ratio, would be the ratio of the resonant period measured in
the model to the equivalent prototype period and Lr is the model to prototype
scale ratio. To proceed, the harbor and adjacent areas would be modeled to
some appropriate scale in a wave basin. Then the model harbor would be
exposed to wave attack for a range of periods covering the scaled range of
prototype waves expected. The harbor response would typically be measured by
wave gages at selected locations of importance and by overhead photography of
water movement patterns (using dye or Xoats). A typical result might show the
response amplitude in the harbor versus incident wave period and would
produce curves with peaks at the various resonant periods. Since bottom
friction and the amplitudes of the incident waves are not typically modeled,
the results indicate only expected periods of resonant ampliWcation in the
harbor and related patterns of horizontal water motion at these resonant
conditions.

If the horizontal and vertical scale ratios are not equal (distorted model), as

may be necessary for economic, space availability, or other reasons, Froude
number similarity leads to


-----

138 / Basic Coastal Engineering


Tr ¼ p[L]ffiffiffiffiffiffiffiL[rh]rv (5:21)

where the subscripts h and v refer to the horizontal and vertical scale ratios. For
additional discussion on the conduct of basin resonance models see Hudson et al.
(1979) and Hughes (1993). Some examples of harbor resonance model studies are
presented by U.S. Army Waterways Experiment Station (1975) and Weggel and
Sorensen (1980).

The resonant modes in an irregular shaped basin can also be investigated by

numerical model analysis. A common approach employs the long wave equations which are solved for the water surface elevation and horizontal velocity
components over a grid pattern that covers the basin. This essentially involves
dividing the basin with a horizontal grid system and solving the equations of
continuity and motion in long wave form at each grid square sequentially
through space for successive time intervals. Typically, for harbor-sized basins
the Coriolis and convective acceleration terms would be omitted from the
equations of motion. The surface stress term would also be omitted but a bottom
friction term may be included. A condition of no horizontal Xow is speciWed for
the basin solid boundaries. At the opening from the basin to the sea the
boundary condition is deWned by the input wave condition that sets the basin
resonating. The model can be run for a range of periods to see which periods
excite the basin. Botes et al. (1984) input a wave spectrum and did a spectral
analysis of the water surface response at a point in the harbor to determine the
signiWcant resonant periods. The model was then run with a sine wave input at
these resonant periods to obtain a detailed look at the resulting water surface
oscillation and horizontal Xow velocity patterns in the harbor. Wilson (1972)
presents a general overview of basin oscillations including a discussion of various
numerical modeling approaches.

5.8 Storm Surge and Design Storms

A storm over shallow nearshore coastal waters or shallow inland water bodies can
generate large water level Xuctuations if the storm is suYciently strong and the
water body is shallow over a large enough area. This is commonly known as storm
surge or the meteorological tide. Storm activity can cause both a rise (setup) and
fall (setdown) of the water level at diVerent locations and times—with the setup
commonly predominating in vertical magnitude, lateral extent, and duration.
SpeciWc causes of the water level change include: surface wind stress and the
related bottom stress caused by currents generated by the surface wind stress,
response to Coriolis acceleration as wind-induced currents develop, atmospheric
horizontal pressure gradients, wind wave setup, long wave generation caused by
the moving pressure disturbance, and precipitation and surface runoV.


-----

Coastal Water Level Fluctuations / 139

Storm surge is generally not an important factor in water level analysis on the

PaciWc coast of the United states owing to the narrow continental shelf along this
coast. However, on the Gulf and Atlantic coasts where the continental shelf is
generally much wider and where hurricanes and extratropical storms are common, storm surge is extremely important. Storm-generated water level Xuctuations in the shallower of the Great Lakes (especially at the BuValo and Toledo
ends of Lake Erie) can also be signiWcant.

Hurricane Camille in August 1969 had estimated sustained peak wind speeds of

165 knots as it crossed the Mississippi coast. The storm surge reached a maximum
of 6.9 m above MSL at Pass Christian, up to 25 cm of rainfall were measured, and
the coastal area in the region of highest winds suVered virtually complete destruction (U.S. Army Engineer District, New Orleans, 1970). Surge levels in excess of
3 m above MSL occurred along the coast from the Mississippi River Delta to the
Mississippi–Alabama line, a coastal distance of over 170 km. Estimated storm
damage (no major urban areas were hit) was just under a billion dollars.

Storm surge calculations require a knowledge of the spatial and temporal

distribution of surface wind speed and direction, and surface air pressure, as well as
the forward path and speed of the design storm. The Atlantic coast of the United
States experiences extratropical storms that result from the interaction of warm
and cold air masses and that can generate a substantial storm surge. However,
along most of the Atlantic coast south of Cape Cod and all of the Gulf coast, the
worststormconditionsordesignstormwillusuallybeahurricaneoftropicalorigin.

Design wind and pressure Weld conditions for a site may be established by

using the measured conditions from the worst storm of record in the general
area. Or, if suYcient data exist, a return period analysis may be conducted to
select storm design parameters (e.g., wind speed, pressure drop) having a speciWed frequency of occurrence for that area. Also, if suYcient historical surge
elevation data are available, direct surge elevation–frequency relationships can
be developed for a given area. Bodine (1969) did this for the Gulf coast of Texas
using data from 19 hurricanes dating from 1900 to 1963.

A hurricane is a cyclonic storm having wind speeds in excess of 63 knots that

originatesinthetropicsnearbutnotattheequator.ThosehurricanesthataVectthe
United States typically move north from the region between Africa and South
America(oftenwithveryirregular paths)intotheGulfofMexicooruptheAtlantic
coast, eventually veering east and out over the Atlantic to dissipate. The driving
mechanism is warm moist air that Xows toward the eye (center) of the hurricane
where the pressure is lowest. After rising in the eye the air Xows outward at higher
altitudes. Coriolis acceleration causes the inward Xowing air to have a circular
component, counterclockwise (looking down) in the northern hemisphere and
clockwise in the southern hemisphere. The diameter of hurricanes usually does
not exceed 300 nautical miles. The deWciency of warm moist air and the existence of
increased surface friction when the hurricane is over land will cause it to dissipate,
as will the deWciency of warm moist air at higher ocean latitudes.


-----

140 / Basic Coastal Engineering

The surface pressure in a hurricane, which decreases from the ambient pres
sure at the periphery Pa to the lowest pressure at the eye Pe can be estimated by
the following empirical equation (see Schwerdt et al., 1979)


pr � pe
pa � pe


¼ e[�][R][=][r] (5:22)


which is based on an analysis of historical hurricane pressure data. In Eq. (5.22), Pr
is the pressure at any radius r from the eye of the hurricane and R is the radius from
the eye to the point of maximum wind speed. Wind speeds increase from the
periphery toward the eye with maximum wind speeds occurring typically at a
radius of between 10 and 30 nautical miles from the eye (where the pressure
gradient is the largest). Inside this point the wind speeds diminish rapidly to near
calm conditions at the eye. The pressure at the periphery may be taken as about the
standard atmospheric pressure of 29.92 inches of mercury. The pressure in the eye
varies signiWcantly, naturally being lower for stronger hurricanes. A pressure in the
eye of the order of 27.5 inches of mercury will occur in a strong hurricane and
pressures as low as near 26 inches of mercury having been recorded. The hurricane
season in the north Atlantic is from June to November with most hurricanes
occurring in the months of August to October.

The U.S. National Weather Service, with support provided by the Nuclear

Regulatory Commission and Army Corps of Engineers has developed hypothetical design hurricanes for the U.S. Atlantic and Gulf coasts that are based on a
return period analysis of signiWcant hurricane parameters (Schwerdt et al., 1979).
They developed a Standard Project Hurricane (SPH) and a Probable Maximum
Hurricane (PMH). The SPH has ‘‘a severe combination of values of meteorological parameters that will give high sustained wind speeds reasonably characteristic of a speciWed location.’’ Only a few hurricanes of record for a large region
covering the area of concern will exceed the SPH. The combined return period
for the total wind Weld will be several hundred years. The PMH has ‘‘a combination of values of meteorological parameters that will give the highest sustained
wind speed that can probably occur at a speciWed coastal location.’’ The PMH
was developed largely for use in the design of coastal nuclear power plants.
Besides being used for storm surge analysis the SPH and PMH are useful for
wave prediction and the analysis of wind loads on coastal structures.

The SPH and PMH are presented in terms of the central pressure in the eye,

the peripheral pressure at the outer boundary, the radius to maximum wind
speed, the forward speed of the hurricane, the direction of movement as the
hurricane approaches the coast, and the inXow angle which is the angle between
the wind direction and a circle concentric with the hurricane eye. (The latter
typically varies from 10 to 30 degrees at points from the location of maximum
wind speed to the hurricane periphery.) Ranges of values for the listed hurricane
parameters are given as a function of coastal location from Maine to Texas. With
selected values of these parameters the surface (10 m elevation) wind Weld can be


-----

Coastal Water Level Fluctuations / 141

Direction of advance

20

50

120

100

80

60

50

Wind speed, mph Scale:

0 20 40 60 80 100

40

miles

Figure 5.9. Typical surface wind Weld for a Standard Project Hurricane.

plotted and the pressure Weld can be calculated from Eq. (5.22). Figure 5.9 shows
the surface wind Weld for a typical SPH.

From economic and other considerations it may be desirable to use a design

hurricane other than the SPH and PMH even though the designer has some
Xexibility in the selection of the parameters for these storms. For example, a
wooden pier with a shorter design life or a rubble mound breakwater that can
relatively easily be repaired would be designed for a lesser storm than the SPH.
North of Cape Cod the design storm is likely to be an extratropical cyclone
(known as a Northeaster) rather than a hurricane. Patterson and Goodyear
(1964) present the characteristics of Standard Project Northeasters that may be
used for storm wind prediction in this region.

5.9 Numerical Analysis of Storm Surge

Several diVerent numerical models have been developed to analyze storm surge
along the open coast and in bays and estuaries (e.g., Reid and Bodine, 1968;
Butler, 1978; Wanstrath, 1978; Tetra Tech, 1981; Mark and ScheVner, 1993).
They are two-dimensional vertically integrated models that apply the long wave


20

50

120

100

80

60

50

Wind speed, mph Scale:

0 20 40 60 80 100

40


-----

142 / Basic Coastal Engineering

equations [Eqs. (5.1), (5.3a), and (5.3b)] to a grid system that covers the area to
be modeled. At each grid point the numerical model calculates the two horizontal Xow components and the water surface elevation at the successive time
intervals for which the model is operated.

Typically, the area to be modeled is divided into square segments and the three

long wave equations are written in Wnite diVerence form for application to each
square segment in the grid. At the sides of squares that are at the lateral water
boundaries the appropriate boundary conditions must be applied to allow for
correct computation of Xow behavior at these boundaries. Typical boundary
conditions might include: water–land boundaries across which there will never
be any Xow, adjacent low-lying areas that will Xood when the water surface level
reaches a certain elevation, inXow from rivers and surface runoV, barriers such as
barrier islands and dredge spoil dikes that can be overtopped, and oVshore
boundaries having a speciWed water level/inXow time history. The computer
solution for the unknown values at each grid square (qx, qy, h) proceeds sequentially over the successive rows and columns for a given time and then time is
advanced and the spatial calculations are repeated.

Several important considerations arise when these models are developed and

applied:

1. If the lateral extent of the water body is suYcient for the horizontal

atmospheric pressure gradient to be important, the hydrostatic water surface elevation response can be calculated separately as a function of location and time and added to the long wave model result.

2. The bottom stress term must be empirically established from previous

experience and by calibration using tide wave propagation analysis for
periods of low winds as well as results of previous storms.

3. For complex coastal boundaries the grid mesh shape and size may have to

be adjusted to produce adequate surge elevation calculations.

4. Wave setup (see Section 2.6) which occurs inside the surf zone is dependent

on the wave conditions generated by the storm. If this is an important
component of the total surge level, wave predictions must also be made so
the wave setup can be calculated.

5. The wind and pressure Welds must be speciWed in the model. For calibration

of models for existing storms there may be adequate information available.
For future predictions for storms where adequate measurements are not
available, the SPH or PMH may be used or one of the available wind Weld
models may be used (e.g., see Thompson and Cardone, 1996).

6. A wind stress drag coeYcient is required to convert the surface wind speed

to a resulting surface stress for the equations of motion. A commonly used
relationship was developed by Van Dorn (1953). From elementary Xuid


-----

Coastal Water Level Fluctuations / 143

mechanics the wind-induced shear stress on a surface is typically written as
a product of the drag coeYcient times the air density times the wind speed
squared. For storm surge analysis it is more useful to write a relationship
for surface stress in terms of the water density r, i.e.,

ts ¼ KsrW[2] (5:23)

where Ks is the wind stress drag coeYcient and W is the wind speed at the
standard 10 m elevation. The relationship given by Van Dorn is


� �2

Ks ¼ 1:21 � 10[�][6] þ 2:25 � 10[�][6] 1 � [5]W[:][6]


(5:24)


where the wind speed is in meters per second. This is based on a Weld study
that was conducted at a yacht basin along the California coast. For extensive evaluations of the available information on wind stress drag coeYcients
see Wilson (1960) and Garrett (1977).

7. A storm is a moving pressure disturbance which, given the right conditions,

can generate long waves that propagate ahead of the storm and can cause
what has been termed an initial setup along the coast (see Sorensen, 1993).
This occurs when the forward velocity of the storm is close to the celerity of
a shallow water wave for the water depth over which the storm is traveling
(i.e., a storm speed Froude number close to unity). It takes time for this
wave to develop so the storm must travel over the right water depth for a
signiWcant period of time.

8. For detailed and suYciently accurate analysis of the surge conditions at

diVerent locations of the water body a suYciently Wne grid must be established since the water depth is assigned a constant average value over each
grid square. But for stability of the model calculations the time interval
selected for calculations must Wt the grid spacing. Thus, Wner grid sizes
require shorter time intervals and a commensurately signiWcant increase in
computation time.

An early but instructive storm surge model was the one employed by Reid

and Bodine (1968) to calculate storm surge in Galveston Bay, Texas. For this
application the equations of motion [Eqs. (5.3a) and (5.3b)] were somewhat
simpliWed. The convective acceleration terms were considered negligible owing
to the scale of the bay as was the Coriolis acceleration term owing both to the
bay scale and the dominance of bottom friction owing to the relatively shallow
water depths. The Van Dorn relationship was used to deWne the wind stress
drag coeYcient. Flooding of low-lying terrain adjacent to the bay and overtopping of the barrier island that separates the bay from the Gulf of Mexico were


-----

144 / Basic Coastal Engineering

included through the application of the boundary conditions. The boundary
condition at the entrance to Galveston Bay from the Gulf was incorporated by
extending the model seaward of the bay, specifying a water level condition at
this seaward boundary and applying a discharge coeYcient for the bay entrance.
The area modeled, including the bay, a very small portion of the Gulf, and lowlying land around the bay had a nominal dimension of about 40 miles by 50
miles. This was subdivided into 2 mile square grids and time steps of 3 and
4 min were used. Bottom friction was initially calibrated for a spring astronomical tide propagating into the bay during a period of calm wind conditions.
Further calibration of bottom friction and discharge coeYcients was carried out
for the well-documented Hurricane Carla of 1961. Then the calibrated model
was veriWed by attempting to duplicate the measured surge conditions of Hurricane Cindy of 1963.

5.10 SimpliWed Analysis of Storm Surge

Occasionally in engineering practice it is not necessary, owing to time and cost
limitations and because of lesser required accuracy, to apply the more sophisticated numerical analysis procedures to estimate storm surge at a given site. A
simpliWed approach to storm surge analysis would involve calculating the wind/
bottom stress-induced surge, the pressure-induced surge, and possibly the Coriolis-induced surge separately. Each is calculated from a simple hydrostatic
balance. Thus, the convective and local acceleration terms as well as continuity
requirements are neglected. This basically assumes a static storm that is in
position for a suYcient length of time for the water level response to come to
equilibrium with suYcient water being available to achieve that equilibrium.
Thus, in most cases a conservative setup estimate would be produced. The eVects
of astronomical tide level variations and wave-induced setup nearshore can also
be separately evaluated if necessary.

Each of these components—wind/bottom stress setup, atmospheric pressure

gradient setup, and Coriolis setup—is brieXy presented below. A few comments
on appropriate tide levels and wave-induced setup are also included.

Wind/Bottom Stress Setup

The wind acting on the water surface causes a shear stress given by Eq. (5.23),
where the wind stress drag coeYcient Ks can be deWned by Eq. (5.24) or some
other relationship as discussed above. The surface wind stress generates a
current that, in turn, develops a bottom stress. Usually, the bottom current
velocity is not known nor can it easily be calculated, so the bottom stress cannot
be directly calculated. Saville (1952), from Weld data collected at Lake Okeechobee, FL, suggested that the bottom stress was in the order of 10% of the surface
wind stress. Van Dorn (1953), from his Weld data and the threshold limits on his


-----

Coastal Water Level Fluctuations / 145

equipment for measuring the bottom stress, reported that it was generally less
than 10% of the surface stress. Thus, the ratio tb=ts ¼ 0:1 can be used for windinduced setup calculations if no better data are available. If adequate wind,
pressure, and resulting setup data are available from a previous storm at a
particular site, it is better to determine a local combined surface and bottom
stress coeYcient Ksb(ts þ tb ¼ KsbrW [2]), which then acts as an ‘‘all inclusive’’
calibration factor for subsequent wind/bottom stress setup calculations.

Figure 5.10 shows a section of a nearshore water segment of length Dx in the

direction in which setup is being calculated, unit width, and depths d and
d þ DSw: DSw is the setup owing to wind and bottom stresses acting over the
distance Dx. The hydrostatic forces on each end are shown and the bottom stress
is drawn in the same direction as the surface wind stress because it is assumed
that the wind-generated current causes a reverse Xow on the bottom. If the wind
is blowing at an angle u to the x direction, then the component of the wind
velocity in the x direction Wx is used. The eVective stress then becomes

ts þ tb ¼ KsbrW [2] cos u ¼ KsbrWWx

Since the water surface slope DSw=Dx is extremely Xat a static balance yields

tsDx þ tbDx þ [1]

2 [g][r][d][2][ �] 2[1] [g][r][(][d][ þ][ D][S][w][)][2][ ¼][ 0]


Inserting the wind/bottom stress relationship, eliminating higher order terms,
and solving yields

Wx

τs

_d + ∆ Sw_ _V_

_d_

τb

∆x

Figure 5.10. DeWnition sketch for wind/bottom stress and Coriolis setup derivations.


τs

_d + ∆ Sw_ _V_

_d_

τb

∆x


-----

146 / Basic Coastal Engineering


"sffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi #

DSw ¼ d 2KsbWWgd [2] xDX þ 1 � 1


(5:25)


where Ksb 1:1 Ks may be used if no better information is available (as dis¼
cussed above).

For a shore normal proWle on the open coast, wind/bottom stress setup calcu
lations can be made using Eq. (5.25), keeping in mind the assumptions discussed
above. The proWle would be broken into segments (not necessarily of equal size) of
length Dx over which an average depth and wind velocity can be deWned. Starting
at the oVshore point where the wind velocity is suYciently low and/or the water is
suYciently deep so setup is negligible, the setup for each segment can be calculated
and summed to yield the total setup at the shore. As the calculation proceeds, the
accumulated setup for the previous segments should be included in determining
the water depth for the next segment setup calculation.

Equation (5.25) can be applied (with caution) to enclosed bays that are not too

irregular in shape. The depth for a given segment would have to be the average over
the length and width of the segment. The volume of water that sets up on the
leeward end of the bay must equal that removed from the windward end and the
two sections would be divided by a nodal line. For a given wind Weld, a nodal line
positionwouldbeassumedandthesetupcalculationswouldbecarriedoutupwind
and down wind from the nodal line. Then the setup and setdown water volumes
would be determined and compared. A balance of the setup and setdown volumes
determines the Wnal surface proWle and nodal line position.

Atmospheric Pressure Gradient Setup

From hydrostatics, the water level variation or setup Sp owing to a horizontal
atmospheric pressure diVerential Dp between two points on a continuous body of
water is

Sp ¼ [D]rg[p] (5:26)


where r is the water density.

By combining Eqs. (5.22) and (5.26) one can calculate the static pressure setup

that occurs at a point of interest in an SPH. For a pressure diVerential of say 2.5
inches of mercury (e.g., 29.9 to 27.4) from the periphery to the eye of a hurricane,
the static pressure setup at the eye would be 0.86 m.

Example 5.10-1

The bottom proWle normal to the shoreline in the area between Galveston and
Port Arthur, TX is tabulated below (depths were read in fathoms and converted
to meters; 1 fathom 6 feet 1.83 m).
¼ ¼


-----

Coastal Water Level Fluctuations / 147

Depth (m) Distance (m)

7.31 2750

10.05 4590

13.72 22930

14.62 45860

20.12 48150

23.97 82550

25.60 100890

27.43 107710

36.57 121530

54.86 144460

73.15 181150

91.43 190320

Seaward of the 91.43 m depth the depth increases relatively rapidly and is

suYciently deep so that little additional setup would occur.

For a 60 knot (30.86 m/s) wind blowing landward along this proWle calculate

the setup on the shore. If the pressure gradient along this proWle is 0.003 inches of
mercury per nautical mile what pressure setup would occur?

Solution:

From Eq. (5.24) the drag coeYcient is


� �2

Ks ¼ 1:21 � 10[�][6] þ 2:25 � 10[�][6] 1 � 30[5][:]:[6]86


¼ 2:72 � 10[�][6]


Then, Eq. (5.25) becomes

2


DSw ¼ d4


sffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi

2(1:1)(2:72)10[�][6](30:86)[2]Dx

1
þ
9:81 d [2]


1
�


3

5


or


DSw ¼ d


"rffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi #

0:00058Dx

1 1
þ �
d[2]


We then break the proWle into segments having a length Dx and a depth
d þ SDSw which is the depth below still water for the segment plus the accumulated surge up to that segment. The accumulated surge is then calculated from
the above equation, starting at the seaward segment and using the depth plus
accumulated surge for d. The results are tabulated below (all values are in
meters):


-----

148 / Basic Coastal Engineering

d Dx DSw d þ SDSw

3.66 2750 0.14 5.74

8.68 1840 0.04 10.72

11.88 18340 0.39 13.53

14.17 22930 0.43 15.39

17.37 2290 0.04 18.55

21.95 34400 0.44 22.69

24.79 18340 0.21 25.32

26.51 6820 0.07 26.97

32.00 13820 0.12 32.34

45.72 22930 0.14 45.92

64.00 36690 0.17 64.03

82.29 9170 0.03 82.29

190320 2.22

Thus, the total wind-induced setup at the shore would be 2.22 m and the setup

proWle could be determined by sequentially summing the values in the second
and third columns.

The distance from the oVshore starting point to the shore is 190320 m ¼ 102:8

nautical miles. Thus, the pressure diVerence is (0.003)102.8 0.31 inches of
¼
mercury. From hydrostatics

Sp ¼ [0][:]12(3[31(13]:28)[:][55)] ¼ 0:11 m

Note how the above calculation relates to Eq. (5.26).

Coriolis Setup

If a current is Xowing along a shoreline, Coriolis acceleration will cause the water
to deXect to the right in the Northern hemisphere. If the shoreline is on the
righthand side of the current the deXection will be restrained, causing a setup of
water on the shore. If the shoreline is on the lefthand side there will be a setdown
at the shore.

In Figure 5.10 a current of velocity V is coming out of the page and Coriolis

acceleration causes a setup as shown. A balance between the hydrostatic forces
and the Coriolis acceleration or force per unit mass yields


1
2 [g][r][d] [2][ þ][ 2][v][V][ sin][ fr][gd][D][x][ �] 2[1] [g][r][(][d][ þ][ D][S][c][)][2][ ¼][ 0]


-----

Coastal Water Level Fluctuations / 149

where Sc is the Coriolis set up. Neglecting higher order terms leads to

Sc ¼ [2]g [v] [V][ sin][ fD][x] (5:27)

which can be used to calculate the setup over a given horizontal distance at any
latitude if the current velocity is known.

Away from the shore, wind-generated currents are free to respond to the

Coriolis acceleration; but nearshore this response is restricted and setup or
setdown occurs. For simple analyses the resulting wind-generated current velocity is not easily determined. Often, the current velocity is small or in a direction
such that the Coriolis setup can be neglected in a simple analysis. The latter is
often true in small bays and lakes.

Bretschneider (1967) solved the equation of motion for the alongshore direc
tion, including only the wind and bottom stresses and the local acceleration to
obtain an equation for the wind-generated longshore current velocity. For the
resulting steady-state condition (i.e., suYcient wind duration)


V Wd [1][=][6]
¼


rffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi

Ks

14:6n[2][ sin][ u]


(5:28)


where n is Manning’s roughness coeYcient (typical value is 0.035), u is the angle
between the wind direction and a line perpendicular to the coast and/or bottom
contours, and V is the resulting alongshore current velocity. The derivation of
Eq. (5.28) assumes that there is no Xow component normal to the shore, limiting
its use to the nearshore region. The author has found that results from Eq. (5.28)
generally agree with the rule of thumb that wind-generated surface current
velocities will be 2% to 3% of the wind speed.

Astronomical Tide and Wave Setup

Storm surge setup calculations should be added to some reasonably expected
higher tide for conservative estimates for engineering design. There is a small
likelihood that the peak of the storm surge will arrive at exactly the same time as
high tide, but assumption of some higher tide level will ensure a conservative
estimate of expected water levels. Note also that there is a nonlinear interaction
between the wind setup and the astronomical tide level (and arrival time) as both
depend on the water depth. When the wind setup is calculated separately and
added to the astronomical tide level the result would be a slightly higher water
level than the true coupled water level.

Wave-induced setup at the shoreline can be calculated using wind-generated

wave predictions (Chapter 6) and the procedures demonstrated in Example 2.61. To make these calculations one must know the breaker wave height and water
depth as well as the nearshore bottom slope.


-----

150 / Basic Coastal Engineering

5.11 Long-Term Sea Level Change

When the mean sea level is measured at many coastal sites over a long period of
time, it is observed that this level is changing relative to the land. The change is
due to a general global eustatic rise in the mean sea level superimposed on a
possible tectonic uplift or subsidence of the coast. Along most of the U.S.
coastline relative sea levels have been rising, except for some coastal regions in
Alaska where coastal uplift rates exceed the eustatic sea level rise to produce a
lowering of the relative sea level. Hicks and Hickman (1988) report on yearly
relative mean sea level trends for 45 U.S. coastal stations based on 50 to over 100
years of tide gage record. The 25 U.S. Atlantic coast relative sea level change
values range from 1.79 to 4.33 mm/year, whereas four stations in Alaska had
þ þ
mean sea level changes of 0.09 to 12.4 mm/year.
� �

A sea level rise of 2 to 4 mm/year produces a rise of 0.2 to 0.4 m in a century.

This can have some noticeable impacts on the coast as the mean water level rises
on the beach face and there is a concurrent retreat of the beach face caused by
this sea level rise. It can also have signiWcant impacts on the design of coastal
structures. See U.S. National Research Council (1987) and Sorensen (1991) for a
discussion of these impacts.

A study conducted by Kyper and Sorensen (1985) well exempliWes the potential

impact of the expected rise in mean sea level on a sandy beach backed by a seawall.
As mean sea level rises the beach face is Xooded by the rising water level. The beach
proWle also responds by retreating as the raised sea levels causes a net movement of
sandonthebeachproWle totheoVshorearea.Foracoastalstructureexposedtothe
sea, the raised sea level means that the water depth is increased at the toe of the
structure. Deeper water typically allows higher waves to reach the structure because the height of a breaking wave is related to the water depth at breaking (see
Section 2.8). Recession of the beach proWle at the toe of the structure further
increases the height of the wave that can attack the structure.

Kyper and Sorensen (1985) studied sea level rise impacts on the beach and

stone mound seawall at Sea Bright NJ, for a range of expected sea level rise
scenarios. Construction of the seawall commenced in 1898. It was observed that
there was increasing damage to the seawall as time progressed through the 1970’s
and 1980’s, by which time much of the seawall had no beach in front of it.
Apparently, the lowering of the beach face in front of the seawall combined with
the rise in mean sea level at the site allowed waves that exceed the height for
which the seawall is stable to cause the damage. It is estimated that the relative
rise in mean sea level at the site was of the order of a half meter during the past
century This was exacerbated by the deWciency of sand transport past the
structure which caused a further lowering of the beach face.

The primary question addressed by Kyper and Sorensen was to investigate the

relative costs of constructing and maintaining an artiWcial beach in front of the


-----

Coastal Water Level Fluctuations / 151

seawall to protect it from wave attack, versus the cost of adding an additional
layer of larger armor stone on the face of the seawall to increase its stability to
the increased wave attack. Quantifying the increased shoreline recession and
coastal Xooding expected from a range of expected future sea level rise scenarios,
allowed the authors to quantify the volume of sand necessary to maintain a
design beach width with a speciWed crest elevation. Then the authors determined
the increased armor stone size for a refurbished seawall for the same expected sea
level rise scenarios. The authors also discuss the impact of no future coastal
engineering works being implemented at the site.

The Wnal choice of whether to construct the protecting beach or to upgrade the

seawall depends on the material costs (beach Wll, stone, etc.) and construction costs
at the time the project is to commence. It also depends on other factors such as the
economic value of recreational beneWts on the expanded beach and the funding
available from national and local sources for the competitive projects.

Global eustatic sea level rises that have been observed during the past century

are believed to be caused by atmospheric warming which causes sea water to
expand and land ice in glaciers to melt, adding water to the seas. There have been
a number of forecasts that this rise in global eustatic sea level will accelerate
during the coming century (see U.S. National Research Council, 1987). If this
happens the eVects on the coastline will be signiWcant.

Large mean water level variations are observed on the Great Lakes. These are

due primarily to changes in seasonal and longer term rainfall/runoV variations.
The lakes can experience mean monthly seasonal Xuctuations of 0.3 m or more
and longer term Xuctuations of 1 to 2 m over a period of several years.

5.12 Summary

This chapter presented the characteristics and, where possible, the techniques for
predicting water level Xuctuations having a period greater than the periods of
waves in the wind wave portion of the wave energy spectrum. The discussion
of surface waves to this point considered only the simple monochromatic form of
these waves. Chapter 6 considers the complex form of wind-generated waves
observed at sea as well as the generation, analysis, and prediction of these waves.

5.13 References

Bodine, B.R. (1969), ‘‘Hurricane Surge Frequency Estimated for the Gulf Coast of

Texas,’’ Technical Memorandum 26, U.S. Army Coastal Engineering Research Center,
Washington, DC.


-----

152 / Basic Coastal Engineering

Botes, W.A.M., Russell, K.S., and Huizinga, P. (1984), ‘‘Model Harbor Seiching Com
pared to Prototype Data,’’ in Proceedings, 19th International Conference on Coastal
Engineering, American Society of Civil Engineers, Houston, pp. 846–857.

Bretschneider, C.L. (1967), ‘‘Storm Surges,’’ Vol. 4, Advances in Hydroscience, Academic

Press, New York, pp. 341–418.

Butler, H.L. (1978), ‘‘Coastal Flood Simulation in Stretched Coordinates,’’ in Proceed
ings, 16th Conference on Coastal Engineering, American Society of Civil Engineers,
Hamburg, pp. 1030–1048.

CamWeld, F.E. (1980), ‘‘Tsunami Engineering,’’ Special Report No. 6, U.S. Army Coastal

Engineering Research Center, Ft. Belvoir, VA.

Carrier, G.F., Shaw, R.P., and Miyata, M. (1971), ‘‘Channel EVects in Harbor Reson
ance,’’ Journal, Engineering Mechanics Division, American Society of Civil Engineers,
Dec., pp. 1703–1716.

Dean, R.G. and Dalrymple, A.T. (1984), Water Wave Mechanics for Engineers and

Scientists, Prentice-Hall, Englewood CliVs, NJ.

Garrett, J.R. (1977), ‘‘Review of Drag CoeYcients Over Oceans and Continents,’’

Monthly Weather Review, Vol. 105, pp. 915–929.

Gilmour, A.E. (1961), ‘‘Tsunami Warning Charts,’’ New Zealand Journal of Geology and

Geophysics, Vol. 4, pp. 132–135.

Harris, D.L. (1981), ‘‘Tides and Tidal Datums in the United States,’’ Special Report No.

7, U.S. Army Coastal Engineering Research Center, Ft. Belvoir, VA.

Hendershott, M.C. (1977), ‘‘Numerical Models of Ocean Tides,’’ The Sea, Vol. 6, John

Wiley, New York, pp. 47–96.

Hicks, S.S. and Hickman, L.E. (1988), ‘‘United States Sea Level Variations through

1986,’’ Shore and Beach, July, pp. 3–7.

Hudson, R.L., Hermann, F.A., Sager, R.A., Whalin, R.W., Keulegan, G.H., Chatham,

C.E., and Hales, L.Z. (1979), ‘‘Coastal Hydraulic Models,’’ Special Report No. 5, U.S.
Army Waterways Experiment Station, Vicksburg, MS.

Hughes, S.A. (1993), Physical Models and Laboratory Techniques in Coastal Engineering,

World ScientiWc, Singapore.

Iida, K. (1969), ‘‘The Generation of Tsunamis and the Focal Mechanism of Earth
quakes,’’ Tsunamis in the PaciWc Ocean (W.M. Adams, Editor) East–West Center
Press, University of Hawaii, pp. 3–18.

Keulegan, J.H. and Harrison J. (1970), ‘‘Tsunami Refraction Diagrams by Digital Com
puter,’’ Journal, Waterways and Harbors Division, American Society of Civil Engineers,
May, pp. 219–233.

Kyper, T.N. and Sorensen, R.M. (1985), ‘‘The Impact of an Accelerated Sea Level Rise on

Coastal Works at Sea Bright, New Jersey,’’ Fritz Laboratory Report 200.85.905.1,
Lehigh University, Bethlehem, PA.

Macmillan, D.H. (1966), Tides, Elsevier, New York.


-----

Coastal Water Level Fluctuations / 153

Mark, D.J. and ScheVner, N.W. (1993), ‘‘Validation of a Continental Scale Storm Surge

Model for the Coast of Delaware,’’ in Proceedings, Estuarine and Coastal Modeling
Conference, American Society of Civil Engineers, New York, pp. 249–263.

Miles, J.W. (1948), ‘‘Coupling of a Cylindrical Tube to a Half Space,’’ Journal, Acoustic

Society of America, pp. 652–664.

Miles, J.W. (1974), ‘‘Harbor Seiching,’’ Annual Review of Fluid Mechanics, Vol. 6, pp. 17–35.

Patterson, K.R. and Goodyear, H.V. (1964), ‘‘Criteria for a Standard Project Northeaster

for New England North of Cape Cod,’’ National Hurricane Research Project Report
68, U.S. Department of Commerce, Washington, DC.

Pugh, D.T. (1987), Tides, Surges and Mean Sea Level, John Wiley, New York.

Raichlen, F.R. (1966), ‘‘Harbor Resonance,’’ in Estuary and Coastline Hydrodynamics

(A.T. Ippen, Editor), McGraw-Hill, New York, pp. 281–340.

Reid, R.O. and Bodine, B.R. (1968), ‘‘Numerical Model for Storm Surges in Galveston

Bay,’’ Journal, Waterways and Harbors Division, American Society of Civil Engineers,
February, pp. 33–57.

Saville, T. Jr. (1952), ‘‘Wind Set-up and Waves in Shallow Water,’’ Technical Memoran
dum 27, U.S. Army Beach Erosion Board, Washington, DC.

Schwerdt, R.W., Ho, F.P., and Watkins, R.R. (1979), ‘‘Meteorological Criteria for

Standard Project Hurricane and Probable Maximum Hurricane Wind Fields, Gulf
and East Coasts of the United States,’’ NOAA Technical Report NWS 23, U.S.
Department of Commerce, Washington, DC.

Sorensen, R.M. (1991), ‘‘Impact of Expected Climate Change EVects on Coastal Structure

Design,’’ in Proceedings, Coastal Structures and Breakwaters Conference, Thomas
Telford, London, pp. 1–12.

Sorensen, R.M. (1993), Basic Wave Mechanics: for Coastal and Ocean Engineers, John

Wiley, New York.

Sorensen, R.M. and Seelig, W.N. (1976), ‘‘Hydraulics of Great Lakes Inlet-Harbor

Systems,’’ in Proceedings, 15th Conference on Coastal Engineering, American Society
of Civil Engineers, Honolulu, pp. 1646–1665.

Tetra Tech (1981), ‘‘Coastal and Flooding Storm Surge Model,’’ Federal Emergency

Management Agency, Washington, DC.

Thompson, E.F. and Cardone, V.J. (1996), ‘‘Practical Modeling of Hurricane Surface

Wind Fields,’’ Journal, Waterway, Port, Coastal and Ocean Engineering Division,
American Society of Civil Engineers, July/August, pp. 195–205.

U.S. Army Engineer District, New Orleans (1970), ‘‘Report on Hurricane Camille, 14–22

August 1969.’’

U.S. Army Waterways Experiment Station (1975), ‘‘Los Angeles and Long Beack Harbors

Model Study,’’ Technical Report H-75-4 (series of reports by Hydraulics Laboratory
staV), Vicksburg, MS.

U.S. National Research Council (1987), ‘‘Responding to Changes in Sea Level—Engin
eering Implications,’’ National Academy Press, Washington, DC.


-----

154 / Basic Coastal Engineering

Van Dorn, W.G. (1953), ‘‘Wind Stress on an ArtiWcial Pond,’’ Journal of Marine Research,

Vol. 12, pp. 249–276.

Wanstrath, J.J. (1978), ‘‘An Open-Coast Mathematical Storm Surge Model with Coastal

Flooding for Louisiana,’’ Miscellaneous Paper 78–5, U.S. Army Engineer Waterways
Experiment Station, Vicksburg, MS.

Weggel, J.R. and Sorensen, R.M. (1980), ‘‘Surging in the Shark River Boat Basin,’’ in

Proceedings, Ports ’80 Conference, American Society of Civil Engineers, Norfolk, VA.

Wiegel, R.L. (1970), ‘‘Tsunamis,’’ Earthquake Engineering (R.L. Wiegel, Editor), Prentice
Hall, Englewood CliVs, NJ, pp. 253–306.

Wilson, B.W. (1960), ‘‘Note on Surface Wind Stress over Water at Low and High Wind

Speeds,’’ Journal of Geophysical Research, Vol. 65, pp. 3377–3382.

Wilson, B.W. (1972), ‘‘Seiches,’’ Advances in Hydroscience, Vol. 8, Academic Press, New

York, pp. 1–94.

Wilson, B.W. and Torum, A. (1968), ‘‘The Tsunami of the Alaskan Earthquake, 1964:

Engineering Evaluation,’’ Technical Memorandum 25, U.S. Army Coastal Engineering
Research Center, Ft. Belvoir, VA.

Zetler, B.D. (1947), ‘‘Travel Time of Seismic Sea Waves to Honolulu,’’ PaciWc Science,

Vol. 1, pp. 185–188.

5.14 Problems

1. Using the noaa.gov website plot the tide curve for Philadelphia PA and

Trenton NJ for the 24 hour period of your birth date this year. Be sure to note
the appropriate vertical datum for the tide levels. Is this tide closer to being a
spring or a neap tide?

2. Using the noaa.gov website plot the tide at Alcatraz Island and at Sacra
mento for the 24 hours of your birth date this year. Plot both tides on the same
Wgure and explain the diVerences.

3. The tide range measured during a single tidal cycle at an oVshore tower

where the water depth is 100 m is 1.15 m. What maximum water particle velocity
at the sea Xoor would you expect?

4. A tide gage at the end of a pier where the water depth is 6 m measures a tide

range of 1.53 m. What tide range would you expect oVshore of the pier where the
water depth is 110 m? What would the maximum water particle velocity be at the
bottom in the 110 m depth? Mention any assumptions made in your analysis.

5. The tide is propagating up a long straight narrow channel (x-direction)

from the sea. Write the appropriate linearized form of the long wave equations
for this situation. Comment on how you might apply these equations to analyze
the tide in this channel, including what information you would need and the
possibility of neglecting any terms in the equations you presented.


-----

Coastal Water Level Fluctuations / 155

6. Steady uniform Xow occurs in a straight prismatic open channel where

bottom and surface friction can be neglected for the sake of our analysis. Starting
with the long wave equations develop an equation for predicting the water
surface slope normal to the direction of Xow along the channel. Mention any
required assumptions.

7. Over a great circle route between an earthquake epicenter on the coast of

Chile and a coastal location in Hawaii the average depth is 50 fathoms for
150 n.m., 1800 fathoms for 390 n.m., 2200 fathoms for 3870 n.m., and 2800
fathoms for 1260 n.m. Calculate the tsunami travel time between these two
points assuming a path along the great circle route.

8. A tsunami wave has a 0.7 m height in water 2000 m deep. If refraction

causes orthogonal spacing to decrease by a factor of two at a depth of 20 m,
what is the wave energy per foot of crest width at the 20 m depth?

9. Are tsunami waves dispersive? Explain your answer.

10. The bottom proWle at a given coastal site varies linearly from 200 m deep

at a distance of 200 km oVshore to 10 m deep at a distance of 10 km oVshore. If
a tsunami wave reaches the oVshore point at 6:00 a.m. what time will it arrive at
the inshore point? (Note: do not solve this problem by simply assuming an
average depth over the travel path of the tsunami.)

11. The U.S. Army Coastal Engineering Research Center had a wave tank

that was 193 m long, 4.57 m wide, and 6.1 m deep. If the tank is Wlled with fresh
water to a depth of 4 m, calculate the fundamental periods of longitudinal and
lateral resonant oscillations in the tank. Does it appear that these fundamental
modes or their harmonics would cause any diYculty to experimenters who wish
to operate at full-scale wave periods?

12. A two-dimensional closed basin is 30 m long and the depth varies linearly

from 2 m at one end to zero at the other end. Calculate the fundamental period
of oscillation for this basin. (Note: do not simply use the average depth of the
basin to solve this problem.)

13. A rectangular marina with a small opening to the sea has horizontal

dimensions of 100 m by 375 m and a constant depth of 5 m. Estimate the Wve
longest resonant periods and draw plan view diagrams that show the nodal line
patterns for these Wve modes of oscillation. For H ¼ 0:5 m for the longest period
mode, what is the largest horizontal water velocity that would occur in the marina?

14. A bay has the dimensions and depth contours shown. Estimate the funda
mental period of longitudinal free oscillation for this bay. If the jettied entrance is
300 m long, 25 m wide, and 4 m deep, calculate the Helmholtz period.


-----

156 / Basic Coastal Engineering

Sea

2 m

4 m
6 m

Bay

0 1000m

Scale

15. Explain the development of Eqs. (5.20) and (5.21) from basic Froude

number similarity requirements.

16. A 50 knot wind blows to the east along the axis of the bay shown in

Problem 14. Calculate the wind-induced setup at the down wind end.

17. An SPH with Pa ¼ 29:9 inches of mercury, Pe ¼ 27:5 inches of mercury,

and R ¼ 15 n:m: is acting on the bay shown in Problem 14. What is the maximum atmospheric pressure induced setup you would expect to Wnd?

18. Consider a hurricane that travels onshore along a path that is normal to a

straight shoreline. The point of maximum wind velocity is just crossing the
shoreline.

(a) Sketch the surface wind velocity vector pattern.
(b) Show the expected wind stress-induced setup/-down distribution along

the coast.

(c) Show the expected Coriolis-induced setup/-down distribution along the

coast.

(d) Show the expected pressure-induced setup/-down along the coast.

19. A Xat-bottom trough 400 m long and Wlled with water to a depth of 0.3 m

has a freeboard (clearance above the still water line) of 0.05 m. What is the
maximum wind speed along the trough axis that can occur without water spilling
out of the trough at the downwind end? Neglect wind waves.

20. The bottom proWle normal to the shore oV a section of the coast has the

following average depths at the given segment distance lengths: 2.7 m (3 n.m.),
3.8 m (7 n.m.), 4 m (10 n.m.), 11 m (20 n.m.), 12.2 m (30 n.m.), 15.5 m
(40 n.m.), 27 m (50 n.m.), 48 m (60 n.m.), 73 m (70 n.m.), and 200 m

(80 n.m.). There is a sustained wind blowing directly onshore at an average
speed of 72 knots. Calculate the wind-induced setup at the shore.


2 m

4 m
6 m

Bay

0 1000m

Scale


-----

## 6

### Wind-Generated Waves

The most apparent and usually the most important waves in the spectrum of

waves at sea (see Figure 5.2) are those generated by the wind. Wind-generated
waves are much more complex than the simple monochromatic waves considered
to this point. We must brieXy look into how these waves are generated by the
wind and some of the important characteristics that result. It is important to
have a means to quantify wind-generated waves for use in various engineering
analyses. It is also important to be able to predict these waves for a given wind
condition—both wave hindcasts for historic wind conditions and wave forecasts
for predicted impending wind conditions. Finally, we also need to look at
procedures for extreme wave analysis, i.e., to predict those extreme wind-generated wave conditions that will be used as the limit for engineering design.

6.1 Waves at Sea

The record of a water surface time history measured at a point in a storm would
show an irregular trace somewhat similar to that depicted in Figure 6.3. A wave
record taken at the same time at a nearby location would be signiWcantly
diVerent but would have similar statistical properties. The records for a particular area may contain locally generated waves from the existing storm superimposed on lower waves having a diVerent range of periods that were generated by
earlier winds acting at some distant location.

As the wind velocity, distance or fetch over which the wind blows, and/or

duration of the wind increase, the average height and period of the resulting
downwind waves will increase (within limits). For a given wind speed and
unlimited fetch and duration there is a Wxed limit to which the average height
and period can grow. At this limiting condition the rate of energy input to the
waves from the wind is balanced by the rate of energy dissipation because of
wave breaking and surface water turbulence. This condition, which is known as a
fully developed sea, is commonly not reached even in large storms.


-----

158 / Basic Coastal Engineering

Waves that are actively being generated have wave crests that are short and

poorly deWned. These crests are propagating in a range of directions around the
dominant wind direction. As the waves propagate through the area where the
wind is acting, they grow in average height and period. After leaving the area of
active wind generation the surface proWles become smoother and the crests
become longer and more easily recognized. These freely propagating waves are
commonly called swell. As swell propagate their average height decreases somewhat owing to air resistance and internal friction, but more importantly because
of angular speading of the wave Weld. Also, period dispersion occurs, causing the
longer waves to propagate ahead of the shorter waves in the Weld of swell.

McClenan and Harris (1975) conducted a study of aerial photographs of swell

at sea and in the nearshore zone. They found a high incidence of one or more
distinct wave trains having long crests and fairly regular wave periods. In many
photographs they could identify as many as four or Wve distinct wave trains
coming from diVerent directions. In the oVshore region the shorter and steeper
waves were usually most visible. However, the predominant surf zone waves in
the same photograph were the longer swell, not as discernible oVshore, which
undergo the greatest increase in steepness while shoaling. These longer waves
tend to dominate surf zone hydraulic and sediment-transport processes. At some
nearshore locations the large number of wave trains observed is due partly to
reXection and refraction-diVraction eVects that cause a wave train to overlap
itself.

6.2 Wind-Wave Generation and Decay

Wind blowing over the surface of a water body will transfer energy to the water
in the form of a surface current and by generating waves on the water surface.
The initial question is, How does a horizontal wind initiate the formation of
waves on an initially Xat water surface? This process is best explained by a
resonance model proposed by Phillips (1957, 1960). There are turbulent eddies
in the wind Weld that exert a Xuctuating pressure on the water surface. These
pressure Xuctuations vary in magnitude and frequency and they move forward at
a range of speeds. The pressure Xuctuations cause water surface undulations to
develop and grow. The key to their growth is that a resonant interaction occurs
between the forward moving pressure Xuctuations and the free waves that
propagate at the same speed as the pressure Xuctuations.

Although the Phillips model explains the initiation of wave motion, it is

insuYcient to explain the continued growth of the waves. This growth is best
explained by a shear Xow model proposed by Miles (1957). As the wind blows
over a forward moving wave a complex air Xow pattern develops over the wave.
This involves a secondary air circulation that is set up around an axis that is
parallel to the wave crest, by the wind velocity proWle acting over a moving wave


-----

Wind-Generated Waves / 159

surface proWle. Below a point on the velocity proWle where the wind velocity
equals the wave celerity, air Xow is reversed relative to the forward moving wave
proWle. Above this point air Xow is in the direction of the wave motion. This
results in a relative Xow circulation in a vertical plane above the wave surface
that causes a pressure distribution on the surface that is out of phase with the
surface displacement. The result is a momentum transfer to the wave that
selectively ampliWes the steeper waves.

The resonance and shear Xow models both function through pressure forces.

There is also a shear force on the water surface that contributes to growth and
deformation of the wave proWle, but this mechanism is apparently less important
than the pressure mechanisms. There are also complex nonlinear interactions
between waves of one period and waves of a slightly diVerent period. These
wave–wave interactions will cause energy transfer from shorter to longer period
waves under certain conditions.

It is desirable to select a single wave height and period to represent a spectrum

of wind-waves for use in wave prediction, wave climate analysis, design of
coastal structures, and so on. If the wave heights from a wave record are ordered
by size one can deWne a height Hn that is the average of the highest n percent of
the wave heights. For example, H10 is the average height of the highest 10% of
the waves in the record and H100 is the average wave height. The most commonly
used representative wave height is H33, which is the average height of the highest
one-third of the waves. This is commonly called the signiWcant height Hs and it is
approximately the height an experienced observer will report when visually
estimating the height of waves at sea. The highest waves in a wave record are
usually the most signiWcant for coastal design and other concerns. But, as we will
see later, these highest waves tend to have periods that are around the middle of
the range of periods in a wave spectrum. So we most commonly deWne a signiWcant period Ts as the average period of the highest one-third of the waves in the
record.

The signiWcant wave height and period as well as the resulting spectrum of

wind-generated waves depend primarily on the distance over which the wind
blows (known as the fetch length F ), the wind velocity W (commonly measured
at the 10 m elevation), and the duration of the wind td. To a lesser (but in some
situations possibly a signiWcant) extent other factors that aVect the resulting
waves generated by a wind Weld are the fetch width, the water depth and bottom
characteristics if the depth is suYciently shallow, atmospheric stability, and the
temporal and spatial variations in the wind Weld during wave generation.

Waves are generated with propagation directions aligned at a range of oblique

angles (< 908) to the direction of the wind. The range of directions decreases with
an increase in wave period as waves grow while propagating along the fetch.
Thus, the smaller the fetch width the lesser the chance shorter waves have of
remaining in the generating area and growing to appreciable size. The water
depth aVects the wave surface proWle form and water particle kinematics and


-----

160 / Basic Coastal Engineering

thus the transfer of energy from the wind to the waves. Water depth also limits
the non-breaking wave heights. Bottom friction dissipates wave energy and thus
retards the rate of wave growth and the ultimate wave size. Atmospheric stability, which depends on the air/sea temperature ratio, aVects the wind velocity
proWle near the sea surface and the resulting wave generation mechanisms. Wind
Welds grow in size and average velocity, change shape with time, and ultimately
decay. These changes profoundly aVect the resulting wave Weld that is generated.
For some simple applications, however, we consider a wave Weld simply deWned
by a selected constant wind speed and fetch length having a speciWed duration.

It is instructive to consider the growth of the signiWcant height and period as a

function of distance along a fetch for waves generated by a wind of constant
velocity, blowing over a constant fetch and having diVerent durations. This is
demonstrated schematically in Figure 6.1. If the wind duration exceeds the time
required for waves to propagate the entire fetch length (i.e., td > F =Cg) the waves
will grow along OAB and their characteristics at the end of the fetch will depend
on the fetch and the wind velocity. This is known as the ‘‘fetch limited’’ condition.
If the duration is less (i.e., td < F =Cg) wave growth reaches only OAC and wave
generation is ‘‘duration limited.’’ If both the fetch and duration are suYciently
large the curve OAB becomes essentially horizontal at the downwind end and a
fully developed sea has been generated for that wind velocity. Note that as the
waves grow, the component periods and thus the component group celerities
continually increase along the fetch so an average group celerity would have to
be used to determine if waves are fetch or duration limited.

Outside of the region where the wind is blowing the waves propagate as swell.

In this region the signiWcant height will decrease and the signiWcant period will
increase. Energy dissipation and lateral spreading of the waves will decrease the

Generation Decay

W = constant (>0) W = 0

B Ts

Hs

A C

Hs, Ts Duration limited


0


X
F


W = constant (>0) W = 0

B

A C

Duration limited


Figure 6.1. Idealized wave growth and decay for a constant wind velocity.


-----

Wind-Generated Waves / 161

1     5 represent

points at increasing
distances along the
wave fetch


1     5 represent

5

points at increasing
distances along the
wave fetch

4

3

2

1


FREQUENCY


Figure 6.2. Wave spectra growth.

wave height. This eVect is greater for the shorter period waves so the signiWcant
period will increase.


The characteristics of the waves generated by a given wind condition may also

be deWned by a wave spectrum. This is a plot of the wave energy density at each
component period or frequency versus the range of component periods or
frequencies. Figure 6.2 shows a series of typical wave spectra at successive points
along a fetch. Note the decrease in the peak frequency (increase in peak period)
as the wave spectrum grows along the fetch. The total area under the spectral
curve, which is related to the spectral energy and signiWcant wave height, also
grows. The higher frequency (lower period) waves on the right side of a spectrum
grow to an energy level or wave height that is limited by breaking, so as further
growth occurs it must take place at the lower frequencies (higher periods). Also,
wave–wave interactions transfer some wave energy from lower to higher wave
periods as the spectrum grows. If the wave spectra were measured at a Wxed point
in the wind Weld as time elapses, the spectra would exhibit a time-dependent
growth that is similar to the growth pattern depicted in Figure 6.2.


6.3 Wave Record Analysis for Height and Period

Our understanding of wind-generated waves at sea comes largely from the
analysis of wave records. Most of these wave records are point measurements
of the water surface time history for a time period of several minutes. As
indicated above, analysis of wave records is commonly carried out in one of


-----

162 / Basic Coastal Engineering

two ways: (1) by identifying individual waves in the record and statistically
analyzing the heights and periods of these individual waves and (2) by conducting
a Fourier analysis of the wave record to develop the wave spectrum. The former
will be discussed in this section and the latter in the next two sections.


Wave Height Distribution

Figure 6.3 shows a short segment of a typical wave record. A question arises as
to which undulations of the water surface should be considered as waves and
what are the individual heights and periods of these waves. The analysis procedure must be statistically reasonable and consistent. The most commonly used
analysis procedure is the zero-upcrossing method (Pierson, 1954). A mean water
surface elevation is determined and each point where the water surface crosses
this mean elevation in the upward direction is noted (see Figure 6.3). The time
elapsed between consecutive points is a wave period and the maximum vertical
distance between crest and trough is a wave height. Note that some small surface
undulations are not counted as waves so that some higher frequency components
in the wave record are Wltered out. This is not of major concern, since for
engineering purposes our focus is primarily on the larger waves in the spectrum.


A primary concern is the distribution of wave heights in the record. If the wave


heights are plotted as a height–frequency distribution the result would typically
be like Figure 6.4 where p(H) is the frequency or probability of occurrence of the
height H. The shaded area in this Wgure is the upper third of the wave heights and
the related signiWcant wave height is shown.

For engineering purposes it is desirable to have a model for the distribution of


wave heights generated by a storm. Longuet-Higgins (1952) demonstrated that
this distribution is best deWned by a Rayleigh probability distribution. Use of this
distribution requires that the wave spectrum has a single narrow band of frequencies and that the individual waves are randomly distributed. Practically, this
requires that the waves be from a single storm that preferably is some distance
away so that frequency dispersion narrows the band of frequencies recorded.
Comparisons of the Rayleigh distribution with measured wave heights by several

Mean surface

T
elevation

H Time, t

Figure 6.3. Typical water surface elevation versus time record.


Mean surface

T
elevation

H


-----

Wind-Generated Waves / 163


p(H)

H Hs

Figure 6.4. Typical wave height–frequency distribution.

authors (e.g., Goodnight and Russell, 1963; Collins, 1967; Chakrabarti and
Cooley, 1971; Goda 1974; Earle, 1975) indicate that this distribution yields
acceptable results for most storms.

The Rayleigh distribution can be written

2H
p(H) ¼ (6:1)

(Hrms)[2][ e][�][(][H][=][H][rms][)][2]

where the root mean square height Hrms is given by


Hrms ¼


sffiffiffiffiffiffiffiffiffiffiffiffiffiffi

X Hi[2]

N


(6:2)


In Eq. (6.2) Hi are the individual wave heights in a record containing N waves.

Employing the Rayleigh distribution leads to the following useful relation
ships:

Hs ¼ 1:416 Hrms (6:3a)

H100 ¼ 0:886 Hrms (6:3b)

The cumulative probability distribution P(H ) (i.e., the percentage of waves
having a height that is equal to or less than H ) is


P(H)
¼


ðH

o


p(H)dH ¼ 1 � e[�][(][H][=][H][rms][)][2] (6:4)


For our purposes, we are more interested in the percentage of waves that have a
height greater than a given height, i.e.,


-----

164 / Basic Coastal Engineering

1 � P(H) ¼ e[�][(][H][=][H][rms][)][2] (6:5)


Since Hs 1:416Hrms [Eq. (6.3a)]
¼

1 � P(Hs) ¼ e[�][(1][:][416)2] ¼ 0:135


so 13.5% of the waves in a storm wave record might have heights that are greater
than the signiWcant height.

Figure 6.5, which is adapted from the U.S. Army Coastal Engineering Re

search Center (1984), is a plot that is useful when applying the Rayleigh distribution. Line a in the Wgure gives the probability P that any wave height will
exceed the height (H=Hrms) and line b gives the average height of the n highest
fraction of the waves.

0.001


0.005

0.01


0.05

0.1


0.5

1.0


a

b


0.5 1.0 1.2


1.4

1.42


1.6 1.8 2.0 2.2 2.4 2.6

H / Hrms


Figure 6.5. Raleigh distribution for wave heights. (U.S. Army Coastal Engineering

Research Center, 1984.)


Example 6.3–1

A wave record taken during a storm is analyzed by the zero-upcrossing method
and contains 205 waves. The average wave height in the record is 1.72 m. Estimate
Hs, H5, and the number of waves in the record that would exceed 2.5 m height.


-----

Wind-Generated Waves / 165


Solution:

From Eqs. (6.3a) and (6.3b) we have


and


Hrms ¼ 0[1]:[:]886[72] [¼][ 1][:][94 m]

Hs ¼ 1:416(1:94) ¼ 2:75 m


From line b in Figure 6.5 H5=Hrms ¼ 1:98 so

H5 ¼ 1:98(1:94) ¼ 3:84 m

From line a in Figure 6.5 at


H

Hrms



[2][:][5]
¼

1:94 [¼][ 1][:][29]


we have P ¼ 0:19. So the estimated number of waves exceeding 2.5 m in height is
205(0:19) ¼ 38:95, or approximately 39 waves.

When a spectrum of waves reaches the shore, wave breaking causes the wave

height distribution to be truncated at the higher end. Some authors have modiWed the Rayleigh distribution to account for nearshore depth-induced wave
breaking (see Collins, 1970; Ibrageemov, 1973; Kuo and Kuo, 1974; Goda,
1975; Hughes and Borgman, 1987).

Maximum Wave Height

There is no upper limit to the wave heights deWned by the Rayleigh distribution.
In a storm, however, the highest wave that might be expected will depend on the
length of the storm as well as its strength. Longuet-Higgins (1952) demonstrated
that for a storm with a relatively large number of waves N, the expected value of
the height of the highest wave Hmax would be


(6:6)


Hmax ¼ 0:707 Hs


pffiffiffiffiffiffiffiffiffi

ln N


For example, a storm having a 6 hour duration of high waves having an average
period of 8 s would about 2700 waves and Hmax would be 1:99Hs. In the
nearshore zone, the highest wave might be limited by wave breaking, provided
the storm can generate suYciently high waves for this limit to apply in the water
depth of concern. However, in deeper water beyond the depth where waves
would break, the value given by Eq. (6.6) should be appropriate.


-----

166 / Basic Coastal Engineering

Wave Period Distribution

It was mentioned previously that the highest waves and the largest energy
concentration in a wind wave spectrum are typically found at periods around
the middle of the period range of the spectrum. Consequently, for engineering
purposes, we are not usually as concerned with the extreme wave periods as we
were with the higher wave heights.

The joint wave height–period probability distribution is of some interest. The

general shape of this distribution is depicted in Figure 6.6 (see Ochi, 1982). This
Wgure shows the distribution of the wave height versus wave period for each
wave in a typical record, nondimensionalized by dividing each height and period
value by the average height and average period, respectively. The contour lines
are lines of equal probability of occurrence of a height–period combination.

Note, in Figure 6.6, that there is a small range of wave periods for the higher

waves and these periods are around the average period of the spectrum of waves.
For the lower waves (but not the lowest), there is a much wider distribution of
wave periods. The signiWcant period Ts is considered to be more statistically
stable than the average period so it is preferred to use the signiWcant period to
represent a wave record. If one is using a spectral approach to analyzing a wave
record (see the next section) the period of the peak of the spectrum known as the
spectral peak period Tp would be used as a representative period. From investigations of numerous wave records the U.S. Army Coastal Engineering Research Center (1984) recommends the relationship Ts ¼ 0:95 Tp.

2.0

Increasing
probability

H of occurence

H100

1.0

0 1.0 2.0

T/T100

Figure 6.6. Typical dimensionless joint wave height–period distribution.


Increasing
probability
of occurence


-----

Wind-Generated Waves / 167

6.4 Wave Spectral Characteristics

An alternate approach to analyzing a wave record such as that shown in Figure 6.3
is by determining the resulting wave spectrum for that record. A water surface
elevation time history can be reconstructed by adding a large number of component sine waves that have diVerent periods, amplitudes, phase positions, and
propagation directions. A directional wave spectrum is produced when the sum
of the energy density in these component waves at each wave frequency S( f,u) is
plotted versus wave frequency f and direction u. Commonly, one-dimensional
wave spectra are developed when the energy for all directions at a particular
frequency S( f ) is plotted as a function of only wave frequency. An alternate
form to the above described frequency spectrum is the period spectrum where
the wave energy density S( T ) is plotted versus the wave period.

From the small-amplitude wave theory, the energy density in a wave is

rgH[2]=8. Leaving out the product of the Xuid density and the acceleration of
gravity, as is commonly done, leads to the following expression for a directional
wave spectrum:


S( f,u) df du
¼


fX þdf uXþdu

f u


H [2]

(6:7)
8


where H is the height of the component waves making up the spectrum. This
simpliWes to


S( f )df
¼


f þdf
X

f


H [2]

(6:8)
8


for a one-dimensional frequency spectrum. For a one-dimensional period spectrum we have


S(T )dT
¼


TXþdT

T


H [2]

(6:9)
8


It can be shown (see Sorensen, 1993) that the following relationship holds:

S( f ) ¼ S(T )T [2] (6:10)

Equation (6.8) indicates that the dimensions for S(f) would be length squared
times time (e.g., m[2]s) and from Eq. (6.9) the dimensions of S(T) would be length
squared divided by time (e.g., m[2]=S). This is consistent with Eq. (6.10).


-----

168 / Basic Coastal Engineering

The exact scale and shape of a wind wave spectrum will depend on the

generating factors of wind speed, duration, fetch, etc. as discussed above. However, a general form of a spectral model equation is

S( f ) ¼ f[A][5][ e][�][B][=][f][ 4] (6:11)

where A and B adjust the shape and scale of the spectrum and can be written
either as a function of the generating factors or as a function of a representative
wave height and period (e.g., Hs and Ts).

Analysis of a wave record to produce the wave spectrum is a complex matter

that is beyond the scope of this text. Software packages are available for this task
that take a digitized record of the water surface and produce the spectral
analysis. Wilson et al. (1974) discuss spectral analysis procedures and give a list
of basic references on the subject.

An important way to characterize a wave spectrum is by the moments of a

spectrum. The nth moment of a spectrum is deWned as


mn ¼


ð1

0


S( f ) f [n]df (6:12)


So, for example, the zeroth moment would just be the area under the spectral
curve. Since a spectrum plot shows the energy density at each frequency versus
the range of frequencies, the area under the spectral curve is equal to the total
energy density of the wave spectrum (divided by the product of the Xuid density
and acceleration of gravity).

As with the analysis procedures discussed in Section 6.3, it would be useful to

have a representative wave height and period for the wave spectrum that can be
derived from the spectrum. The spectral peak period Tp is a representative period
(or one can use its reciprocal, the spectral peak frequency). The spectral moment
concept is useful to deWne a representative wave height.

From the small-amplitude wave theory, the total energy density is twice the

potential energy density of a wave. Thus,


E� ¼ 2 �Ep ¼ T[2]�


ðT�

0


��

rgh [h] dt

2


where T� is the length of wave record being analyzed and the overbar denotes
energy density. This can be written


E� ¼ rgh�[2] ¼ [r][g][ P][ h][2]

N�


(6:13)


-----

Wind-Generated Waves / 169

where the overbar denotes the average of the sum of N� digitized water surface
elevation values from a wave record of length T�. From our deWnition of Hrms
and Hs the energy density can also be written

E� ¼ [r][gH]rms[2] ¼ [r][gH]s[2] (6:14)

8 16


If the zeroth moment of the spectrum equals the energy density divided by rg,
with Eqs. (6.13) and (6.14) we have


E� ¼ rgmo ¼ rg


P h2

N�


(6:15)


and


E� ¼ rgmo ¼ [r][gH]16 s[2] (6:16)

Equation (6.15) provides a useful way to determine the energy density and the
zeroth moment of a wave spectrum from digitized water surface elevation values.
Equation (6.16) leads to a signiWcant height deWnition from the wave spectrum
energy density or zeroth moment:

Hs ¼ 4pffiffiffiffiffiffimo (6:17)

where the designation Hmo will be used for this deWnition of signiWcant height.
Recall that Hs is based on a wave-by-wave analysis from the wave record, but
Hmo is determined from the energy spectrum or, more basically, from digitized
values of the water surface elevation given by the wave record.

Analysis of the same wave records by the wave-by-wave method and by

spectral analysis indicates that Hs and Hmo are eVectively equal for waves in
deep water that are not too steep. For steeper waves and waves in intermediate
and shallow water Hs will be increasingly larger than Hmo so the two terms
cannot be interchangeably used. Figure 6.7, which was slightly modiWed from
Thompson and Vincent (1985) and is based on Weld and laboratory wave
records, shows how Hs and Hmo compare for diVerent relative water depths.
As wave records become more commonly analyzed by computer the second
deWnition of signiWcant height (Hmo) is more commonly being used.

6.5 Wave Spectral Models

As the Rayleigh distribution is a useful model for the expected distribution of wave
heights from a particular storm, it is also useful to have a model of the expected
wave spectrum generated by a storm. Several one-dimensional wave spectra


-----

170 / Basic Coastal Engineering

1.6

Maximum

1.4 Average

Hs

Hmo

1.2

1.0

Intermediate

0.001 0.01


Maximum

Average

Intermediate Deep


0.1


d/g T[2]p

Figure 6.7. Comparison of Hs and Hmo versus relative depth. (Thompson and Vincent,

1985.)

models have been proposed. They generally have the form of Eq. (6.11) and are
derived from empirical Wts to selected sets of wave measurements, supported by
dimensional and theoretical reasoning. Four of these spectral models–called the
Bretschneider, Pierson–Moskowitz, JONSWAP, and TMA spectra–will be presented. These models are of interest from an historic perspective and because of
their common use in coastal engineering practice. The Wrst three models were developed for deep water waves and the last is adjusted for the eVects of water depth.

Bretschneider Spectrum (Bretschneider, 1959)

The basic form of this spectrum is

S(T) ¼ [a][g][2] (6:18)

(2p)[4][ T] [3][e][�][0][:][675(][gT][=][2][p][WF][2][)][4]

where W is the wind speed at the 10 m elevation and


a ¼ 3:44 [F]1[2]

F2[2]


F1 ¼ [gH]W[100][2] F2 ¼ [gT]2pW[100]

H100 and T100 denote the average wave height and period. The parameters F1 and
F2 are a dimensionless wave height and dimensionless wave period, respectively.


-----

Wind-Generated Waves / 171

As will be shown in the next section, Bretschneider empirically related F1 and

F2 to the wind speed, the fetch, and the wind duration to develop a forecasting
relationship for the average wave height and period and, using Eq. (6.18), the
wave period spectrum.

Inserting a, F1, and F2 into Eq. (6.18) leads to

S(T ) ¼ [3][:][44][T] [3][(][H][100][)][2] e[�][0][:][675(][T][=][T][100][)][4] (6:19)

(T100)[4]

Employing Eq. (6.10), Eq. (6.19) can be converted to a frequency spectrum that
would have the general form of Eq. (6.11). Ochi (1982) recommends the relationship T100 0:77Tp from empirical data and the average wave height can be
¼
related to the signiWcant height through the Rayleigh distribution. Thus, given
one of the common representative wave heights and periods the Bretschenider
spectrum can be plotted using Eq. (6.19).

Pierson–Moskowitz Spectrum (Pierson and Moskowitz, 1964)

The authors analyzed wave and wind records from British weather ships operating in the north Atlantic. They selected records representing essentially fully
developed seas for wind speeds between 20 and 40 knots to produce the following
spectrum:


ag[2]
S( f ) ¼ (6:20)

(2p)[4]f [5][ e][�][0][:][74(][g][=][2][p][Wf][ )][4]

In Eq. (6.20) the wind speed W is measured at an elevation of 19.5 m which
yields a speed that is typically 5% to 10% higher than the speed measured at the
standard elevation of 10 m. The coeYcient a has a value of 8:1 � 10[�][3]. Note that
the fetch and wind duration are not included since this spectrum assumes a fully
developed sea. At much higher wind speeds than the 20 to 40 knot range it is less
likely for a fully developed sea to occur.

The following relationships can be developed from the Pierson–Moskowitz

spectrum formulation (see Ochi, 1982):

Hmo ¼ [0][:][21]g[W][ 2] (6:21)


fp ¼ 2[0]p[:][87]W[g] (6:22)

The simple form of the Pierson–Moskowitz spectrum results in it being used in
some situations where the sea is not fully developed.


-----

172 / Basic Coastal Engineering

JONSWAP (Hasselmann et al., 1973)

This spectrum results from a Joint North Sea Wave Project operated by laboratories from four countries. Wave and wind measurements were taken with
suYcient wind durations to produce a deep water fetch limited model spectrum.
If we eliminate the wind speed from Eq. (6.20) by incorporating Eq. (6.22) the
Pierson–Moskowitz spectrum can be written

ag[2]
S( f ) ¼ (6:23)

(2p)[4]f [5][ e][�][1][:][25(][ f][p][=][f][ )][4]

The JONSWAP spectral form is a modiWcation of Eq. (6.23) by developing
relationships for a and fp in terms of the wind speed and fetch, and enhancing
the peak of the spectrum by a factor g. The resulting spectrum is


ag[2]
S( f ) ¼ (6:24)

(2p)[4]f [5][ e][�][1][:][25(][ f][p][=][f][ )][4][ g][a]


where

a e[�]½ [(][f][ �][f][p][)][2][=][2][s][2][f][ 2]p �
¼

s ¼ 0:07 when f < fp
s ¼ 0:09 when f � fp

In the JONSWAP spectrum, g typically has values ranging from 1.6 to 6 but the
value of 3.3 is recommended for general usage. The coeYcient g is simply the
ratio of S( f ) at the peak frequency for the JONSWAP and Pierson—Moskowitz
spectra. This is depicted in Figure 6.8, which demonstrates the eVect of g on the
spectrum shape.

The coeYcient a and the peak frequency fp for the JONSWAP spectrum are

given by


� gF ��0:22

a ¼ 0:076 W [2]


(6:25)

(6:26)


fp ¼ [3]W[:][5][g]


� gF ��0:33

W [2]


The data used to develop the JONSWAP spectrum were collected for relatively
light wind conditions, but data collected at higher wind velocities (see Rye, 1977)
compared reasonably well with this spectral formulation. Mitsuyasu et al. (1980),
using ocean wave records taken near Japan recommended that a value of g given
by


-----

� gF ��0:143

g 7
¼ W [2]


Wind-Generated Waves / 173

(6:27)


might be used. During recent years the JONSWAP spectrum has become the
most used spectrum for engineering design and for laboratory irregular wave
experiments.

S (f) J

γ = S (fp)J

S (f) S (fp)PM

S (f) PM

fp f

Figure 6.8. JONSWAP and PM spectra comparison.

TMA Spectrum (Bouws et al., 1985)

The previous three models were developed for deep water conditions. As wind
waves propagate into intermediate and shallow depths there is a period-dependent change in the shape of the spectrum versus that for deep water. The TMA
spectrum is a wave spectrum based on the generation of waves in deep water that
then propagate without refracting into intermediate/shallow water depths. The
spectral form is a JONSWAP spectrum modiWed by a depth and frequency
dependent factor F( f, d ). Thus, S( f )TMA ¼ S( f )JF( f, d ) where F( f, d ) is a
relatively complex function deWned graphically in Figure 6.9.

Hughes (1984) further proposed that a and g in the JONSWAP spectral

formulation be modiWed to


S (f) J

γ = S (fp)J

S (fp)PM

S (f) PM


� �0:49

a ¼ 0:0078 [2][p][W][ 2]

gLp


(6:28)


-----

174 / Basic Coastal Engineering

1.0


Φ


0.5


0 0.5 1.0 1.5 2.0

2πf (d/g)[1/2]

Figure 6.9. Correction factor for TMA spectrum.

for the TMA spectrum. In Eqs. (6.28) and (6.29) Lp is the wave length

� �0:39

g ¼ 2:47 [2][p][W][ 2]

gLp


(6:29)


for the spectral peak frequency and the water depth for which the TMA
spectrum is being determined.

Directional Wave Spectra

The components that make up a wave spectrum at a particular location will
typically be propagating in a range of directions. A point measurement of the
water surface elevation time history will not detect this directional variability, so
an analysis of this time history yields a one-dimensional spectrum. But, during
recent years, wave gages that can detect the full directionality of the wave Weld at
a given location have come into more common use. Consequently, directional
spectral data are becoming available and signiWcant development of directional
spectral models has taken place.

The directional spread of wave energy in a wind wave Weld is frequency

dependent. Generally, the short period components of the wave spectrum have
a wider range of directions, while the wave energy is more focused on the
dominant direction for the frequencies near the spectral peak. Models for directional wave spectra commonly are one-dimensional spectra corrected by a factor
that depends on the wave frequency and direction, i.e.,

S( f, u) ¼ S( f )G( f, u) (6:30)


-----

Wind-Generated Waves / 175

where G( f, u) is a dimensionless directional spreading function. Since modifying
a one-dimensional spectrum to a directional spectrum does not change the total
energy density, we have


ðp

�p


G( f, u)du ¼ 1 (6:31)


and


ðp

�p


mo ¼


ð1

o


S( f, u)dudf (6:32)


The angle u is usually measured clockwise starting at zero in the dominant wave
direction and has a practical range of �p=2 to þp=2.

One of the originally proposed (St. Dennis and Pierson, 1953) directional

spreading functions was a simple cosine squared function that is independent
of frequency, i.e.,

G( f, u) ¼ G(u) ¼ [2] (6:33)

p [cos][2][ u]

where u varies from �p=2 to þp=2. The simplicity of this function makes it
appealing for some engineering applications.

A much more complex directional spreading function (Mitsuyasu et al., 1975),

which is based on extensive measurements of directional wave spectra, is


��u

G( f, u) G(s) cos[2][s]
¼
2


(6:34a)


where G(s) is


G(s) [2][2][s][�][1]
¼

p


G[2](s 1)
þ

(6:34b)
G(2s 1)
þ


In the above equations G is the gamma function of the term in parentheses, which
is tabulated in some mathematical handbooks. The parameter s was originally
given as a function of wave frequency, wave peak frequency, and wind speed.
Higher values of s give a more widely spread directional spectrum. Goda and
Suzuki (1975) and Goda (1985) give a simpler deWnition of s that is useful for
engineering applications, i.e.,


s ¼ Smax( f =fp)[5] when f < fp

¼ Smax( f =fp)[�][2][:][5] when f > fp


(6:35)


-----

176 / Basic Coastal Engineering

For design purposes, Goda (1985) recommends

Smax ¼ 10 Wind waves
Smax ¼ 25 Swell with short decay distance
Smax ¼ 75 Swell with long decay distance

As a wind wave spectrum approaches the shore, wave shoaling and refraction
tend to reduce the spread of wave directions which would cause some increase in
Smax. Mitsuyasu et al. (1975) employed Eq. (6.34) with a JONSWAP onedimensional spectrum.

Refraction and DiVraction of Directional Spectra

It is common in much of coastal engineering design to select a representative
wave height, period and direction (e.g. Hmo and Tp having the oVshore direction
that is dominant in the wave spectrum). This wave is then treated as a monochromatic wave which is shoaled, refracted and diVracted (if necessary) to the
point of interest in the nearshore area, employing the methods presented in
Chapters 2, 3 and 4. However, shoaling eVects depend on the wave period, and
refraction and diVraction eVects depend on both the wave period and direction.
Thus, a more complete analysis of the changes that take place as a directional
wave spectrum propagates from oVshore to the coast will be dependent on the
frequency and direction distribution in the oVshore wave spectrum. Each frequency and direction component in the spectrum will shoal, refract and diVract
diVerently. The result will depend on the combination of these components at the
point of interest in the coastal zone.

For a directional wave spectrum the combined shoaling/refraction coeYcient

(Kr)s is given by


where


" 1 X1 Xp #1=2

(Kr)s ¼ (m0)s 0 �p S(f, u)Ks[2][K]r[2][D][f][ D][u]

X1 Xp

(m0)s ¼ S( f, u)Ks[2][D][f][ D][u]

0 �p


In order to apply this equation, the directional spectrum would be broken into
directional and frequency segments (Du and Df). Then, a representative value of f
and u from each frequency/direction segment would be used to shoal and refract
a monochromatic wave to the coast, yielding the Ks and Kr values for that
segment. The results would then be recombined using the above equation to yield
a value of (Kr)s for the directional spectrum. Then,


-----

Wind-Generated Waves / 177

(Hmo)c ¼ (Kr)s(Hmo)o

Where the subscripts c and o refer to the signiWcant wave height at the coastal
point of interest and oVshore

This approach is obviously very onerous to apply in practice, especially if a

signiWcant number of direction/frequency components are to be used. And, it
would have to be repeated in toto for a diVerent nearshore hydrography or a
diVerent oVshore directional wave spectrum.

Goda (1985) employed this procedure to develop results that give some

indication of the diVerence in results for a classic monochromatic wave shoaling/refraction analysis versus a directional spectrum shoaling/refraction analysis.
He considered a coastal area with straight shore-parallel bottom contours. This
greatly simpliWed the shoaling/refraction analysis because the refraction coeYcient for each frequency/direction component could more easily be calculated
from Equations 4.2 and 4.3. Goda employed a modiWed Bretschneider spectrum
with a directional spreading function given by Equation 6.34 and Smax ¼ 10, 25
and 75. Dominant oVshore directions for the directional spectrum included 08,
208, and 408. The nearshore coastal point selected for analysis was the point
where d=Lo 0:05, where Lo is calculated using the peak period for the spec¼
trum.

Goda’s results for (Kr)s as a function of the oVshore direction and Smax, and

the comparative result for KrKs for a monochromatic wave are:

Smax 08 208 408

10 0.94 0.93 0.87

25 0.97 0.955 0.88

75 0.99 0.97 0.90

Monochromatic 1.00 0.98 0.91

For the results shown in the above table (but not necessarily so for all

conditions), the monochromatic refraction/shoaling coeYcient is higher than
the coeYcient for the directional spectrum. The diVerence is generally less than
5 percent. Considering how well other factors such as the eYcacy of the shoaling/
refraction analysis and how well the design wave conditions are known, this
diVerence is not exceptional. As expected, the diVerence between the monochromatic and spectral results diminishes as Smax increases (i.e. as the waves more
closely resemble a monochromatic wave).

An eVective diVraction coeYcient for a directional spectrum (Kd)s is given by


" 1 X1 Xp #1=2

(Kd)s S( f, u)Kd[2][D][f][ D][u]
¼ (m0)s 0 �p


-----

178 / Basic Coastal Engineering

where

(m0)s ¼


X1

0


p
X

�p


S( f, u)Df Du


and Kd is the diVraction coeYcient for each frequency/direction component.

Goda (1985) also compared diVraction analyses for a semi-inWnite breakwater

and a breakwater gap using monochromatic waves versus a directional spectrum
using spectral and directional spreading conditions employed in the shoaling/
refraction analysis comparison. The above equations were used for the directional spectrum analysis.

At a particular point in the lee of the breakwater there was a shift in the

spectral peak frequency away from the incident spectral peak frequency. For
monochromatic waves there is no change in the wave frequency as waves diVract
to the lee of a breakwater. A shift in the spectral peak frequency should be
expected because at a particular point in the lee of the breakwater the value of r/
L and thus Kd would be diVerent for the diVerent frequencies in the spectrum. So
the recombined components then yield a diVerent peak frequency.

Also, at a particular point in the lee of the breakwater, the monochromatic

and spectral diVraction coeYcients were diVerent. In many cases these diVerences were quite signiWcant, with the monochromatic analysis often yielding a
much lower wave height than the spectral analysis at a particular point. As might
be expected, comparison of calculated results with some available Weld data on
diVracted wave conditions behind a breakwater at a coastal port indicated that
the spectral approach gave better results.

6.6 Wave Prediction—Early Methods

Early methods for wave prediction were simple empirical formulations relating
the wave height and period to some representative wind speed, fetch, and later
duration.

Selection of Wind Conditions

Prediction of wind generated waves by the simple empirical methods or by the
use of spectral models requires selection of representative values of wind speed,
fetch, and duration. Winds from more than one approach direction may generate
waves that must be considered for design analysis at a given coastal site. The
fetch may be limited by land boundaries and it may be suYciently short so that
one can assume fetch-limited conditions to make the wave predictions.

The best wind data source would be local speed/direction measurements over a

suYcient length of time to do a return period analysis and select a design wind


-----

Wind-Generated Waves / 179

condition. Typical data sources include airports, Coast Guard stations, and
weather ships at sea. If the data are collected inland a correction may be required
to adjust for the typically higher wind speeds that occur over water. Often,
projects conducted by the Army Corps of Engineers or other government and
private organizations have already collected and analyzed available wind data
for the area of concern.

Return period analyses of available wind data in the United States have been

published by Thom (1960) and the American National Standards Institute
(1972). The primary focus of these data analyses is to provide design speeds
for wind load determination. Thom, for example, presents 2-, 50-, and 100-year
return period isotachs for the continental United States, which allow the selection of a given return period wind speed for a site, but not the wind direction.
The stronger winds may predominantly come from a particular direction that is
not important for wave generation at a given site. If a wind rose, giving the
percentage of higher wind speeds from each compass direction, is available for
the area of interest, Thom’s return period values can be adjusted for direction
(see U.S. Army Coastal Engineering Research Center, 1984).

Wind speed estimates can be made from weather charts showing upper eleva
tion pressure contours, but this requires an extensive eVort to develop suYcient
data to select a design wind condition. So, even if a suYcient number of historic
weather charts are available, this eVort is usually not justiWed for development of
design waves for a single project.

Wind speed measurements may be made at some elevation other than the

standard 10 m elevation. Also, the recorded wind speed values are averages for a
time interval that is typically less than the wind duration required for the waves
to travel the length of the generating fetch (F =Cg). Wind speeds are quite
irregular over time and average values generally decrease as the time over
which the average value is determined increases. Recommended procedures for
correcting for elevation and duration of wind measurement are given in U.S.
Army Coastal Engineering Research Center (1984) and Sorensen (1993).

When wave predictions are being made for lakes or bays with narrow or

irregular shapes, delineation of an eVective fetch length can be diYcult. Procedures for determining a fetch to be used in wave prediction are also discussed in
the two references given in the previous paragraph.

Wave Prediction

Over a century ago simple wave prediction formulas, based on rough observations of wind wave height versus wind speed and fetch, were in use. With the
coming of the Second World War and the need for wave forecasts for amphibious landings, Sverdrup and Munk (1947) developed a more rigorous wave
prediction procedure. This procedure involved relatively simple wave energy
growth concepts with empirical calibration using the small amount of available


-----

180 / Basic Coastal Engineering

data. This procedure was improved by Bretschneider (1952, 1958) over subsequent years by improved calibration using accumulated Weld data sets. The
method is now known as the SMB method after the three authors.


Consider a dimensional analysis of the basic deep water wave prediction

relationship


which leads to


Hs, Ts ¼ f (W, F, td, g)

gHs gTs � gF �

W [2][,] 2pW W [2][,][ gt]W[d]

[¼][ f]


(6:36)


Equation (6.36) simply relates the dimensionless signiWcant wave height and
period to the dimensionless fetch and duration. Either the fetch or the duration
term on the right would control, depending on whether wave generation were
fetch or duration limited. Note that the terms on the left are similar to the terms
presented in Eq. (6.18). Also, since C ¼ gT=2p for deep water waves, the second
term on the lefthand side can be written C/W, a parameter known as the wave
age and important to the understanding of wind wave growth.

Equation (6.36) has been presented in the form of empirical equations and


dimensional plots (see U.S Army coastal Engineering Research Center, 1977).
Figure 6.10 presents the relationship as a dimensionless plot as given by

1


10[-1]

10[-2]


10[-3]

10 10[2] 10[3] 10[4]


gTs/2πW

gHs/W[2]


g F/W[2] (solid), g td/W (dashed)

Figure 6.10. SMB wave prediction curves.


-----

Wind-Generated Waves / 181

Eq. (6.36). The Wgure is based on a large amount of Weld data that are not shown.
These data show a lot of scatter as would be expected for this simple approach
where the wind speed, fetch, and duration are represented by average values.
This should be remembered when Figure 6.10 is used.

Given a value for the dimensionless fetch, the solid lines in Figure 6.10 can be

used to predict the dimensionless signiWcant height and period. This can also be
done using the dimensionless duration and the dashed lines. The smaller sets of
values would indicate whether wave generation is fetch or duration limited and
would yield the predicted signiWcant height and period. Note that the curves in
Figure 6.10 are asymptotic to each other and horizontal lines on the righthand
edge; this limit is the fully developed sea condition.

Example 6.6-1

A deep lake has a wind with an average velocity of 30 m/s blowing over it for a
period of 2 hours. The fetch in the direction of the wind is 20 km. Using the SMB
method, what signiWcant wave height and period will be generated at the downwind end of the lake after two hours?

Solution:

For the given fetch and wind speed

gF

218

W [2][ ¼][ 9][:][81(20,000)](30)[2] ¼


Figure 6.10 then yields

or


gHs gTs

W [2][ ¼][ 0][:][034] 2pW

[¼][ 0][:][33]

Hs ¼ [0][:][034(30)]9:81 [2] ¼ 3:1 m


Ts ¼ [0][:][33(2)]9:81[p][(30)] ¼ 6:4 s

For the given duration and wind speed


gtd 2354

¼

W 30

[¼][ 9][:][81(2)(3600)]


Figure 6.10 then yields


-----

182 / Basic Coastal Engineering

gHs gTs

W [2][ ¼][ 0][:][043] 2pW

[¼][ 0][:][40]


or


Hs ¼ [0][:][043(30)]9:81 [2] ¼ 3:9 m


Ts ¼ [0][:][40(2)]9:81[p][(30)] ¼ 7:7 s

The smaller values, Hs ¼ 3:1 m and Ts ¼ 6:4 s control and wave generation is
fetch limited.

Note, that for


Figure 6.10 yields

or


gHs gTs

W [2][ ¼][ 0][:][034] 2pW

[¼][ 0][:][33]

gtd

W

[¼][ 1750]


td ¼ [1750(30)]9:81 ¼ 5350 s(1:5hours)

Thus, after the wind has blown for about 1.5 hours the waves at the downwind
end of the lake reach their limiting height and period. During the remaining half
hour of wind, wave conditions would remain about the same.

The above discussion applies to deep water wave generation. Occasionally, wave
predictions must be made for shallow water bodies where growth of the waves
rapidly becomes depth limited. Empirical plots and dimensionless equations
using the additional term gd=W [2] (where d is the average water depth) are
presented in U.S. Army Coastal Engineering Research Center (1984) and Sorensen (1993), for shallow water wave prediction. Note that these shallow water
wave predictions relationships are based on a very limited data set and should be
used with some caution.

The circular wind Weld in a hurricane presents a complex condition for

determining the representative wind speed, fetch, and duration. A rough estimate
of the peak signiWcant height and period generated by a hurricane can be made
from empirical equations presented by Bretschneider (1957).


-----

Wind-Generated Waves / 183


� �

Hs ¼ 16:5e[0][:][01][R][D][P] 1 þ [208]pffiffiffiffiffiffiffiffiW[a][V]R[F]

� �

Ts ¼ 8:6e[0][:][005][R][D][P] 1 þ [104]pffiffiffiffiffiffiffiffiW[a][V]R[F]


(6:37)

(6:38)


In Eqs. (6.37) and (6.38), R is the radius (nautical miles) from the hurricane eye to
the point of maximum wind speed WR (knots), DP is the pressure diVerence
from the eye to the periphery of the hurricane (inches of mercury), VF is the
forward speed of the hurricane (knots), and a is a correction factor based on
the forward speed which may be taken as unity for slow moving hurricanes. The
calculated signiWcant height is in feet. The U.S. Army Coastal Engineering
Research Center (1984) has a diagram that predicts the variation of the signiWcant height throughout a hurricane in terms of the peak signiWcant height
which occurs in the vicinity of the point of maximum wind speed.

A more sophisticated parametric model for hurricane wave prediction has

been developed by Young (1988). Predictions are based on an equivalent fetch
and wind speed for a given hurricane that are then used with the JONSWAP
model to make signiWcant wave height and period predictions for the hurricane.
The Bretschneider model was based on 13 hurricanes oV the east coast of the
United States; the Young model was based on 43 Australian hurricanes.

6.7 Wave Prediction—Spectral Models

As previously noted, the Bretschneider spectrum is related to the SMB wave
prediction method. Given the signiWcant wave height and period determined
from SMB, the average wave height and period can be estimated from the
relationships discussed earlier, i.e.,

T100 ¼ 0:77Tp ¼ [0]0[:]:[77]95 [T][s][ ¼][ 0][:][81][T][s]

H100 ¼ 0:886Hrms ¼ [0]1[:]:[886]146 [H][s][ ¼][ 0][:][63][H][s]

and the Bretschneider spectrum can be computed from Eq. (6.19).

The Pierson–Moskowitz spectrum is written directly in terms of the wind

speed. So Hmo, fp, and the spectrum can be directly calculated from Eqs. (6.20)
to (6.22). Remember, the wind speed must be corrected to the slightly higher
value at an elevation of 19.5 m and the Pierson–Moskowitz spectrum applies
only to a fully developed sea condition. [For the 30 m/s wind speed in Example
6.6-1 increased by 10% to give the estimated 19.5 m elevation wind speed, Eq.
(6.23) yields Hmo ¼ 23:3 m and Eq. (6.24) yields Tp ¼ 24:3 s. Thus, the condition
in Example 6.6–1 is much less than the fully developed sea condition.]


-----

184 / Basic Coastal Engineering

The JONSWAP spectrum is based on fetch-limited conditions. Given the

wind speed and fetch length, the wave spectrum peak frequency generated by
this wind condition can be calculated from Eq. (6.26) and the spectrum can be
calculated from Eq. (6.24). Given the wave spectrum, the signiWcant wave height
can be determined using Eq. (6.17) where mo is the area under the spectral
curve.

In the last edition of the Shore Protection Manual (U.S. Army Coastal

Engineering Research Center, 1984), a manual used by the Corps of Engineers
for coastal engineering design, a parametric method based on the JONSWAP
spectrum is recommended for deep water wave prediction. This replaced the
SMB method which was recommended in the previous editions of the manual.
The procedure is developed so that it is applicable to both fetch and duration
limited conditions.

To apply this wave prediction procedure, Wrst determine the adjusted wind

speed WA given by

WA ¼ 0:71W [1][:][23] (6:39)

where WA and W are both in meters per second. Then the signiWcant height and
peak period can be calculated from


gHmo

WA[2]

gTp
WA


� gF �0:5

¼ 0:0016 WA[2]

� gF �0:33

¼ 0:286 WA[2]


(6:40)

(6:41)


The values determined from Eqs. (6.40) and (6.41) use only the wind speed and
fetch and are thus only for the fetch-limited condition. A limiting wind duration
would be calculated from


gtd

WA


� gF �0:66

¼ 68:8 WA[2]


(6:42)


If the actual duration is greater than the duration calculated from Eq. (6.42)
the wind generation process is fetch limited and the results from Eqs. (6.40)
and (6.41) are the predicted signiWcant height and peak period. If the actual
duration is less, the process is duration limited. Using the actual duration,
calculate a new eVective fetch from Eq. (6.42) and, with this new fetch
value, calculate the signiWcant height and peak period from Eqs. (6.40) and
(6.41).


-----

Wind-Generated Waves / 185

Example 6.6-2

For the same condition given in Example 6.6-1, calculate the signiWcant height
and peak period using the SPM-JONSWAP procedure.

Solution:

The adjusted wind speed is

WA ¼ 0:71(30)[1][:][23] ¼ 46:6 m=s

Then, Eqs. (6.40) to (6.42) yield


� �0:5 (46:6)2

Hmo ¼ 0:0016 [9][:][81(20,000)](46:6)[2] 9:81 ¼ 3:4 m


� �0:33 46� :6�

Tp ¼ 0:286 [9][:][81(20,000)](46:6)[2] 9:81


¼ 6:1 s


� �0:66 46� :6�

td ¼ 68:8 [9][:][81(20,000)](46:6)[2] 9:81


¼ 6580 s(1:82 hours)


Since the actual duration is greater than the calculated duration, the wave
generation process is fetch limited and Hmo ¼ 3:4 m, Tp ¼ 6:1 s. These values
are close to the values Hs ¼ 3:1 m and Ts ¼ 6:4 s given by the SMB method and
the process is fetch limited as indicated by that method.

6.8 Numerical Wave Prediction Models

During the past few decades there has been a strong eVort to develop numerical
computer models for wave prediction; these eVorts have recently achieved much
success. Generally, these models are based on a numerical integration over a
spatial grid of the spectral energy balance equation

Sin þ Snl þ Sds ¼ [@][S][(]@[f]t[,][ u][)] þ Cg �rS(f, u) (6:43)


where


r ¼ i [@]

@x [þ][ j][ @]@y


-----

186 / Basic Coastal Engineering

In Eq. (6.43), the lefthand terms give the energy input from the wind Sin, the
nonlinear transfer of energy from one frequency to another by wave–wave
interaction Snl, and the energy dissipation Sds by wave breaking and turbulence
as well as bottom eVects in shallow water. The righthand terms give the resulting
growth of the wave spectrum as a function of time and location. The energy
input term includes the Phillips and Miles mechanisms that were brieXy discussed
in Section 6.2. As the wave Weld grows, the nonlinear transfer term accounts for
the transfer of some energy from the shorter to the longer period components on
the growing face of the spectrum (see Figure 6.2). The growing wave Weld may be
given in terms of S( f, u) or more simply S( f ). In shallower water, propagation of
the spectral components from point to point on the grid may include refraction
and shoaling eVects.

A wide variety of numerical wave prediction models have been developed by

various groups around the world (see The SWAMP Group, 1985 and Komen
et al., 1994). These models generally involve the solution of Eq. (6.43) in Wnite
diVerence form throughout a grid placed over the ocean area where active wave
generation is taking place. As wave generation proceeds, the model computes the
wave spectrum at each grid point and time step. Figure 6.11 shows a typical onedimensional spectrum at a point in time and space along with the frequency
dependent magnitude of each of the terms on the left side of Eq. (6.43). The net
input of energy at any frequency would be given by the algebraic sum of
Sin þ Snl þ Sds.

There are theoretical schemes for computation of each of the three lefthand

input terms in Eq. (6.42). But these theoretical schemes are not complete and,

S( f )

S( f ), S

Snl

Sin

f

Sds

Figure 6.11. Typical energy spectrum and energy input/dissipation distribution at a point

in a numerical wave prediction model.


S( f )

Snl

Sin

f


-----

Wind-Generated Waves / 187

particularly in the case of the nonlinear transfer term, too complex for complete
inclusion in a numerical model. So each of the three terms has been strengthened
and simpliWed by empirical calibration using data from Weld studies. The various
wave prediction models diVer in the Wnal form of these input terms, in whether
the model proceeds from meteorological charts of upper atmospheric isobar
patterns or from surface wind Welds, in the spectral model used to deWne
S( f, u) or S( f ) and the related directional spreading term employed, and in the
formal model solution procedures.

Typically wave prediction model results for a given storm system might be the

directional spectrum or perhaps only Hmo, Tp, and the dominant wave propagation direction, at selected coastal grid points. If the model is run for a given
design storm, this output may be for sequential times during the storm at each
coastal grid point. Or the models may be run from historic weather data to
develop longterm wave statistics for a particular coastal region. An example of
this is Hubertz et al. (1993), who developed wave statistics for 108 locations
along the Atlantic coast of the U.S. and 3 coastal locations in Puerto Rico. Wave
predictions were made for each location at a 3-hour interval for 20 years of
weather data from 1956 to 1975.

These models are continually being improved with much of the improvement

coming from the use of additional Weld data to calibrate model operations and
verify model predictions.

6.9 Extreme Wave Analysis

An investigation of the wave climate for a particular coastal site—by the analysis
of wave measurements and/or wave hindcasts from historic weather data—will
usually provide a wave data set that is of insuYcient length. This record must be
extrapolated to a longer time frame to develop design wave conditions for most
coastal projects.

Our primary concern is to determine the wave height (i.e., Hs or Hmo) at the

site that has a particular recurrence interval or return period Tr. We deWne the
return period as the average number of years during which the speciWed wave
height is expected to occur or be exceeded once. For example, a 25-year return
period means that the speciWed wave height will be expected to occur or be
exceeded once on the average of every 25 years. It has a 4% chance of occurring
any given year. It could happen twice in a given year.

A return period analysis is usually not done for wave period. Extreme wave

heights will usually have a relatively well-deWned range of wave periods that
correlate with the wave heights. The duration of high waves that occur during a
design storm may be of concern since the maximum wave height in a storm
depends, as discussed above, on the duration of the high waves produced by the
storm.


-----

188 / Basic Coastal Engineering

Common return periods for the design of important coastal projects are 50 or

100 years. DiVerent components of a large project may be designed for diVerent
return periods. The selected return period for the design of a coastal structure
depends on the design life of the structure which, in turn, is based on the economic
life and possibly the longer expected physical life of the structure. It may also
depend on the importance of the structure—a structure that is critical to the safety
of human life along the coast my have a design life of 50 years but may be designed
for a much longer return period wave to provide an adequate factor of safety.

Wave Height Return Period Analysis

The data set for a return period analysis might typically be the maximum Hs
recorded every 6 hours or daily for a period of a year or a few years. The basic
approach to conducting the return period analysis is: (1) tabulate the values by
magnitude from the highest value to the lowest, (2) plot the cumulative probability distribution of these heights versus wave height on a graph having a
selected probability distribution; the selected distribution should produce an
essentially straight line plot, and (3) extrapolate this plot [by eye or some
analytical method (see Isaacson and MacKenzie, 1981)] to obtain the wave
height value for the probability or related return period desired. This would
yield the signiWcant wave height for the desired return period. The Rayleigh
distribution can then be used to determine other Hn values for this return period.
If a design wave period is desired, a single period or range of periods common to
the peak values of the wave spectrum can be selected.

There does not appear to be one probability distribution function that uni
versally Wts all long-term wave height data (Ochi, 1982). The usual approach is to
try a number of the commonly used distributions and then use the one giving the
best Wt. The probability distributions in common use are tabulated in Table 6.1
(Isaacson and Mackenzie, 1981). In this table, the general relationship for P(H)
versus H is given with coeYcients a, b, and g that are selected by trial to provide

Table 6.1. Common Probability Distributions

Distribution Cumulative Probability


1 " � �2#

dH

aH [exp][ �][1][=][2 ln (][H]a[)][ �] [b]


Log normal 1
P(H) ¼ pffiffiffiffiffiffi2p


ðH

o


Gumbel P(H) ¼ expn � exp �h �Hb�g�io

Frechet P(H) ¼ exph ���Hb �ai


Weibull P(H) ¼ 1 � exp �h �Hb�g�ai


-----

Wind-Generated Waves / 189

the best straight line Wt to the data. Generally, a is a distribution shape factor, b
controls the spread of the distribution along the H axis, and g locates the central
tendency of the distribution along the H axis. Note that some of the distributions
use only two of the coeYcients.

It is most convenient to plot the data for each of these distributions on graph

paper appropriate for the particular distribution. For example, the log normal
plot could be done on arithmetic–normal probability paper with the P(H) term
plotted on the normal distribution axis and the log of H plotted on the arithmetic
axis. For the other distributions, if appropriate paper is not available, arithmetic
scale graph paper can be used with the following values being plotted:

Gumbel: H versus ln { ln [P(H)]}
� �
Frechet: ln (H)versus ln { ln [P(H)]}
� �
Weibull: ln (H g) versus ln { ln [1 P(H)]}
� � �

Note that for the Weibull distribution a value of g must be assumed before the

plot is made. DiVerent g values can be assumed until the best straight line Wt is
achieved.

The return period is related to the cumulative probability distribution by

Tr 1 (6:44)

r 1 P(H)

[¼] �


where r is the time interval in years between successive data points.

In order to plot the data a value of P(H) or Tr has to be assigned to each of

the tabulated wave heights. The most common approach is to use the following
relationship:

m
P(H) ¼ 1 � (6:45)

N 1
þ


or


Tr (6:46)

r m

[¼][ N][ þ][ 1]

To use Eq. (6.45) or (6.46), tabulate the N values of wave height in order of
decreasing size and assign a sequential value of m to each height where m 1 for
¼
the largest height and m N for the smallest height. Thus, from Eq. (6.46), if data
¼
were collected every day for a period of one year, r ¼ 1=365 ¼ 0:00274 years and
N 365. Then, for the largest wave height in the tabulation of heights, m 1 so
¼ ¼


1
P(H) 1
¼ �

365 1
þ [¼][ 0][:][9973]


-----

190 / Basic Coastal Engineering

and


�365 1�

þ

Tr ¼ 365[1] 1


¼ 1:0027 years


A useful concept, related to return period, is the encounter probability E. This is
the probability that a wave having a return period Tr will be equaled or exceeded
during some other period of time T. If Tr[2][=][T][(][r][)][ �] [1 as is usually the case,]

E ¼ 1 � e[�][T][=][T][r] (6:47)

From Eq. (6.47) a wave with a return period of say 100 years has the following
probability of occurring or being exceeded in any 50 year period:

E ¼ 1 � e[�][50][=][100] ¼ 0:393

Thus, this wave, which has a 2% chance of occurring or being exceeded in any
given year, has a 39.3% chance of occurring or being exceeded in the next 50
years (which could be the project design life).

6.10 Summary

This chapter presents basic concepts concerning the nature of wind-generated
waves and the analysis and prediction of these waves. This, coupled with the
material presented in Chapters 2, 3, 4, and 9 supports the development of the
wave climate for a given coastal location. The next chapter is concerned with
wave forces on coastal structures and coastal structure stability requirements.
The succeeding chapter is concerned with coastal processes and the stability of
shorelines. Both chapters rely heavily on a knowledge of the coastal wave climate
as well as the expected water level Xuctuations that will occur.

6.11 References

American National Standards Institute (1972), ‘‘American National Standard Building

Code Requirements for Minimum Design Loads in Buildings and Other Structures,’’
Publication A58.1, New York.

Bouws, E., Gunther, H., Rosenthal, W., and Vincent, C.L. (1985), ‘‘Similarity of the Wind

Wave Spectrum in Finite Depth Water, Part I—Spectral Form,’’ Journal of Geophysical
Research, Vol. 90, pp. 975–986.

Bretschneider, C.L. (1952), ‘‘Revised Wave Forecasting Relationship,’’ in Proceedings,

2nd Conference on Coastal Engineering, Council on Wave Research, University of
California, Berkeley, pp. 1–5.


-----

Wind-Generated Waves / 191

Bretschneider, C.L. (1957), ‘‘Hurricane Design Wave Practices,’’ Journal, Waterways and

Harbors Division, American Society of Civil Engineers, May, pp. 1–33.

Bretschneider, C.L. (1958), ‘‘Revisions in Wave Forecasting: Deep and Shallow Water,’’

in Proceedings, 6th Conference on Coastal Engineering, Council on Wave Research,
University of California, Berkeley, pp. 1–18.

Bretschneider, C.L. (1959), ‘‘Wave Variability and Wave Spectra for Wind-Generated

Gravity Waves,’’ Technical Memorandum 118, U.S. Army Beach Erosion Board,
Washington, DC.

Chakrabarti, S.K. and Cooley, R.P. (1971), ‘‘Statistical Distribution of Periods and

Heights of Ocean Waves,’’ Journal of Geophysical Research, pp. 1361–1368.

Collins, J.I. (1967), ‘‘Wave Statistics from Hurricane Dora,’’ Journal, Waterways and

Harbors Division, American Society of Civil Engineers, May, pp. 59–77.

Collins, J.I. (1970), ‘‘Probabilities of Breaking Wave Characteristics,’’ in Proceedings, 12th

Conference on Coastal Engineering, American Society of Civil Engineers, Washington,
DC, pp. 399–412.

Earle, M.D. (1975), ‘‘Extreme Wave Conditions During Hurricane Camille,’’ Journal of

Geophysical Research, pp. 377–379.

Goda, Y. (1974), ‘‘Estimation of Wave Statistics from Spectral Information,’’ in Proceed
ings, Ocean Wave Measurement and Analysis Conference, American Society of Civil
Engineers, New Orleans, pp. 320–337.

Goda, Y. (1975), ‘‘Irregular Wave Deformation in the Surf Zone,’’ Coastal Engineering in

Japan, Vol. 18, pp. 13–26.

Goda Y. (1985), Random Seas and the Design of Maritime Structures, University of Tokyo

Press, Tokyo.

Goda, Y. and Suzuki, Y. (1975), ‘‘Computation of Refraction and DiVraction of Sea

Waves with Mitsuyasu’s Directional Spectrum,’’ Technical Note, Port and Harbor
Research Institute, Japan.

Goodnight, R.C. and Russell, T.L. (1963), ‘‘Investigation of the Statistics of Wave

Heights,’’ Journal, Waterways and Harbors Division, American Society of Civil Engineers, May, pp. 29–54.

Hasselmann, K., Barnett, T.P., Bouws, E., Carlson, H., Cartwright, D.E., Enke, K.,

Ewing, J.A., Gienapp, H., Hasselmann, D.E., Kruseman, P., Meerburg, A., Muller,
P., Olbers, D.J., Richter, K., Sell, W., and Walden, H. (1973), ‘‘Measurement of WindWave Growth and Swell Decay During the Joint North Sea Wave Project (JONSWAP),’’ Report, German Hydrographic Institute, Hamburg.

Hubertz, J.M., Brooks, R.M., Brandom, W.A., and Tracey, B.A. (1993), ‘‘Wave Hindcast

Information for the US Atlantic Coast,’’ WIS Report 30, U.S. Army Waterways
Experiment Station, Vicksburg, MS.

Hughes, S.A. (1984), ‘‘The TMA Shallow-Water Spectrum Description and Applica
tions,’’ Technical Report CERC 84–7, U.S. Army Waterways Experiment Station,
Vicksburg, MS.


-----

192 / Basic Coastal Engineering

Hughes, S.A. and Borgman, L.E. (1987), ‘‘Beta-Rayleigh Distribution for Shallow Water

Wave Heights,’’ in Proceedings, Coastal Hydrodynamics 87 Conference, American
Society of Civil Engineers, Newark, DE, pp. 17–31.

Ibrageemov, A.M. (1973), ‘‘Investigation of the Distribution Functions of Wave Param
eters During Their Transformation,’’ Oceanology, pp. 584–589.

Isaacson, M. and MacKenzie, N.G. 1981), ‘‘Long-term Distributions of Ocean Waves,’’

Journal, Waterway, Port, Coastal and Ocean Engineering Division, American Society of
Civil Engineers, May, pp. 93–109.

Komen, G.J., Cavaleri, L., Donelan, M., Hasselmann, K., Hasselmann, S., and Janssen,

P.A.E.M. (1994), The Dynamics and Modeling of Ocean Waves, Cambridge University
Press, Cambridge.

Kuo, C.T. and Kuo, S.T. (1974), ‘‘EVect of Wave Breaking on Statistical Distribution of

Wave Heights,’’ in Proceedings, Civil Engineering in the Oceans III. American Society of
Civil Engineers, San Francisco, pp. 1211–1231.

Longuet-Higgins, M.S. (1952), ‘‘On the Statistical Distribution of the Heights of Sea

Waves,’’ Journal of Marine Research, Vol. 11, pp. 246–266.

McClenan, C.M. and Harris, D.L. (1975), ‘‘The Use of Aerial Photography in the Study

of Wave Characteristics in the Coastal Zone,’’ Technical Memorandum 48, U.S. Army
Coastal Engineering Research Center, Ft. Belvoir, VA.

Miles, J.W. (1957), ‘‘On the Generation of Surface Waves by Shear Flows,’’ Journal of

Fluid Mechanics, Vol. 3, pp. 185–204.

Mitsuyasu, H., Tsai, F., Subara, T., Mizuno, S., Ohkusu, M., Honda, T., and Rikiishi, K.

(1975), ‘‘Observation of the Directional Spectrum of Ocean Waves Using a Cloverleaf
Buoy,’’ Journal of Physical Oceanography, Vol. 5, pp. 750–760.

Mitsuyasu, H., Tsai, F., Subara, T., Mizuno, S., Ohkusu, M., Honda, T., and Rikiishi, K.

(1980), ‘‘Observation of the Power Spectrum of Ocean Waves Using a Cloverleaf
Buoy,’’ Journal of Physical Oceanography, Vol. 10, pp. 286–296.

Ochi, M.K. (1982), ‘‘Stochastic Analysis and Probabilistic Prediction of Random Seas,’’

Advances in Hydroscience, Vol. 13, pp. 218–375.

Phillips, O.M. (1957), ‘‘On the Generation of Waves by Turbulent Winds,’’ Journal of

Fluid Mechanics, Vol. 2, pp. 417–445.

Phillips, O.M. (1960), ‘‘On the Dynamics of Unsteady Gravity Waves of Finite Ampli
tude, 1. The Elementary Interactions,’’ Journal of Fluid Mechanics, Vol. 9, pp. 193–217.

Pierson, W.J. (1954), ‘‘An Interpretation of the Observable Properties of Sea Waves in

Terms of the Energy Spectrum of the Gaussian Record,’’ Transactions of the American
Geophysical Union, Vol. 35, pp. 747–757.

Pierson, W.J. and Moskowitz, L. (1964), ‘‘A Proposed Spectral Form for Fully Developed

Wind Seas Based on the Similarity Theory of S.A. Kitaigorodskii,’’ Journal of Geophysical Research, Vol. 69, pp. 5181–5190.

Rye, H. (1977), ‘‘The Stability of Some Currently Used Wave Parameters,’’ Coastal

Engineering, Vol. 1, March, pp. 17–30.


-----

Wind-Generated Waves / 193

St. Dennis, M. and Pierson, W.J. (1953), ‘‘On the Motions of Ships in Confused Seas,’’

Transactions, Society of Naval Architects and Marine Engineers, Vol. 61, pp. 280–357.

Sorensen, R.M. (1993), Basic Wave Mechanics for Coastal and Ocean Engineers, John

Wiley, NY.

Sverdrup, H.U. and Munk, W.H. (1947), ‘‘Wind, Sea and Swell: Theory of Relations for

Forecasting,’’ Publication 601, U.S. Navy Hydrographic OYce, Washington, DC.

The SWAMP Group, (1985), Ocean Wave Modeling, Plenum Press, New York.

Thom, H.C.S. (1960), ‘‘Distributions of Extreme Winds in the United States,’’ Journal,

Structures Division, American Society of Civil Engineers, April, pp. 11–24.

Thompson, E.F. and Vincent, C.L. (1985), ‘‘SigniWcant Wave Height for Shallow Water

Design,’’ Journal, Waterway Port Coastal and Ocean Engineering Division, American
Society of Civil Engineers, September, pp. 828–842.

U.S. Army Coastal Engineering Research Center (1977), Shore Protection Manual, 3rd

Edition, U.S. Government Printing OYce, Washington, DC.

U.S. Army Coastal Engineering Research Center (1984), Shore Protection Manual, 4th

Edition, U.S. Government Printing OYce, Washington, DC.

Wilson, B.W., Chakrabarti, S.K., and Snider, R.H. (1974), ‘‘Spectrum Analysis of Ocean

Wave Records,’’ in Proceedings, Ocean Wave Measurement and Analysis, American
Society of Civil Engineers, New Orleans, pp. 87–106.

Young, I.R. (1988), ‘‘Parametric Hurricane Wave Prediction Model,’’ Journal, Waterway,

Port, Coastal and Ocean Engineering Division, American Society of Civil Engineers,
September, pp. 637–652.

6.12 Problems

1. Plot the Rayleigh distribution [p(H) vs. H] for storm waves having a

signiWcant height of 4.75 m. Note H100, Hrms, and Hs on the diagram.

2. If the average height in a wave record is 3.5 m and the average period is 6.9 s,

how many waves would exceed 4 m height in a wave record that is 30 min long?

3. For the wave record in Problem 2 estimate H15 and Hmax.
4. A wave forecast yields Hs ¼ 2:7 m and Ts ¼ 6:2 s. In one hour, how many

waves will exceed 3 m in height? What will the maximum wave height be?

5. What percentage of the waves in a Rayleigh distribution will exceed the

average height, the rms height and H10?

6. A 50 knot wind blows for 10 hours out of the east toward Milwaukee. Lake

Michigan is 80 nautical miles wide at this location.

(a) Using the SMB procedure, determine the signiWcant height and period

of waves in deep water just oVshore of Milwaukee.

(b) Plot the Bretschneider spectrum for this wind condition.
(c) A tower is located in water 6 m deep just oVshore of Milwaukee. What is

the highest wave you would expect during the storm at the tower?


-----

194 / Basic Coastal Engineering

7. What is the minimum wind duration that can occur for the wind in

Problem 6 and still generate the same wave conditions?

8. For the wind condition in Problem 6, plot the resulting JONSWAP

spectrum. From this, determine Tp and Hmo.

9. For the wind condition given in Problem 6, plot the Pierson-Moskowitz

spectrum. Comment on the results vis-a`-vis the wind conditions.

10. For the wind condition in Problem 6, determine the resulting signiWcant

height and peak period using the SPM–JONSWAP procedure.

11. For the wave conditions calculated in Problem 6, how long would it take

for waves to propagate across Lake Michigan toward the end of the storm?

12. For a water depth of 20 m and the conditions in Problem 6 plot the TMA

spectrum.

13. Write the Bretschneider spectrum [Eq. (6.19)] as a frequency spectrum.
14. Swell from the South PaciWc arrive at the California coast at the same time

as a local storm is taking place. Sketch the frequency spectrum you would expect
to see at the coast in deep water. Explain.

15. Sketch a typical period spectrum and, on the same diagram, sketch how

the spectrum would look after it passed a submerged barrier. Explain.

16. Consider the L-shaped breakwater given in Problem 4.11. Waves having a

typical frequency spectrum propagate from oVshore past the breakwater tip to
point A. Sketch the spectrum at the tip of the breakwater and at point A on the
same diagram. Comment on the diVerence.

17. Waves from a distant storm are recorded by a wave gage located at the

coast. The average period decreases from 9 s to 6 s in 6 hours. How far away
from the gage were the waves generated?

18. A wave gage is operated oVshore of a potential project site for a period of

one year. Owing to gage problems only 47 weeks of data are collected. The gage
is run for a 30-min period each day and the highest signiWcant height measured
each week is tabulated below (wave heights are in meters):

1.05 1.92 3.72 2.04 2.54 1.47 3.50 0.96 2.54 1.36 1.15 3.05 1.80
1.70 2.05 2.07 2.27 1.39 2.39 2.51 0.82 1.86 2.07 3.07 1.66 3.10
2.94 3.00 1.39 3.11 1.39 1.53 2.37 1.16 2.56 2.84 4.53 3.31 1.58
1.46 2.37 2.26 4.48 1.33 2.53 1.37 3.35

Plot the above data [P(H) versus H] on a Gumbel plot and estimate the 10- and
50-year return period signiWcant wave heights. (Note: Normally all 329 data
points would be used in the analysis; the problem was simpliWed to ease the
reader’s computation eVort.)

19. Given the 50-year return period wave height determined in the previous

problem, what is the chance of this wave height occurring in any 5-year period?


-----

## 7

### Coastal Structures

Structures are constructed along the coast for a variety of purposes. Owing to

its nature, there is strong pressure for development of the land and nearshore
areas along the coast. There is a commensurate need to protect this development
from damage by waves and storm surge. Coastal structures are an important
component in any coastal protection scheme. Structures may be designed to act
directly to control wave and storm surge action or secondarily to stabilize a
beach which, in turn, provides protection to the coast.

Sandy beaches, besides providing for coastal protection, have a signiWcant

recreational value. There is a limited amount of sand available in most coastal
areas and the sand is usually moving along the shore as well as on- and oVshore.
Sand may also be artiWcially placed on the shore to supplement the sand that is
there naturally. Often, structures are required to control where this sand remains
and to protect the beach from losses caused by waves and storm surge.

Navigation and the moorage of vessels are important components of coastal

activities. Coastal structures are important to the establishment of safe and
eYcient navigation channels across the coastline to interior harbor areas. Structures are also important to the development of safe harbor areas on the outer
coast as well as in interior bays and estuaries.

Coastal structures are also constructed for other purposes besides those dis
cussed above. These include pile supported piers that extend seaward from the
shore for Wshing, research and coastal access, pipelines that cross the shore and
nearshore waters for waste disposal and the transport of liquid materials, piles
and other structures that support navigation aids, platforms for oil drilling and
production, and structures to moor vessels oVshore.

There are a variety of structure types that can be constructed to satisfy one or

more of the purposes discussed above. These include:

Long thin cylindrical structures including individual piles and framed structures, pipelines, and cables

Large single-unit submerged and partially submerged structures


-----

196 / Basic Coastal Engineering

Moored Xoating structures

Rubble mound structures, both massive structures and rubble mound veneers
to protect embankments

Vertical-faced rigid structures

Some structures may combine the types mentioned above. An example would be
a vertical faced concrete caisson placed on a submerged rubble mound platform
that provides a stable base against wave attack and bottom scour.

There are two primary concerns in the design of any coastal structure. One is

the structural aspects which address the stability of the structure when exposed
to design hydrodynamic and other loadings. The other is the functional aspects
which focus on the geometry of the structure to see that it satisWes the particular
design function(s) such as keeping the wave heights in the lee of the structure
reduced to an acceptable level or helping to retain a suYciently wide beach at the
desired location. This chapter deals primarily with the Wrst concern, but addresses some aspects of the second concern, which are also covered in the next
chapter.

For rigid structures such as piles, vertical-faced walls, and large submerged

structures, our focus is on determining the loadings on the structure. This
leads to the analysis for design stresses which is a classical civil-structural
engineering concern. On the other hand, for a structure such as a rubble
mound breakwater, our concern is to determine the stone unit size (and related
structure component sizes) required to withstand attack by a given design wave
and water level.

7.1 Hydrodynamic Forces in Unsteady Flow

Water particle motion in a wave is continually unsteady Xow. When this unsteady Xow interacts with a submerged solid body a force is exerted on the body
owing both to the particle Xow velocity and the Xow acceleration.

The Xow velocity causes a drag force Fd to act on the submerged body owing

to frictional shear stress and normal pressure that is typically given by

Fd ¼ [C]2[d] [r][Au][2] (7:1)

For streamlined bodies such as an airfoil, A in Eq. (7.1) would be the surface
area, but for a blunter body (e.g., circular and rectangular cross-sections) A is the
cross-sectional area projected in the direction of Xow. In Eq. (7.1) u is the Xow
velocity approaching the body, r is the Xuid density, and Cd is a drag coeYcient
that depends on the body’s shape, orientation to Xow, surface roughness, and the
Xow Reynolds number.


-----

Coastal Structures / 197

For a circular cylinder the Reynolds number R ¼ uD=v where D is the cylinder

diameter and v is the Xuid kinematic viscosity. For a given body shape, orientation, and surface roughness the drag coeYcient depends primarily on the Reynolds number. This dependence has been determined experimentally for a variety
of body shapes and typical values are presented in most Xuid mechanics texts.
Hoerner (1965) gives a thorough compilation of drag coeYcients and related
information for various shapes.

When Xow accelerates past a body the Xow velocity and thus the Reynolds

number and to some extent the drag coeYcient are continually changing. Thus,
since u and Cd are both variable in accelerating Xow the drag force (Eq. 7.1) can
vary signiWcantly. Consider a wave passing a vertical cylindrical pile. The water
particle velocity at any point on the pile continually changes with time and at a
given instant the particle velocity varies along the pile. This produces a very
complex drag force pattern on the pile.

The accelerating Xow causes an additional force on the submerged body beside

that given by Eq. (7.1). This acceleration or inertial force has two components.
One component arises because an accelerating Xow Weld must have a pressure
gradient to cause the Xow to accelerate. This pressure gradient causes a variable
pressure around the body’s surface which produces a net force on the body. Also,
when Xow accelerates past a body an added mass of Xuid is set into motion by the
body. (If, for example, a body that is initially at rest in a still Xuid is accelerated to
some particular velocity, the surrounding Xuid that was initially still is also set into
motion. A force is required to accelerate that additional mass of Xuid. Conversely,
when Xow accelerates past a still body there is an added mass that produces a force
on the body.) This second component of inertial force is a function of the Xuid
density and acceleration, and the body shape and volume.

Thus, when there is unsteady Xow, the total instantaneous hydrodynamic

force F on the body can be written


F [C][d]
¼

2 [r][Au][2][ þ]


ð


A


pxdA þ krV [du] (7:2)

dt


The second term on the right, where px is the pressure acting on the body in the
Xow direction and dA is the diVerential area on which the pressure acts, is the
inertial force owing to the accelerating Xow Weld pressure gradient. The third
term on the right is the added mass term. In this term V is the volume of Xuid
displaced by the body so rV would be the displaced Xuid mass. The dimensionless coeYcient k is the ratio of a hypothetical Xuid mass having an acceleration du/dt to the actual mass of Xuid set in motion (by the body) at its true
acceleration.

The pressure Weld term in Eq. (7.2) can be written in a more usable form by

realizing that this pressure Weld creates a force that is capable of accelerating a
mass of Xuid having the same volume as the body but at a rate du/dt. Thus,


-----

198 / Basic Coastal Engineering

So Eq. (7.2) becomes


ð


A


pxdA ¼ rV [du]

dt


F ¼ [C][d] (7:3)

2 [r][Au][2][ þ][ (1][ þ][ k][)][r][V du]dt

In potential Xow, k has the values given below for various shapes and Xow
orientations:

Sphere k ¼ 0:50

Cube-Xow normal to a side k ¼ 0:67

Circular cylinder-Xow normal to axis k ¼ 1:00

Square cylinder-Xow normal to axis k ¼ 1:20

Additional k values can be obtained from Sarpkaya and Isaacson (1981). In a real
Xuid, Xow patterns past the body and thus the value of k would also depend on the
body’s surface roughness, the Reynolds number, and the past history of the Xow.

Typically, 1 þ k is called the coeYcient of mass or inertia Cm and Eq. (7.3) is

written

F ¼ [C][d] (7:4)

2 [r][Au][2][ þ][ C][m][r][V du]dt

Thus, for potential Xow past a circular cylinder Cm ¼ 2:0, but for real Xow past this
cylinder Cm values less than 2.0 are common. Equation (7.4), when applied to wave
forces on submerged structures, is commonly called the Morison equation after
Morison et al. (1950), who Wrst applied it to the study of wave forces on piles. For
an in-depth discussion of the Morison equation see Sarpkaya and Isaacson (1981).

It is important to note that the application of Eq. (7.4) to determining wave

forces on submerged structures requires that the structure be small compared to
the wave particle orbit dimension so that the assumed Xow Weld past the structure is reasonably valid (see Section 7.3). Also, if the submerged structure
extends up to near or through the water surface, wave-induced Xow past the
structure will generate surface waves which cause an additional force on the
structure not given by the Morison equation.

7.2 Piles, Pipelines, and Cables

Marine piles, pipelines, and cables constitute a class of long cylindrical structures
that must be designed to withstand the unsteady Xow forces from wave action.
There may also be steady current-induced drag forces on these structures.
Electrical cables laid along the sea Xoor are somewhat similar to underwater
pipelines from the stability point of view, but cables are typically less than 15 cm
in diameter while some pipelines such as municipal waste outfall lines can be up


-----

Coastal Structures / 199

to 3 m in diameter. Marine cables are also used to moor ships, buoys, and
Xoating breakwaters. Piles for piers, oVshore drilling structures, dolphins, and
navigation aids are usually vertical or near vertical, but some of these structures
can have horizontal and inclined cylindrical members for cross bracing. Pile
diameters can vary from less than a meter for piers up to a few meters for the
legs of some deep water oil drilling structures.


For a circular cylinder with its axis oriented in a horizontal y or vertical z


direction and wave propagation normal to the axis, the force Fs per elemental
length ds of the cylinder can be written

� � @u

Fs ¼ ds[F] [¼][ C]2[d] [r][Du][2][ þ][ C][m][r][ p]4[D][2] @t (7:5)


The particle velocity u would be given by Eq. (2.21), and the local acceleration [@]@[u]t

given by Eq. (2.23) is used in place of the total acceleration du/dt. Use of the local
acceleration yields reasonable results for most cases but particularly for waves of
low steepness in deeper water. Note that the u[2] term should be computed as u u .
j j

The water particle acceleration lags the particle velocity by 908 so the drag Fd

and inertia Fi components of Fs at a given point along the cylinder will vary
through the wave cycle as shown in Figure 7.1. To construct Figure 7.1 it was
assumed that Cd and Cm remain constant through the wave cycle and structure/
wave conditions are such as to cause the peak inertia and drag forces to be equal.
In any given wave/structure situation the peak total force occurs at some point

_Fs=Fd + Fi_


kx
0 π 2π

Figure 7.1. Surface elevation and drag, inertia, and total forces versus phase position—

for equal peak drag and inertia components.


_Fs=Fd + Fi_

_Fd_ _Fi_

η

0 π 2π


-----

200 / Basic Coastal Engineering

along the wave between the wave crest or trough and the still water line, the exact
position depending on the values of Cd and Cm, the wave height and period, the
water depth, and the cylinder diameter. At the wave crest and trough the total
force is all drag force and at the still water positions along the wave the total
force is all inertia force.

Inserting the relationships for wave particle velocity and acceleration into Eq.

(7.4), diVerentiating F with respect to the phase (kx st), and setting the result
�
equal to zero yields

sin (kx)p ¼ Cd AH2Cm coshV sinh k( kdd þ z) (7:6)

where time is set to zero so (kx)p represents the position along the wave where the
peak force occurs.

Equation (7.6) also indicates the relative magnitudes of the drag and inertia

components of the total force. If the drag component is larger the total peak
force occurs closer to the wave crest and trough, and if the inertia component is
larger the total peak force occurs near the still water line position on the wave.

Since the volume of the cylindrical segment is a function of D[2] whereas the

projected area of the segment is only a function of D, Eq. (7.6) shows that the
ratio D/H indicates where along a wave the peak force will occur and the relative
size of the drag and inertia force components. For a given wave, as the structure
size increases the inertia force tends to become more dominant and vice versa.
For common wave conditions, the total wave force on cables is essentially all
drag force whereas the total force on large structures such as submerged oil
storage tanks is eVectively due solely to inertia eVects. For piles either component may dominate, with drag forces being largest at lower D/H ratios and vice
versa.

Often, structures are attacked simultaneously by waves and a current moving

at some angle to the direction of wave propagation. The total drag force on the
structure is due to the combined eVects of the current and wave particle velocities. The wave characteristics are somewhat modiWed by the current, so the exact
nature of the resulting force on a cylinder is diYcult to determine. The usual
design procedure is to vectorally add the current and wave particle velocities and
use the resulting velocity component in the drag term of the Morison equation.

It was indicated in the previous section that the drag and inertia coeYcients

are generally a function of the structure shape, orientation to Xow, and surface
roughness, as well as the Reynolds number and the prior history of the Xow. For
cylindrical structures in waves it is common to introduce another independent
parameter X/D where X is the distance that a particle moves as it passes the
cylinder, i.e., essentially the particle orbit diameter normal to the cylinder axis.
This parameter indicates how well the Xow Weld develops around the structure in
the wave-induced reversing Xow past the structure.


-----

Coastal Structures / 201

The particle Xow velocity in a wave at the structure can be represented by

� �

u ¼ um sin [2][p][t]

T


where um is the maximum horizontal particle velocity (i.e., u under the wave
crest). Then X equals the average Xow velocity past the structure times the
wave period or

�um �

X T
¼
2p


so


X
D 2p

[¼][ 1]


�umT�

D


The term in parentheses (umT=D) is known as the Keulegan–Carpenter number
KC, which is proportional to X/D and is also commonly used in deWning values
of Cd and Cm.

Note that since um is proportional to pH=T, KC is inversely proportional to

D/H so either KC or D/H has been used in drag and inertia coeYcient investigations. Generally, for KC > 25 drag forces dominate and for KC < 5 inertia
forces dominate.

Most pile and pipeline structures will have several modes of resonant oscilla
tion that may be excited by wave action. This may come about by one of the
resonant modes being approximately equal to the incident wave period. Or, if H/
D is suYciently large so Xow adequately envelops a structure a vortex Weld may
develop in the lee of the structure and cause oscillatory forces that act normal to
the direction of Xow. The frequency of the vortices shed by the structure may
also excite a resonant mode of the structure. The period of vortex shedding Te is
given by the Strouhal number:

S [D]
¼

Teu


where u is the Xow velocity past the structure having a diameter D. S for
the common range of prototype pile Reynolds numbers varies from 0.2 to 0.4.
For example, given typical values of D ¼ 1:0 m, u ¼ 1:5 m=s, and

S ¼ 0:3, Te ¼ 2:2 s. Thus, with an incident wave period that is signiWcantly
greater than 2.2 s, Xow past a pile could last long enough for a few cycles of
vortex shedding to occur.


-----

202 / Basic Coastal Engineering

Piles

Equation (7.5) gives the force per unit length acting on a cylinder. This can be
integrated from the mud line to the water surface to obtain the total force on a
vertical circular cylindrical pile as a function of time, i.e.,


F
¼


ðh

�d


�C2d [r][Du][2][ þ][ C][m][r p]4[D][2] @@ut�


dz


where dz is a unit length of the pile. If we assume that Cd and Cm are constant, that
the water particle velocity and acceleration are given by the small-amplitude wave
theory, that the integration is carried out up to the mean water surface elevation,
and that the pile location is conveniently taken to be at x 0, the integration yields
¼


F [C][d]
¼

8 [r][gD H] [2][n][ cos][2][ (][ �] [s][t][)]

þ Cmrg [p][D][2] H tanh kd sin ( � st)

8


(7:7)


where n is the ratio of the group to phase celerities. Note that cos[2] ( st) should
�
be computed as cos ( st) cos (st) . This wave-induced force causes a moment
� j � j
on the pile around the mudline given by


M
¼


h
Z

�d


�Cd @u�(d z)dz

þ

2 [r][Du][2][ þ][ C][m][r p][D]4 [2] @t


Integration, with the same assumptions yields

� �1 ��

M [C][d]
¼

8 [r][gDH] [2][n][ cos][2][ (][ �] [s][t][)][d][ 1]2 2n 2 2kd sinh 2kd

[þ][ 1] [þ] [þ][ 1][ �] [cosh 2][kd]

(7:8)

[C][m] � �
þ

8 [r][g][p][D][2][ Hd][ tanh][ kd][ sin (][ �] [s][t][) 1][ þ][ 1]kd[ �] sinh[cosh] kd[ kd]


Equations (7.7) and (7.8) yield the force and moment as a function of time. The
peak force and moment will occur at some point along the wave depending on
the wave and pile characteristics, as discussed above. A procedure for the direct
determination of the peak force and moment is given by the U.S. Army Coastal
Engineering Research Center (1984). This peak force and moment procedure
also employs Dean’s stream function wave theory rather than the small-amplitude wave theory because, for most design situations, waves of great height are
being employed as the design wave. Note that the drag and inertia terms in the
moment equation are simply the drag and inertia forces times the water depth


-----

Coastal Structures / 203

times the term in brackets. The term in brackets is simply the fraction of the
depth up from the mudline at which the force acts.

An important aspect of the calculation of wave forces and moments on a pile is

the selection of values for Cd and Cm. One could use the theoretical value of 2.0
for Cm and, after calculating a Reynolds number using some representative water
particle velocity, determine Cd from a typical steady Xow plot of drag coeYcient
versus Reynolds number. Remember that Cd and Cm vary both with depth at an
instant and with time throughout the wave cycle. The value selected for use in
Eqs. (7.7) and (7.8) should provide results that are representative of peak load
and moment conditions.

A number of experiments have been conducted both in laboratory wave tanks

and in the Weld to determine design values for the drag and mass coeYcients. In
the laboratory either monochromatic or spectral waves can be used and wave
characteristics can be controlled to yield results for the desired range of wave
conditions. Also, the experimental setup, which usually involves a wave gage to
measure the incident wave and an instrumented pile to measure the timedependent wave loading, is easier to install, access, and control. However, a
major drawback to laboratory experiments is that they must generally be
conducted at reduced scale so Reynolds numbers are usually orders of magnitude smaller than those found in the Weld. Field experiments are much more
diYcult and expensive to carry out and there is no control over the incident
wave conditions that will occur. Also, particularly for the larger waves, the
wave conditions will be quite irregular and currents may also be acting on the
pile.

By either approach, when a record of the water surface time history and the

resulting time-dependent load on the pile as a wave passes are obtained, a very
serious problem arises as to how to evaluate these data to determine drag and
mass coeYcients. Particle velocities and accelerations are needed to employ the
Morison equation to determine Cd and Cm. So a wave theory must be selected to
calculate particle velocities and accelerations from the wave record. DiVerent
theories, as we have seen, yield diVerent results so the resulting values obtained
are dependent on the wave theory used.

Given a wave record, an associated wave load record, and a selected wave

theory for calculating particle velocities and accelerations, a variety of approaches have been used to determine Cd and Cm values, i.e.

1. At the wave crest and trough the total force is all drag force (see Figure 7.1)

so this value can be used to directly determine a value for the drag
coeYcient from the drag term in the Morison equation. The measured
force, when the wave is at the still water line, is all inertia force so this
condition can be used in turn to determine the coeYcient of mass from the
inertia term in the Morison equation.


-----

204 / Basic Coastal Engineering

2. The Morison equation can be used at any two points along the wave record

such as the points of maximum and zero force to solve for Cd and Cm from
two simultaneous equations.

3. A least-squares Wtting procedure can be employed with the Morison equa
tion serving as the regression relationship. The value


1

T�


Z T�

o


� @u�

F
� [C]2[d] [r][Du][2][ �] [C][m][r p][D]4 [2] @t


dt


is minimized where T� is the length of the wave and wave force records, F is the
time-dependent measured wave force, and the particle velocity and acceleration
at each point along the record are calculated from the measured wave proWle.
This would yield best Wt values of Cd and Cm for the entire wave and wave force
records.

The results of many of these Weld and laboratory experiments are referenced in

Woodward–Clyde Consultants (1980), Sarpkaya and Isaacson (1981), and U.S.
Army Coastal Engineering Research Center (1984). These results typically show
a great deal of scatter in the resulting drag and mass coeYcient values. Based on
evaluations of the available laboratory and Weld experimental results Hogben
et al. (1977) and U.S. Army Coastal Engineering Research Center (1984) have
recommended design values for Cd and Cm. For the latter, a Reynolds number R
is calculated using the maximum water particle velocity in the wave (i.e., at the
crest and water surface). Then for:

R < 10[5], Cd ¼ 1:2

R between 10[5] and 4 � 10[5],Cd decreases from 1.2 to 0.6–0.7

R > 4 � 10[5], Cd ¼ 0:6---0:7

R < 2:5 � 10[5], Cm ¼ 2:0

R between2:5 � 10[5]and5 � 10[5], Cm ¼ 2:5---R=5 � 10[5]

R > 5 � 10[5], Cm ¼ 1:5

The Wnal values selected for design will also depend on the conWdence the
designer has in the selected design wave and the related factor of safety desired.


-----

Coastal Structures / 205

Example 7.2-1

A vertical cylindrical pile having a diameter of 0.3 m is installed in water that is
8 m deep. For an incident wave having a height of 2 m and a period of 7 s,
determine the horizontal force on the pile and the moment around the mudline
when the pile is situated at the halfway point between the crest and still water line
of the passing wave.

Solution:

For T ¼ 7 s, Lo ¼ 9:81(7)[2]=2p ¼ 76:5 m. Then, by trial we can solve Eq. (2.18)
for the wave length at a water depth of 8 m


L

76:5 [¼][ tanh 2][p]L[(8)]

yielding L ¼ 55:2 m and k ¼ 2p=55:2 ¼ 0:1138.

Then, from Eq. (2.21) the maximum horizontal particle velocity is


u [p][(2)]
¼

7

and the Reynolds number is


cosh (0:1138)(8)

sinh (0:1138)(8) [(1)][ ¼][ 1][:][24 m][=][s]


1:24 (0:3)
R
¼

0:93 � 10[�][6][ ¼][ 4][ �] [10][5]

Using the recommended values for Cd and Cm given above yields

Cd ¼ 0:72

Cm ¼ 1:8

From Eq. (2.38)


� 2(0:1138)8 �

n [1] 1
¼ þ

2 sinh 2(0:1138)8


¼ 0:803


We can now calculate the force and moment from Eqs. (7.7) and (7.8) where for
our point along the wave st ¼ 3p=4. From Eq. (7.7)

F ¼ [0][:][72] (9810)(0:3)(2)[2](0:803)(0:707)[2]

8

þ [1][:][8(9810)][p][(0][:][3)][2][(2)] (0:7213)(0:707) ¼ 851 þ 637 ¼ 1488 N

8


-----

206 / Basic Coastal Engineering

and, from Eq. (7.8)

� 1 �1 1 � 3:169 ��

M 851(8) [1]
¼

2 [þ] 2(0:803) 2 [þ] 2(0:1138)8(3:007)

� 1 � 1:444 �

637(8) 1 6550Nm
þ � ¼

(0:1138)8(1:041)


The force calculation shows that the drag and inertia components of the wave
force are about equal at the point considered so the plot of forces would be
somewhat similar to that shown in Figure 7.1, indicating that the calculated force
is approximately the maximum force on the pile. To determine the actual
maximum force one would have to calculate the force for several points along
the wave and interpolate (or use the procedure given in the U.S. Army Coastal
Engineering Research Center (1984)).
The total force at the instant being considered would act at 6550Nm=1488N
¼ 4:40 m up from the mudline.

Marine growth on a pile will increase the eVective diameter of the pile and may

signiWcantly increase the surface roughness. Increased surface roughness will
aVect the drag and inertia coeYcients, particularly for the range of Reynolds
numbers common to Weld conditions. There are little data to indicate the
expected change in Cd or Cm as a function of surface roughness for Weld design
conditions. Blumberg and Rigg (1961) evaluated Cd for a 3-ft diameter cylinder
having varying surface roughnesses and towed through water at a constant
velocity. Reynolds numbers for the experiments varied between 1 10[6] and
�
6 � 10[6]. Cd was generally independent of Reynolds number as would be expected
at these high Reynolds number values, but generally increased from 0.58 for a
smooth cylinder to 1.02 for the roughest cylinder having oyster shells and
concrete fragments in bitumastic on the surface. This indicates that the drag
coeYcients recommended above should be increased if excessive marine growth
is expected over much of a pile length.

Other concerns that may arise concerning the analysis of wave forces on piles

include: expected loadings on pile groups in suYcient proximity to cause Xow
interactions between the piles, broken wave forces on piles in both deep water
and the surf zone, and forces on noncircular cylindrical piles. Discussion of these
concerns may be found in Sarpkaya and Isaacson (1981) and the U.S. Army
Coastal Engineering Research Center (1984).

Pipelines

If possible, particularly in shallow water and across the surf zone, pipelines
should be buried below the ocean bottom to avoid damage from waves and
currents as well as from dragging ship anchors, Wshing trawls, etc. An alternative


-----

Coastal Structures / 207

is to lay the pipeline on the bottom and cover it with a layer of stone or one of a
variety of commercially available mattresses (see Herbich, 1981). For Wrm bottoms where it is not economical to bury or cover the pipeline it may be anchored
to the bottom with commercially available screw anchors placed at set intervals
along the pipeline. Or weights (made of concrete or other materials) may be
attached to the pipeline at set intervals to anchor it in place. During storms waveand current-induced water motion may expose a buried pipeline or scour out the
sea Xoor below a pipeline that is anchored to the bottom.

If a pipeline is carrying a lower density liquid (e.g., fresh water sewage being

discharged through a marine outfall into the ocean) or if there is air in the
pipeline, it will have a buoyant force that must be overcome by the weight of
the pipeline and any anchors. Currents and wave-induced Xow normal to the axis
of a pipeline will cause a lift force on the pipeline owing to the asymmetry of Xow
around the pipeline sitting on the bottom. Currents and waves will also cause
horizontal drag and inertia forces on the pipeline in the direction of current or
wave propagation. Bottom friction between the pipeline and sea Xoor will resist
horizontal forces acting on the pipeline.

The design of a pipeline sitting on the sea Xoor and relying on weight or screw

anchors for stability must include a stability analysis to ensure that the pipeline
will be stable for the expected design wave and current conditions and possible
bottom scour conditions that may occur. This analysis requires selection of a
bottom friction coeYcient (Lyons, 1973) and lift, drag, and inertia coeYcients
for determination of the wave and current-induced forces. The lift force would be
determined from an equation similar to the drag equation [Eq. (7.1)] with a lift
coeYcient Cl in place of Cd . Horizontal wave and current forces would be
determined from the Morison equation. A static force analysis will indicate
whether the pipeline is prone to sliding along the sea Xoor for the design wave
and current conditions.

Ifthe pipelineisraisedfromthe bottom,theverticalasymmetryof Xowdecreases

as does the resulting lift force. When the clearance between the pipeline and the
ocean bottom is about 0.5 diameters, the lift force usually becomes very small.

A variety of studies of the hydrodynamic forces acting on sea Xoor pipelines

have been conducted both for steady Xow in Xumes and for wave action in wave
tanks (Brown, 1967; Beattie et al., 1971; HelWnstine and Shupe, 1972; Brater and
Wallace, 1972; Grace and Nicinski, 1976; Parker and Herbich, 1978; Knoll and
Herbich, 1980). For summary discussions of these investigations see Grace (1978)
and Herbich (1981), who also discuss various other aspects of marine pipeline
design. These references allow the selection of Cd, Cl, and Cm for the given
pipeline condition. Grace (1971), based on the available literature and wave
tank studies, recommends as conservative design values that Cd ¼ 2:0,Cl ¼ 3:0,
and Cm 2:5 for a pipeline on the seaXoor. He recommends that Cd remain
¼
constant for any spacing between the pipeline and ocean Xoor, Cl should diminish
to about 0.9 as the spacing approaches half the pipe diameter, and Cm should


-----

208 / Basic Coastal Engineering

‘‘drop oV ’’ as the spacing increases. These recommendations are quite conservative. Depending on the conservatism desired in the design the reader should
consult the above listed references and adjust the coeYcient values accordingly.

Example 7.2-2

A 0.61 m outside diameter pipeline is sitting on the sea Xoor and has fresh water
with no air pockets within. The pipe is plastic with an inside diameter of 0.53 m
and a weight of 613 N per meter of length in air. Square concrete collar anchors
are attached to the pipeline every 3 meters and each collar weighs 10 kN in air.
What is the allowable current velocity acting normal to the axis of the pipeline if
the pipeline is to be stable against sliding along the sea Xoor? Assume that the
speciWc gravity of sea water is 1.025 and concrete is 2.40.

Solution:

The total submerged pipe weight in seawater is:


" #

613 [p][(0][:][53)][2] (9870)
þ

4


� [p][(0][:][61)][2] (9870)(1:025) ¼ �167 N=m

4


So, without the collars the pipe would Xoat to the surface.

The submerged weight of the collars is:

10,000

� [10,000(9870)(1][:][025)] ¼ 1910 N=m
3 (2:4)(9870)(3)


Thus, the submerged weight of the system is 1910 � 167 ¼ 1743 N=m.

From Lyons (1973) for a sandy sea Xoor we can estimate the static coeYcient

of friction to be m ¼ 0:8. This conservatively neglects the possibility of the collars
digging into the sea Xoor, but sizeable bottom undulations could negate some of
the bottom sliding resistance.

Thus, a static stability analysis, by summing forces in the horizontal direction

yields:

Fd � 0:8(1910 � F1) ¼ 0

or


CdrDU [2] � 0:8 1910� � [C][l][r][DU] [2]�

2 2


0
¼


where Fd and F1 are the current-induced drag and lift per meter of pipe length.
(The extra drag and possible lift caused by the collar are ignored.) Employing
conservative drag and lift coeYcients of 1.8 and 2.5, respectively, yields:


-----

U
¼


Coastal Structures / 209

vffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi
u 2(1910)
uu � � ¼ 1:15 m=s
t1000(0:61) [1][:][8]

0:8 [þ][ 2][:][5]


as the maximum allowable current velocity.

Cables

Rope and woven metal cables are used for ocean towing and the mooring of a
variety of Xoating structures including breakwaters, ships, buoys, and drilling
rigs. Design analysis for these structures when exposed to waves and currents
focuses primarily on the response of the structure with the cable providing a
Xexible restraint to the motion of the structure. The loading on the cable may or
may not necessarily be included, depending on the characteristics of the structure/cable system.

Cable diameters are typically quite small compared to design incident wave

heights. Consequently, D/H values are small or conversely KC values are large
(much greater than 25) so essentially all of the wave force on a cable is caused by the
drag component. Thus, if the force on a cable is to be determined the Reynolds
number for the peak wave-induced particle velocity and the associated drag coeYcient can be determined and the force computed from the standard drag equation.

7.3 Large Submerged Structures

A variety of large submerged structures such as oil storage tanks and caissons for
the mooring of vessels have been constructed in coastal waters. The lateral
dimensions of these structures are typically a signiWcant fraction of the incident
wave length. Commonly, D/H ratios are large and KC values are very small—of
the order of unity or less. These small KC values indicate that horizontal orbit
dimensions are small compared to structure dimensions so that appreciable Xow
separation will not occur and form drag forces are typically negligible. The total
wave force on the structure is due essentially to inertial eVects.

An inherent assumption in the Morison equation is that the particle velocity

and acceleration are essentially constant over a distance equal to the length of the
structure in the direction of wave propagation. This would not be the case for the
large submerged structures being considered. Also, these structures cause a large
amount of scattering or diVraction of the incident wave. Consequently, it is not
appropriate to just employ the inertia term in the Morison equation with an
appropriate mass coeYcient to determine wave loadings on large submerged
structures. Also, it is usually necessary to determine the resulting pressure
distribution on these structures for a given design wave condition.


-----

210 / Basic Coastal Engineering

For large submerged structures, viscous eVects will generally be conWned to

relatively thin boundary layers on the structure surface. As a consequence, it is
usually possible to assume irrotational Xow in the vicinity of the structure and
treat the determination of wave-induced pressures and forces as a potential Xow
problem. Rounder, more streamlined structures will have less Xow separation
than structures having square corners, for example, but if the KC number is
suYciently small, these eVects will be localized and the potential Xow solution
should still be meaningful.

Physical model studies of the wave-induced force and pressure distribution on

large submerged structures are more feasible than model studies of wave loadings on piles, owing to the lesser signiWcance of Reynolds number in the former
case. See Garrison and Rao (1971), Chakrabarti and Tam (1973), and Herbich
and Shank (1970) for examples of these model studies employing various shaped
structures.

Sarpkaya and Isaacson (1981) present a detailed summary of the application

of irrotational Xow theory to the investigation of wave forces and pressures
on large submerged structures. Generally, owing to the complexity of the
problem, the small-amplitude wave theory is used. The velocity potential for
the Xow Weld is assumed to consist of the incident wave and scattered wave
potentials:

f ¼ fi ¼ fs

where the scattered wave potential is due to the interaction of the wave with the
structure. The scattered wave will be a normal outgoing wave at some distance
from the structure. The boundary condition at the structure surface is that the
Xow velocity normal to the surface is zero, i.e.

@f

@n [¼][ 0 at][ S][(][x][,][ y][,][ z][)][ ¼][ 0]


where n is the surface-normal direction and S(x, y, z) 0 deWnes the surface
¼
geometry. A solution is then obtained for fs (see Sarpkaya and Isaacson, 1981)
to yield f ¼ fi ¼ fs.

Then, the lineraized equation of motion

p ¼ �rgz � r [@][f]

@t

yields the time- and space-dependent pressure distribution in the Xow Weld and
particularly on the structure. This can be integrated to determine the horizontal
and vertical force components acting on the structure.


-----

Coastal Structures / 211

7.4 Floating Breakwaters

A breakwater is a structure that protects the area in its lee from wave attack.
Most breakwaters are stone mound or rigid concrete structures. In recent years
there has been an increase in the use of Xoating breakwaters—a Xoating structure
that penetrates the upper part of the water depth and is moored to the bottom by
cables and an anchor.

Floating breakwaters function be reXecting wave energy and dissipating the

kinetic energy in the incident wave. This dissipation is primarily accomplished by
the generation of turbulence in Xow separation as wave-induced Xow passes the
structure and by the breaking of waves over the top of structure. If the incident
wave period is close to one of the resonant periods of the breakwater–mooring
line system, the motion response of the breakwater will be ampliWed which
generally causes increased wave energy dissipation.

Floating breakwaters have some distinct advantages: (1) they are easily adapt
able to large water level Xuctuations as are found, for example, at some recreation/water supply reservoirs; (2) their cost does not rapidly increase with an
increase in water depth as is the case for bottom-mounted Wxed structures; (3)
they are mobile and can relatively easily be relocated; (4) they oVer less obstruction to water circulation and Wsh migration; and (5) they are less dependent on
bottom soil conditions.

However, a primary disadvantage is that they are generally limited for use to

areas where the design incident wave period is relatively small, e.g., reservoirs,
rivers, and other areas having a relatively short wind wave generation distance;
or areas where vessel-generated waves are the dominant incident wave. For a
given water depth, shorter period waves have most of their energy concentrated
near the water surface where the Xoating breakwater is located, while longer
period waves have their energy distributed over a greater portion of the water
column and thus are more eVective at passing the structure. (For deep water
waves over 70% of the kinetic energy is concentrated in the top 20% of the water
column, while for shallow water waves the kinetic energy is essentially evenly
distributed over the water column.) A secondary, but still important disadvantage, is that they are kinetic structures that are more prone to damage at
connecting joints between units and at mooring line connectors. Also, if the
mooring lines or anchors fail, a Xoating breakwater can break loose and damage
nearby vessels, piers, and other structures.

A wide variety of Xoating breakwater types have been constructed (see

Kowalski, 1974 and Hales, 1981). The most commonly used Xoating breakwaters
fall into one of three groups demonstrated schematically in Figure 7.2. The prism
group typically consists of concrete boxes Wlled with Xotation material and
axially connected by Xexible connectors. The catamaran group is a variation
on the prism group which has greater stability to wave agitation for the same


-----

212 / Basic Coastal Engineering

Prism

Catamaran

Flexible assembly

Figure 7.2. Common Xoating breakwater groups.

breakwater mass. It also has better energy dissipation characteristics owing to
Xow separation at the structure’s additional corners. The most common type of
Xexible assembly Xoating breakwater is one made of interconnected scrap tires.

Figure 7.3 shows the transmission coeYcient Ct, deWned as the height of the

transmitted wave in the lee of the breakwater divided by the incident wave
height, for selected representatives of the three groups described above. Ct is
plotted as a function of the ratio of the breakwater dimension in the direction of
wave propagation W divided by the incident wave length. The data for these
curves come from wave tank tests with monochromatic waves employing breakwater models for the prism and catamaran and a prototype structure for the tire
assembly. Breakwater 1 is a concrete box having a prototype width of 4.87 m
and a draft of 1.07 m, tested in water 7.6 m deep (Hales, 1981). Breakwater 2 is a
catamaran breakwater having pontoons 1.07 m wide with a 1.42 m draft and a
total width of 6.4 m (Hales, 1981). The water depth for the catamaran was also
7.6 m. Breakwater 3 is a tire breakwater consisting of four Goodyear modules
for a total width of 12.8 m tested at a water depth of 3.96 m (Giles and Sorensen,
1979). The three breakwaters were moored as depicted in Figure 7.2. Other
mooring arrangements or the same arrangements with diVerent mooring line


Catamaran

Flexible assembly


-----

Ct


1.0

0.8

0.6

0.4

0.2

0


Tire
assembly

Catamaran

Prism


0.2 0.4


Coastal Structures / 213

Tire
assembly

0.6 0.8 1.0 1.2

W / L


Figure 7.3. Transmission coeYcients versus dimensionless size for common Xoating

breakwater groups. (Giles and Sorensen, 1979; Hales, 1981.)

taughtnesses or cable elasticities would somewhat alter the values of the transmission coeYcients.

Example 7.4-1

For the catamaran Xoating breakwater whose transmission characteristics are
given by Figure 7.3, determine the transmission coeYcient for incident waves
having a period of 2, 4, and 6 s.

Solution:

For a water depth of 7.6 m and the three periods of interest Eq. (2.14) yields the
following wave lengths:

T 2 s L 6.3 m
¼ ¼

4 s 24.0 m

6 s 44.4 m

For a breakwater width of 6.4 m the respective W/L values and Ct values from

Figure 7.3 are:


T ¼ 2 s W/L ¼ 0.98 Ct ¼ 0:24

4 s 0.27 0.79

6 s 0.14 0.91

The values for 2 and 6 s were determined by a slight extrapolation of the curve

in Figure 7.3


-----

214 / Basic Coastal Engineering

The Ct values indicate that the catamaran is very eVective for a 2 s wave but
quite ineVective for a 4 or 6 s wave. The prism would have about the same
general eVectiveness and the tire assembly would be similarly but somewhat less
eVective.

The results from Example 7.4–1 are quite indicative of the behavior of typical

Xoating breakwaters employed in typical water depths. For incident wave
periods of 2 to 3 s or less they are useful, but if the incident wave period
approaches 4 s or is higher their eVectiveness is sharply reduced. For a design
wind speed of say 30 m/s (67 miles per hour) and assuming fetch-limited conditions Figure 6.10 indicates that the largest possible fetch for an incident signiWcant wave period to not exceed 3 s is about one kilometer.

Wave-induced loads on Xoating breakwaters are primarily dependent on the

incident wave height. Adequate mooring line–anchor systems must be designed
to resist these loads. Hales (1981) and Harmes et al. (1982) provide some wave
loading data from wave tank experiments. Harmes et al. (1982) concluded that
for the tire breakwaters that they studied, the wave-induced loads increased at a
rate generally proportional to the wave height squared.

The most common types of anchors used for a Xoating breakwater are dead

weight anchors such as concrete blocks, screw anchors, and pile anchors that are
jetted or driven into the sea Xoor. The anchor type used depends on the design
loads and the sea Xoor conditions (see Giles and Eckert, 1979 for a brief review
of anchor design practice).

7.5 Rubble Mound Structures

Rubble mound structures consisting of interior graded layers of stone and an
outer armor layer of stone or specially shaped concrete units are employed in the
coastal zone as breakwaters, jetties, groins, and shoreline revetments. An advantage of rubble mound structures is that failure of the armor cover layer is not
typically sudden, complete, and due to a few large waves but gradual and usually
partial in extent, and spread over the duration of the higher waves that occur in a
storm. If damage does occur, the structure usually continues to function and the
damage can be repaired after the passage of the storm. In some cases it may be
economical to use smaller size armor units, anticipate a certain amount of damage
during a design storm, and provide for subsequent repair of the structure.

Armor units must be of suYcient size to resist wave attack. However, if an entire

structure were to consist of units of this size, the structure would allow high levels
of wave energy transmission and Wner material in the foundation or embankment
below the structure could easily be removed. Thus, the structure unit sizes are
graded in layers, from the large exterior armor units to small quarry-run sizes and
Wner stone at the core and at the interface with the native soil bed.


-----

Coastal Structures / 215

Other rubble mound design concerns include: (1) prevention of scour at the

seaward toe of the structure caused by wave agitation; (2) spreading of the
structure load so that there is no foundation failure owing to excessive loads;
(3) raising the crest of the structure to a suYcient height so wave overtopping
and transmission are not suYcient to attack the land behind a revetment or
regenerate undesirable wave action in the lee of a breakwater, and (4) for
breakwaters that tie into the shore or for revetments that are placed along the
shore, to be sure that scour at the end of the structure does not damage the
structure or diminish its eVectiveness.

Figure 7.4 shows a typical breakwater cross-section. Jetties and groins are

structures built normal to the shore, the former to protect navigation entrances
and the later to stabilize a shoreline that has an alongshore transport of sand.
Typically jetties are less massive than breakwaters and groins are less massive
than jetties. They are usually less complex than the breakwater depicted in
Figure 7.4, often consisting only of an armor layer and a single Wner core/
sublayer.

There are many variations in the cross-section design of breakwaters depend
ing on the design wave climate, brakwater orientation, water depth, stone
availability, foundation conditions, and degree of protection required of the
structure. A concrete cap is most commonly used with concrete armor units.
Two layers of armor units are commonly used. The breakwater crest width may
be dictated by the minimum width needed for construction equipment to operate
on the crest of the structure; otherwise, a minimum width of three armor unit
diameters is usually recommended. Structure face slopes are never steeper than
1.5H:1V and somewhat Xatter slopes are typically used. If the water depth is
suYcient, the seaward armor layer should extend at least 1.5 to 2 times the design
wave height below MLW. Note the extension of the C-stone to assist in toe
protection. If the armor stone weight is W, the Wrst under layer size might be
about W/10 to W/15 and the second underlayer size might be about W/200
(remember that the weight of an armor unit is proportional to the diameter
cubed).


Ocean Concrete

cap

2

1

D - stone

Figure 7.4. Typical rubble mound breakwater cross-section.


Harbor


2

1

D - stone


-----

216 / Basic Coastal Engineering

3

1

MLW

Cutoff wall

Figure 7.5. Typical revetment cross-section.


Runup deflector


Runup deflector

Gravel

3

1 Filter cloth

MLW

Embankment

Cutoff wall


The proWle of a typical shore revetment is shown in Figure 7.5. The armor

layer would be a wider graded stone riprap rather than the well-deWned two-layer
armor system found in a breakwater. Several varieties of interlocking concrete
units have also been used as the armor layer. A Wner sublayer will be used under
the armor layer and this often is placed over a geosynthetic Wlter cloth. A cutoV
wall of sheet piling and/or a pile of larger stone is commonly placed at the toe of
the structure to stabilize the toe against scour. Revetment slopes tend to be Xatter
than breakwater slopes. Additional design guidance for rubble mound structures
is given in the U.S. Army Coastal Engineering Research Center (1984).

Armor Unit Stability

A key element in the design of any rubble mound structure is to determine the
required armor unit size. This in turn dictates much of the remaining geometry of
the structure (i.e., layer dimensions, sublayer unit sizes, structure slopes, crest
width of the structure). The factors aVecting the armor unit size, usually speciWed
as the weight of the unit, are listed below.

Design wave characteristics. The design wave height at the structure is of

critical importance. Some designers use the signiWcant height although more
conservative heights such as H10 have been used. The importance of the structure, how well the design wave height is known, and the desired safety factor will
aVect this choice. The expected duration of attack by high waves during a design
storm is also an important factor. If the water depth at the seaward side of the
structure is suYciently shallow the design wave will break before it reaches the
structure. This will limit the wave height attacking the structure and will aVect
the type of attack that occurs.


-----

Coastal Structures / 217

Armor unit characteristics. The shape, speciWc gravity, and range of unit sizes

in the armor layer are important. More angular rock will be more stable than
rock that is rounded. ArtiWcial concrete armor units are designed to have
irregular interlocking shapes while maintaining suYcient layer porosity when
in place. Narrower stone size ranges are preferred for armor layers as very Wne
sizes are easily removed from the structure and Wner sizes decrease the layer
porosity which decreases its ability to relieve underlayer pressure exerted by
wave action. Lower layer porosities will also increase the elevation of wave
runup on the structure. However, specifying too narrow of a size range to a
quarry operator increases the eVort and thus cost of obtaining the rock.

Armor layer slope. The Xatter the slope the smaller the size of the armor unit

required for stability to wave attack. Smaller sizes yield thinner armor layers but
Xatter slopes require longer layers.

Trunk versus head. The head or end of a structure is typically exposed to more

concentrated wave attack than the trunk or side of the structure. For more
complex structures it is common to have Xatter slopes and/or larger armor unit
sizes at the head to protect against the greater wave attack.

Overtopping. The structure may be designed for moderate or signiWcant wave

overtopping depending on the structure purpose and design criteria. For signiWcant overtopping there is less return Xow on the seaward face of the structure
but greater action on the leeward face. This might allow smaller seaward armor
unit sizes and steeper slopes but more attention will have to be placed on the
design of the structure crest and lee side.

Placement method. Depending on the construction procedure and care taken

as well as the complexity of the structure, the armor unit placement my vary
from plain dumping of the units to selective placement of individual units.
Selective placement of the units will produce a more stable armor layer.

Layer dimensions. Thicker armor unit layers oVer more reserve stability if the

armor layer is damaged during a storm. It is imperative that damage during a
storm not proceed to the point where underlayers are exposed to wave attack.

Allowable damage. It is diYcult to predict the amount of damage that will

occur to a given armor unit layer for a given design storm. But some information
that is available would allow selection of a smaller armor unit with the related
economic beneWts in anticipation of repairing the structure after the damage has
occurred. Smaller units are easier to obtain from a quarry and easier to transport
as well as requiring less total volume, so their cost is less.

Determination of Armor Unit Stability

The hydrodynamic and armor unit interaction forces are very complex so a
completely analytical development of an equation for armor unit stability in
not practicable. Heavy recourse must be made to experiments. The basic problem is to determine the required weight W of an armor unit having a particular


-----

218 / Basic Coastal Engineering

shape and speciWc gravity S (in air), when exposed to waves of a given height and
when placed on a structure face having a given slope u. From a rough analysis of
the forces involved one can deWne a stability number for an armor unit

Ns ¼ H=(S � 1)(W =gs)[1][=][3] (7:9)

where gs is the speciWc weight of the stone or concrete armor unit. The stability
number can be thought of as a dimensionless wave height and the term in the
denominator that is raised to the one-third power is an eVective diameter of the
unit. A number of wave tank experiments have been run (Hudson, 1959) to relate
Ns to the face slope and the armor unit shape at incipient failure of the armor
units on the face. Basically, the experiments involved building an armor unit
slope and exposing it to increasing wave heights until failure was observed. This
failure point deWned the stability number. The result is

Ns ¼ (KDcotu)[1][=][3] (7:10)

where KD is a dimensionless coeYcient that depends on the armor unit shape,
method of placement, location on the structure head or trunk, and whether the
incident wave breaks before reaching the structure or on the structure face slope.
Combining Eqs. (7.9) and (7.10) yields the classic Hudson equation for armor
unit stability.


W gsH [3]
¼

KD(S � 1)[3]cotu


(7:11)


Most laboratory studies to evaluate KD have used waves having a constant

period and height. For irregular waves, some designers use the signiWcant height
for H in Eq. (7.11). For conservative design, the U.S. Army Coastal Engineering
Research Center (1984) recommends use of a higher wave such as H10. Note that
the required armor stone weight is proportional to the design wave height cubed.
The weight used in Eq. (7.11) for stone armor units having a range of sizes is the
median weight (i.e., 50% of the stones would weigh more than W).

Several dozen diVerent shaped artiWcial armor units have been developed.

Three of the most commonly used shapes—the dolos, the tetrapod, and the
tribar—are depicted in Figure 7.6. Quarrystone is most commonly used. However, for a given design wave height and face slope, an artiWcial concrete unit will
have a smaller required size (weight) than a stone for the same stability level (i.e.,
larger KD value). However, concrete armor units are occasionally broken either
during placement or when under wave attack. Thus, if the quarries cannot
produce a suYciently large armor stone or transportation and placement restrictions eliminate the possibility of using a suYciently large stone, artiWcial concrete
units can be used.


-----

Coastal Structures / 219

TETRAPOD DOLOS

TRIBAR

Figure 7.6. Typical concrete armor unit forms.

Selected values of KD are tabulated in Table 7.1 as a function of unit shape,

location on the structure head or trunk, and exposure to breaking or nonbreaking waves (i.e., waves that have or have not broken before they reach the
structure). These values, except for the tribar, are for two layers of units,
randomly placed, with zero allowable damage, and minor or no overtopping of
the structure. The values for the tribar are for a single layer uniformly placed
with the three legs perpendicular to the structure face.

Table 7.1. Suggested KD Values

Trunk Head

Unit Breaking Nonbreaking Breaking Nonbreaking


TETRAPOD DOLOS

TRIBAR


Quarrystone—smooth rounded 1.2 2.4 1.1 1.9

Quarrystone—rough angular 2.0 4.0 1.6 2.8

Riprap 2.2 2.5 — —

Dolos 15.8 31.8 8.0 16.0

Tetrapod 7.0 8.0 4.5 5.5

Tribar 9.0 10.0 7.8 8.5

U.S. Army Coastal Engineering Research Center, 1984.


-----

220 / Basic Coastal Engineering

Table 7.2. H/H (zero damage) as a Function of Percent Damage


Percent Damage


Unit 5–10 10–15 15–20 20–30 30–40 40–50

Quarrystone—smooth 1.08 1.14 1.20 1.29 1.41 1.54

Quarrystone—rough 1.08 1.19 1.27 1.37 1.47 1.56

Tetrapods 1.09 1.17 1.24 1.32 1.41 1.50

Tribar 1.11 1.25 1.36 1.50 1.59 1.64

Dolos 1.10 1.14 1.17 1.20 1.24 1.27

Adapted from U.S. Army Coastal Engineering Research Center, 1984.

The stability coeYcient can be increased if a certain percent damage is to be

allowed for the design wave condition. ModiWed allowable wave height values
can be determined from Table 7.2 which gives the ratio of the wave height
allowed to the wave height for zero damage as a function of percent damage
allowed. Percent damage is deWned as the percent volume of units displaced from
a zone on the structure face that extends from the middle of the breakwater crest
downward to a depth of one wave height below the still water level.

It should be mentioned that some of the values in Table 7.2 are interpolated or

extrapolated from very limited test results. The values generally show the eVect
one can achieve by allowing a certain level of damage to a rubble mound
structure for a given design wave condition. Note also, that the dolos, which
has the highest zero damage KD values, has the lowest reserve stability as
indicated by the lower values in Table 7.2 for higher percent damage.

Sensitivity of the Hudson Equation

In order to have a better appreciation of the Hudson equation (Eq.7.11) for use
in the design of stone mound structures, it is helpful to investigate the inXuence
of small changes in each of the key independent parameters in the equation:
namely the armor unit speciWc gravity, the design wave height, the front face
slope and the KD value used.

Considering a typical armor stone speciWc gravity of 2.6 and salt water, an

increase in the armor stone speciWc gravity of 10% will decrease the armor unit
weight required by 30%. Decreasing the speciWc gravity by 10% increases the
necessary weight by 55%. (But, remember that the armor unit nominal diameter
and thus the armor layer thickness is a function of the cube root of the unit’s
weight.). The approximate speciWc gravity of armor units can vary from concrete
(2.25) to granite (2.65) to basalt (2.90). Thus, concrete blocks would need to be
about double the weight of basaltic blocks (if the units had about the same shape
and thus similar KD values).


-----

Coastal Structures / 221

The design wave height used in the Hudson equation is usually only approxi
mately determined owing to the possible variabilities in wave hindcasting and
wave measurement, variabilities in extreme wave return period analysis, and the
choice of which Hn (e.g. Hs or H10) to use. Given this, an increase in the design
wave height by 10% will require an increase in armor unit weight by 33%. A
decrease in design wave height by 10% will decrease the required unit’s weight by
27%.

Typical front face slopes for stone mound breakwaters vary from about 1:1.5

to 1:2.5 and revetment slopes are usually Xatter. Decreasing the front face slope
from 1:1.5 to 1:2.5 decreases the armor unit’s weight required by 67%. But more
volume of stone is required owing to the longer slope.

The KD values listed in Table 7.1 are those suggested by the U.S. Army Corps

of Engineers. They are empirical values based typically on tests of armor unit
stability carried out in wave tanks. The given values for a particular armor unit
can vary signiWcantly depending on whether the tests were conducted with
monochromatic waves or spectral waves (and if spectral waves, the character
of the wave spectrum used), the Hn value that is to be used when applying the
Hudson equation, and the way armor unit stability is deWned in the wave tank
tests. Given this background and accepting the values in Table 7.1 for example,
the ratio of required armor weight increase in going from dolos to tetrapods (for
trunk, breaking waves) would be 2.25.

The above discussion demonstrates the typical uncertainties involved in using

the Hudson equation for stone mound structure design. The designer must have
a strong sense of the conWdence that can be placed in the various factors that
inXuence the calculation of required armor unit weight. From this, and a
consideration of the costs of the various breakwater components and related
construction costs, choices can be made. Often, especially for fairly major
structures and given suYcient time and funds, the designer would be wise to
have model tests conducted to further strengthen design decisions that are
made.

Example 7.5-1

The head of a rubble mound breakwater that is to be constructed on one of the
Great Lakes is to have an armor face slope of 1:2.5. The breakwater head is in
water having a design depth (high lake level plus design surge level) of 6.6 m and
the bottom slope fronting the structure is 1:30. The deep water design wave
signiWcant height and period are 4.0 m and 7.3 s, respectively, and it may be
assumed that the refraction coeYcient from deep water to the structure is 1.0.
Assume that the breakwater will have only minor overtopping for the design
condition. Determine the required armor unit size if angular quarrystones and
tetrapods are to be considered. Assume S ¼ 2:65 for the stone and S ¼ 2:40 for
concrete.


-----

222 / Basic Coastal Engineering

Solution:

For conservative design we will use H10 as a design wave height. From the
Rayleigh distribution (Figure 6.5, line b) we can show that

H10 ¼ 1:27 Hs ¼ 1:27(4) ¼ 5:1 m

in deep water. From Eq. (2.42) with a refraction coeYcient of unity and a wave
period of 7.3 s we have H10 ¼ 4:9 m at a water depth of 6.5 m (i.e., at the
breakwater head). From Figure 2.12, for the given bottom slope a wave having
a height of 4.9 m will break in water 5.9 m deep. Thus, although H10 will not
break by the time it reaches the structure (where the depth is 6.5 m), some of the
highest waves in the spectrum will break before reaching the structure. This will
slightly decrease the value of H10. We will employ a wave height of H10 ¼ 4:9 m
and assume nonbreaking conditions in our analysis.

Thus, from Table 7.1 for the zero damage condition, nonbreaking waves, and

structure head, KD ¼ 2:8 for the angular quarrystone and KD ¼ 5:5 for the
tetrapods. Then Eq. (7.11) yields


W [(9810)(2][:][65)(4][:][9)][3]
¼

2:8(2:65 � 1)[3](2:5)

for the quarrystone unit median weight and

W [(9810)(2][:][40)(4][:][9)][3]
¼

5:5(2:40 � 1)[3](2:5)


97,300 N
¼

73,400 N
¼


for the weight of the tetrapod units. Note the combined eVect of the higher KD
value for the tetrapods but related lower speciWc gravity of the concrete used for
the tetrapods.

Economic Implications for Design Wave Selection

The common approach to the design of rubble mound structures is to employ a
design wave having a certain return period (e.g. 50 years) and use this to
calculate the required armor unit size as well as the other related characteristics
of the structure. The wave return period is selected based on the design and
economic life of the structure and/or local code or common practice dictates.
Conceptually, if the waves attacking the structure are lower than the design wave
height there would be no damage to the structure. But, higher waves having a
longer return period can also be expected to occur with some probability of
occurrence and damage to the structure can be expected from these waves.


-----

Coastal Structures / 223

An alternative approach is to select the design wave based on an optimization

of the economics of the structure. For a given design wave height, there will be a
related total cost of construction of the structure. As this design wave height is
increased the total construction cost of the structure will increase (larger armor
units, higher crest elevation, etc.) But, the true cost of a structure must also
include the cost of maintenance and repair of any damage during the life of the
structure. As the design wave height is increased, the more robust structure can
be expected to have lower damage and maintenance costs. Both the construction
cost and the maintenance and damage costs can be estimated on an annual basis
and summed to give the amortized annual cost of the breakwater over its design
life, as a function of the design wave height employed. When this is done, the
typical total annual cost of the structure will initially decrease as the design wave
height is increased, but up to a point. Beyond this point the total annual cost will
typically level oV and then begin to increase. The optimum design wave height,
then, is the design wave height that yields the lowest combination of annualized
construction costs plus annualized maintenance plus damage costs.

Generally, this design approach is conceptually desirable; but, in practice, it is

usually quite diYcult to employ. Construction costs can be generally well
deWned, but damage and maintenance costs during the lifetime of the structure
are diYcult to deWne with any conWdence. Also, one could repeat this entire
analysis using diVerent armor units (e.g. dolos vs. tetrapods vs. stone from one
quarry vs. stone from another quarry, etc.) Also, one could repeat this analysis
for diVerent structure crest elevations to include the cost of damage from wave
transmission past the structure for each elevation.

Weggel (1981) presents an analysis employing hypothetical cost data that

further demonstrates this approach to design wave selection.

Armor Stone SpeciWcation

After the design armor stone size is determined from some equation such as the
Hudson equation, additional requirements are typically speciWed for selection of
the speciWc stone to be used. The stone weight calculated by the Hudson
equation is the median weight for a widely graded stone such as that used for a
stone-armored revetment. For a breakwater where there is a speciWc two-layer
armor stone section, the range of allowable stone sizes must still be speciWed. The
U.S. Army Corps of Engineers (U.S. Army Coastal Engineering Research Center, 1984) speciWes that the armor layer stone weight can vary from 0.75 W to
1.25 W. Since the nominal diameter is a function of the cube root of the weight
this is only a 0.93 to 1.09 times the nominal diameter size range. As a practical
matter this is probably too restrictive of a requirement. From the author’s
experience, a broader range of armor stone weights is typically speciWed. Some
stone speciWcations have given a speciWc size gradation to be followed (e.g. 20%
to be between 1.5W and 1.3W, etc.). This restrictive a speciWcation is probably


-----

224 / Basic Coastal Engineering

too diYcult to follow in the Weld. Stone size range can be checked in the Weld by
having the quarry set aside stone samples of speciWed weight for the Weld
inspector to visually compare these stones to the delivered stone.

The Hudson equation leads to two other speciWc stone characteristic require
ments. The calculation is based on a given stone speciWc weight, so a minimum
stone speciWc gravity would typically be speciWed. The selection of a design KD is
based on the stone shape with smooth rounded stone having a lower KD value
than rough angular stone. A related shape issue is that long thin cylindrical stone
are not acceptable. The related speciWcation would specify a maximum to
minimum axis length ratio.

Some of the following stone sample analyses may also be speciWed:

Compressive strength. A minimum stone compressive strength (e.g. 4000 psi)

would be speciWed.

Abrasion. This would specify the percent of stone volume loss allowed after a

speciWed number of revolutions in a tumbler.

Freeze/thaw. For stone in cold regions a test would evaluate the volume of

stone lost by spalling for a certain number of cycles of freezing and thawing of
wet stone.

Petrographic examination. This simply involves the inspection of stone samples

by a knowledgeable person to look for deWcient qualities such as layers of weaker
stone or signiWcant stone cracks.

The Hudson equation [Eq. (7.11)] is most commonly used for the determin
ation of required armor unit size in the design of rubble mound structures.
However, it does not explicitly include such variables as the incident wave
period, the type of wave breaking on the structure, the allowable damage level,
the duration of storm wave attack (i.e., the number of waves that attack the
structure), and the structure (armor and sublayer) permeability. More complex
equations that include these parameters and apply to waves breaking on the
structure face have been presented by van der Meer (1988, 1995). He presents one
equation for plunging breakers and another for surging breakers, with a third
equation to deWne the intersection point between the two equations. The equations were developed only for stone armor units.

Recent Developments

Traditional breakwaters typically contain one or two layers of armor stone with
progressively Wner layers of stone down to the breakwater core. Where the design
wave height is large, large armor units are required. For a variety of reasons
these units may be excessively costly. An alternative type of breakwater, commonly known as a berm breakwater (Baird and Hall, 1984; Willis et al., 1988),
employs stone that has a smaller median diameter and a wider size range for the
armor layer. Figure 7.7 shows a typical proWle of a berm breakwater. The ‘‘as


-----

Coastal Structures / 225

"as built"

Surge

level

MSL

Adjusted

Armor Core

Figure 7.7. Berm breakwater cross-section.

built’’ proWle of the armor layer is expected to adjust as waves attack the
structure forming the adjusted proWle shown in the Wgure. The adjusted proWle
is similar to a beach proWle consisting of extremely coarse material (see Chapter
8) where the armor stones move on the slope in response to wave attack.

Baird and Hall (1984) list some of the advantages of berm breakwaters: (1) the

armor stones can be less than one-Wfth the weight of stones used for conventional
armor units which, with the wider allowable size gradation, maximizes the use of
available stone from a quarry; (2) stone placement is easier than in conventional
breakwaters and construction tolerances and underwater inspection requirements can be relaxed; and (3) the design is much simpler, there being fewer
layers and toe scour protection layers are usually not required. Although the
total stone volume required may be 10% to 20% greater than for a conventional
breakwater, the total cost will usually be signiWcantly less.

Several of these breakwaters have been constructed (see references in the

previous two paragraphs). However, at the present time, it is recommended
that any design be tested in a model study as no simple formulae similar to the
Hudson equation are available to guide the design.

Some laboratory tests (Ward and Ahrens, 1992) have been conducted on a

berm revetment concept which is similar to the berm breakwater concept. The
revetment would consist of a dumped mass of stone placed in front of an
embankment that is to be protected. The stone would have a Wner median size
and a wider gradation than the armor riprap designed by the Hudson equation.
It likewise would adjust its proWle in response to wave attack.

During recent years a number of low-crested and submerged crest breakwaters

have been constructed. These breakwaters are commonly built parallel to the
shore and seaward of the surf zone, with the breakwater crest located around or
below MSL. They function to stabilize a beach or assist in the retention of sand
artiWcially placed on a beach. They have also been placed in front of larger
structures to increase the stability of these structures. With their low crest they let
normal low waves pass through to the beach but cause the breaking of larger
storm waves. In recreational areas they are more aesthetically pleasing than
structures that extend signiWcantly above MSL. Often they are constructed of a
mass of relatively widely graded stone overlying a Wlter layer on the sea Xoor.


"as built"

Surge

level

MSL

Adjusted

Armor Core


-----

226 / Basic Coastal Engineering

Failure of submerged crest breakwaters usually involves removal of stones

from the breakwater crest as wave-induced reversing Xow acts over the crest. A
modiWed stability number Ns[�] [is used to de][W][ne structure stability where]

H [2][=][3]L[1][=][3]

Ns[�] [¼] (S � 1)(W =gs)[1][=][3] (7:12)


In Eq. (7.12) the wave length L is determined for the water depth at the structure.
The wave length is included in the modiWed stability number because experiments have shown that the wave period is much more signiWcant to the stability
of submerged crest breakwaters.

After analyzing the results of a number of laboratory studies of submerged
crest breakwaters van der Meer and Pilarczyk (1990) concluded that the modiWed
stability number is only a function of the damage level and the relative crest
height. The damage level S is deWned as the area of the structure proWle from
which stone has been removed divided by the median diameter squared of the
stone used to construct the breakwater (van der Meer, 1988). The relative crest
height is deWned as the height of the structure crest above the sea Xoor hc divided
by the water depth d at the structure (where d > hc). The resulting relationship
for submerged crest breakwater stability is

hc s (7:13)

d

[¼][ (2][:][1][ þ][ 0][:][1][S][)][e][�][0][:][14][ N][�]


In the modiWed stability number in Eq. (7.13), Tp is used to calculate the wave
length at the structure and Hmo is used for the wave height. Thus, employing Eq.
(7.13) and given the desired structure cross-section proWle one can calculate the
required median stone weight as a function of the incident design wave condition
and the allowable damage level.

A procedure for determining the size of armor stone required for low-crested

stone mound structures (hc > d) has been presented by van der Meer and Pilarczyk
(1990). This procedure gives a ‘‘reduction factor’’ for the median nominal stone
diameter (W=�s)[1][=][3] based onthe medianarmorstonediameterdetermined bysome
armor stone stability formula such as the Hudson equation (Eq. 7.11).

DeWne Rc as the vertical elevation of the structure crest above the design MWL

(i.e. Rc ¼ hc � d). Then a dimensionless structure crest height R[�]c [is given by]

R[�]c p[)][0][:][5]

[¼][ (R][c][=][H][s][)(H][s][=][gT][2]


R[�]c [can be calculated for a given structure crest elevation and design wave]

condition. Then the reduction factor (RF) is

RF ¼ (1:25 � 4:8R[�]c[)][�][1] (7:14)


-----

Coastal Structures / 227

for 0 < R[�]c [<][ 0][:][052.]

Thus, Eq. (7.14) allows for the calculation of the required armor stone nom
inal diameter by multiplying RF times the nominal stone diameter calculated by
the Hudson equation. RF varies from 0.8 for the structure crest at the design
MWL (hc ¼ d) up to unity for a structure crest elevation that allows minor or no
wave overtopping.

Tandem Breakwater Concept

Cox and Clark (1992) present the design of a unique breakwater for the marina
at Hammond, Indiana that they refer to as a tandem breakwater. A conventional
stone mound breakwater for this site, that would control wave transmission by
overtopping to within acceptable limits, would have a 4.6 m freeboard above the
design lake water level with 1:1.5 side slopes. The armor stone size required for
this breakwater ranged up to 8 tons. This breakwater was found to be too costly.
Three alternatives were considered, a berm breakwater, a sheet pile wall, and a
gravity caisson structure. These alternate structure types for this site all proved
to be more expensive than the conventional breakwater design. The least total
cost structure for this site turned out to be a tandem breakwater consisting of a
smaller conventional stone mound main breakwater fronted by a submerged reef
stone breakwater with an open water energy dissipation zone between the
conventional and reef breakwaters.

‘‘A reasonable-cost main breakwater could be built if the freeboard could be

reduced to 10 ft (3.05 m) and the armor sized down to 3 tons with the same
harbor tranquility requirement. This dictated that the transmitted wave from the
reef could not exceed 9 ft (2.74m) in the design storm.’’

The authors felt that the available published information on wave transmission

over a reef structure was insuYcient for a thorough design analysis, so they conducted physical model tests to supplement this available information. They investigated reefs of various depths of submergence, crests widths, and reef porosities.

The Wnal design concept had a conventional breakwater with a freeboard of

3.05m and 3 ton armor stones fronted by a reef structure with a crest width of 7m
located 0.86 m below the design lake water level. The reef breakwater was
constructed of a range of stone sizes from 0 to 1 ton. Both the main and reef
breakwaters had 1:1.5 side slopes. The authors conclude that the tandem breakwater may not always be the most economic design, as overall costs are dependent on local material costs and local water depths.

7.6 Rigid Vertical-Faced Structures

Some classes of coastal structures incorporate a rigid vertical face that is exposed
to wave action. These include caissons typically consisting of a concrete or steel
shell Wlled with sand and gravel and sitting on a gravel base, and vertical concrete


-----

228 / Basic Coastal Engineering

or wood panels supported at intervals by vertical and batter piles. The latter have
been used at marinas and to control wave action at ferry slips. An important
aspect of the design of these structures is the determination of the wave loading
on the structure. If the wave loading is suYcient, caisson structures can slide oV
of their base. Vertical panel structures carry the wave-induced force to the
supporting piles which can fail if the force is excessive.

If the water is suYciently deep at the toe of the structure incident waves will

reXect from the structure, forming a standing wave system with Xuctuating
pressures. For shallower water depths the waves will break directly on the
structure or they will break seaward of the structure and send a turbulent mass
of water forward to impinge on the structure. Each of these conditions is
discussed below.

Nonbreaking-Wave Forces

The pressure distribution in a standing wave is given by Eq. (2.59). If the
standing wave is formed by the complete reXection from a vertical structure
(located at x 0) the crest to trough excursion of the water surface at the
¼
structure is 2H and the dynamic pressure acting on the structure is

pd ¼ [r][gH][ cosh]cosh[ k] kd[(][d][ þ][ z][)] cos st (7:15)

Thus, the dynamic pressure at the toe of the structure (d z 0) varies between
þ ¼

rgH
� (7:16)

cosh kd

as the standing wave oscillates from the crest to trough position. The dynamic

pressure distribution given by Eq. (7.15) is shown in Figure 7.8 for the wave crest
and trough positions. These pressure distributions are almost linear from the
instantaneous water surface to the bottom and are usually assumed to be linear
for simpliWed conservative calculations of standing wave forces and moments on
a vertical structure.

From radiation stress considerations it can be shown that wave reXection

causes the mean water level at the structure to rise above the still water level
by an amount


Dz ¼ [p][H] [2] coth kd (7:17)

L

Wave reXection may not be complete owing to energy losses at the structure (i.e.,
Cr ¼ Hr=Hi < 1:0). Thus


-----

Coastal Structures / 229

Standing wave envelope

H

Mean water level

∆ z

H Still water level

Linear approximation

d

Dynamic pressure

Hydrostatic pressure

_rg H_
_rgd_

cosh kd

Figure 7.8. Standing wave pressure distributions on a vertical wall. (U.S. Army Coastal

Engineering Research Center, 1984.)

2H ¼ Hi þ Hr ¼ (1 þ Cr)Hi

or


Standing wave envelope

H

Mean water level

∆ z

H Still water level

Linear approximation

d

Dynamic pressure

Hydrostatic pressure

_rg H_
_rgd_

cosh kd


H ¼ [(1][ þ][ C][r][)][H][i] (7:18)

2

which is the value depicted in Figure 7.8 and used in calculations. The U.S. Army
Coastal Engineering Research Center (1984) recommends that a minimum value
of Cr ¼ 0:9 be used for design purposes.

Note that the maximum moment exerted on a thin vertical barrier can occur if

there is a wave crest on one side and a wave trough on the other side. Again, for
conservative design this condition is often assumed.

If H Dz exceeds the elevation of the structure crest above the still water level,
þ

water will spill over the crest. This will relieve some of the pressure acting on the
structure just below the crest. Again, for conservative design it is usually assumed that the pressure distribution is the same as if the structure extends up to
H Dz, with the pressure distribution truncated at the structure crest. The same
þ
concept can be applied at the bottom if the structure does not reach to the sea
Xoor.


-----

230 / Basic Coastal Engineering

Example 7.6-1

The breakwater for a small marina is constructed of vertical concrete panels
supported by piles. The water depth at the structure is 4 m and the panels have
an opening of 0.5 m at the bottom to enhance water circulation in the marina.
The panels extend 1.5 m above the still water level (i.e., panel lengths are 5 m).
For an incident wave height of 1 m and a period of 4 s determine the maximum
wave-induced force and moment on the breakwater per unit length. Assume still
water on the lee side.

Solution:

Since the bottom opening will diminish reXection to a small extent we will
assume Cr ¼ 0:9. Then Eq. (7.18) yields

H ¼ [(1][ þ][ 0][:][9)] (1) ¼ 0:95 m

2

From Eq. (2.14) with d ¼ 4 m and T ¼ 4 s, L ¼ 20:86 m and k ¼ 0:3013. Then
Eq. (7.17) yields

Dz ¼ [p][(0][:][95)][2] coth (0:3013)4 ¼ 0:15 m

20:86

and Eq. (7.16) yields a maximum bottom dynamic pressure of


9810(0:95)
pd ¼ cosh (0:3013)4 [¼][ 5125 N][=][m][2]

Then, the pressure on the structure will vary as follows:

z ¼ 0:95 þ 0:15 ¼ 1:10 m p ¼ 0

z ¼ �4:0 m p ¼ 9810(4) þ 5125 ¼ 44; 365 N=m[2]

� �

z ¼ �3:5 m p ¼ 44,365 [3][:][5][ þ][ 0][:][95][ þ][ 0][:][15] ¼ 40,040 N=m[2]

4 þ 0:95 þ 0:15

Thus, the total force per unit length is


40; 040

(3:5 þ 0:95 þ 0:15)(1) ¼ 92, 092 N=m
2

This force acts at a distance of

0:5 þ [(3][:][5][ þ][ 0][:][95][ þ][ :][015)] ¼ 2:03 m

3


-----

Coastal Structures / 231

above the sea Xoor; so the moment per unit length around the sea Xoor is

92,092(2:03) ¼ 187,254 N m=m

Breaking-Wave Forces

When a wave breaks directly on the face of a vertical structure there is a dynamic
impact force on the structure that acts around the still water line. This is superimposed on the normal hydrostatic force. On rare occasions, the breaking wave
will have a vertical face that slams against the structure and causes an extremely
high intensity, short duration (less than 0.01 s typically) pressure on the structure. Although a high instantaneous force can develop, this force is of very short
duration so the eVect may not be great, particularly for massive structures that
require a sustained force to dislocate them. The force may cause localized
damage on a structure face which would be increased by repeated wave attack.

There have been a number of laboratory studies of breaking wave forces on

vertical walls, especially caisson structures resting on rubble underlayers (Goda,
1985; Port and Harbor Research Institute, 1994). This has produced some
semiempirical formulas for the calculation of wave loadings. Owing to their
more common usage in Japan, most of the research on caisson type structures
has been carried out there.

Figure 7.9 shows the proWle of a typical caisson structure. Goda (1985) gives

equations, based on laboratory studies with irregular waves, for determining
both the breaking wave pressure distribution on the structure and the related
uplift pressure on the caisson base. The pressures are related to the maximum
wave height just seaward of the breaker line Hmax which is taken as being equal
to 1:8 Hs. The pressure extends up to an elevation given by

z ¼ 0:75(1 þ cos b)Hmax

z

P1

MWL

Caisson

d d[|]

d*

Armor

P2 Core

Figure 7.9. Broken wave pressure distribution on a caisson. (From Goda, 1985.).


z

P1

MWL

Caisson

d d[|]

d*

Armor

P2 Core


-----

232 / Basic Coastal Engineering

where b is the angle between the direction of wave approach and a line normal to
the caisson face. For force calculations, the pressure distribution would be
truncated at the caisson crest. The key pressures are:

p1 ¼ 0:5(1 þ cos b)(a1 þ a2 cos[2] b)gHmax

p2 ¼ a3p1

� 2 kd [�] �

a1 ¼ 0:6 þ 0:5 sinh 2kd [�]

a2 ¼ "db3 �db d �Hdmax�2#or�H2maxd �


0 � 1 �

a3 ¼ 1 � d[d][�] [1][ �] cosh kd [�]

where, in the term a2 the larger value is used and where db is the water depth at a
distance 5 Hs seaward of the caisson. This latter term recognizes that the greatest
pressures are exerted by waves that break somewhat seaward of the structure and
strike it midway through their plunging distance.

The uplift pressure on the base of the caisson varies linearly from a value

Pu ¼ 0:5(1 þ cos b)a1a3gHmax

to zero on the lee side of the caisson.

With the wave loading and uplift pressure distributions given above, an

analysis of caisson stability against sliding can be carried out. The wave-induced
uplift pressure and the buoyant force on the caisson would be included in the
determination of structure stability to sliding.

Broken-Wave Forces

When waves break completely seaward of a coastal structure, the structure,
which may be located above the still water level, can be subjected to a surge of
water that exerts an impact force on the structure. An example of this type of
structure would be the runup deXector on the shore revetment shown in Figure
7.5. Another example would be a sheet pile wall located back on a beach face.

This situation has not been thoroughly studied experimentally, but the U.S.

Army Coastal Engineering Research Center (1984) presents a method (believed
to be conservative) for broken wave force prediction that is based on a number
of simpliWed but reasonable assumptions. It is assumed that when a wave breaks
on a slope it causes a mass of water to surge forward with a velocity equal to the
wave celerity at breaking, i.e.


ffiffiffiffiffiffiffi
gdb


V
¼


p


-----

Coastal Structures / 233

The vertical thickness of this water mass is assumed to be equal to the crest
amplitude at breaking which is taken as 0:78Hb. It is then assumed that the water
velocity and vertical thickness remain the same until the water reaches the
structure or still water line, whichever comes Wrst. If the structure is located
landward of the still water line, the water velocity and vertical thickness are
assumed to decrease linearly from the value at the still water line to zero at the
hypothetical point of maximum wave runup (if there were no structure to
interfere with the runup). The kinetic energy of the surging water mass is
converted to a dynamic pressure (i.e., the stagnation pressure from the Bernoulli
equation) that acts on the structure face to produce the resulting impact force.
This is added to the hydrostatic force to predict the resulting force on the
structure. This method will give an ‘‘order of magnitide’’ estimate of the broken
wave force on the structure, but model tests are recommended if a more accurate
force estimate is desired.

7.7 Other Loadings on Coastal Structures

Commonly, along the coast, waves are the dominant phenomenon a designer
must consider when designing coastal structures, both because of the loadings
they exert on structures and because of their importance in the transport of
sediment in the nearshore zone. However, at some coastal locations other forces
besides those caused by wave activity can be important to the design of coastal
structures. These include forces exerted directly by currents, the wind, and ice;
earthquake loadings; and vessel-induced forces on dock and other structures.
For more detail on these topics the reader is referred to Bruun (1989),
Gaythwaite (1990), Herbich (1990), and Tsinker (1995).

Currents

Coastal currents are generated by a variety of mechanisms: (1) wind-generated
waves generate alongshore currents in the surf zone (see Chapter 8); (2) the tide
generates reversing currents along the coast and at entrances to harbors, rivers,
and estuaries; and (3) the wind generates currents directly by wind-induced stress
on the water surface (see Chapter 5). Current-induced drag and lift forces on
structures are calculated from the drag equation [Eq. (7.1)] as discussed in
Sections 7.1 and 7.2 and in most elementary Xuid mechanics texts.

Wind

The wind accompanying major storms, especially hurricanes, can cause signiWcant damage to some coastal structures. For a general references on wind
loadings see Simiu and Scanlan (1986). Direct damage is caused primarily to
buildings and other lighter structures along the shore and to oVshore platforms


-----

234 / Basic Coastal Engineering

particularly during construction and towing to the site. Indirect damage to
harbor structures is caused primarily by vessels being torn loose and hitting
these structures. Besides the typical drag and lift calculations for Xuid forces on
structures, the designer must be concerned with wind gusting and Xow-induced
vibrations owing to eddy shedding at the lee side of structures.

The short-term average wind speed in a wind gust can be signiWcantly higher

than the longer term average wind speed. Depending on the structure size and
strength, a 5-s long wind gust might be large enough to envelope a structure and
cause damage.

As is the case for structures in waves, vortex shedding as the wind blows past a

structure can cause a lock-in resonant response if the vortex shedding frequency
matches a resonant frequency of the structure. Winds that cannot damage a
structure by direct form and friction drag may damage the structure by windinduced vibrations.

In the coastal zone, the wind will usually have a high concentration of

suspended water droplets. This can signiWcantly increase the eVective density of
the wind and the resulting drag force on a structure.

Ice

In cold regions ice can have a major negative impact on the design of coastal
structures and the planning and operation of harbors and navigation channels. It
can have a positive impact on some shorelines by protecting them from wave
attack during a large portion of the annual cycle.

The tensile and compressive strength of sea ice is quite variable and is depen
dent on salinity, temperature, depth within the ice sheet, ice growth rate, and the
rate at which a load is applied to the ice. Information on such factors as the
expected return period for given ice thicknesses, the lateral extent of ice Xoes that
commonly occur, and the tide range and expected speeds and directions of ice
Xoe movement as the ice is driven by the wind and currents is needed for eVective
design for ice conditions.

There are several ways in which ice can exert forces on coastal structures (see

Peyton, 1968) including:

1. Moving sheet ice driven by the wind or currents will exert a horizontal force

onastructureatthewaterline.Theforcewillbecausedbytheinitialimpactof
the ice or by the cutting of a slot through the ice sheet as moving ice is crushed
by a structural member. Ice sheets can be as much as a meter or more thick
and, when being crushed, can exert pressures on the order of 200to300 N=cm[2]

of frontal projected area. The nature of ice failure by crushing is such that
structural loading is often cyclic with a frequency of a cycle/s or more.

2. Inclined structural members will lift an ice sheet and cause ice failure by

bending, which results in a much smaller ice force than failure by crushing.


-----

Coastal Structures / 235

Structural members can often be designed with a sloping section over the
expected tide range to cause bending failure of the ice.

3. Ice frozen to a structure at high tide can exert a signiWcant vertical load as

the tide drops and similarly, ice frozen to a structure at low tide can exert an
uplift force as the water level rises. During a thaw, large ice blocks frozen to
structural members can move rapidly and cause damage.

4. Ice sheets resting on a riprap slope and moving with currents and the wind

can ‘‘pluck out’’ armor units to seriously degrade a structure.

5. Damage can be caused by freezing and expansion of seawater in cracks and

other small openings of structural members.

Earthquakes

Besides the damage caused by earthquake-generated tsunamis that arrive at the
coast, earthquakes can cause direct damage to the coast in a variety of ways.
Direct ground shaking can cause structural excitation and damage over a broad
region surrounding the earthquake epicenter. Near the epicenter, fault displacement can cause uplift or subsidence of the earth’s surface which can have a major
impact of coastal projects that survive the shaking. (The 1964 Alaskan earthquake caused uplift of about 2 m at Cordova, Alaska which reduced the water
depths in a small boat basin from 4 m to less than 2 m.) Earthquakes can cause
underwater and shoreline landslides which can damage structures and modify
nearshore hydrography. Also, earthquake-induced vibrations of the ground
mass can cause compaction of cohesionless soils to produce settlement or
cause the liquiWcation of other soils to produce a quick condition resulting in
the sinking or overturning of structures.

Vessels

During berthing operations, damage may occur to both the dock fendering
systems, dolphins and the vessel being docked. The problem may result from
navigation error or the loss of vessel propulsion while docking. Or it may result
from movement of a moored vessel caused by harbor seiching. Typically, the
forces are absorbed both by the fendering system as well the structure supporting
the fenders.

7.8 Wave–Structure Interaction

The primary concern when waves interact with structures is the stability of the
structure when it is exposed to wave-induced forces. For breakwaters, seawalls,
revetments and, to some extent, jetties there is the additional concern of wave
energy passing through or over the structure to cause problems in the lee of the


-----

236 / Basic Coastal Engineering

structure. The transmission of wave energy past Xoating breakwaters has been
discussed in Section 7.4. When waves attack rubble mound breakwaters and
jetties, some wave energy is dissipated and some energy is reXected. The remaining energy may pass through the structure or pass over the structure by running
up the structure face, overtopping the structure crest, and regenerating waves in
the lee of the structure. For seawalls and revetments having land in their lee,
wave energy that is not reXected and dissipated will also cause runup and
possible overtopping to produce Xooding and possible damage to the area
behind the structure.

Owing to the nature of the processes involved, quantitative design information

on wave reXection, runup, overtopping, and transmission is derived primarily
from physical experiments, mostly at reduced scale in wave Xumes and basins.
Besides the characteristics of the incident waves, the results of these processes are
very dependent on the proWle geometry, surface roughness, and porosity of the
speciWc structures. Consequently, although a fairly broad range of structures
have been investigated, speciWc information is not available for every type of
structure the designer may encounter. The designer must use strong judgement in
interpolating and extrapolating the available results, and if the project is of
suYcient importance may have to resort to model tests.

Results of wave reXection, runup, overtopping, and transmission tests for the

various types of structures investigated are found mainly in the reports from the
laboratories that completed the studies as well as journal and conference papers
(see Chapter 1) that summarize the experimental results. The best overall summary of results is found in the U.S. Army Coastal Engineering Research Center
(1984). Wave reXection and runup were brieXy discussed in Sections 2.7 and 2.9,
respectively.

Wave ReXection

A good summary of much of the work on wave reXection from structures can be
found in Seelig and Ahrens (1981) and Allsop and Hettiarachchi (1988). A
general equation for the reXection coeYcient for sloped coastal structures may
be written


Cr ¼ b þaI Ir[2] r[2]


(7:19)


where a and b depend primarily on the structure surface condition and to a lesser
extent on the slope and whether monochromatic or irregular waves are used. Ir is
the Iribarren number, deWned as

m
Ir ¼ pffiffiffiffiffiffiffiffiffiffiffiffiH=Lo (7:20)


-----

Coastal Structures / 237

For stone mound structures and conservative calculations Seelig and Ahrens
(1981) recommend that a ¼ 0:6 and b ¼ 6:6 be used. For structures with concrete
armour units Allsop and Hettiarachchi (1988) recommend a ¼ 0:56 and b ¼ 10:0
for dolos and a ¼ 0:48 and b ¼ 9:62 for tetrapods.

Wave Runup

Monochromatic wave runup R on a smooth impermeable slope, when the water
depth at the toe of the slope is between 1 and 3 times the deep water unrefracted
wave height, can be predicted using Figure 2.15. (Similar Wgures are available for
other toe water depths from the U.S. Army Coastal Engineering Research
Center. 1984). For a stone mound structure this should be reduced by a factor
r having a value of 0.5 to 0.8 (see Table 2.1).

For irregular wave runup it is often assumed that the runup has a Rayleigh

distribution so


Rp
Rs


�ln (1=p)�1=2

¼

2


(7:21)


where Rp is the runup associated with a particular probability of exceedence p
and Rs is the runup of the incident signiWcant wave height as if it were a
monochromatic wave. Note that Rp is not the average runup of the upper p
fraction; it is the runup exceeded by the upper p fraction of the runups. The latter
is most appropriate for determining desired structure crest elevations.

Wave Overtopping

If the elevation of wave runup on the face of a structure suYciently exceeds the
crest elevation, water will Xow over the structure crest to the lee of the structure.
To evaluate potential Xooding conditions in the lee of the structure and to design
a system for removal of the water during a storm, it is necessary to predict the
wave-induced overtopping Xow rate (volume/time/unit length of structure).

No simple relationship is available to predict overtopping rates. The U.S. Army

Coastal Engineering Research Center (1984) presents an empirical equation that
requires the estimation of two coeYcients, with very limited data given on which to
base anestimatefor these coeYcients.Results fromtheuse ofthisequationare very
approximate at best.If determination of overtopping rates is important ina coastal
project design, consideration should be given to the conduct of model studies. For
some empirical data on overtopping of breakwaters and seawalls see Goda (1985),
Ahrens and Heimbaugh (1986), and Aminti and Franco (1988).

Wave Transmission

If an overtopped structure has water in its lee, the overtopping Xow will generate
waves in the lee of the structure. Also, if the structure is suYciently permeable,


-----

238 / Basic Coastal Engineering

some wave energy will propagate through the structure. However, for most
breakwaters a core is provided so that there is essentially no transmission of
windgenerated waves through the structure.

Seelig (1980) conducted a very extensive set of experiments of wave transmis
sion by overtopping of rubble mound structures. He found that most of the
transmitted wave energy had the same frequency as the incident waves, but a
signiWcant portion of the energy had higher frequencies that were harmonics of
the incident frequency.

Seelig presented a simple formula that can be used to estimate the transmission

coeYcient for rubble mound breakwaters:

Ct ¼ C(1 � F =R) (7:22)

where F is the freeboard (vertical distance from the MWL to the structure crest),
R is the runup that would occur if the structure crest were suYciently high for no
overtopping to occur, B is the structure crest width, ds is the water depth at the
structure toe and

C ¼ 0:51 � [0][:][11][B] (7:23)

ds þ F

It is recommended that Eq. (7.22) be applied to the relative depth (ds=gT [2]) range
of 0.03 to 0.006 and the range of B=(ds þ F ) between 0 and 32 as these are the
ranges employed in the data collection.

Madsen and White (1976) developed a numerical procedure for calculating the

transmission coeYcient for waves transmission through a layered stone structure. As indicated above, this would only likely be important for wave periods
signiWcantly greater than those found in the wind wave range.

For low crested stone mound structures, van der Meer and Angremond (1992)

presented a wave transmission coeYcient curve similar to that shown in Figure
7.10. Given the freeboard (which would be negative for a submerged crest) and
the incident wave height one can estimate the transmission coeYcient.

7.9 Selection of Design Waves

An important aspect of the design of coastal structures is the selection of design
wave conditions for the structure. There are several components to this selection
process, most of which have been presented in other chapters of this text. The
overall approach is summarized herein. For more detail see Sorensen (1993).

To start, a wave data base for the site must be established. This typically

involves the collection of information on the wave signiWcant height and period
from the important directions of wave approach and for as long a time period as


-----

Coastal Structures / 239

0 1 2

F / Hi


Ct


1.0

0.8

0.6

0.4

0.2

0
−2 −1


Figure 7.10. Transmission coeYcient versus dimensionless freeboard for a low crested

breakwater. (ModiWed from van der Meer and Angremond, 1992.)

is possible. This data base may be derived from wave hindcasts using historic
meteorological data (Chapter 6) and/or wave measurements made at the site
(Chapter 9). The wave data base is then used to conduct an extreme wave
analysis to establish the signiWcant wave height having a particular return period
or probability of occurrence (Chapter 6).

This wave height is commonly determined for a deep water point oVshore of

the structure’s location. This height must be transferred by refraction, shoaling,
and possibly diVraction analysis (Chapters 2 through 4) to the location of the
structure. To do so, the designer must select a design water level (Chapter 5)
having a return period related to that of the design wave height.

A design wave period or periods must also be selected. If a suYcient data base

is available, a return period analysis can also be done for the signiWcant or
spectral peak wave period. Otherwise one can simply select a wave period or
range of periods that relate to the selected design wave height. For rubble mound
structures this might be just the signiWcant or spectral peak period but, for rigid
structures where wave/structure resonance problems are possible, a range of
periods bracketing the signiWcant period might be investigated. The lower limit
of this range would be set by steepness limits for breaking in deep water. Battjes
(1970) recommends that this lower limit be set by

�32p �1=2

T
¼

g [H][s]


where Hs is the signiWcant height for the return period of interest.


-----

240 / Basic Coastal Engineering

When the design wave or waves is(are) transferred to the structure location,

the Rayleigh distribution can be employed to determine the Hn value to use for
the structure design (Chapter 6). Typically rubble mound structures are designed
for Hs or H10 as discussed above while more rigid structures such as pile
structures and vertical walls would employ a higher wave such as H1 or Hmax.
The wave height at the structure may be limited by the height of a wave that
breaks at some distance (say 0:5 Xp; Chapter 2) seaward of the structure.

Some Design Wave Examples

Saint John Deep, Canada. As part of the design eVort for a proposed deep sea
terminal at St. John, New Brunswick, Canada, Khanna and Andru (1974)
carried out a wave climate study for the site. St. John Deep is on the Bay of
Fundy which opens through the Gulf of Maine to the Atlantic Ocean. Both
waves generated locally and waves approaching the site from the Atlantic Ocean
were of interest in the determination of expected design extreme wave heights.
For a one-year period wind measurements were made at the site and wave
measurements (using an accelerometer buoy, see Section 9.2) were made at a
point oVshore in water about 40 m deep. Owing to instrument malfunctions,
wind records were obtained for 61% of the time and the monthly wave data
collection varied from 54.2% to 92.4 % of the time. Also, eighteen years of wind
records were available from a local airport. A comparison of the wind roses for
the 18-year airport record and the one year of measurements from the site,
indicated that diVerences were not large. Thus, the 18 years of airport wind
records could be used for local wave hindcasts. They used the SMB method
(Section 6.6) for these hindcasts. A third source of wave data was from visual
observations made at a weather ship in the Gulf of Maine. Wave refraction
analyses, using the dominant range of wave periods, were carried out to transpose the waves from the Gulf of Maine to the site. Extreme wave height
projections for the site were then made using Weibull, log normal, and Gumbel
probability distributions for the one year of measured wave data. The results of
the local hindcasts and the transposed Gulf of Maine wave observations were
used to reinforce conWdence in the measured wave projections.

Sines, Portugal. The dolos-armoured stone mound breakwater at the Port of

Sines in Portugal, is directly exposed to wave attack from the Atlantic Ocean.
The breakwater was very seriously damaged by waves from a storm during
February 1978 and additional damage was done during storms in December
1978 and February 1979. In order to support an eVort to understand the speciWc
causes of the damage that occurred and to provide support for the redesign of
the breakwater, extensive studies of the wave climate at the site were carried out
by Mynett, et al. (1983).

A numerical wave hindcasting model was employed to hindcast wave condi
tions for 20 major storms that occurred during the period 1956 to 1980, including


-----

Coastal Structures / 241

the three storms that did damage to the breakwater. Directional wave spectra
were computed at six-hour intervals during the strength of each storm. The
hindcast wave spectra and associated signiWcant wave heights were compared,
when possible, with ship observations and available wave gage measurements
made during the particular storms. This was done to conWrm the numerical wave
hindcasts. Monochromatic wave numerical calculations and physical model studies were then employed to refract and shoal the waves to the site. Extreme wave
predictions were also made from the wave hindcasts for the 20 major storms.

7.10 Summary

A primary focus of this chapter has been the determination of wave loadings on
the various types of structures that are constructed in the coastal zone. This leads
to the structural analysis of these structures so they may be designed. For rubble
mound structures the incident wave conditions lead directly to a selection of the
required armor stone size which, in turn, largely dictates the cross-section
geometry of the structure. Other factors that enter the design of many structures
include the wave reXection, runup, overtopping, and transmission past the
structure.

The functional design of coastal structures also requires an analysis of their

required length, plan shape, and position. For structures such as breakwaters
this largely involves a wave refraction/diVraction analysis to see if the required
protection will be achieved. But for structures on the shore such as groins and
jetties or seawalls and revetments, and for oVshore segmented breakwaters
designed to stabilize a beach, the interaction of these structures with coastal
zone sediment transport processes is also important. Coastal zone transport
processes and the eVect of coastal structures are presented in Chapter 8.

7.11 References

Ahrens, J.P. and Heimbaugh, M.S. (1986), ‘‘Irregular Wave Overtopping of Sea Walls,’’ in

Proceedings, Oceans ’86 Conference, Institute of Electronic and Electrical Engineers,
Washington, DC, pp. 96–103.

Allsop, N.W.H. and Hettiarachchi, S.S.L. (1988), ‘‘ReXections from Coastal Structures,’’

in Proceedings, 21st International Conference on Coastal Engineering, American Society
of Civil Engineers, Malaga, Spain, pp. 782–794.

Aminti, P. and Franco, L. (1988), ‘‘Wave Overtopping on Rubble Mound Breakwaters,’’

in Proceedings, 21st International Conference on Coastal Engineering, American Society
of Civil Engineers, Malaga, Spain pp. 770–781.

Baird, W.F. and Hall, K.R. (1984), ‘‘The Design of Breakwaters Using Quarried Stones,’’

in Proceedings, 19th International Conference on Coastal Engineering, American Society
of Civil Engineers, Houston, pp. 2580–2591.


-----

242 / Basic Coastal Engineering

Battjes, J.A. (1970), ‘‘Long-Term Wave Height Distribution at Seven Stations Around the

British Isles,’’ National Institute of Oceanography, Report A44, United Kingdom.

Beattie, J.F., Brown, L.P., and Webb, B. (1971), ‘‘Lift and Drag Forces on a Submerged

Circular Cylinder,’’ in Proceedings, OVshore Technology Conference, Houston, paper
1358.

Blumberg, R. and Rigg, A.M. (1961), ‘‘Hydrodynamic Drag at Supercritical Reynolds

Numbers,’’ presented at American Society of Mechanical Engineers meeting, Los
Angeles.

Brater, E.F. and Wallace, R. (1972), ‘‘Wave Forces on Submerged Pipelines,’’ in Proceed
ings, 13th Conference on Coastal Engineering, American Society of Civil Engineers,
Vancouver, pp. 1703–1722.

Brown, R.J. (1967), ‘‘Hydrodynamic Forces on a Submarine Pipeline,’’ Journal, Pipeline

Division, American Society of Civil Engineers, March, pp. 9–19.

Bruun, P. (1989), Port Engineering, Fourth Edition, Gulf, Houston.

Chakrabarti, S.K. and Tam, W.A. (1973), ‘‘Gross and Local Wave Loads on a Large

Vertical Cylinder—Theory and Experiment,’’ in Proceedings, OVshore Technology
Conference, Houston, paper 1818.

Cox, J.C. and Clark, G.R. (1992), ‘‘Design Development of a Tandem Breakwater System

for Hammond Indiana,’ in Proceedings, Coastal Structures and Breakwaters Conference, Thomas Telford, London, 111–121.

Garrison, C.J. and Rao, V.S. (1971), ‘‘Interaction of Waves with Submerged Objects,’’

Journal, Waterways, Harbors and Coastal Engineering Division, American Society of
Civil Engineers, May, pp. 259–277.

Gaythwaite, J.W. (1990), Design of Marine Facilities, Van Nostrand Reinhold, New York.

Giles, M.L. and Eckert, J.W. (1979), ‘‘Determination of Mooring Load and Transmitted

Wave Height for a Floating Tire Breakwater,’’ Coastal Engineering Technical Aid 79-4,
U.S. Army Coastal Engineering Research Center, Ft. Belvoir, VA.

Giles, M.L. and Sorensen, R.M. (1979), ‘‘Determination of Mooring Loads and Wave

Transmission for a Floating Tire Breakwater,’’ in Proceedings, Coastal Structures ’79
Conference, American Society of Civil Engineers, Arlington, VA, pp. 1069–1085.

Goda, Y. (1985), Random Seas and Design of Maritime Structures, University of Tokyo

Press, Tokyo.

Grace, R.A. (1971), ‘‘The EVects of Clearance and Orientation on Wave Induced Forces

on Pipelines,’’ Look Laboratory Report 15, University of Hawaii, Honolulu.

Grace, R.A. (1978), Marine Outfall Systems: Design, Planning and Construction, Prentice
Hall, Englewood CliVs, NJ.

Grace, R.A. and Nicinski, S.A. (1976), ‘‘Wave Force CoeYcients from Pipeline Research

in the Ocean,’’ in Proceedings, OVshore Technology Conference, Houston, paper 2767.

Hales, L.Z. (1981), ‘‘Floating Breakwaters: State-of-the-Art Literature Review,’’ Tech
nical Report 81-1, U.S. Army Coastal Engineering Research Center, Ft. Belvoir, VA.

Harmes, V.W., Westerink, J.J., Sorensen, R.M., and McTamany, J.E. (1982), ‘‘Wave

Transmission and Mooring Force Characteristics of PipeTire Floating Breakwaters,’’


-----

Coastal Structures / 243

Technical Paper 82-4, U.S. Army Coastal Engineering Research Center, Ft. Belvoir,
VA.

HelWnstine, R.A. and Shupe, J.W. (1972), ‘‘Lift and Drag on a Model OVshore Pipeline,’’

in Proceedings, OVshore Technology Conference, Houston, paper 1578.

Herbich, J.B. (1981), OVshore Pipeline Design Elements, Marcel Dekker, New York.

Herbich, J.B. (1990), Handbook of Coastal and Ocean Engineering, Gulf, Houston.

Herbich, J.B. and Shank, G.E. (1970), ‘‘Forces Due to Waves on Submerged Structures:

Theory and Experiment,’’ in Proceedings, OVshore Technology Conference, Houston,
paper 1245.

Hoerner, S.F. (1965), Fluid-Dynamic Drag, Third Edition, published by the author.

Hogben, N., Miller, B.L., Searle, J.W., and Ward, G. (1977), ‘‘Estimation of Fluid

Loading on OVshore Structures,’’ Part 2, in Proceedings of the Institute of Civil Engineers, London.

Hudson, R.L. (1959), ‘‘Laboratory Investigation of Rubble Mound Breakwaters,’’ Jour
nal, Waterways and Harbors Division, American Society of Civil Engineers, September,
pp. 93–121.

Khanna, J. and Andru, P. (1974), ‘‘Lifetime Wave Height Curve for Saint John Deep,

Canada,’’ in Proceedings, Conference on Ocean Wave Measurement and Analysis,
American Society of Civil Engineers, New Orleans, pp. 301–319.

Knoll, D. and Herbich, J.B. (1980), ‘‘Simultaneous Wave and Current Forces on a

Horizontal Cylinder,’’ in Proceedings, 17th International Conference on Coastal Engineering, American Society of Civil Engineers, Sydney, pp. 1743–1760.

Kowalski, T. (1974), ‘‘1974 Floating Breakwater Conference Papers,’’ Marine Technical

Report 24, University of Rhode Island, Kingston.

Lyons, C.G. (1973), ‘‘Soil Resistance to Lateral Sliding of Marine Pipelines,’’ in Proceed
ings, OVshore Technology Conference, Houston, paper 1876.

Madsen, O.S. and White, S.M. (1976), ‘‘ReXection and Transmission Characteristics of

Porous Rubble-Mound Breakwaters,’’ Miscellaneous Report 76-5, U.S. Army Coastal
Engineering Research Center, Ft. Belvoir, VA.

Morison, J.R., Johnson, J.W., O’Brien, M.P., and Schaaf, S.A. (1950), ‘‘The Forces

Exerted by Surface Waves on Piles,’’ Petroleum Transactions, American Institute of
Mining Engineers, Vol. 189, pp. 145–154.

Mynett, A.E., de Voogt, W.J.P., and Schmeltz, E.J. (1983), ‘‘West Breakwater-Sines,

Wave Climatology,’’ Proceedings, Coastal Structures ’83 Conference, American Society
of Civil Engineers, Arlington, VA, pp. 17–30.

Parker, M.E. and Herbich, J.B. (1978), ‘‘Drag and Inertia CoeYcients for Partially-Buried

OVshore Pipelines,’’ in Proceedings, OVshore Technology Conference, Houston, paper
3072.

Peyton, H.R. (1968), ‘‘Ice and Marine Structures,’’ Ocean Industry, Houston (three

articles: March, September, and December).

Port and Harbor Research Institute (1994), Proceedings, Wave Barriers in Deep Water

Workshop, Yokosuka, Japan.


-----

244 / Basic Coastal Engineering

Sarpkaya, T. and Isaacson, M. (1981), Mechanics of Wave Forces on OVshore Structures,

Van Nostrand Reinhold, New York.

Seelig, W.N. (1980), ‘‘Two-Dimensional Tests of Wave Transmission and ReXection

Characteristics of Laboratory Breakwaters,’’ Technical Report 80–1, U.S. Army
Coastal Engineering Research Center, Ft. Belvoir, VA.

Seelig, W.N. and Ahrens, J.P. (1981), ‘‘Estimation of Wave ReXection and

Energy Dissipation CoeYcients for Beaches, Revetments and Breakwaters,’’

Technical Paper 81–1, U.S. Army Coastal Engineering Research Center, Ft. Belvoir,
VA.

Simiu, E. and Scanlan, R.H. (1986), Wind EVects on Structures, John Wiley, New York.

Sorensen, R.M. (1993), Basic Wave Mechanics for Coastal and Ocean Engineers, John

Wiley, New York.

Tsinker, G.P. (1995), Marine Structures Engineering, Chapman and Hall, New York.

U.S. Army Coastal Engineering Research Center (1984), Shore Protection Manual, U.S.

Government Printing OYce, Washington, DC.

van der Meer, J.W. (1988), ‘‘Rock Slopes and Gravel Beaches Under Wave Attack,’’ Delft

Hydraulics Communication 396, Technical University, Delft, The Netherlands.

van der Meer, J.W. (1995), ‘‘A Review of Stability Formulas for Rock and Riprap Slopes

Under Wave Attack,’’ Chapter 13, River, Coastal and Shoreline Protection (Thorne,
C.R., Abt, S.R., Barends, F.B.J., Maynord, S.T., and Pilarczyk, K.W., Editors), John
Wiley, New York.

van der Meer, J.W. and Angremond, K. (1992), ‘‘Wave Transmission at Low-Crested

Breakwaters,’’ Coastal Structures and Breakwaters, Institution of Civil Engineers,
Thomas Telford, London, pp. 25–41.

van der Meer, J.W. and Pilarczyk, K.W. (1990), ‘‘Stability of Low-Crested and Reef

Breakwaters,’’ in Proceedings, 22nd International Conference on Coastal Engineering,
American Society of Civil Engineers, Delft, pp. 1375–1388.

Ward, D.L. and Ahrens, J.P. (1992), ‘‘Laboratory Study of a Dynamic Berm Revetment,’’

Technical Report CERC-92–1, U.S. Army Waterways Experiment Station, Vicksburg,
MS.

Weggel, J.R. (1981), ‘‘Some Observations on the Economics of ‘‘Overdesigning’’ Rubble
Mound Structures with Concrete Armor,’’ Coastal Engineering Technical Aid 81–7,
U.S. Army Coastal Engineering Research Center, Ft. Belvoir, VA.

Willis, D.H., Baird, W.F., and Magoon, O.T. (1988), Berm Breakwaters: Unconventional

Rubble-Mound Breakwaters, Conference Proceedings, American Society of Civil Engineers, Ottawa.

Woodward—Clyde Consultants (1980), ‘‘Assessment of the Morison Equation,’’ Report

N68305–80-C–0007 For the U.S. Naval Facilities Engineering Command, Washington,
DC.


-----

Coastal Structures / 245


7.12 Problems

1. The Xow velocity of water approaching a 1 m diameter sphere is given by

V ¼ 1:2 þ 1:75t[1][:][5] where V is in m/s and t is in s. Determine the total force on the
sphere at t 2 s. Consult an elementary Xuid mechanics text for any needed
¼
coeYcients not given in this text.

2. A sphere having a diameter of 0.7 m is tethered 5 m below the still water

level where the water depth is 10 m. A 6 s, 1 m high wave passes the sphere.
Determine and plot the horizontal components of the drag, inertia, and total
force on the sphere through one wave period. Assume Cd ¼ 0:6 and Cm ¼ 1:5.

3. A vertical 1 m diameter circular pile standing in water 14 m deep is sub
jected to a 4 m high, 9 s wave. Calculate and plot the drag, inertia, and total
force distributions along the pile at the instant that the wave crest is 20 m
seaward of the pile.

4. For the pile and wave condition given in Problem 3, determine the time

interval before the arrival of that wave crest at which the maximum force occurs
and determine that force. What is the maximum moment around the sea Xoor
acting on the pile?

5. A horizontal cylindrical cross brace on an oVshore tower having a 0.8 m

diameter and a length of 9 m is located 6 m below the still water level. The water
depth is 30 m. For a 12 s, 5 m high wave approaching normal to the axis of the
brace, calculate and plot the drag, inertia and total horizontal forces on the brace
as a function of time for one wave period.

6. The design wave for a lake has deep water values of

Hs ¼ 2:5 m and Ts ¼ 4:6 s. The wave approaches shore with a Kr ¼ 0:87 at the
end of a pier located in water 5 m deep. The piles at the end of the pier have a
diameter of 0.3 m. Determine the design moment around the sea Xoor and
discuss the basis of the design wave you selected.

7. A 0.8 m diameter submerged pipeline resting on an essentially horizontal

sea Xoor is subjected to a 4 m high, 11 s wave propagating normal to the pipeline
axis. The water depth is 14 m. Assume a bottom friction coeYcient of 0.8 and
Cd ¼ 1:8and Ct ¼ 2:5. What minimum weight per meter of length should the
pipeline have if it relies on its weight for stability?

8. A Xoating tire breakwater is installed at a marina where the water depth is

4 m. The breakwater width in the direction of wave propagation is 12 m. If the
incident wave height is 1.2 m with a period of 2.1 s what is the wave height in the
lee of the breakwater? What is the wave height in the lee if the wave period is
4.1 s?

9. A revetment having a proWle similar to that shown in Figure 7.5 is placed on

the face of a small earth dam (1:3.5 slope). The toe of the revetment is at a depth of


-----

246 / Basic Coastal Engineering

2 m below the design water level and the bottom slope in front of the revetment is
1:50. For a design wave in deep water having Hs ¼ 1:9 m andTs ¼ 4:5 s determine
the median size armor stone required for zero damage of the structure. Assume
Kr ¼ 0:78. Select a desired crest elevation for the revetment.

10. What weight concrete tribars are needed as armor units for a breakwater

(cross-section similar to Figure 7.4) if no damage is allowed and minor wave
overtopping is assumed? The design water depth at the seaward toe of the
breakwater is 6 m and the sea Xoor in front of the breakwater has a 1:20 slope.
A design wave with Hs ¼ 4:9 m and Ts ¼ 8 s in deep water (assume Kr ¼ 1:0) is
to be used.

11. A submerged crest stone mound breakwater is constructed in water that is

5.1 m deep with its crest located 1.0 m below the still water level. The incident
design wave has a signiWcant height of 1.45 m and a signiWcant period of 4.4 s.
What median diameter stone is required for zero damage stability (assume
speciWc gravity of stone is 2.65) if the face slope is 1:1.75?

12. Consider the breakwater in Problem 11; however, the crest is located

1.0 m above the design MWL. What median diameter armor stone is required
for a stable structure?

13. A rigid vertical wall has a reXection coeYcient of 0.9. The water depth at

the toe of the structure is 3 m. For an incident wave having a height of 1.2 m and
a period of 4.5 s, plot the total pressure along the wall when the crest of the
standing wave is at the wall. Compare this to the linear distribution commonly
assumed for design purposes.

14. A rigid vertical wall has a reXection coeYcient assumed to be 0.95. The

water depth at the toe of the wall is 4.2 m. What is the maximum moment
around the toe of the wall for a 1 m, 6 s wave, assuming that a wave trough
acts at the back side when a crest acts at the front?

15. A vertical wall is constructed on a beach with a 1:15 slope. The toe of the

wall is at an elevation of 0.5 m above the mean water level. For a normally
þ
incident 2 m, 7 s design wave estimate the dynamic pressure on the wall. If this
pressure is assumed to be constant across the wall, what is the total design force
on the wall?

16. For the breakwater in Problem 10, estimate the wave reXection coeYcient.

If the crest height is located 2.4 m above the design water level and the crest
width is 3.5 m, estimate the transmitted wave height owing to wave overtopping.

17. For the breakwater in Problem 10, what height above the design water

level must the breakwater crest have if for the given wave condition only 10% of
the waves are to run up above the crest elevation?

18. For the submerged breakwater in Problem 11, and the given wave condi
tion, estimate the height of the transmitted wave.


-----

## 8

### Coastal Zone Processes

The zone of interest in this chapter is that segment of the coast located between

the oVshore point where shoaling waves begin to move sediment and the onshore
limit of active marine processes. The latter is usually delineated by a dune Weld or
cliV line, unless a line of structures is constructed along the coast. Most of the
world’s coastlines consist of sandy beaches. In some locations the beach is
covered partially or completely with coarser stone known as shingle. Many
shorelines consist of long beaches occasionally interrupted be a river, coastal
inlet, or rocky headland. In other locations there are short pocket beaches
between large headlands that limit the interchange of sediment between adjacent
beaches.

Although sandy beaches predominate, some coastlines are fronted by steep

cliVs at the water’s edge that may or may not have a small beach at their toe.
Where wave and current action is relatively mild and a river provides large
deposits of sediment a delta may extend seaward of the line of the coast. The
emphasis in this chapter is on those sections of the coast having a sandy beach.

Beach and nearshore sediments are continually responding to direct wave

action, wave-induced littoral currents, currents induced by the wind and tide,
and the wind directly. However, direct wave action and wave-induced littoral
currents are usually the dominant factor in shaping beaches, except near coastal
inlets where tide- and river-induced Xow will typically dominate.

The stability of a section of sedimentary shoreline depends on a balance

between the volume of sediment available to that section and the net onshore–
oVshore and alongshore sediment transport capacity of waves, wind, and currents in that section. The shoreline may thus be eroding, accreting, or remaining
in equilibrium. If equilibrium does exist, it is usually a ‘‘dynamic equilibrium’’
where the shoreline is responding to continuously variable winds, waves, and
currents. Also, the supply of sediment to the beach is usually variable in time and
space. Dynamic equilibrium usually means that the average shoreline position is
relatively stable over a period of months or years while the instantaneous
position undergoes short-term oscillations.


-----

248 / Basic Coastal Engineering

Construction of structures, dredging of channels and harbors, beach nourish
ment with sand, and other projects in the coastal zone have often been carried
out to limit or reverse shoreline erosion or accretion. At times, these projects
have upset the existing dynamic equilibrium of adjacent shorelines. The result is
a continuing shoreline change ultimately to reach a new equilibrium condition
that may or may not be desirable.

Coastal developments can aVect coastal zone processes by: (1) changing the

rate and/or characteristics of sediment supplied to the coast, (2) adjusting the
level of wave energy Xux to the coast, and (3) directly interfering with coastal
sediment transport processes. Two examples of the Wrst eVect are the construction of a dam that traps sediment on a river that otherwise would deliver the
sediment to the coast, and the periodic placement of sand on a beach, to nourish
the beach. Examples of the second and third eVects respectively are: construction
of a shore parallel oVshore breakwater that intercepts waves approaching the
shore to, in turn, reduce the wave-induced alongshore sediment transport; and
construction of a shore perpendicular groin across the surf zone to directly
interrupt wave-induced alongshore sediment transport.

This chapter Wrst considers the characteristics of the sediment on a beach.

Then shore normal and alongshore transport processes and resulting beach
changes, including those caused by structures, are presented. Numerical models
for predicting beach change are discussed. Beach nourishment, sediment bypassing past shoreline obstructions, and dune stabilization are presented. The chapter is concluded with a discussion of the concept of a sediment budget for a
coastal segment, a useful tool in understanding beach behavior.

8.1 Beach Sediment Properties and Analysis

Of greatest interest are those physical properties of beach sediments that control
their response to wind, wave, and current action and, in turn, are important to the
design of engineering works in the coastal zone. We are primarily interested in
noncohesive granular sediments. Physical properties of these sediments include:

1. Petrology or chemical constituents of the sediment grains

2. SpeciWc gravity of the grain materials and the bulk speciWc weight of the

granular mass

3. Bulk porosity and permeability of the granular mass

4. Grain shape

5. Representative grain sizes and size distribution

For engineering purposes, the representative grain sizes and size distribution

are the most important beach sediment properties and the only properties
commonly measured and employed in deWning sediment properties.


-----

Coastal Zone Processes / 249

The common procedures for measuring sediment size and size distribution—

namely sieving and settling tube analysis—include the eVects of some of the
other properties. Sieving incorporates some aspects of grain shape and settling
tube analysis incorporates grain shape and speciWc gravity. In the latter grain
shape is incorporated in a better way in that the hydrodynamic behavior, as
aVected by shape, comes into play.

It can also be shown that the permeability of a granular soil mass is related to

the sediment size and size distribution (e.g., see Krumbein and Monk, 1942).

Most beach sands consist predominately of quartz (2.65 speciWc gravity) with

smaller portions of feldspar (2.54 to 2.64 s.g.) and a small content of a variety of
heavy minerals (s.g. greater than 2.87). In tropical regions such as Florida and
the Caribbean, beach sands are commonly derived from shallow water reefs and
are largely calcium carbonate (2.72 s.g.).

Representative Size and Size Distribution

Sediment grains found in the coastal zone will have a wide variety of shapes.
Grain sizes are given as a grain diameter. Whether the grain size measurement
was done by sieving or settling tube analysis will yield a slightly diVerent grain
diameter for a given grain shape. The analysis technique should be considered
when comparing grain size analyses.

A full range of sediment sizes from clay (less than one micron diameter) to

gravel and boulders (tens of centimeters diameter) may be found in the coastal
zone. Except for shingle beaches, most beaches consist of sand with grain
diameters typically between 0.1 and 1 mm.

A number of formal sediment size classiWcations have been proposed; a

commonly used classiWcation is that proposed by Wentworth (1922) and given
in Table 8.1. Since most sediment sample size distributions are skewed with a
preponderance of Wner sizes, the Wentworth scale is logarithmic with base 2.
This allows a better deWnition of the Wner sizes.

Many physical scientists deWne grain diameter by the phi unit f proposed by

Krumbein (1936) and based on the Wentworth size classiWcation. For a grain
diameter d given in mm,

f ¼ � log2 d (8:1)

where the minus sign is used so the more common sand grain diameters having
d > 1 mm will have a positive phi value. Wentworth size class boundaries are
thus whole numbers in phi units. However, the phi unit system can cause some
confusion because phi units increase with decreasing particle size and each whole
number interval represents a diVerent range of particle sizes.

The grain size distribution and representative grain sizes are best deWned by

standard statistical techniques. Sediment sample size distributions are commonly
represented by a cumulative size frequency distribution, which is a plot of the


-----

250 / Basic Coastal Engineering

Table 8.1 Wentworth Size ClassiWcation

Particle Diameter

Class mm phi units

Boulder
256 — �8

Cobble — 128 — �7

64 — �6

— 32 — �5

Pebble — 16 — �4

— 8 — �3

4 — �2

Gravel
2 — �1

Very coarse sand
1 — 0

Coarse sand
1/2 — 1

Medium sand
1/4 — 2

Fine sand
1/8 — 3

Very Wne sand
1/16 — 4

— 1/32 — 5

Silt — 1/64 — 6

— 1/128 — 7

1/256 — 8

cumulative percent of the grains having a diameter that is coarser (or Wner) than
a particular size versus grain size given either in mm or phi units. Figure 8.1 is an
example of such a distribution for a beach sand sample.

The important characteristics of a sediment sample cumulative size frequency

distribution can generally be deWned by three statistical parameters: the central
tendency (mean, median, or modal diameter), the dispersion or sorting (standard
deviation), and the possible asymmetry (skewness). The median diameter is easiest
to determine from a cumulative size frequency diagram and is less aVected by a
small percentage of extremely large or small sizes than is the mean, so it is usually
used to deWne central tendency. As sediment is transported down a river and
deposited at the coast, the coarser sizes often remain behind in the river bed and
the Wner sizes are usually deposited oVshore, so beach sediments are usually well
sorted sand (i.e, have a relatively narrow size range). As discussed above, beach
sand grain diameters are usually skewed toward the Wner sizes.

The most commonly used parameter in engineering practice to deWne a beach

sand sample is the median diameter d50 given in mm. For the sample depicted in
Figure 8.1 d50 ¼ 0:23 mm. Several other descriptive measures, based on sediment

|Class|mm|phi units|
|---|---|---|
|Boulder|256 — — 128 — 64 — — 32 — — 16 — — 8 — 4 — 2 — 1 — 1/2 — 1/4 — 1/8 — 1/16 — — 1/32 — — 1/64 — — 1/128 — 1/256 —|8 7 6 5 4 3 2 1 0 1 2 3 4 5 6 7 8|
|Cobble|||
|Pebble|||
|Gravel|||
|Very coarse sand|||
|Coarse sand|||
|Medium sand|||
|Fine sand|||
|Very Wne sand|||
|Silt|||
||||


-----

Coastal Zone Processes / 251


98

95

90

84
80

70

60

50

40

30

20
16

10

5


2


2.61

1.81 2.13

1.01


−1 0 1 2 3 4

Φ

2 1 0.5 0.25 0.125 0.0625

mm

Figure 8.1. Plot of typical sand sample size analysis.


Table 8.2. Sediment Sample Descriptive Measures

Measure Name DeWnition


Sorting Phi deviation measure sf ¼ [1]2 [(][f][84][ �] [f]

Skewness Phi skewness measure af ¼ [M][f][ �]sf[M][d][f]


after Inman, 1952.

size analyses, have been proposed to deWne the central tendency, sorting and
asymmetry of a sediment sample (see GriYths, 1967 for a listing and discussion of
these parameters). One system commonly used in engineering practice was developed by Inmann (1952). A portion of this system is presented in Table 8.2 where


-----

252 / Basic Coastal Engineering

f16, f50, and f84 are the16, 50, and 84%coarser phidiametersfromthe cumulative
frequency size distribution.

In an arithmetic normal distribution the spacing between the 16th and the 84th

percentiles is two standard deviations. This suggests the deWnition of the phi
deviation measure, which indicates the spread or sorting of the sample from the
median size. These percentiles are also used to deWne the phi mean diameter by
averaging the phi value at two separated reasonably representative values. The
phi skewness measure gives an indication of the displacement of the median
value from the mean value and thus indicates the sample skewness. The phi
deviation measure is used in the denominator so the phi skewness measure is
independent of the actual sediment size.

The descriptive measures deWned in Table 8.2, when evaluated for the sample

described by Figure 8.1 yield

Mdf ¼ 2:13

Mf ¼ (2:61 þ 1:01)=2 ¼ 1:81

sf ¼ (2:61 � 1:01)=2 ¼ 0:80
af ¼ (1:81 � 2:13)=0:80 ¼ �0:40

A discussion of beach sediment sampling and grain size analysis is presented in
Chapter 9.

8.2 Beach ProWles and ProWle Change

Waves that reach a sandy shore, then break and run up on the beach face, will
continually reshape the beach. This continuous reshaping occurs because the
incident wave characteristics (height, period, and/or approach direction) are seldom constant for anysigniWcant time span. Reshapingof the beach is caused by the
wave-induced currents that develop in the surf zone and, by the direct action of the
waves through turbulence generated by the breaking waves and the surge of water
up and down the beach face. Concurrent reshaping of the beach owing to waveinduced sediment transport takes place both in the on-/oVshore directions and in
the alongshore direction. Although these eVects occur together it is easier to
consider them separately. This section focuses on the natural beach proWle geometry and the wave-induced changes that occur for a typical shore-normal beach
proWle. Alongshore processes will be considered in the two subsequent sections.

Mechanisms Causing Beach ProWle Change

There are a number of mechanisms that can cause the transport of sand across a
beach proWle. Some of these mechanisms will only transport sand in the oVshore
direction leading to proWle retreat, while others will only transport sand onshore
building up the proWle. And, there are mechanisms that can cause either proWle


-----

Coastal Zone Processes / 253

buildup or retreat depending on the wave and water level conditions, local beach
slope and sand characteristics. These mechanisms are described below.

. As a wave propagates shoreward in the nearshore zone there is an asymmetry in the horizontal water particle velocities at the sea Xoor, with a
higher and shorter duration onshore velocity under the wave crest and a
lower and longer duration oVshore velocity under the wave trough. The
resulting shear stress exerted on a bottom sand grain depends on the water
particle velocity squared. Consequently, there will be a larger onshore
stress followed by a signiWcantly lower oVshore stress. The net bottom
stress will act in the onshore direction. The resulting onshore transport
tendency is increased owing to the fact that a certain threshold stress must
be exceeded for a bottom particle to move.

. Beaches typically slope seaward across the entire proWle (except for a short
segment on the landward face of oVshore bars). Thus, a component of
gravity will typically act in the oVshore direction on a bottom sand grain.

. Wave-induced setup in the surf zone will lead to a bottom return Xow in the
seaward direction (undertow) that will exert a seaward stress on sand grains.
Also, on a long segment of beach where a signiWcant alongshore current
develops, there may be spatially periodic seaward Xowing rip currents (see
Section 8.3) that can transport large volumes of beach sand seaward.

. Turbulencecausedbybreakingwavesinthesurfzonewillsuspendsediment–
the suspension being intermittent with the breaking of successive waves. The
net transport of sand will be controlled by the net time-integrated horizontal
Xow velocity during the interval of sediment suspension. This mechanism
may transport sediment in either the onshore or oVshore direction.

. Onshore winds will exert an onshore stress on the water surface and a consequent return Xow at the bottom that can assist in transporting sand seaward.

This summary indicates the complexity of mechanisms that operate to form a
beach proWle and to establish the grain size distribution across this proWle. This
complexity is compounded by the fact that the diVerent mechanisms have signiWcantly diVerent strengths and these relative strengths vary as the wave, wind
and water level conditions vary.

Beach proWles measured normal to the shoreline over the zone of active coastal

processes are of great importance to coastal engineering studies. This active
zonenormallyextendsfromtheonshorecliV,dune,orstructurelinetoapointoVshore
wherethereislittlesigniWcantwave-inducedsedimentmovement(atatypicaldepth
ofabout10 mfortheopenocean).OverthisactivezoneaportionofthebeachproWle
canchangedrasticallyinafewhoursbecauseofasuddenincreaseinwaveactivity.

Beach proWle data are important for an understanding and quantiWcation of

coastal zone processes and the related interaction of coastal structures with these


-----

254 / Basic Coastal Engineering

Coast Backshore Foreshore


Nearshore

Surf Zone

Breaker

Calm

wave profile


Coast Backshore Foreshore Nearshore

Beach

face

Surf Zone

Winter

Summer
berm

berm

Breaker

Dunes or Scarp MWL

cliff

Storm Longshore

wave bar

profile

Calm


Beach


Figure 8.2. Typical beach proWles (vertical scale exaggerated) and terminology.

processes. The total seasonal envelope of proWle change must be deWned, for
example, for the design of such coastal structures as groins, piers, seawalls, and
marine pipelines that cross the coastal zone, as well as for the establishment of
coastal boundaries and the design of beach nourishment projects.

Figure 8.2 shows typical somewhat idealized beach proWles. Progressing sea
ward from the dune, cliV, or structure line a beach proWle typically includes one
or two relatively Xat berms that slope landward, a seaward sloping foreshore
where the active wave runup on the beach face takes place, and a concave
nearshore proWle, possibly having one or more breakpoint bars lying approximately parallel to the shore. The above assumes a suYciently wide beach for
these features to develop. If the beach is narrow, the beach face may extend
directly to the dune, cliV, or structure line.

The dashed line in Figure 8.2 deWnes the proWle that would be established after

a relatively long period of calm wave action. Sand is slowly transported landward to build the beach face in the foreshore zone and to extend the berm
seaward, thus causing a steeper beach face proWle slope. With the appearance
of higher and steeper waves common during a period of storm activity sand is
transported seaward so the proWle can be expected to adjust to the form shown
by the solid line. The beach proWle in the vicinity of the mean water level is thus
cut back and the slope is Xaitened. A scarp will form at the edge of the berm. The
sand transported oVshore will build a larger oVshore bar around the point of
wave breaking. If the wave attack is severe or after a series of storms the proWle
may be cut back to the dune or cliV line, causing recession of these features.

At most coastal locations, storm waves predominate during the winter months

and calmer waves occur during the summer. Thus, the terms winter and summer
proWle are often used to deWne the two types of beach proWle. But hurricanes on
the Atlantic and Gulf coasts and summer storms in the PaciWc southern hemisphere can cause the recession of the beach proWle during the summer.


-----

Coastal Zone Processes / 255

The beach berm is constructed during calm wave periods when waves run up


on the beach face and deposit sand. Consequently, the elevation of the crest of
the berm is closely tied to the mean elevation of wave runup as the beach face is
building.

The beach face slope, which varies with the steepness of the incident waves as


discussed above, also depends on the sand size that constitutes the beach face.
This is demonstrated in Figure 8.3, which is a plot of the beach face slope as a
function of the median sand grain diameter (at the mid-tide elevation on the
beach face) for high-energy and low-energy wave exposure. For the same incident wave energy level a beach made of a coarser sand will have a steeper beach
face slope. Conversely, for a given sand size, beaches exposed to higher wave
energy will have a Xatter beach face slope (as discussed above). For example, the
beaches of the northern shores of New Jersey have typical average median grain
diameters of around 0.4 to 0.5 mm and beach face slopes around 1:10 to 1:15,
while the beaches on the southern shore (which have about the same wave
exposure) have typical average median grain diameters of around 0.15 to
0.25 mm and, consequently, much Xatter slopes around 1:40.

Nearshore bar geometry and spacing closely respond to the predominant wave


action. With the occurrence of higher waves a bar will move seaward (as will the
wave breaker line), and the size of the bar will grow. With the return of lower
waves the bar may be stranded at its seaward position while a new smaller bar is

1.0


0.8

0.6


0.4

0.2


High wave

energy

Low wave

energy


4 6 8 10 15 20 40 60 80 100


BEACH FACE SLOPE, l/m

Figure 8.3. Beach face slope versus median sand grain diameter for high and low wave


energy exposure. (ModiWed from Wiegel, 1964.)


-----

256 / Basic Coastal Engineering

formed closer to the shore. During extremely low waves no bars will be built.
Shore parallel bars are also less common where the tide range is large.

The occurrence of a calm or storm wave proWle depends on the beach sand

properties as well as the incident wave characteristics. One relationship, derived
from Kriebel et al. (1986), indicates that the parameter H0=Vf T, where Vf, is the
settling velocity of a sand grain in still water, appears to be a useful indicator of
proWle characteristics. When the value of this parameter exceeds about 2 to 2.5
an erosive or storm wave proWle will develop whereas when the value of this
parameter is less than about 2 to 2.5 the beach face accretes.

A beach proWle may recede as much as 30 m in the landward direction during

a single intense storm. If much of the beach sand is carried too far oVshore for
subsequent return to the beach face and the nearshore zone by calm waves, and
there is insuYcient net sand accumulation from alongshore transport processes,
permanent recession of the shoreline will result. Seelig and Sorensen (1973)
studied shoreline position changes during the past century at 226 points along
the 650 km long Texas coast. The MLW shoreline position at 50% of the points
showed a small rate of change of less than �2 m=year. But at 40% of the points a
net shoreline recession in excess of 2 m/year, with extreme rates in excess of
10 m/year, was observed. The remaining 10% of the points, mainly near jettied
inlet entrances, showed shoreline net advances in excess of 2 m/year.

The sand size, as indicated by the median grain size for a sample, will vary along

the beach proWle, particularly for beaches with coarse composite sizes. From a
study of samples from several PaciWc coast beaches, Bascom (1951) found the sand
to be the coarsest at the plunge point in the wave breaker zone where the highest
turbulence levels occur. The next coarsest sand was found on the berms, likely
because of the winnowing of Wner sizes by the wind. Where a dune Weld exists, the
dune sand was progressively Wner in the landward direction. Sand grain sizes also
progressively decreased in the seaward direction from the surf zone.

In addition to wind wave-induced beach proWle changes, there will be a

recession of the beach proWle if there is a relative rise in mean sea level as has
been historically happening along most coastlines of the world. Besides the
Xooding of a proWle caused by a relative rise in MSL, there will be an adjustment
of the proWle as sand is transported oVshore and the MSL position on the beach
face is shifted landward to produce a recession of the shoreline. Bruun (1962)
discussed this process and presented a procedure to analyze the distance a
shoreline will retreat owing to a given small rise in MSL. Weggel (1979) presents
techniques for the practical application of the Bruun procedure.

Equilibrium Beach ProWles

As discussed above, as the wave and water level conditions vary, the beach

proWle will respond by changing. A useful concept, however, is the equilibrium
beach proWle. This is the mean proWle that would occur when proWles are


-----

Coastal Zone Processes / 257

measured over a period of several years. This concept is useful for a variety of
coastal engineering analysis and design purposes including:

. Some numerical models for alongshore morphology change require a
representative beach proWle.

. When before and after beach proWles are required for the computation of
beach nourishment volumes.

. When analyses are to be conducted to deWne the impact of long term sea
level change.

. For analyses of the impact of coastal structures such as seawalls on the
resulting beach proWle.

For example applications of the equilibrium beach proWle concept to the

purposes listed above, see Dean (1991).

The most common form of an equation to deWne the equilibrium beach proWle is

z Ax[n]
¼

where z is the depth below the mean water level for a given distance x oVshore. The
power n is commonly taken as two-thirds based both on empirical data (Bruun,
1954 and Dean 1987) and on physical reasoning (see Dean and Dalrymple, 2002).
The coeYcient A is related to the settling velocity of sand grains in water which, in
turn, can be related to the sand grain particle diameter D. A useful relationship for
AisA ¼ 0:21 D[0][:][48] (Dean,1987)whereDisgiveninmmandAhastheunitsofm[1][=][3].

This equilibrium beach proWle equation deWnes a proWle that is concave and

has an increasing slope at given point for increasing sand grain diameters.
However, it also predicts an inWnite slope at the shoreline (x 0) so it should
¼
not be applied very close to the shoreline. Other more complex proWle form
equations have been proposed that overcome this problem (see Komar, 1998).

Beach ProWle Closure Depth

Seaward of some point along a beach proWle in the oVshore direction there will
be insigniWcant sand transport for a given wave condition. This point will be
further oVshore for higher and longer period waves. However, for coastal
engineering design, it is desirable to deWne a proWle closure depth at some
oVshore point where there is negligible proWle change for some signiWcant level
of wave action. DeWnition of this proWle closure depth is useful, for example, for
establishing the seaward limit of the placement of beach sand during a beach
nourishment project, deciding at what water depth a pipeline placed across the
nearshore zone might no longer need to be buried, or deciding how far seaward
to make beach proWle measurements for a beach monitoring program.


-----

258 / Basic Coastal Engineering

Hallermeier (1977) deWned a closure depth dc that ‘‘gives a seaward limit to

extreme surf-related eVects, so that signiWcant alongshore transport and intense
onshore-oVshore transport are restricted to water depths less than dc.’’ This depth
wasdevelopedfromlaboratorydataandlimited Welddata.Birkemeier(1985),using
more extensive Weld data modiWed Halermeier’s formulation for closure depth to

dc ¼ 1:75 Hs � 57:9[H[2]s [=][gT][2]s []]


where Hs is the extreme nearshore signiWcant wave height in meters exceeded 12
hours per year and Ts is the associated wave period. Birkemeier found that a
reasonable Wt to the data can also be obtained by the simpler relationship

dc ¼ 1:57Hs

where Hs is again deWned as that height occurring on average 12 hours per year.
It can be shown (U.S. Army Coastal Engineering Research Center, 1985) that
this relationship becomes

dc ¼ 6:75Hs

where Hs is now the mean average signiWcant wave height. Of course, a better
way to determine the closure depth for a given coastal site is to accurately
measure the beach proWle many times over the period of a year and determine
the depth at which there are no signiWcant depth variations over that time period.

8.3 Nearshore Circulation

Sustained winds blowing along the coast will generate an alongshore coastal
current. Propagation of the tide along the coast coupled with Coriolis acceleration will generate reversing coastal currents. The tide may also generate strong
reversing currents at inlet, harbor, and estuary entrances. The ebb Xow of these
currents may be supplemented by river and surface runoV. However, away from
the immediate inXuence of tide-generated currents at coastal inlets, the dominant
alongshore currents are those in the surf zone generated by waves breaking
oblique to the shoreline. These wave-induced longshore currents and the associated surf zone wave-induced turbulence are responsible for most of the alongshore sediment transport in the nearshore zone.

Figure 8.4 is a schematic plan view of a portion of the foreshore–nearshore zone

with waves approaching at an angle to the shoreline, breaking and running up on the
beach face. Also shownis the resulting longshore current velocitydistribution, which
extends from a point just seaward of the wave breaking line in to the beach face. The
maximum current velocity is typically in the surf zone just inside of the breaker line.


-----

Backshore


Coastal Zone Processes / 259

Longshore

current


Offshore

Figure 8.4. Wave-generated longshore current.


Limit of wave uprush

Particle runup

motion

Longshore

MSL

current

Wave

breaking αb

line


Szuwalski (1970) presents the results of nearly 6000 longshore current velocity


measurements made at a number of coastal locations in California. The vast
majority of the measurements yielded velocities under 0.5 m/s with only occasional velocities reaching a value of 1 m/s. These values are consistent with results
presented by Ingle (1966) and Komar (1975). Although these velocities are
relatively low, the longshore current’s capacity to transport sediment is signiWcantly increased by the turbulence generated in the surf zone by wave breaking.

The mechanism primarily responsible for wave-generated longshore currents


is the alongshore component of radiation stress in oblique breaking waves. Also,
variations in the alongshore distribution of wave breaker heights will cause
alongshore variations in the surf zone wave setup and the generation of currents
from areas of high waves to area of low waves. These two mechanisms may
support or oppose each other in establishing a longshore current. On most
sections of coastline, the former mechanism (oblique wave breaking) will predominate.

Successive waves in a wave train will have diVerent heights and periods. Often


the arriving waves consist of alternating groups of higher and lower waves,
resulting in pulsating components of radiation stress. Thus, the wave-induced
long-shore current often exhibits a pulsating behavior having a period of a few
minutes.

The most promising analytical approach to longshore current prediction is


based on the work of Longuet-Higgins (1970). He equated the alongshore


-----

260 / Basic Coastal Engineering

component of radiation stress with the bottom frictional resistance developed by
the longshore current. A modiWed form of the Longuett-Higgins equation for
longshore current velocity, based on calibration with Weld data, is given by the
U.S. Army Coastal Engineering Research Center (1984) as

U ¼ 20:7 m(gHb)[1][=][2] sin 2ab (8:2)

In Eq. (8.2) U is the average longshore current velocity across the surf zone, m is
the bottom slope in the surf zone, Hb is the wave breaker height, and ab is the
wave breaker angle (see Figure 8.4). Although Eq. (8.2) is generally considered to
be the best available for longshore current velocity prediction, the diVerence
between predicted and observed velocities can exceed 50%. If there is a sustained
alongshore wind, the wind stress acting on the surf zone can accordingly modify
the wave-induced current. Likewise, an alongshore current just seaward of the
surf zone can, through turbulent momentum exchange, modify the surf zone
current.

Example 8.3-1

A train of waves has a height of 1.3 m and an approach angle of 158 at the
breaker line. The average beach slope in the surf zone is 1:30 (m ¼ 0:033).
Estimate the alongshore Xow rate in the surf zone.

Solution:

From Eq. (2.68) the water depth at the breaker line will be approximately

db ¼ Hb=0:9 ¼ 1:3=0:9 ¼ 1:44 m

This assumes that the wave is a shallow water wave, a reasonable assumption in
most cases. The width of the surf zone will then be 1.44(30) 43.2 m and the surf
¼
zone cross-section area will be 1:44(43:2)(0:5) ¼ 31:1 m[2].

From Eq. (8.2) the average current velocity in the surf zone will be

U ¼ 20:7(0:033)(9:82 � 1:3)[0][:][5] sin 30[�] ¼ 1:22 m =s

From continuity, the Xow rate will be the average velocity times the cross-section
area or 1:22(31:1) ¼ 37:9 m[3]=s.

If a longshore current is intercepted by a headland or a structure (e.g., groin or

jetty) oriented normal to the shoreline, it will be deXected seaward as a rip
current and dissipated. A new current will develop downcoast of the obstruction.
Even on a long, relatively straight, uninterrupted shoreline the longshore current
will often be interrupted by a seaward Xowing rip current that relieves the


-----

Coastal Zone Processes / 261

Riphead


Groin


Beach face


Wave mass transport Rip current

Longshore current MSL


Figure 8.5. Typical wave-generated nearshore circulation.

continuous accumulation of water in the surf zone. This is demonstrated in
Figure 8.5. The rip current will likely be situated at a position of lower incident
wave heights and will usually scour a seaward trough, helping to stabilize its
position. Shorter period incident waves tend to produce more frequent but
smaller rip currents.

8.4 Alongshore Sediment Transport Processes and Rates

The wave-induced current in the surf zone and the turbulence induced by wave
breaking combine to cause alongshore sediment transport on beaches. Sand is
transported both in suspension and along the bed (suspended and bed loads,
respectively). The suspended load is relatively high where wave breaking is most
active, i.e., near the breaker line for plunging breakers but more evenly spread
across the surf zone for spilling breakers. In addition, the oblique wave runup
and gravity-induced return Xow on the beach face (see Figure 8.4) cause a ‘‘zigzag’’ sand particle motion on the beach, with a net movement in the downcoast
direction.

For both the suspended and bed load transport modes, Wner sand sizes will be

carried in larger volumes and over longer distances than coarser sizes. A consequence of this is that sediment from a particular point source (e.g., a stream
entering the coast) will have successively Wner median diameters at greater
downcoast distances from the source.

When considering longer term longshore sediment transport rates (volume per

time, typically per year), it is important for coastal engineering design to distinguish between the net and gross rates at a particular coastal location. The annual
directional distribution of the alongshore component of wave energy Xux and the
resulting sediment transport rate distribution will commonly be divided in the
upcoast and downcoast directions. (The direction of predominant transport


-----

262 / Basic Coastal Engineering

being termed the downcoast direction.) The annual directional distribution of
wave energy may cause the transport rate in one direction to be so predominant
that the gross transport is just slightly larger than the net transport rate. On the
other hand, the transport rates may be approximately equal in both the upcoast
and downcoast directions so that a large gross transport rate may produce a net
transport rate near zero.

Longshore transport rates are usually given as annual volumes of transported

sediment, but it must be remembered that the shorter term rates can be extremely
variable, exceeding the average annual rate by several times during a storm and
falling to near zero during the periods of low incident waves. Seasonal variations
(often summer versus winter) can also be quite variable both in rate and direction. In addition, annual transport rates can be quite variable from year to year
owing to Xuctuations in the wave climate, modiWcations to coastal structures that
impact the transport rate, and variations in the volume of sediment available
from a major source (e.g., a river that has large Xood Xows only periodically and
is nearly dry the remainder of the time).

Longshore Transport Rates

Some average annual net longshore transport rates and directions are listed in
Table 8.3 to demonstrate the order of magnitude and variability of transport
rates on U.S. beaches. These rates have been obtained from Army Corps of
Engineers project reports and U.S. Congress House Documents, and were
summarized in the U.S. Army Coastal Engineering Research Center (1984). It
should be noted that some of the rates (especially along the New Jersey coast,
e.g., see Sorensen, 1990) no longer occur owing to the construction of structures
that have limited sediment sources and controlled longshore transport. Some of
the variability in rates for nearby locations is due to the fact that the rates were
averages determined for diVerent time spans. The net rate of 765,000 m[3]=year at
Oxnard Plain Shore is also essentially the gross rate, as transport is strongly
unidirectional. On the other hand, the Gulf shore at Corpus Christi is near a
converging nodal point where the net transport is near zero, but the gross
transport rate is estimated to be around 550,000 m[3]=year.

Many of the transport rates listed in Table 8.3 were determined primarily by

hydrographic surveys of the volume of sand trapped upcoast or eroded downcoast of a groin, jetty, or other structure that creates a barrier to littoral
sediment transport. The rate at Sandy Hook was determined by surveys of the
rate of growth of Sandy Hook, a terminal spit. Some of the rates may be
underestimates because most structures do not act as complete barriers to
longshore transport. Transport rate estimates have also been made from periodic dredging records at harbor entrances where a dredged entrance channel
crosses the surf zone and is suYciently wide and deep to act essentially as a
sediment trap.


-----

Coastal Zone Processes / 263

Table 8.3. Estimated Net Longshore Transport Rates and Directions

Location Net Rate(m[3]/yr) Direction

Sandy Hook, NJ 355,000 N

Asbury Park, NJ 153,000 N

Shark River, NJ 229,000 N

Manasquan, NJ 275,000 N

Barnegat Inlet, NJ 191,000 S

Absecon Inlet, NJ 306,000 S

Cold Spring Inlet, NJ 153,000 S

Ocean City, MD 115,000 S

Atlantic Beach, NC 22,500 E

Hillsboro Inlet, FL 57,000 S

Pinellas County, FL 38,000 S

Perdido Pass, AL 153,000 W

Santa Barbara, CA 214,000 E

Oxnard Plain Shore, CA 765,000 S

Port Hueneme, CA 382,000 S

Santa Monica, CA 206,000 S

El Segundo, CA 124,000 S

Camp Pendleton, CA 76,000 S

Milwaukee County, WI 6,000 S

Racine County, WI 31,000 S

Kenosha, WI 11,000 S

Functional design of many coastal projects requires that estimates of the local

net and gross longshore sediment transport rate be made. Examples of these
types of projects include the design of a system to mechanically bypass sediment
past some obstruction such as a harbor entrance, or estimation of future
periodic maintenance dredging requirements for a channel that is to be dredged
across the surf zone. These estimates can often be made in one of the following
ways:

1. If the longshore transport rate has been established at a nearby location

with similar beach characteristics, shoreline orientation, and annual wave
climate, this rate can be adapted to the project site with possible modiWcations to adjust for local conditions. This requires good engineering judgment because the transport rate can change signiWcantly over short
distances along the coast as well as with the passage of time. The establishment of a sediment budget for the local coastal area (see Section 8.9) can be
helpful in this eVort.

2. If there are nearby traps to littoral transport and data deWning the induced

beach changes that have occurred over a period of time are available or can


-----

264 / Basic Coastal Engineering

be collected, transport estimates can be made. When evaluating these data
to estimate the transport rate, due consideration must be given to the
eVectiveness of the trap and the seasonal and long-term variability of the
transport rate that can occur.

3. A number of longshore transport rate formulas have been established that

relate the transport rate to the incident wave climate and beach characteristics (see Horikawa, 1988 for a summary). To establish the transport rate
at a site using these equations the wave climate (wave height and direction)
for at least a year should be determined from wave measurements and/or
wave hindcasts.

The best known and easiest to apply longshore transport formula is the CERC

formula (U.S. Army Coastal Engineering Research Center, 1984). Also see
Bodge and Kraus (1991) for a discussion of this formula. The volumetric
longshore sediment transport rate Q is given by


Q K
¼


rffiffiffi Hg b5=2 sin 2ab (8:3)

g 16(s � 1)a[0]


where g is the ratio of wave height to water depth at breaking which may be taken
as 0.9, a’ is the ratio of solid to total volume for the sediment and may be taken as
0.6 if better information is not available, and s is the sediment speciWc gravity
which may be taken as 2.65 if better information is not available. Hb is the wave
breaker height, commonly taken as the signiWcant wave height at breaking. K is a
coeYcient commonly taken as 0.32 for typical beach sands. For much coarser
shingle beaches the appropriate value of K would be much smaller (possibly by a
factor of 10 to 20).

It should be noted that the transport rate given by Eq. (8.3) is the potential

transport rate, meaning that it is the transport rate if sand is available across
the entire surf zone to be transported. For example, at some Caribbean
beaches that consist of a narrow beach fronted by fringing coral reefs over a
portion of the surf zone, the actual transport rate is often much smaller than
the rate given by Eq. (8.3). There is also some indication that the coeYcient
K varies with the wave breaker type and beach slope (see Bodge and Kraus,
1991).

Example 8.4-1

During the peak of a storm, waves approach a beach with their crests oriented at
an angle of 128 with the shoreline and a signiWcant wave height of 2.1 m at the
breaker line. Estimate the hourly potential longshore transport rate at this site
during the storm peak.


-----

Coastal Zone Processes / 265

Solution:

Using Eq. (8.3) with the suggested values for the various coeYcients and other
parameters yields


(2:1)[5][=][2] sin 24[�]


Q [0][:][32]
¼

16


rffiffiffiffiffiffiffiffiffi

9:81


0:9


¼

16 0:9 (2:65 � 1)0:6

¼ 0:173 m[3]=s(623 m[3]=hour)


8.5 Shore Response to Coastal Structures

Structures are constructed in the coastal zone primarily to stabilize or expand a
segment of the beach, to protect the coastline in the lee of the structure from
wave-induced damage and Xooding, to protect and stabilize navigable entrance
channels, and to provide a sheltered area for moored vessels. In essentially all
cases these structures interact with the active wave, current, and resulting sediment transport processes in the vicinity of the structure.

For discussion purposes most of these structures can be grouped into three

classes: (1) structures constructed essentially perpendicular to the shoreline and
attached to the shore, (2) structures constructed essentially parallel to the shore
on the beach face or berm, and (3) structures constructed oVshore essentially
parallel to the shoreline, and commonly segmented.

Shore-Perpendicular Structures

This class of structures includes groins that trap sediment being transported
along the coast in the surf zone or sediment that has been mechanically placed
on the beach where there is a potential for longshore transport and jetties, which
are typically more massive than groins, extend further seaward, and are constructed to stabilize and protect a navigable channel across the coastline.

Figure 8.6 shows, in plan view, the shoreline response to a single shore

perpendicular structure exposed to waves arriving from the dominant direction
shown. Depending on the width of the surf zone the structure may trap some or
most of the longshore sediment transport. This will cause an upcoast accumulation of sediment (A) plus the deposition of sediment at (B) owing to the rip
current that will develop along the upcoast face of the structure. Downcoast of
the structure (C) the beach will erode to satisfy the potential sediment transport
capacity of the waves at that point. Both upcoast and downcoast of the structure,
the shoreline will adjust so that it will parallel the incoming wave crest positions
as aVected by refraction and diVraction. Some sediment will be transported past
the structure as the upcoast segment of the beach is Wlling, particularly if the crest


-----

266 / Basic Coastal Engineering

B

A
D

C

Original MSL

Resulting MSL

Figure 8.6. Shore response to placement of a shore-perpendicular structure.

of the structure is not too high and/or the structure is somewhat permeable to
sand movement. After the upcoast beach segment is full all of the longshore
transport will pass either through, over, or around the structure, some of it being
deposited oVshore downcoast of the structure and the remainder of the sediment
being transported to and along the shore.

Usually, the wave direction and breaker height are continually changing so

complete equilibrium between the incident wave crest and the shoreline orientation is never completely achieved. The beach is continually adjusting to the
changing wave characteristics. However, if the waves come from one predominant direction with only occasional reverses, the resulting shoreline will closely
approximate that shown in Figure 8.6. Waves from the other direction would
transport sediment back toward the structure to form the Wllet at D which would
be diYcult to remove when the waves return to the predominant direction.

The amount of sediment that passes a Wlled structure and returns to the

downcoast shore depends on how much sediment moves over and through the
Wlled structure and how long the structure is compared to the width of the surf
zone (which varies with the incident wave height and tide range). The recommended design proWle for a groin consists of a horizontal crest across the beach
berm to the seaward extent to which it is desired to retain sand, followed by an
intermediate downward sloping section paralleling the beach face to a second
horizontal section out to the end of the groin and set at MLW or MLLW (U.S.
Army Coastal Engineering Research Center, 1984). The groin essentially acts as
a template for the desired beach proWle just upcoast of the groin.

A shoreline response similar to that shown in Figure 8.6 would also develop at

a pair of jetties constructed at the entrance to a harbor or interior bay. A portion
of the sediment that moves past the oVshore end of the upcoast jetty would be
transported further oVshore if there is a suYciently strong tidal ebb current.


B

A
D

C

Original MSL


-----

Coastal Zone Processes / 267

A tidal Xood current will transport some of the bypassing sediment into the
harbor or bay. Since the purpose of a jetty system is not to trap longshore
sediment transport and jetties are typically much longer than groins, a mechanical sediment bypassing system may be necessary.

A common method of preventing beach erosion or rebuilding eroded beaches

is to construct a series of groins along the shore to trap and hold existing
longshore transport and/or to be artiWcially Wlled with sand (Figure 8.7).
A system of groins can be constructed one section at a time by beginning at
the downcoast end and adding new groins as the spaces between the older groins
are Wlled with sand. If the entire system is constructed at one time, the updrift
groins will Wll Wrst, and the shoreline between the remaining groins will adjust to
the incident waves and subsequently Wll as sediment begins to bypass the upcoast
groins. Remember, erosion will occur downcoast of the groin system at a rate
approximately equal to the rate of sediment deposition in the system (in addition
to any natural net erosion that was occurring at the site prior to groin construction). Because of this downcoast erosion it may be desirable to artiWcially Wll the
groin system with sand (see Section 8.7). A groin system will not interfere with
the on-/oVshore transport of sand that occurs with the arrival of calm/storm
wave conditions and that may produce a net longer term erosion or accretion.

The common ratio of groin spacing to length (MSL shoreline to seaward end)

is between 1.5:1 and 4:1, the ratio depending on the resulting shoreline orientation which in turn depends on the angle of incidence of the dominant waves.
A design engineer must consider the annual range of incident wave conditions
and, from this, anticipate the resulting range of shoreline positions that will
develop. It is important that the groins not be Xanked by erosion at the landward
end, particularly when newly constructed upcoast groins temporarily deny littoral drift to a downcoast segment or when extensive erosion occurs downcoast
of the last groin in a system.

Shore-Parallel Onshore Structures

Seawalls, revetments, and bulkheads constitute this class of coastal structures.
Seawalls are massive structures that primarily rely on their mass for stability.
Examples are stone mounds and monolithic concrete structures similar to the
seawall at Galveston, Texas. Revetments (see Figure 7.5) are an armoring veneer


MSL after

groin construction

Original MSL


MSL after

natural / artificial


Net transport


MSL after

fill

groin construction


Figure 8.7. Shore response to a series of shore-perpendicular structures.


-----

268 / Basic Coastal Engineering

on a beach face or sloping bluV and are typically installed where the wave climate
is milder than where seawalls are employed. Bulkheads are a vertical wall with
tiebacks into the soil placed behind the bulkhead. They function more as an
earth retaining structure than as a structure designed primarily to withstand
wave attack. See the U.S. Army Coastal Engineering Research Center (1984) for
examples of these structures.

This class of structures is designed primarily to protect the shore landward of

the structure and typically will have little eVect on the adjacent upcoast and
downcoast areas. However, if they are built to maintain a section of shoreline in
an advanced position, this outward jutting section of the shoreline will act as a
headland and may trap some portion of the longshore sediment transport. The
upcoast and downcoast ends of these structures must tie into a noneroding
portion of the shore or must be protected by end walls so the structure is not
Xanked by the erosion of adjacent beaches.

When storm waves arrive, the beach proWle in front of these structures will be

cut back as depicted in Figure 8.2 with the wave agitation caused by the structure
often increasing the amount of proWle cutback over that which would occur at a
nonstructured proWle. The amount of beach face proWle cutting that occurs would
likely be greater at a vertical-faced solid structure than at a sloped stone mound
structure owing to the higher wave reXection of the former. For this reason, the toe
of these structures must be placed suYciently deep into the beach face or stabilized
by placing a stone mat or vertical cutoV wall at the toe. When calm waves return
the beach in front of the structure will usually rebuild to its prestorm condition.

A shore parallel onshore structure will impact littoral processes in two ways. By

preventing erosion of the shore it limits this section of the shore as a possible
source of sediment for longshore transport. If the structure is built seaward of the
water line it will reduce the size and transporting capacity of the surf zone, unless
the increased surf zone wave agitation due to the structure counteracts this eVect.

Shore-Parallel OVshore Structures

Figure 8.8 shows, in plan view, a shore-parallel oVshore breakwater and the
refraction/diVraction pattern that develops in the lee of the structure for
oblique incident waves. Also shown are the original shoreline and the resulting
shoreline caused by the modiWed wave pattern. The oblique waves produce
longshore transport from the readers left to right. The reduced wave energy in
the lee of the structure diminishes the longshore transport capacity of the waves
causing a shoreline bulge (salient) in the lee of the structure. The waves shape the
salient to parallel the dominant incoming wave crests. A sediment budget for the
vicinity of the structure requires that the sand deposited to form the salient be
made up for by downcoast erosion. The volume of sand trapped by the structure
depends on the length of the structure, its distance oVshore compared to the width
of the surf zone, and whether energy is transmitted over or through the structure.


-----

Coastal Zone Processes / 269

Incident

waves

Original MSL
Resulting MSL

Figure 8.8. Shore response to a shore-parallel oVshore structure.

OVshore breakwaters have been constructed for beach stabilization, both for

nourished and unnourished beaches. This may typically involve the construction
of a series of breakwaters with intervening gaps having a length about equal to the
length of the breakwaters. Often oVshore breakwaters are constructed with their
crest at or below MLW. These structures are less expensive and more aesthetic to
the environment. Low waves propagate over the structure but the higher storm
waves break at the structure so their capacity to erode a beach or damage shore
facilities is greatly reduced. For additional guidance on the functional design of
oVshore breakwaters see Rosati and Truitt (1990) and Rosati (1990).

8.6 Numerical Models of Shoreline Change

Figure 8.9 shows an idealized short section of the active portion of a sandy beach
from the berm down to the oVshore point at which longshore transport processes
are no longer active. The volume of the segment would be h(dx) dy. An equation
of continuity for the sediment in the beach section can be written that equates the
net longshore transport into and out of the section with the change in beach
section volume. This is


Incident

waves

Original MSL
Resulting MSL


� �

Q � Q þ [@][Q]

@x [dx]



[h dx dy]
¼

dt


or


dQ

(8:4)

dx dt

[þ][ h dy] [¼][ 0]


-----

270 / Basic Coastal Engineering

x

Q + [∂][Q]

∂x [dx]

dy

y

Q

h

Figure 8.9. Shore segment for sediment continuity equation development.

Equation (8.4) simply says that the advance or retreat of the shoreline (dy/dt) is
related to the net change in longshore transport (dQ/dx) across that section.

The longshore transport rate at any point along a beach can be determined

from Eq. (8.3). The change in transport rate across the beach section could be
caused by a change in the breaker wave height or by a change in the wave
breaker angle relative to the shoreline orientation. The latter could arise because
of a change in the approaching wave direction across the beach section and/or
because of a change in the shoreline orientation from one end to the other end of
the section.

Equations (8.3) and (8.4) have been used as a basis for simple numerical

models of shoreline change (see Hanson, 1989 and Hanson and Kraus, 1989
for a commonly used model). The shoreline in question is divided into numerous
short segments (dx) which may include structures such as groins. With the
oVshore wave climate (average wave height, period, direction for a time interval)
and nearshore hydrographic data the waves can be refracted to the shoreline.
From this, the longshore transport rate at the boundary of each segment can be
calculated. Then Eq. (8.4) yields the resulting advance or retreat of the shoreline
in that segment over the time interval dt. With the new shoreline position at all
segments at the end of the time interval, the process is repeated.

These shoreline change models are typically run to investigate shoreline

change over distances of from one to tens of kilometers and for time intervals
of months to longer than 10 years. These models, which are commonly referred
to as one-line models, do not consider onshore/oVshore sediment transport
across the beach proWle. More sophisticated N-line models which also attempt
to account for across-shore processes have been developed (see Perlin and Dean,
1983, for example). In these models the beach proWle is divided into N segments


Q + [∂][Q]

∂x [dx]

dy

y

Q

h


-----

Coastal Zone Processes / 271

and the continuity of sediment transport equation is written for transport in both
the x and y directions. A transport prediction equation is required for both
alongshore and onshore/oVshore to operate the model. The model output is the
change in the shoreline with time at each of the N proWle segments along the
entire alongshore section of shoreline being studied.

A wide variety of more sophisticated numerical models for beach processes

and resulting shoreline change are continuously being developed and used in
design analysis. They Wnd particular application for smaller spatial and time
scales (e.g. for evaluating shoreline response over a few hundred meters to a few
kilometers during one storm or a few weeks time interval).

The most sophisticated models are three-dimensional beach evolution models.

An example is the model employed by Shimzu, et al. (1990). First, the model
calculates the nearshore distribution of wave heights and directions including the
eVects of refraction, shoaling, diVraction, and breaking. Then, the spatial distribution of radiation stresses is determined from the wave Weld in order to predict
the current Weld including that in the vicinity of structures. Finally, bottom
elevation changes are determined by computing the sediment transport spatial
distribution owing to the wave- and current-induced bottom shear stress.

A variety of quasi-three dimensional models have also been developed that

simplify computational requirements by employing some two-dimensional aspects. Examples are Briand and Kamphius (1990) and Larson et al. (1990).

Another useful class of numerical models for shoreline change are those that

deWne just the wave-induced change in a beach proWle at a point along the shore
(see Larson et al., 1988, Hedegaard, et al., 1991 and Nairn and Southgate, 1993,
for example). These models are particularly valuable in predicting the retreat of a
beach/dune proWle and the related oVshore bar development owing to storm
wave attack and the related rise in mean water level due to storm surge. They are
based on a shore-normal sediment transport mechanism due to wave attack
coupled with a mass conservation relationship for beach sand on the proWle.
The models are typically calibrated with beach proWle data taken before, during
(in wave tanks), and after periods of storm wave activity.

8.7 Beach Nourishment and Sediment Bypassing

An important component of many beach expansion projects for recreation and/or
shore protection involves the mechanical placement of sand on the beach. Beach
nourishment involves the transfer of sand from some source to the beach that is to
be nourished. If the sand source is a deposit of longshore drift and the transfer
involves placement of this sand at some point downcoast of the obstruction that
caused the deposition, this form of beach nourishment is commonly called sediment bypassing. Both beach nourishment and sediment bypassing projects often
involve the construction of structures to improve the eYciency of the project.


-----

272 / Basic Coastal Engineering

Sand bypassing and beach nourishment, particularly when extensive struc
tures are not constructed to hold the sand at the point of placement, must usually
be carried out periodically for the life of the project. This may still be the most
economical solution to a problem. The bottom line is to achieve the lowest cost
per meter of nourished beach per year over the project life.

Beach Nourishment

The primary sources of sand for beach nourishment are: oVshore deposits,
deposits in bays and estuaries, land quarries, and deposits at navigation entrances. Often, sand borrowed from bays and estuaries is very fine and thus
not suYciently stable for placement on a beach with ocean wave exposure. The
last source involves removal of sand deposited in the navigation channel or
upcoast of jetties constructed to stabilize the channel. Placement of sand would
be on a downcoast beach that is eroded owing to the sand being removed from
the littoral zone by the navigation entrance.

The types of structures most commonly employed with a beach nourishment

project are groins or, to a lesser extent, segmented oVshore breakwaters. When
these structures are constructed to stabilize a beach, it was noted above that as
they are naturally Wlled by longshore transport of sand, the downcoast area may
seriously erode until natural bypassing of the structures commences. This can be
alleviated by the immediate nourishment of the beach in the areas where natural
deposition is expected.

A cost-eVective source of borrow material for beach nourishment must have a

suitable particle size distribution for the wave climate and beach slope at the
nourishment location. The coarser the borrow material the more stable it will be,
and thus the more cost eVective it will be. Coarser sand will form a steeper
proWle, and if too coarse may be undesirable for recreational beaches. The sand
must not contain undesirable contaminants and, for recreational beaches the
color of the sand may be important. Removal of the sand should not cause
environmental or ecological problems at the borrow site.

The most common sand transfer procedure is to remove the sand by a dredge

and transport it by pipeline or barge to the nourishment site. Shorter transport
distances will decrease costs, as will borrow sites where a dredge can operate
without signiWcant down time owing to high wave action. Borrow areas in deeper
water may involve larger unit costs owing to limitations on the dredges that are
available for sand removal.

The design beach Wll proWle at the nourishment site usually includes extension

of the berm to achieve the desired beach width and then a seaward slope to below
MLW that is typically steeper than the natural slope at the site. Allowance must
be made for the subsequent natural reshaping of the beach proWle by wave
action. And, if structures are not in place to control longshore transport of
sand, the beach area at the ends of the Wll area will lose sand to downcoast


-----

Coastal Zone Processes / 273

beaches, which may be a desirable process. Some beach Wll projects, where there
is a strong net littoral drift in a particular direction, will include the placement of
excess sand at the updrift end to act as a sand supply reservoir.

To quantify the volume of sand needed for a nourishment site, besides the design

Wll proWle, one must deWne the overWll required to allow for subsequent removal of
the Wner sizes of the Wll material owing to winnowing by wave action. A model for
predicting an overWll factor was developed by James (1975) and is presented in the
U.S. Army Coastal Engineering Research Center (1984). This factor is the estimated number of cubic meters of Wll material required to produce one cubic meter
of beach material when the Wlled beach has come to equilibrium. The model is
based on the sediment size distributions of the samples from the borrow area and
the natural beach where the Wll is to be placed. Although this model is used in
practice it is based on some somewhat arbitraryassumptions onthe behavior of the
Wll material and it has not been well evaluated in practice.

As noted above, it is commonly necessary to maintain a beach nourishment

project by subsequent periodic renourishment of the beach. In order to evaluate
the performance of the initial beach nourishment eVort and to guide the timing,
location and required sediment volumes for the periodic renourishment, a beach
monitoring program should be established. This would, at a minimum, require
periodic surveys of the beach topography and hydrography (see Section 9.4).
Additional monitoring activities might include nearshore wave measurements,
sand sample analysis, and aerial photographs.

For additional discussion on the technical as well as the economic and political

aspects of beach nourishment the reader is referred to the U.S. Army Coastal
Engineering Research Center (1984), Marine Board, National Research Council
(1995), Simm et al. (1996), and Dean (2002).

Sediment Bypassing

Often a shoreline harbor or a jettied navigation channel entrance will, as a
consequence of structures and a channel being constructed across the surf
zone, trap sediment that otherwise would be transported downcoast. To alleviate
the resulting downcoast erosion and/or the unwanted sediment deposition in the
harbor or entrance channel, it becomes necessary to mechanically bypass sediment past the harbor or channel entrance.

Sediment bypassing is most often accomplished on either an intermittent or

continuous basis with a Xoating hydraulic dredge and a discharge pipeline that
extends to the downcoast sediment discharge point. Bypassing has also been
accomplished by trucking the sediment past a channel entrance and by a permanently installed pumpout system that can reach the deposited sediment and
pass it through a pipeline to the discharge point.

Often the design of a project, where a need for sediment bypassing is antici
pated, will include structures that force the sediment to deposit in a well-deWned


-----

274 / Basic Coastal Engineering

deposition basin and protect the dredge from wave attack. Most hydraulic
dredges become much less eYcient when exposed to even moderate wave action
which causes the intake line to lift oV of the sea Xoor.

There will be some natural bypassing of most obstructions. It is important to

locate and size the deposition basin so as much natural bypassing as possible
takes place and so that there is no undesired deposition in the adjacent harbor or
entrance channel. When the gross longshore transport rate greatly exceeds the
net transport rate it is most desirable, but not always possible, that the bypassing
system be designed to only bypass the net rate.

The design of a sediment bypassing system requires that the following basic

information be determined:

1. The incident wave climate must be established. This is important for the

functional and structural design of any structures. And it is important for
the establishment of annual net and gross longshore sediment transport
rates. It is also desirable to establish whether transport direction reversals
are short term in duration or longer term like seasonal reversals. In addition, the volumes of sand that might be deposited in a deposition basin
during a single major storm should be estimated.

2. The surf zone dimensions and position must be determined as this is where

the longshore transport takes place. This will depend on the beach slope,
the distribution of incident wave breaker heights, and the tide range.

3. Any tidal or other current Xow patterns in the vicinity of the deposition

basin must be determined.

4. If a dredge is to be used, the capacities of available dredges must be

established.

Figure 8.10 illustrates the more common types of sand bypassing systems in

use. For a more detailed discussion of these various systems including some
examples of each, see the U.S. Army Coastal Engineering Research Center
(1984).

Figure 8.10 (upper left) illustrates the classic example of an updrift Wllet

forming and growing until sediment moves past the channel entrance. Some of
this sediment is carried into the entrance channel on Xood tide and some is lost to
the littoral zone when it is transported oVshore on the ebb tide. Simple bypassing
operations including trucking, a dredge that cuts its way into the Wllet from the
lee side, or a Wxed pumping plant have been used to bypass sand to the downcoast side of the entrance.

For this condition, if the channel entrance geometry permits, it is best to allow

the sediment to deposit in the channel where a dredge can safely operate to
transport the sediment to the discharge area. This allows as much natural bypassing as possible but sand jetted oVshore by an ebb tide is not trapped for bypassing.


-----

Coastal Zone Processes / 275

Deposition Deposition Dredge

zone zone

Discharge

Deposition

Deposition

Weir

Dredge

Dredge

Deposition

Discharge

Discharge

Figure 8.10. Typical sand bypassing systems. (ModiWed from U.S. Army Coastal

Engineering Research Center, 1984.)

At a harbor with a shore-connected breakwater (Figure 8.10 lower left), the

longshore drift will eventually move into the harbor entrance to form a depositional spit at the end of the breakwater. The breakwater and spit will protect a
dredge operating in their lee to maintain the harbor entrance and mooring areas.

Figure 8.10 (upper right) shows an eVective but capital expensive bypassing

system in which an oVshore breakwater causes a sediment deposition zone and
provides a sheltered area for a dredge to operate. The breakwater can also be
placed to provide additional shelter from wave attack for the channel entrance
and interior.

The system depicted in Figure 8.10 (lower right) consists of a weir (with a crest

elevation at or near MSL) at the shoreward end of the upcoast jetty, which, in


Deposition Deposition Dredge

zone zone

Discharge

Deposition

Deposition

Weir

Dredge

Dredge

Deposition

Discharge

Discharge


-----

276 / Basic Coastal Engineering

turn, is oriented to create a protected deposition basin in the lee of the weir and
jetty. The weir is positioned to cross the surf zone so much of the sand reaching it
moves over the weir into the deposition basin. It is important that tidal/river Xow
not cause the dredged navigation channel to migrate into the deposition basin.

8.8 Wind Transport and Dune Stabilization

In addition to the sand transported by waves and littoral currents, signiWcant
volumes of sand from the beach face and backshore can be transported by the
wind. Where there is a wide beach, a predominant onshore wind as is common in
many areas, and low coastal topography, wind transported sand can develop a
major dune system extending landward from the beach berm. (see Figure 8.1).
The dunes, called foredunes, are continuous irregular mounds of sand situated
adjacent and parallel to the beach. A well-established dune system functions as a
reservoir that can nourish a beach when the dunes are attacked by waves at
higher water levels, and as a shore protection and Xooding prevention structure
as they yield to wave attack during a storm.

Field and laboratory studies indicate that there are three mechanisms respon
sible for the transport of sediment by wind:

1. Saltation. Particles rise from the bed surface at a nearly vertical (slightly

downwind) angle, travel forward in an arc, and land at a Xat (108 to 158)
angle at a point 6 to 10 times the arc height downwind. Upon landing, they
may jump or saltate again, or they may dislodge other particles that then
saltate. The maximum elevation particles achieve is usually less than 0.5 m
but may reach 1 m. Saltation is usually the predominant mode of sand
transport by wind, often accounting for up to 80% of the total transport load.

2. Surface creep. About 25% or less of the wind load is transported by surface

sliding or rolling of the particles in essentially continuous contact with the
bed. This involves the larger sand grains and the driving forces are wind
shear stress and the impact of saltating particles.

3. Suspension. Owing to the low relative density of air, a negligible volume of

sand size particles is carried by turbulent suspension. Dust and other Wne
particle sizes not commonly found on a beach can be transported long
distances at relatively high altitudes by turbulent suspension.

There is a threshold wind velocity below which sand will not be transported by

the wind. This threshold velocity and subsequent sand transport rate depend on
the grain size distribution, moisture content of the sand bed, wind vertical
velocity proWle, wind gustiness, sand bed slope, and the existence of vegetation.

Several semi-empirical predictor equations for the wind transport rate have

been developed (see Horikawa, 1988 for a summary and discussion of these


-----

Coastal Zone Processes / 277

equations). These equations generally relate the transport rate to a representative
grain diameter and the wind shear velocity (square root of the wind-induced
shear stress divided by the air density), and contain empirical coeYcients that
relate to the grain size distribution and other factors. These equations are based
on Weld and lab measurements, generally with dry sand and not-too-irregular
topography. Often, high wind speeds at the coast occur during storms when there
is accompanying precipitation. Given this and the approximate nature of the
results given by the available transport formulas, it is generally diYcult to
calculate long-term wind transport rates at the coast.

The development of a strong and continuous foredune system immediately

adjacent to the beach is very desirable where space permits and an adequate
supply of sand is being transported landward by the wind. This can be assisted
by the installation of semiporous fencing (highway snow fencing) or by the
planting of vegetation (particularly beach grasses) to trap sand. Both are particularly eVective because of the saltation and surface creep transport mechanisms, which limit sand transport to a region of a meter or less from the beach
surface. Recommended practices for fence construction and grass selection,
planting, and care are presented in the U.S. Army Coastal Engineering Research
Center (1984).

When planted in suYcient quantity and cared for (e.g., prohibit walking on

dunes), grasses will continuously trap sand as they grow and the dunes increase
in size. ProWle data taken at several beaches show dune crest elevations growing
at an average rate of about a half meter per year for several years to reach
elevations of 3 to 8 m. Fences are less desirable because fencing must be added as
dunes grow and the fences deteriorate and become aesthetically less pleasing. In
some locations, where a protective dune Weld must rapidly be established, the
dunes were built with earth moving equipment and then stabilized by planting
vegetation.

8.9 Sediment Budget Concept and Analysis

In some coastal areas continuous longshore transport of sand can take place
over very great distances. However, in many areas sand is transported only short
distances alongshore from its source or sources before being deposited at one or
more semipermanent locations known as sinks. An improved qualitative, and
often quantitative, understanding of the littoral processes in a coastal area can
often be accomplished by constructing a sediment budget for that area. This
involves deWning and quantifying, as well as possible, all of the sediment sources
and sinks within the study area for the sand being transported alongshore and
relating these to the transport into and out of the area at the area boundaries. If
these sources, sinks, and transport rates can be adequately quantiWed (e.g., cubic
meters of sand per year) then a quantitative sediment budget can be developed.


-----

278 / Basic Coastal Engineering

Common sand sources include:

1. Rivers. Many rivers discharge sediment to the coast on a regular basis, but

some rivers are ephemeral and deposit sediment only during periods of
heavy precipitation. Much of the sediment load from a river may be Wner
than the sand size range and will remain in suspension until deposited
oVshore. Rivers that discharge into estuaries or large bays may have most
of the sand size particles deposited before reaching the shore. Dams and
erosion control projects on a river watershed may greatly diminish the
amount of beach sand contributed to the coast.

2. Beach and cliV erosion. In many areas the main source of sand in the littoral

zone is a section of the beach and/or cliVs that is eroding. CliV erosion
usually occurs during storms when any fronting beach is cut back so waves
can attack the toe of the cliV. Only a portion of the sediment contributed by
the eroding cliVs may be in the beach sand size range.

3. ArtiWcial beach nourishment. Periodic nourishment of the beach in a study

area may be the primary source of sand in an area that suVers a deWciency
of sand.

4. Nearshore reefs. In tropical climates beaches often consist primarily of sand

(calcium carbonate) derived from nearshore reefs constructed by marine
life. The reefs also act to shelter the beach from wave attack.

Common sinks include:

1. Tidal entrances. Harbor, bay, and estuary entrances with tide-generated

reversing Xows can trap large volumes of sediment on both the landward
and seaward ends of the entrance. The Xood tide carries sediment through
the entrance where it is deposited in quieter waters. The ebb tide jet may
carry sediment far enough oVshore to be eVectively removed from the
littoral zone.

2. Structures. Structures such as groins, jetties, and breakwaters that pur
posely or inadvertently trap sand will act as a sink while the upcoast Wllet
is forming. Natural bypassing of the structure will develop after the structure is Wlled.

3. Wind transport. At most coastal locations the dominant transport of sand

by wind is from the beach berm to the dune Welds where the sand may be
stabilized by vegetation. Dune overwash during a storm may permanently
remove sand from the littoral zone.

4. OVshore deposition. Storm wave attack on a beach may carry some sand

suYciently far oVshore that it is not returned to the beach during calm wave
conditions.


-----

Coastal Zone Processes / 279

Dominant

waves

Sea

G

C D E F H

Dunes
Lake

B

A

River

Figure 8.11. Sediment budget example.

5. Natural formations. These include depositional features such as spits (A in

Figure 8.11) that grow from the shore in the downcoast direction or
submarine canyons that lie close to the shore and transport sand oVshore.

6. Beach mining. Sand is a valuable natural resource in many coastal areas. As

a consequence it has been mined from the beach for use elsewhere.

For an illustration of the sediment budget concept consider the hypothetical

coastal segment depicted in Figure 8.11. This coastal segment consists of a line of
eroding cliVs from B to D, a river discharging to the coast (E), and a straight
segment of sandy beach from F to H. The dominant waves approach the coast in
the direction shown.

As the cliVs erode, the sand-sized material in the cliVs contributes sand to

the littoral zone. Periodic aerial photographs and/or land surveys of the
cliVs combined with samples to determine the size distribution of the cliV
material would quantify the amount of beach sand being contributed to the
littoral zone.

A diverging nodal zone would be located around C with the sand contributed

by the cliVs being transported toward A to form the spit and toward D. Eastward
from the cliVs sand would be added to the littoral zone from the river. The
volume of this material would be estimated from predictions of river transport
rates for the sediment size range found in the littoral zone.

The incident waves would produce a potential net longshore transport rate

given by Eq. (8.3). Wave measurements and/or hindcasts would be required to
make this determination. If the cliVs and river can produce enough sand to
satisfy this potential, the beach along F to H would be dynamically stable. If


G

C D E F H

Dunes
Lake

B

A

River


-----

280 / Basic Coastal Engineering

not, sand would be eroded from the western edge of the beach to satisfy the
deWcit. Any sand transported by wind to produce the dunes would enter the
budget balance by subtracting sand from the beach at F. Dune growth can be
estimated from periodic aerial photographs and land surveys

If an inlet with a pair of jetties were to be constructed (G) to open the lake to

navigation, this budget analysis would indicate the rate at which sand might be
trapped at the inlet and the consequent need for sediment bypassing to maintain
the beach at H. A dam constructed on the upper watershed of the river would
trap some of the sediment that otherwise reaches the littoral zone. This would
diminish the volume of sediment available for transport alongshore and contribute to erosion along the shore from F to H. The same can be said for any eVort to
stabilize the cliVs between C and D which would diminish the volume of sand
available for transport downcoast.

Often, it is diYcult to quantify some components of the sediment budget, and

rough estimates of these components must be made to balance the budget. The
sediment budget is still useful to give an indication of conditions in the study area
as well as the potential impact of proposed projects.

8.10 Coastal Entrances

At many coastal locations there are inlets that form waterway passages to the
interior. Often they are through barrier islands to the bays that are located
behind the barrier island. Their primary purpose is usually for vessel navigation
to the interior bay or a harbor. They also function for water exchange to improve
water quality in the bay or harbor. And some entrances act as Wsh passes to allow
for Wsh migration.

Most coastal entrances are constructed by dredging the entrance channel

and stabilizing it by a pair of jetties (see Figure 8.10, upper left diagram).
Some, however, have been formed naturally when storm surge caused a barrier
beach to be overwashed and a natural channel to be formed. To stabilize
this naturally formed channel, jetties are then constructed. In either case, the
channel would be dredged to the desired design depth and usually out to a point
seaward of the ends of the jetties where the design depth bottom contour is
reached.

Jetty systems at channel entrances have the following purposes:

. They control the geometry of the channel for secure navigation. This
may include keeping the axis of the channel from meandering and limiting
the width of the channel so tide-induced Xow causes a suYciently deep
channel to be maintained. There will often be a bar located across
the entrance to the channel and seaward of the outer ends of the jetties. A
well trained ebb Xow jet will assist in keeping the channel open across the bar.


-----

Coastal Zone Processes / 281

. They limit the deposition of sediment in the channel from both the updrift
and downdrift sides; and, related to this, they prevent the channel from
migrating along the shore (usually in the downdrift direction).

. They provide protection to vessels in the navigation channel from wave
attack. This may include temporary protection for a Xoating dredge as part
of a sediment bypassing system.

The required depth for a navigation channel (measured below Mean Lower

Low Water) depends primarily on the channel’s design vessel; i.e. typically the
largest vessel that is to use the channel. This depth is the sum of:

1. The design vessel draft.

2. The amount of vertical motion below MLLW that the vessel undergoes

owing to wave action. Since wave action is stronger toward the seaward end
of the channel, the channel design depth may be greater at the seaward end
than along the inner portion of the channel.

3. An additional depth to provide for safe clearance between the design vessel

keel and the channel bed. This allowance depends on the Wrmness of the
channel bottom.

4. An additional depth for overdredging to allow for some sediment depos
ition before the channel has to be dredged again.

Tobiasson and Kollmeyer (1991) recommend that the channel have a min
imum width of 75 feet (22.8m), but if possible, a 100 foot (30.5 m) width is to be
preferred. Dredged side slopes plus any clearance space between the dredged
channel and the jetty structures would add additional width to the channel. If
sailboats not under power are to use the channel, additional width must be
allowed for tacking.

The reversing Xow through the channel entrance caused by the rising and

falling tide plus the seaward Xow from river and surface runoV to the bay will
assist to keep the channel open. The resulting ebb and Xood Xow velocities
through the channel depend primarily on a relationship between the minimum
cross-sectional area of the channel measured below mean sea level (Ac) and the
contributing bay or harbor tidal prism for the spring tide range (P). The tidal
prism is the volume of water that Xows into the bay on Xood tide and back out of
the bay on ebb tide. O’Brien (1966) gives this relationship for an entrance with
two jetties as

Ac ¼ 4:69(10[�][4])P[0][:][85]

Where Ac and P are given in ft[2] and ft[3] respectively. Jarrett (1976) gives similar
results based on a much more extensive data base. If the calculated Ac value is


-----

282 / Basic Coastal Engineering

close to the design cross-sectional area based on navigational requirements, then
the tide can be counted on to signiWcantly maintain the channel from sand
deposition.

Bruun (1978) found that the ratio of the tidal prism volume to the annual gross

volume of sediment transported past the channel entrance is also an indicator of
potential channel entrance shoaling. If this ratio exceeds 150 there is little
entrance shoal formation and good entrance Xushing by the tide. As this ratio
reduces to around 20 to 50, entrances suVer severe shoaling and require signiWcant maintenance dredging.

8.11 Summary

In this chapter we were concerned with shorelines that consisted of a sandy
beach. The focus was those nearshore processes that shaped a beach, both in
plan and proWle. We also considered the impact of typical coastal structures on
beach processes—how to predict these eVects and, where there were negative
eVects, how to overcome these negative eVects.

Much of coastal engineering relies on design methods that have a strong

empirical component (e.g., wave and water level prediction, wave interaction
with structures, analysis of the response of coastal structures to wave attack, and
prediction of beach processes and their response to coastal structures). Development of these design methodologies therefore requires physical measurements,
either in a laboratory or the Weld and often both. This is the focus of the
remaining chapter in this text.

8.12 References

Bascom, W.N. (1951), ‘‘The Relationship Between Sand Size and Beach-Face Slope,’’

Transactions, American Geophysical Union, December, pp. 866–874.

Birkemeier, W.A. (1985), ‘‘Field Data on Seaward Limit of ProWle change,’’ Journal,

Waterway, Ports, Coastal and Ocean Division, American Society of Civil Engineers,
Vol. 111, pp. 598–602.

Bodge, K.R. and Kraus, N.C. (1991), ‘‘Critical Examination of Longshore Transport

Rate Magnitude,’’ Proceedings, Coastal Sediments ’91 Conference, American Society of
Civil Engineers, Seattle, pp. 139–155.

Briand, M.H.G. and Kamphius, J.W. (1990), ‘‘A Micro Computer Based Quasi 3D Sedi
ment Transport Model,’’ Proceedings, 22[nd] International Conference on Coastal Engineering, American Society of Civil Engineers, Delft, The Netherlands, pp. 2159–2172.

Bruun, P. (1954), ‘‘Coast Erosion and the Development of Beach ProWles,’’ Technical

Memorandum 44, U.S. Army Corps of Engineers Beach Erosion Board, Washington,
DC.


-----

Coastal Zone Processes / 283

Bruun, P. (1962), ‘‘Sea Level Rise as a Cause of Erosion,’’ Journal, Waterways and

Harbors Division, American Society of Civil Engineers, February, pp. 117–133.

Bruun, P. (1978), Stability of Tidal Inlets – Theory and Engineering, Elsevier, Amsterdam.

Dean, R.G. (1987), ‘‘Coastal Sediment Processes: Toward Engineering Solutions,’’ Pro
ceedings, Coastal Sediments ’87, American Society of Civil Engineers, New York, pp.
1–24.

Dean, R.G. (1991), ‘‘Equilibrium Beach ProWles: Characteristics and Applications,’’

Journal of Coastal Research, Vol. 7, pp. 53–84.

Dean, R.G. and Dalrymple, R.A. (2002), Coastal Processes with Engineering Applications,

Cambridge University Press, New York.

Dean, R.G. (2002), Beach Nourishment Theory and Practice, World ScientiWc, Singapore.

GriYths, J.C. (1967), ScientiWc Method in Analysis of Sediments, McGraw-Hill, New

York.

Hallermeier, R.J. (1981), ‘‘A ProWle Zonation for Seasonal Sand Beaches from Wave

Climate,’’ Coastal Engineering, Vol. 4, pp. 253–277.

Hanson, H. (1989), ‘‘GENESIS—A Generalized Shoreline Change Numerical Model,’’

Journal of Coastal Research, Vol. 5, No. 1, pp. 1–27.

Hanson, H. and Kraus, N.C. (1989), ‘‘Genesis: Generalized Model for Simulating Shore
line Change,’’ Technical Report CERC-89–19, U.S. Army Waterways Experiment
Station, Vicksburg, MS.

Hedegaard, I.B., Diegaard, R. and Fredsoe, J. (1991), ‘‘OVshore/Onshore Sediment

Transport and Morphological Modelling of Coastal ProWles,’’ Proceedings, Coastal
Sediments’91, American Society of Civil Engineers, Seattle, pp. 643–657.

Horikawa, K. (1988), Nearshore Dynamics and Coastal Processes—Theory. Measurement

and Predictive Models, University of Tokyo Press, Tokyo.

Ingle, J.C. (1966), The Movement of Beach Sand, Elsevier, New York.

Inmann, D.L. (1952), ‘‘Measures for Describing the Size Distribution of Sediments,’’

Journal, Sedimentary Petrology, September, pp. 125–145.

James, W.R. (1975), ‘‘Techniques in Evaluating Suitability of Borrow Material for Beach

Nourishment,’’ Technical Memorandum 60, U.S. Army Coastal Engineering Research
Center, Ft. Belvoir, VA.

Jarrett, J.T. (1976), ‘‘Tidal Prism – Inlet Area Relationships,’’ General Investigation of

Tidal Inlets Report 3, U.S. Army Coastal Engineering Research Center, Ft. Belvoir, VA.

Komar, P.D. (1975), ‘‘Nearshore Currents: Generation by Obliquely Incident Waves and

Longshore Variations in Breaker Height,’’ in Nearshore Sediment Dynamics and Sedimentation, (J. Hails and A. Carr, editors), John Wiley, New York.

Komar, P.D. (1998), Beach Processes and Sedimentation, Second Edition, Prentice-Hall,

Upper Saddle River, NJ.

Kriebel, D.L., Dally, W.R., and Dean, R.G. (1986), ‘‘Undistorted Froude Model for Surf

Zone Sediment Transport,’’ in Proceedings, 20th International Conference on Coastal
Engineering, American Society of Civil Engineers, Teipei, Taiwan, pp. 1296–1310.


-----

284 / Basic Coastal Engineering

Krumbein, W.C. (1936), ‘‘Application of Logarithmic Moments to Size Frequency Dis
tribution of Sediments,’’ Journal, Sedimentary Petrology, pp. 35–47.

Krumbein, W.C. and Monk, G.D. (1942), ‘‘Permeability as a Function of the Size

Parameters of Sand,’’ Technical Publication 1492, Petroleum Technology, July, pp.
1–11.

Larson, M., Kraus, N.C. and Hanson, H. (1990), ‘‘Decoupled Numerical Model od 3D

Beach Change,’’ Proceedings, 22[nd] International Conference on Coastal Engineering,
American Society of Civil Engineers, Delft, The Netherlands, pp. 2173–2185.

Larson, M., Kraus, N.C., and Sunamura, T. (1988), ‘‘Beach ProWle Change: Morphology,

Transport Rate and Numerical Simulation,’’ in Proceedings, 21st International Conference on Coastal Engineering, American Society of Civil Engineers, Malaga, Spain,
pp. 1295–1309.

Longuet-Higgins, M.S. (1970), ‘‘Longshore Currents Generated by Obliquely Incident Sea

Waves,’’ Journal, Geophysical Research, Vol. 75, pp. 6778–6789, 6790–6801.

Marine Board, National Research Council (1995), Beach Nourishment and Protection,

National Academy Press, Washington, DC.

Nairn, R.B. and Southgate, H.N. (1993), Deterministic ProWle Modelling of Nearshore

Processes. Part 2, Sediment Transport and Beach ProWle Development,’’ Coastal Engineering, Vol. 19, pp. 57–96.

O’Brien, M.P. (1966), ‘‘Equilibrium Flow Areas of Tidal Inlets on Sandy Coasts,’’

Proceedings, 10[th] International Conference on Coastal Engineering, American Society
of Civil Engineers, New York, pp. 676–686.

Perlin, M. and Dean, R.G. (1983), ‘‘A Numerical Model to Simulate Sediment Transport

in the Vicinity of Coastal Structures,’’ Miscellaneous Report 83–10, U.S. Army Coastal
Engineering Research Center, Ft. Belvoir, VA.

Rosati, J.D. (1990), ‘‘Functional Design of Breakwaters for Shore Protection,’’ Technical

Report CERC-90–15, U.S. Army Waterways Experiment Station, Vicksburg, MS.

Rosati, J.D. and Truitt, C.L. (1990), ‘‘An Alternative Design Approach for Detached

Breakwater Projects,’’ Technical Report CERC-90–7, U.S. Army Waterways Experiment Station, Vicksburg, MS.

Seelig, W.N. and Sorensen, R.M. (1973), ‘‘Texas Shoreline Changes.’’ Journal, American

Shore and Beach Preservation Association, October, pp. 23–25.

Shimzu, T., Hitoshi, N. and Kosuke, K, (1990), ‘‘Practical Application of the Three
Dimensional Beach Evolution Model,’’ Proceedings, 22[nd] International Conference on
Coastal Engineering, American Society of Civil Engineers, Delft, the Netherlands, pp.
2481–2494.

Simm, J.D., Brampton, A.H., Beech, N.M., and Brooke, J.S. (1996), Beach Management

Manual, Report 153, Construction Industry Research and Information Association,
London.

Sorensen, R.M. (1990), ‘‘Beach Behavior and EVect of Coastal Structures, Bradley Beach,

New Jersey,’’ Journal, American Shore and Beach Preservation Association, January,
pp. 25–29.


-----

Coastal Zone Processes / 285

Szuwalski, A. (1970), ‘‘Littoral Environment Observation Program in California—Pre
liminary Report,’’ Miscellaneous Publication 2–70, U.S. Army Coastal Engineering
Research Center, Washington, DC.

Tobiasson, B.O. and Kollmeyer, R.C. (1991), Marinas and Small Craft Harbors, Van

Nostrand and Reinhold, New York.

U.S. Army Coastal Engineering Research Center (1984), Shore Protection Manual, U.S.

Government Printing OYce, Washington, DC.

U.S. Army Coastal Engineering Research Center (1995), ‘‘Beach-Fill Volume Required to

Produce SpeciWed Beach Width,’’ Coastal Engineering Technical Note II-32, U.S.
Army Waterways Experiment Station, Vicksburg MS.

Weggel, J.R. (1979), ‘‘A Method for Estimating Long-Term Erosion Rates from a Long
Term Rise in Water Level,’’ Coastal Engineering Technical Aid 79–2, U.S. Army
Coastal Engineering Research Center, Ft. Belvoir, VA.

Wentworth, C.K. (1922), ‘‘A Scale of Grade and Class Terms for Clastic Sediments,’’

Journal, Geology, pp. 377–392.

Wiegel, R.L. (1964), Oceanographical Engineering, Prentice-Hall. Englewood CliVs, NJ.

8.13 Problems

1. A sieve analysis of a beach sample yields the following results:

Opening Size (mm) Weight Retained (grams)

2.000 0

1.414 0

1.000 0.3

0.707 1.7

0.500 6.2

0.353 27.8

0.250 24.1

0.177 17.7

0.125 15.3

0.088 5.0

0.062 1.9

Plot the cumulative frequency distribution on log-normal graph paper and
determine the median diameter, the phi median diameter, the phi mean
diameter, the phi deviation measure, and the phi skewness measure. If the
sample were collected on the beach face of a beach directly exposed to
ocean waves, estimate the beach face slope.


-----

286 / Basic Coastal Engineering

2. Estimate the beach face slope for the sample analysis shown in Figure 8.1

which is for a beach on a small lake.

3. A beach consists of quartz sand particles having an average median

settling diameter of 0.27 mm. Assume Stokes law is valid to deWne particle
settling velocity. Plot, on a graph of wave height H0 versus period T, the line
(band) separating eroding and accreting beach proWles. Use a range of H0 and T
values common to the ocean environment. Discuss the practical signiWcance of
the results indicated by this plot. After a storm, what slope might the beach face
have?

4. Waves approach a sand beach and break in water 1.1 m deep, with the

wave crests forming an angle of 128 with the shoreline. Estimate the volume of
sand that is transported alongshore in one hour.

5. A wave train has a deep water height of 2.5 m and a period of 7 s. It

propagates toward the shore across essentially shore parallel bottom contours.
In deep water the wave crests lie at an angle of 368 to the bottom contours and
shoreline. What is the potential longshore sediment transport volume in a period
of one hour?

6. An essentially straight sand beach has a north—south orientation. The net

littoral transport is from north to south and owing to sea level rise and a slight
deWciency of sediment available for transport the beach suVers continuing erosion. A series of four groins is simultaneously constructed on the upper end of
the beach. With a sketch describe the shoreline response. What might you do to
overcome any negative impacts on the shoreline?

7. At a tidal inlet on a north—south oriented coastline, the average annual

longshore transport is 300,000 m[3] to the south mostly during the winter and
130,000 m[3] to the north mostly during the summer. The average nearshore beach
slope is 1:40 and visual estimates throughout the year yield an average breaker
height of 1.1 m. A 100 m wide navigation channel is to be dredged to a depth of
4 m MSL and protected by shore-normal parallel jetties. The mean tide range
�
is 0.9 m. Show, with drawings, and explain the suggested layout of the jetties
including a sediment bypassing system.

8. Discuss in detail where it is appropriate to use groins for shore stabiliza
tion. For these uses, what precautions must be taken?

9. Explain what information you would need and how you would proceed to

predict the plan shape of the beach behind a newly constructed shore parallel
oVshore breakwater.

10. From a study of the details of the coastal hydrographic chart provided by

your instructor, discuss the features observed and the active coastal zone processes.


-----

## 9

### Field and Laboratory Investigations

The coastal zone—where the land, sea, and air meet—is one of the most

complex areas for conducting civil engineering analysis and design. Owing to
the nature of the coastal zone, most coastal engineering analysis and design
procedures have a partial or complete empirical basis. This empirical basis
must be developed and continually improved through extensive Weld, and in
some cases, laboratory investigations.

Our understanding of most coastal processes has been developed largely

through Weld measurements and laboratory experiments. Numerical models for
predicting wind waves, storm surge, and beach response all require substantial
calibration and veriWcation using extensive experimental data sets. The conditions at a given coastal site must be adequately deWned to complete a project
design. In addition, the performance of completed coastal projects should be
evaluated for a signiWcant post construction period in order to provide adequate
maintenance and a better understanding of the eVectiveness of the project design
and construction. This is particularly true for projects that have not achieved the
success desired by the designer.

Most coastal processes occur over relatively long time spans and have large

spatial extents. They also involve or are impacted by a variety of coastal factors
(e.g., waves, wind, the tide and storm surge, currents, and beach sediment
properties). Consequently, the cost of Weld data collection can be quite high.
But continued advancement of coastal engineering requires that these costs be
anticipated and met.

To function as a coastal engineer, one must have a basic understanding of the

types of Weld and laboratory investigations that are commonly employed. This
chapter gives an overview of the common types of measurements made and,
where appropriate, the typical equipment used.


-----

288 / Basic Coastal Engineering

9.1 Field Investigations

For discussion purposes Weld investigations can be classiWed into three primary
categories: (1) measurement of wind-generated waves and other hydrodynamic
measurements, (2) measurement of beach sediment properties and morphology
as well as sediment transport processes, and (3) investigation of the behavior of
coastal structures.

The Wrst category includes the measurement of water surface time histories to

deWne the various components of the wave energy spectrum deWned in Figure
5.2. The measurement of the wind wave portion of the spectrum is usually done
directly while the longer period components of the spectrum require that the
wind wave frequencies be Wltered out so the longer period components are more
easily discerned. Other hydrodynamic measurements include the wind and
coastal currents.

Beach morphology can be measured by standard surveying techniques. How
ever, owing to the dynamic nature of the coastal zone where large areas across
the surf and nearshore zones must be rapidly measured, some unique techniques
for hydrographic measurement have been developed. In addition it is often
desirable to measure the actual transport of sediment as well as the resulting
hydrographic changes. This presents some signiWcant tactical problems that have
not been completely mastered.

Most coastal structures are designed to remain in place and suVer little

deterioration during their design life. Periodic visual inspection of the structures
throughout their lifetime will guide the possible need for maintenance and repair.
However, to develop improved design procedures it is often desirable to make
inplace measurements of the loads and/or resulting stresses exerted by waves and
currents on structural members. For stone-mound structures it may be desirable
to measure the wave-induced movement of individual armor units.

9.2 Wind-Wave Measurements

Visual Observations

Wind-wave measurements can be made by the simpler and less expensive approach
of an observer visually estimating the height, period, and direction of the waves.
The estimated wave height is assumed to be the signiWcant height and the estimated
period is assumed to be the average, spectral peak, or signiWcant period. Reasonable results require an observer with some experience at making wave observations.Some scaledobject inview mightbeusedto estimatewave heightanda watch
is used to time a given number of waves to estimate the wave period.

Studies to compare visual estimates of wave height with measured values have

concluded that individual wave height estimates can signiWcantly diVer from


-----

Field and Laboratory Investigations / 289

measured values, but longer term compilations of wave height estimates are
more representative of measured values (see Schneider and Weggel, 1980, Soares,
1986). Schneider and Weggel (1980) found that visually estimated wave periods
were on average higher than the peak period of the measured spectrum, primarily because the observers failed to include smaller waves in their estimate.

An example of a coastal visual wave observation program is the Littoral

Environment Observation program of the U.S. Army Corps of Engineers
(Schneider, 1981). Volunteers at over 200 coastal locations estimate wave
breaker height, period, and direction as well as other nearshore phenomena
such as longshore current velocity and beach face slope.

Weather ships stationed at Wxed positions at sea and observers on cruising

maritime vessels also make periodic wave height, period, and direction estimates
as well as meteorological observations including wind speed and direction. These
data have been collected and published. For the United States data are published
by the National Climate Data Center (U.S. Naval Weather Service Command,
1976).

Instrumental Wave Measurements

Wave measurements, yielding a one-dimensional water surface time history or,
recently with more frequency, directional wave data are made with a wide variety
of instrument types. The nature of these instruments dictates that most wave
measurements be made in coastal areas. The cost in physical eVort and money to
maintain an operating wave gage is relatively large. For a variety of reasons, the
percentage of time that worthwhile data are obtained is commonly much less
than 100%. Most of the common types of instruments in use are brieXy discussed
below. For a more detailed coverage of instruments and procedures for wave
measurement see National Research Council (1982), Ribe and Russin (1974),
and Tucker (1991).

The common types of one-dimensional wave gages include:
StaV gages. This is a vertical staV that penetrates the water surface and is

capable of electronically detecting the variation of the water surface elevation
with time by a change in resistance, capacitance, or inductance. StaV gages
usually must be mounted on a rigid structure that does not interfere with the
water motion in the vicinity of the gage. Depending on the type and mounting of
the gage some of the following diYculties may be encountered: marine fouling or
ice may prevent the probe from detecting the water surface movement, lightning
may disrupt system electronics, gage-induced and other surface disturbances
may cause erroneous readings, and human tampering or Xoating objects may
damage the gage.

A variation on the electronic staV gage is the photo-pole gage, which consists of

a vertical pole with a scale marked on it that is photographed by a movie or video
camera. The resulting photographs are analyzed frame-by-frame to produce


-----

290 / Basic Coastal Engineering

the surface record time history. This requires a lot of eVort, but the photo-pole
gage requires no electrical power, is self-calibrating, and has no nonlinearity
problems. It is most useful for special studies rather than synoptic measurement
of wave climate.

Pressure gages. In Section 2.4 it was noted that a submerged pressure sensor

can serve as a wave gage if it is suYciently close to the surface to adequately
detect the wave-induced dynamic pressure variation. These gages are typically
mounted on a stable base placed on the sea Xoor in the nearshore area or on the
leg of a pile-supported structure. Pressure gages avoid the free surface so they are
not exposed to ice, tampering, or damage from Xoating objects, but they may
suVer marine fouling and damage from dragging anchors and Wsh trawls.

For relatively low-amplitude swell Eq. (2.32) can be used to determine the

wave height and period. For higher amplitude waves some nonlinear theory must
be used (see Grace, 1978 and Hsiang et al., 1986) and the analysis becomes more
complex. For wave spectra, the measured pressure spectrum can be computed
and converted to the surface wave spectrum using the dynamic pressure variation
in Eq. (2.32).

Accelerometer buoy gages. A moored Xoating buoy containing a device to

measure the time-dependent vertical acceleration of the buoy can be employed
as a wave gage. If the vertical acceleration is electronically integrated twice a
signal that represents the time-dependent surface elevation is produced. This
signal is then transmitted directly or by satellite link to a shore receiver. Commercially available accelerometer buoy gages are typically spheres about a meter
or less in diameter and have been moored in water up to 200 m deep. Since they
operate on the surface, they are prone to damage by ice, Xoating objects, or
vandalism.

It is becoming more common to include wave direction in a wave measure
ment program. This is typically done by one of the following types of instrumentation:

Point-array gages. A horizontal array of one-dimensional wave gages operat
ing simultaneously can produce data that will yield the directional wave spectrum. This typically involves three to six gages along a line or on a twodimensional grid, with a gage spacing that depends on the anticipated range of
wave frequencies to be measured.

Bottom-mounted combination gages. A bottom-mounted pressure gage to

measure the surface elevation time history combined with a device such as a
sphere with orthogonal strain gages that measures the wave-induced drag force
in horizontal orthogonal components will function as a directional wave gage.
Orthogonal current meters may also be used to detect wave directionality.

Heave–pitch–roll buoy gages. This is a moored buoy that simultaneously

measures vertical acceleration and the local water surface slope in orthogonal
directions as a function of time.


-----

Field and Laboratory Investigations / 291

9.3 Other Hydrodynamic Measurements

Water Level Fluctuations

Time-dependent mean water level changes having periods greater than those
common to the wind wave portion of the wave energy spectrum—particularly
the astronomical and meteorological tides—must be measured for many coastal
projects and for a synoptic understanding of a coastal area. These water level
Xuctuations can be determined from most periodic wind wave measurements by
analyzing the record using a procedure that Wlters out the wind wave frequencies
in the record. Instruments for directly measuring water level Xuctuations achieve
the same result by mechanically Wltering out the higher frequency components in
the measured water surface time history.

One simple device for mean water level measurements is the stilling well-Xoat

system depicted in Figure 5.1 and discussed in that section. The higher frequency
component damping achieved by frictional dissipation at the oriWce and by the
stilling well to oriWce area ratio may be insuYcient for the accuracy of water level
measurement desired. Also, wave nonlinear eVects can cause a net displacement
of the mean water level inside the well relative to the mean water level outside the
well (Cross, 1968). To eliminate these problems some investigators have used
stilling wells with long narrow diameter tubes attached to the oriWce to provide
additional linear damping (see Seelig, 1977).

A submerged pressure measuring device can be used to measure water level

Xuctuations if suitable high-frequency damping is achieved. This can also be
achieved by a long narrow tube leading from the water to the pressure transducer. A variation on this system is to lay a long tube from the shore to a point
oVshore where the water level is to be measured and to drive air through the tube
out the open end located underwater. The pressure gage is connected to the
landward end of the tube and, since the hydrostatic pressure of the air in the tube
can be neglected, measures the pressure at the seaward end of the tube. The air in
the tube dampens the higher frequency components.

Coastal Currents

The coastal currents of interest include nearshore currents seaward of the surf
zone and in channel entrances, as well as the longshore current in the surf zone.
Currents in the surf zone are much more diYcult to measure because of wave
breaking and the related higher turbulence level which suspends sand and
entrains air, as well as because of the shallower depths with Xuctuating water
levels that will cause alternate water and air exposure at some locations.

Current measurements can best be grouped into two classes: Eulerian, which

involve measurements at Wxed points with current meters, and Lagrangian,
which involve the measurement of water paths and speeds with Xoats or dye


-----

292 / Basic Coastal Engineering

that follow the water motion and are tracked by some surveying procedure. For
some studies such as determining the current velocity in an inlet during a tidal
cycle the Eulerian approach is appropriate, whereas to determine the fate of
wastes discharged from a marine outfall the Lagrangian approach is better. In
many studies a combination of the two classes is best.

The following types of current meters are in common use:
Propeller and rotor current meters. Current meters, which measure current

speed with a propeller or rotor whose speed of angular rotation is related to
the passing Xow velocity and that may have a vane to measure Xow direction, are
in common use in oceanographic studies. They are also useful for applications
outside the surf zone and in channel entrances.

Electromagnetic current meters. A relatively small sensor (sphere or cylindrical

slice) with internal electronic components measures the Xow speed and direction
past the meter. It functions by electronically setting up a magnetic Weld that is
modiWed as water Xows past the sensor. This in turn modiWes a current voltage in
a separate pair of orthogonal electrodes in the sensor. The meter has no moving
parts and can be strongly constructed and supported for measurements in the
surf zone.

Ultrasonic current meter. This meter consists of piezoelectric transducers

which act both as transmitter and receiver of ultrasonic waves. The water Xow
velocity past the unit is detected either by measuring the modiWed speed of the
ultrasonic pulse or by measuring the modiWed frequency of the pulse as it moves
with and then against the Xow. Orthogonal units allow the determination of Xow
direction too. Although it has no moving parts this type of meter has seen much
less use in the surf zone.

Bottom-mounted combination wave gages that contain a sphere with orthog
onal strain gages to measure wave direction will also yield current information if
the data are appropriately analyzed.

The common applications of Xoat or dye tracers include:
Floats. A tracking Xoat must be buoyant but not extend above the surface so

much that it is aVected by the wind. A brightly painted plastic bottle almost Wlled
with water makes an inexpensive but useful Xoat. If it is desired to measure the
Xow velocity at a particular distance below the surface a Xoat with little drag can
be tethered to and support a submerged drogue that has a higher drag and
indicates the Xow conditions at that submerged point. Floats may be tracked
by a pair of transits employing triangulation or by sequential photographs taken
at Wxed time intervals from a helicopter or balloon. Sequential timed determinations of position allow sequential velocity determinations to be made.

A point velocity determination can be made by releasing a Xoat on a short

tether of known length and measuring the time required for the tether to become
fully extended.

Dye. Any type of concentrated dye that is very visible and not harmful to the

environment may be used. Dye tracing has been used for easy estimates of


-----

Field and Laboratory Investigations / 293

current speeds in the surfzone by measuring the time it takes the dye to travel a
measured alongshore distance. Dye patches diVuse so they cannot be used for
long distances like Xoats.

Wind

Wind speed and direction data are often available from local airports and other
meteorological stations. The standard elevation for wind measurements is 10 m
above the ground surface and there should be no nearby obstructions to distort
the measurements. For wind stress determinations (e.g., for wind transport of
sand studies) a series of at least four velocity measurements should be made over
a vertical distance within close proximity to the ground.

Recording anemometers which consist of a propeller or rotating cups are

commonly used. The propeller anemometer also has a vane to direct the propeller into the wind and to record the wind direction. Ultrasonic sound anemometers have also been used. A simple hand held anemometer which has a ball in
a calibrated tube of increasing diameter with an open end that is to be exposed to
the wind (like a Xoat Xow meter for pipe Xow measurement) is useful for easy
Weld estimates of wind speed.

9.4 Coastal Morphology and Sedimentary Processes

Many coastal engineering activities are concerned with the interaction of coastal
sedimentary processes and coastal works such as the construction of structures for
shore protection and stabilization, dredging at channel entrances and harbors, and
beach nourishment. To understand these processes and to monitor eVects of
coastal works it is important to be able to measure shoreline topography/hydrography, sediment properties, and sediment transport processes and rates.

Coastal Morphology

The above-water topography and submerged hydrography where coastal processes are active must periodically be measured for many types of coastal
investigations. Since the beach face and nearshore zone are often undergoing
relatively rapid change, large areas must often be surveyed quite rapidly. For
example, an investigation of the impact of a seawall on the storm wave-induced
scour and natural rebuilding in front of the seawall may require surveys to be
carried out just before the storm arrives, immediately after the storm abates, and
periodically thereafter until signiWcant changes have ceased. Hydrographic surveys across the surf zone (especially during the arrival of high waves) can be very
diYcult to carry out.

The most common surveys involve the measurement of a series of beach

proWles oriented perpendicular to the shore and extending from the dune, cliV,


-----

294 / Basic Coastal Engineering

or structure line to the oVshore point where negligible change in bottom hydrography is occurring. These proWles may be equally spaced or more closely spaced
in the area of greatest interest (e.g., up- and downcoast of a new structure) with
wider spacing at some distant point to measure background changes that are
naturally being caused by the wave/current conditions in the area. To quantify
bottom changes at a tidal or harbor entrance channel a series of proWle surveys
would typically be measured along parallel lines oriented normal to the channel
axis.

The spacing of proWle lines, the techniques used to determine the position of

the measurement points, and the precision of the bottom elevation measurement
must all be consistent with the desired accuracy of the survey. For example, an
error of 3 cm in depth measurement over an active coastal proWle line that is
300 m long and covering a distance of a kilometer along the shoreline represents
9000 m[3] of sediment (if the selected proWle lines are fully representative of the
beach in between the proWles).

Beach proWles are commonly measured by standard level and taping surveys.

Two Xags or targets along the proWle line at the landward end allow the rod
person to maintain the correct orientation. If repetitive surveys are to be made
over time at a given shore location it is important to establish a permanent
reference benchmark that will survive signiWcant beach erosion. The benchmark
must be referenced to some datum such as NGVD. The rod person will work as
far seaward as safety and ability to hold the rod steady will allow. Where there is
a signiWcant tide range, surveys should be coordinated with low tide conditions.
This will allow the wading portion of the proWle to be extended to a little more
than a meter below the lowest tide level. To extend the proWle further seaward
the remainder of the proWle would be done with a vessel and fathometer or
leadline at higher tide levels, being sure to overlap the two portions of the proWle
survey as a check.

The seaward portion of a proWle line, measured from a vessel, will typically be

much less accurate than the landward portion of the proWle measured by standard surveying techniques. To overcome this problem, other beach proWling
techniques have been developed:

Survey sled. The survey sled consists of a pair of parallel sled runners about

5 m long and spaced 2 to 3 m apart that, with guy wires, supports a vertical pole
marked with a scale. A vessel pulls the sled to an oVshore position from which it
is winched back to and on shore along the proWle line while a level is used to read
bottom elevations from the scale on the pole. The distance oVshore along the
proWle can be determined from a scale on the line that pulls the sled landward
(Langley, 1992). Comparative tests (Clausner et al., 1986) indicate that the sea
sled technique performs as well as any other procedure and much better than
soundings from a vessel.

Diver/stakes. This approach is useful if comparative bottom elevations at

selected locations are to be measured over a long period of time and diving


-----

Field and Laboratory Investigations / 295

services are available. Semipermanent vertical stakes are securely placed into the
sea Xoor at the points of interest. A diver routinely visits the stakes and measures
the distance from the top end of the stake to the sea Xoor to measure the change
that has taken place.

CRAB. The U.S. Army Corps of Engineers (Birkemeier and Mason, 1984) has

a Coastal Research Amphibious Buggy (CRAB) that is a 10.6 m high tripod on
wheels that can be driven through the surf and nearshore area. The driver and
motor sit on a platform on top of the tripod. As the CRAB is driven through the
area to be surveyed periodic total station measurements can be made on the
reXector prism mounted on the CRAB to establish x–y–z coordinates of successive sea Xoor positions. The CRAB also serves as a mobile platform to access the
surf and nearshore zones to make a variety of other measurements.

Besides the proWle surveys discussed above, other coastal morhpology meas
urements of interest to the coastal engineer include:

Aerial photographs. The standard vertical air photographs employed for

photogrammetric measurement of land topography are frequently used in
coastal engineering studies. Overlapping photographs taken periodically along
the coastal section of interest are very valuable in giving a synoptic picture of the
characteristics of the coastline and periodic changes in these characteristics.
Sequential photographs may also be analyzed to measure shoreline change
rates (Anders and Byrnes, 1991).

Laser technology. An airborne laser transmitter and receiver can be used to

detect the water and sea Xoor surface elevations. Systems employing this technology from a helicopter can quickly, and with acceptable accuracy in many
shallow water situations, measure the hydrography over broad areas (Irish and
White, 1997).

Seismic reXection and side scan sonar. With side scan sonar, acoustical pulses

are transmitted to the sea Xoor and the return signal can be read to detect the
surface texture and (with calibration data from occasional bottom samples) the
composition of segments of the sea Xoor surface. Seismic reXection, often used in
conjunction with side scan sonar, can be used to detect the geometry of subbottom layers (Williams, 1982). These techniques are useful, for example, in
Wnding and quantifying the volume of potential oVshore sand borrow areas for
beach nourishment.

Sediment Properties

It was noted in Chapter 8 that the beach sediment property of greatest interest to
coastal engineers is the representative grain size and size distribution.

The number and type of sediment samples to be collected in a sampling

program depends on the intended use of the sample analyses and the time and
funding available for the sampling and analysis program. For a potential borrow
area for beach nourishment, core samples should be taken throughout the


-----

296 / Basic Coastal Engineering

borrow area. For beaches, samples can be taken from the upper few centimeters
of depth.

Beach sand characteristics commonly vary more across the shore-normal

proWle than alongshore. The U.S. Army Coastal Engineering Research Center
(1984) recommends that for reconnaissance surveys a sample be taken from the
wetted beach face and from the dunes at points along the shoreline selected from
a visual inspection of beach variability. For more thorough sampling programs,
samples might be taken at constant spacings along the active beach proWle and at
set distances alongshore. A quarter of a cup sample is generally adequate for
most sample analysis procedures.

A Weld estimate of the median sand grain size can be made by visual comparison

of a sample with diVerent diameter particles glued to a card or contained in vials.
Laboratory grain size analyses are either done by sieving or settling tube analysis.

Sieve analysis. U.S. Standard Sieve opening sizes vary from 125 mm down to

0.038 mm, with opening sizes below 5.6 mm decreasing by a constant ratio of the
fourth root of 2 (¼ 1.19) or 0:25F intervals. For typical beach sands, alternate
sieve sizes between 2.0 mm and 0.062 mm (i.e., 0:5F intervals) might be used to
perform a size analysis.

A dry sample (40 to 60 grams if Wne sand, 100 to 150 grams if coarse) is passed

through the series of sieves and the percent of total cumulative sample weight
collected on successively larger sieves is plotted versus sieve opening size to yield
a cummulative size–frequency diagram similar to Figure 8.1.

Settling tube analysis. The terminal settling velocity of a particle in still water

depends on the particle size, shape, and speciWc gravity. Settling tube analysis
yields a grain sedimentation diameter which is the diameter of a sphere of the
same density as the sediment grain and with the same settling velocity in water at
a standard temperature. The sedimentation diameter will be close to but not
generally equal to the sieve diameter of a sand grain.

A variety of types of settling tubes are in use. Generally they are a still vertical

water column in which a sample settles and is collected at the bottom. The rate of
accumulation of the grains at the bottom is then related directly to the grain cummulative size–frequency distribution. The rate of accumulation of sediment grains
can be determined by weighing the accumulated grains, by measuring the decreasing water pressure just above the accumulation point, or by a visual procedure.

Settling tube size analyses are faster than sieve analyses and do not require as

large a sample. Most settling tube systems are designed to record data electronically and then directly plot the cummulative size–frequency diagram and compute basic sediment size parameters.

Sediment Transport

Longshore sediment transport rates have beem measured primarily by conducting periodic topographic/hydrographic surveys at locations where erosion or


-----

Field and Laboratory Investigations / 297

deposition is occurring (see Chapter 8). However, there have been some Weld
experiments in which ‘‘instantaneous’’ measurements of sediment transport
patterns and rates have been made.

Transport patterns. Field measurements of nearshore sediment transport pat
terns have been made by tagging a signiWcant volume of sediment grains,
returning them to the nearshore area, and sampling to detect where the tagged
sediment has been transported. An example of such a study would be to determine the patterns of sand movement around and through a groin that is naturally bypassing sediment.

There has been some use of radioactive tracers, but most tracer studies use a

Xuorescent dye to color sand particles. The dying technique must produce a
coloring that will be resistant to washing oV the grains and that will not change
grain transport characteristics. After the tagged sand grains have been released,
samples are collected in the down-transport direction. When the samples are
dried and spread, an ultraviolet light may be used to count the number of tagged
particles. Plotted contours of tagged particle concentration will indicate the
transport pattern; and if the time of sample release and collection are noted,
particle transport velocities may be estimated. Horikawa (1988) discusses these
matters in more detail.

Transport rates. Field measurements of sediment transport rate have been

made by using both sediment tracers and sediment traps that collect suspended
load and bed load material passing the trap.

To determine volumetric sediment transport rates using tagged sand particles

requires that beach face core samples be taken and the depth of mixing of tagged
particles be determined from these cores. This gives the depth of the transport
layer which, when multiplied by the width of the transport layer and the transport velocity (from tracer displacement and elapsed time), yields the volumetric
transport rate. Komar and Inman (1970) used this technique to measure longshore transport rates in the surf zone.

A variety of traps for collecting suspended load and bed load have been used

(Horikawa, 1988). Essentially, these are devices that collect moving sediment so
that the concentration of suspended sediment load at sampling points or the
volume of bed sediment entering a given trap opening width in a given time can
be measured. Horikawa (1988) indicates that it is easier to collect suspended load
than bed load samples because the suspended load generally has a lower concentration and because bed load samplers tend to disturb the sea Xoor which
aVects the accuracy of sample collection.

Suspended load traps include intake pipes facing the Xow where the Xow is

pumped by suction at a pipe entrance velocity that should approximate the
oncoming Xow velocity, and grab samplers that quickly close to trap a set
volume of sand/water mixture. The measured suspended load concentration
integrated over a cross-section perpendicular to the Xow with the water volumetric transport rate gives the total suspended load transport rate. Bed load


-----

298 / Basic Coastal Engineering

traps include containers with one open side facing the oncoming bed load
transport, and larger open containers with the opening facing upward and
having its edge at the bed surface. The volume of sediment accumulated in a
given time is the bed load transport rate at that point that can be integrated
across the width of the transport zone.

9.5 Coastal Structures

Field investigations of coastal structures typically involve the direct measurement of hydrodynamic loadings on rigid structures such as piles and sea walls or
measurement of the displacement of armor units on rubble mound structures.
The hydrodynamic loadings of greatest interest are those caused by waves, which
would be measured at the structure by one of the wave gages discussed above.

For large structures such as seawalls and revetments the loading on a structure

is best measured by installing several pressure transducers into the face of the
structure, measuring the time-dependent pressures, and integrating the pressure
distribution over the face to determine the total force as well as its distribution as
a function of time (e.g., see De Girolamo et al., 1995). Commercially available
pressure transducers consist of a small diaphragm with a strain gage that
measures the pressure on the diaphragm by the pressure-induced bending of
the diaphragm. It is important that the pressure transducers be selected with
some knowledge of the frequency and maximum magnitude of the expected
pressure Xuctuations that are to be measured. As discussed in Section 7.6,
breaking wave-induced pressures can have a relatively large magnitude for a
very short duration.

For thin structures such as cylindrical piles, the loading on a test section of the

pile would be measured. This has been done by installing a ring of pressure
transducers around the circumference of the pile at the test section or by building
a load cell into the test section. The load cell would have interior strain gages
mounted so that the measured strain is related to the instantaneous load on the
test section.

Failure of rubble mound structures occurs when a signiWcant number of armor

units are displaced. Thus, Weld monitoring of the behavior of a rubble mound
structure requires a survey of the position of armor units immediately after
construction and before and after major storms. This can be done by marking
points on selected units and surveying the position of these points using standard
surveying techniques. An innovative improvement on standard surveying has
been to employ stereophotogrammetry using photographs taken from the air
(Davis and Kendall, 1992). Side scan sonar has been used to investigate the
condition of underwater armor units.

Large concrete armor units may fail when wave action causes the units to rock

in place and break. There is a related question of whether concrete units should


-----

Field and Laboratory Investigations / 299

be reinforced with steel rebar. To address this question some Weld armor units
have been instrumented with strain gages to measure in situ tensile stresses
(Howell, 1985).

9.6 Laboratory Investigations

Most laboratory investigations for coastal engineering are concerned with surface waves. There have been a few studies of wind-blown sand and coastal dune
processes, and some laboratory investigations of wind-wave generation processes. Also, steady Xow currents have been added in some tidal Xow model
studies and instantaneous tidal current Xows have been simulated by steady Xow
in basins.

But surface wave investigation are by far the most common. They may be

grouped into short wave and long wave studies. The former are concerned with
the wind wave portion of the wave spectrum and the latter with long wave
phenomena including tides, basin oscillations and tsunami propagation and
eVects.

One major advantage of laboratory wave studies is the control that the

investigator has over input wave conditions. Within the limits of the laboratory
wave generator being used, any monochromatic or spectral wave condition can
be run for any length of time. Owing to their smaller scale and the diYculties
involved in Weld work, laboratory studies can generally be conducted faster and
at lower cost.

But laboratory studies can have major drawbacks, namely scale and labora
tory eVects. Scale eVects generally arise over diYculties in maintaining viscous
and surface tension similarity where necessary. At smaller scales in the laboratory, Reynolds and Webber numbers are typically smaller than in the prototype.
If these forces are important in the prototype they are diYcult to simulate in the
laboratory, or they may be unimportant in the prototype but signiWcant in the
laboratory. For example, there have been numerous wave tank investigations of
wave loadings on vertical cylindrical piles but the laboratory Reynolds numbers
are several orders of magnitude smaller than found in the Weld for storm wave
conditions. Beach sand grains when scaled down to a laboratory size may be so
small that intersurface forces dominate whereas they are not important in the
Weld.

Laboratory eVects may also cause unsurmountable diYculties. The wave

generator employed in the lab may not be able to fully simulate the Weld waves
that can occur. During the early decades of wave tank research, wave generators
could produce only monochromatic waves. Recently, one-dimensional and directional spectral wave generators have come into use. Lateral boundaries on
three-dimensional models may aVect conditions over a signiWcant portion of the
laboratory investigation that is not aVected in the Weld.


-----

300 / Basic Coastal Engineering

Some laboratory investigations are studies of basic phenomena such as meas
uring the wave loading on a rigid vertical cylinder for a selected range of incident
wave conditions and water depths. Other investigations involve scaled model
studies of given Weld sites for selected Weld conditions, such as an investigation of
wave propagation toward the shore and into the lee of a proposed harbor breakwater conWguration. Numerical models are increasingly being used in the place
of physical models owing to their lower costs and greater Xexibility. Some Weld
problems such as coastal storm surge can only reasonably be studied by Weldcalibrated numerical models.

Much, but not all, of the instrumentation used in laboratory studies is similar

to the instrumentation used in the Weld (modiWed to smaller laboratory time and
spatial scales and less rigerous conditions). For more extensive discussion of
coastal engineering laboratory investigations see Hughes (1993) and Hudson
et al. (1979).

9.7 Wave Investigation Facilities

Wave investigations have primarily been conducted in Xumes and basins—tanks
holding water with a wave generator and, if necessary, a wave absorber to
prevent waves from reXecting back to the area where the investigation is being
conducted. A wide range of size and shape Xumes and basins have been used.
Flumes having common lengths of 30 to 40 m, widths of a meter or so, and water
depths of less than a meter are used for two-dimensional investigations. Basins
would be signiWcantly wider and used for three-dimensional studies.

Wave tanks constructed during the early to middle years of the 1900s had only

monochromatic wave generators. By 1960–1970 irregular or spectral wave generators became increasingly common. Figure 9.1 schematically depicts various
types of monochromatic wave generators (see Sorensen, 1993 for more detailed
discussion.). Most common are the piston or Xap generators, the former being
better for shallow water waves and the latter better for deep water waves. Some
more complex wave generators are designed so that they can be modiWed from
piston to Xap motion as the desired wave period is changed. The frequency of
oscillation of the piston or Xap establishes the wave period and the amplitude of
piston or paddle motion (for a given wave period) establishes the wave amplitude.

A variety of wave absorbers have been used. The ideal absorber would be a

rough porous Xat slope, but this requires a large portion of the wave Xume or
basin, and would not be easy to relocate as studies change. Consequently,
modiWcations of this ideal have been employed (see Sorensen, 1993).

If, for example, the stability of a proposed rubble mound structure is being

investigated, the model structure will cause wave reXection, the reXected waves
propagatingback to the wave generator, reXecting fromthe generator, etc. to cause


-----

Field and Laboratory Investigations / 301

Piston Flap

Plunger Pneumatic

Figure 9.1. Various monochromatic wave generators. (Sorensen, 1993.)

a very diVerent incident wave condition than that desired. In the past this problem
was dealt with by using a long wave Xume, generating a burst of a few waves, and
stopping the generator between bursts to allow the reXected wave energy to
dissipate. Recently, wave generators have been designed that detect the reXected
waves and adjust the piston or blade motion to cancel out the reXected waves.

During the past few decades irregular wave generators have become common.

Figure 9.2 schematically depicts a common type of irregular wave generator. An
appropriate electrical input signal is sent to the generator to drive the piston/
blade by a hydraulic, pneumatic, or mechanical device. The servo senses the
piston motion and sends a proportional voltage feedback to the signal control.
The input and feedback signals are continuously compared to adjust the piston
motion to the desired form. A monochromatic wave can be generated by inputting a sinusoidal signal. A nonsinusiodal oscillating signal can be input to
generate better cnoidal or solitary waves. For spectral waves the input signal is
typically produced in one of three ways:

1. By superimposing a large number of sine waves of diVerent periods and

amplitudes with random phasing

2. By Wltering a white noise electrical signal to form the desied irregular wave

input signal spectrum


Piston Flap

Plunger Pneumatic


-----

302 / Basic Coastal Engineering

Input signal

signal

control

Blade

Hydraulic

pneumatic Servo Piston

or

mechanical

drive

Figure 9.2. Typical irregular wave generator. (Sorensen, 1993.)

3. By creating an input signal that will produce a previously measured or

artiWcially constructed surface elevation time history

There have been some eVorts to use wind to generate irregular wave spectra in

laboratories. But, because of scaling problems (see Sorensen, 1993) and improved mechanical spectral wave generators, waves generated solely by the
wind are no longer used. Wind has been used over mechanically generated
irregular waves to more realistically steepen the fronts of waves as would happen
during a storm.

For some three-dimensional studies it is desirable to generate directional wave

spectra. This has been done by using a series (e.g., 60 to 80) of individually
activated wave generators along a line and facing in the same direction. By a very
complex operation of driving each of the generators with a diVerent period,
amplitude and phasing, a directional wave spectrum can be generated.

9.8 Scaling of Laboratory Investigations

Laboratory investigations are commonly carried out at signiWcantly reduced
scale from the prototype. Thus, attention must be paid to appropriate scaling
relationships. Wave motion predominantly involves a balance between pressure,
gravity, and inertia so Froude similarity dominates. But, as discussed above,
viscous and surface tension forces may be important. For Froude similarity the
time ratio equals the square root of the length ratio, the pressure ratio equals the
length ratio, and the force ratio equals the length ratio to the 2.5 power.

Scale diVerences are commonly accounted for in experimental results by

presenting the results on dimensionless plots (e.g., see Figures 2.11, 2.12, 2.15,
3.5, 4.9, 4.11, 6.10, and 7.3). Consider Figure 2.15, which gives the results from a


Input signal

signal

control

Blade

Hydraulic

pneumatic Servo Piston

or

mechanical

drive


-----

Field and Laboratory Investigations / 303

wave tank experiment at reduced scale on wave runup on a plane slope. Gravitational eVects are included in the Ho0=gT 2 term which is similar to a Froude

number. Surface tension and viscous eVects are not accounted for—it being
implicit that they are negligible or can be accounted for with an additional
correction factor.

If the lengths of laboratory waves are greater than about 3 cm surface tension

forces will be negligible as they are at prototype scale. Surface tension forces will
become important in physical models where the reduced scale causes very
shallow depths in some areas of the model. To overcome this potential problem
some models employ a distorted scale (i.e., a vertical length ratio that is larger
than the horizontal length ratio).

As discussed earlier, it is often impossible to conduct a laboratory investiga
tion at a suYciently large scale to fully eliminate viscous scale eVects in some
experiments such as the measurement of wave forces on a vertical pile. The
investigator must be aware that these scale eVects exist when considering the
results from such an experiment, and, when comparable near prototype scale
data are available, try to quantitatively account for this eVect.

An important facet of coastal engineering is the response of a sandy beach to

wave action. At a reduced laboratory scale the prototype sand size is reduced to
subsand size so sediment transport processes are not correctly simulated. The
usual approach in these experiments is to use a very Wne sand or some other
granular material of lower density to simulate sand in the laboratory. The
conduct of wave-sediment transport investigations then becomes more of an
art than a science. Several investigators (e.g., Noda, 1972; Kamphius and Readshaw, 1978; Kamphius, 1985; Kreibel et al., 1986) have developed testing procedures and related scaling guidance for these experiments.

When a three-dimensional investigation such as a study of the refraction and

diVraction that occurs as waves propagate from deep water to the shore is
conducted, space and cost limitations may require that the investigation be
conducted with less than optimum lateral basin dimensions. An undistorted
model scale may then lead to very shallow water depths in a portion of the
basin—and consequent viscous and surface tension scale eVects. Also, wave
heights may be so reduced as to be diYcult to measure with the required
accuracy. Thus, a distorted scale investigation may be necessary.

At a distorted scale, sloped boundaries become steeper which increases their

wave reXection characteristics compared to the Xatter prototype slope. This
problem can be overcome, for example, by increasing the laboratory boundary’s
roughness and porosity to reduce wave reXection. The impact of a distorted scale
on wave refraction and diVraction is more complex.

For shallow water waves wave celerity depends only on the water depth, so

refraction patterns are unaVected. For intermediate depth waves refraction is
aVected by scale distortion. A distorted scale intermediate depth wave investigation can be carried out if appropriate depth ratio and wave length ratios are


-----

304 / Basic Coastal Engineering

used (see Sorensen, 1993). But if signiWcant diVraction also occurs a conXict
arises so that it is impossible to correctly scale refraction and diVraction in an
intermediate depth wave investigation. For shallow water waves it is possible to
correctly scale both refraction and diVraction at the same time (see Sorensen,
1993). Pure diVraction investigations (constant depth) involve no scaling problems when a distorted scale is used.

9.9 Common Types of Investigations

Generally speaking, laboratory investigations are either basic investigations into
wave mechanics and the interactions of waves with beaches and structures or
model investigations for speciWc projects. Both are carried out in two-dimensional
tanks and/or three-dimensional basins. Some examples are presented below to give
a general sense of the important types of studies that have been conducted.

Investigations of basic wave mechanics have included measurement of surface

proWles and water particle velocity Welds to evaluate the eYcacy of various wave
theories for diVerent ranges of wave height and period and water depth. Extensive studies of wave breaking, runup, reXection, overtopping rate, and transmission past structures have been conducted—both as basic investigations and as
investigations for speciWc design projects that, in turn, have added to our general
knowledge of the phenomena involved. Basic investigations and model studies of
short wave refraction, diVraction, and three-dimensional reXection have been
conducted. Long wave investigations involving tide and tsunami propagation
and basin resonance have been important to our understanding of bay, coastal
river, and harbor hydrodynamics.

The design of stable rubble mound structures and the prediction of wave
induced pressure distributions and forces on piles, seawalls, and large submerged
structures require the evaluation of empirical coeYcients included in the design
formulas. Much of the guidance in this area comes from laboratory investigations. This is also true for the dynamic response of Xoating structures and the
wave transmission characteristics of Xoating breakwaters.

While, as indicated above, there are often serious scaling problems with

the investigation of beach response to wave attack, some useful basic investigations and model studies for speciWc locations have been carried out. This
is particularly true for the investigation of wave-induced scour at coastal structures. Some model studies where the bottom geometry is Wxed but a granular
tracer is used to indicate potential shoaling and scour patterns have been useful.

The vast majority of coastal engineering laboratory investigations focus on the

characteristics and eVects of short and long period surface gravity waves. But
other useful laboratory investigations have been carried out including studies of
internal waves, coastal and inlet currents, marine waste diVusion, and wind
loadings on structures.


-----

Field and Laboratory Investigations / 305

9.10 Summary

Coastal engineering is an atypical branch of civil engineering in that coastal
engineering design is less dependent on government or professional society
developed design codes (e.g., versus the design of bridges, buildings, highways,
and water treatment facilities). It requires a thorough understanding of the
complex air/water/land environment at the site where a design is to be carried
out, coupled with an understanding of the procedures needed to satisfy design
requirements in this complex environment. Both this understanding of the
coastal environment and the development of coastal engineering design procedures are strongly dependent on Weld and laboratory investigations–the subject of
this chapter.

9.11 References

Anders, F.J. and Byrnes, M.B. (1991), ‘‘Accuracy of Shoreline Change Rates as Deter
mined from Maps and Aerial Photographs,’’ Journal, American Shore and Beach
Preservation Association, January, pp. 17–26.

Birkemeier, W.A. and Mason, C. (1984), ‘‘The CRAB: A Unique Nearshore Surveying

Vehicle,’’ Journal of Surveying Engineering, American Society of Civil Engineers, March,
pp. 1–7.

Clausner, J.E., Birkemeier, W.A., and Clark, G.R. (1986), ‘‘Field Comparison of Four

Nearshore Survey Systems,’’ Miscellaneous Paper CERC 86–6, U.S. Army Waterways
Experiment Station, Vicksburg, MS.

Cross, R.H. (1968), ‘‘Tide Gage Frequency Response,’’ Journal, Waterways and Harbors

Division, American Society of Civil Engineers, August, pp. 317–330.

Davis, R.B. and Kendall, T.R. (1992), ‘‘Application of Extremely Low Altitude Photo
grammetry for Monitoring Coastal Structures,’’ Proceedings, Coastal Engineering Practice ’92, American Society of Civil Engineers, Long Beach, pp. 892–897.

De Girolamo, P., Noli, A., and Spina, D. (1995), ‘‘Field Measurement of Loads Acting On

Smooth and Perforated Vertical Walls,’’ Proceedings, Advances in Coastal Structures and
Breakwaters Conference (J.E. CliVord, Editor) Thomas Telford, London, pp. 64–76.

Grace, R.A. (1978), ‘‘Surface Wave Heights from Pressure Records,’’ Coastal Engineering,

Vol. 2, pp. 55–68.

Horikawa, K. (1988), Nearshore Dynamics and Coastal Processes–Theory, Measurement

and Predictive Model, University of Tokyo Press, Tokyo.

Howell, G.L. (1985), ‘‘Crescent City Prototype Dolos Study,’’ Proceedings, Workshop on

Measurement and Analysis of Structural Response in Concrete Armor Units, U.S. Army
Waterways Experiment Station, Vicksburg, MS.

Hsiang, W., Dong-Young, L., and Garcia, A. (1986), ‘‘Time Series Surface-Wave Recov
ery from Pressure Gage,’’ Coastal Engineering, Vol. 10, pp. 379–393.


-----

306 / Basic Coastal Engineering

Hudson, R.L., Herrmann, F.A., Sager, R.A., Whalin, R.W., Keulegan, G.H., Chatham,

C.E., and Hales, L.Z. (1979), ‘‘Coastal Hydraulic Models,’’ Special Report No. 5, U.S.
Army Waterways Experiment Station, Vicksburg, MS.

Hughes, S.A. (1993), Physical Models and Laboratory Techniques in Coastal Engineering,

World ScientiWc, Singapore.

Irish J.L. and White, T.E. (1997), ‘‘Coastal Engineering Applications of Higher-resolution

Lidar Bathymetry,’’ Coastal Engineering (in press).

Kamphius, J.W. (1985), ‘‘On Understanding Scale EVects in Coastal Mobile Bed

Models,’’ Physical Modelling in Coastal Engineering, (R.A. Dalrymple, Editor), A.A.
Balkema, Rotterdam, pp. 141–162.

Kamphius, J.W. and Readshaw, J.S. (1978), ‘‘A Model Study of Alongshore Sediment

Transport Rate’’ in Proceedings, 16th International Conference on Coastal Engineering,
American Society of Civil Engineers, Hamburg, pp. 1656–1674.

Komar, P.D. and Inman, D.L. (1970), ‘‘Longshore Sand Transport on Beaches,’’ Journal

of Geophysical Research, Vol. 75, pp. 5914–5927.

Kreibel, D.L., Dally, W.R., and Dean, R.G. (1986), ‘‘An Undistorted Froude Model for

Surf Zone Sediment Transport,’’ in Proceedings, 20th International Conference on
Coastal Engineering, American Society of Civil Engineers, Taipei, Taiwan, pp. 1296–
1310.

Langley, T.B. (1992), ‘‘Sea Sled Survey Through the Surf Zone,’’ Journal, American Shore

and Beach Preservation Association, April, pp. 15–19.

National Research Council (1982), ‘‘Proceedings, Workshop on Wave Measurement

Technology,’’ NRC Marine Board, Washington, DC.

Noda, E.K. (1972), ‘‘Equilibrium Beach ProWle Scale-Model Relationships,’’ Journal,

Waterways and Harbors Division, American Society of Civil Engineers, November,
pp. 511–528.

Ribe, R.L. and Russin, E.M. (1974), ‘‘Ocean Wave Measuring Instrumentation,’’ Pro
ceedings, Conference on Ocean Wave Measurement and Analysis, American Society of
Civil Engineers, New Orleans, pp. 396–416.

Schneider, C. (1981), ‘‘The Littoral Environment Observation (LEO) Data collection

Program,’’ Coastal Engineering Technical Aid 81–5, U.S. Army Coastal Engineering
Research Center, Ft. Belvoir, VA.

Schneider, C. and Weggel, J.R. (1980), ‘‘Visually Observed Wave Data at Pt. Mugu,

California,’’ in Proceedings, 17th International Conference on Coastal Engineering,
American Society of Civil Engineers, Sydney, pp. 381–393.

Seelig, W.N. (1977), ‘‘Stilling Well Design for Accurate Water Level Measurement,’’

Technical Paper 77–2, U.S. Army Coastal Engineering Research Center, Ft. Belvoir,
VA.

Soares, C.G. (1986), ‘‘Assessment of the Uncertainty in Visual Observations of Wave

Heights,’’ Ocean Engineering, Vol. 13, pp. 37–56.

Sorensen, R.M. (1993), Basic Wave Mechanics for Coastal and Ocean Engineers, John

Wiley, New York.


-----

Field and Laboratory Investigations / 307

Tucker, M.J. (1991), Waves in Ocean Engineering–Measurement, Analysis, Interpretation,

Ellis Horwood, New York.

U.S. Army Coastal Engineering Research Center (1984), Shore Protection Manual, U.S.

Government Printing OYce, Washington, DC.

U.S. Naval Weather Service Command (1976), ‘‘Summary of Synoptic Meteorological

Observations,’’ National Climate Data Center, Ashville, NC.

Williams, S.J. (1982), ‘‘Use of High Resolution Seismic ReXection and Side-Scan Sonar

Equipment for OVshore Surveys,’’ Coastal Engineering Technical Aid 82–5, U.S. Army
Coastal Engineering Research Center, Ft. Belvoir, VA.


-----

### Appendices

A. Notation and Dimensions

A L[2] bay surface and channel cross-section area, structure

projected area

Ac — channel cross section area

Ai L tidal component amplitude

a[0] — sediment porosity

ac, at L wave crest amplitude; trough amplitude

ax, az L=T [2] horizontal and vertical components of acceleration

B L wave orthogonal spacing, structure crest width

Bo L wave orthogonal spacing in deep water

C L/T wave celerity

Cd — drag coeYcient

Cg L/T wave group celerity

Cl — lift coeYcient

Cm — coeYcient of mass

Co L/T wave celerity in deep water

Cr — wave reXection coeYcient

Ct — wave transmission coeYcient

d L water depth, sediment grain diameter

d [0] L setup, setdown of mean water level

db L water depth at point of wave breaking

dc L channel depth

ds L water depth at structure toe

d50 L median grain diameter

D L cylinder diameter

E, Ek, Ep F total, kinetic, potential energy per unit crest width

E[¯] F/L average energy per unit surface area

F L, F,— wind fetch length, freeboard, force acting on a body,

Froude number

F1, F2 — dimensionless coeYcients in Bretschneider spectrum

Fc F centrifugal force

Fd F drag force

Fg F gravitational force

Fi F inertia force


-----

310 / Basic Coastal Engineering

Fs F/L force per unit length

f 1/T Coriolis parameter

fp 1/T wave frequency at spectral peak

G( f, u) — directional spectrum spreading function

g L=T [2] acceleration of gravity

H L wave height

Hb L breaking wave height

Hd L diVracted wave height

Hi L incident wave height

Hmax L maximum wave height

Hmo L signiWcant wave height based on spectral energy

Hn L average height of highest n percent of waves

Ho L wave height in deep water

Hr L reXected wave height

Hrms L root mean square wave height

Hs L signiWcant wave height based on individual wave

analysis

h L vertical distance from berm crest to depth at which

wave transport of sediment vanishes

hc L structure crest height above the sea Xoor

Ir — Iribarren number

K — coeYcient in sediment transport equation

KD — armor unit stability coeYcient

Kd — diVraction coeYcient

Kr — refraction coeYcient

Ks — shoaling coeYcient, wind stress drag coeYcient

Ksb — wind/bottom stress coeYcient

k 1/L,— wave number, inertia coeYcient

k[2] — parameter in cnoidal wave theory

KC — Keulegan–Carpenter number

L L wave length

Lc L channel length

Lo L wave length in deep water

Lp L wave length for fp at water depth of interest

Lr — model/prototype length ratio

M, N — solitary wave theory coeYcients, resonance modes

M FL moment acting on a structure

MdF — phi median diameter

MF — phi mean diameter

m — beach slope

mn L[2]=T [n] nth moment of a wave spectrum

mo L[2] zeroth moment of a wave spectrum


-----

Appendices / 311

N — number of waves in a wave record, number of data

points in a return period analysis

Ns — armor unit stability number

Ns[�] — modiWed armor unit stability number

N� — number of digitized values from a wave record

n — ratio of wave group to phase celerity

P F/T wave power per unit crest width, tidal prism

P(H) — cummulative probability of H

p F =L[2] pressure

p(H) — probability of H

Q L[2]=T [2], L[3]=T Bernoulli constant, potential volumetric sediment

transport rate

qx, qy L[2]=T Xow rate per unit width

R L,— vertical elevation of wave runup above SWL, radial

distance to point of maximum hurricane wind
speeds, Reynolds number

Rp L runup exceeded by p percent of waves

Rs L runup of signiWcant wave

r —, L, T wave runup correction factor, radial distance in the

lee of a barrier, radial distance from hurricane eye,
time interval between data points

S — Strouhal number, structure damage level, Xuid

speciWc gravity

Sc L Coriolis setup

Sds L[2]=T [2] spectral energy dissipation rate

Sin L[2]=T [2] spectral energy input rate from the wind

Snl L[2]=T [2] spectral energy transfer rate by nonlinear interaction

Sp L atmospheric pressure setup

Sw L wind stress setup

Sxx, Syy, F/L radiation stress components

Sxy

S( f ) L[2]T frequency spectrum energy density

S( f, u) L[2]T directional spectrum energy density

S(T) L[2]=T period spectrum energy density

T T wave period

Te T eddy shedding period

TH T Helmholtz resonant period

TI T tidal component period

Tn, TNM T resonant periods of basin oscillation

Tp T wave period at spectral peak

Tr —, T model/prototype time ratio, return period

Ts T signiWcant period

T� T wave record length


-----

312 / Basic Coastal Engineering

T100 T average wave period

t T time

td T wind duration

tT T tsunami wave travel time

U L/T current velocity

Ur — Ursell parameter

u¯ L/T mass transport velocity

u,v,w L/T velocity components

V L[2], L=T, L[3] volume of mass transport per unit crest width in a

solitary wave, current velocity normal to
x-direction, volume of a body, vessel speed

VF L/T hurricane forward speed

Vf L/T particle settling velocity

W L/T, L, F wind velocity, Xoating breakwater width, channel

width, armor unit weight

WA L/T adjusted wind speed for SPM–JONSWAP method

WR L/T wind speed at R in a hurricane

X L particle travel distance

XP L wave breaker plunge distance

x,y,z L coordinate distances

a — beach slope angle, angle between wave crest line and

bottom contour line

ab — wave breaker angle with the shoreline

af — phi skewness measure

b — angle between barrier and line to point of interest

G L basin horizontal dimension

g — ratio of breaker height to water depth at breaking,

JONSWAP peak enhancement factor

gs F =L[3] speciWc weight of stone

Di — tidal component phase lag

DP F =L[2] diVerence between central and ambient pressures in a

hurricane

e L vertical component of particle displacement

z L horizontal component of particle displacement

h L surface elevation above still water level

ht L trough distance below still water line

u — angle between wave orthogonal and x-axis, angle of

wave approach to a barrier, angle between wind
and coordinate direction, rubble structure
face slope

m — coeYcient of static friction

n L[2]=T Xuid kinematic viscosity

r FT [2]=L[4] Xuid density


-----

Appendices / 313

s 1/T wave angular frequency

sF — phi deviation measure

t F =L[2] horizontal shear stress

F(f, d) — TMA spectrum function

F L[2]=T;— velocity potential; latitude; phi grain size measure

c L[2]=T stream function

cs L[2]=T stream function at water surface

v 1/T speed of earth’s rotation


-----

314 / Basic Coastal Engineering

B. Selected Conversion Factors

Multiply By To obtain

feet 0.3048 meters

fathoms 6.0 feet

1.829 meters

statute miles 5280 feet

1.609 kilometers

nautical miles 6076.115 feet

1.852 kilometers

acres 43,560 square feet

cubic yards 0.765 cubic meters

cubic meters 1.309 cubic yards

cubic feet 7.48 gallons (U.S.)

slugs 14.594 kilograms

pounds 4.448 Newtons

short tons 2000 pounds

metric tons 2205 pounds

long tons 2240 pounds

statute miles/hour 1.47 feet/second

knots 1.151 statute miles/hour

1.692 feet/second

pounds/square inch 0.0680 atmospheres

2.036 inches of mercury

6985 Newtons/square meter

2.307 feet of water

cubic feet/second 448.8 gallons/minute

0.0283 cubic meters/second

horse power 550 foot pounds/second

745.7 Watts (Newton meters/second)

foot pounds 1.356 Joules (Newton meters)


-----

Appendices / 315

C. Glossary of Selected Terms

Selected terms encountered in the text or common to U.S. coastal engineering
practice are deWned below. Most of these deWnitions are taken (many with
modiWcation) from: Allen, R.H. (1972), ‘‘A Glossary of Coastal Engineering
Terms,’’ U.S. Army Coastal Engineering Research Center, Ft. Belvoir, VA.

Accretion The buildup of a beach owing to natural processes which may be

supplemented by the interference of a structure with littoral processes.

Armor unit Stone or precast concrete unit placed on a stone mound coastal

structure as the primary protection against wave attack.

ArtiWcial nourishment The replenishment of a beach with material (usually

sand) obtained from another location.

Bar A submerged embankment of sand or other natural material built on the

sea Xoor in shallow water by the action of currents and waves.

Bay A recess in the shore or an inlet of a sea between two headlands, not as

large as a gulf but larger than a cove.

Beach berm A nearly horizontal part of a beach or backshore formed by the

deposit of material by wave and wind action. Some beaches have no berms;
others have more than one.

Beach face The section of the beach normally exposed to wave uprush.

Breakwater A structure that protects a shore area, harbor anchorage, or basin

from waves.

Bulkhead A structure (usually vertical) that prevents sliding or collapsing of a

soil embankment. A secondary purpose is to protect the embankment against
damage by wave action.

Bypassing Hydraulic or mechanical movement of beach material from the ac
creting updrift side to the eroding downdrift side of an inlet or harbor entrance.

Celerity The propagation speed of the wave form.

Coast That area of land and water that borders the shoreline and extends

suYciently landward and seaward to encompass the area where processes
important to the shore area are active.

Decay distance The distance waves travel as swell from the generating area. As

they travel through this region of relatively calm winds the signiWcant height
decreases and the signiWcant period increases. Dispersion of the spectral
components also occurs.


-----

316 / Basic Coastal Engineering

Deep water waves Waves propagating across water depths that are greater than

half the wave length.

DiVraction (of waves) The phenomena by which energy is transferred laterally

along the wave crest. When a train of waves is interrupted by a barrier
diVraction causes energy to be transmitted into the lee of the barrier.

Diurnal tide A tide having only one high and one low water level in a tidal day.

Duration, minimum The time necessary for steady-state wave conditions to

develop for a given wind velocity and fetch length.

Ebb Tide The interval between high water and the following low tide.

Fetch The surface area of the sea over which wind blows to generate waves.

Flood tide The interval between low water and the following high tide.

Forecasting, wave The prediction of future wave conditions for existing or

future wind or weather conditions.

Foreshore The part of the shore lying between the crest of the seaward berm (or

upper limit of wave runup at high tide) and the ordinary low water mark.

Fully developed sea The ultimate wind-generated wave condition that can be

reached for a given wind speed.

Groin A structure built generally perpendicular to the shoreline to trap littoral

drift and/or hold artiWcial nourishment.

Group celerity The speed at which a group of waves propagates.

Hindcasting, wave The prediction of wave conditions for historic wind or

weather conditions.

Inlet A short, narrow waterway connecting a bay, lagoon, or similar water

body to a larger body of water and often maintained by tidal and river Xow.

Jetty A structure built generally perpendicular to the shoreline to prevent shoal
ingofachannelbylittoralmaterials,andtodirectandcontrol Xowinthechannel.

Knot A term for speed equalling one nautical mile per hour.

Littoral current A current in the surf zone generated by incident wave action.

Littoral drift The sedimentary material in and near the surf zone moved by

waves and currents.

Littoral transport The movement of littoral drift.

Littoral zone The zone extending seaward from the shoreline to just beyond the

wave breaker line.

Longshore transport rate The volume of sedimentary material per unit time

being transported parallel to the shore.

Mean higher high water The average height of the higher high tide levels

averaged over a 19-year period.

Mean high water The average height of all the high tide levels averaged over a

19-year period.

Mean lower low water The average height of the lower low tide levels averaged

over a 19-year period.

Mean low water The average height of all of the low tide levels averaged over a

19-year period.


-----

Appendices / 317

Mean sea level The average height of all tide levels (usually on an hourly basis)

averaged over a 19-year period.

Mean tide level An elevation that is midway between mean high water and

mean low water.

Monochromatic waves A train of waves each having the same wave height and

period.

National Geodetic Vertical Datum 1929 (NGVD 1929) Mean sea level from

data at 26 North American coastal stations averaged over 19 years up to 1929.

Nautical mile The length of a minute of arc, generally one minute of latitude.

Accepted in the United States as 6076.115 ft or 1852 m.

Neap tide The tide occurring near the time when the sun and moon are most out

of phase producing the two lower tide ranges during the monthly tidal cycle.

Nodal zone A shore location where the net direction of longshore transport of

sediment changes.

North American Vertical Datum 1988 (NAVD 1988) Adjustment of NGVD

1929 to 1988 including gravimetric and other anomalies.

Orthogonal A line drawn perpendicular to successive wave crests.

Phi sediment size The negative logarithm to the base two of the sediment

particle diameter.

Pier A structure, usually of open construction (e.g., on piles), extending out

into the water from shore, to serve as a vessel landing place, a recreational
facility, etc.

Quay A section of paved stabilized bank along a navigable waterway or in a

harbor, used to load and unload vessels.

Radiation stress The excess Xux of momentum owing to the existence of a wave.

Recession The retreat of a beach or other coastal section owing to natural

processes and/or the eVects of structure interference with littoral processes.

Refraction (of waves) The process by which intermediate or shallow water

waves have their direction changed because the bottom contour is not parallel
to the wave crest. May also be caused by currents.

Relative depth The ratio of water depth to wave height.

Revetment A facing or veneer of stone, concrete blocks, etc. placed on a sloping

embankment to protect against erosion by waves or currents.

Rip current A strong relatively narrow current Xowing seaward through and

beyond the surf zone owing to the piling up of water in the surf zone by waves.

Riprap A protective layer of stone typically having a wide size gradation and

placed to protect an embankment from erosion.

Rubble mound structure A structure built of a mound of stones typically with an

outer layer of large stone sizes (armor stone) and one or more interior layers of
smaller stone.

Runup The surge of water up a slope (beach or structure) from the breaking of

a wave. QuantiWed as the highest elevation above mean sea level reached by
the water.


-----

318 / Basic Coastal Engineering

Scarp, beach An almost vertical surface on the beach caused by erosion of the

beach material from just in front of the scarp.

Sea breeze A light onshore directed wind resulting from the unequal tempera
ture of the sea and land.

Seas Waves in the fetch being actively generated by the wind.

Seawall A structure, usually massive in nature (rubble mound or concrete)

designed to prevent Xooding and wave damage to the land in its lee.

Seiche A resonant oscillation in a body of water.

Semidiurnal tide A tide with two relatively equal high and low water levels in a

tidal day.

Setup (setdown) The wave-induced rise (fall) of the mean water level above

(below) the still water level.

Shallow water waves Waves in water suYciently shallow that the water depth is

less than one-twentieth of the wave length.

Shingle Granular beach material coarser than ordinary gravel.

Shoal (noun) An especially shallow section of the nearshore area, often caused

by sediment deposition.

Shoal (verb) To become shallow; to cause to become shallow; or, for waves, to

propagate from deep in to shallower water.

Shoreline The boundary between the land surface and the surface of a water

body such as an ocean, sea, or lake.

SigniWcant wave height The average height of the highest one-third of the waves

in a given wave record.

SigniWcant wave period The average period of the highest one-third of the

waves in a given wave record.

Solitary wave A wave having a crest but no trough (so the wave length is

inWnite).

Spring tide The tide occurring near the time when the sun and moon are most

in phase producing the two higher tide ranges during the monthly tidal cycle.

Standing wave A wave produced by the propagation in opposite directions of

two identical wave trains. The resulting water surface oscillates only in the
vertical direction with alternating nodal and antinodal points.

Storm surge The buildup of the water level along the coast owing to wind
induced shear and pressure forces.

Surf beat Irregular oscillations of the nearshore water level with periods of the

order of minutes.

Surf zone The area between the outermost breaker and the limit of wave runup.

Swell Freely propagating wind-generated waves that have propagated out from

the area of generation.

Tidal prism The total volume of water that enters into or Xows out of a harbor

or estuary in one tidal cycle, excluding river Xow and surface runuV.

Tide range The diVerence in height between successive high and low tides.


-----

Appendices / 319

Tombolo A segment of deposited material in the lee of an oVshore structure

that connects the structure to the land.

Transitional (or intermediate) water wave A wave propagating in water having a

depth between one-half and one-twentieth of the wave length.

Tsunami A long period wave generated by an underwater disturbance.

Wave steepness The ratio of wave height to wave length.

Wave train A series of waves traveling in the same direction.


-----

### Index

Armor unit, per cent damage, 214, 217

shape, 215–218
stability, 216–217
stability coefficient, 217–218
weight, 215, 220–221

Armor stone specification, 223–224

Basin oscillations, 113–138

Helmholtz resonance, 136–137
resonant patterns, 117, 133, 201
resonant period, 114

Beach, berm, 224

dynamic equilibrium, 247–248
measurements, 269
nourishment, 256, 272
profile, 224–225
slope, 254

Beach profile closure depth, 257–258
Bernoulli equation, 15, 32, 233
Bottom stress, 115–116, 123, 134, 138, 142,

144

coefficient, 145

Boundary conditions, 10–11, 13, 53, 69,

136, 142, 144

Breakwater, berm, 224–225, 234

floating, 199, 209, 211–212
low-crested, 215
offshore, 79, 214
rubble mound, 196, 215, 221,

225

Bretschneider wave spectrum, 149, 170,

177, 182–183

Cables, 195, 198–200, 209
Coastal engineering, definition, 3

literature, 3–4, 6
recent trends, 5

Coastal entrances, 280–282
Coastal environment, 1–2, 305


Coriolis acceleration, 115–117, 134,

138–139, 143, 148–149, 258

parameter, 116

Currents longshore, 149, 258–260

measurement, 288
rip, 253, 261
wind-generated, 247

Design storm, 138–141, 187, 214, 216–217,

227

Design wave, 79, 99, 177–179, 187–188,

196, 202, 204, 207, 209, 215–216, 218,
220–222, 224, 226, 238–241

Design wave selection

economic implications of, 222–223

Diffraction, analysis, 92–104

coefficient, 93
diagrams, 97–98
laboratory studies, 93
phenomenon, 80

Dispersion equation, 15, 17, 21, 47
Drag, coefficient of, 196–197, 203–206
Dune, characteristics, 247, 254

stabilization, 248, 276–277

Duration limited condition, 160, 184

Equilibrium beach profiles, 256–257
Equivalent deep water wave height, 45, 82
Extreme wave height analysis, 157, 187,

240

Fetch limited condition, 160, 178, 184, 214
Force, current-induced, 198

drag, 196–197, 199–201
ice-induced, 234–235
inertia, 197, 199–201, 203
lift, 207
measurement, 203–206
pressure-induced, 228–230


-----

322 / Index

Force, current-induced, 198 (Continued )

vessel-induced, 233
wind-induced, 276

Freeboard, 227, 238–239
Froude number, 105, 137, 143, 156, 303
Fully developed sea, 157, 160, 171, 181, 183

Groin, 214–215, 241, 248, 254, 260,

265–267

Hudson equation, 218, 220–221, 223–227

sensitivity of, 220

Hurricane, characteristics, 139, 182

probable maximum, 140, 183
standard project, 140–141
waves, 183

Inertia, coefficient of, 198, 199–201,

206–207

Inman’s size description parameters,

251–252

Iribarren number, 236

Jetty, 260, 262, 266–267, 275–276,

280–281

JONSWAP wave spectrum, 170, 172–173,

176, 183

Keulegan-Carpenter parameter, 201

Laplace equation, 11, 13, 53, 69–70, 136
Large submerged structures, 196, 209–210,

304

Lift, coefficient of, 207
Longshore bar, 254
Long wave equations, 114–115, 123, 133,

138, 142

Mass, coefficient of, 66, 197, 198, 203–204,

206, 209

transport, 58–60, 66, 261–262

Morison equation, 198, 200, 203–204, 207,

209

Nodal point, longshore transport, 262

water surface, 9, 35, 114, 116, 132–133,

136, 174, 288


Particle, acceleration, 18–19, 21, 199

orbit, 12, 15–16, 19–22, 38, 58, 65, 118,

120, 198, 201, 209

velocity, 12–13, 15, 18–24, 27, 31, 37, 48,

64, 66–71, 132, 197, 199–205, 209,
253, 304

Phi unit, 249–250
Pierson-Moskowitz wave spectrum,

171–172, 183

Piles, 195, 198, 202, 206, 228, 230, 298–299,

304

Pipelines, 4, 195, 198–199, 206–207, 254
Probability distribution, 162–163, 188–189,

240

wave height, 24–27, 33–34, 37–39, 47,

54, 61–62, 72, 79–85, 88, 93, 96, 99,
105, 125–126, 135, 159–165, 168, 170,
176, 187, 215, 221, 261, 264, 290

sediment size, 249–252, 273, 279, 296

Radiation stress, 30–35, 228, 259–260, 271
Rayleigh distribution, 162–166, 169, 171,

188, 222, 237, 240

Refraction, analysis, 71, 80–82, 90,

99–100, 177, 240

caustic, 88–89
coefficient, 82, 85, 90, 177, 221–222
current-induced, 91, 198, 207, 209, 233,

271

diagrams, 82–83, 86–88, 125–126
manual analysis, 82
numerical computation, 89, 186–187,

257

phenomenon, 79–80, 91, 233
template, 82, 86–88, 266

Refraction and diffraction of directional

spectra, 176–178

Relative depth, 12, 15–17, 26, 47–48, 54,

58, 61, 71–72, 79, 86, 173, 238

Resonance, 117, 119, 122, 124, 128,

130–133, 136–138, 158–159, 239, 304

Return period, 71, 139–140, 178–179,

187–190, 221–222, 234, 239

Revetment, 4, 45, 102, 214–216, 221,

223, 225, 232, 235–236, 241, 267,
298


-----

Reynolds number, 196–198, 200–201,

203–206, 209–210, 299

Sea level change, 150–151, 257
Sediment, properties, 248–252, 287–288,

293

sampling, 252, 295–298
size analysis, 252, 296
size distribution, 248–249, 295
Wentworth size classification, 249–250

Sediment budget, 248, 263, 268,

277–280

Sediment bypassing, 248, 267, 271,

273–276, 280–281, 286

Sediment transport, interaction with

structures, 265–269

longshore rate, 262–265
measurement, 249–252
processes, 293

Shoaling coefficient, 81, 177
Shoreline, numerical models, 248, 257,

269–271

Sink, sediment, 277–278
SMB wave prediction method, 183
Snell’s law, 83–84, 86
Source, sediment, 261–262, 268, 277
Spectral energy balance equation, 185
Spit, 262, 275, 279
Standing wave, 35, 37–38, 51, 130,

132–136, 228, 246

Storm surge, characteristics, 105

numerical analysis, 141, 144
simplified analysis, 144

Strouhal number, 201
Surf beat, 114–115
Swell, 158, 160, 176, 290

Tide, classification, 120,

components, 119–120
datums, 120–121
gage, 126, 150, 154
generation, 117–120
prediction, 119–120, 122–123
range, 122–123, 154

TMA wave spectrum, 170, 173–174
Transmission coefficient, 212–213, 238


Index / 323

Tsunami, defense against, 126–127, 304

generation, 124
runup, 124, 126
travel time, 126, 155

Ursell number, 62–63

Velocity potential, 11, 13–14, 18, 21, 35,

53–55, 69, 136, 210

Vessel-generated waves, 10, 80, 102–105,

211

Visual wave observation, 289

Wave breaking, 11, 32, 34, 38–44, 65, 68,

89, 157, 165, 186, 224, 254, 258–259,
261, 291, 304

breaker classification, 40–41

Wave celerity, 11, 14–17, 28, 39, 53, 56,

59–62, 65, 67–69, 79, 82–83, 87,
89–91, 105, 114, 159, 232, 303

Wave classification, 15–17
Wave, design, 79, 216, 222,

238–240

Wave direction, 91–93, 98, 175–176, 266,

270, 290, 292

Wave energy, 11, 22–25, 28–32, 67, 79–80,

88, 92–93, 99, 117, 126

energy density, 24
energy dissipation, 33–34
kinetic, 22–23, 35
potential, 22–23, 35
spectrum, 80, 92, 114, 137, 151,

167–176

Wave frequency, 167, 174–175, 178

angular, 12, 14, 134
spectral peak, 168, 174, 178, 239

Wave gage, accelerometer buoy, 290

directional, 290
photo-pole, 289–290
pressure, 290
staff, 289

Wave generation, 158–161, 179–180
Wave group celerity, 28–30
Wave height, distribution, 162–165

significant, 160, 162
maximum, 165


-----

324 / Index

Wave length, 11–12, 14–16, 21–24,

29–30, 37–38, 40, 53, 56, 59,
61–65, 70, 80–82, 86, 93, 96–98,
104, 125, 130, 174, 209, 212,
226, 303

Wave measurement, 288–290
Wave number, 12, 14, 70, 90, 134
Wave orthogonal, 79, 83, 89–90, 126
Wave overtopping, 4, 215, 217, 227, 237
Wave period, average, 166

distribution, 166
significant, 161, 164
spectral peak, 166

Wave power, 24–27, 67, 72, 125
Wave prediction, empirical, 179–183

hurricane, 182–183
numerical, 185–187
spectral models, 169–178

Wave-induced pressure force, 210
Wave reflection, coefficient, 37–38, 101–102

three-dimensional, 101
two-dimensional, 37–38

Wave record analysis, 161–166
Wave runup, 5, 42, 44–47, 217, 233, 237,

254–255, 261, 303

Wave setup and setdown, 30–35
Wave, shallow water, 17, 34, 40, 53–54, 64,

91, 114–115, 117–118, 125, 130,


132–133, 143, 182, 211, 260, 300,
303–304

Wave spectrum, characteristics, 161,

167–169

directional, 174–176
models, 169–174
moments, 168–169

Wave steepness, 12, 19, 41–42, 46, 55–59,

61, 71–72, 92, 126

Wave surface profile, 12, 14, 63
Wave theory, cnoidal, 61–64

numerical, 68–69
range of application, 71–72
small-amplitude, 10–15, 67
solitary, 64–65
Stokes, 54–61

Wave transformation, 5, 54, 79–80
Wave transmission, 99, 223, 227, 237–238,

304

Wave-wave interaction, 159, 161, 186
Wind, duration, 149

fetch, 160, 171
force, 276
measurement, 172, 179, 240, 293
sediment transport by, 261–264
stress, 128, 138, 142–145, 260, 293
stress coefficient, 145


-----

