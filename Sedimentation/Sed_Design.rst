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
As flocs settle in water, they will fall at a speed dictated by the weight of the floc, the buoyancy of the floc, and drag from the water. These three forces - the gravitational weight force, the buoyant force, and the drag force - dictate the speed at which a floc falls and are detailed in the following free body diagram. We care about determining the speed at which flocs will fall because knowing this information will help inform our sedimentation reactor design criteria.

.. _figure_terminal_velocity_FBD:
.. figure:: Images/terminal_velocity_FBD.png
    :height: 100px
    :align: center
    :alt: Buyouant force, drag force, and gravitational force shown for floc free body diagram.

    Free body diagram of a floc in water.

To determine the force balance on a falling floc, consider:

.. math::

  \sum F = m a

At terminal velocity, the floc has been falling for a long period of time so there is no acceleration and the right side of the equation simplifies to zero.

:math:`F_{drag} + F_{buoyant} - W_{floc} = 0`

Each of the force components can be determined by:

.. math::

  F_{drag} = C_D A_{floc} \rho_{H_2O} \frac{v_t^2}{2}

  F_{buoyant} = \rlap{-}V_{floc} \rho_{H_2O} g

  W_{floc} = \rlap{-} V_{floc} \rho_{floc} g

| Where:
| :math:`\rlap{-}V_{floc} =` floc particle volume
| :math:`A_{floc} =` particle projected cross-sectional area
| :math:`\rho_{floc} =` particle density
| :math:`\rho_{H_2O} =` water density
| :math:`g =` acceleration due to gravity
| :math:`C_D =` drag coefficient
| :math:`v_t=` particle terminal velocity
| :math:`D=` particle diameter

Plugging into the original force balance,

.. math::

  [C_D A_{floc} \rho_{H_2O} \frac{v_t^2}{2}]+[\rlap{-}V_{floc} \rho_{H_2O} g]-[\rlap{-}V_{floc} \rho_{floc} g] =0

Solving for terminal velocity, :math:`v_t`, provides

.. math::

  v_t = \sqrt{\frac{4}{3}\frac{gD}{C_D}\frac{(\rho_{floc}-\rho_{H_2O})}{\rho_{H_2O}}}

Terminal velocity is a function of fluid density, floc density, gravity, particle diameter, and the drag coefficient. To calculate velocity, all of those inputs must be determined.

The first component that we will focus on is the drag coefficient, :math:`C_D`. The drag coefficient is function of Reynolds Number, :math:`Re`, and the characteristic flow around a particle. As a reminder, :math:`Re = \frac{v_t D}{\nu}` where :math:`v_t` is the velocity of the fluid, :math:`D` is the length scale, and :math:`\nu` is kinematic viscosity.

Drag coefficients are used to describe flow around a particle.

.. _figure_drag_coeff_Re_base:
.. figure:: Images/drag_coeff_Re_base.png
    :height: 100px
    :align: center
    :alt: Drag coefficient as a function of Reynolds number.

    Drag coefficient as a function of Reynolds number.

As an introduction to this drag coefficent diagram, we can compare it to something we've already learned about: the Moody diagram. Drawing parallels between the two will help us understand some important relationships better.

.. _table_Moody_DragCoefficient:

Below is a table to compare the significance of the Moody diagram and the Drag Coefficient diagram.

+--------------------------------+-----------------------------------+-------------------------------------------------------------+
| Characteristic                 | Moody Diagram                     | Drag Coefficient Diagram                                    |
+================================+===================================+=============================================================+
| Relationship to                | friction factor,                  | drag coefficient,                                           |
| Reynolds number                | :math:`f`                         | :math:`C_D`                                                 |
+--------------------------------+-----------------------------------+-------------------------------------------------------------+
| Type of head loss              | major losses as                   | minor losses as                                             |
|                                | shear force on                    | expansion around a                                          |
|                                | pipe walls                        | particle                                                    |
+--------------------------------+-----------------------------------+-------------------------------------------------------------+
| Laminar region                 | :math:`f = \frac{64}{Re}`         |:math:`C_D = \frac{24}{Re}`                                  |
+--------------------------------+-----------------------------------+-------------------------------------------------------------+
| High Reynolds number           | :math:`f` remains constant        | :math:`C_D` remains constant                                |
| (:math:`f`, :math:`C_D`)       |                                   |                                                             |
+--------------------------------+-----------------------------------+-------------------------------------------------------------+
| High Reynolds number           | head loss increases by velocity in| force of drag increases by velocity in                      |
| (:math:`h_L`, :math:`F_{drag}`)|  :math:`h_L = \frac{fLv^2}{2Dg}`  |  :math:`F_{drag} = C_D A_{floc} \rho_{H_2O} \frac{v_t^2}{2}`|
+--------------------------------+-----------------------------------+-------------------------------------------------------------+





The flow around the particle and the Reynolds Number can be described in the laminar, turbulent, or turbulent-boundary regions. In the laminar region, which holds when :math:`Re < 1`, :math:`C_D = \frac{24}{Re}`. This region of laminar flow, represented as the straight line on the log-log plot, where :math:`C_D = \frac{24}{Re}` is referred to as Stokes Law. You'll notice that the line for Stokes Law shown in the figure extends past the laminar region. This was done because it highlights that even though Stokes Law is not exactly correct past the turbulent region, it is still a pretty good approximation near :math:`C_D = 1`.

.. _figure_drag_coeff_Re_full:
.. figure:: Images/drag_coeff_Re_full.png
    :height: 100px
    :align: center
    :alt: Drag coefficient as a function of Reynolds number.

    Drag coefficient as a function of Reynolds number.

Let's consider the drag coefficient diagram at Reynolds numbers of :math:`10^5`. We notice that there is a "bump" in the plot, in which drag coefficients drop. This is because at really high Reynolds numbers, the boundary layer around the particle became turbulent. This causes the wake behind the particle to be a little smaller, leading to a slight reduction in drag. The drag coefficient decreases, but the total drag force does not necessarily decrease (and likely keeps on increasing).

To understand this phenomenon, think about a golf ball. Golf balls are designed with dimpled surfaces because the dimpled surface forces the transition described above to happen at lower Reynolds numbers. The dimples initiate turbulence in the boundary layer and cause a slight reduction in the drag coefficient. Thus, dimpled golf balls can travel further than smooth ones.

You might think: why aren't more surfaces dimpled? If I want my car to get better mileage, should I dimple its surface to take advantage of the same turbulent boundary layer properties as the golf ball? But before you go and damage some metal, let's think. If a car and golf ball are traveling through air at the same speed, what will be their relative Reynolds numbers? We know that :math:`Re = \frac{v_t D}{\nu}` and :math:`D_{golfball} << D_{car}`. The relative length scales mean that cars have much higher Reynolds numbers than the golf ball. In fact, the Reynolds number for a car is so high that it is already past the point that the boundary layer becomes turbulent. The golf ball needs to be dimpled because its Reynolds numbers are not so large that they will pass the turbulent boundary transition.

Let's go back to the realm of water treatment. We care about drag coefficients and terminal velocities because they help describe how flocs will move in water. Flocs tend to exist in the region between 1< :math:`Re` < 10. This region is not perfectly described by Stokes Law, but it is used as an appropriate approximation. We have already solved for the general equation for terminal velocity using the force balance approach. Now, we can solve for a terminal velocity equation specifically in the laminar region.

Plug the drag coefficient and Reynolds numbers for laminar flow into the general terminal velocity equation:

.. math::

  v_t = \sqrt{\frac{4}{3}\frac{gD}{C_D}\frac{(\rho_{floc}-\rho_{H_2O})}{\rho_{H_2O}}}

  C_D = \frac{24}{Re}

  Re = \frac{v_tD}{\nu}

to yield,

.. math::

  v_t = \frac{D^2g}{18\nu}\frac{\rho_{floc} -\rho_{H2O}}{\rho_{H2O}}

Again, we can draw a parallel with the Moody Diagram. The general form of the terminal velocity equation is like the Darcy-Weisbach equation; it is always true. The terminal velocity in the laminar flow region is like the Hagen-Poiselle equation; it is only good for laminar flow. We will use the laminar specific condition because we are working with flocs with low Reynolds numbers.

Our equations for terminal velocity depend on the density of a floc. As discussed in previous sections, we know that there is a specific relationship between the density of a floc and the diameter of a floc because flocs are fractals and as flocs get bigger, their density gets lower. We can account for the size and density relationship by modifying the terminal velocity equation. [[MORE INFO NEEDED TO UNDERSTAND WHAT HAS ALREADY BEEN EXPLAINED IN THE FLOCCULATION SECTION]]

.. math::

  v_t = \frac{D_0^2g}{18\phi\nu}\frac{\rho_{floc} -\rho_{H2O}}{\rho_{H2O}} \left( \frac{D}{D_0} \right) ^{D_{fractal}-1}

| Where:
| :math:`D_0 =` diameter of clay = 4 :math:`\mu m`
| :math:`D_{fractal} =` 2.3
| :math:`D =` floc diameter (:math:`\mu m`)

The following plot shows the relationship between floc diameter and terminal velocity.

.. _figure_terminal_velocity_floc_diam:
.. figure:: Images/terminal_velocity_floc_diam.png
    :height: 100px
    :align: center
    :alt: Terminal velocity as a function of floc diameter, taking into account the changing density of flocs.

    Terminal velocity as a function of floc diameter, taking into account the changing density of flocs.

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

.. _figure_horizontal_flow_tank_base:
.. figure:: Images/horizontal_flow_tank_base.png
    :height: 100px
    :align: center
    :alt: Horizontal flow sedimentation tank.

    Horizontal flow sedimentation tank.

| Where:
| :math:`L =` length [L]
| :math:`W =` width [L]
| :math:`H =` height [L]
| :math:`A_p =` plan view area of the tank [:math:`L^2`]

Let's begin with a few questions that will describe our horizontal flow sedimentation tank shown above. We will assume that 1) water travels uniformly from one end of the tank to the other, and 2) the particle that we are discussing is 35 :math:`\mu m` (which is the size of particle that AguaClara plate settlers can capture).

1) How much time is required for water to pass through the tank?

To determine this value, we can use the given volume and flow rate information by the following relationship:

.. math::
  \theta = \frac{\rlap{-}V_{tank}}{Q}

| Where:
| :math:`\theta =` residence time [T]
| :math:`\rlap{-}V_{tank} =` volume of the sedimentation tank [:math:`L^3`]
| :math:`Q =` flow rate through the tank [:math:`\frac{L^3}{T}`]

2) In the "worst case scenario", how far must a particle fall to reach the bottom of the tank?

The "worst case scenario" is the condition in which a particle must travel the furthest in order to be successfully captured by the sedimentation tank. We assume that particles are evenly distributed throughout the height and width of the reactor entrance. Therefore, a particle entering at the top of the entrance of the reactor would need to fall a distance of :math:`H` to reach the bottom. Any particle entering from a position lower than the top of the tank would need to fall a distance :math:`< H`. We refer to the "worst case scenario" pathway as the "critical path" of the particle in the sedimentation tank design because this is the case which we must design to treat. The height that the particle must fall is called the "critical height", :math:`H_c`.

3) How fast must the particle fall?

We know that for a particle to fall to the bottom successfully, it needs to fall fast enough that it can reach the bottom before the water that is carrying it leaves the reactor. Water is carrying the particle across the reactor at the horizontal velocity speed, :math:`v_H`. Gravity is causing the particle to settle at its terminal velocity, :math:`v_t`. In order to reach the bottom, that settling velocity needs to be the capture velocity, :math:`v_c`, to ensure that the particle will reach the bottom of the reactor. We can see the critical path of the particle in the following figure.

.. _figure_horizontal_flow_tank_capture:
.. figure:: Images/horizontal_flow_tank_capture.png
    :height: 100px
    :align: center
    :alt: Horizontal flow sedimentation tank with capture velocity.

    Horizontal flow sedimentation tank with capture velocity.

Capture velocity can be determined by the distance that a particle must travel and the time that the particle has to travel.

.. math::
  v_c = \frac{H}{\theta}

We can make some substitutions into the equation for :math:`v_c` to solve for it in explicit terms of reactor plan view area. We are interested in plan view area because this will indicate the efficiency and cost of an associated reactor.

.. math::
  v_c = \frac{H}{\theta} = \frac{HQ}{\rlap{-}V_{tank}} = \frac{Q}{LW} = \frac{Q}{A_p}

  v_c = \frac{Q}{A_p}

Thus, we have capture velocity which is a descriptor of a sedimentation tank. It determines how fast a particle has to settle in order to be reliably captured by a particular sedimentation tank, assuming idealized flow. The capture velocity is not a particle property, but rather a sedimentation tank property.

4) Will any particles that are smaller than 35 :math:`\mu m` be captured in the sedimentation tank?

This question is important because as stated in the beginning of this section, our discussion assumed that the particle in question was 35 :math:`\mu m`. If we design a sedimentation tank to capture particles that are 35 :math:`\mu m`, we also have to understand the impact of our design on particles smaller than 35 :math:`\mu m`.

To answer this question, think about the two extremes of our reactor.

- We could have a small particle entering the reactor at the top, defining the critical path in the same "worst case scenario". This particle would not be successfully captured by the tank because its terminal velocity is less than the capture velocity, meaning that it doesn't have enough time in the reactor to settle.
- We could have a small particle entering the reactor near the bottom, in a "best case scenario". In this case, the particle does not have a large distance to fall because it is already close to the bottom of the tank. Small particles entering the reactor may be able to be caputured by a tank designed for particles 35 :math:`\mu m` or larger, but it depends on the height at which they enter the reactor.

.. _figure_horizontal_flow_tank_small_capture:
.. figure:: Images/horizontal_flow_tank_small_capture.png
    :height: 100px
    :align: center
    :alt: Horizontal flow sedimentation tank with critical path and small particle.

    Horizontal flow sedimentation tank with critical path and small particle.

