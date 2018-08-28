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

.. math::  h_{l_{FiBw}} = H_{FiSand} * 0.99






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
- trunk and branches are short manifolds (fL/d) (**friction factor, L, diam?**), therefore: piezometric head variablitty dominated by pressure recovery as given by :math:`\frac{V^2}{2g}` with the velocity as the initial velocity of the manifold 1. ------ this is the limiting constraint for the velocity in the trunk and branches, which can be relaxed with added headloss in the slots
- limit the imbalance between inlets that carry water for two layers and inlets that carry water for one layer. -1 *perhaps top/bottom inlet should have half the number of slots* -2 current assumption: backwash branches will have half the slot areas
- if slots are used to generate head loss (to improve flow distribution) sand blocking, :math:`(1-\epsilon)` during filtration must be accounted for
- the slots are not blocked during backwash (excepy maybe at initiation)

Backwash Constraints
- flow rate from each slot/hole must be close to average (within *20%*)
- as there is not head loss in fluidized bed, the manifold must be designed with the appropriate head loss for indpendent uniform flow distribution
- headloss through slots/holes will be 36x greater during backwash because of 6x increase in velocity
- to make flow more uniform: 1. decrease head loss + pressure recovery in manifold 2.  increase head loss in slots
- slot head loss must not impede the filtration mode capacity
- this sets maximum headloss for each mode: 1. during filtration <10% clean bed head loss 2. during backwash <36x the filtration limits

  Additional concerns:
  - there are two manifold systems, the trunks into the branches and the branches into the slots. Thus pressure recovery must be small in both trunk and branches so that the slots can reconcile the changes in flow, because flow distribution is fairly uniform in short manifold systems when total port area is equal to or less than manifold area.



Flow Distribution constraint: ratio of pressure recovery to clean bed head loss
==================================================================================

There are three flow distribution problems in the filter design:
1. Between slots along manifold branches
2. Between branches along manifold trunks
3. Between filter layers

The relative distribution of the flow through a particular path is defined as:

.. math::

  \Pi_Q = \frac{Q_{long}}{Q_{short}} = \sqrt{\frac{C_{p_{Short}}}{C_{p_{Short}}}}

| Such that:
| :math:`\Pi_Q =` the ratio of flow
| :math:`Q_{long} =` the flow through the longest filter path (lowest layer, at the furthest slot on the furthest branch)
| :math:`\Q_{Long} =` the flow through the shortest filter path (top layer, closest slot on the first branch)
| :math:`C_{p_{short}} =` pressure coefficient at the end of the shortest path
| :math:`C_{p_{long}} =` pressure coefficient at the end of the longest path

:math:`C_p` is defined in Fluids review (**Make this actually be defined here**)

.. math::

  \Pi_Q = \frac{Q_{long}}{Q_{short}} = \sqrt{\frac{H_{LSand}-PR}{H_{LSand}}}


| Such that:
| :math:`H_LSand =` the head loss in the sand bed
| :math:`PR =` pressure recovery (as defined by: :math:`\frac{V^2}{2g}`)


:math:`PR = H_{LSand}(1- \Pi_Q^2)`

These relationships define the head loss constraints of the filter.

The ratio, :math:`\Pi_{ManifoldQ}` has been arbitrarily given a value of :math:`0.85`, meaning the flow exiting the longest path is 85% of the flow exiting from the shortest path.

Thus from above:

:math:`1 - \Pi_{ManifoldQ}^2 = .278 = \Pi_{ManifoldHeadLoss}`

Where the ratio of the pressure recovery in the branches to the head loss through the clean bed (or through just the slots/holes in backwash) is:

:math:`\Pi_{ManifoldHeadLoss} = \frac{PR}{H_{LSand}}`

Though the piezometric head profiles fothe inlet and outlet manifolds for the middle layers may be parallel, meaning the pressure recovery is less constrained for a good flow distribution, we still need a tight constraint for the outer manifolds where the velocity is 1/2 and the PR is 1/4 that of the inner layer, while smaller still in the bottom-most manifold where the velocity head is tiny as the diameter is larger.




.. _heading_n_filter:

Number of filters
===================

Parameters:
:math:`PR_{ManBranchEst} = 0.8cm`
:math:`ND_{BwTrunkMax} = 8in`
:math:`HL_{BWSlotsEst}= 10cm`
:math:`PR_{BwManifoldMax} = HL_{BWSlotsEst}*\Pi_{ManifoldHeadLoss}`

