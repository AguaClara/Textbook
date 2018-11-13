.. _title_Sed_Design:

********************
Sedimentation Design
********************

***************************************
Foundational Concepts
***************************************

To understand how sedimentation works, a few key concepts must first be developed. This includes understanding how and why flocs move in water. Remember, the goal of sedimentation reactor design is to optimize the floc-settling process.

Terminal Velocity
===============================
As flocs settle in water, they will fall at a speed dictated by the weight of the floc, the buoyancy of the floc, and drag from the water. These three forces - the gravitational weight force, the buoyant force, and the drag force - dictate the speed at which a floc falls and are detailed in the following free body diagram. We care about determining the speed at which flocs will fall because [WHY].

[FLOC FORCES FREE BODY DIAGRAM]

To determine the force balance on a falling floc, consider:

.. math::

  \sum F = m a

At terminal velocity, the floc has been falling for a long period of time so there is no acceleration and the right side of the equation simplifies to zero.

:math:`F_{drag} + F_{buoyant} - W_{floc} = 0`

Each of the force components can be determined by:

.. math::

  F_{drag} = C_D A_{floc} \rho_{H_2O} \frac{v_t^2}{2}

  F_{buoyant} = V\llap{---}_{floc} \rho_{H_2O} g

  W_{floc} = V\llap{---}_{floc} \rho_{floc} g

| Where:
| :math:`V\llap{---}_{floc} =` floc particle volume
| :math:`A_{floc} =` particle projected cross sectional area
| :math:`\rho_{floc} =` particle density
| :math:`\rho_{H_2O} =` water density
| :math:`g =` acceleration due to gravity
| :math:`C_D =` drag coefficient
| :math:`v_t=` particle terminal velocity
| :math:`D=` particle diameter

Plugging into the original force balance,

.. math::

  [C_D A_{floc} \rho_{H_2O} \frac{v_t^2}{2}]+[V\llap{---}_{floc} \rho_{H_2O} g]-[V\llap{---}_{floc} \rho_{floc} g] =0

Solving for terminal velocity, :math:`v_t`, provides

.. math::

  v_t = \sqrt{\frac{4}{3}\frac{gD}{C_D}\frac{(\rho_{floc}-\rho_{H_2O})}{\rho_{H_2O}}}

Terminal velocity is a function of fluid density, floc density, gravity, particle diameter, and the drag coefficient. To calculate velocity, all of those inputs must be determined.

The first component that we will focus on is the drag coefficient, :math:`C_D`. The drag coefficient is function of Reynolds Number, :math:`Re`, and the characteristic flow around a particle. As a reminder, :math:`Re = \frac{v_t D}{\nu}` where :math:`v_t` is the velocity of the fluid, :math:`D` is the length scale, and :math:`\nu` is kinematic viscosity.

Drag coefficients are used to describe flow around a particle.
[INCLUDE FIGURE FOR DRAG COEFFICIENT AND REYNOLDS NUMBER]

As an introduction to this drag coefficent diagram, we can compare it to something we've already learned about: the Moody diagram. Drawing parallels between the two will help us understand some important relationships better.

.. _table_Moody_DragCoefficient:
.. csv-table:: Comparison between the Moody diagram and the drag coefficient diagram.
  :header: "Characteristic", "Moody Diagram", "Drag Coefficient Diagram"
  :widths: 10, 10, 10
  :align: center

  "Relationship to Reynolds number", "friction factor," :math:`f`, "drag coefficient, :math:`C_D`
  "Type of head loss", "major losses as shear force on pipe walls", "minor losses as expansion around a particle"
  "Laminar region", :math:`f = \frac{64}{Re}`, :math:`C_D = \frac{24}{Re}`
  "Effect of higher Reynolds numbers on force", at high :math:`Re`, :math:`f` stays about constant but overall head loss increases with velocity :math:`v^2` by :math:`h_L = \frac{fLv^2}{2Dg}`, at high :math:`Re`, :math:`C_D` stays about constant but force of drag increases with velocity :math:`v^2` by :math:`F_{drag} = C_D A_{floc} \rho_{H_2O} \frac{v_t^2}{2}`

The flow around the particle and the Reynolds Number can be described in the laminar, turbulent, or turbulent-boundary regions. In the laminar region, which holds when :math:`Re < 1`, :math:`C_D = \frac{24}{Re}`. This region of laminar flow, represented as the straight line on the log-log plot, where :math:`C_D = \frac{24}{Re}` is referred to as Stokes Law. You'll notice that the line for Stokes Law shown in the figure extends past the laminar region. This was done because it shows that even though Stokes Law is not exactly correct past the turbulent region, it is still a pretty good approximation near :math:`C_D = 1`.

Let's consider the drag coefficient diagram at Reynolds numbers of :math:`10^5`. We notice that there is a "bump" in the plot, in which drag coefficients drop. This is because at really high Reynolds numbers, the boundary layer around the particle became turbulent. This causes the wake behind the particle to be a little smaller, leading to a slight reduction in drag. The drag coefficient decreases, but the total drag force does not necessarily decrease (and likely keeps on increasing).

To understand this phenomenon, think about a golf ball. Golf balls are designed with dimpled surfaces because the dimpled surface forces the transition described above to happen at lower Reynolds numbers. The dimples initiate turbulence in the boundary layer and cause a slight reduction in the drag coefficient. Thus, dimpled golf balls can travel further than smooth ones.

Now, you might think: why aren't more surfaces dimpled? If I want my car to get better mileage, should I dimple its surface to take advantage of the same turbulent boundary layer properties as the golf ball? But before you go and damage some metal, let's think. If a car and golf ball are traveling through air at the same speed, what will be their relative Reynolds numbers? We know that :math:`Re = \frac{v_t D}{\nu}` and :math:`D_{golfball} << D_{car}`. The relative length scales mean that cars have much higher Reynolds numbers than the golf ball. In fact, the Reynolds number for a car is so high that it is already past the point that the boundary layer becomes turbulent. The golf ball needs to be dimpled because its Reynolds numbers are not so large that they will pass the turbulent boundary transition.

