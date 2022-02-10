.. _title_Flocs_Fractals_Forces_and_Fluidized_Suspensions_Introduction:

************************
Flocs, Fractals, Forces
************************

The physics of flocs, fractals, fluids, and forces define the processes of flocculation, flocnets, lamellar sedimentation, and filters. The chemical bonds that hold flocs together determine the maximum diameter that a floc can grow to in the fluid shear of a flocculator. The force of gravity is strong enough to break flocs and determines the maximum size that a floc can grow to on planet earth or, for that matter, in the flocnet that forms in the bottom of the AguaClara clarifiers. The maximum diameter that a floc can grow to without being pulled apart by gravity sets a maximum terminal velocity for flocs and that has direct implications for the maximum upflow velocity than can be used in upflow clarifiers.

The three forces of chemical bonds, gravity, and shear can be grouped into two dimensionless parameters that will define the relationships between floc size, floc density, and these forces.

Characteristic Core Particle
============================

The concept of a characteristic core particle that sets the floc properties as it moves through the process of the flocculation, flocnet, settlers, and filter arose with two AguaClara plants in Honduras that ran into difficulties treating water from pristine high elevation mountain water sources. In both cases the water was very low turbidity and was yellow from dissolved organics. The exact source of the color was not identified, but it was likely the decaying leaf litter from the forests.

The high concentration of dissolved organics in the raw water requires a significant dosage of coagulant and there is very little clay present. The result is a very low density floc made of organic matter that is close to the density of water and perhaps even less dense than water and coagulant nanoparticles. These low density flocs are not captured efficiently by the plate settlers. The challenge of treating these two water sources led to the insight that we could characterize the properties of a floc if we understood the characteristic density and size of the core particle that aggregates to form the flocs.

The algorithm to define the characteristic density and diameter of the core particle is still under development. Nonetheless, the density and diameter of the characteristic core particle that aggregates to form the flocs are the key parameters that determine the performance of each stage of the treatment process.


Fractal Flocs
=============

Flocs are fractals. Fractals describe structures in which similar patterns occur over a range of scales. During flocculation flocs grow larger and larger by combining similar sized flocs. Flocs do not combine like raindrops! As raindrops combine they conserve both volume and mass.  With each subsequent collision the floc incorporates more water and thus its density gradually approaches the density of water. The inclusion of more and more water as the floc grows means that the floc mass is NOT conserved as it grows. Likewise, the volume of the floc is not conserved as it grows.

When :math:`n_{raindrops}` of equal volume :math:`\rlap{-} V_0` combine the resulting volume is :math:`\rlap{-} V = \rlap{-} V_0 n_{raindrops}`. When flocs combine the equation is slightly more complicated.

.. math::
  :label: V_floc_of_n_cp

  \rlap{-} V_{floc} = \rlap{-} V_{cp} n_{cp}^\frac{3}{\Pi_{fractal}}

| Where
| :math:`\rlap{-} V_{floc}` is the floc volume
| :math:`n_{cp}` is the number of core particles in the floc
| :math:`\rlap{-} V_{cp}` is the core particle volume
| :math:`\Pi_{fractal}` is the floc volume-based fractal dimension

Raindrops conserve volume when they collide and have a :math:`\Pi_{fractal}` of 3. If a particle would conserve its projected area when it combines, then it would have a :math:`\Pi_{fractal}` of 2. If a particle would conserve its diameter when it combines, then it would have a :math:`\Pi_{fractal}` of 1. A fractal dimension of 1 could occur if the particles all attached into a single long chain.

The fractal dimension of the resulting floc is a function of the difference in size of the colliding particles. We will show in the chapter on flocculation that the aggregation of flocs in a shear environment is limited to flocs that are of similar size. The sequential collisions of similar sized particles is the basis of the hierarchical model described by `Meakin (1988) <https://www-sciencedirect-com.proxy.library.cornell.edu/science/article/pii/0001868687800167>`_. The fractal dimension of flocs that form from collisions of similarly sized flocs has a slightly lower value than would be obtained from collisions between differently sized flocs.

The fractal dimension of flocs formed through hierarchical (same size) collisions has been bracketed between about 1.89 and 2.13. The fractal dimension of 1.89 is the result of aggregation where the flocs only attach at one point and do not rotate and make additional attachments after the initial collision. `Meakin (1988) <https://www-sciencedirect-com.proxy.library.cornell.edu/science/article/pii/0001868687800167>`_ simulated floc cluster aggregation that considered potential relative rotation of the two flocs and the formation of additional attachment points. After the initial collision with one attachment point the flocs rotate until they collide again and make a second attachment. The two attachment points will still allow rotation about an axis defined by the two attachment points. The flocs can rotate about that axis until a 3rd point of attachment is formed. With 3 points of attachment the relative motion of the 2 flocs is completely constrained.

The fractal dimension increases with each additional attachment point. `Meakin (1988) <https://www-sciencedirect-com.proxy.library.cornell.edu/science/article/pii/0001868687800167>`_ found  fractal dimensions :math:`\Pi_{fractal}` of 1.89, 2.08, and 2.13 were obtained for initial contact, rotation until contact in a direction that decreases the distance between the centers of mass of the two flocs, and then rotation about the axis defined by the two contact points in a direction that would again move their centers of mass to be closer.

.. math::
  :label: D_floc_of_n_cp

  D_{floc} = D_{cp} n_{cp}^\frac{1}{\Pi_{fractal}}

