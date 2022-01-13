.. _title_estars:

*****************************************
Enclosed Stacked Rapid Sand Filter Design
*****************************************



The Enclosed Stacked Rapid Sand filter, EStaRS, is a compact filter built inside a pipe. Open Stacked Rapid Sand, OStaRS, construction methods require that a person be able to work inside the filter to finish the waterproofing of the concrete walls and to install the pipe modules for the inlets and outlets. The minimum filter area for OStaRS is approximately 1 square meter. Given a backwash velocity of 11 mm/s that corresponds to a minimum flow of about 11 L/s. It is always best to have at least 2 filters operating in parallel so that the filters can be backwashed when the plant is operating at less than 50% of the design flow rate. Thus EStaRS filters will be used for plants with flows less than about 20 L/s.

* Use standard caps on the top and bottom of the filter body.
* Use clamp on fittings to split the filter body at two places between layers.
* Use clamp on fittings on trunks to enable removal.
* Use trunks that are 2" ND so that the molded ends of the branches have something to prevent them from rotating.
* Join branches across trunk with an upper and lower strap that is clamped in place with hose clamps.
* use band clamps on inside of filter to connect trunks
* weld a pipe stub to pass through the filter body for the trunks

The EStaRS filters should be modular with one pipe connection to attach to the settled water source and another pipe connection to attach to the finished water. The flow division between filters could be an LFOM for each filter in the inlet tank. To make a filter modular the inlet and outlet tanks need to be integrated into the filter module.

The inlet and outlet tanks could be separate or connected and they could be rectangular PVC tanks or PVC pipes.

Previous problems with EStaRS filters included air entrainment and fabrication problems with the filter internal piping. Corrugated pipes that are available for filter body diameters greater than 60 centimeters that are available in Honduras have very thin inner walls that are not thick enough for strong welds. This requires use of a gasket seal for passing the trunk lines through the filter body. The corrugated pipes are also more difficult to attach the required end caps on the filter body. For these reasons we do not recommend using corrugated pipes for the filter body. Smooth walled PVC pipe is available in sizes up to 60 cm in diameter (ND = 24") and is the material of choice for the filter body.

Air entrainment may be a problem in the inlet pipes. If air is carried into the filter the head loss through the filter will increase rapidly. Byron Zuniga reports that he was unable to get an effective backwash at the San Juan Guarita plant based on the observation that the head loss increased rapidly after backwash even though there was no evidence of turbidity release during backwash. This observation is consistent with air being entrained in the inlet pipes and carried into the filter where it rapidly fills the pores of the sand and thus prevents water from flowing through those pores.

The solution to air entrainment is to design the inlet pipes to act like tube settlers so that the air can return to the inlet tank.

We need a method to measure the flow rate entering the filters. The slot weir in the OStaRS filter could be used to measure the flow and would have a nonlinear scale. An alternative that the operators would readily understand would be to replace the slot weir with an LFOM.

The 4 EStaRS that are in operation in Central America as of 2021 have winged pipes with orifices for the inlets. There are no reports of problems with sand entering the inlet pipes and thus that appears to be a success. This does require the use of a gate valve for the backwash pipe to ensure that the transition from backwash to filtration mode doesn't happen too quickly. During this transition there is reverse flow from the filter into the inlet pipes and if that flow rate is too high it could carry sand into the inlet branches.

Air venting from trunks
***********************
The trunks are initially filled with air.
The trunks must have a water seal that is as low as the siphon water seal (is this the constraint?) to ensure that air is never sucked into the filter during backwash.
The trunk entry into the filter body is thus at a local high point and air that accumulates in the top of the trunk and the top of the branches has no way to get out.
There must be a vent on the top of the trunks where they enter the filter body.

Vent options
============

1) tube straight up to top of inlet tank (will suck air during backwash)
1) tube that connects into the top of the filter body (during filtration air will travel up the tubes and vent into the top of the filter body. During backwash water will take this shortcut to bypass the sand. It could work if the tubes are small enough that the bypass during backwash is small)
1) Use sloped section of trunk line to act as tube settler to remove bubbles that are entrained in the inlet. This doesn't solve the problem of air that is in the local high spot of trunks.

It seems that the only option is to connect the air release tubes to the top of the filter.

Elevation considerations
========================

The head loss through the sand during backwash is equal to the settled depth of sand. This means that the water level in the top inlet pipe will drop by an amount equal to the depth of the sand. That means that the bottom of the inlet tank must be ABOVE the top of the sand + the OD of the trunk + head loss in the backwash trunk inlet.


********
Old info
********

used for low flow plants because they are less resource intensive to construct than a small version of the full-size concrete filter, additionally the OStaRS become infeasible in term of maintenance at very low flows because it would very narrow and very deep. This difficulty is noted in OStaRS filters handling less than 8 L/s corresponding to plant flows less than 16 L/s. This challenge invites the EStaRS as an alternative.

Because the EStaRS filter is constructed using only pipes and couplings, the possible EStaRS sizes are discretized as pipes are not available in every conceivable size. This constraint means that there are only three available sizes of EStaRS: 1 ft, 2 ft, and 3 ft diameter, which treat 0.764 L/s, 3.07 L/s, and 7.024 L/s, respectively.

As with the OStaRS, each plant should have at least 2 filters so that one can still be in use even when the other is in backwash. If the plant flow is more than corresponds with 2 filters, additional filters can and should be added in parallel to accommodate additional flow. In additional to requiring multiple filters there are other parts of the design that are the same for both types of filters! The stacked trunk and branch system is the most notable of these similarities, with key differences being in how the inlet and outlet system can be designed. Both the "traditional" concrete entrance/exit channel and boxes can be used, but a more compact design features entrance and exit tanks made from large diameter pipes making them modular. Most of this design file considers the shared characteristics of the concrete and pipe hydraulic controls.


.. attention::

  In this file, many values are functions of pipe nominal diameter and SDR. For the simplicity of reading, those values are written with just the geometric value used. For example, if an outer diameter (OD) is needed, it is written as :math:`OD_{ExamplePipe}` rather than :math:`OD(ND_{ExamplePipe}, SDR26)` which is more similar to how it would be found explicitly. Some other features that follow this convention are Inner Diameters and Radii, Outer Radii, and wall thicknesses.


:numref:`table_comparsion_filters` shows some of the design differences between the different filter types. The parameters included in the table will be described throughout this design.

.. _table_comparison_filters:

+--------------------------+------------------+-----------------+----------------------+--------------------------------------+
| Feature                  | EStaRS for PF300 |EStaRS concrete   | EStaRS "Micky Mouse" | OStaRS                              |
+==========================+==================+==================+======================+=====================================+
| Signal for BW            | 60cm head loss   | 75cm head loss   | 75cm head loss       | Min 20cm, function of trunk diameter|
+--------------------------+------------------+------------------+----------------------+-------------------------------------+
| Entrance Tank Material   | Concrete/PVC     | Concrete         | PVC                  | Concrete                            |
+--------------------------+------------------+------------------+----------------------+-------------------------------------+
| Design Flow for 1 Filter | <.75 L/s         | .764 - 7.024 L/s | .764 - 7.024 L/s     | >8 L/s                              |
+--------------------------+------------------+------------------+----------------------+-------------------------------------+
| Sand Layer Height        | 15cm             | 20cm             | 20cm                 | 80cm head loss                      |
+--------------------------+------------------+------------------+----------------------+-------------------------------------+


[Add a section (table or figure) on your proposal for number and size of filters as a function of flow rate over the range of flows that you anticipate EStaRS will be used.]

Overall Filter Size
===================================================

Generally 2 or more filters are considered, so that one can still be in use when the other is being backwashed. The number and size of the filters as a function of the design flow rate and the maximum flow a filter of a particular size can handle.

In the design the first step is to determine what size EStaRS is needed because this determines nearly every parameter. :numref:`figure_body_d_and_n` shows the process by which the number and size of EStaRS is determined.

.. _figure_body_d_and_n:

