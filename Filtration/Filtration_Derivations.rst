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



More things here!



Overall Goals:
- Uniformity in the sand bed through appropriate headloss

.. note::
  Pressure recovery occurs when fluid velocity slows down. This happens in the filter at the end of a manifold pipe, ebcause the fluid must stop at the end. This stoppage causes the pressure to increase locally, which then, when the fluid passes into the outlet, increases the local velocity leading to non-uniform flow.


Constraints:

Filtration Constraints
- inlet manifolds need to have small piezometric head relative to clean sand bed
- trunk and branches are short manifolds (fL/d) (**friction factor, L, diam?**), therefore: piezometric head variablitty dominated by pressure recovery as given by :math:`\frac{V^2}{2g}` with the velocity as the initial velocity of the manifold
  - this is the limiting constraint for the velocity in the trunk and branches, which can be relaxed with added headloss in the slots
- limit the imbalance between inlets that carry water for two layers and inlets that carry water for one layer.
  - *perhaps top/bottom inlet should have half the number of slots*
  - current assumption: backwash branches will have half the slot areas
- if slots are used to generate head loss (to improve flow distribution) sand blocking, :math:`(1-\epsilon)` during filtration must be accounted for
- the slots are not blocked during backwash (excepy maybe at initiation)

Backwash Constraints
- flow rate from each slot/hole must be close to average (within *20%*)
- as there is not head loss in fluidized bed, the manifold must be designed with the appropriate head loss for indpendent uniform flow distribution
- headloss through slots/holes will be 36x greater during backwash because of 6x increase in velocity
- to make flow more uniform:
  - decrease head loss + pressure recovery in manifold
  - increase head loss in slots
- slot head loss must not impede the filtration mode capacity
- this sets maximum headloss for each mode.
  - during filtration <10% clean bed head loss
  - during backwash <36x the filtration limits

  Additional concerns:
  - there are two manifold systems, the trunks into the branches and the branches into the slots. Thus pressure recovery must be small in both trunk and branches so that the slots can reconcile the changes in flow, because flow distribution is fairly uniform in short manifold systems when total port area is equal to or less than manifold area.

Sand Layer Thickness as Function of trunk diameters
====================================================

Flow Distribution constraint: ratio of pressure recovery to clean bed head loss
================================================================================

There are three flow distribution problems in the filter design:
1. Between slots along manifold branches
2. Between branches along manifold trunks
3. Between filter layers

The relative distribution of the flow through a particular path is defined as:

:math:`\Pi_Q = \frac{Q_{long}}{Q_{short}} = \sqrt{\frac{C_p_{Short}}{C_p_{Short}}}`

| Such that:
| :math:`\Pi_Q =` the ratio of flow
| :math:`Q_{long} =` the flow through the longest filter path (lowest layer, at the furthest slot on the furthest branch)
| :math:`\Q_{Long} =` the flow through the shortest filter path (top layer, closest slot on the first branch)
| :math:`C_{p_{short}} =` pressure coefficient at the end of the shortest path
| :math:`C_{p_{long}} =` pressure coefficient at the end of the longest path

:math:`C_p` is defined in Fluids review (**Make this actually be defined here**)

:math:`\Pi_Q = \frac{Q_{long}}{Q_{short}} = \sqrt{\frac{H_{LSand}-PR}{H_{LSand}}}`

| Such that:
| :math:`H_LSand = ` the head loss in the sand bed
| :math:`PR =` pressure recovery (as defined by: :math:`\frac{V^2}{2g}`)


:math:`PR = H_{LSand}(1- \Pi_Q^2)`

These relationships define the head loss constraints of the filter.

The ratio, :math:`\Pi_{FiManifoldQ}` has been arbitrarily given a value of :math:`0.85`, meaning the flow exiting the longest path is 85% of the flow exiting from the shortest path.

Thus from above:

:math:`1 - \Pi_{FiManifoldQ}^2 = .278 = \Pi_{FiManifoldHeadLoss}`

Where the ratio of the pressure recovery in the branches to the head loss through the clean bed (or through just the slots/holes in backwash) is:

:math:`\Pi_{FiManifoldHeadLoss} = \frac{PR}{H_{LSand}}`







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
