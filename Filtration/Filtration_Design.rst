.. _title_filtration:


*******************
Filtration Design
*******************

This section deals with search for a self-backwashing filter which is functional over a wide range of flows. While in basic concept,running water through a sand bed, filters are the simplest of the unit processes, the are probably the most complex in design within an AguaClara plant because they are not inherently self-cleaning. Additionally. The search to overcome this problem has led to the development of a Stacked Rapid Sand Filter (StaRS Filter) a novel filter design which provides a hydraulic backwash system and works over a large range of flows with some adpatation for small flows.


.. _heading_filtration_terms:

Important Terms and Equations
===============================
Terms:

1. Porosity
2. StaRS Filter
3. Backwash


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
    A_{Total} = \frac{Q}{v_{Dynamic}} + \frac{Q}{v_{Rough}} + \frac{Q}{v_{Slow}}

Using this formula it becomes easy to see the relative sizes of different filter systems, we as how complex filter system quickly add up in terms of size. **Note: Clare, consider adding the table from slide 23 here.** :numref:`figure_relative_area_of_filtration!`shows the relative area of various filtration technologies.

.. _figure_relative_area_of_filtration:

.. figure:: /Images/figure_relative_area_of_filtration.png
  :align: center
  :alt: table showing the relative areas of multistage filtration techniques to AguaClara unit processes
  :width: 80%


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
| :math:`h_{l_{FiBw}` = the headloss in the fluidized bed
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

When considering backwash design, there are two main factors that constitute a dilemma. The first, backwash velocity must be must greater than filtration velocity (to expand the sand bed), and second, the backwash water must be clean water (cleaning with dirty water introduces more particles into the filter). This limits the paths water can take during the backwash process. The conventional options include pumping it back from the storage tank, using a set of parallel fiters to backwash one filter at a time, or storing the filtered water at an adequate elevation. Due to energy limitations and space constraints, the conventional solutions are simply not feasible for this system. Examples that illustrate why they cannot work can be found in the derivations sections(?)(or the examples?)

**brief example here?**

To avoid electricity, pumps can be immeidately ruled out.

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

As changing the material characteristics of the sand is challenging, a more compact filter is the chosen design. As it happens this innovation results in a more concpetually difficult filter. In the design, six layers of sand are stacked, there are four inlets, and three outlets which are all in use during filtration. During backwash only one inlet is used and the backwash water is discarded through a separate manifold. Throughout this section, figures and images will be the best methods to understand the design flow through the system, and will be supplemented by the text.

This overall design can be seen in Figure XXXXX.

(figure of the full system)

Tasks for clare for Thursday + Friday morning: insert images! none of them are in yet. Save as pngs. streamline the way you want this to work as well. like overall structure

In is most basic schema, the filter is a series of pipes leading into a deep box with 1.2 meters of sand (for most filters)

As a parcel of water traveling in the filter the first part of the filter is the inlet box. The inlet box is a shallow box with four holes in the bottom. The holes lead into four pipes which lead into different levels of the sand filter. At the outlet of each of these pipes into the sand filter is a structure designed to spread the flow over the entire footprint area of the filter. These structures have slots which allow water out of the inlet pipes into the sand bed. Across a layer of sand from the inlet is an outlet pipe in the same shapes as the slotted pipe inlets. Water passes into the pipes and up to the fitler outlet box where it only needs to be chlorinated before being distributed.

Steps of designing a filter.
1. Calculate backwash velocity from sand diameter
  - complicating factors:
      - wall shear
      - lift as a unit and fall together
      - stratification will always occur if a range of sizes exists
2.





















.. _siphon:

Siphon
========

Backwash is initiated through the activation of a siphons system. In the sipohoning process two things must happen for a success.
  1. Backwash can be initiated at any point in time
  2. Backwash can be prevented with the siphon as well

  In under the siphon, the ideal gas law, **Add a ref**, is the most important equation to understand how it is initiated. 
