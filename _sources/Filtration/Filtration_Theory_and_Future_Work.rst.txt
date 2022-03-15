.. raw:: html

    <embed>
       <link rel="canonical" href="https://aguaclara.github.io/Textbook" />
       <script src="https://hypothes.is/embed.js" async></script>
    </embed>

.. _title_Filtration_Theory_and_Future_Work:

***********************
Filtration Future Work
***********************

`Be sure to run the import code before trying any of the code examples linked in this section <https://colab.research.google.com/drive/15IrqdHgnk3NZVTiIuhQc6YdwFgquIHD1#scrollTo=iraCMmqY4sT2&line=1&uniqifier=1>`_

Constriction Velocity
======================

The maximum velocity in a pore is set by the strength of the coagulant bonds and the size of the core particles that are being captured by the filter. The drag force on the core particle must be balanced by the chemical bond strength and that relationship is given by Equation :eq:`Fbond_of_v_constriction`.

The minimum diameter of a particle deposition constriction is set by the maximum constriction velocity, :math:`v_{constriction_{max}}`.

.. math::
  :label: eq_D_constriction_min

    D_{constriction_{min}} = \Lambda_{pore} \sqrt\frac{4 v_a}{\pi v_{constriction_{max}}}

The head loss through a flow constriction can be estimated from the head loss through a flow expansion. We will use the form of the expansion Equation :eq:`eq_exp_v_in` that is based on the contraction velocity. The jet is assumed to expand sufficiently so that the residual kinetic energy is insignificant.

.. math::
  :label: eq_exp_v_constriction

     h_{e_{constriction}} =  \frac{\bar v_{constriction_{max}}^2}{2g}

The number of deposited constrictions per unit depth in a filter is

.. math::

    N_{constrictions_{series}} = \frac{H_{filter}}{\Lambda_{pore}}

The total head loss in a filter if taken to the point where the active filtration zone exited the filter and all pores were constricted would be

.. math::
  :label: eq_he_filter

    h_{e_{filter_{max}}} = \frac{H_{filter}}{\Lambda_{pore}}  \frac{\bar v_{constriction_{max}}^2}{2g}

The effect of increasing the pore size on terminal head loss is to decrease the *final* head loss when the active zone reaches the bottom of the filter because of the effect of :math:`\Lambda_{pore}`in the first term of Equation :eq:`eq_he_filter`. Note that this does not yet address the rate of head loss accumulation which is expected to be a function of sand grain diameter.

We can solve Equation :eq:`eq_he_filter` for maximum constriction velocity based on experimental measurements of the head loss at filter failure that is due to constrictions. Note that this head loss does NOT include the clean bed head loss.

.. math::
  :label: eq_he_filter2

    v_{constriction_{max}} = \sqrt{ \frac{2g\Lambda_{pore}}{H_{filter}}h_{e_{filter_{max}}}}

From :numref:`figure_Head_loss_vs_time` we have an estimate of 80 cm of head loss through a 20 cm bed of 0.5 mm diameter sand. This gives an estimate of 163 mm/s for the constriction velocity. This can be combined with Equation :eq:`Fbond_of_v_constriction` to estimate the coagulant bond strength to be 3.9 nN.


.. _heading_Shear_big_flocs_to_improve_filter_performance:

Shear Big Flocs
================

Here we explore the possibility of breaking flocs as they enter the filter bed to eliminate large flocs that may be reducing filter performance.

Primary particles have the lowest probability of hitting the wall in a constriction. Thus primary particles can travel the greatest distance through the active zone and still have a very small chance of being deposited near the end of the active zone. Thus it is possible that primary particles set the maximum length of the active zone and flocs tend to fill in the active zone at the upstream end. The larger the floc the more likely it will fill in an upstream constriction and thus shorten the active zone.

This suggests that one way to improve filter performance is to have a zone of very high shear that rips flocs apart so that they don't fill in the upstream pores in the active zone so quickly. This is because smaller flocs will not be removed as efficiently by each constriction and thus they will penetrate deeper into the active zone. One possible method to create a high shear zone is to size the flow injection area to achieve high shear through the first sand grains. The idea is to shred incoming flocs so they have a lower probability of being removed per pore and thus more of these small flocs penetrate deeper into the active filtration zone before being captured. Smaller flocs are also more dense and thus don't fill up the available volume in the constrictions as fast as the large flocs that they came from.

We need an estimate of the shear through the first pores as the water enters the sand. The Kozeny equation is valid up to a particle Reynolds number of 1 (:eq:`eq_Re_porous_media`). The Reynolds number at this proposed flow injection site will be much larger than 1 and thus the Ergun equation (:eq:`eq_Ergun`) that is valid for laminar and turbulent flow in porous media will be used.