Now, let's go back to the realm of water treatment. We care about drag coefficients and terminal velocities because they help describe how flocs will move in water. Flocs tend to exist in the region between 1< :math:`Re` < 10. This region is not perfectly described by Stokes Law, but it is used as an appropriate approximation. We have already solved for the general equation for terminal velocity using the force balance approach. Now, we can solve for a terminal velocity equation specifically in the laminar region.

Plug the drag coefficient and Reynolds numbers for laminar flow into the general terminal velocity equation:

.. math::

  v_t = \sqrt{\frac{4}{3}\frac{gD}{C_D}\frac{(\rho_{floc}-\rho_{H_2O})}{\rho_{H_2O}}}

  C_D = \frac{24}{Re}

  Re = \frac{v_tD}{\nu}

to yield,

.. math::

  v_t = \frac{D^2g}{18\nu}\frac{\rho_{floc} -\rho_{H2O}}{\rho_{H2O}}

Again, we can draw a parallel with the Moody Diagram. The general form of the terminal velocity equation is like the Darcy-Weisbach equation; it is always true. The terminal velocity in the laminar flow region is like the Hagen-Poiselle equation; it is only good for laminar flow. We will use the laminar specific condition because we are working with flocs with low Reynolds numbers.

Our equations for terminal velocity depend on the density of a floc. As discussed in previous sections, we know that there is a specific relationship between the density of a floc and the diameter of a floc because flocs are fractals and as flocs get bigger, their density gets lower. We can account for the size and density relationship by modifying the terminal velocity equation. [[[[MORE INFO NEEDED TO UNDERSTAND WHAT HAS ALREADY BEEN EXPLAINED IN THE FLOCCULATION SECTION]]]]

.. math::

  v_t = \frac{D_0^2g}{18\phi\nu}\frac{\rho_{floc} -\rho_{H2O}}{\rho_{H2O}} \left( \frac{D}{D_0} \right) ^{D_{fractal}-1}

| Where:
| :math:`D_0 =` diameter of clay = 4 :math:`\mu m`
| :math:`D_{fractal} =` 2.3
| :math:`D =` floc diameter (:math:`\mu m`)

The following plot shows the relationship between floc diameter and terminal velocity.

[[[[[[[[[[[INCLUDE FIGURE]]]]]]]]]]]

Three important regions are highlighted in the plot. At small floc diameters, less than 10 :math:`\mu m`, terminal velocity is less that 0.1 :math:`\frac{mm}{s}`. A terminal velocity this low would require extremely large sedimentation tanks for reasonable treatment. Because large sedimentation tanks are costly and unfeasible, we use flocculation to aggregate particles and achieve floc sizes of greater diameters and higher terminal velocities.

For floc diameters around 35 :math:`\mu m`, the terminal velocity is about 1.2 :math:`\frac{mm}{s}`. AguaClara plate settlers are designed to settle out flocs of this size (particles dropping at 1.2 :math:`\frac{mm}{s}`) so the smallest floc that we can capture is 35 :math:`\mu m`. This will be explored in more detail in later sections.

Flocs with large diameters around 200 :math:`\mu m` have a terminal velocity of about 1 :math:`\frac{mm}{s}`. In our sedimentation tanks, which are upflow sedimentation tanks, we have water flowing up at about 1 :math:`\frac{mm}{s}` to capture a 200 :math:`\mu m` floc. These flocs are clearly visible but are small. This is what we design our sedimentation tanks to be able to capture. This will be explored in more detail in later sections.

Our understanding of floc terminal velocity suggests that we can decide the size of the floc that we want our sedimentation tank to capture. If we decide that we want to capture flocs that are 200 :math:`\mu m` or larger, we know that we must design for water flowing at 1 :math:`\frac{mm}{s}`. Alternatively, we know that if we design a reactor in which water flows at 1 :math:`\frac{mm}{s}`, we will only be able to capture flocs that are 200 :math:`\mu m` or larger. This begins our discussion of sedimentation tank design.

Capture Velocity
===============================
Settle capture velocity is defined as the velocity of the slowest settling particle that a sedimentation tank captures reliably. It is a property of the geometry of the sedimentation tank. Because it is a property of geometry, we can use it as an important design tool; because we can control reactor geometry, we can control the sizes of particles that we can settle.

Note: there are a couple of different terms used to describe the sedimentation process. We can say that sedimentation tanks "capture" particles when particles are settled out. We can also say that sedimentation tanks "remove" particles. Both terms refer to the process of particles or floc settling out of suspension in water. If a particle is captured or removed by a sedimentation tank, it means that the particle is stuck in the tank and that water leaving the reactor will have fewer particles in it.

We will develop our definition of settle capture velocity using examples of a horizontal flow and vertical flow sedimentation tanks. It should be noted that there are many idealizations and simplifications made for modeling sedimentation tanks. We assume that water will move through the reactor as expected (in the case of the horizontal flow sedimentation tank, from one end to the other), but we know that there are many more fluids complications than are described here. We assume that everything is moving at the average velocity and there are no turbulence or velocity profiles. For the time being, we will ignore what will happen to particles once they are captured by the sedimentation tank. Our intuition tells us that particles which settle will need to be removed somehow, and that is correct. This will be discussed in later sections. For now, we only care about capturing the particles, and later we will care about what we do with them once they are captured.

Horizontal Flow Sedimentation Tank
----------------------------------

[[[[[[[[[show horizontal flow sedimentation tank]]]]]]]]]

| Where:
| :math:`L =` length [L]
| :math:`W =` width [L]
| :math:`H =` height [L]
| :math:`A_p =` plan view area of the tank [:math:`L^2`]

