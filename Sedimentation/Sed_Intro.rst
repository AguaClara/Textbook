.. _title_Sedimentation_Intro:

***************************************
Sedimentation Introduction
***************************************

.. _Sedimentation Unit Process Overview:

Sedimentation is a gravity-driven unit process in which suspended flocs are settled out from water. Large flocs made up of many primary particles and coagulant will settle if given enough time. Sedimentation is commonly preceded by coagulation/flocculation processes - coagulation/flocculation aim to form flocs which will be large enough to settle in sedimentation - and is commonly followed by filtration processes for further treatment. Sludge consolidation processes are often present alongside sedimentation to reduce the waste stream of settled flocs. Optimizing sedimentation is important because the more particles that sedimentation can remove, the fewer particles the filter will have to remove. This is good because filters can only handle a small amount of solids, and cleaning the filters with backwash uses a lot of water so we want to reduce the number of backwashes. The goal of sedimentation is to concentrate a waste stream of flocs, or sludge.

To introduce you to sedimentation, we will begin with a simple example. If a jar of water filled with flocs was left at rest, flocs would begin to settle due to gravitational forces pulling them down. Large flocs would settle first, but if left for long enough, all flocs would settle to the bottom of the jar. In its most basic form, the jar represents a sedimentation tank in which flocculated water is treated. Settled flocs are waste and the water on the top of the jar, referred to as the supernatant, is the settled water.

Constraints of space, time, and cost make it important to optimize the settling process. It would not be realistic to design water treatment systems that use the basic jar-like system to settle flocs because large flow rates would require unreasonably large reactor volumes and long retention times. The goal of sedimentation reactor design is to employ geometries that promote settling and allow for fast treatment with small footprints.

What if we were to do the same jar experiment with raw water that did not go through successful coagulation and flocculation? Would we observe the same settling and successful particle removal? To answer this, we must recall information learned in the section on coagulation and flocculation; those two treatment processes serve to destabilize and agglomerate particles to form flocs that will be heavy enough to settle. If the particles are colloids and are not destabilized, no amount of time will allow for the settling. This emphasizes the fact that successful sedimentation can only happen with successful coagulation and flocculation steps before it.

The three main steps that need to be accomplished for a sedimentation system to be successful are as follows:

1) Suspended flocs need to be able to settle out of the water.
2) Settling flocs need to be able to move from wherever they settle to a lower section of the tank.
3) Accumulated flocs at the bottom of the tank need to be removed.

Sedimentation is ubiquitous in water treatment. Nevertheless, the process is very complex with many failure modes and there are many active research areas. The following sections will explore the state of conventional sedimentation systems and their challenges, gaps in knowledge, and the AguaClara approach to sedimentation.

To understand how sedimentation works, a few key concepts must first be developed. This includes understanding how and why flocs move in water. Remember, the goal of sedimentation reactor design is to optimize the floc-settling process.

Terminal Velocity
===============================
As flocs settle in water, they will fall at a speed dictated by the weight of the floc, the buoyancy of the floc, and drag from the water. These three forces - the gravitational weight force, the buoyant force, and the drag force - dictate the speed at which a floc falls and are detailed in the free body diagram of :numref:`figure_terminal_velocity_FBD`. We care about determining the speed at which flocs will fall because knowing this information will help inform our sedimentation reactor design criteria.

.. _figure_terminal_velocity_FBD:

.. figure:: Images/terminal_velocity_FBD.png
    :height: 300px
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

  F_{buoyant} = \rlap{--}V_{floc} \rho_{H_2O} g

  W_{floc} = \rlap{--}V_{floc} \rho_{floc} g

| Where:
| :math:`\rlap{--}V_{floc} =` floc particle volume
| :math:`A_{floc} =` particle projected cross-sectional area
| :math:`\rho_{floc} =` particle density
| :math:`\rho_{H_2O} =` water density
| :math:`g =` acceleration due to gravity
| :math:`C_D =` drag coefficient
| :math:`v_t=` particle terminal velocity
| :math:`D=` particle diameter

Plugging into the original force balance,