**Explain where these came from**

First Constraint: Pressure Recovery in trunks during forward Filtration;

Use the Kozeny equation to find the headloss through the clean bed. Assume the depth of the sand bed as calculated above in the :ref:`_heading_sand_layer_from_trunk_diam` section

Second Constraint: Pressure recovery in lowest trunk during backwash

.. math:: V_{BwManTrunkMaxPR} = \sqrt{2g*(HL_{BWSlotsEst}*\Pi_{ManifoldHeadLoss} - PR_{ManBranchEst} )}

This velocity is used to find the flow possible in the pipe, using the inner diameter of the pipe, and is rounded to the nearest 1 L/s.

.. math:: Q_{PRBwTrunk} = \pi*ID_{BwTrunkMax}^2 * V_{BwManTrunkMaxPR}

The flow set by the maximum pressure recovery is then the lesser of the flow calculated from forward filtration or backwsh. This value is the maximum flow through on filter.

Knowing the maximum flow through one filter, finding the number of filters is simple.

If the plant flow is less than 16 L/s, EStaRS should be used, as having two filters is ideal, but the minimum filter flow is 8 L/s, which is not possible below 16 L/s.
In all other cases at least 2 filters should be used to allow for backwash during low flows.

Thus the number of filters for plants is:

.. math:: max(\frac{Q_{Plant}}{Q_{MaxPR}}, 2)

The flow through each filter given the number of filters:

.. math:: Q_{Fi} = \frac{Q_{Plant}}{N_{Fi}}

Within a filter, the flow through each layer:

.. math:: Q_{Layer} = \frac{Q_{Fi}}{N_{Layer}}

This is the flow that sets the pipe size for each trunk within each layer of the filter. The Nominal Diameter (ND) of the trunk pipes is then determined using the available pipe sizes. This design assumes SDR 26 to be conservative and avoid looping.

First, find the diameter based on the flow and velocity. A doubled flow is used because the two middle trunks must carry flow for two layers (**check this for correctness**)

.. math:: \frac{2Q_{Layer}}{V_{ManTrunkMaxPR}} = A_{TrunkCalc} = \frac{\pi*ID_{TrunkCalc}^2}{4}

Within the set of available inner diameters for SDR 26 pipes,  this :math:`D_{TrunkCalc}` value is rounded up to the nearest real size. This size is found in the specified pipe database, and kept as a ND. This functioanlly obtained ND value is compared to the maximum filter trunk ND (:math:`ND_{TrunkMax}`). The lesser of the two values is chosen. The lesser value is chosen because selecting the maximum pressure recovery in a previous step can result in a filter flow rate slightly larger than the maximum for the max trunk diameter. The max trunk diameter is still used in this case, though it just barely violates the pressure recovery constraint

That process is repeated to find the size of the backwash trunk, the only difference is the flow rate and velocity used are those for the backwash trunk.

.. math:: \frac{Q_{Fi}}{V_{BwManTrunkMaxPR}} = A_{BwTrunkCalc} = \frac{\pi*ID_{BwTrunkCalc}^2}{4}

Finding the pipe sizes lets the pressure recovery be determiend for the trunk in forward filtration:

.. math:: PR = \frac{V^2}{2g} \longrightarrow \frac{\frac{2Q_{Layer}}{\pi*D_{Trunk}^2}}{2g} = PR_{ForwardTrunk}


and in backwash:

.. math:: \frac{\frac{2Q_{Fi}}{\pi*D_{TrunkBw}^2}}{2g} = PR_{BwTrunk}

These values allow the necessary height of sand in each layer to be determined, as in the following section.

.. _heading_sand_layer_from_trunk_diam:

Sand Layer Thickness as Function of trunk diameters
====================================================


To make construction easier, all sand depths get rounded up to the nearest centimeter.

The following are the functions which determine the heights of the all the sand layers.

.. math:: H_{layer} = f(ND_{trunk}) =

This relates to the distance between the manifold branches and how the water will distribute amoung the layers.

<Insert picture of side view of filter>


Clean bed head loss
====================

The headloss through a bed of sand is determined with the Kozeny Equation (**ref for this eventually**)

