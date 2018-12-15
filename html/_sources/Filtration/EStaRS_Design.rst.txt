.. _title_estars:

*******************
EStaRS Design
*******************


Some parts of the design are the same!


Dimensions and Pipe Size
=========================
.. two filters are assumed

The filter flow and backwash velocity are used to find an area, this area is used to find the Nominal Diameter of the pipe to be used for the filter. If the value is not one of the options, the next largest pipe size is selected.

The height of the filter layer is taken as 0.2 meters.
Some other variables defined here:

These are all minimums!

.. math::

  ND_{FiTrunkMinLow} = 1.5in
  ND_{FiBranchMinLow} = 1in
  ND_{BallValve} = 3in
  ND_{BedTester} = 0.5in
  ND_{BedTesterOuter} = 1in
  ND_{FiAirRelValve} = 0.5in
  ND_{FiBwTrunkMinLow} = 2in
  ND_{FiBwBranchkMinLow} = 1in



The branch spacing is a function of the size of the EStaRS. The "maximum" spacing is somewhat arbitrarily set 10cm. This value is meant to balance even flow distribution across each layer with ease of fabrication and material use. As a result the expression for number of branches is the following:
  :math:`B_{FiBranchMax} = 10cm`

.. math::

    N_{FiBranchMin} = round(\frac{ID_{FiPipe}}{B_{FiBranchMax}})

the ID function also takes the SDR for the pipe (26), but in the equation above was left out so the overall mechanism of the calculation is clearer. The value is rounded because an integer number of branches is needed.

The number of inlet and outlet pipes are fixed by the way the filter works and are shown below:

.. math::


    N_{FiInletPipesLow} = 4

    N_{FiOutletPipesLow} = 3


The area of the filer is defined as: :math:`ID_{pipe}^2 / 4`

Sand Layer Thickness as a Function of Diameter
===============================================

Two heights are defined here. Both are defined as functions:

:math:`H_{FiLayerF}` the height of a standard filter layer. It is defined as the maximum value between the defined layer height, the outer radius (OR) of the trunk  (as a fucntion of nominal diameter) plus the minimum filter trunk spacing  , the outer diameter of the iftting of the trunk (also as function of ND), and the fernco outer diameter (again a fucntion of ND). Each of these is rounded to the nearest 1cm.

and

