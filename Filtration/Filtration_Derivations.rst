.. _title_filtration_derivations:


***********************
Filtration Derivations
***********************

.. _derivation_backwash_headloss_force_balance:


To determine the head loss during backwash a force balance should be performed between the water and the sand per unit of filter area (thus pressure values will be yielded). A schematic for this system is shown below:

.. _figure_force_balance:
.. figure:: Images/figure_force_balance.png
    :align: center
    :width: 50%
    :alt: This figure is a simplified schematic of the filter force balance.


The pressure from the water:

.. math::
  P_{Manometer} = \rho_{Water} g \left( H_{W_1} + H_{W_2} + \phi_{FiSand} H_{FiSand} \right) + \rho_{Sand} g \left( 1 - \phi_{FiSand} \right) H_{FiSand}

| Such that:
| :math:`P_{Manometer} =` total height from the bottom of the filter to the inlet box
| :math:`\rho_{Water} =` density of water
| :math:`H_{W_1} =` the distnace from the top of the settled sand bed to the water surface in the filter
| :math:`H_{W_2} =` the height of the water below the sand bed but within the filter
| :math:`\phi_{FiSand} =` porosity of sand
| :math:`H_{FiSand} =` height of the filter bed
| :math:`\rho_{Sand} =` density of sand

The pressure from the sand:

.. math::
  P_{Manometer} = \rho_{Water} g \left( H_{W_1} + H_{W_2} + H_{FiSand} + h_{l_{FiBw}} \right)


| Such that:
| :math:`h_{l_{FiBw}} =` the difference in height of the inlet and water surface height during backwash; the backwash head loss


Setting them equal for a force balance:

.. math::
  \rho_{Water} g \left( H_{W_1} + H_{W_2} + \phi_{FiSand} H_{FiSand} \right) + \rho_{Sand} g \left( 1 - \phi_{FiSand} \right) H_{FiSand} = \rho_{Water} g \left( H_{W_1} + H_{W_2} + H_{FiSand} + h_{l_{FiBw}} \right)

Which simplifies to:

.. math::
  h_{l_{FiBw}} = \frac{\rho_{Sand} - \rho_{Water}}{\rho_{Water}} \left( 1 - \phi_{FiSand} \right) H_{FiSand}
  or
  h_{l_{FiBw}} = H_{FiSand} \left( 1 - \phi_{FiSand} \right)  \left( \frac{\rho_{Sand}}{\rho_{Water}} - 1 \right)

This result gives a ratio of the head loss during backwash to the height difference during forward operation. With :math:`\phi_{FiSand} = 0.4` and :math:`\rho_{Sand} = 2650 kg/m^3` the value of this ratio is:

.. math::
  \left( 1- \Phi_{FiSand} \right) \left( \frac{\rho_{FiSand}}{\rho_{Water}} - 1 \right) = 0.99

Thus:

.. math::
  h_{l_{FiBw}} = H_{FiSand} * 0.99






.. _siphon_derivation:

Siphon Derivation
====================

The siphon is defined by its airtrap!