We will use the Camp Stein velocity gradient to estimate injection velocity required to create very small flocs. The important parameter for floc break up is a force that can be obtained from the velocity gradient multiplied by the dynamic viscosity.

Solving :eq:`eq_G_CS_porous_media` for the approach velocity, :math:`v_a`, we obtain

.. math::

    v_a = \left( G_{CS}^2 \frac{2\nu D_{sand}}{f_{\phi}} \frac{\phi^4}{(1-\phi)} \right)^{\frac{1}{3}}

to estimate the injection area that should be used to break up flocs entering the sand bed.


.. _heading_floc_size_and_velocity_gradient_calculations:

Floc Size Calculations
=======================

`The code to make a figure showing the relationship between approach velocity and headloss can be found here. <https://colab.research.google.com/drive/15IrqdHgnk3NZVTiIuhQc6YdwFgquIHD1#scrollTo=Mlv81ZYLi1Gc&line=25&uniqifier=1>`_



.. _figure_Head_loss_Ergun_and_Kozeny:

.. figure:: ../Images/Head_loss_Ergun_and_Kozeny.png
   :width: 400px
   :align: center
   :alt: Head loss Ergun and Kozeny

   The Ergun and Kozeny equations are very similar even at approach velocities that are much larger than are used in rapid sand filtration. At very high velocities the turbulent term in the Ergun equation begins to be significant.

`The code for the following graph is found here. <https://colab.research.google.com/drive/15IrqdHgnk3NZVTiIuhQc6YdwFgquIHD1#scrollTo=g4nn81gGi9aS&line=3&uniqifier=1>`_


.. _figure_G_vs_approach_velocity:

.. figure:: ../Images/G_vs_approach_velocity.png
   :width: 400px
   :align: center
   :alt: G vs approach velocity

   The Camp Stein velocity gradient increases rapidly with approach velocity.


`See here for how the injection port width and injection velocity are determined. <https://colab.research.google.com/drive/15IrqdHgnk3NZVTiIuhQc6YdwFgquIHD1#scrollTo=KqQCyZaZjBJm&line=3&uniqifier=1>`_

The analysis above suggests that the approach velocity required to break flocs down to a dimension of :math:`20 \mu m` is approximately 80 mm/s. This is based on a VERY bad guesstimate of the relationship between floc size and shear.

We need to know how much energy would be expended to force the water through this high velocity injection zone. Once the water enters the sand it will spread radially in all directions. As the water spreads it will slow down and the head loss per distance traveled will decrease. We need to integrate this head loss over the first few centimeters to get an estimate of the injection head loss.

The velocity at distance r from the center of the injection line can be calculated from the velocity at :math:`r_0` by continuity.

.. math::

    v_{a_r} r= v_{a_{r_0}} r_0

.. math::

    v_{a_r}= v_{a_{r_0}} \frac{r_0}{r}



.. math::

    dh_f= \frac{dr}{2g D_{sand}} \left( 300 \frac{\nu (1-\phi)^2}{D_{sand} \phi^3}v_a  + 3.5 \frac{ (1-\phi) }{\phi^3}v_a^2 \right)

Now substitute for the approach velocity

.. math::

   \frac{dh_f}{dr}= \frac{1}{2g D_{sand}} \left[ 300 \frac{\nu (1-\phi)^2}{D_{sand} \phi^3}\left(v_{a_{r_0}} \frac{r_0}{r}\right)  + 3.5 \frac{ (1-\phi) }{\phi^3} \left(v_{a_{r_0}} \frac{r_0}{r}\right)^2 \right]


.. math::

    dh_f= \frac{v_{a_{r_0}}r_0}{2g D_{sand}} \left[ 300 \frac{\nu (1-\phi)^2}{D_{sand} \phi^3}\left( \frac{1}{r}\right)  + 3.5 \frac{ (1-\phi)v_{a_{r_0}}r_0 }{\phi^3} \left( \frac{1}{r}\right)^2 \right] dr

We will create terms to make the integration easier

.. math::

    a_0 = \frac{v_{a_{r_0}}r_0}{2g D_{sand}}

.. math::

    a_1 = 300 \frac{\nu (1-\phi)^2}{D_{sand} \phi^3}

.. math::

    a_2 = 3.5 \frac{ (1-\phi)v_{a_{r_0}}r_0 }{\phi^3}

Now we set up the numerical integration and integrate from the injection site to the radius where the velocity is equal to the filtration velocity.

