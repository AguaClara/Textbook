.. _filtration:


*************
Filtration
*************



.. _filter_types:

=============
Filter Types
=============

The principal difference in various filters is the difference in velocity of water through them. This in turn determines the plan area of the filter for a particular flow.

For a multistage filter system, the filter areas for the Dynamic, Roughing, and Slow Sand filters are included in a total are. For a given flow, and the velocity for each filter type the total area is:


.. math::
  :label: area_stuff

    A_{Total} = \frac{Q}{v_{Dynamic}} + \frac{Q}{v_{Rough}} + \frac{Q}{v_{Slow}}

Using this formula it becomes easy to see the relative sizes of different filter systems. **Note: Clare, consider adding the table from slide 23 here.**

Understanding the amount of area requires for this component makes it easy to see why certain systems would be preferable to others, but also that overall filtration is only a polishing step and cannot treat as well as other unit processes.




.. _porosity:

Porosity
===========

In understading how sand filtration works, porosity is one of the most important concepts to be familiar with. Porosity refers to the ratio of the void volume to the total volume of a control volume.

.. math::
  :label: porosity

    \phi_{FiSand} = \frac{\rlap{-} V_{voids}}{\rlap{-} V_{total}}


Porosity is determined by the geometry of the material in the control volume, but also by the size of the particles involved. If you have three different sized spheres (such as .0um clay, .2mm sand, and 1 cm gravel) in three different buckets, each bucket will have the same porosity. To minimize the porosity, the three materials could be mixed because the smaller materials would be filling the pore space of the larger material.

.. porosity image goes here! slide 1 in diagrams slide

One way that the relative size of particles is characterized is by describing the size of the smallest 10% of grains, and the smallest 60% of grains. That is:

.. math::
  :label: D_10_sand

    \D_{10} = the sieve size that passes 10% by mass of the sand through

.. math::
  :label: D_60_sand

    \D_{60} = the sieve size that passes 60% by mass of the sand through

:math:'D_{10}' is used for particle removal models, and :math:'D_{60}' is used for hydrualic modeling.

The relationship of the two, the uniformity coeffecient:

.. math::
  :label: uniformity_coefficient

    UC = \frac{D_{60}}{D_{10}}

describes the uniformity of the sand. A :math:`UC = 1` indicates that every grain of sand is the same size, which is the ideal case. A large :math:`UC` is indicative of a wide range of grain sizes which can cause trouble during filter operation and backwash, as stratification occurs and the porosity changes with respect to depth in the filter. Using the minimum fluidization velocity equation from sedimentation (=====) and adapted for the physical characteristis of sand, the water velocity needed during backwash can be seen as:

.. math::
  :label: minimum_fluidization_velocity_sand

  V_{MinFluidization} = \frac{\phi_{FiSand}^3 g D_{60}^2}{36 k \nu \left( 1 - \phi_{FiSand} \right)}
  \left( \frac{\rho_{Sand}}{\rho_{Water}} - 1 \right)


From this equation it can easily be seen that if the diameter of the sand at the top is half the diameter of the sand at the bottom, it will fluidize at one quarter the velocity. This result indicates that fluidization occurring at the top of the filter is **not** indicative of fluidization at the bottom.

This result is also important in determining the expansion of the sand bed during the backwash process. As the sand fluidizes within the filter, it is lifted causing a change in porosity of the sand bed (as the volume of water occupied by the sand is increased.) The porosity and height of the sand bed are directly related through the following equation:


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




.. _backwash:

Backwash
===========

When considering backwash design, there are two main factors that constitute a dilemma. The first, backwash velocity must be must greater than filtration velocity (to expand the sand bed), and second, the backwash water must be clean water (cleaning with dirty water introduces more particles into the filter). This limits the paths water can take during the backwash process. The conventional options include pumping it back from the storage tank, using a set of parallel fiters to backwash one filter at a time, or storing the filtered water at an adequate elevation.

**brief example here?**

To avoid electricity, pumps can be immeidately ruled out.

Parallel filters would require too much area and wouldn't work well under low flow conditions:

Given:

.. math::
 :label: filter_example_conditions
  Q_{Plant} = 6 \, \frac{L}{s} \,\,\,\,\, V_{Fi} = 1.8 \, \frac{mm}{s} \,\,\,\,\, V_{Bw} = 9 \, \frac{mm}{s}

As the ratio of the backwash velocity to the filter velocity is 5, 5 filters will be needs to provide enough flow to backash one: Therefore the number of parallel filters is 6:

:math:`N_{Fi} = \frac{V_{Bw}}{V_{Fi}} + 1 = 6`

In this system, the water exiting five of the filters would be diverted to backwash one of the other filters. In addtion to requiring the plan view area of 6 filters, each filter would need to be backwashed independently, meaning it would take 6x longer and use 6x the water as compared to just having one filter. Another detriment to this system is that in low flows (such as drought conditions) not enough water would be passing through the system to backwash at points since all the water is diverted to backwash.

The third option, elevating the filtered water to provide enough head to cause backwash, is also unfeasible.

**add the third one at some later point if it's useful**

How can we find a solution?

If the velocities could be more similar less space would be needed!

This could be accomplished in several ways, such as decreasing the media density thus lowering velocity to fluidize it, decrease the media diameter thus lowering the fluidization velocity, or make a more compact filter which filters in parallel and backwashes in series.

As changing the material characteristics of the sand is challenging, a more compact filter is the chosen design. In the design, six layers of sand are stacked, there are three inlets, and four outlet

This overall design can be seen in Figure XXXXX.
















.. _siphon:

Siphon
========