| Where
| :math:`D_{floc}` is the floc diameter
| :math:`n_{cp}` is the number of core particles in the floc
| :math:`D_{cp}` is the core particle diameter
| :math:`\Pi_{fractal}` is the floc volume-based fractal dimension

The number of core particles in a floc is obtained by solving Equation :eq:`D_floc_of_n_cp` for :math:`n_{cp}`.

.. math::
  :label: n_cp_of_D_floc

  n_{cp} = \left(\frac{D_{floc}}{D_{cp}}\right)^{\Pi_{fractal}}

Floc Density
============

The density of a floc decreases as it grows larger. The density of the floc can be calculated based on conservation of mass and volume. Note that as the floc grows it incorporates more and more water and thus the initial mass of the core particles does not equal the final mass of the larger flocs.

.. math::
  :label:

  M_{mix} = M_1 + M_2

Mass conservation can be written in terms of density as:

.. math::
  :label:

  \rho_{mix} \rlap{-} V_{mix} =
  \rho_1 \rlap{-} V_1 + \rho_2 \rlap{-} V_2

Written in terms of water and core particles the floc mass conservation and taking into account that the water volume is equal to the floc volume minus the core particle volume we obtain

.. math::
  :label: floc_mass_conservation

  \rho_{floc} \rlap{-} V_{floc} =
  \rho_{H_2O} \rlap{-} V_{floc} - \rho_{H_2O}\rlap{-} V_{n_{cp}} + \rho_{cp} \rlap{-} V_{n_{cp}}

where :math:`\rlap{-} V_{n_{cp}}` is the total volume of the core particles in the floc. The buoyant density is the parameter of interest when calculating terminal velocity and thus Equation :eq:`floc_mass_conservation` can be rewritten as

.. math::
  :label: floc_buoyant_density_1

  \left( \rho_{floc} - \rho_{H_2O} \right)  =
  \left( \rho_{cp}  - \rho_{H_2O} \right) \frac{\rlap{-} V_{n_{cp}}}{ \rlap{-} V_{floc}}

The floc volume can be rewritten as a function of the floc diameter.

.. math::
  :label: volume_floc_of_D

  \rlap{-}V_{floc} =
  \frac{\pi}{6} D_{floc}^3

The volume of core particles in the floc is a function of the number of core particles.

.. math::
  :label: volume_core_particles_of_D_1

  \rlap{-}V_{n_{cp}} =
  n_{cp} \frac{\pi}{6} D_{cp}^3

The number of core particles can be eliminated from Equation :eq:`volume_core_particles_of_D_1` by substituting Equation :eq:`n_cp_of_D_floc`.

.. math::
  :label: volume_core_particles_of_D

  \rlap{-}V_{n_{cp}} =
  \frac{\pi}{6} D_{cp}^3 \left(\frac{D_{floc}}{D_{cp}}\right)^{\Pi_{fractal}}


Substituting the floc volume and the core particle volume into Equation :eq:`floc_buoyant_density_1`

.. math::
  :label: floc_buoyant_density_2

  \left( \rho_{floc} - \rho_{H_2O} \right)  =
  \left( \rho_{cp}  - \rho_{H_2O} \right) \frac{\frac{\pi}{6} D_{cp}^3
  \left(\frac{D_{floc}}{D_{cp}}\right)^{\Pi_{fractal}} }{ \frac{\pi}{6} D_{floc}^3}

Simplifying :eq:`floc_buoyant_density_2` we obtain

.. math::
  :label: floc_buoyant_density

  \left( \rho_{floc} - \rho_{H_2O} \right)  =
  \left( \rho_{cp}  - \rho_{H_2O} \right)
  \left(\frac{D_{cp}}{D_{floc}}\right)^{3-\Pi_{fractal}}

For volume-based fractal dimension less than 3 the buoyant density decreases as the floc size increases. The smaller than fractal dimension the less dense the resulting floc.

.. _heading_Floc_Terminal_Velocity:

Floc Terminal Velocity
======================

As flocs settle in water, they will fall at a speed dictated by the weight of the floc, the buoyancy of the floc, and drag from the water. These three forces - the gravitational weight force, the buoyant force, and the drag force - dictate the speed at which a floc falls and are detailed in the free body diagram of :numref:`figure_terminal_velocity_FBD`. We care about determining the speed at which flocs will fall because knowing this information will help inform our sedimentation reactor design criteria.

.. _figure_terminal_velocity_FBD:

.. figure:: ../Images/terminal_velocity_FBD.png
    :height: 300px
    :align: center
    :alt: Buyouant force, drag force, and gravitational force shown for floc free body diagram.

    Free body diagram of a floc in water.

To determine the force balance on a falling floc, consider:

.. math::

  \sum F = m a

At terminal velocity, the floc has been falling for a long period of time so there is no acceleration and the right side of the equation simplifies to zero.

:math:`F_{drag} + F_{buoyant} - W_{floc} = 0`

The drag force is determined by:

.. math::
  :label: drag_force_on_sphere

  F_{drag} = C_D A_{floc} \rho_{H_2O} \frac{v_t^2}{2}

The buoyant force is given by:

.. math::
  :label: buoyant_force_on_sphere

  F_{buoyant} = \rlap{-}V_{floc} \rho_{H_2O} g

The weight of the sphere is given by:

.. math::
  :label: gravity_force_on_sphere

  W_{floc} = \rlap{-}V_{floc} \rho_{floc} g

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

  \left [C_D A_{floc} \rho_{H_2O} \frac{v_t^2}{2} \right]+\left [\rlap{-}V_{floc} \rho_{H_2O} g\right ]-\left [\rlap{-}V_{floc} \rho_{floc} g \right] =0

Solving for terminal velocity, :math:`v_t`, we obtain

.. math::
  :label: v_t_general

  v_t = \sqrt{\frac{4}{3}\frac{g D_{floc}}{C_D}\frac{(\rho_{floc}-\rho_{H_2O})}{\rho_{H_2O}}}

Terminal velocity is a function of fluid density, floc density, gravity, particle diameter, and the drag coefficient. To calculate velocity, all of those inputs must be determined.

The first component that we will focus on is the drag coefficient, :math:`C_D`. The drag coefficient is function of Reynolds Number, :math:`Re`, and the characteristic flow around a particle. As a reminder, :math:`Re = \frac{v_t D_{floc}}{\nu}` where :math:`v_t` is the velocity of the fluid relative to the particle, :math:`D_{floc}` is the characteristic length scale (in this case the floc diameter), and :math:`\nu` is kinematic viscosity.

Drag coefficients are used to describe flow around a particle and are shown in :numref:`figure_drag_coeff_Re_base`.

.. _figure_drag_coeff_Re_base:

.. figure:: ../Images/drag_coeff_Re_base.png
    :height: 300px
    :align: center
    :alt: Drag coefficient as a function of Reynolds number.

    Drag coefficient on a sphere as a function of Reynolds number.

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

.. figure:: ../Images/drag_coeff_Re_full.png
    :height: 300px
    :align: center
    :alt: Drag coefficient as a function of Reynolds number.

    Drag coefficient as a function of Reynolds number.

Note that the coefficient of drag in the transition region is an important parameter to understand. Equations for the coefficient of drag are explored in the paper by `Yang et al. in "General formulas for drag coefficient and settling velocity of sphere based on theoretical law" <https://www.sciencedirect.com/science/article/pii/S2095268615000178>`_. They have determined that Oseen law based formulas are recommended for use.

Let's consider the drag coefficient diagram at Reynolds numbers of :math:`10^5`. We notice that there is a "bump" in the plot, in which the drag coefficients drop. This is because at really high Reynolds numbers, the boundary layer around the particle became turbulent. This causes the wake behind the particle to be a little smaller, leading to a slight reduction in drag. The drag coefficient decreases, but the total drag force does not necessarily decrease (and likely keeps on increasing).

To understand this phenomenon, think about a golf ball. Golf balls are designed with dimpled surfaces because the dimpled surface forces the transition described above to happen at lower Reynolds numbers. The dimples initiate turbulence in the boundary layer and cause a slight reduction in the drag coefficient. Thus, dimpled golf balls can travel further than smooth ones.

You might think: why aren't more surfaces dimpled? If I want my car to get better mileage, should I dimple its surface to take advantage of the same turbulent boundary layer properties as the golf ball? But before you go and damage some metal, let's think. If a car and golf ball are traveling through air at the same speed, what will be their relative Reynolds numbers? We know that :math:`Re = \frac{v_t D}{\nu}` and :math:`D_{golfball} << D_{car}`. The relative length scales mean that cars have much higher Reynolds numbers than the golf ball. In fact, the Reynolds number for a car is so high that it is already past the point that the boundary layer becomes turbulent. The golf ball needs to be dimpled because its Reynolds numbers are not so large that they will pass the turbulent boundary transition.

Let's go back to the realm of water treatment. We care about drag coefficients and terminal velocities because they help describe how flocs will move in water. Flocs tend to exist in the region between 1< :math:`Re` < 10. This region is not perfectly described by Stokes Law, but it is used as an appropriate approximation. We have already solved for the general equation for terminal velocity using the force balance approach. Now, we can solve for a terminal velocity equation specifically in the laminar region.

Plug the drag coefficient for laminar flow, :math:`C_D = \frac{24}{Re}`, and Reynolds number, :math:`Re = \frac{v_t D_{floc}}{\nu}`,  into the general terminal velocity Equation :eq:`v_t_general` to obtain

.. math::

  v_t = \frac{D_{floc}^2g}{18\nu}\frac{\rho_{floc} -\rho_{H_2O}}{\rho_{H_2O}}

Again, we can draw a parallel with the Moody Diagram. The general form of the terminal velocity equation is like the Darcy-Weisbach equation; it is always true. The terminal velocity in the laminar flow region is like the Hagen-Poiselle equation; it is only good for laminar flow. We will use the laminar specific condition because we are working with flocs with low Reynolds numbers.

Our equations for terminal velocity depend on the density of a floc. As discussed in previous sections, we know that there is a specific relationship between the density of a floc and the diameter of a floc because flocs are fractals and as flocs get bigger, their density gets lower. We can account for the size and density relationship by substitution Equation :eq:`floc_buoyant_density` into the terminal velocity equation.

.. math::
  :label: vt_of_floc

  v_t = \frac{D_{cp}^2g}{18\nu}\frac{\rho_{cp} -    \rho_{H_2O}}{\rho_{H_2O}} \left( \frac{D_{floc}}{D_{cp}} \right) ^{\Pi_{fractal}-1}