Let's begin with a few questions that will describe our horizontal flow sedimentation tank shown above. We will assume that 1) water travels uniformly from one end of the tank to the other, and 2) the particle that we are discussing is 35 :math:`\mu m` (which is the size of particle that AguaClara plate settlers can capture).

1) How much time is required for water to pass through the tank?

To determine this value, we can use the given volume and flow rate information by the following relationship:

.. math::
  \theta = \frac{V\llap{---}_{tank}}{Q}

| Where:
| :math:`\theta =` residence time [T]
| :math:`V\llap{---}_{tank} =` volume of the sedimentation tank [:math:`L^3`]
| :math:`Q =` flow rate through the tank [:math:`\frac{L^3}{T}`]

2) In the "worst case scenario", how far must a particle fall to reach the bottom of the tank?

The "worst case scenario" is the condition in which a particle must travel the furthest in order to be successfully captured by the sedimentation tank. We assume that particles are evenly distributed throughout the height and width of the reactor entrance. Therefore, a particle entering at the top of the entrance of the reactor would need to fall a distance of :math:`H` to reach the bottom. Any particle entering from a position lower than the top of the tank would need to fall a distance :math:`< H`. We refer to the "worst case scenario" pathway as the "critical path" of the particle in the sedimentation tank design because this is the case which we must design to treat. The height that the particle must fall is called the "critical height", :math:`H_c`.

3) How fast must the particle fall?

We know that for a particle to fall to the bottom successfully, it needs to fall fast enough that it can reach the bottom before the water that is carrying it leaves the reactor. Water is carrying the particle across the reactor at the horizontal velocity speed, :math:`V_h`. Gravity is causing the particle to settle at its terminal velocity, :math:`V_t`. In order to reach the bottom, that settling velocity needs to be the capture velocity, :math:`V_c`, to ensure that the particle will reach the bottom of the reactor. We can see the critical path of the particle in the following figure.

[[[[[[[[[show horizontal flow sedimentation tank with capture velocity]]]]]]]]]

Capture velocity can be determined by the distance that a particle must travel and the time that the particle has to travel.

.. math::
  V_c = \frac{H}{\theta}

We can make some substitutions into the equation for :math:`V_c` to solve for it in explicit terms of reactor plan view area. We are interested in plan view area because this will indicate the efficiency and cost of an associated reactor.

.. math::
  V_c = \frac{H}{\theta} = \frac{HQ}{V\llap{---}_{tank}} = \frac{Q}{LW} = \frac{Q}{A_p}

  V_c = \frac{Q}{A_p}

Thus, we have capture velocity which is a descriptor of a sedimentation tank. It determines how fast a particle has to settle in order to be reliably captured by a particular sedimentation tank, assuming idealized flow. The capture velocity is not a particle property, but rather a sedimentation tank property.

4) Will any particles that are smaller than 35 :math:`\mu m` be captured in the sedimentation tank?

This question is important because as stated in the beginning of this section, our discussion assumed that the particle in question was 35 :math:`\mu m`. If we design a sedimentation tank to capture particles that are 35 :math:`\mu m`, we also have to understand the impact of our design on particles smaller than 35 :math:`\mu m`.

To answer this question, think about the two extremes of our reactor.

- We could have a small particle entering the reactor at the top, defining the critical path in the same "worst case scenario". This particle would not be successfully captured by the tank because its terminal velocity is less than the capture velocity, meaning that it doesn't have enough time in the reactor to settle.
- We could have a small particle entering the reactor near the bottom, in a "best case scenario". In this case, the particle does not have a large distance to fall because it is already close to the bottom of the tank. Small particles entering the reactor may be able to be caputured by a tank designed for particles 35 :math:`\mu m` or larger, but it depends on the height at which they enter the reactor.

[[[[[[[[[show horizontal flow sedimentation tank with capture velocity for small particles compared to the 35 um condition]]]]]]]]]

Vertical Flow Sedimentation Tank
----------------------------------
We will complete the same exercise for vertical flow sedimentation tanks. In vertical flow sedimentation tanks, water flows up from the bottom of the reactor and exits near the top of the reactor.

[[[[[[[[[show vertical flow sedimentation tank]]]]]]]]]

1) How much time is required for water to pass through the tank?

The answer is the same for the horizontal flow sedimentation tank because this is a property of reactor flow rate and volume.

.. math::
  \theta = \frac{V\llap{---}_{tank}}{Q}

| Where:
| :math:`\theta =` residence time [T]
| :math:`V\llap{---}_{tank} =` volume of the sedimentation tank [:math:`L^3`]
| :math:`Q =` flow rate through the tank [:math:`\frac{L^3}{T}`]

2) How far must a particle fall relative to the fluid to not be carried out the exit?

Note how this question is different from the question we asked for the horizontal flow sedimentation tank. In the horizontal flow sedimentation tank, particles could settle to the bottom of the reactor. We care about particles settling to the bottom because we assume that if particles hit the bottom of the reactor, then they would be captured and would not leave the reactor. Remember, the goal of sedimentation is to remove particles from suspension in water. In the vertical flow sedimentation tank, we also want to remove particles from suspension, but because there is a different geometry, we now are interested in the relative movement of particle to water. If a particle is falling due to the forces of gravity, but also water is pushing up on it, the only way for a particle to remain in the reactor is if it either falls at the same velocity or faster than the water is pushing it.

If a particle is falling at the same velocity that water is moving it, it will be stationary in the reactor. Water flowing through the reactor moves a distance :math:`H` in time :math:`\theta`, which means that a stationary particle must settle the same distance :math:`H` in the same time :math:`\theta`. Therefore, the answer is :math:`H`.

3) How fast must the particle fall (relative to the fluid)?

We determined in the previous question that a particle must fall a distance :math:`H` in time :math:`\theta`. Therefore, we determine the same capture velocity for vertical flow sedimentation tanks as for horizontal flow sedimentation tanks.