.. figure:: ../Images/figure_body_d_and_n.png
    :width: 70%
    :align: center
    :alt: flowchart showing how the filter size is determined, internal image

    This flowchart shows the way the plant flow is used with the available pipe diameters to determine an appropriate size and number of filters based on the total plant flow.


The constraint that defines the filter body size is ultimately the backwash velocity. For the sand used in the filters the required upwards velocity to fluidize the sand is 9.8 mm/s. Using this velocity and the flow area of a pipe, as based on the inner diameter, provides a maximum flow for the filter, based on :math:`Q_{Filter} = V_{BW}*A_{Filter}`. This :math:`Q_{Filter}` describes the flow that must be seen for backwash to happen properly. Another array is generated by diving :math:`Q_{Plant}` by :math:`Q_{Filter}`. This array is equal to the required number of filters (:math:`N_{Filter}`) of a particular diameters to serve a plant with a flow of :math:`Q_{Plant}`. The value that is the smallest number of filters greater than or equal to 2 should is chosen, and the corresponding index of pipe diameter yields the size. If the chosen number is not an integer, it is rounded up to the nearest integer to provide the number of filters to be included. Rounding up guarantees that the entire plant flow can be filtered.




Constraints for Inner Parts
==============================


From the determination of the filter body size, the branch and trunk manifolds are the next most important feature of the design. Some relevant variables defined here. These are constrains that are set before component dimensions are determined.



+-----------------------------+--------------------------------------+--------------+-------------------------------------------------------------------+
| Variable Name               | Description                          | Default Value| What Constrains the Default Value                                 |
+=============================+======================================+==============+===================================================================+
|  :math:`ND_{BallValve}`     |                                      |        3 in  |                                                                   |
+-----------------------------+--------------------------------------+--------------+-------------------------------------------------------------------+
|  :math:`ND_{BedTester}`     |                                      | 0.5in        |                                                                   |
+-----------------------------+--------------------------------------+--------------+-------------------------------------------------------------------+
|  :math:`ND_{BedTesterOuter}`|                                      | 1in          |                                                                   |
+-----------------------------+--------------------------------------+--------------+-------------------------------------------------------------------+
|  :math:`ND_{FiAirRelValve}` | Air Valve diameter                   |        0.5in |                                                                   |
+-----------------------------+--------------------------------------+--------------+-------------------------------------------------------------------+
|  :math:`ND_{FiBwTrunkMin}`  | Minimum backwash trunk diameter      | 3in          |  Must fit branches and accommodate full filter flow               |
+-----------------------------+--------------------------------------+--------------+-------------------------------------------------------------------+
|  :math:`ND_{FiBwBranchkMin}`| Mininmum backwash branch diameter    |    1in       |  Slotted pipes cannot be fabricated smaller than 1 in             |
+-----------------------------+--------------------------------------+--------------+-------------------------------------------------------------------+
|  :math:`ND_{FiTrunkMin}`    | Minimum trunk diameter               |   2in        |  Must be able to fit branches without significant flow obstruction|
+-----------------------------+--------------------------------------+--------------+-------------------------------------------------------------------+
|  :math:`ND_{FiDrainExit}`   | Minimum drain pipe diameter          | 3in          |  Entire filter flow can drain with 10 cm of head                  |
+-----------------------------+--------------------------------------+--------------+-------------------------------------------------------------------+
|  :math:`ND_{FiOverflowEnt}` | Minimum overflow pipe diamete        |  3in         |  Entire filter flow can drain with 10cm of head                   |
+-----------------------------+--------------------------------------+--------------+-------------------------------------------------------------------+
|  :math:`ND_{FiBranchMin}`   |  Minimum branch diameter            |   1in        |  Slotted pipes cannot be fabricated smaller than 1 in              |
+-----------------------------+--------------------------------------+--------------+-------------------------------------------------------------------+
|  :math:`D_{OrificeMax}`     |  Maximum orifice size on branches    |     1/4in    |  Larger will leave gaps along the wings for sand to escape        |
+-----------------------------+--------------------------------------+--------------+-------------------------------------------------------------------+


*trunk sizes based on Juan Guzmán's recommendation in November 2018 to account for fabrication problems*

Another important value determined by the filter body size is the area of the filter which is defined as: :math:`ID_{pipe}^2 / 4`. This becomes important later in determination of the mass of sand needed.

The pipe sizes recommended in this section come from certain assumptions of the amount of head required to use the filter. In November 2018, the difference in elevation of the water level from the exit tank to the entrance tank was increased to 75cm (an additional increase from 60, which was decided a year or so earlier) so that extra head loss in the manifold system does not influence filter functionality as has been seen in the field. This additional head will allow smaller manifold pipes to be used, as the added head loss in smaller pipes (from the increase of velocity) will not overcome the entrance and exit heights. Smaller manifold pipes will mean the entrance and exit tanks can stay narrower, though taller.

The determination of sizes for the drain and overflow come from using the orifice equation and the maximum flow that could be seen in the filter with a 10 cm safety height due the height of the weirs in the entrance and exits boxes in the concrete design and the height of pipe stubs in the Micky Mouse design. The goal with the drain especially is to allow the water to exit at the same flow it is entering in the event that the outflow isn't working properly.

A schematic of these pipes can be see below in {Make a basic drawing of the filter or an Onshape drawing}. The image is not to scale, but shows generally how pipes are organized within the filter.

