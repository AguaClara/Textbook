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

The "worst case scenario" is the condition in which a particle must travel the furthest in order to be successfully captured by the sedimentation tank. We assume that particles are evenly distributed throughout the height and width of the reactor entrance. Therefore, a particle entering at the top of the entrance of the reactor would need to fall a distance of :math:`H` to reach the bottom. Any particle entering from a position lower than the top of the tank would need to fall a distance :math:`< H`.

3) How fast must the particle fall?

We know that for a particle to fall to the bottom successfully, it needs to fall fast enough that it can reach the bottom before the water that is carrying it leaves the reactor. Water is carrying the particle across the reactor at the horizontal velocity speed, :math:`V_h`. gravity is causing the particle to settle at its terminal velocity, :math:`V_t`. In order to reach the bottom, that settling velocity needs to be the capture velocity, :math:`V_c`, to ensure that the particle will reach the bottom of the reactor. We can see the path that the "worst case scenario" particle will take in the following figure.

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

- We could have a small particle entering the reactor at the top, in the same "worst case scenario". This particle would not be successfully captured by the tank because its terminal velocity is less than the capture velocity, meaning that it doesn't have enough time in the reactor to settle.
- We could have a small particle entering the reactor near the bottom, in a "best case scenario". In this case, the particle does not have a large distance to fall because it is already close to the bottom of the tank. Small particles entering the reactor may be able to be caputured by a tank designed for particles 35 :math:`\mu m` or larger, but it depends on the height at which they enter the reactor.

[[[[[[[[[show horizontal flow sedimentation tank with capture velocity for small particles compared to the 35 um condition]]]]]]]]]

Vertical Flow Sedimentation Tank
----------------------------------
We will complete the same exercise for vertical flow sedimentation tanks.

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

Note how this question is different from the same question for the horizontal flow sedimentation tank. In the horizontal flow sedimentation tank, particles could settle to the bottom of the reactor. We cared about particles settling to the bottom because it means that In the vertical flow sedimentation tank, particles w

Floc rollup
===============================

Floc blankets
===============================

Sludge disposal
===============================

***********************************************
Design Approach
***********************************************

- flow distribution is primary constraint
  - don't worry about floc breakup
  - avoid flow circulations

- easy operation and maintenance

***********************************************
Components of an AguaClara Sedimentation Tank
***********************************************

Note: this section should use words and figures to describe the different parts of the tank and what their purpose is, with brief explanation of how they work.

- Inlet and outlet channels
  - Flow distribution
- Inlet manifold

  First, the inlet manifold has a diffuser system that straightens the fluid jets that are exiting the manifold so that they have no horizontal velocity component. This is critical because even a small horizontal velocity causes a large scale circulation that transports flocs directly to the top of the sedimentation tank. Inlet manifolds without flow straightening diffusers are commonly used in vertical flow sedimentation tanks including designs by leading competitors.

- Diffusers

  Second, the diffusers create a line jet that spans the entire length of the sedimentation tank. The line jet enters a jet reverser and the vertical upward jet momentum is used to resuspend flocs that have settled to the bottom of the sedimentation tank. The resuspended flocs form a fluidized bed (floc blanket) with a suspended solids concentrations of approximately 1-5 g/L. The high concentration of particles leads to an increase in collisions and particle aggregation. The floc blanket reduces settled water turbidity by a factor of 10 (Garland et al., 2017) and provides two additional benefits. The floc blanket creates a uniform vertical velocity of water entering the plate settlers and the floc blanket transports excess flocs to a floc hopper for final removal by opening a small drain valve.

Note: discuss "sed tank as a circuit: flow distribution challenge"

- Jet reverser and bottom geometry

  Third, the bottom geometry is shaped so that all flocs that settle are transported to the jet reverser. Thus there is no accumulation of settled flocs in the main sedimentation basin. Sludge that is allowed to accumulate in the bottom of sedimentation tanks in tropical and temperate decomposes anaerobically and generates methane. The methane forms gas bubbles that carry suspended solids to the top of the sedimentation tank and cause a reduction in particle removal efficiency.  The AguaClara sedimentation tank bottom geometry prevents sludge accumulation.

- Floc blankets
- Floc hopper

  The hydraulic self cleaning sedimentation tank with a high performing floc blanket, zero sludge accumulation, and with no moving parts outperforms conventional sedimentation tanks on capital cost, performance, and maintenance costs. Mechanical sludge removal systems are well known to be costly to install and a challenge to maintain.

- Plate settlers
- Submerged outlet manifold

***********************************************
Design of an AguaClara Sedimentation Tank
***********************************************

Note: this section will build off of the conceptual understanding established in the previous section and will explain how the tank works with derivations and mathematical models.

- Inlet and outlet channels
  - Exit weir height
  - Drain for flocculated water (waste)
  - Pipe stubs to block certain tanks when they need to be taken offline

- Inlet manifold
- Diffusers
  - Width,
- Jet reverser
- Floc blankets
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

*******************************************************
Sedimentation Challenges, Confusions, and Failure Modes
*******************************************************

- Flow circulations
- Floc Volcanoes
- NOM impact on floc density
- Role of floc blanket
