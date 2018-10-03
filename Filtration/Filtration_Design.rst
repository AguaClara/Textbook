.. _title_filtration:


*******************
Filtration Design
*******************

This section deals with search for a self-backwashing filter which is functional over a wide range of flows. While in basic concept, running water through a sand bed, filters are the simplest of the unit processes, the are probably the most complex in design within an AguaClara plant because they are not inherently self-cleaning. Additionally. The search to overcome this problem has led to the development of a Stacked Rapid Sand Filter (StaRS Filter) a novel filter design which provides a hydraulic backwash system and works over a large range of flows with some adaptation for small flows.


.. _heading_filtration_terms:

Important Terms and Equations
===============================
Terms:

1. Porosity
2. StaRS Filter
3. Backwash
4. Pressure Recovery


Equations:

1.

.. _heading_aguaclara_filtration_technologies:

AguaClara Flow Control and Measurement Technologies
=====================================================




.. _heading_filter_types:

=============
Filter Types
=============

The principal difference in various filters is the difference in velocity of water through them. This in turn determines the plan view area of the filter for a particular flow.

For a multistage filter system, the filter areas for the Dynamic, Roughing, and Slow Sand filters are included in a total area. For a given flow, and the velocity for each filter type the total area is:


.. math::
   :label: area_stuff

    A_{Total} = \frac{Q}{v_{Dynamic}} + \frac{Q}{v_{Rough}} + \frac{Q}{v_{Slow}}

Using this formula it becomes easy to see the relative sizes of different filter systems, we as how complex filter system quickly add up in terms of size. This table shows the relative area of various filtration technologies.


Understanding the amount of area requires for this component makes it easy to see why certain systems would be preferable to others, but also that overall filtration is only a polishing step and cannot treat as well as other unit processes, predominantly the flocculation-sedimentation combination.


.. _heading_porosity:

Porosity
===========

In understading how sand filtration works, porosity is one of the most important concepts to be familiar with. Porosity refers to the ratio of the void volume to the total volume of a control volume.

.. math::
   :label: porosity

    \phi_{FiSand} = \frac{\rlap{-} V_{voids}}{\rlap{-} V_{total}}


Porosity is determined by the geometry of the material in the control volume, but also by the size of the particles involved. If you have three different sized spheres (such as .0um clay, .2mm sand, and 1 cm gravel) in three different buckets, each bucket will have the same porosity as seen in :numref:`figure_porosity`. To minimize the porosity, the three materials could be mixed because the smaller materials would be filling the pore space of the larger material.

.. _figure_porosity:

.. figure:: Images/figure_porosity.png
    :align: center
    :alt: This figure illustrates how different sized materials have the same total bulk porosity

    Within each box, the spheres are different sizes. However the total porosity is the same. To minimize the pore space, the smaller particles could be used to fill the spore space between the larger particles, though in a filter this is not necessarily ideal.

One way that the relative size of particles is characterized is by describing the size of the smallest 10% of grains, and the smallest 60% of grains. That is:

:math:`D_{10}` = the sieve size that passes 10% by mass of sand through

:math:`D_{60}` = the sieve sixe that passes 60% by mass of sand through

:math:`D_{10}` is used for particle removal models, and :math:`D_{60}` is used for hydrualic modeling.

The ratio of the two is the uniformity coeffecient:

.. math::
   :label: uniformity_coefficient

    UC = \frac{D_{60}}{D_{10}}

The uniformity coefficient describes the uniformity of the sand. A :math:`UC = 1` indicates that every grain of sand is the same size, which is the ideal case. A large :math:`UC` is indicative of a wide range of grain sizes which can cause trouble during filter operation and backwash, as stratification occurs and the porosity changes with respect to depth in the filter, which affects the requirements for backwash.


During backwash, the sand is fluidized and the sand bed expands. This expansion causes a change in porosity of the sand bed (as the volume of water occupied by the sand is increased). The porosity and height of the sand bed are directly related through the following equation:

.. math::
   :label: backwash_porosity

    \phi_{FiSandBw} = \frac{\phi_{FiSand} H_{FiSand} A_{Fi} + \left( H_{FiSandBw} - H_{FiSand} \right) A_{Fi}}{H_{FiSandBw} A_{Fi}}

| Such that:
| :math:`phi_{FiSandBw}` = sand porosity during backwash
| :math:`phi_{FiSand}` = settled sand porosity
| :math:`H_{FiSand}` = height of sand in the filter
| :math:`H_{FiSandBw}` = height of sand during backwash
| :math:`A_{Fi}` = filter area

From this it becomes possible to directly relate porosity (as above) to the filter expansion ratio, which is simply the ratio of the heights of the expanded sand bed and the settled sand bed:

.. math::
   :label: filter_expansion_ratio

  \Pi_{FiBw} = \frac{H_{FiSandBw}}{H_{FiSand}}