.. math::

  \left [C_D A_{floc} \rho_{H_2O} \frac{v_t^2}{2} \right]+\left [\rlap{--}V_{floc} \rho_{H_2O} g\right ]-\left [\rlap{--}V_{floc} \rho_{floc} g \right] =0

Solving for terminal velocity, :math:`v_t`, provides

.. math::

  v_t = \sqrt{\frac{4}{3}\frac{gD}{C_D}\frac{(\rho_{floc}-\rho_{H_2O})}{\rho_{H_2O}}}

Terminal velocity is a function of fluid density, floc density, gravity, particle diameter, and the drag coefficient. To calculate velocity, all of those inputs must be determined.

The first component that we will focus on is the drag coefficient, :math:`C_D`. The drag coefficient is function of Reynolds Number, :math:`Re`, and the characteristic flow around a particle. As a reminder, :math:`Re = \frac{v_t D}{\nu}` where :math:`v_t` is the velocity of the fluid relative to the particle, :math:`D` is the characteristic length scale (in this case the particle diameter), and :math:`\nu` is kinematic viscosity.

Drag coefficients are used to describe flow around a particle and are shown in :numref:`figure_drag_coeff_Re_base`.

.. _figure_drag_coeff_Re_base:

.. figure:: Images/drag_coeff_Re_base.png
    :height: 300px
    :align: center
    :alt: Drag coefficient as a function of Reynolds number.

    Drag coefficient as a function of Reynolds number.

As an introduction to this drag coefficient diagram, we can compare it to something we've already learned about: the Moody diagram. Drawing parallels between the two will help us understand some important relationships better.

.. _table_Moody_DragCoefficient:

.. csv-table:: Comparison of the Moody diagram and the Drag Coefficient diagram.
   :header: "Characteristic", "Moody Diagram", "Drag Coefficient Diagram"
   :align: left

   Relationship to Reynolds number, "friction factor, :math:`f`", "drag coefficient, :math:`C_D`"
   Type of head loss, major losses as shear force on pipe walls, shear on sphere and pressure drag from wake
   Laminar region, ":math:`f = \frac{64}{Re}`", :math:`C_D = \frac{24}{Re}`
   "High Reynolds number (:math:`f`, :math:`C_D`)", ":math:`f` remains constant", ":math:`C_D` remains constant"
   "High Reynolds number (:math:`h_L`, :math:`F_{drag}`)", :math:`h_L = \frac{fL\bar v^2}{2Dg}`,:math:`F_{drag} = C_D A_{floc} \rho_{H_2O} \frac{v_t^2}{2}`


The flow around the particle and the Reynolds Number can be described in the laminar, turbulent, or turbulent-boundary regions as shown in :numref:`figure_drag_coeff_Re_full`. In the laminar region viscous forces dominate, :math:`Re < 1`,and the coefficient of drag is represented as the straight line with a slope of -1 on the log-log plot. The equation for drag on a sphere in laminar flow :math:`C_D = \frac{24}{Re}` is referred to as Stokes Law. You'll notice that the line for Stokes Law shown in the figure extends past the laminar region. This was done because it highlights that even though Stokes Law is not exactly correct past the turbulent region, it is still a pretty good approximation for  :math:`Re < 10`.

.. _figure_drag_coeff_Re_full:

.. figure:: Images/drag_coeff_Re_full.png
    :height: 300px
    :align: center
    :alt: Drag coefficient as a function of Reynolds number.

    Drag coefficient as a function of Reynolds number.

Note that the coefficient of drag in the transition region is an important parameter to understand. Equations for the coefficient of drag are explored in the paper by `Yang et al. in "General formulas for drag coefficient and settling velocity of sphere based on theoretical law" <https://www.sciencedirect.com/science/article/pii/S2095268615000178>`_. They have determined that Oseen law based formulas are recommended for use.

Let's consider the drag coefficient diagram at Reynolds numbers of :math:`10^5`. We notice that there is a "bump" in the plot, in which the drag coefficients drop. This is because at really high Reynolds numbers, the boundary layer around the particle became turbulent. This causes the wake behind the particle to be a little smaller, leading to a slight reduction in drag. The drag coefficient decreases, but the total drag force does not necessarily decrease (and likely keeps on increasing).

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

  v_t = \frac{D^2g}{18\nu}\frac{\rho_{floc} -\rho_{H_2O}}{\rho_{H_2O}}