The head loss between the lowest layer is different than the other five layers because, it is slightly thicker as calculated just above.

Auxilliary box widths and plumbing
===================================

not today

Number of manifold branches
==============================

Constraints for number of manifold branches:
1. Even number, because branches on both sides of the trunks
2. max allowable flow through backwash branches
3. allowable **average** flow for pressure recovery term

First, the maximum pressure recovery in backwash branch:

.. math:: PR_{BwManBranchMax} = HL_{BWSlotsEst}*\Pi_{ManifoldHeadLoss} - PR_{BwTrunk}

the resulting velocity from this pressure recovery:

.. math:: V_{BwManBranchMax} = \sqrt{2g*PR_{BwManBranchMax}}

The maximum allowable flow through this branch is then:

.. math:: Q_{BwBranchMaxPR} = V_{BwManBranchMax}*\pi*IR_{BranchManifold}^2

The allowable average flow is also necessary, which is derived thusly:

.. math:: \Pi_{Q} = \frac{Q_{min}}{Q_{max}}

Assume linear flow distrubution between branches:

.. math::

  Q_{ave} = \frac{Q_{max} + Q_{min}}{2}

  Q_{ave} = \frac{Q_{max} + \Pi_{Q}Q_{max}}{2}

  Q_{ave} = Q_{max}(\frac{1 + \Pi_{Q}} {2} )

  \Pi_{Q} = \sqrt{1 - \Pi_{HL}}

  Q_{ave} = Q_{max}(\frac{1 + \sqrt{1 - \Pi_{HL}}} {2} )

Thus, the average allowable flow:

.. math:: Q_{BwBranchAveMaxPR} = Q_{BwBranchMaxPR}(\frac{1 + \sqrt{1-\frac{PR_{BwTrunk}}{HL_{BWSlotsEst}}}} {2} )

Then the number of manifold branches (rounded up to he nearest even number) because of backwash flow distribution:

.. math:: N_{BwManBranchMin} =  \frac{Q_{Fi}}{Q_{BwBranchAveMaxPR}}

.. _heading_n_manifold_for_filt:

To determine the minimum for the forward filtration flow distribution is a similar process with flows and PR adjusted for forward flow.

.. math:: PR_{ManBranchMax} = HL_{CleanLayerMin}*\Pi_{ManifoldHeadLoss} - PR_{ForwardTrunk}

The resulting velocity from this pressure recovery:

.. math:: V_{ManBranchMax} = \sqrt{2g*PR_{ManBranchMax}}

The maximum allowable flow through this branch is then:

.. math:: Q_{ForwardBranchMaxPR} = V_{ManBranchMax}*\pi*IR_{BranchManifold}^2

The average allowable flow:

.. math:: Q_{ForwardBranchAveMaxPR} = Q_{ForwardBranchMaxPR}(\frac{1 + \sqrt{1 - \frac{PR_{ForwardTrunk}}{HL_{CleanLayer}}}} {2} )

Then the number of manifold branches (rounded up to he nearest even number) because of backwash flow distribution:

.. math:: N_{ManBranchMin} =  \frac{2Q_{Layer}}{Q_{ForwardBranchAveMaxPR}}

Then the design minimum number of branches is the maximum of the two minimums:

.. math:: N_{ManBranchMin} \ and \ N_{BwManBranchMin}:

In addition to the minimums based on the flow constraints, a maximum number of branches exists for geometry reasons, so that the filter box width matches the auxiliary box width (when there is more than one filter)

This maximum is determined by the following rounded down to a whole number:

.. math::

  N_{ManSideBranchMaxMult} = \frac{\frac{A_{Active}}{W_{ActiveMin}} - OD_{BwManBranch} + L_{ManFerncoCoupling} + S_{BranchToWall}}{B_{ManifoldBranch}}

| Such that:
| :math:`N_{ManSideBranchMaxMult} =` the maximum number of branches per side
| :math:`A_{Active} =` the active area of the filter (perpendicular ot flow direction)
| :math:`W_{ActiveMin} =` the width of the filter area (**length of trunk?**)
| :math:`OD_{BwManBranch} =` the outer diameter of the branch piping
| :math:`L_{ManFerncoCoupling} =` the length of the fernco coupling (**in legnth dir of branches?**)
| :math:`S_{BranchToWall} =` the spacing from the end of the branch to the inner edge of the filter
| :math:`B_{ManifoldBranch} =` the **length?** of the branches

