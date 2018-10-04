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

However,the actual maximum of flow that the filter would see is actually the larger flow between that value and the :math:`Q_{Fi}` the flow through the filter.

**This makes less sense now that I'm writing it in, why would this be greater than backwash flow?**

Depending on the total flow of the EStaRS and the size of the modules, varying numbers of filters will need to be used.

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

Because the 2 inner inlets (the ones that aren't the backwash trunk or the uppermost trunk) distribute flow to two layers the flow between them is equal to :math:`2Q_{FiLayer}` which is shown in the schematic. In a later section, we will show that the flow within each layer is not exactly even because of the headloss through various paths, but for the calculation of maximum flow, even flow is an appropriate guess (**do we know know this**)

From the schematic we can also see that the maximum flow experienced by any trunk is :math:`2Q_{FiLayer}`, using this value it is possible to calculate the maximum branch through a branch.

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


Pressure Recovery in Trunks during forwasrd filtration
---------------------------------------------------------

The total allowable pressure recovery of the filter manifold is controlled by the headloss in each sand layer and the headloss ratio, :math:`\Pi_{ManifoldHeadLoss}`, as defined above in "Flow Distrbution Constraints".

The head loss through the sand layer, :math:`HL_{FiCleanLayerMin}` is a fuction of layer depth, :math:`H_{FiLayer}` and overall velocity of the filter , :math:`\frac{Q_{FiLayer}}{A_{Fi}}`, using the Kozeny Equation (**link Kozeny**).

Using the definition of the pressure recovery ratio, the maximum allowable pressure recovery in the filter manifold can be calculated:

.. math::

  PR_{FiMax} = HL_{FiCleanLayerMin}*\Pi_{ManifoldHeadLoss}


Subtracting the previously calculated branch PR from this maximum determine how much PR 'is left' for the trunks. The maximum trunk PR can then be calculated back to a velocity.

.. math::

  PR_{TrunkEst} = PR_{FiMax} - PR_{FiBwManBranchEst}

  V_{FiTrunkMaxPR} = \sqrt{2g*PR_{TrunkEst}}


The velocity is important because it, along with the known flow rate throug the trunk are used to find a theoretical area for the flow. This area sets and ideal ID for a trunk pipe. Using the pipe database allows a search for the closest match.

.. math::

  ID_{TrunkIdeal} = \sqrt{\frac{4*\frac{2*Q_{FiLayer}}{{V_{FiTrunkMaxPR}}}}   {\pi}}

In the pipe database the nearest, larger, pipe size is chosen for SDR 26. The associated ND is compared with :math:`ND_{FiTrunkMinLow}, whichever is larger is chosen as :math:`ND_{FiTrunk}`

Pressure Recovery in lowest trunk during backwash
----------------------------------------------------------------



Manifold Pipe Lengths
======================

Inlet Orifice and Outlet Slot Design
========================================

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