Vertical Flow Sedimentation Tank
----------------------------------
We will complete the same exercise for vertical flow sedimentation tanks. In vertical flow sedimentation tanks, water flows up from the bottom of the reactor and exits near the top of the reactor.

.. _figure_vertical_flow_tank_base:
.. figure:: Images/vertical_flow_tank_base.png
    :height: 100px
    :align: center
    :alt: Vertical flow sedimentation tank.

    Vertical flow sedimentation tank.

1) How much time is required for water to pass through the tank?

The answer is the same for the horizontal flow sedimentation tank because this is a property of reactor flow rate and volume.

.. math::
  \theta = \frac{\rlap{-}V_{tank}}{Q}

| Where:
| :math:`\theta =` residence time [T]
| :math:`\rlap{-}V_{tank} =` volume of the sedimentation tank [:math:`L^3`]
| :math:`Q =` flow rate through the tank [:math:`\frac{L^3}{T}`]

2) How far must a particle fall relative to the fluid to not be carried out the exit?

Note how this question is different from the question we asked for the horizontal flow sedimentation tank. In the horizontal flow sedimentation tank, particles could settle to the bottom of the reactor. We care about particles settling to the bottom because we assume that if particles hit the bottom of the reactor, then they would be captured and would not leave the reactor. Remember, the goal of sedimentation is to remove particles from suspension in water. In the vertical flow sedimentation tank, we also want to remove particles from suspension, but because there is a different geometry, we are now interested in the relative movement of particle to water. If a particle is falling due to the forces of gravity, but also water is pushing up on it, the only way for a particle to remain in the reactor is if it either falls at the same velocity or faster than the water is pushing it.

If a particle is falling at the same velocity that water is moving it, it will be stationary in the reactor. Water flowing through the reactor moves a distance :math:`H` in time :math:`\theta`, which means that a stationary particle must settle the same distance :math:`H` in the same time :math:`\theta`. Therefore, the answer is :math:`H`.

3) How fast must the particle fall (relative to the fluid)?

We determined in the previous question that a particle must fall a distance :math:`H` in time :math:`\theta`. Therefore, we determine the same capture velocity for vertical flow sedimentation tanks as for horizontal flow sedimentation tanks.

.. math::
  v_c = \frac{H}{\theta}

We can the same substitutions to show,

.. math::
  v_c = \frac{H}{\theta} = \frac{HQ}{\rlap{-}V_{tank}} = \frac{Q}{LW} = \frac{Q}{A_p}

Again, we find that capture velocity is,

.. math::
  v_c = \frac{Q}{A_p}

It doesn't matter whether water is flowing horizontally or vertically in the tank. What determines the capture velocity is the flow rate and the plan view area of the sedimentation tank.

4) Will any particles that are smaller than 35 :math:`\mu m` be captured in the sedimentation tank?

This question is surprisingly complex because we have to consider what we have learned so far about sedimentation and also recall what we have learned about flocculation.

Let's start with the simple sedimentation approach. We can compare the vertical flow sedimentation tank with the horizontal flow sedimentation tank. In a horizontal flow tank, the capture of particles smaller than the design particle (35 :math:`\mu m`) is possible depending on the height which the particle enters the reactor. In a vertical flow tank, all particles enter the reactor at the same height (which is the bottom of the tank). This means that any particle entering the reactor will need to fall the same distance :math:`H` in time :math:`\theta` relative to the water if it will be captured. If particles smaller than 35 :math:`\mu m` enter the reactor, they will not be captured because they are not able to settle fast enough.

However, we must also consider potential flocculation processes that could occur in the sedimentation tank. A sedimentation tank is still subject to the same laws of fluids as the flocculator, meaning that there will still be shear in the reactor. While it may not be as much shear as that introduced in the flocculator, there are still velocity gradients which mean that there could be some additional flocculation happening in the sedimentation tank. In the flocculator, the main mechanism that led to flocculation was the deformation of fluid which caused particles to collide. In the sedimentation tank, the main mechanism that can lead to flocculation is velocity gradients. Flocculation is provided by an opportunity for collision by differences in relative velocities of particles. Big particles in the sedimentation tank settle out but are still in suspension, and small particles continue to move up through the large particles. There is relative velocity between particles based on their terminal velocities.

Understanding relative velocities is very important to understand how vertical flow sedimentation tanks work. Let's consider an example to develop our understanding of differential sedimentation. Imagine that two people are skydiving; one person is 150 lbs and the other person is 300 lbs. Assume that both people are using the same size parachutes and are jumping out of the same stationary helicopter. If the 150 lb person jumps out first and the 300 lb person jumps out a few moments after, what will happen? The 300 lb person will fall faster than the 150 lb person, causing a collision in the air. In a sedimentation tank, we would describe the collision due to differential sedimentation as flocculation because particles are colliding and growing.

Now that we understand differential settling and the potential for flocculation in a sedimentation tank, let's revisit the original question. Can smaller particles be captured? The answer is that smaller particles can be captured only if they collide with other particles and grow so that they have a terminal velocity that is greater than the capture velocity. This flocculation that happens in the sedimentation tank is an additional mechanism for removing particles.

There are some important differences between horizontal and vertical sedimentation tanks. Many of these points will be discussed later when we learn specifically about the AguaClara design process, but it is important to get introduced to these ideas now:

- vertical flow tanks require careful attention to the delivery of water in the bottom of the tank and the extraction of water in the top of the tank;
- vertical and horizontal flow tanks may have different velocities and turbulence capacities due to plan view areas;
- research on tube settlers [[[[cite brentwoodprocess.com]]]] suggests that settle capture velocities should be 0.12 - 0.36 mm/s;
- research on horizontal flow tanks [[[[cite Schulz and Okun (surface water treatment for communities in developing countries)]]]] suggests that settle capture velocities should be 0.24 - 0.72 mm/s.

[[What is the information on "vertical flow sedimentation tanks and "stagnant water (or ripe for innovation)"]]

Now that we have developed a good understanding of the basic principles of sedimentation, we will transition to a discussion of AguaClara innovations.

***********************************************
AguaClara Design Approach
***********************************************

The AguaClara sedimentation tank is a high-rate vertical flow sedimentation tank that was designed with two goals in mind:

1) to use flow distribution as a primary design constraint and,

2) to ensure easy operation and maintenance.

[[QUESTION ABOUT FLOC BREAKUP]]

"Sedimentation Tank as a Circuit" Introduction
================================================

To understand how we will use flow distribution as a primary design constraint, we will develop a concept called the "sedimentation tank as a circuit". This concept will be elaborated on as you learn about the sedimentation tank components and design, but we will introduce it now because it is a driving principle for flow distribution in AguaClara sedimentation tanks. The chapter on Manifold design will be very useful to understand some of these fluids concepts. [[[[link]]]]

An electrical circuit is a path in which electrons flow from a voltage or current source. Electrical circuits frequently have resistors, which are passive electrical components to create resistance in the flow of electric current. What does this have to do with sedimentation tanks? In our "sedimentation tank as a circuit" concept, we will draw parallels between how electrons flow through a circuit to how water flows through the sedimentation tank.

The AguaClara treatment train is designed so that flow is driven by potential energy. The entrance of the sedimentation tank, where water comes from the flocculator, is the source of the flow. Water then moves through the sedimentation tank and exits to the filter. At different points throughout the flow of water in the sedimentation tank, there are changes in piezometric head from fluid acceleration/deceleration and head loss. In the development of our circuit concept, piezometric head is like electrical resistance.

In electrical circuits, electrons will travel the path of least resistance in a parallel path system. Water is similar in that it will flow in the path of least resistance.

.. _figure_circuit_base:
.. figure:: Images/circuit_base.png
    :height: 100px
    :align: center
    :alt: Sedimentation tank as a circuit.

    Sedimentation tank as a circuit.

The figure shows flow through a sedimentation system in which there are two sedimentation bays working in parallel. Each bay has multiple components through which piezometric head changes; wherever a resistor symbol is shown, it means that there is a difference in piezometric head in that section of pipe. We want to understand what is going on between the influent channel and the effluent channel so that we can design to control head loss and fluid flow.

Remember, the goal is to have even flow distribution. It is bad if different flow paths have different head losses or changes in piezometric head. We must consider this between sedimentation bays (comparing each bay to each other) and within a single sedimentation bay (comparing the flows at different points within the sedimentation bay). We want to limit differences in "resistance" to ensure equal flow distribution. Therefore, we define

- anything that makes parallel flow paths different is "bad" head loss.
- anything that increases head loss through all of the paths, to make differences between the paths less significant, is "good" head loss.

We can artificially introduce the second form of head loss to dominate the resistance and render small variations due to pressure recovery insignificant. We will go through each part of the sedimentation tank to understand how these goals drive AguaClara designs. As we learn about each component, we will attempt to categorize its contribution into creating "good" or "bad" head loss.

***********************************************
Components of an AguaClara Sedimentation Tank
***********************************************

[[Note: this section should use words and figures to describe the different parts of the tank and what their purpose is, with brief explanation of how they work. **Perhaps include the final equation necessary for each component, and just don't include the derivations? Not sure how it will fit into flow yet** ]]

In this section, we will develop a conceptual understanding of the sedimentation tank using figures and images. We will be using a mixture of terminology typically found in water treatment settings and AguaClara-specific terminology. We will discuss the different parts of the sedimentation tank in the sequence that a parcel of water would encounter it, from the beginning of the unit process to the end. The three main sections are 1) how water enters the sedimentation tank, 2) how water moves through the sedimentation tank, and 3) how water leaves the sedimentation tank.

.. _figure_sed_tank_overview:
.. figure:: Images/sed_tank_overview.png
    :height: 100px
    :align: center
    :alt: Overview of an AguaClara Sedimentation tank.

    Overview of an AguaClara Sedimentation tank.

1) How water enters the sedimentation tank
============================================

Influent Channel
--------------------

After water exits the flocculator, it is ready for sedimentation. In AguaClara plants, there is one flocculator per treatment train. However, depending on the plant flow rate, one plant may have multiple sedimentation units operating in parallel; we call each of these sedimentation units a 'bay' or a 'tank'. Because there may be multiple sedimentation bays, we have to distribute flocculated water between the bays. To do this, we have an **influent channel**, which receives water from the flocculator and passes it to the sedimentation bays. The channel is long, concrete, and relatively shallow. The objective of the channel is to distribute water and flocs to the sedimentation bays without allowing any settling of flocs in the influent channel. The minimum velocity in the influent channel is about 0.15 mm/s to prevent flocs from settling. In the bottom of the channel, there are pipes that lead to the bottom of each sedimentation bay.

.. _figure_influent_channel_bays:
.. figure:: Images/influent_channel_bays.png
    :height: 100px
    :align: center
    :alt: Influent channel with pipes leading to different sedimentation bays.

    Influent channel with pipes leading to different sedimentation bays.

Does the water in the influent channel get evenly distributed between the different bays? If not, which bay will receive the most water? [[[[link to Manifold chapter]]]] We know from our understanding of fluids and flow distribution that in a pipe (or channel) with multiple orifices that is closed at one end, the distribution of flow is nonuniform along the length of the pipe; it is decelerating. This nonuniformity is due to differences in velocity and pressure in different parts of the pipe. Where else in fluids have we discussed decelerating floc? We have discussed this in flow expansions. And what do we know about pressure in flow expansions? We know that there is higher pressure and slower velocities. At the end of the pipe, there is low velocity and thus high pressure, driving the flow through the orifices at the end. For this same reason, a channel with orifices will have greatest flow delivery to the last orifice. Is this type of head loss "good" or "bad"? In our definition of "good" and "bad", we stated that "bad" head loss creates unequal flow in parallel flow paths. The head loss in the influent channel is therefore "bad" head loss because it can lead to different bays in parallel receiving different flows.

Sedimentation units have multiple bays for a few different reasons. Plants with higher flow rates require more sedimentation bays because the flow through each bay is limited by other design constraints, namely upflow velocity, which will be discussed later. Additionally, it is good to have more than one bay for maintenance purposes; if one bay needs to be cleaned, we want to always have another that can be working. Pipe stubs can be used to plug the entrance hole to a sedimentation bay to shut it down for maintenance.

Of note is that the sedimentation tank influent channel is located directly next to a drain channel. This drain channel was built to remove poorly flocculated water from the treatment train. If an operator observes poor flocculation, they can change the chemical dosing in an attempt to improve flocculation. In the meantime, they will want to dump the poorly flocculated water to avoid poor effluent quality. Operators can plug the entrance hole to the sedimentation bays, allowing the influent channel to fill with water. Once water reaches the height of the wall separating it from the drain channel, the water will pour over from the influent channel into the drain channel. This allows operators to easily dump poorly treated water and then easily restart sedimentation once flocculation performance improves.

Bottom Geometry: Influent Manifold, Diffusers, and Jet Reverser
--------------------------------------------------------------------------------

Now, we will focus on a single bay of the sedimentation system. Flocculated water enters a pipe in the bottom of the influent channel and travels down a few feet. The pipe then has a 90 degree bend and extends along the bottom of the entire length of the sedimentation bay. This section of pipe that distributes water at the bottom of the sedimentation bay is referred to as the **influent manifold**.

.. _figure_influent_channel_manifold:
.. figure:: Images/influent_channel_manifold.png
    :height: 100px
    :align: center
    :alt: Influent channel with pipe leading to one inlet manifold.

    Influent channel with pipe leading to one inlet manifold.

Water exits the influent manifold through a series of orifices and **diffusers** in the bottom of the pipe. Orifices refer to the holes that are drilled into the underside of the manifold while diffusers are what we call short stubs of pipe that extend down from the orifice, perpendicular to the influent manifold. The orifices and diffusers point down to the bottom of the sedimentation bay and extend along the length of the pipe at regular intervals to ensure that water is evenly distributed within the bay. The ends of the diffuser tubes are flattened so that they are thin rectangles and when placed side-by-side achieve a line-jet effect. The end of the influent manifold is capped.