| Where:
| :math:`D_{cp} =` diameter of core particle
| :math:`\Pi_{fractal} =` volume-based fractal dimension
| :math:`D_{floc} =` floc diameter
| :math:`\rho_{cp} =` density of the core particle making up the floc

The following plot in :numref:`figure_terminal_velocity_floc_diam` shows the relationship between floc diameter and terminal velocity.

.. _figure_terminal_velocity_floc_diam:

.. figure:: ../Images/terminal_velocity_floc_diam.png
    :width: 400px
    :align: center
    :alt: Terminal velocity as a function of floc diameter, taking into account the changing density of flocs formed from clay.

    Terminal velocity as a function of floc diameter taking into account the changing density of flocs.

Three important regions are highlighted in the plot. At small floc diameters, less than 10 :math:`\mu m`, terminal velocity is less that 0.1 :math:`\frac{mm}{s}`. A terminal velocity this low would require extremely large sedimentation tanks for reasonable treatment. Because large sedimentation tanks are costly and unfeasible, we use flocculation to aggregate particles and achieve floc sizes of greater diameters and higher terminal velocities.

For flocs made of clay and with diameters around 35 :math:`\mu m`, the terminal velocity is about 0.12 :math:`\frac{mm}{s}`. AguaClara plate settlers are designed to settle out flocs of this size (particles dropping at 0.12 :math:`\frac{mm}{s}`) so the smallest floc that the plate settlers can reliably capture is 35 :math:`\mu m`. This will be explored in more detail during the discussion on :ref:`capture velocity <heading_capture_velocity>`.

Clay based flocs with diameters around 200 :math:`\mu m` have a terminal velocity of about 1 :math:`\frac{mm}{s}`. In our sedimentation tanks, which are upflow sedimentation tanks, we have water flowing up at about 1 :math:`\frac{mm}{s}` to capture a 200 :math:`\mu m` floc. These flocs are clearly visible but are small.

Our understanding of floc terminal velocity suggests that we can decide the size of the floc that we want the plate settlers to capture. If we decide that we want to capture flocs that are 35 :math:`\mu m` or larger, we know that we must design the plate settlers to capture flocs falling at 0.12 :math:`\frac{mm}{s}`.

Chemical Bond Strength
======================

The chemical bonds formed by the polymers or the coagulant nanoparticles could be strong, intramolecular bonds such as covalent bonds in which valence electrons are shared, or a non-covalent bond that does not involve sharing electrons. Non-covalent bonds include hydrogen bonding, and Van der Waals forces.

The strength of a polymer chain with carbon-carbon bonds is of the order of 1 to 10 nN (`Levinthal and Davison, 1961 <https://doi.org/10.1016/S0022-2836(61)80030-2>`_). Covalent bonds rupture at approximately 1600 pN, noncovalent bonds break at about 160 pN, and hydrogen bonds break at about 4 pN (`Forces involved at the biological level <http://www.picotwist.com/index.php?content=smb&option=odg>`_).

If we assume that the flocs are joined by 3 bonds to create a constrained connection then we can compare the fluid shear forces that are pulling flocs apart to the strength of potential bonds. The result of this force comparison is shown in :numref:`figure_Shear_force_and_bond_strength`.

.. _figure_Shear_force_and_bond_strength:

.. figure:: ../Images/Shear_force_and_bond_strength.png
   :width: 400px
   :align: center
   :alt: figure_Shear_force_and_bond_strength

   The diameter of flocs after flocculation suggests that covalent bonds are likely responsible for holding flocs together.

Given that flocs grow to be approximately 1 mm in a 100 Hz flocculator it suggests that the bonds holding the flocs together are either covalent bonds or noncovalent bonds that are stronger than hydrogen bonds. Van der Waals interactions are weaker than hydrogen bonds and thus Van der Waals interactions likely are not significant for flocculation when using coagulants.

Van der Waals forces have traditionally been viewed as the primary force responsible for holding flocs together after the repulsive electrostatic force was neutralized. The analysis of the forces shown above reveals that Van der Waals forces are too weak to allow the formation of large easily settled flocs in the shear environment of a flocculator. Instead flocculation is based on stronger noncovalent bonds or perhaps even covalent bonds.

Hydrated oxides of polyvalent metals like Fe(III), Al(III), Ti(IV) and Zr(IV) exhibit ligand sorption properties by forming inner-sphere complexes (`Sarkar et al, 2007 <https://doi.org/10.1016/j.reactfunctpolym.2007.07.047>`_). In inner-sphere complexes the coagulant nanoparticle forms covalent bonds with the molecules in the surface of the raw water particles. Inner sphere bonds are strong and stable. In contrast, outer sphere bonds include a molecule of water between the two surfaces and form a transient bond.

Given that

#. Aluminum and iron coagulant nanoparticles form covalent bonds with arsenic
#. Outer sphere complexes are transient
#. The shear forces acting on flocs suggest strong bonds

we conclude that the coagulant nanoparticles likely form covalent bonds with inorganic particles present in raw water.

Shear Force Acting on Flocs
===========================

The hydrodynamic force caused by a velocity gradient for two identically sized particles is given by `Goren, 1971 <https://doi.org/10.1016/0021-9797(71)90244-X>`_

.. math::
  :label: shear_force_on_doublet

  F_{shear_{max}} =
  \frac{3 \pi}{4} \mu D_{floc}^2 G