`For an inlet that service two layers, see here to determine the head loss through the sand <https://colab.research.google.com/drive/15IrqdHgnk3NZVTiIuhQc6YdwFgquIHD1#scrollTo=PF8v34hSjJtx&line=11&uniqifier=1>`_

The analysis above suggests that a high velocity and high velocity gradient injection into the sand bed with the goal of breaking flocs into pieces that are 20 :math:`\mu m` in diameter would require about 12 cm of head loss. This is based on the assumption that the water would be able to flow radially from the injection point and thus rapidly slow down. Thus the head loss rapidly decreases with distance from the injection point.

This is an experiment worth trying. It will help us understand if large flocs result in poorer filter performance.

Floc Volume
============

The volume of solids deposited in one pore can be obtained based on the average diameter of clean pore constrictions, the diameter of the constricted pore after solids deposition, and the thickness of the deposit. We already have an estimate for the diameter of the constricted pore after solids deposition. The thickness of the deposit must be proportional to some other length scale. We initially hypothesized that the thickness of the deposit scaled with the diameter of the flocs that make it up. That led to the conclusion that increased coagulant dose would increase the total mass of solids that could be retained by the filter before breakthrough. That doesn't match experimental data and thus we now propose that the average thickness of the deposit scales with the sand grain size, or pore size, or pore separation distance. We will use the pore separation distance as our scaling parameter.

There are several options for estimating the areal extent of the constriction. We already have an estimate of the inner diameter of the constriction and thus all we need is an estimate of the outer extent of the deposited constriction.  One option would be to take the area of a circle defined by 3 spheres coming close together. That is a clear underestimate because the constriction must extend into the gaps between the spheres. A second option would be to use the porosity to estimate the average plane view area of the pores. If we assume that the pore must connect vertically and thus has a height :math:`\Lambda_{pore}`, then the plane view area is given by

.. math::

    A_{pore} = \phi\Lambda_{pore}^2

The area of the deposit is obtained by subtracting the constriction opening from the previous equation.

.. math::

    A_{deposit} = \Lambda_{pore}^2\left(\phi-\frac{v_a}{ v_{constriction}} \right)

The volume of the deposit is thus

.. math::

   \rlap{-} V_{deposit} = \Pi_{pore}^{deposit}\Lambda_{pore}^3\left(\phi-\frac{v_a}{ v_{constriction}} \right)

where :math:`\Pi_{pore}^{deposit}` a number much less than 1 that represents the fixed ratio between the thickness of the deposit and the pore separation distance.

The head loss per volume of particles deposited can be obtained by dividing the head loss per pore by the volume of particles per pore.

.. math::

    h_{l_{per_{deposit}}} = \frac{\bar v_{constriction}^2}{2g\Pi_{pore}^{deposit}\Lambda_{pore}^3\left(\phi-\frac{v_a}{ v_{constriction}} \right)}

If the primary goal for filter design were to decrease head loss per volume of solids deposited, then selecting larger sand (increasing :math:`\Lambda_{pore}`) would be the clear strategy. Increasing the sand diameter by a factor of two should decrease the head loss by a factor of 8. Increasing the approach velocity :math:`v_a`, results in a small increase in the head loss per volume of deposited material.

We need a method to connect turbidity removed by a filter into volume of deposited flocs. We will make this connection by first assuming that the flocs have a characteristic size based on a high shear event on their way into the filter. We begin with the relationship between the number of clay particles in a floc and the floc diameter.

.. math::

    D_{floc} = D_{clay} n_{clay}^\frac{1}{\Pi_{fractal}}

Where :math:`\Pi_{fractal}` is the volume based fractal dimension of a floc. We estimate :math:`\Pi_{fractal}` to have a value of 2.1. We can rearrange this equation and solve for the number of clay particles in a floc.

.. math::

    n_{clay} = \left(\frac{D_{floc}}{D_{clay}}\right)^{\Pi_{fractal}}

Now we can create a relationship for the concentration of clay in a floc dividing the mass of clay by the volume of the floc.

.. math::

    C_{clay_{floc}} = \frac{n_{clay}\rlap{-} V_{clay}\rho_{clay}}{\rlap{-} V_{floc}} = \frac{n_{clay}D_{clay}^3\rho_{clay}}{D_{floc}^3}= \frac{D_{clay}^3\rho_{clay}}{D_{floc}^3}\left(\frac{D_{floc}}{D_{clay}}\right)^{\Pi_{fractal}}

With one more simplification we obtain the desired equation for the clay concentration in a floc of given diameter.