.. _figure_influent_manifold_diffuser_base:
.. figure:: Images/influent_manifold_diffuser_base.png
    :height: 100px
    :align: center
    :alt: Influent manifold with diffusers.

    Influent manifold with diffusers.

.. _figure_influent_manifold_diffuser_flow:
.. figure:: Images/influent_manifold_diffuser_flow.png
    :height: 100px
    :align: center
    :alt: Influent manifold and diffuser flow paths.

    Influent manifold and diffuser flow paths.

[[need to discuss the energy dissipation rate and floc breakup]]

[[NEED TO TALK ABOUT FLOW DISTRIBUTION / MANIFOLDS PPT]]
Recall the discussion about flow distribution in the influent channel. We know that the sedimentation bay furthest away from the flocculator would receive the most flow from the influent channel due to fluids principles. For the same reasons, the orifice at the end of the influent manifold would receive the most flow in the pipe. Is the type of head loss introduced by the 90 degree bend "good" or "bad"? This head loss is "good" because it increases head loss through all paths equally.

Is the type of head loss in the influent manifold "good" or "bad"? Like the influent channel, it would be "bad" head loss because it can lead to different flow along the length of the sedimentation tank; the end of the sedimentation tank would receive more flow than the beginning.

However, the diffuser system was designed to greatly impact the overall flow distribution in an attempt to make the flow more equal in all parts of the system. Diffusers are designed to introduce 1 cm of head loss [[[[link to derivation]]]]. This is "good" head loss because it uniformly increases the head loss through all flow paths. The "good" head loss from the diffusers dominate the "bad" head loss from the influent channel and manifold, making differences between the paths less significant.

The influent manifold diffuser system straightens the fluid jets that are exiting the manifold so that they have no horizontal velocity component. This is critical because even a small horizontal velocity causes a large scale circulation that transports flocs directly to the top of the sedimentation tank. Influent manifolds without flow straightening diffusers are commonly used in vertical flow sedimentation tanks including designs by leading manufacturers.

.. _figure_flow_circulation:
.. figure:: Images/flow_circulation.png
    :height: 100px
    :align: center
    :alt: Flow with a horizontal velocity component that causes problematic flow circulation.

    Flow with a horizontal velocity component that causes problematic flow circulation.

.. _figure_flow_straightening:
.. figure:: Images/flow_straightening.png
    :height: 100px
    :align: center
    :alt: Flow with the diffusers to remove horizontal velocity component to prevent problematic flow circulation.

    Flow with the diffusers to remove horizontal velocity component to prevent problematic flow circulation.

The diffusers create a line jet that spans the entire length of the sedimentation tank. This line jet enters the bay going down, but we want the water to ultimately flow up to make our vertical flow sedimentation tank. To get the flow to redirect upwards, we use a **jet reverser**, which is half of a pipe that is laid in the bottom of the bay.

You may be wondering, why do we need a jet reverser in the first place? Why don't we just have the diffusers point up to avoid having to change the flow in the first place? The answer has multiple components.

- If the diffusers were to point up, they could clog if anything settles in them. While this is unlikely due to the high velocity of flow exiting the small cross-sectional area diffuser, it is something that is avoided by pointing them down.
- If flow were just to point directly up, it would not have an opportunity to sufficiently spread into the width of the sedimentation bay, which could lead to "short-circuiting" and poor flow distribution overall.
- The jet reverser functions as a way to keep flocs suspended by ensuring that anything that settles will be propelled back up from the force of the diffuser jet. Because the diffusers and jet reverser are responsible for resuspension, their design must meet minimum velocity requirements [[[[link]]]]. The jet reverser and diffuser alignment is not symmetrical; the diffusers are offset from the jet reverser centerline. This is intentionally done to ensure that the diffuser jet never collapses to promote a floc blanket, which will be discussed next.

.. _figure_jet_placement:
.. figure:: Images/jet_placement.png
    :height: 100px
    :align: center
    :alt: The jet reverser and diffuser alignments; the offset jet is the most successful.

    The jet reverser and diffuser alignments; the offset jet is the most successful.

There is a lot of research interest in determining the optimal upflow velocity for floc blankets considering that high velocity is better for resuspension but breaks more flocs. Currently, AguaClara plants use an upflow velocity of 1 mm/s.

.. _figure_flat_bottomed_tank:
.. figure:: Images/flat_bottomed_tank.png
   :target: https://www.youtube.com/watch?v=04OksWoRmQI
   :width: 400px
   :align: center
   :alt: Flat bottomed tank with settled flocs.

   Flat bottomed tank with settled flocs.

As shown above, in a flat bottom geometry, flocs settle in the corners of the tank because there is no direct flow of water to resuspend it. Flocs fall in such a way that the corners of the tank will fill first, with more and more flocs settling until the angle of repose is created. This angle that is occupied by flocs suggests that if we want to avoid having flocs settle, we should fill the sides of the tank in with concrete and create a sloped bottom so that there are no surfaces for settling.

The influent manifold, diffusers, and jet reverser work with a **sloped bottom geometry** in an AguaClara plant. The slope on either side of the diffusers is at a 50 degree angle. The bottom geometry allows for smooth flow expansion to the entire plan view area of the bay, and ensures that all flocs that settle are transported to the jet reverser. The diffusers do not touch the bottom of the tank so that flocs on both sides of the diffuser can fall into the jet reverser for resuspension. Thus, there is no accumulation of settled flocs in the main sedimentation basin. Sludge that is allowed to accumulate in the bottom of sedimentation tanks in tropical and temperate climates decomposes anaerobically and generates methane. The methane forms gas bubbles that carry suspended solids to the top of the sedimentation tank and cause a reduction in particle removal efficiency. The AguaClara sedimentation tank bottom geometry prevents sludge accumulation while also ensuring good flow distribution.

.. _figure_sed_cross_section:
.. figure:: Images/sed_cross_section.png
    :height: 100px
    :align: center
    :alt: Cross-section of the bottom of the sedimentation tank.

    Cross-section of the bottom of the sedimentation tank.

.. _figure_bottom_of_sed_tank_detail:
.. figure:: Images/bottom_of_sed_tank_detail.png
    :height: 100px
    :align: center
    :alt: Detail of the bottom of the sedimentation tank.

    Cross-section of the bottom of the sedimentation tank.

.. _figure_Floc_Blanket_Floc_Hopper:
.. figure:: Images/Floc_Blanket_Floc_Hopper.png
   :target: https://www.youtube.com/watch?v=2x12wGb7xZE
   :width: 400px
   :align: center
   :alt: Sloped bottom tank with fully suspended flocs.

   Sloped bottom tank with fully suspended flocs.

So we know that the diffusers, jet reverser, and sloped bottom ensure that no sludge accumulates in the bay by creating a system to resuspend any settled flocs. What are the failure modes for this system? For one, we need to ensure that the jet of water exiting the diffuser is able to maintain its upward direction after the jet reverser. The jet is influenced by the flows that are coming down the sloped sides of the tank. Thus, the jet must have enough momentum to remain upwards even with the momentum from other flows downwards. We can control the momentum of the jet by controlling the cross-sectional area of the diffuser slot. A smaller cross-sectional area will increase the velocity of the jet but the mass is the same because the flow rate for the plant is the same, thus increasing the momentum.

.. _figure_jet_angle:
.. figure:: Images/jet_angle.png
    :height: 100px
    :align: center
    :alt: Jet diameter and current of settled flocs.

    Jet diameter and current of settled flocs.

.. _figure_diffuser_jet_reverser:
.. figure:: Images/diffuser_jet_reverser.png
   :target: https://youtu.be/WEM-YyGITlQ
   :width: 400px
   :align: center
   :alt: Jet reverser resuspending flocs.

   Jet reverser resuspending flocs.

[[Don't worry about floc breakup.]]
  Avoid flow circulations
[[needhelpquestion]]

2) How water moves through the sedimentation tank
==================================================
Floc Blanket
----------------------------------------

The line jet from the diffusers enters the jet reverser to force flow up through the sedimentation bay. The vertical upward jet momentum is used to resuspend flocs that have settled to the bottom of the sedimentation tank. The resuspended flocs form a fluidized bed which is called a **floc blanket**. The bed is fluidized because flocs are kept in suspension by the upflowing water.

For a floc blanket to form, a sedimentation system requires that 1) all flocs be returned to the bottom of the sedimentation tank and 2) requires that all settled flocs be resuspended by incoming water. As will be discussed soon, plate settlers are used to return flocs to the bottom of the bay, while the jet reverser and sloped bottom geometry allow for floc resuspension. Any surface with a horizontal component in a sedimentation tank must be sloped to allow settled flocs to return to the resuspension zone. A flat bottom geometry does not allow for the formation of a floc blanket, as discussed previously.

.. _figure_floc_blanket_experiment:
.. figure:: Images/floc_blanket_experiment.png
   :target: https://www.youtube.com/watch?v=w8ZFCz54IBs
   :width: 400px
   :align: center
   :alt: Floc blanket formation over time.

   Floc blanket formation over time.

Floc blankets improve the performance of a sedimentation tank and reduces settled water turbidity by a factor of 10 (Garland et al., 2017) for multiple reasons:

- by providing additional collision potential. The high concentration of particles, with a suspended solids concentrations of approximately 1-5 g/L, leads to an increase in collisions and particle aggregation. As discussed for vertical flow sedimentation tanks, flocculation can occur in a floc blanket due to shear from suspended flocs which are colliding and growing. Fluidized flocs provide a collision potential of a few thousand. This collision potential is small compared to the collision potential from the flocculator. So how does a small :math:`G \theta` cause a large reduction in turbidity? The two-fold answer may be that the lower :math:`G` value provides an opportunity for all flocs to grow larger without floc breakup. The high concentration of flocs provides many opportunities for clay particles to collide with big flocs, but it is not clear if or when those collisions are successful. We also want to know which flocs are active or inactive in collisions in the floc blanket. [[[[link to derivation]]]]

- by creating a uniform vertical velocity of water entering the plate settlers.

- by transporting excess floc consolidation pipe with a drain port, called the floc hopper. The floc hopper is discussed in the next section.

While we have just explained three reasons that the floc blanket improves sedimentation effluent quality, we do not yet have a model for floc blanket performance. Additional research is needed to create this model, and to determine optimal upflow velocity.

Consider the requirements that we have stated for the creation of the floc blanket. Could we design for a floc blanket in a treatment plant that experiences flow variability? There are some plants that only run for certain hours of the day. While this intermittent flow would impact many parts of the plant, how would it impact the floc blanket specifically? Can a settled floc blanket be resuspended?

We do not yet have a way to design for variable or intermittent flow rates in a sedimentation tank [[is this true?]]. The ability of a settled floc blanket to resuspend is dependent on the characteristics of the flocs themselves. For example, sticky and clumpy flocs would have a more difficult time resuspending because they tend to settle into hard masses in the absence of sufficient upflow velocities. The capacity for resuspension may require site-specific analysis. The AguaClara pilot PF300 in testing at the Cornell Water Treatment Plant is going to determine whether the floc blanket at that site will be able to itermittent flow; the pilot plant and the Cornell Water Treatment Plant will be offline from around 10pm - 5am daily.

It is of interesting note that the suspended solids concentration in the floc blanket is approximately 1-5 g/L. This concentration corresponds to measurements of thousands of NTU, which is remarkably turbid water. A water treatment plant could have 5 NTU water entering the plant, and water in the bottom of the sedimentation tank could have 1000 NTU. This is one clue that there are interesting things happening in the floc blanket; the bottom of the sedimentation tank can be a completely different world from the rest of the treatment process.

An understanding the bottom of a sedimentation tank is important to understand how sedimentation tanks work. However, most sedimentation tanks do not allow the operator to observe what is happening. Without being able to observe the bottom of the sedimentation tank, an operator would not know what is happening or if a floc blanket is forming successfully. AguaClara research teams are working to develop a probe to get data on floc blanket performance. Until then, there are two ways to learn about the floc blanket. The AguaClara plant at the University of Zamorano in Honduras was built with a translucent wall on one end of a sedimentation bay. This allows students and operators to observe the floc blanket. The AguaClara pilot PF300 in testing at the Cornell Water Treatment Plant has small sample ports installed into the side of the reactor. Drawing a sample of water at different heights of the reactor will indicate if a floc blanket has grown, and how deep it is.

Let's recap some important conclusions from this section on the floc blanket.

- The low G flocculation in the floc blanket may allow for the rapid growth of the flocs coming from the flocculator.
- The floc blanket reduces the effluent turbidity from the sedimentation tank.
- The floc blanket requires a mechanism to keep the flocs resuspended:
  - an upflow velocity of approximately 1 mm/s is the current AguaClara design parameter;
  - sloped surfaces to return flocs to the resuspension point is necessary to prevent floc build-up.
- We do not have a model for floc blanket performance, meaning that we don't know the optimal floc blanket depth or optimal upflow velocity.
- We do not yet have a consistent way for operators to observe the floc blanket.
- We do not know what exactly contributes to the ability of a floc blanket to resuspend or survive variable flow.

Floc Hopper
----------------------------------------

The **floc hopper** is a "weir" that provides an opportunity for floc consolidation. The floc hopper controls the depth of the floc blanket because as the floc blanket grows, it will eventually reach the top of the floc hopper. Because flocs are more dense than water, the flocs "spill" over the edge of the floc hopper which allows the floc blanket to stay a constant height while sludge accumulates and consolidates in the floc hopper.

.. _figure_floc_hopper_highlight:
.. figure:: Images/floc_hopper_highlight.png
   :target: https://youtu.be/xh9dTjWRoto
   :width: 400px
   :align: center
   :alt: Floc hopper detail with flocs "spilling" over the wall.

   Floc hopper detail with flocs "spilling" over the wall.