Again, we can draw a parallel with the Moody Diagram. The general form of the terminal velocity equation is like the Darcy-Weisbach equation; it is always true. The terminal velocity in the laminar flow region is like the Hagen-Poiselle equation; it is only good for laminar flow. We will use the laminar specific condition because we are working with flocs with low Reynolds numbers.

Our equations for terminal velocity depend on the density of a floc. As discussed in previous sections, we know that there is a specific relationship between the density of a floc and the diameter of a floc because flocs are fractals and as flocs get bigger, their density gets lower. We can account for the size and density relationship by modifying the terminal velocity equation.

.. _heading_terminal_velocity_equation:

.. math::

  v_t = \frac{D_0^2g}{18\phi\nu}\frac{\rho_{floc_0} -\rho_{H_2O}}{\rho_{H_2O}} \left( \frac{D}{D_0} \right) ^{D_{fractal}-1}

| Where:
| :math:`D_0 =` diameter of clay
| :math:`D_{fractal} =` fractal dimension
| :math:`D =` floc diameter
| :math:`\rho_{floc_0} =` density of the primary particle making up the floc

The following plot in :numref:`figure_terminal_velocity_floc_diam` shows the relationship between floc diameter and terminal velocity.

.. _figure_terminal_velocity_floc_diam:

.. figure:: Images/terminal_velocity_floc_diam.png
    :height: 300px
    :align: center
    :alt: Terminal velocity as a function of floc diameter, taking into account the changing density of flocs formed from clay.

    Terminal velocity as a function of floc diameter, taking into account the changing density of flocs.

Three important regions are highlighted in the plot. At small floc diameters, less than 10 :math:`\mu m`, terminal velocity is less that 0.1 :math:`\frac{mm}{s}`. A terminal velocity this low would require extremely large sedimentation tanks for reasonable treatment. Because large sedimentation tanks are costly and unfeasible, we use flocculation to aggregate particles and achieve floc sizes of greater diameters and higher terminal velocities.

For floc diameters around 35 :math:`\mu m`, the terminal velocity is about 0.12 :math:`\frac{mm}{s}`. AguaClara plate settlers are designed to settle out flocs of this size (particles dropping at 0.12 :math:`\frac{mm}{s}`) so the smallest floc that we can capture is 35 :math:`\mu m`. This will be explored in more detail during the discussion on :ref:`capture velocity <heading_capture_velocity>`.

Flocs with large diameters around 200 :math:`\mu m` have a terminal velocity of about 1 :math:`\frac{mm}{s}`. In our sedimentation tanks, which are upflow sedimentation tanks, we have water flowing up at about 1 :math:`\frac{mm}{s}` to capture a 200 :math:`\mu m` floc. These flocs are clearly visible but are small.

Our understanding of floc terminal velocity suggests that we can decide the size of the floc that we want our sedimentation tank to capture. If we decide that we want to capture flocs that are 35 :math:`\mu m` or larger, we know that we must design for water flowing at 0.12 :math:`\frac{mm}{s}`. Alternatively, we know that if we design a reactor in which water flows at 1 :math:`\frac{mm}{s}`, we will only be able to capture flocs that are 200 :math:`\mu m` or larger.

.. _heading_capture_velocity:

Capture Velocity
===============================
Settle capture velocity is defined as the velocity of the slowest settling particle that a sedimentation tank captures reliably. It is a property of the geometry of the sedimentation tank. Because it is a property of geometry, we can use it as an important design tool; because we can control reactor geometry, we can control the sizes of particles that we can settle. However, the size of particles that a sedimentation tank can capture is also a function of the viscosity of the water and thus is influenced by temperature.

Note that there are a couple of different terms used to describe the sedimentation process. We can say that sedimentation tanks "capture" particles when particles settled. We can also say that sedimentation tanks "remove" particles. Both terms refer to the process of particles or floc settling out of suspension in water. Sedimentation tanks separate some particles from the water and eventually divert those captured particles into a waste stream.