(should have a sketch for dimensions!)

As there are branches on both sides of the trunk, this number id multiplied by 2 to get the total maximum number of branches.

.. math::

  N_{ManBranchMaxMult} = 2*N_{ManSideBranchMaxMult}

**Include only one filter????????? that design is in here?????
the red text is here with a not from skyler or the error if the geo branches doesn't meet flow distribtuion constraint????**










Filter box dimensions and manifold pipe lengths
================================================

.. note::
  In this section and beyond, B is used to describe the center-to-center distance between features (such as slots or orifices) and W is the width of a feature (such as the width of a slot)

From the number of manifold branches the lengths of the manifold pipes as well as the various filter box dimensions can be determined.

The total length of the filter (which is in the direction of the trunk) is determined by adding the spaces the branches take up.

In this section several "expert inputs" become relevant. Expert input are parameters that are the same across all plants due to constraints during construction or set sizes of equipment. The other use of expert inputs if for values determined to be functional, but without the same research pressure to make them perfectly correct. An example of this is the spacing between manifold branches.

The total length of the filter is the sum of several things:

.. math::

  L_{Fi} = (\frac{N_{ManBranch}}{2} -1 )B_{ManifoldBranch} + OD_{BwManBranch} + L_{ManFerncoCoupling} + S_{BranchToWall}

The active width of the filter is the active area divided by the length:

.. math::

  W_{Active} = \frac{A_{Active}}{L_Fi}

This width is the active filter width, which does not include the projected area of the trunk lines, though it is assumed that the space betweent the branch holders contributes to the active area.

The the total width is:

.. math::

  W_{Fi} = W_{Active} + OD_{BWTrunk}

The width of the filter entrance is the sum of half the width of the filter, the outer radius of the cap of the backwash trunk, the minimum space between fittings in a tank or fittings and the wall of the tank, the thickness of the filter walls, and the thickness of the filter box walls. That is:

.. math:: W_{entrance} = \frac{W_{Fi}}{2} + OR_{Fitting} + S_{Fitting} + T_{FiWall} + T_{FiBoxWall}

The width of the filter overflow depends in the number of filters. If there is one filter, then :math:`W_{FiOverflow} = W_{FiOverflowMin}`. In most cases when there are 2 or more filters, the width of the overflow box is:

.. math:: W_{FiOverflow} = W_{Fi} + T_{FiWall} - W_{FiEntrance} - 2T_{FiBoxWall}

The length of the filter with regards to the manifold braches is the next calculable attribute:

.. math:: L_{ManBranch} = \frac{W_{Fi}}{2} - OR_{Fitting} - OR_{BranchHolder} + 2L_{ManBranchExt} - S_{ManAssembly}


This length is the length of the filter per manifold branch.  Thus the total length of the filter where the manifold branches are is this lengths multiplied by the number of branches:

.. math::

  L_{ManBranchTot} = L_{ManBranch}N_{ManBranch}

The length of the backwash manifold is calculated similarly.

.. math::

  L_{BwManBranch} = \frac{W_{Fi}}{2} - OR_{BwTrunk} - OR_{FittingBWBranchHolder} - OR_{BWBranchHolder} + 2L_{ManBranchExt} - S_{ManAssembly}

  L_{BwManBranchTot} = L_{BwManBranch}N_{ManBranch}

Next, the length of the trunks:

.. math::

  L_{Trunk} = L_{Fi} - \frac{L_{ManFerncoCoupling}}{2} - T_{TrunkCap} - S_{ManAssembly}

  L_{BWTrunk} = L_{Fi} - \frac{L_{ManFerncoCoupling}}{2} - T_{BwTrunkCap} - S_{ManAssembly}

And the lengths of the branch holders:

.. math::

  L_{BranchHolder} = L_{Fi} - 2T_{BranchHolder} - 2S_{ManAssembly}

  L_{BwBranchHolder} = L_{Fi} - 2T_{BwBranchHolder} - 2S_{ManAssembly}





Manifold slot/orifice design
===============================

**Note** Previously all manifold branches were slotted, and the middle two inlets and hte three outlets had identical slotted pipes. The top and bottom inlets  were different becausethey only received half the flow but we wanted the same slot head loss through all manifolds.