.. math::
  V_c = \frac{H}{\theta}

We can the same substitutions to show,

.. math::
  V_c = \frac{H}{\theta} = \frac{HQ}{V\llap{---}_{tank}} = \frac{Q}{LW} = \frac{Q}{A_p}

Again, we find that capture velocity is,

.. math::
  V_c = \frac{Q}{A_p}

It doesn't matter whether water is flowing horizontally or vertically in the tank. What determines the capture velocity is the flow rate and the plan view area of the sedimentation tank.

4) Will any particles that are smaller than 35 :math:`\mu m` be captured in the sedimentation tank?

This question is surprisingly complex because we have to consider what we have learned so far about sedimentation and also recall what we have learned about flocculation.

Let's start with the simple sedimentation approach. We can compare the vertical flow sedimentation tank with the horizontal flow sedimentation tank. In a horizontal flow tank, the capture of particles smaller than the design particle (35 :math:`\mu m`) is possible depending on the height which the particle enters the reactor. In a vertical flow tank, all particles enter the reactor at the same height (which is the bottom of the tank). This means that any particle entering the reactor will need to fall the same distance :math:`H` in time :math:`\theta` relative to the water if it will be captured. If particles smaller than 35 :math:`\mu m` enter the reactor, they will not be captured because they are not able to settle fast enough.

However, we must also consider potential flocculation processes that could occur in the sedimentation tank. A sedimentation tank is still subject to the same laws of fluids as the flocculator, meaning that there will still be shear in the reactor. While it may not be as much shear as that introduced in the flocculator, there are still velocity gradients which mean that there could be some additional flocculation happening in the sedimentation tank. In the flocculator, the main mechanism that led to flocculation was the deformation of fluid which caused particles to collide. In the sedimentation tank, the main mechanism that can lead to flocculation is velocity gradients. Flocculation is provided by an opportunity for collision by differences in relative velocities of particles. Big particles in the sedimentation tank settle out but are still in suspension, and small particles continue to move up through the large particles. There is relative velocity between particles based on their terminal velocities.

Understanding relative velocities is very important to understand how vertical flow sedimentation tanks work. Let's consider an example to develop our understanding of differential sedimentation. Imagine that two people are skydiving; one person is 150 lbs and the other person is 300 lbs. Assume that both people are using the same size parachutes and are jumping out of the same stationary helicopter. If the 150 lb person jumps out first and the 300 lb person jumps out a few moments after, what will happen? The 300 lb person will fall faster than the 150 lb person, causing a collision in the air. In a sedimentation tank, we would describe the collision due to differential sedimentation as flocculation because particles are colliding and growing.

Now that we understand differential settling and the potential for flocculation in a sedimentation tank, let's revisit the original question. Can smaller particles be captured? The answer is that smaller particles can be capture only if they collide with other particles and grow so that they have a terminal velocity that is greater than the capture velocity. This flocculation that happens in the sedimentation tank is an additional mechanism for removing particles.