Consolidated sludge in the bottom of the floc hopper is then removed from the sedimentation tank through small drain valve controlled by the operator. Floc hoppers in the lab-scale and PF300 setting are currently set at a 45 degree angle, but further optimization is needed.

.. _figure_benchtop_sed:
.. figure:: Images/benchtop_sed.png
    :height: 100px
    :align: center
    :alt: Benchtop sedimentation tank setup, highlighting the floc blanket and floc hopper.

    Benchtop sedimentation tank setup, highlighting the floc blanket and floc hopper.

The floc hopper allows for a self-cleaning sedimentation tank. By gravity, flocs are sent over to a floc hopper. This means that operators only have to clean the sedimentation tank once every three to six months because there is no stagnant accumulation of anoxic sludge. When operators do clean the sedimentation tank, they are primarily cleaning plate settlers. Under normal operation, operators can open the floc hopper drain valve whenever they want to easily drain the sludge. We don't yet have a method to guide the operation of the floc hopper, so operators determine how frequently to drain the floc hopper from experimental and operational experience. Without the floc blanket transport system, other methods would be required to remove accumulated sludge in the bay. Mechanical sludge removal systems are common alternatives but are well known to be costly to install and a challenge to maintain.

We've stated that a benefit of the floc blanket is that flocs can be removed without mechanical assistance, but why do we need the floc hopper at all? Why can't we just install drain holes in the bottom of the sedimentation tank so that any accumulated sludge is removed? This is a question that plagued AguaClara in its early years. At first, before we were able to successfully build and operate a floc blanket, we had sludge accumulate in the bottom of the sedimentation bay. Therefore, we needed to remove the sludge with drain holes at the bottom. However, to have those drain holes where the sludge was accumulating in the tank, designers made a flat bottom tank. But as we now know, the flat bottom tank is part of the reason that there wasn't any floc blanket forming. As soon as we realized that we could grow a floc blanket with a sloped bottom tank and a jet reverser, we could not use drain holes in the bottom of the tank. Why? Because in the bottom of tanks with floc blankets created by jet reversers, there is no settling. Drain holes at the bottom of a sloped tank would be draining a combination of flocculated water and floc blanket water, neither of which are consolidated thus making the draining ineffective and inefficient. A benefit of the floc hopper is that there is no upflow velocity, which means that the sludge is able to settle and become more dense, allowing for less water waste from draining sludge.

Floc blanket flow into the floc hopper is a function of the mass flux of particles into the sedimentation tank. In order to optimize the floc hopper design, we need to characterize the consolidation rate of the flocs. We do not have a good model for this yet; developing one would allow us to optimize design and guide operators for how much and how frequently the floc hopper should be drained.


Plate Settlers
--------------------

After flowing through the floc blanket, flocs reach the **plate settlers**. Plate settlers are sloped surfaces that provide additional settling area for flocs, thereby increasing the effective settling area of the sedimentation unit without increasing the plan view area. AguaClara plate settlers are sloped at 60 degrees. In our discussion of horizontal and vertical flow sedimentation tanks, an important design parameter was capture velocity which was set by flow rate and plan view area of the sedimentation tank. With the introduction of plate settlers, the important design parameter changes. What matters is not just the plan view area of the sedimentation tank, but instead the projected area of all of the surfaces where particles can settle out, which we call the effective settling area. Without plate settlers, the only way we could improve performance and impact the capture velocity was by increasing the plan view area of the sedimentation tank. With plate settlers, we can improve performance by adding additional settling area without increasing the plan view area. This allows for greater treatment efficiency at low cost because we can maintain a small footprint. Note that plate settlers can also be referred to as lamella settlers, or lamellas.

[[need information about laminar flow between plates]]

The first thing that we will discuss is how flocs can settle on plates. To understand this, we will ask a few questions about how particles and flocs will flow between two plate settlers.

1) What is the critical path?

We need particles to settle on the bottom plate for it to be effectively captured. Thus, the critical path can be shown by a floc that enters the plate settlers closest to the upper plate, because it will have the greatest distance to settle.

.. _figure_plate_settler_critpath:
.. figure:: Images/plate_settler_critpath.png
    :height: 100px
    :align: center
    :alt: Critical path between two plate settlers.

    Critical path between two plate settlers.

2) How far must the particle settle to reach the lower plate?

Let's make a simplification and assume that water is flowing with uniform velocity between the plates, represented by a "top hat" velocity profile. This is a significant assumption, but it is used to help us understand the critical path. The fluid is carrying the floc between the inclined plates while gravity is pulling the floc down. Therefore, a particle must fall the vertical distance between the plates, which is the critical height, :math:`H_c`. The plates are positioned at an angle, :math:`\alpha`, to ensure that settling flocs slide down to the floc blanket. The critical height :math:`H_c` can be expressed in terms of plate settler length, :math:`L`, and plate settler angle, :math:`\alpha`, by :math:`H_c=\frac{S}{cos\alpha}`.

.. _figure_plate_settler_critheight:
.. figure:: Images/plate_settler_critheight.png
    :height: 100px
    :align: center
    :alt: Critical height between two plate settlers.

    Critical height between two plate settlers.

3) What is the total vertical distance that the critical particle will travel?

Taking the vertical component of the critical path, we see that the total vertical distance is :math:`H` where :math:`H =L sin\alpha`.

4) What is the net vertical velocity of a floc between the plate settlers?

The fluid carries the floc between the plate settlers while gravity pulls the floc down. The velocity through the plate settlers has both a horizontal component, :math:`v_{P,H}`, and vertical component, :math:`v_{P,V}`, with a resultant force we call :math:`v_{\alpha}`.

.. _figure_plate_settler_valpha:
.. figure:: Images/plate_settler_valpha.png
    :height: 100px
    :align: center
    :alt: Velocity components between two plate settlers.

    Velocity components between two plate settlers.

This means that the net vertical velocity :math:`v_{P,net}` is the vertical component of flow minus the settling velocity of the floc. Recall our previous discussion of terminal velocity and capture velocity; in this case, because we are designing a plate settler specifically to capture the critical particle, the terminal velocity equals the capture velocity. The terminal velocity is a function of the velocity that the critical particle settles at and the capture velocity is a function of the reactor geometry which we are designing to capture the critical particle. Thus, :math:`v_{P,net}=v_{P,V}-v_{c}`.

.. _figure_plate_settler_vnet:
.. figure:: Images/plate_settler_vnet.png
    :height: 100px
    :align: center
    :alt: Net velocity between two plate settlers.

    Net velocity between two plate settlers.

From answering the questions above, we know that the particle must fall the distance :math:`H_c` at its terminal velocity in the same amount of time that it rises a distance :math:`H` at its net upward velocity, because otherwise it would not be captured; time to travel :math:`H_c` = time to travel :math:`H`

Finding time by dividing by distance by velocity for each travel,

 :math:`Time = \frac{H_c}{v_c} = \frac{H}{v_{P,net}}`

Substituting for :math:`v_{P,net} = v_{P,V}-v_{c}`,

 :math:`Time = \frac{H_c}{v_c} = \frac{H}{v_{P,V}-v_{c}}`

Using trigonometric substitutions for :math:`H_c` and :math:`H`,

 :math:`Time = \frac{S}{v_ccos\alpha} = \frac{Lsin\alpha}{v_{P,V}-v_{c}}`

Rearranging to solve for :math:`v_{c}`,

 :math:`v_c = \frac{S*v_{P,V}}{Lsin\alpha cos\alpha + S}`

Rearranging to solve for :math:`\frac{v_{P,V}}{v_{c}}`,

 :math:`\frac{v_{P,V}}{v_{c}} = 1+\frac{L}{S}cos\alpha sin\alpha`

The equation that we determined for critical velocity, :math:`v_c`, shows its dependence on plate settler geometry. Through another derivation, we can prove that by considering the total projected area over which particles can settle, we determine the same critical velocity.

Beginning with :math:`Q = vA`, we can can modify the equation to fit the specific flow through a plate settler, :math:`Q = v_{\alpha}SW`.

Using trigonometric substitutions, we know that :math:`\frac{v_{P,V}}{v_{\alpha}} = sin\alpha` and :math:`\frac{v_{P,V}}{sin\alpha} = v_{\alpha}`. So,

 :math:`Q = \frac{v_{P,V}SW}{sin\alpha}`

Determining the horizontal projection of the plate settlers,

 :math:`S = Lcos\alpha + \frac{S}{sin\alpha}`

Substituting for area, :math:`A`,

 :math:`A = (Lcos\alpha + \frac{S}{sin\alpha})W`

Solving for :math:`v_c = \frac{Q}{A}`

 :math:`v_c = \frac{S*v_{P,V}}{Lsin\alpha cos\alpha + S}`

We can see that there are five parameters which will impact each other in our design :math:`v_{P,V}, v_{c}, L, S`, and :math:`\alpha`. AguaClara plants typically use constants for :math:`v_{P,V}, v_{c}, S`, and :math:`\alpha`, leaving :math:`L` to be calculated. More information is found in the section on how to design a plant [[]].

Now that we have established how flocs settle on the plate and the increase in plan view area that plate settlers offer, we need to discuss how flocs will act once they are on the plates. We want particles and flocs that settle to agglomerate and slide down the plate settlers to be returned to the floc blanket. We will explore this concept by first considering the desired spacing between plate settlers.

Let's start with a basic question. If we know that adding plate settlers improves performance, why don't we just keep adding more and more plate settlers to our system? Is there any impact of placing plates closer together?

We know that more plates means more effective settling area which means that we could remover more particles and make our tank smaller to save money and limit the use of concrete. But how close can those plates be?

The Ten State Standards report that plate settlers should have a separation of two inches, with very long plate settlers, which means very deep tanks. Sedimentation tanks are usually 4 meters deep, maybe because filters are also deep. This is a result of the engineering context rather than the basic design principles. The Ten State Standards are primarily based off the modification of existing sedimentation tanks which were usually built deep and then plate settlers were added. This means that there wasn't added incentive to optimize the entire plate settler and tank process because the tanks were already built. However, AguaClara designs are made to use all of the AguaClara innovations in a green field, meaning that we are incentivized to optimize every part of this design process [[weird way to say this...reword]].

AguaClara plants can design for changes in the depth and/or plan view area of the tank for optimal plate settler efficiency. We want to have the smallest and shallowest tanks possible for low cost and ease of construction. We know that in the plate settler design, there is a dimensionless parameter of plate spacing to length, :math:`\frac{S}{L}`. The ratio is close to constant, which means that if we double the length of the plate settler, we can double the spacing between the plate settler and get the same performance as when we started. Conversely, if we halve the distance between the plate settlers, we can halve the length of the plate settlers. But how far can we push this? Can we make really compact plate settlers?

What we really want to know is: what is the connection of spacing between plate settlers and performance?

.. _figure_plate_settler_depth:
.. figure:: Images/plate_settler_depth.png
    :height: 100px
    :align: center
    :alt: Relationship between plate settler length and sedimentation tank depth.

    Relationship between plate settler length and sedimentation tank depth.

When we were discussed how plate settlers promote settling, we assumed a uniform velocity profile between the plates. However, we know from fluid mechanics and boundary layer rules that in reality, there is a nonuniform velocity profile. The flow between the plates, as determined by the Reynolds number, is laminar which means that there is a parabolic velocity profile between the plates and the shape of the parabola is affected by the distance between the plates.

There are some cases in which the plates are so close that even if flocs settle on the plate, they do not slide down. This is called **floc rollup**. Consider the following questions:

1) Why would flocs roll up?

It is a force balance! There is a force of gravity pulling the particle down, balanced with the force that the fluid flow exerts through drag related to viscosity. But why does it matter if plates are close together for floc roll up? The average velocity between plates is about 1 mm/s and is the same for any spacing. However, when plates are closer together the velocity profile is much steeper. Compared with plates with greater spacing, the closer plates cause there to be a higher velocity closer to the surface of the plate. This means that flocs between closely spaced plates will see a greater velocity closer to the plate settler, which will impact the force balance. The derivation of the force balance is [[[[link]]]]. The velocity that the flocs slide down the plate is called :math:`v_{Slide}`.

[[[[need to make. force balance diagram]]]]

2) How would you define the transition between floc rollup and slide down? What would describe the case for a floc that is stationary on the plate settler (not rolling up or sliding down?)

The transition is defined as when the gravitational forces and the fluid drag forces match.

3) Will little flocs or big flocs be most vulnerable to floc rollup?

This is a very complicated question. We would expect big flocs to slide down because they are heavier and have a greater gravitational force. However, bigger flocs also have a greater drag force and are out further into the flow. Because of the velocity profile, they will feel a higher velocity than smaller flocs. This means that the answer to this question should be determine mathematically, which it is in the next section.

4) Will large or small spacing between plates cause more floc rollup?

As we have already suggested, small spacing between plates will cause more floc rollup due to the steeper resulting velocity profile between the plates.

So what does this mean for plate settler spacing? Let's review some results from lab experiments. The following graph shows minimum plate settler spacing (mm) as a function of floc terminal velocity (mm/s). Some important things to note are that AguaClara plate settlers are designed for a capture velocity of 0.12 mm/s (recall that this capture velocity means that we want to capture flocs that are settling at 0.12 mm/s and faster). Before AguaClara filters were designed and deployed, AguaClara adopted the 0.12 mm/s capture velocity in an effort to reduce effluent turbidity as much as possible.