where :math:`D_{floc}` is the diameter of each of the two flocs that have joined and :math:`G` is the uniform velocity gradient.

Flocs will break (or will not grow larger) when the fluid forces acting on the floc exceed the strength of the bonds that hold the floc together. The fluid shear stress is given by Equation :eq:`tau_of_mu_G`. The velocity gradient is caused by turbulent kinetic energy dissipation as given by Equation :eq:`G_Camp_Stein`. Equation :eq:`tau_of_mu_G` and Equation :eq:`G_Camp_Stein` can be combined to obtain an estimate of the fluid shear stress, :math:`\tau`.

.. math::
  :label: fluid_shear_stress

	 \tau =
   \rho \sqrt{\varepsilon \nu} =
   \mu G

The shear stress is a function of the rate of turbulent energy dissipation and the viscosity of the fluid. The shear stress increases as the water temperature decreases. The shear force acting to pull a doublet floc apart is given in Equation :eq:`shear_force_on_doublet` and can be combined with Equation :eq:`tau_of_mu_G` to obtain

.. math::
  :label: fluid_shear_stress_on_doublet

	 F_{shear_{max}} =
     3 \tau \frac{ \pi D_{floc}^2}{4} =
     3 \tau A_{floc}

The floc will break apart when the :math:`F_{shear_{max}}` exceeds the coagulant bond strength of the coagulant nanoparticles and the particles they attach to. Thus we can create a dimensionless parameter describing the ratio of the fluid shear stress to the bond strength by dividing Equation :eq:`fluid_shear_stress_on_doublet` by :math:`F_{covalent}`.

.. math::
  :label: fluid_shear_stress_to_bond_ratio

	 \Pi_{bond}^{shear} =
   \frac{F_{shear_{max}}}{F_{bond}} =
   \frac{3 \tau A_{floc}}{F_{bond}}

The expectation is that the flocs will break for values of :math:`\Pi_{bond}^{shear}>1`. The value of :math:`\Pi_{bond}^{shear}` will ideally be measured experimentally since there are a number of unknowns buried in the term including a characteristic length of the lever arm that the coagulant bond is acting on.  This analysis shows that the maximum size of a floc is set by the fluid shear stress, :math:`\tau`. Previously it wasn't clear if floc size was limited by energy dissipation rate or by the velocity gradient. Neither of those parameters captures the physics because ultimately it is a force that breaks the covalent bond and thus it must be a fluid force (not energy dissipation rate or velocity gradient) that can be used as a design parameter. By recognizing that the shear stress :math:`\tau` must be limited we can now develop design equations that account for the effects of viscosity and temperature on the design.

When flocs are broken by the shearing action of the fluid it is possible that a primary particle is torn off or that the floc is broken in half. The method of breaking matters because if primary particles are dislodged from a floc then any breaking will lead to a deterioration of the sedimentation tank performance because some of those primary particles will make it through the floc blanket and won't be captured by the plate settlers. Conventional wisdom would suggest that flocs will be broken into little pieces. If that were the case then any floc breakup would cause the settled water turbidity to increase. `Garland, 2016 <https://doi.org/10.1089/ees.2015.0314>`_ showed that there was no sign of increased settled water turbidity up to an energy dissipation rate of 300 mw/kg (:numref:`figure_sed_performance_vs_jet_edr` adapted from `Garland, 2016 <https://doi.org/10.1089/ees.2015.0314>`_).

.. _figure_sed_performance_vs_jet_edr:

.. figure:: ../Images/Sed_performance_vs_jet_edr.png
   :width: 400px
   :align: center
   :alt: Sed tank performance as a function of jet energy dissipation rate

   System suspended solids concentrations during steady state as a function of jet energy dissipation rate given an upflow velocity of 1.2 mm/s.  Results shown are averaged over 2 residence times (1200 seconds) of the sedimentation tank.


The maximum energy dissipation rate below the performance deterioration obtained by Garland (300 mW/kg) can be converted into the corresponding *average* velocity gradient using :eq:`G_Camp_Stein` to obtain 560 Hz (assuming a water temperature of 22°C). Similarly, the energy dissipation rate can be converted to a shear stress using Equation :eq:`fluid_shear_stress` to obtain 0.55 Pa. The fluid shear combined with the strength of covalent bonds can be used to solve for the floc diameter using Equation :eq:`fluid_shear_stress_on_doublet`.

.. math::
  :label: d_floc_shear_stress

   D_{floc_{max}} =
   \sqrt{\frac{4F_{bond}}{3 \pi \tau}}

The floc size that corresponds to 300 mW/kg is 35 micrometers. For clay dominated flocs Equation :eq:`vt_of_floc` gives a 0.13 mm/s sedimentation velocity which is just slightly higher than the 0.1 mm/s capture velocity used by Garland.

Garland's experiment with the result of floc breakup at the sedimentation tank inlet is consistent with several hypotheses.