There are some important differences between horizontal and vertical sedimentation tanks. Many of these points will be discussed later when we learn specifically about the AguaClara design process, but it is important to get introduced to these ideas now. We know that vertical flow tanks require careful attention to the delivery of water in the bottom of the tank and the extraction of water in the top of the tank. We know that vertical and horizontal flow tanks may have different velocities and turbulence capacities due to plan view areas.
[[[[[[[[[[[[[[What is the information on "vertical flow sedimentation tanks and "stagnant water (or ripe for innovation)"]]]]]]]]]]]]]]

Now that we have developed a good understanding of the basic principles of sedimentation, we will transition to a discussion of AguaClara innovations.

***********************************************
AguaClara Design Approach
***********************************************

The AguaClara sedimentation tank is a high-rate vertical flow sedimentation tank that was designed with two goals in mind:

1) to use flow distribution as a primary design constraint and,

2) to ensure easy operation and maintenance.

[[[[[[[[[[[QUESTION ABOUT FLOC BREAKUP]]]]]]]]]]]

We will go through each part of the sedimentation tank to understand how these goals drive AguaClara designs.

***********************************************
Components of an AguaClara Sedimentation Tank
***********************************************

Note: this section should use words and figures to describe the different parts of the tank and what their purpose is, with brief explanation of how they work.

In this section, we will develop a conceptual understanding of the sedimentation tank using figures and images. We will be using a mixture of terminology typically found in water treatment settings and AguaClara-specific terminology. We will discuss the different parts of the sedimentation tank in the sequence that a parcel of water would encounter it, from the beginning of the unit process to the end. The three main sections are 1) how water enters the sedimentation tank, 2) how water moves through the sedimentation tank, and 3) how water leaves the sedimentation tank.

[[[[[[[[[[[[[[INCLUDE PICTURE/VIDEO OF SED TANKS WITH FLOW SHOWN BY ARROWS]]]]]]]]]]]]]]

1) How water enters the sedimentation tank
-------------------------------------------
**Inlet Channel**

After water exits the flocculator, it is ready for sedimentation. In AguaClara plants, there is one flocculator per treatment train. However, depending on the plant flow rate, one plant may have multiple sedimentation units operating in parallel; we call each of these sedimentation units a 'bay' or a 'tank'. Because there may be multiple sedimentation bays, we have to distribute flocculated water between the bays. To do this, we have an **inlet channel**, which receives water from the flocculator and passes it to the sedimentation bays. The channel is long, concrete, and relatively shallow. The objective of the channel is to distribute water and flocs to the sedimentation bays without allowing any settling of flocs in the inlet channel. In the bottom of the channel, there are pipes that lead to the bottom of each sedimentation bay.

Does the water in the inlet channel get evenly distributed between the different bays? If not, which bay will receive the most water? We know from our understanding of fluids and flow distribution that in a pipe (or channel) with multiple orifices that is closed at one end, the distribution of flow is nonuniform along the length of the pipe; it is decelerating. This nonuniformity is due to differences in velocity and pressure in different parts of the pipe. Where else in fluids have we discussed decelerating floc? We have discussed this in flow expansions. And what do we know about pressure in flow expansions? We know that there is higher pressure and slower velocities. At the end of the pipe, there is low velocity and thus high pressure, driving the flow through the orifices at the end. For this same reason, a channel with orifices will have greatest flow delivery to the last orifice. We will revisit this concept later to understand how AguaClara plants attempt to minimize this unequal flow distribution.

[needhelpquestion]

Sedimentation units have multiple bays for a few different reasons. Plants with higher flow rates require more sedimentation bays because the flow through each bay is limited by other design constraints, namely upflow velocity, which will be discussed later. Additionally, it is good to have more than one bay for maintenance purposes; if one bay needs to be cleaned, we want to always have another that can be working. Pipe stubs can be used to plug the entrance hole to a sedimentation bay to shut it down for maintenance.

**Bottom Geometry: Inlet Manifold, Diffusers, and Jet Reverser **

Now, we will focus on a single bay of the sedimentation system. Flocculated water enters a pipe in the bottom of the inlet channel and travels down a few feet. The pipe then has a 90 degree bend and extends along the bottom of the entire length of the sedimentation bay. This section of pipe that distributes water at the bottom of the sedimentation bay is referred to as the **inlet manifold**.

Water exits the inlet manifold through a series of orifices and **diffusers** in the bottom of the pipe. Orifices refer to the holes that are drilled into the underside of the manifold while diffusers are what we call short stubs of pipe that extend down from the orifice, perpendicular to the inlet manifold. The orifices and diffusers point down to the bottom of the sedimentation bay and extend along the length of the pipe at regular intervals to ensure that water is evenly distributed within the bay. The ends of the diffuser tubes are flattened so that they are thin rectangles and when placed side-by-side achieve a line-jet effect. The end of the inlet manifold is capped.

[[[[[[[[[[[NEED TO TALK ABOUT FLOW DISTRIBUTION / MANIFOLDS PPT]]]]]]]]]]]
Recall the discussion about flow distribution in the inlet channel. We know that the sedimentation bay furthest away from the flocculator would receive the most flow from the inlet channel due to fluids principles. For the same reasons, the orifice at the end of the inlet manifold would receive the most flow in the pipe. However, the diffuser system was designed to greatly impact the overall flow distribution in an attempt to make the flow more equal in all parts of the system. To understand how the diffusers work, we will explain a concept referred to as "sedimentation tank as a circuit".

[[[[[[[SED TANK AS A CIRCUIT]]]]]]]

The inlet manifold diffuser system straightens the fluid jets that are exiting the manifold so that they have no horizontal velocity component. This is critical because even a small horizontal velocity causes a large scale circulation that transports flocs directly to the top of the sedimentation tank. Inlet manifolds without flow straightening diffusers are commonly used in vertical flow sedimentation tanks including designs by leading manufacturers.

The diffusers create a line jet that spans the entire length of the sedimentation tank. This line jet enters the bay going down, but we want the water to ultimately flow up to make our vertical flow sedimentation tank. To get the flow to redirect upwards, we use a **jet reverser**, which is half of a pipe that is laid in the bottom of the bay.

You may be wondering, why do we need a jet reverser in the first place? Why don't we just have the diffusers point up to avoid having to change the flow in the first place? The answer has multiple components. First, if the diffusers were to point up, they could clog if anything settles in them. While this is unlikely due to the high velocity of flow exiting the small cross-sectional area diffuser, it is something that is avoided by pointing them down. Second, if flow were just to point directly up, it would not have an opportunity to sufficiently spread in the sedimentation bay, which could lead to "short-circuiting" and poor flow distribution overall. Third, the jet reverser functions as a way to keep flocs suspended by ensuring that anything that settles will be propelled back up from the force of the diffuser jet. The jet reverser and diffuser alignment is not symmetrical; the diffusers are offset from the jet reverser centerline. This is intentionally done to ensure that the diffuser jet never collapses to promote a floc blanket, which will be discussed next. There is a lot of research interest in determining the optimal upflow velocity for floc blankets considering that high velocity is better for resuspension but breaks more flocs. Currently, AguaClara plants use an upflow velocity of 1 mm/s.

[[[[[[[[[[[[PICTURE OF FLAT BOTTOM, CENTERED, and OFFSET JET]]]]]]]]]]]]

As shown above, in a flat bottom geometry, flocs settle in the corners of the tank because there is no direct flow of water to resuspend it. Flocs fall in such a way that the corners of the tank will fill first, with more and more flocs settling until the angle of repose is created. This angle that is occupied by flocs suggests that if we want to avoid having flocs settle, we should fill the sides of the tank in with concrete and create a sloped bottom so that there are no surfaces for settling.

The inlet manifold, diffusers, and jet reverser work with a **sloped bottom geometry** in an AguaClara plant. The bottom geometry allows for smooth flow expansion to the entire plan view area of the bay, and ensures that all flocs that settle are transported to the jet reverser. The diffusers do not touch the bottom of the tank so that flocs on both sides of the diffuser can fall into the jet reverser for resuspension. Thus, there is no accumulation of settled flocs in the main sedimentation basin. Sludge that is allowed to accumulate in the bottom of sedimentation tanks in tropical and temperate climates decomposes anaerobically and generates methane. The methane forms gas bubbles that carry suspended solids to the top of the sedimentation tank and cause a reduction in particle removal efficiency. The AguaClara sedimentation tank bottom geometry prevents sludge accumulation while also ensuring good flow distribution.

So we know that the diffusers, jet reverser, and sloped bottom ensure that no sludge accumulates in the bay by creating a system to resuspend any settled flocs. What are the failure modes for this system? For one, we need to ensure that the jet of water exiting the diffuser is able to maintain its upward direction after the jet reverser. The jet is influenced by the flows that are coming down the sloped sides of the tank. Thus, the jet must have enough momentum to remain upwards even with the momentum from other flows downwards. We can control the momentum of the jet by controlling the cross-sectional area of the diffuser slot. A smaller cross-sectional area will increase the velocity of the jet but the mass is the same because the flow rate for the plant is the same, thus increasing the momentum.

[[[[[[[[PICTURE SHOWING JET COLLAPSE]]]]]]]]

[[[[[[[[[[[[[[[[MORE INFO ABOUT SHORT CIRCUITING]]]]]]]]]]]]]]]]

[[[[[[[[[[[[[[[[[[[[Don't worry about floc breakup.]]]]]]]]]]]]
  Avoid flow circulations
[needhelpquestion]

2) How water moves through the sedimentation tank
-------------------------------------------------
**Floc Blanket and Floc Hopper**

The line jet from the diffusers enters the jet reverser to force flow up through the sedimentation bay. The vertical upward jet momentum is used to resuspend flocs that have settled to the bottom of the sedimentation tank. The resuspended flocs form a fluidized bed which is called a **floc blanket**. The bed is fluidized because flocs are kept in suspension by the upflowing water.

For a floc blanket to form, a sedimentation system requires that all flocs be returned to the bottom of the sedimentation tank and requires that all settled flocs be resuspended by incoming water. As will be discussed soon, plate settlers are used to return flocs to the bottom of the bay, while the jet reverser and sloped bottom geometry allow for floc resuspension. Any surface with a horizontal component in a sedimentation tank must be sloped to allow settled flocs to return to the resuspension zone. A flat bottom geometry does not allow for the formation of a floc blanket, as discussed previously.

Floc blankets improve the performance of a sedimentation tank and reduces settled water turbidity by a factor of 10 (Garland et al., 2017) for multiple reasons.

- Additional collision potential. The high concentration of particles, with a suspended solids concentrations of approximately 1-5 g/L, leads to an increase in collisions and particle aggregation. As discussed for vertical flow sedimentation tanks, flocculation can occur in a floc blanket due to shear from suspended flocs which are colliding and growing. Fluidized flocs provide a collision potential of a few thousand. This collision potential is small compared to the collision potential from the flocculator. So how does a small :math:`G \theta` cause a large reduction in turbidity? The answer may be that the lower :math:`G` value provides an opportunity for all flocs to grow larger without floc breakup. The high concentration of flocs provides many opportunities for clay particles to collide with big flocs, but it is not clear if or when those collisions are successful. Which flocs are active and which flocs are inactive in the floc blanket?

[[[[[[[[[[[[[[[[[[[[[[[[[rhetorical or no?]]]]]]]]]]]]]]]]]]]]]]]]]

[[[[[[[[[[[[FILTER VS FLOCCULATOR QUESTION]]]]]]]]]]]]
We just explained that flocs in the floc blanket cause shear and energy gradients, thus leading to collisions and growing flocs. This explanation suggests that the floc blanket acts like a flocculator. However, there is another proposed model for floc blanket operation in which the floc blanket acts like a filter. Although you haven't necessarily learned about filters yet, all you need to know for now is that sand in a sand filter creates head loss. The sand is essentially inert and creates shear but isn't "colliding" with particles going past it. So the two models proposed for floc blankets are the flocculator or filter model; which is it? Are floc blankets like flocculators or filters, and how can we find out? We can learn more by delving into the discussion about relative :math:`G \theta` values between the flocculator and the floc blanket. Through laboratory testing, we know that flocculators have :math:`G \theta` values on the order of 20,000 and the floc blanket have on the order of 4,000.

[[[needhelpquestion what I have written seems wrong]]]

If the filter model of floc blankets was correct and the flocs were just taking up space and causing head loss, we would expect a 24,000 :math:`G \theta` flocculator to function the same as a 20,000 :math:`G \theta` flocculator coupled with a 4,000 :math:`G \theta` floc blanket. However, if we just changed our flocculator to be closer to 24,000 :math:`G \theta`, we would have not gotten the impressive removal efficiency that the floc blankets demonstrate. So, we must assume that large flocs in the floc blanket are involved in some collisions with the smaller flocs going through it. However, we still do not have a model set of equations to describe floc blanket performance.

- creating a uniform vertical velocity of water entering the plate settlers.

- The floc blanket transports excess flocs to the floc hopper for final removal through a small drain valve.  The **floc hopper** is a "weir" that provides an opportunity for floc consolidation. The floc hopper controls the depth of the floc blanket because as the floc blanket grows, it will eventually reach the top of the floc hopper. Because flocs are more dense than water, the flocs "spill" over the edge of the floc hopper which allows the floc blanket to stay a constant height while sludge accumulates and consolidates in the floc hopper. Floc blanket flow into the floc hopper is a function of the mass flux of particles into the sedimentation tank. We need to characterize the consolidation rate of the flocs to optimize the floc hopper design. The ideal depth of the floc blanket has not yet been determined.

The floc hopper allows for a self-cleaning sedimentation tank. By gravity, flocs are sent over to a floc hopper. This means that operators only have to clean the sedimentation tank once every three to six months because there is no stagnant accumulation of anoxic sludge. When operators do clean the sedimentation tank, they are primarily cleaning plate settlers. Under normal operation, operators can open the floc hopper drain valve whenever they want to easily drain the sludge. Without the floc blanket transport system, other methods would be required to remove accumulated sludge in the bay. Mechanical sludge removal systems are common alternatives but are well known to be costly to install and a challenge to maintain.

A benefit of the floc blanket is that flocs can be removed without mechanical assistance, but why do we need the floc hopper at all? Why can't we just install drain holes in the bottom of the sedimentation tank so that any accumulated sludge is removed? This is a question that plagued AguaClara in its early years. At first, before we were able to successfully build and operate a floc blanket, we had sludge accumulate in the bottom of the sedimentation bay. Therefore, we needed to remove the sludge with drain holes at the bottom. However, to have those drain holes where the sludge was accumulating in the tank, designers made a flat bottom tank. But as we now know, the flat bottom tank is part of the reason that there wasn't any floc blanket forming. As soon as we realized that we could grow a floc blanket with a sloped bottom tank and a jet reverser, we could not use drain holes in the bottom of the tank. Why? Because in the bottom of tanks with floc blankets created by jet reversers, there is no settling. Drain holes at the bottom of a sloped tank would be draining a combination of flocculated water and floc blanket water, neither of which are consolidated thus making the draining ineffective and inefficient. A benefit of the floc hopper is that there is no upflow velocity, which means that the sludge is able to settle and become more dense, allowing for less water waste from draining sludge.

After flowing through the floc blanket, flocs reach the **plate settlers**. Plate settlers are sloped surfaces that provide additional settling area for flocs, thereby increasing the effective settling area of the sedimentation unit without increasing the plan view area. In our discussion of horizontal and vertical flow sedimentation tanks, the important design parameter was capture velocity which was set by flow rate and plan view area of the sedimentation tank. With the introduction of plate settlers, the important design parameter changes. What matters is not just the plan view area of the sedimentation tank, but instead the projected area of all of the surfaces where particles can settle out, which we call the effective settling area. Without plate settlers, the only way we could improve performance and impact the capture velocity was by increasing the plan view area of the sedimentation tank. Now that we know about plate settlers, we can improve performance by just adding plate settlers. This allows for greater treatment efficiency at low cost because we can maintain a small footprint. Note that plate settlers can also be referred to as lamella settlers, or lamellas.

[[[[need information about laminar flow between plates]]]]

[[[[include figure for plate settler and labeled geometry]]]]

The first thing that we will discuss is how flocs can settle on plates. To understand this, we will ask a few questions.

1) What is the critical path?

We need particles to settle on the bottom plate for it to be effectively captured. Thus, the critical path can be shown by a floc that enters the plate settlers closest to the upper plate, because it will have the greatest distance to settle.

2) How far must the particle settle to reach the lower plate?

Let's make a simplification and assume that water is flowing with uniform velocity between the plates, represented by a "top hat" velocity profile. This is a significant assumption, but it is used to help us understand the critical path. As the fluid is carrying the floc between the inclined plates while gravity is pulling the floc down. Therefore, particle must fall the vertical distance between the plates, which is the critical height :math:`H_c`. The plates are positioned at an angle, :math:`\alpha`, to ensure that settling flocs slide down to the floc blanket. The critical height :math:`H_c` can be expressed in terms of plate settler length, :math:`L`, and plate settler angle, :math:`\alpha`, by :math:`H_c=L sin\alpha`.

3) What is the net vertical velocity of a floc between the plate settlers?

The fluid carries the floc between the plate settlers while gravity pulls the floc down. The velocity through the plate settlers has both a horizontal component :math:`V_{P,H}` and vertical component :math:`V_{P,V}`, with a resultant force we call :math:`V_{P,\alpha}`. This means that the net vertical velocity :math:`V_{P,net}` is the vertical component of flow minus the settling velocity of the floc. Recall our previous discussion of terminal velocity and capture velocity; in this case, because we are designing a plate settler specifically to capture the critical particle, the terminal velocity equals the capture velocity. The terminal velocity is a function of the particle which we are setting as the smallest particle that we want to reliably capture and the capture velocity is a function of the reactor geometry which we are designing to capture the critical particle. Thus, :math:`V_{P,net}=V_{P,V}-V_{c}`.

[[[[[need more explanation here help about why capture and terminal are the same here]]]]]

[[[[include figure showing the relevant velocities in the plate settler, including resultant particle velocity]]]]

Now that we have established how flocs settle on the plate, we need to discuss how flocs will act once they are on the plates. We want particles and flocs that settle to agglomerate and slide down the plate settlers to be returned to the floc blanket. However, there are some constraints that we must consider.

Let's start with a basic question. If we know that adding plate settlers improve performance, why don't we just keep adding more and more plate settlers to our system? Why would we want to put plates closer together? This could be for a few reasons. We know that more plates means more effective settling area which means that we could remover more particles and make our tank smaller to save money and limit the use of concrete.

The Ten State Standard's include that plate settlers should have separations of two inches, with very long plate settlers, which means very deep tanks. Sedimentation tanks are usually 4 meters deep, maybe because filters are also deep. This is a result of the engineering context rather than the basic design principles. The Ten State Standards are primarily based off the modification of existing sedimentation tanks which were usually built deep and then plate settlers were added. This means that there wasn't added incentive to optimize the entire plate settler and tank process because the tanks were already built. However, AguaClara designs are made to use all of the AguaClara innovations in a green field, meaning that we are incentivized to optimize every part of this design process [[[weird way to say this...reword]]].

This means that we can change the depth and plan view area of the tank for optimal plate settler efficiency. We want to have the smallest and shallowest tanks possible for low cost and ease of construction. We know that in the plate settler design, there is a dimensionless parameter of plate spacing to length, :math:`\frac{S}{L}`. The ratio is close to constant, which means that if we double the length of the plate settler, we can double the spacing between the plate settler and get the same performance as when we started. Conversely, if we halve the distance between the plate settlers, we can halve the length of the plate settlers. But how far can we push this? Can we make really compact plate settlers?

What we really want to know is: what is the connection of spacing between plate settlers and performance?

[[[[[[show graphic of large spacing and small spacing with floc rollup]]]]]]

When we were discussed how plate settlers promote settling, we assumed a uniform velocity profile between the plates. However, we know from fluid mechanics and boundary layer rules that in reality, there is a nonuniform velocity profile. The profile resembles a parabola between the plates; the shape of the parabola is affected by the distance between the plates.

There are some cases in which the plates are so close that even if flocs settle on the plate, they do not slide down. This is called **floc rollup**. Consider the following questions:

1) Why do flocs roll up?

It is a force balance! There is a force of gravity pulling the particle down, balanced with the force that the fluid flow exerts through drag related to viscosity. But why does it matter if plates are close together or flow up? The average velocity between plates are the same for any spacing. However, when plates are closer together the velocity profile is much steeper. Compared with  plates with greater spacing, the closer plates cause there to be a higher velocity closer to the surface of the plate. This means that flocs between closely spaced plates will see a greater velocity, which will impact the force balance. The derivation of the force balance is done in the next chapter. The velocity that the flocs slide down the plate is called :math:`V_{slide}`.

[[[[force balance diagram]]]]

2) How would you define the transition between floc rollup and slide down? What would describe the case for a floc that is stationary on the plate settler (not rolling up or sliding down?)

The transition is defined as when the gravitational forces and the fluid drag forces match.

3) Will little flocs or big flocs be most vulnerable to floc rollup?

This is a very complicated question. We would expect big flocs to slide down because they are heavier and have a greater gravitational force. However, bigger flocs also have a greater drag force and are out further into the flow. They will feel a higher velocity than smaller flocs. This means that it is not clear, and we will determine  this mathematically later.

4) Will large or small spacing between plates cause more floc rollup?

As we have already suggested, small spacing between plates will cause more floc rollup due to the resulting velocity profile between the plates.

So what does this mean for plate settler spacing? Let's review some results from lab experiments. The following graph shows minimum plate settler spacing (mm) as a function of floc terminal velocity (mm/s). Some important things to note are that AguaClara plate settlers are designed for a capture velocity of 0.12 mm/s (recall that this capture velocity means that we want to capture flocs that are settling at 0.12 mm/s and faster) [[[[why? where does this come from?]]]] Reading the graph, we can see the line for 1 mm/s upflow velocity, :math:`V_{P,V}`, at 0.12 mm/s requires a minimum plate spacing of about about 2.5 mm to prevent floc rollup. Now, let's interpret this result. If the upflow velocity increases, we see that the required spacing between plates increases. The results from these experiments will help us answer one of our previous questions: will little flocs or big flocs be most vulnerable to floc rollup? From the graph, we know that it is the little ones. Smaller floc terminal velocities indicate smaller particles, and the graph shows that smaller floc terminal velocities require larger distances of floc spacing to not roll up. The bigger the flocs, the smaller the spacing required to not roll up. Little flocs are harder to capture as you move plates closer together. Little flocs roll up first.

[[[[plot of minimum plate spacing, function of floc Vt]]]]

This analysis suggests that the Standard design is nowhere near the constraint of floc roll up (recall that standard design has separations of 5 cm). AguaClara plate settlers are currently using separations of 2.5 cm, which is also far above the constraint of floc roll up. So if we determined that the minimum spacing for floc roll up constraints is closer to 2.5 mm, why are we using 2.5 cm? The answer is related to our initial assumptions about the floc composition and terminal velocity. When we calculated terminal velocities, we did so for clay-based flocs. But in reality, there are many kinds of flocs formed in water treatment plants. Dissolved organic matter also interacts with coagulant to form flocs that we assume are much less dense than clay based flocs. We don't currently have a good model to understand how these organic-matter flocs. We don't know what the terminal velocity of flocs is if they are made of organics, coagulant, and clay. Even without knowing specifics, how will minimum plate spacing be impacted by flocs that are formed from organic matter instead of clay? If we use dissolved organic matter, the equation predicts that spacing will change primarily due to the big difference in floc density. As floc density decreases, as we expect for organic matter, minimum spacing increases. However, we don't yet know what that spacing is or where the boundary is because we don't know the properties of the humic acid-coagulant flocs. This prompts us to opt for safety factors, so we have chosen a plate settler spacing of 2.5 cm. There is room to learn more here.

Why does the plate settling distance matter so much? How much does it impact the rest of the sedimentation tank and its design?


[[[[sed tank as a circuit, include plate settlers in the discussion now]]]]

3) How water leaves the sedimentation tank
-------------------------------------------------

- Submerged outlet manifold
- Outlet channel to filter
- overflow channel

The hydraulic self cleaning sedimentation tank with a high performing floc blanket, zero sludge accumulation, and with no moving parts outperforms conventional sedimentation tanks on capital cost, performance, and maintenance costs.

***********************************************
Design of an AguaClara Sedimentation Tank
***********************************************
In the next section, we will develop the mathematical models that help us explain the design.

Note: this section will build off of the conceptual understanding established in the previous section and will explain how the tank works with derivations and mathematical models.

How do we actually design a sedimentation tank? What are the parameters that actually matter?

- Inlet and outlet channels
  - Exit weir height
  - Drain for flocculated water (waste)
  - Pipe stubs to block certain tanks when they need to be taken offline

- Inlet manifold
- Diffusers
  - Width,
- Jet reverser
- Floc blankets
  Neglecting the addition of coagulant, the density of the floc blanket is approximately equal to the mass of clay and water divided by the volume of the sedimentation bay.
  gtheta? calculate velocity, head loss
- Floc hopper
- Plate settlers
  - Capture area
  - Lost triangle
  - Design criteria:
    - Upflow velocity
      - Set by floc blanket velocity requirement

    - Capture velocity
      - Target turbidity
      - Particle size distribution after floc blanket

    - Plate angle
      - Self cleaning

    - Plate spacing
      - Clogging
      - Floc roll-up
        - Slide capture velocity

    - Plate length
      - Dependent on other parameters

- Submerged outlet manifold
- overflow channels
- drain pipe

*******************************************************
Sedimentation Challenges, Confusions, and Failure Modes
*******************************************************

- Flow circulations
- Floc Volcanoes
- NOM impact on floc density
- Role of floc blanket