Reading the graph, we can see the line for 1 mm/s upflow velocity, :math:`v_{P,V}` [[I don't think this is the right variable name]], at 0.12 mm/s capture velocity requires a minimum plate spacing of about about 2.5 mm to prevent floc rollup. Now, let's interpret this result. If the upflow velocity increases, we see that the required spacing between plates increases. The results from these experiments will help us answer one of our previous questions: will little flocs or big flocs be most vulnerable to floc rollup? From the graph, we know that it is the little ones. Smaller floc terminal velocities indicate smaller particles, and the graph shows that smaller floc terminal velocities require larger distances of floc spacing to not roll up. The bigger the flocs, the smaller the spacing required to not roll up. Little flocs are harder to capture as you move plates closer together. Little flocs roll up first.

.. _figure_floc_vsed:
.. figure:: Images/floc_vsed.png
    :height: 100px
    :align: center
    :alt: Minimum plate settler spacing as a function of floc sedimentation velocity.

    Minimum plate settler spacing as a function of floc sedimentation velocity.

This analysis suggests that the Standard design is nowhere near the constraint of floc roll up (recall that Standard design reports separations of 5 cm). AguaClara plate settlers are currently using separations of 2.5 cm, which is also far above the constraint of floc roll up. So if we determined that the minimum spacing for floc roll up constraints is closer to 2.5 mm, why are we using 2.5 cm? The answer is related to our initial assumptions about the floc composition and terminal velocity. When we calculated terminal velocities, we did so for clay-based flocs. But in reality, there are many kinds of flocs formed in water treatment plants. Dissolved organic matter also interacts with coagulant to form flocs that we assume are much less dense than clay based flocs. We don't currently have a good model to understand how these organic-matter flocs. We don't know what the terminal velocity of flocs is if they are made of organics, coagulant, and clay. But even without knowing specifics, how do we think minimum plate spacing will be impacted by flocs that are formed from organic matter instead of clay? If we use dissolved organic matter, the equation predicts that spacing will change primarily due to the big difference in floc density. As floc density decreases, as we expect for organic matter, minimum spacing increases. However, we don't yet know what that spacing is or where the boundary is because we don't know the properties of the humic acid-coagulant flocs. This prompts us to opt for safety factors, so we have chosen a plate settler spacing of 2.5 cm. There is room to learn more here.

Why does the plate settling distance matter so much? How much does it impact the rest of the sedimentation tank and its design?

One impact of plate settler spacing is on sedimentation tank depth. We know that the spacing between plate settlers has a strong influence on sedimentation tank depth and closer plate settlers allows for shallower tanks. There is a diminishing effect for small spacings, meaning that the difference in depth between 5 and 2.5 cm spacing is greater than the different in depth between 2.5 and 1 cm spacing. Because AguaClara does not yet have a good model for non-clay flocs, we cannot optimize our plate settler spacing and thus cannot optimize for the shallowest tanks possible.

Another impact of plate settler spacing is on flow distribution in the tank. This is related to our previous discussion of pressure recovery and flow distribution. Reduced spacing between plates leads to an increased pressure drop through the plate settlers due to higher head loss. Therefore, plate settlers with small spacing will have more uniform flow distributions because head loss will dominate. The pressure difference between one plate settler and the next would be very small compared to the pressure difference between the bottom of the plate settlers and the top of the plate settlers. This use of head loss can potentially get us better flow distribution. When the plates are brought closer together, there is more shear between the plates because the average velocity remains the same. The velocity gradient is higher between closer plates, which leads to higher shear, and thus higher head loss.

However, if the plates are closer together, then they will be shorter in length to keep the capture velocity constant. The decrease in length decreases the total amount of shear. The head loss from the competing impacts to shear can be determined through a force balance and the Navier-Stokes equation, as shown in the derivations section [[[[link and plot]]]]. The important thing to note is that after determining head loss as a function of plate settler spacing, we realize that the plate settlers do not provide much head loss at the design separation of 2.5 cm. Head loss through plate settlers is really small, which means that they do not contribute much to equalizing flow distribution. So, is this head loss "good" or "bad"? It is neither because it is so small that it is negligible in our overall system.

The velocities of any eddies or mean flow need to be less than 4 mm/s to achieve uniform flow through plate settlers. This means that if there is any flow entering the plate settlers at greater than 4 mm/s, the head loss provided by the plate settlers will not help at all to dampen the nonuniformity and there will not be adequate flow distribution. Luckily for us, the upflow velocity through the sedimentation tank is on average 1 mm/s, which fulfills the requirement of less than 4 mm/s. However, remember the diffusers that distribute water into the sedimentation tank? They create velocities on the order of 100s of mm/s [[help]]. Those high initial velocities are damped out by the floc blanket which helps to distribute the flow. If we weren't able to use the floc blanket to dampen the flow to be less than 4 mm/s, then the plate settlers would not provide any head loss to help with uniform flow distribution. This point about uniform flow is really important.

Now, lets discuss a plate settler problem that has not yet been solved: **floc volcanoes**. Floc volcanoes occur when water and flocs rise preferentially in one part of the sedimentation tank. At points of high velocity, flocs can rise to the surface of the water. Consider the following case: an AguaClara plant in San Nicolas, Honduras, was witnessing intermittent floc volcanoes in the sedimentation tanks. During operation, the plant was treating raw water with 4 NTU with a PACl dose of 3.5 mg/L. The settled water turbidity varied between 0.5 and 4 NTU. What might explain the floc volcanoes and very poor plant performance? Try coming up with a hypothesis that matches the information given to us from the plant. We want to figure out what is causing this problem so we can design a solution. What questions would you want to ask the technicians or engineers in Honduras? This exercise emphasizes the idea that asking the right questions are sometimes the hardest first step to learning more information.

Some hypotheses and questions may include:

1) is the problem related to dissolved air flotation? Dissolved air coming out of flocculation can cause flocs to float to the top.

After asking the operators, we are told that there are not any bubbles in the sedimentation tank.

2) is the problem regularly intermittent? Is there anything that we can correlate these fluctuations to?

After asking the operators, we are told that the floc volcanoes appear in the early afternoon each day.

.. _figure_temp_turbidity:
.. figure:: Images/temp_turbidity.png
    :height: 100px
    :align: center
    :alt: Turbidity as a function of time in San Nicolas, Honduras.

    Turbidity as a function of time in San Nicolas, Honduras.

Using this new information, we have to make another hypothesis about why the floc volcanoes are impacted daily. Perhaps it is related to the sun and daily temperature changes. We can ask the operators to measure the water temperatures so we can do some analysis. The operators measure temperature and we plot the results, providing the following graph.

We know that this plant brings water from a water source about 14 km away. The water is transported in a galvanized iron pipe that is placed on the surface of the ground because there is no concern about freezing pipes in Honduras (galvanized iron is not damaged by UV like PVC pipe is). The pipe functions as a 14 km water heater, raising the temperature of the water to the plant after noon.

But why does the temperature difference cause a problem for the plate settlers?
The problem is that there is warmer water entering the sedimentation tank than what is in it. This temperature difference causes a density difference in the sedimentation tank and plate settlers. The less dense, warmer water rises to the top of the plate settlers while the cold water drops to the bottom of the plate. This creates a current, allowing water to flow up on the top and settle on the bottom. The temperature gradient changes slowly over a few hours.

.. _figure_temp_tube_settler:
.. figure:: Images/temp_tube_settler.png
    :height: 100px
    :align: center
    :alt: Hot water rising and cold water settling in a tube settler.

    Hot water rising and cold water settling in a tube settler.

So, now that we think we know what the problem is, how would we try to solve it? One idea would be to paint the entire line to reflect heat, but this is not feasible due to cost. The town Water Board had been maintaining the distribution line by cleaning weeds and brush from the pipe. The solution ended up being to just let the weeds grow over the pipe to provide shade. We haven't yet come up with a real solution. A possible long-term solution could be to design a sedimentation tank that has a really short residence time. The longer the residence time in the sedimentation tank, the worse the problem is because there is a large variation between the water that entered it last night and the water that enters it this afternoon. A tank with a really short residence time, on the order of a few minutes, would ensure that the water coming in would be very close to the water already in the tank.

Let's recap some important conclusions from this section on plate settlers.

1. Reynolds number calculations of flow through plate settlers prove that there is laminar flow between plate settlers. This is important because it allows us to assume that a parabolic velocity profile is established.
#. There is very low head loss between plate settlers so they will not do a good job of helping to achieve uniform flow between the plate settlers.
#. The plate settlers are designed to capture flocs with sedimentation velocities greater than the settle capture velocity. AguaClara currently uses :math:`v_c = 0.12` mm/s but this value needs to be further optimized; we would like to know how settled water turbidity changes with capture velocity. Future work includes choosing a settle capture velocity based on overall plate performance.
#. Plate settler spacing:

   a. Plate settler spacing determines the ability of flocs to roll down the incline.
   b. Smaller spacings between plate setters have diminishing returns in terms of sedimentation tank depth. The current AguaClara spacing is 2.5 cm but there is room for further optimization.
   c. Flocs made from natural organic matter (NOM) may be less dense, more prone to floc rollup, and may require larger spacing between plate settlers.


3) How water leaves the sedimentation tank
===========================================

Now that we have passed through the plate settlers, we are ready to leave the sedimentation tank.

Submerged Effluent Manifold
----------------------------------------

The **submerged effluent manifold**, sometimes called a launder, collects settled water from the sedimentation tank. It is a horizontal pipe that extends along the length of the tank and is located above the plate settlers but below the surface of the water. The submerged pipe has orifices drilled into its top; water enters the pipe through the orifices and the pipe leads out of the sedimentation tank. Recall that the influent manifold also uses a submerged pipe and orifice design to distribute flow. However, unlike the influent manifold, the effluent manifold does not include diffusers because we do not need to precisely control velocity and flow direction.

.. _figure_effluent_manifold:
.. figure:: Images/effluent_manifold.png
    :height: 100px
    :align: center
    :alt: Effluent manifold from the side- and top-view.

    Effluent manifold from the side- and top-view.

The orifices in the pipe are evenly distributed along the length of the pipe to promote even flow collection from the tank. The orifices are designed create uniform head loss. Is this head loss "good" or "bad"? Like the diffusers, the orifices in the effluent manifold create "good" head loss because they increase head loss through all flow paths. This is critical because there is pressure recovery within the effluent manifold that creates "bad" head loss.

Are there effluent manifold exit losses? What type of head loss would it be? This head loss is a result of exit loss into its receiving channel. Is it "good" or "bad"? This head loss is also "good" head loss because it impacts all flow paths the same; each sedimentation tank bay and all water within a single bay is subject to the same amount of exit loss.

Why did AguaClara design the effluent manifold to be submerged? It is designed to be submerged because sometimes there are particles or substances that rise to the top of sedimentation tanks and float on the water surface. These particles or substances may be flocs that escaped capture and remain buoyant, or may be foam or scum that results from organic matter in the water. No matter what it is that is rising to the water surface, we want to avoid it entering the settled water effluent pipe. Placing the effluent manifold below the surface allows particles or substances floating on the surface to remain separate from the effluent water headed towards filtration. Operators can then skim the water surface to remove and dispose of anything that floats.

Why are the orifices in the effluent manifold located at the top of the pipe?
They are located on the top to promote even flow collection and for ease of operation and maintenance. The orifices need to be either located on the top or bottom so that they are symmetrical about the tank because if the orifices were put on the sides, then they might not draw water evenly from the entire tank. So, we are to choose between the top or the bottom; which would be better for operation and maintenance? The top is better because orifices located on the top of the pipe can be easily observed and maintained by operators in case any clogging occurs. We also want to limit the number of flocs that rise through the plate settlers and enter the effluent manifold. Locating the orifices on the top discourages that from happening by not drawing up directly from the top of plate settlers and by giving more time for flocs to potentially settle.

Exit Weir and Effluent Channel
----------------------------------------

The submerged effluent manifold transports water from the sedimentation tank to a channel that runs perpendicular to the sedimentation bays. The channel collects water from all of the sedimentation bays. Water leaves this channel by flowing over a small wall, called the **exit weir**. The exit weir is used as a flow control device because it is the free-fall that controls water levels all the way upstream to the previous free-fall, which was the LFOM. So, the height of the exit weir is critical to ensuring appropriate water levels in the flocculator and sedimentation tank. In construction, great care is taken to ensure that this wall is precise and level.

After the water flows over the exit weir, it is collected in the **effluent channel**. The effluent channel has pipes embedded in the bottom of it which lead the settled water to the filter inlet box. Like the sedimentation tank influent channel, the effluent channel is located directly next to the drain channel. This allows the operator to remove poorly settled water from the treatment train. If an operator observes poor sedimentation, they can plug the entrance hole to the filter box, allowing the effluent channel to fill with water. Once water reaches the height of the wall separating it from the drain channel, the water will pour over from the influent channel into the drain channel.

.. _figure_channel_labeled:
.. figure:: Images/channel_labeled.png
    :height: 100px
    :align: center
    :alt: Image of sedimentation channels.

    Image of sedimentation channels.

.. _figure_channel_labeled_cad:
.. figure:: Images/channel_labeled_cad.png
    :height: 100px
    :align: center
    :alt: Figure of sedimentation channels.

    Figure of sedimentation channels.


Sedimentation Conclusions and Review
=======================================

Conclusions
--------------------------------

You have now been introduced to the AguaClara sedimentation tank in three parts: 1) how water enters the sedimentation tank, 2) how water moves through the sedimentation tank, and 3) how water leaves the sedimentation tank. This introduction should allow you to understand the components of the sedimentation unit process, the purpose of each component, and AguaClara-specific innovations.

Let's recap some important points about the sedimentation tank.

- The AguaClara sedimentation tank includes three process in one tank: flocculation, sedimentation, and consolidation.
- Floc blankets improve sedimentation tank performance.
- The floc blanket and floc hopper design eliminate the need for mechanized sludge removal by using hydraulic sludge removal.
- Plate settlers make it possible to significantly reduce the plan-view area of the sedimentation tank.
- Reduced plate settler spacing allows for shallower, and therefore cheaper, tanks.
- Flow distribution is very important in sedimentation tank design.
- Hydraulic residence times can be greatly decreased using AguaClara innovations. While some standards suggest a minimum of four hours for sedimentation processes, AguaClara plants have shown that a hydraulic residence time of 24 minutes is sufficient for efficient sedimentation.
- The AguaClara sedimentation tank design is driven by the need for high treatment capability coupled with easy operation and maintenance.
- There is "good" head loss introduced by the influent manifold entrance, diffusers, effluent manifold orifices, and effluent manifold exit. There is "bad" head loss introduced by pressure recovery in the influent channel, influent manifold, and effluent manifold. Even flow distribution is achieved by ensuring that "good" head loss dominates through intentional design.