:math:`H_{FiBottomLayerF}` the height of The bottom filter layer. This is defined as the maxiumum value between 1. The defined layer height, the OR of the trunk + OR of the backwash trunk  (as functions of ND's of the trunk and BW trunk) + minimum filter trunk spacing, the sum of fitting OR's for the trunk and BW trunk (function of ND's), and the average of the ferco OD's as a function of NDs. Each rounded to the nearest 1cm.


Flow Distribution Constraints: ratio of pressure recovery to clean bed head loss
===================================================================================

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
| :math:`Q_{Long} =` the flow through the shortest filter path (top layer, closest slot on the first branch)
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

Though the piezometric head profiles for the inlet and outlet manifolds for the middle layers may be parallel, meaning the pressure recovery is less constrained for a good flow distribution, we still need a tight constraint for the outer manifolds where the velocity is 1/2 and the PR is 1/4 that of the inner layer, while smaller still in the bottom-most manifold where the velocity head is tiny as the diameter is larger.




Filter Flow Rates and Layer Height
===================================

As the maximum flow of the filter is constrained by the available sizes of the pipe for the filter, the maximum flow of the filter is characterized by: :math:`Q_{Bw} = V_{Bw}A_{Fi}`

However,the actual maximum of flow that the filter would see is actually the larger flow between that value and the :math:`Q_{Fi}` the flow through the filter. For example, if two EStaRS designed for 3.08 L/s each are used for a plant flow of 7 L/s, each filter will actually see 3.5 L/s of flow. This is greater than what the filter was designed for, and this larger flow must be accounted for.

.. note::
  Knowing which flow is being used to calculate the size of certain components is **extremely** important. For calculations involving the pipe manifold the maximum flow that could be seen by the filter should be used (:math:`Q_{FiMax}`). This is because the pressure recovery term is the limiting characteristic, and so a greater flow corresponds to a greater velocity which increases PR, which is unideal. For calculations concerning the system of weirs required for backwash, which are calculated in "Backwash Control Volume",the backwash flow :math:`Q_{FiBw}` is required because backwash cannot be performed effectively with less flow that the backwash flow. While it is *possible*  that backwash could be necessary in extremely low flow conditions, it has never been an issue in any plant, so this is not accounted for. Additionally, it is possible that these two values are the same, in which case the distinction is not necessary.

Depending on the total flow of the EStaRS and the size of the modules, varying numbers of filters will need to be used, though minimum should always be 2.

This design will focus on flow through one filter, as having several filters in parallel wouldn't alter the flow within one, thought flow will be split between the filters.

The entire area of the filter is assumed to be active and is denoted as :math:`A_{Fi}`.

Within each filter the flow is diverted across six layers. (:math:`N_{FiLayer} = 6`)

Thus the flow through each layer is: :math:`Q_{FiLayer} = \frac{Q_{Fi}}{N_{FiLayer}}`

From the area of the filter and the velocity required for backwash, the backwash flow can be determined: :math:`Q_{FiBw} = V_{FiBw}A_{Fi}`

.. this value is the same as the max filte flow, is it useful to have these values specified multiple times??

In this section is also where the filter layer height is actually calculated using the function from the "Sand Layer Thickness As a Function of Diameter" Section: :math:`H_{FiLayer}`


Filter Trunk and Branch Diameters
==================================

In determining the size of the trunk and branches of the EStaRS the pressure recovery constraints are the most important design considerations. Having a pressure recovery term that is too high will lead to and uneven flow distribution. The two pressure recovery terms that are of particular concern are those in the trunks and branches during forward filtration, and the pressure recovery in the lowest branch during backwash. To calculate the estimated pressure recovery term the first thing to find is the velocity in the branches during forward filtration and during backwash.

Determining Forward Filtration and Backwash Velocities
--------------------------------------------------------

See Figure XXXX for a schematic of the filter layers.

.. image:: Images/figure_flow_distribution_estars.PNG

From the section above it is apparent that the total flow through the filter is the flow through each layer times the number of layers or :math:`Q_{Fi} = N_{Layers}*{Q_{FiLayers}`

In the case of 6 filter layers, this is :math:`6Q_{FiLayer}`

Because the 2 inner inlets (the ones that aren't the backwash trunk or the uppermost trunk) distribute flow to two layers the flow between them is equal to :math:`2Q_{FiLayer}` which is shown in the schematic. In a later section, we will show that the flow within each layer is not exactly even because of the headloss through various paths, but for the calculation of maximum flow, even flow is an appropriate guess. (**do we know know this**)

From the schematic we can also see that the maximum flow experienced by any trunk is :math:`2Q_{FiLayer}`, using this value it is possible to calculate the maximum branch through a branch. Using :math:`2Q_{FiLayer}` is a conservative estimate, most branches will not see this flow, however because the pressure recovery is the main constraint in the filter pipe manifold, it is best to use the maximum possible flow to determine allowable PR.

On each layer trunk, there are :math:`N_{FiBranch}` branches on **each side** of the trunk. That means the total number of branches on each trunk is :math:`2N_{FiBranch}`

Using the maximum flow in a trunk and the number of branches on a trunk the maximum flow in a branch becomes:

.. math::

    Q_{FiBranchMax} = \frac{2Q_{FiLayer}}{2N_{FiBranch}}

Using the ND of the Filter Manifold Branches, as defined above, the minimum flow area of a branch can be calculated:

.. math::

  A_{FiBranchMin} = \frac{ID_{FiBranch}^2 *\pi}{4}


Knowing the area allows the velocity within a branch to be found.

.. math::

  V_{FiBranchEst} = \frac{Q_{FiBranchMax}}{A_{FiBranchMin}}

From the velocity the pressure recovery term can be determined, this equation comes from the definition of pressure recovery:

.. math::

  PR_{FiManBranchEst} = \frac{V_{FiBranchEst}^2}{2g}

:note: Have i descirbed pressure recovert yet in this section! or does it need to be described here?

A similar series of calcualtions can be done for the backwash branches based on :math:`Q_{FiBw}`:

.. math::

  Q_{FiBwBranchMax} = \frac{Q_{FiBw}}{2N_{FiBranch}}

  A_{FiBwBranchMin} = \frac{ID_{FwBwBranch}^2 *\pi}{4}

  V_{FiBwBranchEst} = \frac{Q_{FiBwBranchMax}}{A_{FiBwBranchMin}}

  PR_{FiBwManBranchEst} = \frac{V_{FiBwBranchEst}^2}{2g}


The two pressure recovery terms calculated here are compared against the allowable PR terms.


First Constraint: Pressure Recovery in Trunks during forward filtration
---------------------------------------------------------

The total allowable pressure recovery of the filter manifold is controlled by the headloss in each sand layer and the headloss ratio, :math:`\Pi_{ManifoldHeadLoss}`, as defined above in "Flow Distrbution Constraints".

The head loss through the sand layer, :math:`HL_{FiCleanLayerMin}` is a fuction of layer depth, :math:`H_{FiLayer}` and overall velocity of the filter , :math:`\frac{Q_{FiLayer}}{A_{Fi}}`, using the Kozeny Equation (**link Kozeny**).

Using the definition of the pressure recovery ratio, the maximum allowable pressure recovery in the filter manifold can be calculated, this value is not necessarily the actual pressure recovery the system may see, just the allowable maximum:

.. math::

  PR_{FiMax} = HL_{FiCleanLayerMin}*\Pi_{ManifoldHeadLoss}


Subtracting the previously calculated branch PR from this maximum determine how much PR is theoretically left for the trunks. The maximum trunk PR can then be calculated back to a velocity.

.. math::

  PR_{TrunkEst} = PR_{FiMax} - PR_{FiBwManBranchEst}

  V_{FiTrunkMaxPR} = \sqrt{2g*PR_{TrunkEst}}


The velocity is important because it, along with the known flow rate throug the trunk are used to find a theoretical area for the flow. This area sets and ideal ID for a trunk pipe. Using the pipe database allows a search for the closest match.

.. math::

  ID_{TrunkIdeal} = \sqrt{\frac{4*\frac{2*Q_{FiLayer}}{{V_{FiTrunkMaxPR}}}}   {\pi}}

In the pipe database the nearest, larger, pipe size is chosen for SDR 26. The associated ND is compared with :math:`ND_{FiTrunkMinLow}`, whichever is larger is chosen as :math:`ND_{FiTrunk}`. From this ND the ID is found knowin the pipe is SDR 26.

Then the PR term can be found:

.. math::

  PR_{FiTrunk} = \frac{(\frac{2Q_{FiLayer}}{(\pi\frac{ID_{FiTrunk}^2}{4})})^2}{2g}

Knowing the actual (for this flow) PR term provides a better value for determining the allowable PR in the branches.

So now, the :math:`PR_{FiBranchMax}` is the different between the allowable PR and the PR calculated for the trunk:

.. math::

  PR_{FiBranchMax} = PR_{FiMax} - PR_{FiTrunk}

Then the maximum velocity in the branches can be found. Which, as above leads to the actual size of the branches.

.. math::

  V_{FiBranchMax} = \sqrt{2g*PR_{FiBranchMax}}

The ND is found by again comparing the :math:`ND_{FiBranchMin}` with the ND that emerges from taking the ID as calculated from the velocity and the flow:

.. math::

  ID_{FiBranchEst} = \sqrt { \frac{4}{\pi}(\frac{\frac{2Q_{FiLayer}}{2N_{FiBranch}}}{V_{FiBranchMax}})^2}

This ID is compared with available IDs of SDR26 and the nearest value that is above that ID is chosen to compare against :math:`ND_{FiBranchMin}` as defined in the beginning.

**if this can be streamlined in python it should be, because going from ID to ND to actual ND to ID is a pain**

For the chosen ND, the corresponding ID is used to determine the PR in the branches with SDR26.

.. math::

  PR_{FiBranch} = \frac{(\frac{\frac{2Q_{FiLayer}}{2N_{{FiBranch}}}}{(\pi\frac{ID_{FiBranch}^2}{4})})^2}{2g}


The sum of the PRs from the branches can then be compared to the maximum allowable PR term. If the design logic worked properly then :math:`(PR_{FiBranch} +  PR_{FiTrunk}) < PR_{FiMax}` with  :math:`PR_{FiBranch} +  PR_{FiTrunk} = PR_{FiMan}` indicating the pressure recovery in the Filter Manifold.

Second Constraint: Pressure Recovery in lowest trunk during backwash
----------------------------------------------------------------

The second pressure recovery constraint is in the backwash branch during backwash. During backwash the lowest trunk sees all the flow at a higher velocity than any branch does during forward filtration. Because the velocity is higher, the PR term will also be higher, so it must be constrainted to maintain even flow.

In backwash there is no headloss through the sand bed because the sand is fully fluidized. The startup time in which it takes to fluidize the bed is ignored in this design. Thus the only headloss occurs from the flow expansion as water exits the fiter manifold out of the exits holes.

The initial estimate of headloss through the holes is :math:`HL_{FiBwOrifices} = 10cm`.

Using the headloss ratio, :math:`\Pi_{ManifoldHeadLoss}` , the allowable PR canbe determined: :math:`PR_{FiBwManMax} = HL_{FiBwOrifices}*\Pi_{ManifoldHeadLoss}`

From above the PR estimate for the Backwash Branches exists.

This allows the maximum velocity in the BW Trunk to be found

.. math::

  V_{FiBwTrunkMaxPR} = \sqrt{2g *(PR_{FiBwMax}-PR_{FiBwBranchEst})}

From the velocity the ND of the backash trunk can be found based on the necessary inner diameter and pipe schedule as calculated using the flow area.

.. math::

  ID_{FiBranchEst} = \sqrt { \frac{4}{\pi}(\frac{Q_{FiBW}}{V_{FiBwTrunkMaxPR}})^2}

The corresponding ND (usign SDR 26) is compared against :math:`ND_{FiBwTrunkMin}`. The larger pipe is chosen for the design. The ID from the chosen pipe size is then used to find the actual backwash PR for the backwash trunk.

.. math::

  PR_{FiBwTrunk} = \frac{(\frac{Q_{FiBw}}{(\pi\frac{ID_{FiBwTrunk}^2}{4})})^2}{2g}


Then the actual allowable pressure recovery for the backwsh branches can be found.

  .. math::

    PR_{FiBwBranchMax} = PR_{FiBwMax} - PR_{FiBwTrunk}

Then the branch velocity can be found:

.. math::

  V_{FiBwBranchMax} = \sqrt{2g *(PR_{FiBwBranchMax})}

Then, as above this velocity is used to find the area of the backwash branch with:

.. math::

  A_{BwBranchEst}  = \frac{Q_{FiBw}}{2N_{FiBwBranch}}

If it seems like these processes are 1. similar and 2. circular in their logic, you are correct on both counts! The determination of PR for backwash and forward filtration follows the same steps, the only difference is with the flows and conditions required. It seems circular because the initial calculations are done on guesses, if these guesses weren't made solving for other quantities couldn't be done. The step where the trunk calculations are resolved for the branch conditions mainly acts to assess if the initial guesses were reasonable, and corrects the error in the guess, though of course the initial guess could've been correct! Running the final values back through the entire process should yield the same results meaning the iteration found a solution.

Manifold Pipe Lengths
======================

Come back to this a little bit...

Inlet Orifice and Outlet Slot Design
========================================

Knowing the PR in the BW manifold, the design head loss through the outlet orifices can be determined based on:

.. math::

  HL_{BwOrifices} = \frac{PR_{BwManTotal}}{\Pi_{ManifoldHeadLoss}}

With this head loss the necessary total area of the orifices for the backwash branch can be determined using the orifice equation **REF**, as :math:`HL_{BwOrifices}` , :math:`\Pi_{VCOrifice}`, and :math:`Q_{FiBw}` are known.

This area is doubled to find the area of the slots.

  .. math::

    A_{FiManSlots} = 2*A_{FiBwOrifices}

**why is this? I don't know!**

Also the area of the backwash orifices is equal to :math:`A_{FiTopManSlots}`, which is the area of the **this is the area of something thats for sure**

Outlet Design
---------------

Due to fabrication methods for the slotted pipes (manufacturing by machine), the slot width, :math:`B_{slot}` is always .008 inch. *The number of slot rows is also fixed at 2, because each branch has slots on the top and bottom because the outlet pipes are accepting flow from two layers of sand, one above and one below.*

From the cumulative area of slots and the width of the slots **where the hell does the width come from** The total length of slots can be determined. This length of slots is for one side of one branch *yes?*

As the branches are different lengths along one trunk, the number of slots is different per branch depending on the length. Dividing the Length of the



Inlet Design
--------------

Regarding the inlets, those for backwash are determined differently than the orifices on the rest of the inlet branches. This section traces the process for the backwash branches and then the rest of the manifold branches.

The spacing of orifices, :math:`B_{OrificeEst}` is estimated at 1cm.

The number of orifices per branch is the floor value of:

.. math::

  N_{BwBranchOrifices} = \frac{L_{FiBwBranchLow} - B_{OrificeEst} - 2*L_{FiBranchExt}}{B_{OrificeEst}}

  and

  N_{BranchOrifices} = \frac{L_{FiBranchLow} - B_{OrificeEst} - 2*L_{FiBranchExt}}{B_{OrificeEst}}

The only difference between the two is the length of the branches. Because the backwash trunk is slightly larger than the rest of the trunks, the branches must be slightly shorter so that the whole manifold fits in the filter body.

Then for each the total number of orifices necessary for a layer of the manifold can be found by summing the array of number of holes (:math:`N_{BranchOrifices}`) and multiplying by 2 to account for the trunks having branches on two sides.

Have the holes close together is important to maintaing an even flow distribution, which is why the holes spacing is determined before hole size (which is also constrained by available drill bit sizes)

The drill bit sizes considered are 1/8 inch and 1/4 inch.

The choice of drill bit size is then determined using the cumulative area of orifice needed for a branch.

Generally, the hole diameter is chosen from the closest (but larger) drill bit based on:

.. math::

  D_{guess} = 2*\sqrt{\frac{A_{OrificeTotal}}{\pi*N_{OrificePerBranch}}}

  Where:
  A_{OrificeTotal} = (A_{BwOrifices}, A_{FiManSlots}, A_{FiTopManSlots})

These 3 distinct diameters are compared to available drill bits, and actual diameters are chosen.

Because this diameter is likely larger than the calculated diameter, the number of holes must be recalculated for each. The new number of holes is the minimum between the new calculated number (rounded down to the nearest integer) and the original number of holes (which was defined as a maximum). The new calcualtion is done as follows:

.. math::

  N_{OificesEstNew} = \frac{A_{TotalNecessaryArea}}{\frac{\pi}{4}D_{Orifice}^2}

Again using the three areas, but now also with the new corresponding diameters.

This number of holes can be used to check that total area of holes is close to the total area necessary to provide the appropriate amount of headloss.

The head loss calculation can then be checked as well for all 5 branch systems involved: the backwash branches in forward, the backwash branches in backwash, the top inlet pipe during filtration, the other inlet pipes during filtration, and the outlet pipes during filtration.

The head loss for each branch type is:

.. math::

    HL = \frac{\frac{Q}{\Pi*A*\epsilon}^2}{2g}

With the relevant parameters for each type of manifold branch shown below in **this figure**


**Make the table not here because formatting yo**




Entrance and Exit Pipe Dimensions
==================================

Total Sand Depth, Filter Pipe Length, Head Loss
=================================================

Plumbing Head Loss
=====================



Path head loss calculations and flow distribution between layers
=================================================================

Now that the sand layer depth is set the Kozeny Head Loss can be determined for the clean bed and the headloss through various flow paths can be determined.

First use the Kozeny Equation (**ref kozeny** )to find the HL in the central layers and also the bottom layer with :math:`H_{Layer}` and :math:`H_{BottomLayer}`

As the filter has 6 layers there are six possible paths for the water to take.

Overview of the algorithm of this section:

In each path the path headloss is the sum of : inlet plumbing, sand layer, and outlet plumbing (for the relevant flow)

Find the max headloss through the respective paths (Q1 - Q6)
Find the min headloss through the respective paths (Q1 - Q6)
Find the average headloss of the paths (sum(HL)/6)
^^a theoretical term because the flow distrubution will sort itself out because that's how headloss works
Find Pi_layer. The ratio of  the flow distribution. Goal is close to 1.

Because the flow distribution will change to make the headlosses even, it can be taken as true that :math:`HL_{Path1} = HL_{Path2}` and so on for each path. This assumes the clean bed headlosses and also accounts for the varying flows in each path.


It is also known that the flow must add up to the flow in the filter. Knowing that a system of equations can be set up to use the healoss and total flow requirement to solve for the flow in each layer. Those flows are then taken as the flow through each layer.

Siphon Design
==================

Elevations and Filter Sizing
=============================

Backwash Flow Control
===========================

Sand Volume
==============

Filter Stability
==================

Materials
=============