Now the design has changed to having inlet branches with orifices instead of slots to avoid clogging. Sand is kept out with downward-facing U-channels around the pipes that create gravity exclusion zones. The outlet manifdol are stll slotted because we don't yet have a design that would keep sand out of the orifices during normal filtration.

The basis of the design of the orifices is the head loss through the bottom manifold orifices during backwash in order to get good flow distribution along the manifold.

.. math::

  HL_{BwOrificeEst} = \frac{PR_{BwManTotal}}{\Pi_{ManifoldHeadLoss}}

  A_BwManOrificeEst = \frac{Q_{Fi}}{\Pi_{VC}\sqrt{2g(HL_{BwOrificeEst})}}

  A_{BwManOrificeEst} = 2A_{BwManOrificeEst}

  A_{TopManOrificeEst} = A_{BwManOrificeEst}

  A_{OutletManSlots} = A_{InletManOrificesEst}


Outlet Design:

Parameters:

.. math::

  B_{ManSlot} = \frac{1}{8}in = 3.175mm

  N_{SlotRows} = 2

Lengths:

.. math::

  L_{OutletManSlotBranchTotal} = \frac{A_{OutletManSlots}}{W_{ManSlots}N_{ManBranch}}

  L_{OutletBranchSlotted} = L_{ManBranch} - 2L_{ManBranchExt} - B_{ManSlot}

Number of outlet slots per branch, then rounded down to the nearest integer:

.. math:: N_{OutletManSlotsPerRow} =  \frac{L_{OutletBranchSlotted}}{B_{ManSlot}}

Then the number of the slots per branch:

.. math:: N_{OutletManSlotsPerBranch} = N_{OutletManSlotsPerRow}N_{SlotRows}

Thus the length of the slot is:

.. math:: L_{OutletManSlotCurvedInner} = \frac{ L_{OutletManSlotBranchTotal}}{N_{OutletManSlotsPerBranch}}

This amount should be checked to ensure that it does not exceed what is possible given the 1/2 unner circumference of the branch.

Inlet Design:


Parameter:
:math:`B_{ManOrificeEst} = 1cm`
.. is this a diameter of the orifice?

For the backwash branches the maximum number of orifices is (rounded down an integer):

.. math:: N_{BwManBranchOrificeMax} = \frac{L_{BwManBranch} - 2L_{ManBranchExt} - B_{ManOrificeEst}}{B_{ManOrificeEst}}

The maximum number of orifices on the backwas manifold is:

.. math:: N_{BwManOrificeMax} = N_{ManBranch} N_{BwManBranchOrificeMax}

On the other inlets an identical calculation is done :

.. math::

  N_{ManBranchOrificeMax} = \frac{L_{ManBranch} - 2L_{ManBranchExt} - B_{ManOrificeEst}}{B_{ManOrificeEst}}

  N_{ManOrificeMax} = N_{ManBranch} N_{ManBranchOrificesMax}

  -----

Determining the diameter of the orifices is next.
In this design only drill bit sizes of 1/4" and 1/8" are considered. The total area of the orifices is divided by the maximum number of orifices. From this a radius is calculated and double to get a diameter. This diameter is compared to the available  drill bit options and rounded up to the closest size. This is done for the backwash manifold, inner inlet manifolds, and the top inlet manifold as shown below:
.. why are these the only two drill bit sizes considered?

.. math::

  D_{BwManOrifice} = 2\sqrt{\frac{A_{BwManOrificeEst}}{\pi* N_{BwManBranchOrificesMax}}}

  D_{InletManOrifice} = 2\sqrt{\frac{A_{InletManOrificeEst}}{\pi* N_{ManOrificesMax}}}

  D_{TopManOrifice} = 2\sqrt{\frac{A_{TopManOrificeEst}}{\pi* N_{ManOrificesMax}}}

Thus the hole size is determined!

The actual number of inlet orifices can then be calculated. A calculation is done for each "type" of inlet, if that number is larger than the maximum allowed number of orifices then the maximum is used. Otherwise the calculated number is used.

The calculations for number of orifices based on orifice size is:

.. math::

  N_{BwManOrificesCalc} = \frac{A_{InletManOrificesEst}}{\frac{\pi}{4}*D_{BwManOrifice}^2}

  N_{InletManOrificesCalc} = \frac{A_{InletManOrificesEst}}{\frac{\pi}{4}*D_{InletManOrifice}^2}

  N_{TopManOrificesCalc} = \frac{A_{FiTopManOrificesEst}}{\frac{\pi}{4}*D_{TopManOrifice}^2}