.. _figure_circuit_full:
.. figure:: Images/circuit_full.png
    :height: 100px
    :align: center
    :alt: Sedimentation tank as a circuit, showing "good" and "bad" head loss.

    Sedimentation tank as a circuit, showing "good" and "bad" head loss.

Review
--------------------------------
You can review your understanding of AguaClara sedimentation tanks by asking yourself the following questions:

#. Why do horizontal flow sedimentation tanks perform must worse than theory predicts?
#. How does the floc blanket improve sedimentation tank performance?
#. What is the purpose of the floc hopper?
#. Why do we use plate settlers?
#. What is the failure mechanism for small spacing between plate settlers?
#. What helps the flow divide evenly between and within the sedimentation tanks?

The hydraulic self cleaning sedimentation tank with a high performing floc blanket, zero sludge accumulation, and with no moving parts outperforms conventional sedimentation tanks on capital cost, performance, and maintenance costs. We will now transition to the mathematical models which explain how we make these advancements possible.

***********************************************
Design of an AguaClara Sedimentation Tank
***********************************************
In the next section, we will develop the mathematical models that help us explain the design.

Note: this section will build off of the conceptual understanding established in the previous section and will explain how the tank works with derivations and mathematical models.

Comparison of velocities and flow in sedimentation tank
========================================================

To understand how water flows in the sedimentation tank, we must understand how the water velocity changes with the geometry. There are four distinct zones in the sedimentation tank: 1) the velocity of water exiting the diffusers, 2) the velocity of water moving through the floc blanket, 3) the velocity of water that enters the plate settlers, and 4) the velocity of water through the plate settlers. The geometry of the sedimentation tank changes in these four zones, so we will follow these changes to make sure that we understand the conservation of flow. The flow going through the sedimentation tank is the same everywhere, but average velocities are different. The fact that flow rate is velocity multiplied by area, :math:`Q = v * A`, will be our guiding principle. In all cases,

| :math:`Q_{Sed} =` flow rate through each sedimentation tank
| :math:`W_{Sed} =` width of each sedimentation tank

.. _figure_sed_tank_flow_conserve:
.. figure:: Images/sed_tank_flow_conserve.png
    :height: 100px
    :align: center
    :alt: AguaClara sedimentation tank showing "lost triangle" and its impact on relevant lengths.

    AguaClara sedimentation tank showing "lost triangle" and its impact on relevant lengths.

1) Velocity and flow exiting the diffusers
------------------------------------------------------------

This is discussed specifically in the section on diffusers [[should the diffuser explanation go here? or elsewhere?]]

2) Velocity and flow in the floc blanket
----------------------------------------

After the water exits the diffusers and jet reverser, it flows through the expanded floc blanket region where:

| :math:`L_{SedFloc} =` length of the sedimentation tank that has a floc blanket
| :math:`v_{S,V} =` upflow velocity of the water through the floc blanket

Thus, :math:`Q_{Sed} = W_{Sed}*L_{SedFloc}*v_{S,V}`

3) Velocity and flow entering the plate settlers
------------------------------------------------------------

The 'active' sedimentation zone refers to the area of the tank in which water can flow through the plate settlers where:

| :math:`L_{SedActive} =` length of the sedimentation tank that includes entrance to a plate settlers
| :math:`v_{A,V} =` upflow velocity of the water entering the plate settlers; vertical velocity in 'active' region

The only reason that there is a distinction between this area and the floc blanket area is because plate settlers are built at an angle. This angle creates a "lost triangle" because there is a space in which the plate settlers are not effective and water does not flow through them. Because the active length is less than the floc blanket length, :math:`L_{SedActive} < L_{SedFloc}`, and because flow must be conserved, the average active velocity must be greater than the average upflow velocity through the floc blanket, :math:`v_{A,V} > v_{S,V}`. The same flow going through less area means that the velocity must increase.

Thus, :math:`Q_{Sed} = W_{Sed}*L_{SedActive}*v_{A,V}`, and :math:`v_{A,V} > v_{S,V}`.

4) Velocity and flow in the plate settlers
-------------------------------------------

Now, we will discuss flow through plate settlers where:

| :math:`v_{P,V} =` upflow velocity of the water in the plate settlers; vertical velocity component between the plate settlers
| :math:`S =` spacing between plate settlers
| :math:`B =` center-to-center distance between plate settlers
| :math:`T =` thickness of plate settlers
| :math:`L =` length of plate settlers

We know that plate settlers have a certain thickness and take up area, which means that once we reach the plate settler zone, there is less area for water to travel through. Because flow is conserved and there is a decrease in area, we know that the upflow velocity of water through the plate settlers must increase compared to the upflow velocity of water below the plate settlers, :math:`v_{P,V} > v_{A,V}`.

Thus, :math:`v_{P,V} > v_{A,V} > v_{S,V}`

In addition to the vertical velocity component increasing between the plates, the resultant velocity of water between the plates increases compared to :math:`v_{A,V}`. What are the two reasons that this is true?

- the first reason, as already discussed, is that the vertical velocity component needs to increase to ensure conservation of flow.

- the second reason has to do with the fact that the resultant velocity of water between the plates is at an angle. This means that there is a horizontal component introduced. Because we know that the vertical velocity increases, and there is a new positive horizontal velocity component, the resultant velocity must also increase.

Now, consider a tube settler used in a lab setting instead of a plate settler. If a tube settler was designed with an angle to mimic a plate settler, would the water change vertical velocity after the angle? How does this compare to the plate settler scenario? In the case of the tube settler, the vertical velocity does not increase because there is no change in flow area; the diameter of the tube is constant throughout, meaning that for the flow to remain constant, the velocity does not change.

For another example of flow conservation, let's consider the relationship between :math:`v_{P,V}*S` and :math:`v_{A,V}*B`. :math:`B` is the center-to-center distance between plate settlers, and does not take into account the thickness of plate settlers. Considering only the center-to-center distance means that the area for water to travel through does to change from before the plate settlers to within the plate settlers because we are not accounting for any thickness. If the area does not change, then velocity should also not change to keep flow conserved. However, if we are to account for thickness, we must discuss :math:`S` which is the spacing between plate settlers. This does take into account the change in area,  which means that the velocity would need to increase through the lesser area. So if we look at the flow through plate settlers, we can confirm that :math:`v_{P,V}*S = v_{A,V}*B`.

By using flow conservation and plate settler geometry, we can begin to understand the mathematical relationships that drive design.

Plate Settler Design
========================================================
Plate Settler Parameters
-------------------------

From the relationship that :math:`v_{P,V}*S = v_{A,V}*B`, we can solve for :math:`B` or :math:`L` in terms of their related parameters. [[figure out how to either link or incorporate this with the discussion of this in the plate settler explanation]].

Let's start with the relationships that we already know:

:math:`v_{P,V}*S = v_{A,V}*B` and :math:`B = S+T`

.. _figure_SvsBplatesettlers:
.. figure:: Images/SvsBplatesettlers.png
    :height: 100px
    :align: center
    :alt: Thick plate settlers.

    Thick plate settlers.

.. _figure_plate_settler_base:
.. figure:: Images/plate_settler_base.png
    :height: 100px
    :align: center
    :alt: Plate settlers.

    Plate settlers.

Solving for :math:`v_{P,V}`, we rearrange and substitute by,

 :math:`v_{P,V}*S = v_{A,V}*(S+T)`

 :math:`v_{P,V} = \frac{v_{A,V}*(S+T)}{S}`

We also already know from our discussion of plate settlers that we can relate capture velocity, :math:`v_c`, to :math:`S, L, \alpha`, and :math:`v_{P,V}` by, [[link to previous discussion]]

 :math:`v_c = \frac{S*v_{P,V}}{Lsin\alpha cos\alpha + S}`

Substitute for :math:`v_{P,V} = \frac{v_{A,V}*(S+T)}{S}` by,

 :math:`v_c = (\frac{S}{Lsin\alpha cos\alpha + S})(\frac{v_{A,V}*(S+T)}{S})`

Now, we can use this form of the capture velocity equation to solve for :math:`B` or :math:`L`, as shown by,

 :math:`B = \frac{Lsin\alpha cos\alpha - T}{\frac{v_{P,V}}{v_c}-1}`

 :math:`L = \frac{B(\frac{v_{P,V}}{v_c}-1) + T}{sin\alpha cos\alpha}`

 :math:`L = \frac{S(\frac{v_{P,V}}{v_c}-1) + T(\frac{v_{P,V}}{v_c})}{sin\alpha cos\alpha}`

The AguaClara plate settler design approach is summarized in the following table:

+----------------------+----------------------+-----------------------------------+----------------------------+--------------------------+
| Parameter            | Variable             | Determined by:                    | Determines:                | Value                    |
+======================+======================+===================================+============================+==========================+
| Upflow velocity      | :math:`v_{S,V}`| floc blanket                      | size of tank               | 1 :math:`\frac{mm}{s}`   |
|                      |                      | upflow requirements               |                            |                          |
+----------------------+----------------------+-----------------------------------+----------------------------+--------------------------+
| Capture velocity     | :math:`v_c`          | target turbidity                  | particle size distribution | 0.12 :math:`\frac{mm}{s}`|
|                      |                      |                                   | after floc blanket         |  **needs research**      |
+----------------------+----------------------+-----------------------------------+----------------------------+--------------------------+
| Plate angle          | :math:`\alpha`       | self-cleaning requirements        | :math:`L`                  | 60 deg                   |
+----------------------+----------------------+-----------------------------------+----------------------------+--------------------------+
| Spacing              | :math:`S`            | clogging and floc                 | :math:`L`                  | 2.5 cm                   |
|                      |                      | rollup constraints                |                            |                          |
+----------------------+----------------------+-----------------------------------+----------------------------+--------------------------+
| Plate settler length | :math:`L`            | :math:`v_{S,V},v_c,\alpha,S`      | tank depth                 | Calculated for each plant|
+----------------------+----------------------+-----------------------------------+----------------------------+--------------------------+

.. _figure_plate_settler_model_table:
.. figure:: Images/plate_settler_model_table.png
    :height: 100px
    :align: center
    :alt: Plate settler models and relevant equations.

    Plate settler models and relevant equations.

Floc Rollup and Slide Velocity
------------------------------

As has been discussed, floc rollup is a failure mode of plate settler performance [[link]]. To determine the appropriate spacing between plate settlers, we must consider the potential for flocs to rollup because we want to minimize rollup and promote settling. We will determine this by calculating the floc sedimentation velocity, :math:`v_{Slide}`, that can be captured given a plate spacing. The steps to calculate this are:

1) find the velocity gradient next to the plate

2) find the fluid velocity at the center of the floc

3) find terminal velocity of the floc down the plate (for the case of zero velocity fluid)

4) set those two velocities equal for the critical case of no movement, and the required plate spacing

5) find the floc sedimentation velocity, :math:`v_{Slide}`

We will solve for both the plate settler and tube settler conditions.

1) Find the velocity gradient next to the plate:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Plate Settler
"""""""""""""

.. _figure_plate_settler_boundary_conditions:
.. figure:: Images/plate_settler_boundary_conditions.png
    :height: 100px
    :align: center
    :alt: Boundary conditions in plate settlers.

    Boundary conditions in plate settlers.

.. _figure_floc_rollup_base:
.. figure:: Images/floc_rollup_base.png
    :height: 100px
    :align: center
    :alt: Velocity profile between plate settlers.

    Velocity profile between plate settlers.

We begin by describing the conditions of infinite horizontal plates.

:math:`\frac{y^2}{2}\frac{dp}{dx} + Ay + B = \mu u` [[need explanation of variables and where this came from]]

We employ the no-slip condition to solve for the constants A and B. The no-slip condition is that :math:`u = 0` at :math:`y = 0` and :math:`y = S`, where :math:`u` is the horizontal velocity component, :math:`y` is the location in the y-axis direction between plates, and :math:`S` is the spacing between plates.

at :math:`u = 0` and :math:`y = 0`:

 :math:`\frac{0}{2}\frac{dp}{dx} + A*0 + B = \mu *0`

 :math:`B = 0`

at :math:`u = 0` and :math:`y = S`, the solving for A:

 :math:`\frac{S^2}{2}\frac{dp}{dx} + AS + 0 = \mu *0`

 :math:`\frac{S^2}{2}\frac{dp}{dx} + AS = 0`

 :math:`A = \frac{-S}{2}\frac{dp}{dx}`

Our initial equation can be updated as,

:math:`\frac{y^2}{2}\frac{dp}{dx} + \frac{-S}{2}\frac{dp}{dx}y + B = \mu u`

If we let :math:`\frac{dp}{dx}` be negative [[??]], then we can solve for :math:`\tau` [[?]].

 :math:`\mu(\frac{du}{dy}) = y \frac{dp}{dx} + A`

 :math:`\tau = (y - \frac{S}{2}) \frac{dp}{dx}`

Determining the average velocity between plates, :math:` v_{\alpha}`, [[??]]

 :math:`u = \frac{y(y-S)}{2\mu} \frac{dp}{dx}`

 :math:` v_{\alpha} = \frac{q}{S} = \frac{1}{S} \int_{0}^{S}udy = \frac{1}{S} \int_{0}^{S} (\frac{y^2 - Sy}{2\mu} (\frac{dp}{dx}))dy`

Integrating to get average velocity, then solving for :math:`\frac{dp}{dx}`,

 :math:` v_{\alpha} = \frac{S^2}{12\mu} \frac{dp}{dx}`

 :math:` \frac{dp}{dx} = \frac{12\mu v_{\alpha} }{S^2}`