We will develop our definition of settle capture velocity using examples of horizontal flow and vertical flow sedimentation tanks. It should be noted that there are many idealizations and simplifications made for modeling sedimentation tanks. We assume that water will move through the reactor as expected (in the case of the horizontal flow sedimentation tank, from one end to the other), but we know that there are many more fluids complications than are described here. We assume that everything is moving at the average velocity and there are no turbulence or velocity profiles. For the time being, we will ignore what will happen to particles once they are captured by the sedimentation tank. Our intuition tells us that particles which settle will need to be removed somehow, and that is correct. For now, we only care about capturing the particles, and later we will care about what we do with them once they are captured.

Temperature plays an important role in sedimentation processes. Colder temperatures mean more viscous fluid; particles suspended in viscous fluid don't fall as quickly as they would in warmer, less viscous fluid. Sedimentation tanks don't work as well in cold temperatures as they do in warm temperatures. If the goal is for the sedimentation tank to remove a certain size of particle, then the required capture velocity must also be a function of temperature. Keep this in mind throughout the chapter as you learn how capture velocity drives to plant design.

Horizontal Flow Sedimentation Tank
----------------------------------

.. _figure_horizontal_flow_tank_base:

.. figure:: Images/horizontal_flow_tank_base.png
    :height: 300px
    :align: center
    :alt: Horizontal flow sedimentation tank.

    Horizontal flow sedimentation tank.

| Where:
| :math:`L =` length [L]
| :math:`W =` width [L]
| :math:`H =` height [L]
| :math:`A_p =` plan view area of the tank [:math:`L^2`]

Let's begin with a few questions that will describe our horizontal flow sedimentation tank in :numref:`figure_horizontal_flow_tank_base`. We will assume that 1) water travels uniformly from one end of the tank to the other, and 2) the particle that we are discussing is 35 :math:`\mu m` (which is the size of particle that AguaClara plate settlers can capture).

1) How much time is required for water to pass through the tank?

To determine this value, we can use the given volume and flow rate information by the following relationship:

.. math::

  \theta = \frac{\rlap{--}V_{tank}}{Q}

| Where:
| :math:`\theta =` residence time :math:`[T]`
| :math:`\rlap{--}V_{tank} =` volume of the sedimentation tank :math:`\left[L^3\right]`
| :math:`Q =` flow rate through the tank :math:`\left[\frac{L^3}{T}\right]`

2) In the "worst case scenario", how far must a particle fall to reach the bottom of the tank?

The "worst case scenario" is the condition in which a particle must travel the furthest in order to be successfully captured by the sedimentation tank. We assume that particles are evenly distributed throughout the height and width of the reactor entrance. Therefore, a particle entering at the top of the entrance of the reactor would need to fall a distance of :math:`H` to reach the bottom. Any particle entering from a position lower than the top of the tank would need to fall a distance :math:`< H`. We refer to the "worst case scenario" pathway as the "critical path" of the particle in the sedimentation tank design because this is the case which we must design to treat. The height that the particle must fall is called the "critical height", :math:`H_c`.

3) How fast must the particle fall?

We know that for a particle to fall to the bottom successfully, it needs to fall fast enough that it can reach the bottom before the water that is carrying it leaves the reactor. Water is carrying the particle across the reactor at the horizontal velocity speed, :math:`v_H`. Gravity is causing the particle to settle at its terminal velocity, :math:`v_t`. In order to reach the bottom, that settling velocity needs to be the capture velocity, :math:`\bar v_c`, to ensure that the particle will reach the bottom of the reactor. We can see the critical path of the particle in :numref:`figure_horizontal_flow_tank_capture`.

.. _figure_horizontal_flow_tank_capture:

.. figure:: Images/horizontal_flow_tank_capture.png
    :height: 300px
    :align: center
    :alt: Horizontal flow sedimentation tank with capture velocity.

    Horizontal flow sedimentation tank with capture velocity.


Capture velocity can be determined by the distance that a particle must travel and the time that the particle has to travel.

.. math::

  \bar v_c = \frac{H}{\theta}

We can make some substitutions into the equation for :math:`\bar v_c` to solve for it in explicit terms of reactor plan view area. We are interested in plan view area because this will indicate the efficiency and cost of an associated reactor.