| Such that:
| :math:`Pi_{FiBw}` = the expansion ratio value
| :math:`H_{FiSand}` = height of sand in the filter
| :math:`H_{FiSandBw}` = height of sand during backwash



.. _heading_headloss_requirements:

Headloss Requirements
======================
One of the key parameters in design of a filter is the headloss through the system because it determines the required fluid velocity for backwash. The Karmen Kozeny Equation, an adaptation of the Hagen-Pouseille equation (ref from elsewhere, not linked yet) describes the headloss through a clean bed during filtration.

.. math::
   :label: karmen_kozeny_clean_bed

    \frac{h_l}{H_{FiSand}} = 36 k \frac{\left( 1 - \phi_{FiSand} \right)^2}{\phi_{FiSand}^3} \frac{\nu V_{Fi}}{g D_{60}^2}

| Such that:
| :math:`h_l` = headloss in sand bed
| :math:`H_{FiSand}` = the sand bed depth/length of flow paths
| :math:`phi_{FiSand}` = porosity of sand
| :math:`nu` = kinematic viscosity
| :math:`V_{Fi}` = the water velocity in the filter
| :math:`D_{60}` = the size of the sand
| :math:`g` = gravity
| :math:`k` = Kozeny constant (5 for most filtration cases)

This equation is valid for Reynolds numbers less than 6. Where:
:math:`{\rm Re}  = \frac{D_{60} V_{Fi}}{\nu}`

The headloss during backwash is taken as the design parameter, so other values are constructed around it.

The following equation describes the headloss through the fluidized bed:

.. math::
   :label: headloss_fluidzed_bed

    \frac{h_{l_{FiBw}}}{H_{FiSand}} = \left( 1 - \phi_{FiSand} \right)\left( \frac{\rho_{Sand}}{\rho_{Water}} - 1 \right)

| Such that:
| :math:`h_{l_{FiBw}}` = the headloss in the fluidized bed
| :math:`H_{FiSand}` =  the depth of the settled sand bed
| :math:`phi_{FiSand}` = the settled sand porosity
| :math:`rho_{Sand}`  = the sand density
| :math:`rho_{Water}` = the water density

Using these two equations the minimum velocity for snad fluidization can be found!

.. math::

   :label: minimum_fluidization_velocity_sand

   V_{MinFluidization} = \frac{\phi_{FiSand}^3 g D_{60}^2}{36 k \nu \left( 1 - \phi_{FiSand} \right)} \left( \frac{\rho_{Sand}}{\rho_{Water}} - 1 \right)

From this equation it can easily be seen that if the diameter of the sand at the top is half the diameter of the sand at the bottom, it will fluidize at one quarter the velocity. This result indicates that fluidization occurring at the top of the filter is **not** indicative of fluidization at the bottom.

This parameter is the most important parameter to consider as it is a property of the sand not of the water!



.. _heading_backwash:

Backwash
===========

When considering backwash design, there are two main factors that constitute a dilemma. The first, backwash velocity must be must greater than filtration velocity (to expand the sand bed), and second, the backwash water must be clean water (cleaning with dirty water introduces more particles into the filter). This limits the paths water can take during the backwash process. The conventional options include pumping it back from the storage tank, using a set of parallel filters to backwash one filter at a time, or storing the filtered water at an adequate elevation. Due to energy limitations and space constraints, the conventional solutions are simply not feasible for this system. Examples that illustrate why they cannot work can be found in the derivations sections(?)(or the examples?)

**brief example here?**

To avoid electricity, pumps can be immediately ruled out.

Parallel filters would require too much area and wouldn't work well under low flow conditions:

Given:

.. math::
   :label: filter_base_conditions

    Q_{Plant} = 6 \, \frac{L}{s} \,\,\,\,\, V_{Fi} = 1.8 \, \frac{mm}{s} \,\,\,\,\, V_{Bw} = 9 \, \frac{mm}{s}

As the ratio of the backwash velocity to the filter velocity is 5, 5 filters will be needs to provide enough flow to backash one: Therefore the number of parallel filters is 6:

:math:`N_{Fi} = \frac{V_{Bw}}{V_{Fi}} + 1 = 6`

In this system, the water exiting five of the filters would be diverted to backwash one of the other filters. In addtion to requiring the plan view area of 6 filters, each filter would need to be backwashed independently, meaning it would take 6x longer and use 6x the water as compared to just having one filter. Another detriment to this system is that in low flows (such as drought conditions) not enough water would be passing through the system to backwash at points since all the water is diverted to backwash.

The third option, elevating the filtered water to provide enough head to cause backwash, is also unfeasible.

**add the third one at some later point if it's useful**

How can we find a solution?

If the velocities could be more similar the filter could work!

This could be accomplished in several ways: such as decreasing the media density thus lowering velocity to fluidize it, decrease the media diameter thus lowering the fluidization velocity, or make a more compact filter which filters in parallel and backwashes in series.

