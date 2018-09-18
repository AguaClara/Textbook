.. _title_Sed_Design:

********************
Sedimentation Design
********************

***************************************
Foundational Concepts
***************************************

To understand how sedimentation works, a few key concepts must first be developed. This includes understanding how and why flocs move in water. Remember, the goal of sedimentation reactor design is to optimize the floc-settling process.

Terminal velocity:
As flocs settle in water, they will fall at a speed dictated by the weight of the floc, the buoyancy of the floc, and the drag from the water. These three forces - the gravitational weight force, the buoyant force, and the drag force - that dictate the speed at which a floc falls are detailed in the following free body diagram. We care about determining the speed at which flocs will fall because [WHY].

[FLOC FORCES FREE BODY DIAGRAM]

To determine the force balance on a falling floc, consider:

.. math::

  \sum F = m a

  F_{drag} + F_{buoyant} - W_{floc} = 0

Each of the force components can be determined by:

.. math::

  F_{drag} = C_D A_{floc} \rho_{H_2O} \frac{v_t^2}{2}

  F_{buoyant} = V\llap{---}_{floc} \rho_{H_2O} g

  W_{floc} = V\llap{---}_{floc} \rho_{floc} g

| Where:
| :math:`V\llap{---}_{floc} =` floc particle volume
| :math:`A_{floc} =` particle cross sectional area
| :math:`\rho_{floc} =` particle density
| :math:`\rho_{H_2O} =` water density
| :math:`g =` acceleration due to gravity
| :math:`C_D =` drag coefficient
| :math:`v_t=` particle terminal velocity
| :math:`D=` particle diameter

Plugging into the original mass balance,

.. math::

  [C_D A_{floc} \rho_{H_2O} \frac{v_t^2}{2}]+[V\llap{---}_{floc} \rho_{H_2O} g]-[V\llap{---}_{floc} \rho_{floc} g] =0

Solving for terminal velocity, :math:`v_t`, provides

.. math::

  v_t = \sqrt{\frac{4}{3}\frac{gD}{C_D}\frac{(\rho_{floc}-\rho_{H_2O})}{\rho_{H_2O}}}


* capture velocity
  + k

- floc rollup
- floc blankets
- sludge disposal

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
