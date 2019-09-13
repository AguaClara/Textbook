.. _title_hydraulics_intro:

********************************************
Hydraulics Introduction
********************************************

The hydraulic controls provide the basis for efficient and robust water treatment plant operation. Water must move through unit processes and between unit processes and the flow passages must be designed to meet various constraints. One constraint is that water that is carrying a significant amount of sediment (flocculator and sedimentation tank inlet) must have sufficient velocity and turbulence levels to minimize sedimentation.  A more challenging constraint is that the flow must be divided equally between parallel processes. Flow distribution through parallel paths is a key hydraulic design constraint for all municipal scale water treatment plants. The parallel path constraint only goes away for laboratory scale processes where there is a single tube settler and a filter with a single layer of sand.

Municipal water treatment plants

.. _figure_circuit:

.. figure:: Images/circuit.png
    :width: 400px
    :align: center
    :alt: Sedimentation tank flow circuit

    The flow through a sedimentation tank is analogous to an electrical circuit with wires and resistors. Identical resistors in parallel paths help improve flow distribution between the paths. Differences in piezometric head (think voltage) in the manifolds that connect to multiple parallel paths.




.. _OStaRS_Design:

Open Stacked Rapid Sand Filter Design
=====================================

Design steps
------------

1.  Calculate array of maximum filter flows given available trunk sizes and given constraint of flow distribution between filter layers during filtration
1.  Calculate the orifice head loss required for each
1.  Calculate filter flow given minimum number of filters
1.  Find the available maximum filter flow that is equal or greater than the filter flow required given the minimum number of filters
1.  Find the corresponding Trunk size.
1.  Design the branches based on manifold flow distribution requirements
1.  Design the siphon pipe given a reasonable (help!!) constraint on drain time
1.  Design the siphon air valve given volume of air in the siphon
1.  Calculate all elevations
1.  Design backwash flow control weir

Design assumptions
------------------

* Simplest design to fabricate will have identical trunk lines for all inlets
*

Maximum Trunk Flows
-------------------

The trunks are constrained to both provide similar flow to each filter layer and to provide similar flow to each branch within the sand bed. Providing the same flow to each filter layer during filtration is the key constraint that determines the size of the trunk lines. The most challenging flow distribution is between middle inlets that carry flow for two layers and the top and bottom inlets that carry flow for one sand layer.

.. _figure_Trunk_flows:

.. figure:: Images/Trunk_flows.png
    :width: 400px
    :align: center
    :alt: Trunk flows

    The flows through the inlet trunks of stacked rapid sand filters are not identical and this requires a careful hydraulic design.


The flow distribution within the filter bed to ensure complete fluidization of the sand bed during backwash can be achieved by increasing the head loss through the flow control orifices in the branches. Calculating this required head loss is the second step in designing the filter inlet piping.

The factor of two difference in design flow rates for outer and inner inlet trunks requires that the head loss through the trunks be small relative to the head loss through the orifices and sand bed.  The orifices contribute very little to the flow distribution because the orifices also have to deliver the backwash flow which is 6 times the filtration flow for the bottom inlet. That means that the orifice head loss during filtration is 1/36th of the head loss during backwash.

The solution path for design of the requires setting a constraint on how far the flows can diverge from the target, setting the head loss through the two paths from the inlet box through the sand to be equal, and ensuring that mass is conserved. With these constraints it is possible to solve for the maximum head loss in the trunks and then calculate the required trunk diameter to meet the head loss constraint.

Nomenclature
------------

.. _table_Trunk_Nomenclature:

.. csv-table:: Nomenclature for filter trunk design.
   :header: "Symbol", "Units", "Description"
   :align: left

   ":math:`\Pi_Q`", "dimensionless", "ratio of minimum layer flow to maximum layer flow"
   ":math:`Q_{IT_i}`",":math:`\frac{L}{s}`", "actual flow in **I**nlet **T**runk i"
   ":math:`Q_{L_i}`",":math:`\frac{L}{s}`", "actual flow in filter **L**ayer i"
   ":math:`\overset{u}{Q}_L`",":math:`\frac{L}{s}`", "ideal uniform flow in each filter layer"



.. math::
   :label: Flow_ratio

    \Pi_Q = \frac{0.5Q_{T_3}}{Q_{T_4}} = \frac{Q_{L_{4,5}}}{Q_{L_6}}

Where :math:`\Pi_Q` is slightly less than 1 and represents the extent of uniform flow distribution. Flows :math:`Q_3` and :math:`Q_4` represent the actual flow through the two trunk lines, not the ideal flows. We need to specify the flow distribution error that we are willing to accept. My initial guess is that a value of about 0.85 would be reasonable. This means that the bottom layer of the filter and the top layer of the filter will receive more flow. That will result in them filling with particles faster which will cause a slight improvement in flow distribution between the layers.

The relationship between :math:`Q_3`, :math:`Q_4`, and the target value of :math:`\overset{u}{Q}_{layer}` can be obtained because 50% of the filter flow goes through the bottom two inlets. The "u" indicates the ideal "uniform" flow. Thus we have:

.. math::
   :label: Flow_ratio

     3 \overset{u}{Q}_{layer} = Q_3 + Q_4

.. math::
   :label: Flow_Trunk_3

     3 \overset{u}{Q}_{layer} = (2\Pi_Q +1) Q_4

.. math::
   :label: Head_loss_Path_6

     h_{L} = h_{L_{sand}} + h_{L_{T}} + h_{L_{Orifices}}