As changing the material characteristics of the sand is challenging, a more compact filter is the chosen design. As it happens this innovation results in a more conceptually difficult filter. In the design, six layers of sand are stacked, there are four inlets, and three outlets which are all in use during filtration. During backwash only one inlet is used and the backwash water is discarded through a separate manifold. Throughout this section, figures and images will be the best methods to understand the design flow through the system, and will be supplemented by the text.

This overall design can be seen in Figure XXXXX.

(figure of the full system)

Tasks for Clare for Thursday + Friday morning: insert images! none of them are in yet. Save as pngs. streamline the way you want this to work as well. like overall structure

In is most basic schema, the filter is a series of pipes leading into a deep box with 1.2 meters of sand (for most filters)

As a parcel of water traveling in the filter the first part of the filter is the inlet box. The inlet box is a shallow box with four holes in the bottom. The holes lead into four pipes which lead into different levels of the sand filter. At the outlet of each of these pipes into the sand filter is a structure designed to spread the flow over the entire footprint area of the filter. These structures have slots which allow water out of the inlet pipes into the sand bed. Across a layer of sand from the inlet is an outlet pipe in the same shapes as the slotted pipe inlets. Water passes into the pipes and up to the filter outlet box where it only needs to be chlorinated before being distributed.

Steps of designing a filter.
1. Calculate backwash velocity from sand diameter
- complicating factors:
-- wall shear
-- lift as a unit and fall together
--- stratification will always occur if a range of sizes exists
2.





















.. _siphon:

Siphon
========

Backwash is initiated through the activation of a siphons system. In the siphoning process two things must happen for a success.
  1. Backwash can be initiated at any point in time
  2. Backwash can be prevented with the siphon as well

  In under the siphon, the ideal gas law, **Add a ref**, is the most important equation to understand how siphoning works..




------------------------------------


Design from MathCad adapted for me
==================================

Overall Goals:
- Uniformity in the sand bed through appropriate headloss

.. note::
  Pressure recovery occurs when fluid velocity slows down. This happens in the filter at the end of a manifold pipe, ebcause the fluid must stop at the end. This stoppage causes the pressure to increase locally, which then, when the fluid passes into the outlet, increases the local velocity leading to non-uniform flow.


Constraints:

Filtration Constraints
- inlet manifolds need to have small piezometric head relative to clean sand bed
- trunk and branches are short manifolds (fL/d) (**friction factor, L, diam?**), therefore: piezometric head variability dominated by pressure recovery as given by :math:`\frac{V^2}{2g}` with the velocity as the initial velocity of the manifold
-- this is the limiting constraint for the velocity in the trunk and branches, which can be relaxed with added headloss in the slots
- limit the imbalance between inlets that carry water for two layers and inlets that carry water for one layer.
-- *perhaps top/bottom inlet should have half the number of slots*
-- current assumption: backwash branches will have half the slot areas
- if slots are used to generate head loss (to improve flow distribution) sand blocking, :math:`(1-\epsilon)` during filtration must be accounted for
- the slots are not blocked during backwash (excepy maybe at initiation)

Backwash Constraints:
- flow rate from each slot/hole must be close to average (within *20%*)
- as there is not head loss in fluidized bed, the manifold must be designed with the appropriate head loss for indpendent uniform flow distribution
- headloss through slots/holes will be 36x greater during backwash because of 6x increase in velocity
- to make flow more uniform:
-- decrease head loss + pressure recovery in manifold
-- increase head loss in slots
- slot head loss must not impede the filtration mode capacity
- this sets maximum headloss for each mode.
-- during filtration <10% clean bed head loss
-- during backwash <36x the filtration limits

  Additional concerns:
  - there are two manifold systems, the trunks into the branches and the branches into the slots. Thus pressure recovery must be small in both trunk and branches so that the slots can reconcile the changes in flow, because flow distribution is fairly uniform in short manifold systems when total port area is equal to or less than manifold area.

Sand Layer Thickness as Function of trunk diameters
====================================================

Flow Distribution constraint: ratio of pressure recovery to clean bed head loss
================================================================================

Number of filters
===================

Clean bed head loss
====================

Auxilliary box widths and plumbing
===================================

Number of manifold branches
==============================

Filter box dimensions and manifold inlet pipes
===============================================

Manifold slot/orifice design
===============================

Plumbing head losses
======================

Total Sand depth and backwash head loss
========================================

Path head loss calculations and flow distribution between layers
=================================================================

Siphon design
===============

Inlet channel and elevations
=============================

Elevations
===========

Inlet Weir Design
==================

Entrance and overflow box lengths (X-direction)
===============================================

Siphon Valve sizes
===================

Sand Removal Pipe
==================

Trunk Line purge valves
=========================

Main plant drain channel
=========================

Sand Volume
=============

Backwash Lagoon
=================