.. math::
    C_{clay_{floc}} = \rho_{clay} \left(\frac{D_{clay}}{D_{floc}}\right)^{3-\Pi_{fractal}}

The mass of clay per pore is obtained by multiplying the deposit volume by the concentration of the flocs.

.. math::

    M_{clay_{pore}} =\rho_{clay}  \Pi_{pore}^{deposit}\Lambda_{pore}^3\left(\phi-\frac{v_a}{ v_{constriction}} \right)\left(\frac{D_{clay}}{D_{floc}}\right)^{3-\Pi_{fractal}}

The mass of clay per plan view area of the filter is obtained by multiplying by the number of pores per depth of the filter and dividing by the plan view area of a pore, :math:`\Lambda_{pore}^2`.

.. math::

    M_{clay_{filter}} =H_{filter} \rho_{clay}  \Pi_{pore}^{deposit}\left(\phi-\frac{v_a}{ v_{constriction}} \right)\left(\frac{D_{clay}}{D_{floc}}\right)^{3-\Pi_{fractal}}

According to this model, the mass of clay that can be held by a filter increases linearly with filter depth. The retained mass is independent of the sand size. This is an easy hypothesis to test. Note, however, that this model does not account for the depth of the active zone. Presumably the active zone depth may be greater for larger diameter media and thus breakthrough may occur sooner for larger diameter media.

If coagulant dose increases it will have two effects. The primary particle attachment strength will increase, the constricted velocity will increase, and the mass retained will increase. The size of the flocs will also increase and that will result in a slight decrease in the retained mass.

Thus it isn't immediately clear how changing the coagulant dose will change the maximum mass of retained particles. The evidence from the AguaClara filter theory team is that the mass of clay retained decreases as the coagulant dose increases.

The head loss per mass of particles deposited can be obtained by dividing the head loss per pore by the mass per pore.

.. math::

      h_{e_{permassclay}} = \frac{\bar v_{constriction_{max}}^2}{2g\rho_{clay}  \Pi_{pore}^{deposit}\Lambda_{pore}^3\left(\phi-\frac{v_a}{ v_{constriction}} \right)}\left(\frac{D_{floc}}{D_{clay}}\right)^{3-\Pi_{fractal}}

The head loss per mass of solids removed is significantly lower for larger sand sizes. When the coagulant dose increases the head loss increases rapidly because the constricted velocity increases and the floc diameter increases. Unfortunately we do not yet have a model describing floc size as a function of both velocity gradient and coagulant nanoparticle coverage.

Particle Removal Efficiency
===========================

Particle removal is complicated. We hypothesize that flocs form the deposits that change the flow from being wall shear dominated with a parabolic velocity profile to being uniform velocity flow through the constrictions. This uniform velocity profile transports a very small fraction of clay particles close enough to the deposit to be captured.

During filter ripening the particles that pass through the filter would be expected to be the primary particles because removal efficiency increases very rapidly with size. During the main part of the filter run the escaping particles are primary particles that weren't captured by the actively growing deposits. Breakthrough at the end of the filter run is caused by both primary particles and flocs.

The flocs form a series of actively growing deposits. The number of actively growing deposits in series is possibly a function of the average volume of the flocs (smaller flocs result in more active deposits) and the volume fraction of the flocs normalized by the volume fraction of the primary particles. If this dimensionless volume fraction increases there may be more active deposits and hence improved removal of primary particles.

Proposed Experiments
=====================

 #. Compare different sizes of sand media. Expect to get poorer removal efficiency with larger sand sizes, similar mass of particles retained at breakthrough, and much lower head loss.
 #. dual media. expect to find less head loss and poorer performance than single small media. And expect the smaller media to not contribute anything.
 #. How small could the sand media be? We could get better filter performance if we used smaller sand. Shallow sand beds are apparently fine and if we used smaller diameter sand the filter layer depth could be reduced even more. Why not use a 0.2 mm sand and 5 cm sand layers? If we offset the inlet and outlet branches (with branches spaced on 10 cm centers and inlet and outlet branches offset by 5 cm) there would still be a significant path length.
 #. Floc amendment. We could add floc hopper particles to the filter to increase the ratio of flocs to primary particles. Presumably this would reduce effluent turbidity IF there aren't many primary particles in the floc hopper. We could compare the prospects of using smaller sand grains vs adding floc amendment as strategies to get higher performing filters.
 #. Now that we know that sand doesn't remove clay without the help of flocs, could we invent a filter that could capture clay and other primary particles without requiring ripening? We need a filter media that has sharp edges or sudden constrictions that create high velocity near the edge. Washers with holes the size of constrictions aren't available.