Using Navier-Stokes to model the flow between the plates, and substituting our equation for :math:` \frac{dp}{dx}`, [[??]]

 :math:`(\frac{du}{dy})_{y=0} = \frac{-S}{2\mu} \frac{dp}{dx} `

 :math:`(\frac{du}{dy})_{y=0} = \frac{-S}{2\mu} \frac{12\mu v_{\alpha} }{S^2} `

Simplifying the :math:`(\frac{du}{dy})_{y=0}`, we have the velocity gradient as function of average velocity for plate geometry as,

 :math:`(\frac{du}{dy})_{y=0} = \frac{6 v_{\alpha}}{S}`

 :math:`\frac{ dv_{\alpha} }{ dy_{y=0} } = \frac{6 v_{\alpha}}{S} `

.. _figure_floc_rollup_step1:
.. figure:: Images/floc_rollup_step1.png
  :height: 100px
  :align: center
  :alt: Velocity gradient next to the plate.

  Velocity gradient next to the plate.


Tube Settler
"""""""""""""
For tube settlers, we will assume laminar flow through circular tubes. :math:`R` is the radius of the tube, and we assume that the maximum velocity is when :math:`r = 0`. The velocity distribution is paraboloid of revolution, therefore average velocity, :math:`v`, is half of the maximum velocity, :math:`v_{max}`. So, :math:`v = \frac{1}{2}v_{max}`. We also know that :math:`Q = vA` and :math:`Q = v \pi R^2`. In the case of the tube settler, :math:`\frac{dp}{dx}` is the pressure gradient in the direction of flow, not the pressure gradient due to changes in elevation.

 :math:`v_{\alpha} = \frac{r^2 - R^2}{4\mu} \frac{dp}{dx}`

 :math:`v_{max} = - \frac{R^2}{4\mu} \frac{dp}{dx}`

 :math:`v = - \frac{R^2}{8\mu} \frac{dp}{dx}`

 :math:`Q = - \frac{\pi R^4}{8\mu} \frac{dp}{dx}`

Rearranging the flow equation :math:`Q` to solve for :math:`\frac{dp}{dx}`,

 :math:`\frac{dp}{dx} = - \frac{8 \mu Q}{\pi R^4}`

Plugging :math:`\frac{dp}{dx}` into the original equation fo :math:`v_{\alpha}`,

  :math:`v_{\alpha} = -2Q \frac{r^2 - R^2}{\pi R^4} `

  :math:`\frac{ dv_{\alpha} }{ dr_{r=R} } = \frac{-4Q}{\pi R^3} `

The resulting velocity gradient as function of average velocity for tube geometry is,

  :math:`\frac{ dv_{\alpha} }{ dy_{y=0} } = \frac{8v_{\alpha}}{D} `

2) Find the fluid velocity at the center of the floc:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Now, we want to determine the velocity at the center of the floc. For linearized plates, the plate geometry condition, we determined that,

:math:`\frac{ dv_{\alpha} }{ dy_{y=0} } = \frac{6 v_{\alpha}}{S} `

The center of the floc is approximately half of the floc diameter, :math:`D`. So, to find the fluid velocity at the center of the floc, we linearize the differential and plug in :math:`\frac{D}{2}` to yield,

 :math:`v_{\alpha} \approx (\frac{6 v_{\alpha}}{S}) (\frac{D}{2}) `

Substituting by the trigonometric relationship :math:`v_{\alpha} = (\frac{v_{P,V}}{sin\alpha})`, we find the fluid velocity at the center of the floc as,

 :math:`v_{\alpha} \approx \frac{3 v_{P,V} D}{Ssin\alpha} `

.. _figure_floc_rollup_step2:
.. figure:: Images/floc_rollup_step2.png
   :height: 100px
   :align: center
   :alt: Fluid velocity at the center of the floc.

   Fluid velocity at the center of the floc.

3) Find terminal velocity of the floc down the plate (for the case of zero velocity fluid):
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Recall from previous sections [[link]] that the terminal velocity, :math:`v_t`, of the floc can be calculated by, [[??]]

:math:`v_t = \frac{D_0^2g}{18\phi\nu}\frac{\rho_{floc} -\rho_{H2O}}{\rho_{H2O}} \left( \frac{D}{D_0} \right) ^{D_{fractal}-1}`

We can rearrange this equation to solve for :math:`D` by

:math:`D = D_0 ( \frac{18 v_t \phi \nu }{D_0^2g} \frac{ \rho_{H2O}}{ \rho_{floc} - \rho_{H2O}}) ^{\frac{1}{ D_{fractal} - 1}}`

We will need this equation for :math:`D` in the next step.

.. _figure_floc_rollup_step3:
.. figure:: Images/floc_rollup_step3.png
   :height: 100px
   :align: center
   :alt: Terminal velocity of the floc down the plate (for the case of zero velocity fluid).

   Terminal velocity of the floc down the plate (for the case of zero velocity fluid).

4) Set the fluid velocity at the center of the floc equal to the terminal velocity of the floc to find the critical case of no movement, and the required plate spacing:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The floc settles due to gravitational forces. First, the :math:`\alpha` component of the gravitational settling force, :math:`v_{t,\alpha}`, must be found by trigonometric relationships.

 :math:`v_{t,\alpha} = v_t sin\alpha`

Setting :math:`v_{\alpha} = v_{t,\alpha}` yields,

 :math:`\frac{3 v_{P,V} D}{Ssin\alpha} \approx v_t sin\alpha`

Solving for :math:`S` to determine plate spacing,

 :math:`S \approx \frac{3 v_{P,V} D}{v_t sin^2\alpha}`

In this equation, we have both :math:`v_t` and :math:`D`, but we can simplify further because we know that :math:`v_t` and :math:`D` are related by the relationship shown in step 3. Therefore,

:math:`S \approx \frac{3}{sin^2\alpha} \frac{v_{P,V}}{v_t} D_0 \left( \frac{18 v_t \phi \nu }{D_0^2g} \frac{ \rho_{H2O}}{ \rho_{floc} - \rho_{H2O}} \right) ^{\frac{1}{ D_{fractal} - 1}} `

:math:`S` is the smallest spacing that will allow a floc with a given settling velocity to remain stationary on the slope and not be carried upward by rollup.

5) Find the floc sedimentation velocity, :math:`v_{Slide}`:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Finally, we can determine :math:`v_{Slide}` by,

:math:`v_{Slide} = v_{P,V} \left[ \left( \frac{3D_0}{Ssin^2\alpha} \right)^{D_{fractal} - 1} \left( \frac{18 v_{P,V} \phi \nu }{D_0^2g} \frac{\rho_{H2O}}{\rho_{floc} - \rho_{H2O}} \right) \right] ^ {\frac{1}{ D_{fractal} - 2}} `

:math:`v_{Slide}` is the terminal sedimentation velocity of the slowest-settling floc that can slide down an incline. Flocs with with terminal velocity (the slide velocity) will be held stationary on the incline because of a balance between gravitational forces and fluid drag. Flocs with a terminal velocity lower than :math:`v_{Slide}` will be carried out of the top of the settler (i.e., they will rollup) even if they settle onto the settler wall. Thus, the slide terminal velocity represents a constraint on the ability of plate settlers to capture flocs.

What happens if the primary particles are less dense? [[need more explanation]]
:math:`v_{Slide}` will increase because the particles need to be able to settle faster in order to not experience rollup.


Head Loss through Plate Settlers
--------------------------------

Flow through the sedimentation tank is controlled by head loss in an attempt to achieve flow uniformity. We have already explained that plate settler spacing impacts head loss [[[[link]]]], but by what mathematical relationship? Will putting plate settlers closer together result in more or less head loss? This question is complicated because closer plate settlers would create more shear and head loss, but shorter plate settlers also mean that they become shorter which would decrease shear and head loss.

Let's start with a force balance. Assume that there is a fully established velocity profile that is parabolic with laminar flow. The forces that we care about are shear forces on the walls of the plate settlers and the differential pressure from flow in the direction of the velocity.

.. _figure_plate_settler_headloss_diag:
.. figure:: Images/plate_settler_headloss_diag.png
   :height: 100px
   :align: center
   :alt: Velocity, shear forces, and pressure loss through plate settlers.

   Velocity, shear forces, and pressure loss through plate settlers.

The shear forces act over the area of the two plates, resulting in :math:`F_{shear} = 2 \tau L W` where :math:`\tau` is the viscous shear component.

The pressure force is exerted over the entire width of the plate and the plate spacing. Pressure at the entrance of the plate settlers is different from the exit of the plate settlers by :math:`\Delta P`. The resulting pressure force is :math:`F_{pressure} = \Delta P W S`. So,

 :math:`F_{shear} = F_{pressure}`

 :math:`2 \tau L W = \Delta P W S `

Dividing both sides by width, :math:`W`, and solving for :math:`\Delta P` yields,

 :math:`\Delta P = \frac{2 \tau L}{S} `

We need to figure out what each of the terms on the right side of the equation is equal to so we can calculate :math:`\Delta P`. Ultimlately, we need :math:`\Delta P` to calculate head loss because :math:`h_L = \frac{\Delta P}{\rho g}`.

:math:`\tau =\mu \frac{du}{dy}`, where :math:`\tau` is shear, :math:`\mu` is the viscosity, and :math:`\frac{du}{dy}` is the velocity gradient. Using the Navier-Stokes equation, we can find the velocity gradient as a function of the average velocity between the plates, yielding shear based on the vertical velocity entering the plates as,

 :math:`\tau = \mu \frac{6 v_{P,V}}{S sin\alpha}`

:math:`L` is found using the equation for capture velocity, :math:`v_c = \frac{S*v_{P,V}}{Lsin\alpha cos\alpha + S}`. Capture velocity is kept constant so we solve for :math:`L`,

 :math:`L = \frac{S \left( \frac{v_{P,V}}{v_c} -1 \right)}{sin\alpha cos\alpha}`

Substituting :math:`\tau` and :math:`L` into the equation for :math:`\Delta P`,

 :math:`\Delta P = 2\mu \left( \frac{6v_{P,V}}{S sin^2 \alpha cos\alpha} \right) \left( \frac{v_{P,V}}{v_c} -1 \right)`

Now that we have an equation for :math:`\Delta P`, we can solve for head loss.

:math:`h_L = \frac{\Delta P}{\rho g}`

:math:`h_L = 2 \frac{\mu}{\rho g} \left( \frac{6v_{P,V}}{S sin^2 \alpha cos\alpha} \right) \left( \frac{v_{P,V}}{v_c} -1 \right)`

Recall that head loss through plate settlers is really small, on the order of micrometers, :math:`\mu m`. We are interested in understanding how the head loss relates to velocity, through the relation :math:`v = \sqrt{2gh}` [[help]]. The resulting two plots show how head loss and velocity relate to plate settlers.

.. _figure_plate_settler_headloss_spacing:
.. figure:: Images/plate_settler_headloss_spacing.png
   :height: 100px
   :align: center
   :alt: Head loss as a function of plate settler spacing.

   Head loss as a function of plate settler spacing.

Floc Blanket Design
========================================================

Floc Blanket Collision Potential
--------------------------------
We have learned that growing a floc blanket leads to better sedimentation tank performance. One explanation for the improved performance is that the floc blanket acts like an additional flocculator because there are additional collisions between particles. To understand the nature and significance of these additional collisions, we can calculate the floc blanket velocity gradients and residence time to find collision potential, :math:`G\theta`. In a floc blanket, we expect that :math:`G` is small; however, :math:`\theta` is large, which means that :math:`G\theta` in the floc blanket may be significant.

First, we will find :math:`\theta`. If we simplify the bottom of the sedimentation tank and approximate it as a simple rectangle, we can easily determine the residence time. If the depth of the floc blanket is 1 m and the upflow velocity is 1 mm/s, we determine that

:math:`\theta = 1000 s`

Next, we will find :math:`G`. Before we begin, consider why there is a velocity gradient in the floc blanket. What causes it? Water is flowing up through the floc blanket while the flocs in the floc blanket are being pulled down by gravity. The differential velocities are caused by particles settling and rising at different velocities relative to the fluid due to drag, gravity, and fluid flow. In the fluid around each particle, there is a velocity gradient and shear between the particles and the surrounding fluid.

Entering the sedimentation tank, there is a large range of particle sizes in the water. The range exists from big flocs made up with hundreds of millions of clay particles to primary particles that made it through flocculation without successful collision. These differentially sized particles create velocity gradients as the particles and flocs are acted on by both settling forces and upward fluid flow forces.

Large flocs provide velocity gradients that can potentially cause collisions between other small particles that we are still trying to capture. Through our derivation to determine :math:`G` in a floc blanket, we will also test an assumption. We will assume that primary particles coming into the floc blanket are not interacting with large flocs. Instead,  we will assume that the the fluid shear and differential velocities promote interactions between two primary particles.

So, how can we calculate the velocity gradient? In flocculators, we determined :math:`G` from head loss and residence time. In sedimentation tanks, we determine :math:`G` the same way. Let's calculate the head loss through the floc blanket. To do this, we need to know the density of the floc blanket and we need to know the relationship between head loss a fluidized bed and density of the bed.

Floc blanket density
^^^^^^^^^^^^^^^^^^^^
To calculate the density of the floc blanket at steady-state, we will use principles of mass and volume conservation.

:math:`C_{clay} = \frac{m_{clay}}{\rlap{-}V_{fb}}`

:math:`\rho = \frac{m_{TOT}}{\rlap{-}V}`

We will start by finding the mass of clay and the mass of water in the floc blanket, where:

| :math:`C_{clay} =` concentration of clay in the floc blanket
| :math:`\rlap{-}V_{fb} =` volume of floc blanket
| :math:`\rho_{clay} =` density of clay
| :math:`\rho_{H_2O} =` density of water
| :math:`\rho_{fb} =` density of floc blanket

The mass of clay in the floc blanket is concentration multiplied by volume, shown by :math:`m_{clay} = C_{clay}\rlap{-}V_{fb}`