.. math::

  \bar v_c = \frac{H}{\theta} = \frac{HQ}{\rlap{--}V_{tank}} = \frac{Q}{LW} = \frac{Q}{A_p}

  \bar v_c = \frac{Q}{A_p}

Thus, we have capture velocity which is a descriptor of a sedimentation tank. It determines how fast a particle has to settle in order to be reliably captured by a particular sedimentation tank, assuming idealized flow. The capture velocity is not a particle property, but rather a sedimentation tank property.

4) Will any particles that are smaller than 35 :math:`\mu m` be captured in the sedimentation tank?

This question is important because as stated in the beginning of this section, our discussion assumed that the particle in question was 35 :math:`\mu m`. If we design a sedimentation tank to capture particles that are 35 :math:`\mu m`, we also have to understand the impact of our design on particles smaller than 35 :math:`\mu m`.

To answer this question, think about the two extremes of our reactor.

- We could have a small particle entering the reactor at the top, defining the critical path in the same "worst case scenario". This particle would not be successfully captured by the tank because its terminal velocity is less than the capture velocity, meaning that it doesn't have enough time in the reactor to settle.
- We could have a small particle entering the reactor near the bottom, in a "best case scenario". In this case, the particle does not have a large distance to fall because it is already close to the bottom of the tank. Small particles entering the reactor may be able to be captured by a tank designed for particles 35 :math:`\mu m` or larger, but it depends on the height at which they enter the reactor as shown in :numref:`figure_horizontal_flow_tank_small_capture`.

.. _figure_horizontal_flow_tank_small_capture:

.. figure:: Images/horizontal_flow_tank_small_capture.png
    :height: 300px
    :align: center
    :alt: Horizontal flow sedimentation tank with critical path and small particle.

    Horizontal flow sedimentation tank with critical path and small particle.

Vertical Flow Sedimentation Tank
----------------------------------
We will complete the same exercise for vertical flow sedimentation tanks shown in :numref:`figure_vertical_flow_tank_base`. In vertical flow sedimentation tanks, water flows up from the bottom of the reactor and exits near the top of the reactor.

.. _figure_vertical_flow_tank_base:

.. figure:: Images/vertical_flow_tank_base.png
    :height: 500px
    :align: center
    :alt: Vertical flow sedimentation tank.

    Vertical flow sedimentation tank.

1) How much time is required for water to pass through the tank?

The answer is the same for the horizontal flow sedimentation tank because this is a property of reactor flow rate and volume.

.. math::

  \theta = \frac{\rlap{--}V_{tank}}{Q}

| Where:
| :math:`\theta =` residence time [T]
| :math:`\rlap{--}V_{tank} =` volume of the sedimentation tank [:math:`L^3`]
| :math:`Q =` flow rate through the tank [:math:`\frac{L^3}{T}`]

2) How far must a particle fall relative to the fluid to not be carried out the exit?

Note how this question is different from the question we asked for the horizontal flow sedimentation tank. In the horizontal flow sedimentation tank, particles could settle to the bottom of the reactor. We care about particles settling to the bottom because we assume that if particles hit the bottom of the reactor, then they would be captured and would not leave the reactor. Remember, the goal of sedimentation is to remove particles from suspension in water. In the vertical flow sedimentation tank, we also want to remove particles from suspension, but because there is a different geometry, we are now interested in the relative movement of particle to water. If a particle is falling due to the forces of gravity, but also water is pushing up on it, the only way for a particle to remain in the reactor is if it either falls at the same velocity or faster than the water is pushing it.

If a particle is falling at the same velocity that water is moving it, it will be stationary in the reactor. Water flowing through the reactor moves a distance :math:`H` in time :math:`\theta`, which means that a stationary particle must settle the same distance :math:`H` in the same time :math:`\theta`. Therefore, the answer is :math:`H`.

3) How fast must the particle fall (relative to the fluid)?

We determined in the previous question that a particle must fall a distance :math:`H` in time :math:`\theta`. Therefore, we determine the same capture velocity for vertical flow sedimentation tanks as for horizontal flow sedimentation tanks.

.. math::

  \bar v_c = \frac{H}{\theta}

We can the same substitutions to show,

.. math::

  \bar v_c = \frac{H}{\theta} = \frac{HQ}{\rlap{--}V_{tank}} = \frac{Q}{LW} = \frac{Q}{A_p}

