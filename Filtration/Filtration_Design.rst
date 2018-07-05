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

.. code:: python

  from aide_design.play import*
  x = 6




Porosity
===========

In understading how sand filtration works, porosity is one of the most important concepts to be familiar with. Porosity refers to the ratio of the void volume to the total volume of a control volume.

.. math::
  :label: porosity

    \phi_{FiSand} = \frac{\rlap{-} V_{voids}}{\rlap{-} V_{total}}


Porosity is determined by the geometry of the material in the control volume, but also by the size of the particles involved. If you have three different sized spheres (such as .0um clay, .2mm sand, and 1 cm gravel) in three different buckets, each bucket will have the same porosity. To minimize the porosity, the three materials could be mixed because the smaller materials would be filling the pore space of the larger material.

.. porosity image goes here! slide 1 in diagrams slide

In a sand filter, the porosity becomes especially important during the backwash process. In backwash, water is pushed upward into the sand. This force causes the sand to lift within the column of water. This lift causes expansion of the sand bed which is directly related to the new porosity of the sand bed, becasue the water volume occupied by sand has increased. This relationship is:

.. math::
  :label: backwash_porosity

  \phi_{FiSandBw} = \frac{\phi_{FiSand} H_{FiSand} A_{Fi} + \left( H_{FiSandBw} - H_{FiSand} \right) A_{Fi}}{H_{FiSandBw} A_{Fi}}

| Such that:
| :math:'phi_{FiSandBw}' = sand porosity during backwash
| :math:'phi_{FiSand}' = settled sand porosity
| :math:'H_{FiSand}' = height of sand in the filter
| :math:'H_{FiSandBw}' = height of sand during backwash
| :math:'A_{Fi}' = filter area

From this it becomes possible to directly relate porosity (as above) to the filter expansion ratio, which is simply the ratio of the heights of the expanded sand bed and the settled sand bed:

.. math::
  :label: filter_expansion_ratio

  \Pi_{FiBw} = \frac{H_{FiSandBw}}{H_{FiSand}}

| Such that:
| :math: 'Pi_{FiBw}' = the expansion ratio value
| :math:'H_{FiSand}' = height of sand in the filter
| :math:'H_{FiSandBw}' = height of sand during backwash





Backwash
===========