Comparing these calculations to the output provides values for :math:`N_{BwManOrifices}`, :math:`N_{InletManOrifices}`, and :math:`N_{TopManOrifices}` which are then used to find the actual areas of the inlet orifices

.. math::

  A_{BwManOrifices} = \frac{\pi}{4}D_{BwManOrifice}^2 * N_{BwManOrifices}

  A_{InletManOrifices} =  \frac{\pi}{4}D_{InletManOrifice}^2 * N_{InletManOrifices}

  A_{TopManOrifices} =  \frac{\pi}{4}D_{TopManOrifice}^2 * N_{TopManOrifices}

------

Recalling the outlet area, a conservative headloss calculation can be made accounting for sand blockage. Currently, this is not included inteh total path headloss; it is unclear if it applies.

.. math::

  HL_{OutletSlotForward} = \frac{(\frac{2Q_{FiLayer}}{A_{OutletManSlots}*\epsilon_{Sand}*\Pi_{VCOrifice}})^2}{2g}

Additionally the headloss from each of the inlets can be found.

.. math::

  HL_{BwManOrifice} = \frac{(\frac{Q_{Fi}}{A_{BwManOrifices}*\epsilon_{Sand}*\Pi_{VCOrifice}})^2}{2g}

  HL_{BwManOrificeForward} = \frac{(\frac{Q_{FiLayer}}{A_{BwManOrifices}*\epsilon_{Sand}*\Pi_{VCOrifice}})^2}{2g}

  HL_{InletManOrificeForward} = \frac{(\frac{2Q_{FiLayer}}{A_{InletManOrifices}*\epsilon_{Sand}*\Pi_{VCOrifice}})^2}{2g}

  HL_{TopManOrificeForward} = \frac{(\frac{Q_{FiLayer}}{A_{TopManOrifices}*\epsilon_{Sand}*\Pi_{VCOrifice}})^2}{2g}


Plumbing head losses
======================

Total Sand depth and backwash head loss
========================================

Here, :math:`H` is used as height of sand, though as the filter extends downward it may be more intuitive to think of this as a depth of sand.

The overall depth of sand is:

.. math:: H_{Sand} = (N_{Layer} - 1)H_{Layer} + H_{BottomLayer} + OR_{BwManBranchFitting} + OR_{ManBranch}

During filtration not all of the sand is activiely involved in the process, the amount of sand that is active is all the sand contained in the sand layers.

.. math:: H_{SandActive} = H_{Sand} - OR_{BwManBranch} - OR_{ManBranch}

The height of the fluidized sand bed is the height of the settled sand bed times the expansion ratio:

.. math:: H_{FluidizedBed} = \Pi_{Fluidized} H_{Sand}

Knowing the depth of the fluidized bed allows the steady state headloss to be calculated for backwash.

.. math::

  HL_{BwSandSS} = \frac{H_{Sand}(\rho_{Sand} - \rho_{H2O})(1 - \epsilon_{Sand})}  {\rho_{H20}}

The value of this HL is very close to the total depth of sand in the filter, though it should be noted that this value does neglect losses in the plumbing.

.. math:: HL_{Terminal} = HL_{CleanLayer} + HL_{Dirty}

.. math:: HL_{BwInitiation} = HL_{BwSF} + HL_{BwSandSS}

.. note:: What are these terms? have them explained! also explain how the terms below are gotten

How much does the filter bed over-fluidize when the entrance box level lowers after backwash initiation!

.. math::

  H_{FluidizedBedVariation} = \frac{(HL_{BwInitiation}-HL_{BwSandSS})(W_{FiEntrance}L_{FiEntranceEst} - 3 \pi OR_{Trunk}^2 - \pi OR_{BwTrunk}^2)}{A_{FiActive}}




Path head loss calculations and flow distribution between layers
=================================================================

Now that the sand layer depth is set the Kozeny Head Loss can be determined for the clean bed and the headloss through various flow paths can be determined.

First use the Kozeny Equation (**ref kozeny** )to find the HL in the central layers and also the bottom layer with :math:`H_{Layer}` and :math:`H_{BottomLayer}`



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