The mass of water in the floc blanket is related to the volume fraction of the floc blanket that is occupied by clay, :math:`\frac{C_{clay}}{\rho_{clay}}`, whic is a very small number. :math:`\left( 1 - \frac{C_{clay}}{\rho_{clay}} \right)` is the fraction of the floc blanket that is occupied by water, also called the water volume fraction. So, :math:`m_{H_2O} = \left( 1 - \frac{C_{clay}}{\rho_{clay}} \right) \rho_{H_2O} \rlap{-}V_{fb}`.

Now, we know how much clay and water is in our system. The density of the system, neglecting the addition of coagulant, is,

 :math:`\rho_{fb} = \frac{m_{clay} + m_{H_2O}}{\rlap{-}V_{fb}}`

Substituting for :math:`m_{clay}` and :math:`m_{H_2O}`,

 :math:`\rho_{fb} = \left( 1 - \frac{C_{clay}}{\rho_{clay}} \right)\rho_{H_2O} + C_{clay}`

This can be rearranged to yield the following equation derived from first principles,

 :math:`\rho_{fb} = \left( 1 - \frac{\rho_{H_2O}}{\rho_{clay}} \right)C_{clay} + \rho_{H_2O}`

AguaClara researchers in the lab developed an empirical equation through experimental studies to calculate floc blanket density. They determined that,

:math:`\rho_{fb} = 0.687C_{clay} + \rho_{H_2O}`

Comparing the empirical equation to the one determined by first principles, it clear that the coefficient,

:math:`\left( 1 - \frac{\rho_{H_2O}}{\rho_{clay}} \right) = 0.687`

Floc blanket head loss
^^^^^^^^^^^^^^^^^^^^^^^

Now that we can calculate the density of the floc blanket, we can calculate the head loss through the floc blanket. This topic will be discussed further in the chapter on filtration. For now, all you need to know is that density can be related to head loss in the floc blanket through the height of the floc blanket, :math:`H_{fb}`, and the densities of the floc blanket and water.

:math:`\frac{h_L}{H_{fb}} = \frac{\rho_{fb} - \rho_{H_2O}}{\rho_{H_2O}} `

There will be a small amount of head loss through the floc blanket because the density of the floc blanket is greater than the density of water by only a little bit. Remember that :math:`\frac{C_{clay}}{\rho_{clay}}` is really just the fraction of the floc blanket that is occupied by clay.

Plugging in the equation for :math:`\rho_{fb}` and solving for :math:`h_L`,

 :math:`h_L = H_{fb} \left( \frac{\rho_{clay}}{\rho_{H_2O}} - 1 \right) \frac{C_{clay}}{\rho_{clay}}`

Floc blanket velocity gradient and collision potential
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

With the equation for :math:`h_L`, we can calculate :math:`G`. We will also use the other equations we developed in the chapter on flocculation [[[[link]]]].

 :math:`G = \sqrt{\frac{\epsilon}{\nu}}`

 :math:`\epsilon = \frac{gh_L}{\theta}`

We will start by determining :math:`\epsilon ` by calculating :math:`\theta` using the porosity of the floc blanket, :math:`\phi_{fb}`,

 :math:`\theta = \frac{H_{fb} \phi_{fb}}{v_{S,V}}`

Plugging :math:`\theta` into :math:`\epsilon` yields

 :math:`\epsilon = \frac{gv_{S,V}}{\phi_{fb}} \frac{h_L}{H_{fb}}`

Substituting into our equation for :math:`G`,

 :math:` G =  \sqrt{\frac{gv_{S,V}}{\nu \phi_{fb}} \frac{h_L}{H_{fb}}}`

Using our equation for :math:`h_L`,

 :math:` G =  \sqrt{\frac{gv_{S,V}}{\nu \phi_{fb}} \left( \frac{1}{\rho_{H_2O}} - \frac{1}{\rho_{clay}} \right) C_{clay} }`

 :math:`\phi_{fb} \approx 1` and is a function of :math:`C_{clay}`

We can plot our results for :math:`G` over a range of typical floc blanket concentrations, which is around 1 - 5 g/L. [[[[plot]]]] We find that :math:`G` ranges from 2 to 6 Hz. Recall that for flocculator design, we get anywhere from 70 to several hundred Hz. The :math:`G` provided by the floc blanket is much smaller than :math:`G` provided by the flocculator. This is an important point because in the low :math:`G` environment of the floc blanket where there are low levels of energy dissipation, we can grow larger flocs. The flocs are experiencing less shear so they can grow close to millimeter size.

We can plot our results for :math:`G\theta` by multiplying :math:`G` by the residence time we found earlier, :math:`\theta = 1000 s`. The result is that :math:`G\theta` ranges from 2,000 to 6,000. Compare this to the :math:`G\theta = 20,000` for the flocculator used in experiments [[[[Garland]]]].

.. _figure_lab_setup:
.. figure:: Images/lab_setup.png
   :height: 100px
   :align: center
   :alt: Lab setup for flocculator, half-sedimentation tank, and plate settler testing.

   Lab setup for flocculator, half-sedimentation tank, and plate settler testing.

.. _figure_floc_conc_G:
.. figure:: Images/floc_conc_G.png
   :height: 100px
   :align: center
   :alt: Velocity gradient and collision potential as a function of floc blanket concentration.

   Velocity gradient and collision potential as a function of floc blanket concentration.

How does such a small :math:`G\theta` cause such a large reduction in turbidity? The question we are really asking is, is there anything special about the :math:`G\theta` provided by the floc blanket compared to the :math:`G\theta` provided by the flocculator? If so, what is the difference and why is it so beneficial?

Experimental data helps explain this. Two systems were set up: one had a flocculator where :math:`G\theta = 20,000` with a floc blanket where :math:`G\theta = 4,000`; the other just had a flocculator where :math:`G\theta = 24,000`. Using the same influent water quality and coagulant dosing, we find that the first system with the flocculator and floc blanket performed better than the second system, even though the overall :math:`G\theta` values were the same.

To understand this, we have to review assumptions in the derivation for :math:`G`. Recall our assumption that fluid shear promotes the collision of two primary particles instead of the collision of primary particles with existing, large flocs. If our assumption was true, we would expect to see no difference between our two experimental setups. However, because we know that the two experimental setups did have different results, our assumption must be false because the assumption does not explain or account for these differences. There must be another mechanism occuring to explain why the floc blanket greatly improves treatment quality. This leads us to believe that the flocs in the floc blanket must be more involved than simply providing shear and velocity gradients; they must be involved in some collisions with the small particles coming through the floc blanket.

This highlights an important distinction:

#. The model created by the original derivation assumption would suggests that flocs in the floc blanket are inert - simply occupying space and causing there to be head loss in the floc blanket - without being involved in any collisions. This model is disproved through the experimental analysis of the two experimental setups.
#. The model created after the analysis of experimental results suggests that flocs in the floc blanket are not inert - they are involved in collisions with small particles entering the floc blanket - and are growing in size. The model is supported through the experimental analysis.

Diffuser Design
======================

Diffusers are shaped so that they remain a circular pipe in one end that fits into the influent manifold orifice, and the other end is deformed to the shape of a thin rectangle. Recall that this deformation is done to create a line jet entering the jet reverser in the bottom of the sedimentation tank. Diffusers are shaped by dipping the pipe stubs in hot oil, and then pushing the maleable and heated pipe onto a metal form. This metal form is sized so that the target shape is achieved.

.. _figure_BvsS_diffuser:
.. figure:: Images/BvsS_diffuser.png
    :height: 100px
    :align: center
    :alt: Diagram of diffuser exit.

    Diagram of diffuser exit.

| :math:`T_{diff} =` thickness of diffuser wall
| :math:`S_{diff} =` internal width of diffuser
| :math:`B_{diff} =` center-to-center spacing between diffusers; external width of diffuser
| :math:`W_{diff} =` internal width of diffuser
| :math:`v_{jet} =` velocity of the jet exiting the diffuser
| :math:`Q_{diff} =` flow rate through each diffuser
| :math:`h_{L,jet} =` head loss in jet leaving the jet reverser

Determining flow through a diffuser
-----------------------------------

What is the flow rate of a single diffuser in the bottom of the sedimentation tank? Consider a sedimentation tank that is 6 m long, 1 m wide and 2 m deep, with an upflow velocity of 1 mm/s and a diffuser spacing of 5 cm.

 What is this question really asking? This question is asking us to understand that each diffuser "serves" a specific cross-sectional area of the sedimentation tank; all of the diffusers together serve the entire area of the sedimentation tank. So, let's imagine a single diffuser serving a slice of a sedimentation tank. With this in mind, we can easily solve this using :math:`Q = vA`. The area, :math:`A`, is the slice of the sedimentation tank that we are serving. We are told that the tank is 1 m wide, so :math:`W_{tank} = 1` m. The length of the slice is dictated by the spacing of the diffusers, :math:`B_{diff}`, so :math:`B_{diff} = 5` cm.

  :math:`A = B_{diff}W_{tank}`

  :math:`A = 5cm * 1m`

  :math:`A = 50,000mm^2`

 The problem statement includes that :math:`v_{S,V} = 1` mm/s. Plugging into our flow equation,

  :math:`Q_{diff} = v_{S,V}A `

  :math:`Q_{diff} = (1 \frac{mm}{s})(50,000mm^2)`

  :math:`Q_{diff} = 50,000 \frac{mm^3}{s}`

  :math:`Q_{diff} = 50 \frac{mL}{s}`

 The flow rate of each diffuser is :math:`50 \frac{mL}{s}`.

Properties of :math:`v_{jet}`
-------------------------------
:math:`v_{jet}` is defined as the velocity of the water jet exiting the diffuser. After exiting the diffuser, this water jet is sent into the jet reverser to make a 180 degree turn. Does the water jet change pressure or velocity as it exits the jet reverser? Do we need to consider the effects of a *vena contracta*?

Recall that a *vena contracta* is associated with a change in pressure that causes a contraction and subsequent acceleration of the fluid [[[[link to fluids review]]]]. Water exiting the diffuser is pointed directly down and the streamlines are straight and parallel, which means that the pressure across the streamlines is constant. Water exiting the jet reverser is pointed directly up and the streamlines are straight and parallel, which again means that the pressure across the streamlines is constant. Because the pressure is constant at the exit of the diffuser and at the exit of the jet reverser, we assume that the pressure of the water in the space between those two points is also constant because there is no physical barrier. If the pressure in this bottom section of the sedimentation tank is constant from the exit of the diffuser to the exit of the jet reverser, we can infer that they are equal.

By Bernoulli, if the pressures between the exit of the diffuser to the exit of the jet reverser are equal then the velocities must also be equal. Bernoulli is applicable here because there is no flow expansion yet. The shear along the wall of the jet reverser is insignificant due to the short flow path. The water accelerates to account for the directional change but the absolute velocity does not change as it goes around the jet reverser.

.. _figure_Wdiff_Wjet:
.. figure:: Images/Wdiff_Wjet.png
    :height: 100px
    :align: center
    :alt: Diagram of diffuser exit and jet.

    Diagram of diffuser exit and jet.

Therefore, the velocity at the exit of the diffuser is equal to the velocity at the exit of the jet reverser.

Diffuser Design
---------------------

What is the target shape of the diffuser? We know that the diffuser must be sized so that our velocity constraints will be achieved. The minimum velocity constraint comes from the need to keep flocs resuspended. We also know that in the active region of our sedimentation tank, we want an upflow velocity of 1 mm/s. Additionally, because diffusers are a key component of our "sedimentation tank as a circuit", we want to precisely control head loss in the jet leaving the jet reverser because that will help us achieve uniform flow within and between sedimentation tanks. AguaClara designs set head loss in the jet constant at 1 cm.

Let's begin by finding the internal width of a single diffuser. Using conservation of flow, we know that,

:math:`Q_{diff} = v_{jet}W_{diff}S_{diff} = v_{S,V}W_{Sed}B_{diff}`

Solving for :math:`W_{diff}`,

 :math:`W_{diff} = \frac{v_{S,V}W_{Sed}B_{diff}}{v_{jet}S_{diff}}`

Using the constraint of head loss in the jet and solving for :math:`v_{jet}`,

 :math:`h_{L,jet} = \frac{v_{jet}^2}{2g}`

 :math:`v_{jet} = \sqrt{2gh_{L,jet}}`

Substituting back into the equation for :math:`W_{diff}`, we can find the minimum diffuser width required to not exceed target head loss as,

:math:`W_{diff,min} = \frac{v_{S,V}W_{Sed}B_{diff}}{(\sqrt{2gh_{L,jet}})S_{diff}}`

Now that we have determined the minimum width, we can use known parameters and constraints to find a precise value for :math:`W_{diff}` and :math:`v_{jet}`.

Using known constants for :math:`v_{S,V} = 1 \frac{mm}{s}`, :math:`h_{L,jet} = 1 cm`, and :math:`W_{Sed} = 1m`, we can find that :math:`W_{diff,min} = 2.7mm`. The mold used to create diffusers in Honduras comes in sizes of 1/8 in, or 3.175 mm, so to find :math:`W_{diff}` we round up to 3.175 mm.

:math:`W_{diff} = 3.175 mm`

Solving for :math:`v_{jet}` from our earlier equations yields,

:math:`v_{jet} = \frac{v_{S,V}W_{Sed}B_{diff}}{W_{diff}S_{diff}}`

Using known constants,

:math:`v_{jet} \approx 380 \frac{mm}{s}`


*******************************************************
Sedimentation Challenges, Confusions, and Failure Modes
*******************************************************

Unsolved sedimentation tank failure modes:

#. Floc volcanoes and temperature-induced flow circulations [[[[link]]]]
#. Dissolved air flotation that results from air coming out of solution. Two sources of air include 1) compressed air traveling from the transmission line and 2) increased temperature which releases dissolved air.
#. Slime growth from iron-oxidizing bacteria.
#. NOM impact on floc density