#. The bonds holding flocs together are likely strong (order 1.6 nN). It is not yet clear what the origin of the bonds is. Van der Waals forces may be of similar magnitude, but they would also apply to water molecules and thus there wouldn't be a mechanism for the coagulant to displace water molecules between approaching surfaces. For example, the gecko adhesion to surfaces is reduced by a factor of 40 when the surface is wet (`Stark et al., 2012 <https://doi.org/10.1242/jeb.070912>`_). Thus a force that is stronger than any bonds between water molecules and the surfaces must be responsible for joining coagulant nanoparticles and the particles present in the raw water. One likely candidate is covalent bonds.
#. Flocs are broken where there is the largest force per bond. This would logically occur at the connection between the two subunits that form the floc. Thus when flocs break they would not be expected to produce tiny fragments.
#. The fluid shear stress determines the force acting to tear a floc apart. Thus given a constant energy dissipation rate the force acting to break up flocs will increase as the temperature drops (see Equation :eq:`fluid_shear_stress`)
#. Settled water turbidity increases when the floc terminal velocity is less than the capture velocity of the plate settlers.

Equation :eq:`d_floc_shear_stress` can be written as a function of the velocity gradient by substituting Equation :eq:`fluid_shear_stress` for the fluid shear.

.. math::
  :label: d_floc_G

   D_{floc_{max}} =
   \sqrt{\frac{4F_{bond}}{3 \pi \mu G_{max}}}

Equation :eq:`d_floc_G` must be based on the maximum velocity gradient in a reactor and not the average value. This is particularly important for flocculators that are not designed to have uniform velocity gradients.

.. math::
  :label: Gmax_of_d_floc

  G_{max} =
  \frac{4F_{bond}}{3 \pi \mu D_{floc_{max}}^2}

.. _figure_GmaxofFlocD:

.. figure:: ../Images/GmaxofFlocD.png
    :width: 400px
    :align: center
    :alt: internal figure

    The maximum velocity gradient that flocs can withstand decreases rapidly as flocs increase in diameter.

The maximum floc diameter is influenced by temperature because as the viscosity increases the shear force exerted on the floc increases. Equation :eq:`d_floc_G` shows this dependency and illustrates one of the reasons (see :numref:`figure_DmaxofGandTemp`) why temperature is a critical parameter in the design of drinking water treatment plants.

.. _figure_DmaxofGandTemp:

.. figure:: ../Images/DmaxofGandTemp.png
    :width: 400px
    :align: center
    :alt: internal figure

    The maximum floc size at a maximum velocity gradient of 100 Hz increases with temperature due to a decrease in the viscosity.

Linking Velocity Gradient and Capture Velocity
==============================================

The coagulant bond strength provides a link between flocculator design and sedimentation tank design.

We can substitute equation :eq:`d_floc_G` into equation :eq:`vt_of_floc` and solve for the maximum flocculator velocity gradient that will produce flocs that are large enough to be captured by the sedimentation tank. The capture velocity of the sedimentation tank must be equal to or smaller than the floc terminal velocity to ensure capture of the floc.

.. math::
  :label: vc_of_G

  v_c = \frac{D_{cp}^2g}{18\nu}\frac{\rho_{cp} -    \rho_{H_2O}}{\rho_{H_2O}} \left( \frac{  \sqrt{\frac{4F_{bond}}{3 \pi \mu G_{max}}}}{D_{cp}} \right) ^{\Pi_{fractal}-1}

Solve equation :eq:`vc_of_G` for the maximum velocity gradient :math:`G_{max}`.

.. math::
  :label: G_of_vc_and_fractal

   G_{max} = \frac{4F_{bond}}{3 \pi \nu \rho_{H_2O} D_{cp}^2}\left(  \frac{D_{cp}^2g}{18 v_c \nu} \frac{\rho_{cp} - \rho_{H_2O}}{\rho_{H_2O}}\right) ^\frac{2}{\Pi_{fractal}-1}

Equation :eq:`G_of_vc_and_fractal` can be simplified by making the assumption that the floc fractal dimension exiting the flocculator is approximately 2.

.. math::
  :label: G_of_vc_and_fractal_of_2

   G_{max} \approx  \frac{4F_{bond}}{3 \pi \nu^3 \rho_{H_2O}}\left(  \frac{g D_{cp}}{18 v_c} \frac{\rho_{cp} - \rho_{H_2O}}{\rho_{H_2O}}\right) ^2

Equation :eq:`G_of_vc_and_fractal_of_2` reveals the key relationships between flocculator and sedimentation tank design. The flocculator velocity gradient must decrease in proportion to the square of the sedimentation tank capture velocity. If AguaClara were to increase the sedimentation tank capture velocity from 0.12 to 0.3 mm/s the flocculator velocity gradient would need to decrease by a factor of 6.25. The dramatic effect of temperature is revealed as well. It is well known that flocculation/sedimentation processes perform poorly at low temperatures. The kinematic viscosity of water approximately doubles as the temperature drops from 20°C to 0°C. That results in a need to decrease the velocity gradient by a factor of 8! Finally, the dissolved organic matter and inorganic particles together determine the density and diameter of the core particles that make up the flocs. Organic matter reduces the density of the core particles and that requires a lower velocity gradient. The worst combination of parameters is a cold water with a high dissolved organic concentration and a low concentration of inorganic particles.

The effect of water temperature and sedimentation tank capture velocity on the maximum flocculator velocity gradient are shown in :numref:`figure_Gmax_of_T_and_vc`. The model assumptions were:

  * :math:`F_{bond} = 0.57 nN`
  * :math:`D_{cp} = 5 \mu m`
  * :math:`\rho_{cp} = 2650 \frac{kg}{m^3}`

The value of :math:`F_{bond}` was selected to match the results of `Garland, 2016 <https://doi.org/10.1089/ees.2015.0314>`_.