Again, we find that capture velocity is,

.. math::

  \bar v_c = \frac{Q}{A_p}

It doesn't matter whether water is flowing horizontally or vertically in the tank. What determines the capture velocity is the flow rate and the plan view area of the sedimentation tank.

4) Will any particles that are smaller than 35 :math:`\mu m` be captured in the sedimentation tank?

This question is surprisingly complex because we have to consider what we have learned so far about sedimentation and also recall what we have learned about flocculation.

Let's start with the simple sedimentation approach. We can compare the vertical flow sedimentation tank with the horizontal flow sedimentation tank. In a horizontal flow tank, the capture of particles smaller than the design particle (35 :math:`\mu m`) is possible depending on the height which the particle enters the reactor. In a vertical flow tank, all particles enter the reactor at the same height (which is the bottom of the tank). This means that any particle entering the reactor will need to fall the same distance :math:`H` in time :math:`\theta` relative to the water if it will be captured. If particles smaller than 35 :math:`\mu m` enter the reactor, they will not be captured because they are not able to settle fast enough.

However, we must also consider potential flocculation processes that could occur in the sedimentation tank. A sedimentation tank is still subject to the same laws of fluids as the flocculator, meaning that there will still be shear in the reactor. While it may not be as much shear as that introduced in the flocculator, there are still velocity gradients which mean that there could be some additional flocculation happening in the sedimentation tank. In the flocculator, the main mechanism that led to flocculation was the deformation of fluid which caused particles to collide. In the sedimentation tank, the main mechanism that can lead to flocculation is velocity gradients. Flocculation is provided by an opportunity for collision by differences in relative velocities of particles. Big particles in the sedimentation tank settle out but are still in suspension, and small particles continue to move up through the large particles. There is relative velocity between particles based on their terminal velocities.

Understanding relative velocities is very important to understand how vertical flow sedimentation tanks work. Let's consider an example to develop our understanding of differential sedimentation. Imagine that two people are skydiving; one person is 150 lbs and the other person is 300 lbs. Assume that both people are using the same size parachutes and are jumping out of the same stationary helicopter. If the 150 lb person jumps out first and the 300 lb person jumps out a few moments after, what will happen? The 300 lb person will fall faster than the 150 lb person, causing a collision in the air. In a sedimentation tank, we would describe the collision due to differential sedimentation as flocculation because particles are colliding and growing.

Now that we understand differential settling and the potential for flocculation in a sedimentation tank, let's revisit the original question. Can smaller particles be captured? The answer is that smaller particles can be captured only if they collide with other particles and grow so that they have a terminal velocity that is greater than the capture velocity. This flocculation that happens in the sedimentation tank is an additional mechanism for removing particles.

There are some important differences between horizontal and vertical sedimentation tanks. Many of these points will be discussed next when we learn specifically about the :ref:`AguaClara design process <heading_Sed_Design>`, but it is important to get introduced to these ideas now:

- vertical flow tanks require careful attention to the delivery of water in the bottom of the tank and the extraction of water in the top of the tank;
- vertical and horizontal flow tanks may have different velocities and turbulence capacities due to plan view areas;
- research on tube settlers by `Brentwood Industries <https://www.brentwoodindustries.com/water-wastewater-products/tube-settlers/>`_ suggests that settle capture velocities should be 0.12 - 0.36 mm/s;
- research on horizontal flow tanks in *Surface Water Treatment for Communities in Developing Countries* by Schulz and Okun suggests that settle capture velocities should be 0.24 - 0.72 mm/s.

With this understanding of the basic principles of sedimentation, we will transition to a discussion of AguaClara innovations.

References
============

Schulz, C. R., Okun, D. A., & Water and Sanitation for Health Project (U.S.). (1984). Surface water treatment for communities in developing countries. New York: Wiley.

Comments, Corrections, or Questions
====================================

This textbook is an ever-evolving project. If you find any errors while you are reading, or if you find something unclear, please let the authors know. Write your comment in `this Github issue <https://github.com/AguaClara/Textbook/issues/83>`_ and it will be addressed as soon as possible. Please look at other comments before writing your own to avoid duplicate comments.