[We need an Onshape drawing! Perhaps early next year. The pipes MUST go to the floor. Exit to distribution starts at the bottom of the exit tank. Possibly the top of the exit and entrance tanks are only 10 cm above the filter body. Filter Body has an air vent. Need flow control weir system. Is it possible to have some of the pipes exit through the side of the entrance and exit tanks so those tanks don't have to be so large? Sand drain? Pipe stubs in entrance and exit tanks for automated switch from filter to backwash. Backwash drain pipe with valve? Considering putting numbers on the inlets and outlets so that you can ]


It is important that the heights between the top of the settled water inlet and the overflow are 10 cm apart because if that distance is too small the overflow may not be large enough to handle excess flow as based on the safety height to find the overflow pipe area.

During operation the height of water in the entrance tank is watched to determine when backwash is necessary as it rises as head loss in the filter increases.

In addition to these numerical constraints there are several other constraints that are more clearly outlined in words.

.. _word_constraints_of_the_filter:

1. All inlet and outlet pipes must bend and rest on the floor before connecting to the entrance or exit tank to prevent air from getting into the filter body.
#. The exit branches are slotted pipes and the inlet branches have orifices with wings
#. The branches on either side of a trunk are composed of one length of pipe meaning the trunk has to be large enough so the branches don't act like valves.
#. The branch spacing must be small compared to the sand layer depth, to efficiently use the sand. See :numref:`figure_layer_depth_and_branch_spacing` for a visual. They must however, also be far enough apart so that they can be feasible to fabricate.
#. The orifice spacing must be small compared to the branch spacing (for the same reasons as above)
#. The exit tank contain pipes for: the plant exit, the three filter outlets, and a drain.
#. The entrance tank contains pipes for: the four inlet pipes, an overflow pipe, and the inlet for the settled water.
#. During forward filtration there should be even flow between filters in parallel.
#. Within each filter there should be equal flow within each sand layer.
#. The filter body must have an air vent.
#. The filter body must contain a sand drain. (Which should only be used to replace sand, because it makes a mess!)
#. The maximum flow in the filter should only ever be what the filter is designed for!

.. _figure_layer_depth_and_branch_spacing:

.. figure:: ../Images/figure_layer_depth_and_branch_spacing.png
    :width: 70%
    :align: center
    :alt: schematic of brach spacing as comared to layer thickness, interal image

    This figure shows the way the branch spacing should be small compared to the sand layer thickness. Water flows in the direction of decreasing piezometric head as shown by the vertical arrows on the left. On the right the flow of water within each sand layer is shown. If the branches were further apart the lines showing the path of the water would not utilize all the sand within the layer, resulting in wasted space, a source of inefficiency in the filter. Thus keeping the branches close together is important. This will be explored numerically in a following section.

Filter Flow Rates and Layer Height
===================================

As the maximum flow of the filter is constrained by the available sizes of the pipe for the filter, the design flow of the filter is characterized by: :math:`Q_{Bw} = V_{Bw}A_{Fi}`. Filters **should not** be run at flows above those for which they were designed. In the determination of the size of the internal components of a filter the design flow of the filter should always be used, this ensures that all parts can handle the maximum flow in the filter

  .. note::
    It may seem peculiar that there is no minimum flow in the filter. This is because a filter, during forward filtration, will function fine at lower flows. A minimum flow constraint does occur with backwash, but if the flow is that low that less than one filter is needed it is unlikely that it will need to be backwashed regularly enough to be a concern. This issue has not been seen in any plant to date and is not accounted for in the design.


This design will focus on flow through one filter, as having several filters in parallel wouldn't alter the flow within one, though flow will be split between the filters. To do this a weir system is in place to split flow about evenly during forward filtration.

Within each filter the flow is then further split into the 6 layers of the filter.

The entire area of the filter is assumed to be active and is denoted as :math:`A_{Fi}`, as calculated previously as a function of ID.

Within each filter the flow is diverted across six layers. (:math:`N_{FiLayer} = 6`)

Thus the flow through each sand layer is: :math:`Q_{FiLayer} = \frac{Q_{Fi}}{N_{FiLayer}}`.

This is not the flow experienced by all the pipe layers though. As shown in :numref:`figure_numbered_filter_layers` the two inner inlets, I-2 and I-3 each serve 2 filter layers and as a result carry flows that are double :math:`Q_{FiLayer}`

.. _figure_numbered_filter_layers:

.. figure:: ../Images/figure_numbered_filter_layers.png
    :width: 70%
    :align: center
    :alt: filter manifold layer schematic, interal image

    This schematic shows the layers of the filter and the amount of flow within each pipe layer.

This is important in knowing the maximum flow that will be in a trunk or branch at any given time, as that will be used to determine the orifice area as a function of the allowable head loss in combination with the spacing of branches and as a result the flow in each branch.



Sand Layer Thickness and Branch Spacing
============================================


In the EStaRS filters, of all three sizes (1ft, 2ft, and 3ft), the sand layer thickness will be 20cm for each layer, except for filters designed to go with PF300 plants, then the depth will be 15cm so that all processes can be at the same elevation. In the OStaRS there are functions that define the sand layer depth, but the minimum distance, 20cm is applicable until trunk diameters are larger than 6 inches. Because for EStaRS this variable is unchanging the equations are not included, but it can be found in the OStaRS filter design file in the :ref:`sand layer thickness <heading_sand_layer_thickness>` section.

The OStaRS filters have an option to increase the layer depth to account for the added width of the pipes in a larger filter, but in the EStaRS the trunk sizes will never be large enough because the flow is substantially lower.

So:

.. math::

  H_{FiSandLayer} = 20cm

This is the center to center distance of the trunks.

As described in the constraints above, the spacing of the branches must be small compared to the layer depth. In this case, small can be taken to be half the distance, so :math:`\Pi_{Spacing} = 0.5`. Thus:

.. math::

  S_{Branches} = H_{FiSandLayer}*\Pi_{Spacing} = 10cm

This is the center to center distance of the branches and is meant to balance even flow distribution across each layer with ease of fabrication and material use (i.e. having 100 branches would mean very good flow distribution, but would be impossible to fabricate).

Then the number of branches on each side of the trunk is:

.. math::

    N_{FiBranchMin} = round(\frac{ID_{FiPipe}}{B_{FiBranchMax}})

the ID function also takes the SDR for the pipe (26), but in the equation above was left out so the overall mechanism of the calculation is clearer. The value is rounded because an integer number of branches is needed. The various dimensions of each filter pipe layer can be seen in :numref:`figure_manifold_sizing`.

.. _figure_manifold_sizing:

.. figure:: ../Images/figure_manifold_sizing.png
    :width: 70%
    :align: center
    :alt: filter manifold schematic, interal image

    This schematic shows the general naming and dimensions for one layer of the filter. This is a top down view.

Setting the number of branches allows the flow within each branch to be determined, knowing that the area of the inlet orifices can be determined. It will also allow the sizes of branches and trunks to be determined.

In determining the size of the trunk and branches of the EStaRS the pressure recovery constraints are the most important design considerations. Having a pressure recovery term that is too high will lead to an uneven flow distribution. The two pressure recovery terms that are of particular concern are those in the trunks and branches during forward filtration, and the pressure recovery in the lowest branch during backwash. The first step is to find the flow rate in the branches. Then the PR constraint can be used to find the minimum diameter needed for forward filtration and during backwash.



.. _flow_distribution_constraints:

Flow Distribution Constraints: ratio of pressure recovery to clean bed head loss
===================================================================================

In the EStaRS there are three components where flow distribution must be considered:

1. Between slots along outlet manifold branches and between orifices on inlet branches

2. Between branches along manifold trunks

3. Between filter layers

Having uneven flow distribution is unwanted for several reasons, the mostly importantly being that the goal is for each parcel of water to spend approximately the same amount of time in the filter. If flow isn't distributed well the distribution of residence times for the parcels will widen which decreases treatment efficiency.

The basis of this part of the design is using head loss in an analogous way as resistors in an electrical system. If head loss is intentionally high at a certain point in the filter, then other differences between paths (such a length of the pipe, or which orifice along a branch is the outlet) will not matter because the head loss of those differences is comparatively small. Additionally, some variation is considered. Creating a system with perfectly identical paths would be extraordinarily complex and would require setting the head loss (and pressure recovery) to zero for paths that have different lengths, so some dissimilarity is allowed for the sake of simplicity.


Design
-------

The relative distribution of the flow through a particular path is defined as:

.. math::

  \Pi_Q = \frac{Q_{long}}{Q_{short}} = \sqrt{\frac{C_{p_{Short}}}{C_{p_{Short}}}}

| Such that:
| :math:`\Pi_Q =` the ratio of flow
| :math:`Q_{long} =` the flow through the longest filter path (lowest layer, at the furthest slot on the furthest branch)
| :math:`Q_{Long} =` the flow through the shortest filter path (top layer, closest slot on the first branch)
| :math:`C_{p_{short}} =` pressure coefficient at the end of the shortest path
| :math:`C_{p_{long}} =` pressure coefficient at the end of the longest path

:math:`C_p` is defined thoroughly in :ref:`Filtration Introduction <title_filtration>`

.. math::

  \Pi_Q = \frac{Q_{long}}{Q_{short}} = \sqrt{\frac{h_{L_{sand}}-PR}{h_{L_{sand}}}}


| Such that:
| :math:`h_{L_{Sand}} =` the head loss in the sand bed
| :math:`PR =` pressure recovery (as defined by: :math:`\frac{V^2}{2g}`)


:math:`PR = h_{L_{sand}}(1- \Pi_Q^2)`

These relationships define the head loss constraints of the filter.

The ratio, :math:`\Pi_{Q}` has been  somewhat arbitrarily given a value of :math:`0.85`, meaning the flow exiting the longest path is 85% of the flow exiting from the shortest path.

Thus from above:

:math:`1 - \Pi_{Q}^2 = .278 = \Pi_{ManifoldHeadLoss}`

Where the ratio of the pressure recovery in the branches to the head loss through the clean bed (or through just the slots/holes in backwash) is:

:math:`\Pi_{ManifoldHeadLoss} = \frac{PR}{h_{L_{sand}}}`

**make this useful**

This equation is used to determine the smallest pipe size that meets the pressure recovery constraint for a certain flow. It almost provides a maximum value for head loss within the system, summing the various pressure recovery terms and comparting to this value will show if the design makes sense. As the head loss through  the sand is known, the equation can be directly solved for pressure recovery. From the total filter flow the flow through any branch can be determined. As the pressure recovery term is directly related to the velocity in the pipe a maximum velocity can be determined from the PR term. This maximum velocity can be used to find the minimum area for the branches from pressure recovery, which can provide a pipe diameter. This value can be compared to the minimum determined by the fabrication constraint of the slotted pipes and the larger of the 2 minimums is used for the design.

Though the piezometric head profiles for the inlet and outlet manifolds for the middle layers may be parallel, meaning the pressure recovery is less constrained for a good flow distribution, a tight constraint is still needed for the outer manifolds where the velocity is 1/2 and the PR is 1/4 (because pressure recovery goes with the square of the velocity) that of the inner layer, while the term is smaller still in the bottom-most manifold where the velocity head is tiny as the diameter is larger to accommodate for full filter flow during backwash.

See the section on Pressure Recovery  in :ref:`Filtration Intro <title_filtration>` for more infomation if this is unclear.






Flow in branches to find orifice area and number
--------------------------------------------------


The overall steps to find the total orifice area and number of orifices necessary:
  1. Determine the fraction of flow that comes out of the longest branches
  2. Set head loss to be low (<5cm)
  3. Use the flow that will be in the largest branch to determine the area
  4. Set the area of one orifice to be the largest it can be due to fabrication constraints.
  5. Divide the area obtains in 3 by the area of one orifice as determined in 4. This is the number of orifices necessary on the longest branch.

*The number of orifices for the other branches requires the spacing of the orifices which requires the trunk size, which is determined later, so hold tight.*

As shown in the previous section maximum flow in a trunk will be either :math:`Q_{Fi}` or :math:`\frac{Q_{Fi}}{3}` (the equivalent of :math:`2Q_{Layer}`). As we are concerned with maximum flows and corresponding maximum velocities, those flows are considered for the design.

In this case the longest branch is slightly less than :math:`\frac{ID_{Fi}}{2}`. To keep the calculations simple the maximum fraction of the flow served by any branch would be in the longest branch, the approximate area of the filter layer served would be approximately the length of this branch time the spacing of the branches. :numref:`figure_flow_fraction_branch`

.. _figure_flow_fraction_branch:

.. figure:: ../Images/figure_flow_fraction_branch.png
    :width: 80%
    :align: center
    :alt: filter schematic, interal image

    The red box shows the approximate area served by the longest branch. The area is slightly overestimated, but using a rectangular area and by assuming the branch is exaclty half the length of the inner diameter ensures that the largest fraction possible does not exceed what is designed for.


From that area, the fraction of the filter layer served by the hypothetical longest branch can be directly found by dividing that area by the total cross-sectional area of the filter.

.. math::

   \frac{(\frac{ID_{Fi}}{2} * S_{Branch})}{\pi*\frac{ID_{Fi}^2}{4}}  = \Pi_{branch}
   \\ \\ Then: \\ \\
   \Pi_{branch}*2Q_{FiLayer} = Q_{BranchMax}


This describes the largest flow in any branch during forward filtration. For the backwash branches the only difference is with the flow:

.. math::

  \frac{\frac{ID_{Fi}}{2} * S_{Branch}}{\pi*\frac{ID_{Fi}^2}{4}} =  \Pi_{branch}
  \\ \\ Then: \\ \\
  \Pi_{branch}*Q_{Fi} = Q_{BranchBWMax}


These two flows can be used with the pressure recovery terms to determine the smallest branch sizes that can work.

Using this flow the total area of the inlet orifices can be found for the longest branch, this area can then describe the number of orifices and their spacing. The spacing then applies to all the branches not just the longest one.

Because the pressure recovery in the branches is the constraint in determining total orifice sizing, it is convenient to first consider the generic pressure recovery term:

.. math::

  h_L = \frac{(\frac{Q}{\Pi*A*\epsilon})^2}{2g}

In the equation above the HL is equivalent to the pressure recovery, the velocity term has just been replaced with the flow to area ratio at the inlets or outlets. Depending on which inlet or outlet system is being looked at the porosity term and flow term will vary. Additionally, we are setting the head loss to be small so the term being found is the total area required to keep the head loss small. Thus it can be rearranged to:

.. math::

  A = \frac{1}{\frac{(\sqrt{2g*h_L})*\Pi*\epsilon}{Q}}

The suggested design head loss for the inlets and outlets is 5 cm, but is flexible in the . The following table shows the other constraints used to solve for the required areas.


.. _table_branch_head_loss:

+--------------------------------+-------------------------+--------------------------------------+-----------------------+-----------------+-----------+
|                                | :math:`Q`               | :math:`h_L`                          | :math:`\epsilon`      | :math:`\Pi`     | :math:`g` |
+================================+=========================+======================================+=======================+=================+===========+
| :math:`A_{InletOrifices}`      | :math:`Q_{BranchMax}`   |:math:`h_{L_{InletOrificesFW}}= 5cm`  | 1                     | :math:`\Pi_{VC}`| g         |
+--------------------------------+-------------------------+--------------------------------------+-----------------------+-----------------+-----------+
| :math:`A_{OutletSlots}`        | :math:`Q_{BranchMax}`   |:math:`h_{L_{OutletSlotsFW}}= 5cm`    |:math:`\epsilon_{sand}`| :math:`\Pi_{VC}`| g         |
+--------------------------------+-------------------------+--------------------------------------+-----------------------+-----------------+-----------+
| :math:`A_{BWorifices  }`       | :math:`Q_{BranchBWMax}` |:math:`h_{L_{BWorificesBW}}= 5cm`     | 1                     | :math:`\Pi_{VC}`| g         |
+--------------------------------+-------------------------+--------------------------------------+-----------------------+-----------------+-----------+

Though the bottom inlet layer has two conditions for flow, forward filtration and backwash, the flow is six times higher during backwash, so the forward filtration condition is not considered, as it would not be the limiting head loss. For the same reason the top inlet is not considered because its flow will always be lower than that in the two inner inlets serving two layers.


This area is the total area of inlet/outlet space required along the longest branch.

If we assume that:

.. math::

    D_{Orifice} = D_{OrificeMax} \\ \\ Then: \\ \\ D_{Orifice} = 0.25in

This diameter can be used to find the area of one orifice, :math:`A_{Orifice}`.

Then:

.. math::

   \frac{A_{InletOrifices}}{A_{Orifice}} , \frac{A_{BWorifices}}{A_{Orifice}}


are the respective number of orifices necessary on the longest branch for the regular inlet manifolds and the backwash manifold respectively.

Those values divided by the length of the longest branch provides the spacing for the orifices. However here it become important to use the actual longest length of the branch, so that it is clear that all the orifices will fit.

The factors that makes the length of the branch different from simply :math:`ID/2`, are the cap on the end and the width of the trunk. These can both be seen in :numref:`figure_branch_length`

.. _figure_branch_length:

.. figure:: ../images/figure_branch_length.png
    :width: 80%
    :align: center
    :alt: filter manifold, interal image

    This image shows an old image of a filter inlet manifold. The center dotted line shows the midline of the trunk, and the circle shows the cap on the end of one branch. The radius of the trunk and the depth of the cap at then end must be subtracted from the length to determine the spacing of the orifices. This image also shows how not all of the branch length is used for inlet orifices.

Before getting to the diameter of the trunk, the branch diameter must be found. Following the same process as above it is possible to determine the area necessary to limit the pressure recovery term. Additionally there is a minimum branch constraint due to the fabrication of slotted pipes.

**mention slots as well since they have to be included, they can be in a different section but should still be around here somewhere** They also depend on the size of the branch because of the curvature


Flow in trunks to determine branch area
----------------------------------------

As stated above the maximum flow in a trunk will be either :math:`Q_{Fi}` or :math:`\frac{Q_{Fi}}{3}` (the equivalent of :math:`2Q_{Layer}`). As we are concerned with maximum flows and corresponding maximum velocities, those flows are considered for the design.

The number of branches is set based on the spacing constraint, thus all this section aims to find is an acceptable area of the branches to keep pressure recovery low to keep flow distribution even.

Again begin with:

.. math::

  h_L = \frac{(\frac{Q}{\pi*A*\epsilon})^2}{2g}

And then rearrage so solve for area:

.. math::

  A = \frac{1}{\frac{(\sqrt{2g*h_L})*\pi*\epsilon}{Q}}


Where, the conditions are the same as for the :math:`A_{BwOrifices}` above except that :math:`Q = Q_{Fi}` for the backwash condition and :math:`Q = \frac{Q_{Fi}}{3}` for the forward filtration condition.

The areas determined is the minimum total area of the branches, :math:`A_{BranchTotalMinBW}` and :math:`A_{BranchTotalMinFW}`. As the number of branches is determined solely by the size of the filter, dividing this area by the number of branches yields the minimum area of an individual branch. Here is it important to remember that both sides of the trunk have branches!

.. math::

    Remember: \\
    N_{BranchTrunk} = 2*Round(\frac{ID_{Fi}}{B_{FiBranchMax}})
   \\ So: \\
    A_{BranchMinBW} = \frac{A_{BranchTotalMinBW}}{N_{BranchTrunk}}
   \\ and \\
    A_{BranchMinFW} = \frac{A_{BranchTotalMinFW}}{N_{BranchTrunk}}


Those areas directly correspond to diameters. To keep the design consistent the same size pipe will be used for all branches so the larger of the two sizes (which will be from the backwash calculation) will be used to determine the size of the branches. If both values are smaller than the minimum needed to slot the pipes, then the predefined minimum will be used. If the diameter calculated is not a regular pipe inner diameter the next largest actual pipe size should be used.

Outlet area, slots and affirmation of branch sizing
---------------------------------------------------------


Due to fabrication methods for the slotted pipes (manufacturing by machine), the slot width, :math:`B_{slot}` is always 0.2 mm. The number of slot rows is also fixed at 2, because each branch has slots on both sides. This constrains the minimum size that the slotted pipes can be, becasue


the total slot area for one outlet layer needs to be able to accept :math:`\frac{Q_{Fi}}{3}`, this includes two layers of slots on each branch.

The total area of the slots for one layer should be at least equal to the total orifice area on the inlet manifolds of the the inner two inlet layer (the ones that each serve :math:`\frac{Q_{Fi}}{3}`). Assuming that flow will be distributed on the same way for the outlet manifold as it was on the inlet manifold, in terms of relative flow per branch, it then follows that the area of orifices on the longest outlet branch should be equal to the area of orifices on the longest inlet branch (which are the same length!):

.. math::

    A_{SlotsLongestBranch} = A_{OrificesLongestBranch}

Knowing the slot width makes determining the total slots length of the longest branch easy to find.

.. math::

   \frac{A_{SlotsLongestBranch}}{B_{Slot}} = L_{SlotsLongestBranch}

From the cumulative area of slots and the width of the slots, the total length of slots can be determined. This length of slots is for one side of one branch *yes?*

As the branches are different lengths along one trunk, the number of slots is different per branch depending on the length, but the spacing is the same so the variation is accounted for.



Pressure Recovery and branch diameter to determine trunk sizing
-------------------------------------------------------------------

In determining the trunk size both pressure recovery and the influence of the branches intercepting the trunks must be considered.

.. _figure_branch_configuration:

.. figure:: ../Images/figure_branch_configuration.png
    :width: 80%
    :align: center
    :alt: branch photograph, interal image

    1. Image 1 shows the use of 1 pipe for the branches on both sides of the trunk, the location of the opening into the branches causes the pipe to act as a valve inside the trunk. This causes massive head loss in the filter. 2. Image 2 shoes an alternate method of connecting branches to trunks, with 2 separate pipes being used. In this design it takes much less force to dislodge the branch from the trunk due to the cantilever of every branch. 3. Image 3 shows a similar branch construction as in image 1 but with the hole in the branch drilled in such a way that it causes a smaller (but still significant) flow constriction. 4. Image 4 shows a branch in a similar orientation to image 1 but, the branch is going through a larger pipe so the flow constriction is not as significant.


The images above show some of the challenges with determining the size of the trunks, as well as the importance of thoughtful fabrication.

**Must figure out the importance of the valve effect on this to determine the algorithm**

Trunk sizing and caps: orifice and slot spacing
------------------------------------------------------



Determining Forward Filtration and Backwash Velocities
--------------------------------------------------------

See  :numref:`figure_estars_flow_schematic` for a schematic of the filter layers. For a schematic of flow during backwash see :numref:`figure_estars_bw_flow_schematic`.

.. _figure_estars_flow_schematic:

.. figure:: ../Images/figure_flow_distribution_estars.png
    :width: 80%
    :align: center
    :alt: filter schematic, interal image

    This schematic shows the flows through every inlet and outlet components of the EStaRS system. Each of the outlets takes in flow from two filter layers as do the inner inlets. The outer inlets provide water for only one layer. The bottom inlet must also accommodate the flow required for backwash and is larger in diameter to account for this.

Because the 2 inner inlets (the ones that aren't the backwash trunk or the uppermost trunk) distribute flow to two layers the flow between them is equal to :math:`2Q_{FiLayer}` which is shown in the schematic. In a later section, we will show that the flow within each layer is not exactly even because of the head loss through various paths, but for the calculation of maximum flow, even flow is an appropriate guess.


.. _figure_estars_bw_flow_schematic:

.. figure:: ../Images/figure_bw_flow_distribution.png
    :width: 80%
    :align: center
    :alt: filter schematic, interal image

    This schematic shows the flows through an EStaRS during backwash. For the design, it is assumed that filter is being used to full capacity so that flow total flow during forward filtration is equal to the backwash (design) flow. In practice those values might be different, in which case the flow is the design flow, **not** the sum of the filter layers. Rather than the outlet pipes, a separate backwash manifold is used to discard the water used during backwash.

On each layer trunk, there are :math:`N_{FiBranch}` branches on **each side** of the trunk. That means the total number of branches on each trunk is :math:`2N_{FiBranch}`



Using the minimum ND of the Filter Manifold Branches, as defined above, the minimum flow area of a branch can be calculated: [I'm lost here. You haven't calculated the Branch diameter yet. See my approach above for calculating the area served by one branch. The ID of the branch is irrelevant. I now realize that we made a mistake in first creating the text. You can't see the mistakes if you don't actually do the calculations. I always develop a method in a calculation space (now python) AND in an equation derivation space (now RST)].



First Constraint: Pressure Recovery in Trunks During Forward Filtration
---------------------------------------------------------------------------

[This section needs to go above the section where you calculate the branch diameter given the PR constraint.]

The total allowable pressure recovery of the filter manifold is controlled by the head loss in each sand layer and the head loss ratio, :math:`\Pi_{ManifoldHeadLoss}`, as defined above in :ref:`Flow Distrbution Constraints <flow_distribution_constraints>`.

The head loss through the sand layer, :math:`HL_{FiCleanLayerMin}` is a fuction of layer depth, :math:`H_{FiLayer}` and overall velocity of the filter , :math:`\frac{Q_{FiLayer}}{A_{Fi}}`, using the Kozeny Equation in :ref:`Headloss Requirement <heading_headloss_requirements>` in the Filtration Design section.

Using the definition of the pressure recovery ratio, the maximum allowable pressure recovery in the filter manifold can be calculated, this value is not necessarily the actual pressure recovery the system may see, just the allowable maximum:

.. math::

  PR_{FiMax} = HL_{FiCleanLayerMin}*\Pi_{ManifoldHeadLoss}


Subtracting the previously calculated branch PR from this maximum determine how much PR is theoretically left for the trunks. The maximum trunk PR can then be calculated back to a velocity.
[The PR in the branches must be low in order to ensure uniform flow along the length of a branch. The PR in the Trunks must be low to ensure that each branch has the same piezometric head driving flow into (or out of) the filter. Also note that there will be another constraint for the trunk that is designed to get uniform flow distribution between filter layers. And one must consider the flow blockage in the trunk line caused by the branches when calculating the pressure recovery.]

.. math::

  PR_{TrunkEst} = PR_{FiMax} - PR_{FiBwManBranchEst}

  V_{FiTrunkMaxPR} = \sqrt{2g*PR_{TrunkEst}}


The velocity is important because it, along with the known flow rate through the trunk, are used to find a theoretical area for the flow. This area sets and ideal ID for a trunk pipe. Using the pipe database allows a search for the closest match.

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


For the chosen ND, the corresponding ID is used to determine the PR in the branches with SDR26.

.. math::

  PR_{FiBranch} = \frac{(\frac{\frac{2Q_{FiLayer}}{2N_{{FiBranch}}}}{(\pi\frac{ID_{FiBranch}^2}{4})})^2}{2g}


The sum of the PRs from the branches can then be compared to the maximum allowable PR term. If the design logic worked properly then :math:`(PR_{FiBranch} +  PR_{FiTrunk}) < PR_{FiMax}` with  :math:`PR_{FiBranch} +  PR_{FiTrunk} = PR_{FiMan}` indicating the pressure recovery in the Filter Manifold.

Second Constraint: Pressure Recovery in lowest trunk during backwash
------------------------------------------------------------------------

The second pressure recovery constraint is in the backwash branch during backwash. During backwash the lowest trunk sees all the flow at a higher velocity than any other trunk does during filtration meaning all of its branches experience a higher flow as well. Because the velocity is higher, the PR term will also be higher, so it must be constrained to maintain even flow.

The initial estimate of head loss through the holes is :math:`HL_{FiBwOrifices} = 10cm`. [where did this come from? One proposal is the same constraint as we discussed with the horizontal filter. The head loss through the orifice must be close to the distance between orifices. This is to ensure that the entire bed fluidizes. If there is a section of the filter where the sand isn't fluidized, then that sand will form an incline that is the angle of repose of sand in water. Thus, the maximum depth that the first covered orifice under the settled sand will be determined by the distance between orifices and the angle of repose of the sand. If we assume conservatively that the angle of repose is 45 degrees, then the depth of sand would equal the spacing between the orifices. And if the head loss through the orifices was equal to that depth of sand, then there would be enough water coming out of the first covered orifice to fluidize the sand above it.

Darn... My analysis in the previous paragraph is flawed because the water flows from the orifices into a big half pipe BEFORE coming into contact with sand. Thus, the head loss through the orifices DOES NOT help ensure that the sand fluidizes everywhere in the filter. Similarly, the orifices don't have to be sized to get the same flow out of the first and last orifice in a branch because flow equalization will occur in the half pipe. So perhaps the goal is to get reasonable flow distribution between first and last orifice so that the equalization flow has a much lower velocity than the main flow in the branch. We need to figure this out! and this can go near the top of the design. My sense is that there may be a good deal of flexibility in the total orifice area.   ]

[Need to start by calculating the diameter of these orifices and somehow set the spacing between orifices. This requires a design algorithm. Not sure of the steps yet. I understand that the maximum size hole that can be drilled is something close to 1/4" because larger holes end up coming out the side of the gap between the wing pipe and the branch. Once you know the max diameter that can be used for the orifice (Juan should know this) then you can calculate the total maximum orifice area required (based on an algorithm that we need to invent). Then calculate the spacing between the orifices to get the required number of orifices.  ]

Using the head loss ratio, :math:`\Pi_{ManifoldHeadLoss}` , the allowable PR can be determined: :math:`PR_{FiBwManMax} = HL_{FiBwOrifices}*\Pi_{ManifoldHeadLoss}`


Manifold Pipe Lengths
======================



Come back to this a little bit... depends on fabrication methods

Inlet Orifice and Outlet Slot Design
========================================
[I believe these calculations can go above the pipe size calculations. I believe the orifice area is set by the backwash fluidization of the next covered orifice constraint. And I think that constraint is minimal because the orifices end up being very close together. ]

Knowing the PR in the BW manifold, the design head loss through the outlet orifices can be determined based on:

.. math::

  HL_{BwOrifices} = \frac{PR_{BwManTotal}}{\Pi_{ManifoldHeadLoss}}

With this head loss the necessary total area of the orifices for the backwash branch can be determined using the orifice equation **REF**, as :math:`HL_{BwOrifices}` , :math:`\Pi_{VCOrifice}`, and :math:`Q_{FiBw}` are known.

This area is doubled to find the area of the slots. [I am not sure why this is true? Because two layers are served perhaps?]

  .. math::

    A_{FiManSlots} = 2*A_{FiBwOrifices}



Also the area of the backwash orifices is equal to :math:`A_{FiTopManSlots}`, which is the area of the manifold that takes in backwash water for removal from the treatment train.





Inlet Design
--------------

Regarding the inlets, those for backwash are determined differently than the orifices on the rest of the inlet branches. This section traces the process for the backwash branches and then the rest of the manifold branches.



The only difference between the two is the length of the branches. Because the backwash trunk is slightly larger than the rest of the trunks, the branches must be slightly shorter so that the whole manifold fits in the filter body.

Then for each the total number of orifices necessary for a layer of the manifold can be found by summing the array of number of holes (:math:`N_{BranchOrifices}`) and multiplying by 2 to account for the trunks having branches on two sides.

The drill bit sizes considered are 1/16 inch, 1/8 inch, 3/16 in, and 1/4 inch. The maximum hole size is 1/4in because when the holes are larger they stick out from under the edge of the wings. This is constrained by the curvature of the wings as shown below in **Figure XYZ**



Pipes 2, 4, and 6 (the outlet pipes) are all identical and the total head loss through the outlet system is approximately three times the :math:`HL_{OutletSlotForWard}` as calculated based on the table above. The outlet pipes are the only pipes where the porosity of the sand is accounted for because the outlet slot system is the only place in the filter where the sand interfaces with the pipe openings. The exclusion zones prevent sand at the inlets and as such the porosity is not accounted for in any other head loss calculation, see **FIGURE SOMETHING OR OTHER FOR IMAGE OF THE EXCLUSION ZONE**. Pipe 7 experiences 2 different head losses depending on whether the filter is in forward filtration or backwash. Pipes 3 and 5 are also identical.

Additional note for :numref:`table_branch_head_loss`. The pipes show the overall flow direction at each layer. The each of those numbers pipes, from a vertical cross-sections looks generally like the trunk and branches in :numref:`figure_circle_branches`.

.. _figure_circle_branches:

.. figure:: ../Images/figure_circle_branches.png
    :width: 60%
    :align: center
    :alt: basic sketch of flow path within a manifold layer

    A generic sketch of one layer of a manifold. The yellow arrows indicate this is an influent manifold. The number of branches is variable depending on the size of the filter.


Having these geometries and head losses determined means the parameters for the rest of the system can be determined, as most of it depends on the sizes of the trunks and branches.

Entrance and Exit Pipe Dimensions for "Micky Mouse" design
============================================================

The construction of the entrance and exit pipes are the main difference between the "conventional" filter entrance/exits tanks and the "Micky Mouse" design. The difference can be seen in the :numref:`figure_estars_comparison`

.. _figure_estars_comparison:

.. figure:: ../Images/figure_estars_comparison.png
    :width: 80%
    :align: center
    :alt: CAD "conventional" vs micky mouse photo design

    These images show the difference in the two styles of EStaRS. In the image on the left, the "Micky Mouse" design is shown. the two pipes on the upper right and left are the entrance and exit tanks for the filter. The image on the right shows the EStaRS design that is more similar to the design of the OStaRS with a concrete entrance and exit system. Note that these two systems are for different flow rates which is why the image on the right shows two modules.

In this sections the sizes of these tanks are determined.

The size of the entrance and exit tank pipe dimensions is constrained by the sizes and number of the pipes that feed into or out of each tank.

The entrance needs to have space for: 4 inlets, one of which is the bottom, slightly larger pipe for backwash, an inlet from the sedimentation tank, and an overflow pipe, so that if the entrance pipe overflows the water is directed elsewhere rather than just spilling all over the place. The outlet tank pipe requires space for three outlets from the filter, an outlet to the plant exit, and a drain in the event that maintenance needs to be done or if the effluent quality is not sufficient.

The pipes connect lengthwise with the pipe so it is their total area that must fit with the area of the tanks. In addition to the pipe area, they will be connected with flexible couplings, which add extra space considerations. Additionally, for ease of fabrication the flexible couplings should not be closer than 1 cm to each other. The pipe sized determined in this section come from using Onshape to determine feasible pipe placements (as there are many configurations that may fit)

The minimum sizes for the trunks and drains specified at the beginning of this file turn out to be sufficient for each design, therefore the entrance tank must accommodate: 4 2" pipes and 1 3" pipes (with the overflow being the only pipe that comes from the side of the tank). These dimensions require a 12in pipe. The exit tank requires 4 2" pipes and 1 3" pipe as well, but the drain is included in that number. Thus a 12" pipe is required for the exit as well.

Total Sand Depth, Filter Pipe Length
=================================================

In determining the total sand depth and total length of the filter pipe several distances are assumed:

| :math:`T_{BottomCap} = 1 in` This is the thickness of the cap at the bottom of the filter, without this cap the pipe would be open on the bottom.
| :math:`H_{TopCap} = 6 in` This is the overlap of the cap onto the filter pipe.
| :math:`H_{FilterValve} = 10 cm` This is the height of the sand drain. It should not opened unless all the sand is to come out of the filter!
| :math:`H_{FiBottom} = 5cm + T_{BottomCap}` This is the elevation at which the sand starts, and exists because the cap has thickness.
| :math:`H_{FluidizedBedtoSiphon} = 20cm` This is a safety distance to prevent sand from ever escaping the filter during filtration or backwash.

The minimum height of sand in the filter is the depth of each filter layer times the number of filter layers plus the outer radius of the backwash trunk. The outer radius is added because the layer height is defined as the center-to-center distance of the layer, but on the bottom layer there is an additional radius depth of sand, as shown in the following equation.

:math:`H_{FiSand} = N_{Layer}*H_{FiLayerMin} + OR_{BwTrunk}` **the actual height should just be calculated here?**


The active sand depth (the sand actually used during filtration) is just the number of layer times sand depth. This depth is useful to consider how much sand is being used during filtrations. **should this consider the sand around each branch/trunk or does that not matter?**

:math:`H_{FiSandActive} = N_{Layer}*{H_FiLayerMin}`

The total height of the filter needs to account for the safety distance to prevent sand escape in addition to the necessary space for the sand to fluidize. At the velocity backwash occurs, the ratio of the fluidized bed height to the settled bed height is: :math:`\Pi_{FiFluidized} = 1.3`

It is assumed that all of the sand fluidizes so that:

:math:`H_{FluidizedBed} = \Pi_{FiFluidized}*H_{FiSand}` **make this variable match up**

Then, the height of the filter, characterized as a length because it is in the direction of flow is the sum of these components:

.. math::

  L_{FilterBody} = H_{FiBottom} + H_{FluidizedBed} +  H_{FluidizedBedtoSiphon} + OD_{BWTrunkFitting} + S_{Fitting}

Where :math:`S_Fitting` is the spacing of the fitting? **But what does this look like? Add a pic**

This length comes out to be around 2 meters which is much less than that required for an OStaRS!

.. _fluidized_bed_headloss_variation:

Fluidized Bed Head Loss and Variation
======================================

One the depth of the fluidized bed is determined, the steady state head loss during backwash can be determined. Knowing this will inform later assumptions about relative head loss in the system.

The following expression is used to find this value:

.. math::

  HL_{BwSS} = \frac{H_{FiSand}*(\rho_{Sand} - \rho_{Water})*(1 - \epsilon_{Sand})}{\rho_{Water}}

This head loss value should be very close to the depth of the settled sand bed.  This equation for head loss comes from **...where does it come from....**


The head loss of a dirty bed is taken as :math:`HL_{FiDirty} = 0.75m` As a result the height in the filter for backwash initiation to occur is the sum of head loss in the other components. **check this**

.. _plumbing_head_loss:

Plumbing Head Loss
=====================



Path head loss calculations and flow distribution between layers
=================================================================

Now that the sand layer depth is set the Kozeny Head Loss can be determined for the clean bed and the head loss through various flow paths can be determined.

First use the Kozeny equation from :ref:`Headloss Requirements <heading_headloss_requirements>` to find the head loss in each of the sand layers. In the design for the OStaRS a different layer height may be used for the bottom layer to account for the larger backwash pipe, but in the EStaRS that difference does not matter, as that additional depth does not contain head loss that matter for the flow.

As the filter has 6 layers there are six possible paths for the water to take. The calculations for head loss through each layer depends specifically on which layer when it comes to minor loss coefficients and lengths of flow paths but the overall process is the same. This section outlines the algorithm without going into the specific calculations necessary for the head loss determination.


In each path, the path head loss is the sum of : inlet plumbing major and minor losses, sand layer losses, and outlet plumbing (for the relevant flow) minor losses

The design steps are as follows:

1. Find the max head loss through the respective paths (Q1 - Q6) using the equations specified in :ref:`Plumbing Head Loss <plumbing_head_loss>`

#. Find the min head loss through the respective paths (Q1 - Q6) using the equations specified in :ref:`Plumbing Head Loss <plumbing_head_loss>`

#. Find the average head loss of the paths :math:`(\frac{sum(HL)}{6})` (*This average is a theoretical term because the flow distribution will change slightly to make the head loss pretty much even in each path (otherwise flow distribution would be a non-issue) It is expected that each layer will have a head loss close to this average*)

#. Find :math:`\Pi_{layer}`. The ratio of  the flow distribution. The goal is to be close to 1. This term is calulated as the square root of the ratio of the minimum path head loss to the maximum path head loss. :math:`\Pi_{layer}` is a check to ensure all paths provide approximately the same impediment to flow.

In figuring out the flow for each layer from the head losses, some assumptions should be made to turn the manifold system into a system of equations.

Because the flow distribution will change to make the head losses even, it can be taken as true that :math:`HL_{Path1} = HL_{Path2}` and so on for each path, with head loss being a function of the flow. In each path the clean bed head losses are also accounted for, as from the Kozeny equation mentioned previously.

The other necessary constraint is a mass balance:

The flow in all the layers must add up to the flow in the filter. With this information,  a system of equations can be set up to use the head loss and total flow requirement to solve for the flow in each layer. Those flows are then taken as the flow through each layer.

The 6 equations to be solved are:

.. math::

  Q_1 + Q_2 + Q_3 + Q_4 + Q_5 + Q_6 = Q_{Fi}

  HL_{Path1}(Q_1) = HL_{Path2}(Q_2)

  HL_{Path2}(Q_2) = HL_{Path3}(Q_3)

  HL_{Path3}(Q_3) = HL_{Path4}(Q_4)

  HL_{Path4}(Q_4) = HL_{Path5}(Q_5)

  HL_{Path5}(Q_5) = HL_{Path6}(Q_6)

Each of the head losses as a function of Q in the latter 5 of the equations to be solved are fairly simple to solve using any kind of solving program (such as Python!)

Siphon Design and Head Loss
==============================


The siphon in the EStaRS system is different from the OStaRS system because it doesn't involve air to create suction. It acts simply as an exit for water at the top of the filter. This system only works because the entire filter is enclosed, meaning if the head loss out through the siphon pipe is less than going out the other exits, that is the flow path the water will take. Based on this strict definition of the siphon, this system isn't really a siphon to maintain parallel naming to the OStaRS, it is called that.

.. _figure_siphon_schematic:

.. figure:: ../Images/figure_siphon_schematic.png
    :width: 80%
    :align: center
    :alt: siphon schematic for EStaRS systems

    This figure shows the important components to the siphon system in an EStaRS system. The component labelled entrance tank either the filter entrance box (for the Micky Mouse design) or the concrete filter entrance box. In either design the head loss calculations are the same.


It works by simply opening the siphon valve as labelled in :numref:`figure_siphon_schematic`, then the inlet pipes are closed in the entrance tank with pipe stubs starting at the top, eventually leaving only the backwash pipe open. That's it! To end backwash, the process is reversed. Inlets are opened back up one at time, and THEN the valve is closed. Though this process is simple it requires some finesse get right. If all the inlet are closed immediately then the water level in the filter entrance tank will drop too low and air will get in the filter. Air in the filter causes head loss problems and is unwanted. To avoid this the pipe stubs to close the inlets are wiggled around to act as valves so that the water level during backwash is around 10cm above the bottom of the filter entrance tank. :numref:`figure_siphon_schematic` has this value labelled.

It is important to maintain this height because the height of the water level during backwash as compared to the height of the outlet of the siphon pipe controls the backwash flow. If the water level is too low, the sand may not fluidize. If the water level is too high, the sand may over-fluidize and be washed out of the filter.

The pipe size for the siphon is the same as the backwash trunk: :math:`ND_{Siphon} = ND_{BwTrunk}`, this diameter is really a minimum to ensure the siphon pipe doesn’t accumulate too much head loss.

The preliminary estimate of siphon length is twice the length of the filter: :math:`L_{SiphonEst} = 2*L_{FilterBody}`. By making this initial assumption the major losses through this length of the siphon piping can be calculated.

There are assumed to be minor losses in the entrance, exit, and in three elbows.

.. math::

  K_{FiSiphon} = K_{PipeEnt} + 3*K_{Elbow90} + K_{PipeExit}


The maximum head loss for siphon initiation is the sum of head losses of other predetermined quantities including:

:math:`HL_{BWinitiation}` (From head loss section)
:math:`HL_{FiForwardNoSuckAir}` (The height the water level needs to be to stop air from getting into the filter.)
:math:`HL_{FiDirty}`  (as defined in Expert Inputs) (The height water is allowed to rise in the entrance tank before backwash should be started, this varies on the style of filter. See :numref:`table_comparsion_filters` for the different values)
:math:`HL_{BwInletPlumbing}`
:math:`HL_{SiphonMax}` (as defined in expert inputs) (the maximum head loss allowed through the siphon at stea)

with  :math:`H_{SiphonNoSuckAir}` subtracted

These values are calculated or described in the :ref:`Fluidized Bed and Head Loss Variation <fluidized_bed_headloss_variation>` section or defined as Expert Inputs for the system. This value represents the highest the water can be over the siphon exit.

To determine a more appropriate siphon head loss the actual head losses are determined.

The head loss of the siphon pipe is determined by major losses resulting from the backwash flow through the pipe. This pipe is labelled in the schematic.

The outlet system head loss is taken as a head loss from a weir using the backwash flow and inner diameter of the siphon pipe.

The orifice head loss of the siphon (where it connects from the filter body into the siphon pipe) is determined using the orifice equation with the inner diameter, the Vena Contracta coefficient, and the backwash flow as inputs.

From those calculated parameters the steady state backwash head loss can be found as follows:

.. math::

  HL_{FiBwTotalSS} = HL_{BwInletPlumbing} + HL_{BwSS} + HL_{SiphonOrifice} + HL_{FiSiphonPipe} + HL_{SiphonOutlet}


The first term comes from the :ref:`Plumbing Head Loss <plumbing_head_loss>` section the second term comes from the :ref:`Fluidized Bed and Head Loss Variation <fluidized_bed_headloss_variation>` section. The last three were described just above.

This the distance in height that must exist between the siphon outlet and 10 cm above the bottom of the filter entrance box, as shown in the schematic. Because the backwash system works using the difference in elevation getting these values correct is critical.

Additionally, the density of the fluidized sand can be determined.

.. math::

   \rho_{Fluidized} = \rho_{H2O}*\epsilon_{Sand}*\Pi_{Fluidized} + \frac{\rho_{FiSand}*(1-\epsilon_{sand})}{\Pi_{Fluidized}}


Elevations and Filter Sizing
=============================

Backwash Flow Control
===========================

Sand Volume
==============

Determining the sand volume allows for cost estimation and stability assessments of the filter. As sand is only in the main filter body that is the volume of largest concern. Most generally, the amount of sand needed is the volume of sand that would fit into the filter body to the proper height with the volume of the pipe manifold subtracted, because volume containing pipes should not have sand.

The plumbing within the filter body consists of the Backwash Trunk, the other inlet/outlet trunks, and the branches.

Approximating each of these as cylinders and excluding the small volume taken up by pipe caps, this calculation is very straight forward.

The volume of the backwash trunk is: :math:`\frac{\pi}{4}*OD_{BWTrunk}^2*ID_{FiPipe}`

The volume of the rest of the trunks is :math:`\frac{\pi}{4}*OD_{Trunks}^2*ID_{FiPipe}*6`
where 6 is the number of trunks excluding the backwash trunk.

The volume occupied by the branches is :math:`OD_{Branches}^2 *L_{TotalBranches}*7`

Where 7 is the number of layers of branches, and :math:`L_{TotalBranches}` the total lengths of the branches for one filter layer.

Thus the total plumbing volume is:

:math:`\rlap{-} V_{FiPlumbing} = \rlap{-} V_{BWTrunk} + \rlap{-} V_{Trunks} + \rlap{-} V_{Branches}`

Then the total sand volvume in the filter is the volume of the filter (a function of its heigth and area) minus the volume of the plumbing.

:math:`\rlap{-} V_{SandTotal} = (A_{Fi}*H_{FiSandLow}) - \rlap{-} V_{FiPlumbing}`.

Multplying the density of the sand, :math:`\rho_{Sand}` by the volume of the sand gives the mass of the sand, :math:`M_{Sand}`

The mass of one sand bag, :math:`M_{SandBag}` is 50 pounds so the number of sand bags can be determined by: :math:`N_{Fi}*\frac{M_{Sand}}{M_{SandBag}}` (rounded up to a whole number).

As a safety factor, this value is multiplied by 1.25 to get the total number of sand bags:

.. math::

  N_{SandBag} = 1.25(N_{Fi}*\frac{M_{Sand}}{M_{SandBag}})



Materials
=========

For construction and cost estimates the PVC material quantities can be found.

The total length of the largest diameter pipe  for the filter body, :math:`L_{TotalFiPipe}` is equal to the length of one filter times the number of filters: :math:`L_{FilterBody}*N_{Fi}`

The total length of pipe for the entrance and exit tanks is:

:math:`L_{TotalEntExitPipe} = N_{Fi}*(H_{EntranceTank} + H_{ExitTank})`

The total lengths of the branch manifold piping is the sum of the total manifold piping of one layer times 3, for the three inlets which are all the same size (the slotted pipes are ordered separately because they cannot be hand fabricated at this point). This value is multiplied by 1.5 to account the wings that create the gravity exclusion zone around the inlets, wings are half pipes of the same size!  Thus:

.. math::

  L_{TotalBranchManifold} = 1.5*(3*\Sigma L_{FiManBranch})

The lengths of the slotted pipes would be just :math:`3*\Sigma L_{FiManBranch}`, where (in both) :math:`L_{FiManBranch}` is an array of lengths for an entire filter layer

    **note from the writer of this section, at the time of writing is it unclear if the filter manifolds can be constructed with one branch serving both sides of the trunk, this section assumes it can and is being done, so elsewhere in this code the array of branch lengths may just be an array of branches on one side of the trunk! Beware of this as it can cause problems as the lengths will be off by around 2x! If this is resolved in the future all sections will be updated to contain the most correct information**


Lastly, the number of wings to be made is the number or filters times the number of branches (per side) per layer times 4, as there are 4 inlets which require wings!

:math:`N_{Wing}` is equal to :math:`N_{Fi}*2N_{FiBranchLow}*4`.