.. _figure_Gmax_of_T_and_vc:

.. figure:: ../Images/Gmax_of_T_and_vc.png
    :width: 400px
    :align: center
    :alt: internal figure

    The maximum average velocity gradient :math:`G_{CS}`, that can be used in the flocculator decreases rapidly as the water temperature decreases because the higher viscosity prevents flocs from growing as large in the flocculator and reducers their terminal velocity in the plate settlers.

Cold temperatures are known to be particularly challenging for flocculation and the model results (equation :eq:`G_of_vc_and_fractal_of_2`) shown in :numref:`_figure_Gmax_of_T_and_vc` provides insight into the dramatic reduction in velocity gradient required for effectively cold weather operation.

The effects of the core particle density on the velocity gradient may also be dramatic especially as the particle density approaches water. Water sources that have high concentrations of dissolved organics require pilot testing to ensure that flocs with a reasonable terminal velocity can be produced.

:numref:`figure_Gmax_of_T_and_vc` suggests that AguaClara should limit the flocculation velocity gradient to 100 Hz for raw waters with a minimum temperature of 5°C. The velocity gradient may need to be lowered or the capture velocity may need to be reduced for raw water with high concentrations of dissolved organic matter. More research is required to characterize the effect of dissolved organic matter on the core particles that make up the flocs.

Drag Force on a Floc in a Filter Constriction
=============================================

The drag force on a floc or core particle that has attached to a constriction wall in a sand filter can be modeled as the drag on a sphere in uniform flow. The uniform flow approximation is reasonable because the constriction is expected to have a sharp entrance as particles preferentially deposit there. The drag force, Equation :eq:`drag_force_on_sphere`, is counteracted by the chemical bond force.

The maximum velocity in a pore is hypothesized to be set by the bond strength of the coagulant nanoparticles and the fluid drag on the primary particle that is attaching. It is assumed that the last particles that are able to deposit in a pore are primary particles because they can fill in the last available volume before the pore velocity is too high for any other particles to attach. It is possible that the attachment strength of the primary particles is a function of the fraction of their surface area that is covered by coagulant nanoparticles, :math:`\Gamma`. The total force acting downward on a primary particle that attaches to a constriction is the sum of the drag and the particle buoyant weight. These forces are counteracted by the force of the coagulant bonds.

.. math::
  :label: Fbond_drag_gravity

    F_{bond} = F_{drag} + F_{weight} - F_{buoyancy}

The flocs and particles that are captured in a filter are small in diameter and the strength of the coagulant bonds is large compared with forces of their buoyant weight. Equation :eq:`Fbond_drag_gravity` can be simplified to

.. math::
  :label: Fbond_drag

    F_{bond} = F_{drag}

The drag force is assumed to be set by the average pore water velocity because the deposition occurs near the entrance to the constriction before the boundary layer on the wall can develop. The velocity profile through the constriction could be uniform or the boundary layer could be developing and then the velocity at the wall could be significantly reduced. The particles are expected to attach at the sharp edge at the entrance to the constriction and the boundary layer is not expected to have grown significantly. Thus the velocity through the constriction is assumed to be uniform. The drag force on a clay particle that has attached to the wall of the constriction is

.. math::

  F_{drag} = C_D \frac{\pi}{4} D_{cp}^2 \rho_{H_2O} \frac{v_{constriction}^2}{2}

At Reynolds numbers (based on core particle diameter) less than about 10 the drag coefficient is given by

.. math::

  C_D = \frac{24}{Re} = \frac{24\nu}{v_{constriction}D_{cp}}

Thus the drag on a core particle is equal to the bond force and is given by

.. math::
  :label: Fbond_of_v_constriction


  F_{bond} = 3\pi \nu v_{constriction} D_{cp} \rho_{H_2O}

Gravity Acting on Flocs
=======================

In the same way that fluid shear sets a maximum size for flocs, gravity also limits floc size. As flocs grow larger their terminal velocity increases and they have a larger surface area that is experiencing shear as the floc falls through the water. The buoyant weight of the floc is counteracted by the shear on the floc. The shear tends to tear the floc apart and thus the coagulant nanoparticle bonds must hold the floc together. This problem might seem intractable because it isn't initially clear how many coagulant nanoparticle bonds are responsible for holding a floc together.

The majority of the floc growth will occur in the flocculator where only similarly sized flocs collide. At most flocs attach to each other at 3 points because additional connections would require deformation of the floc. This would suggest that 3 coagulant nanoparticle bonds prevent a floc from splitting in half. The shear forces on the floc cause a torque on each half of the floc such that the bottom of the floc is in tension and the top of the floc is in compression. The bonds will only fail in tension and thus it is one or two bonds in the bottom half of the floc that are holding the floc together.

We can create a dimensionless number that is the ratio of the bond strength to the buoyant weight of the floc.

.. math::
  :label: bong_1

  \Pi_{bond}^g = \frac {\rlap{-} V_{floc} \left(\rho_{floc} - \rho_{H_2O} \right) g} {F_{bond}}

To obtain an equation that is a function of the floc diameter we substitute the floc volume (Equation :eq:`volume_floc_of_D`) and the floc buoyant density (Equation :eq:`floc_buoyant_density_2`) into Equation :eq:`bong_1`.

.. math::
  :label: bong_of_D_floc_1

  \Pi_{bond}^g =
  \frac {\pi D_{floc}^3 g} {6 F_{bond}}
  \left( \rho_{cp}  - \rho_{H_2O} \right)
  \left(\frac{D_{cp}}{D_{floc}}\right)^{3-\Pi_{fractal}}

Separate the floc diameter term and simplify as much as possible.

.. math::
  :label: bong_of_D_floc

  \Pi_{bond}^g =
  \frac {\pi  g\left( \rho_{cp}  - \rho_{H_2O} \right) D_{cp}^{3-\Pi_{fractal}}} {6 F_{bond}} D_{floc}^{\Pi_{fractal}}

The maximum size of a floc that is under the influence of gravity can be obtained by solving Equation :eq:`bong_of_D_floc` for :math:`D_{floc}`.

.. math::
  :label: D_floc_of_bong_1

  D_{floc} =
  \left[\frac {6 F_{bond} \Pi_{bond}^g} {\pi  g\left( \rho_{cp}  - \rho_{H_2O} \right) D_{cp}^{3-\Pi_{fractal}}}\right]^{\frac{1}{\Pi_{fractal}}}

Unit calculations are problematic when the exponent on the units isn't an integer. To avoid that dilemma with the volume-based fractal dimension we will make the term that is raised to a fractional power be dimensionless by factoring out the diameter of the core particle.

.. math::
  :label: D_floc_of_bong

  D_{floc_{max}}^g = D_{cp}
  \left[\frac {6 F_{bond} \Pi_{bond}^g} {\pi  g\left( \rho_{cp}  - \rho_{H_2O} \right) D_{cp}^3}\right]^{\frac{1}{\Pi_{fractal}}}


The value of :math:`\Pi_{bond}^g` will need to be determined experimentally. A preliminary force analysis by Kevin Sarmiento suggests that this dimensionless factor may be approximately 8 based on reasonable assumptions for the length of the moment arm acting on one coagulant nanoparticle bond.

The maximum floc size that can be obtained based on a :math:`\Pi_{bond}^g = 8` as a function of the core particle density is shown in :numref:`figure_DmaxofFbondandGravity`.

.. _figure_DmaxofFbondandGravity:

.. figure:: ../Images/DmaxofFbondandGravity.png
    :width: 400px
    :align: center
    :alt: internal figure

    The maximum floc size deceases rapidly as the density of the core particle increases.

The maximum size of flocs that can be obtained with aluminum-based coagulants is thus limited due to the force of gravity. This has direct implications for the use of ballasted sand flocculation that uses micro-sand (size 40 - 150 µm) to increase the sedimentation velocity of the flocs. Equation :eq:`D_floc_of_bong` reveals that aluminum-based coagulants aren't strong enough to hold two micro-sand particles together. Ballasted sand flocculation requires additional polymers that increase the bond strength to create flocs around the micro-sand.

Maximum Floc Terminal Velocity
==============================

Given that the maximum floc size is limited by gravity we can determine the maximum terminal velocity that can be obtained by a floc. Then we can use the terminal velocity equation to find the maximum diameter of a floc that is falling through water under the influence of gravity. The force balance requires that the buoyant force be equal to :math:`F_{bond} \Pi_{bond}^g` in the terminal velocity equation.


.. math::
  :label: v_t_of_F_bond_1

  F_{drag} = C_D A_{floc} \rho_{H_2O} \frac{v_t^2}{2} = F_{bond} \Pi_{bond}^g


Plugging into the force balance between buoyant weight and bond force and assuming laminar flow we obtain

.. math::
  :label: v_t_of_F_bond_2

  \frac{24 \nu}{v_t D_{floc}} \frac{\pi}{4} D_{floc}^2 \rho_{H_2O} \frac{v_t^2}{2}  = F_{bond} \Pi_{bond}^g

Solving for terminal velocity, :math:`v_t`, we obtain

.. math::
  :label: v_t_of_F_bond_3

  v_t  =
  \frac{F_{bond} \Pi_{bond}^g}{3 \pi \nu D_{floc} \rho_{H_2O}}

The maximum floc diameter and the bond strength are related through Equation :eq:`D_floc_of_bong` and that relationship can be used to eliminate the floc diameter from Equation :eq:`v_t_of_F_bond_3`.

.. math::
  :label: v_t_of_F_bond

  v_t  =
  \frac{F_{bond} \Pi_{bond}^g}{3 \pi \nu \rho_{H_2O} D_{cp}
  \left[\frac {6 F_{bond} \Pi_{bond}^g} {\pi  g\left( \rho_{cp}  - \rho_{H_2O} \right) D_{cp}^3}\right]^{\frac{1}{\Pi_{fractal}}} }

The maximum terminal velocity (Equation :eq:`v_t_of_F_bond`) that can be obtained based on a :math:`\Pi_{bond}^g = 8` as a function of the core particle density is shown in :numref:`figure_vtmaxofFbondandGravity`.

.. _figure_vtmaxofFbondandGravity:

.. figure:: ../Images/vtmaxofFbondandGravity.png
    :width: 400px
    :align: center
    :alt: internal figure

    The maximum terminal velocity increases as the density of the core particle increases.

The maximum upflow velocity in the bottom of an upflow clarifier is limited by the maximum terminal velocity of the flocs. The flocs can grow to an even larger size while sliding down the plate settlers, but when they begin freefall they break apart and reach this maximum terminal velocity. The terminal velocity will also have direct influence on the concentration of the flocnet.
