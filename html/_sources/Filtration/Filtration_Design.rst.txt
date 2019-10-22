.. _title_Filtration_Design:


*******************
Filtration Design
*******************


1.  Calculate array of maximum filter flows given available trunk sizes and given constraint of flow distribution between filter layers during filtration
1.  Select the trunk size that gives a number of filters equal to or less than the minimum number of filters required for operation and maintenance.
1.  Calculate filter flow given minimum number of filters
1.  Calculate the orifice head loss required to provide uniform flow to the sand bed during backwash.
1.  Design the branches based on manifold flow distribution requirements
1.  Design the siphon pipe given a reasonable (help!!) constraint on drain time
1.  Design the siphon air valve given volume of air in the siphon
1.  Calculate all elevations
1.  Design backwash flow control weir



Potential Changes to the Filter Design
======================================

* Have the siphon manifold exit straight through the side of the filter (perhaps in line with the other inlets and outlets) and then elbow up to the required elevation and elbow and Tee back down again. This would make the siphon install inside the filter be a single straight pipe instead of the large assembly that is currently used. This will have the additional advantage that the connection between this drain manifold and the pipe stub in the wall doesn't have to be leak tight! The connection could be a wrap of stainless steel and two hose clamps.
* Switch to gravity exclusion zones that include orifices to get uniform flow distribution without risk of sand scour.
* Simplest design to fabricate will have identical trunk lines for all inlets
* Change the inlet and outlet boxes so that all of the inlet trunks have only one elbow
* Outlet trunks each have 2 elbows


Maximum Trunk Flows
===================

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
============

.. _table_Trunk_Nomenclature:

.. csv-table:: Nomenclature for filter trunk design.
   :header: "Symbol", "Units", "Description"
   :align: left

   ":math:`\Pi_Q`", "dimensionless", "ratio of minimum layer flow to maximum layer flow"
   ":math:`Q_{IT_i}`",":math:`\frac{L}{s}`", "actual flow in Inlet Trunk i"
   ":math:`Q_{L_i}`",":math:`\frac{L}{s}`", "actual flow in filter Layer i"
   ":math:`\overset{u}{Q}_L`",":math:`\frac{L}{s}`", "ideal uniform flow in each filter layer"
   ":math:`h_{L_i}`",":math:`m`", "head loss from inlet tank all the way through the sand in layer i"



.. math::
   :label: Flow_ratio

    \Pi_Q = \frac{0.5Q_{IT_3}}{Q_{IT_4}} = \frac{Q_{L_{4,5}}}{Q_{L_6}}

Where :math:`\Pi_Q` is slightly less than 1 and represents the extent of uniform flow distribution. Flows :math:`Q_{IT_3}` and :math:`Q_{IT_4}` represent the actual flow through the two inlet trunk lines, not the ideal flows. We need to specify the flow distribution error that we are willing to accept. A value of about 0.85 would be reasonable and experiments to measure the effect of poor flow distribution on filter performance are needed. Non uniform flow distribution means that the bottom layer of the filter and the top layer of the filter will receive more flow. That will result in them filling with particles faster which will cause a slight improvement in flow distribution between the layers.

The unknown actual flow rates can be eliminated from subsequent equations for head loss by replacing them with the known target flow through a layer of sand. The next equations develop these relationships.

The relationship between :math:`Q_{IT_3}` and :math:`Q_{IT_4}` and the target value of :math:`\overset{u}{Q}_L` can be obtained because 50% of the filter flow goes through the bottom two inlets and thus we can use a mass balance around the bottom half of the filter. Thus we have:

.. math::
   :label: Flow_layer_uniform

     3 \overset{u}{Q}_L = Q_{IT_3} + Q_{IT_4}

Eliminate :math:`Q_{IT_3}` from equation :eq:`Flow_layer_uniform` by substituting equation :eq:`Flow_ratio` and solve for :math:`Q_{IT_4}`.

.. math::
   :label: Flow_Trunk_4

     \frac{Q_{IT_4}}{\overset{u}{Q}_L} = \frac{3}{2\Pi_Q +1}


.. math::
   :label: Flow_Trunk_3

    \frac{Q_{IT_3}}{\overset{u}{Q}_L} = \frac{6\Pi_Q}{2\Pi_Q +1}

The actual flows through the filter layers can also be expressed as a function of the ideal uniform flow through a filter layer and the flow ratio. The flow of water through the bottom layer (layer 6) of sand is equal to the flow of water through trunk 4.

.. math::
   :label: Flow_Layer_6

    \frac{Q_{L_6}}{\overset{u}{Q}_L} = \frac{Q_{IT_4}}{\overset{u}{Q}_L} = \frac{3}{2\Pi_Q +1}


The flow through layers 4 and 5 are identical and from equation :eq:`Flow_ratio` they are equal to :math:`\Pi_Q` times the flow in layer 6, :math:`Q_{L_6}`.

.. math::
   :label: Flow_Layer_45

    \frac{Q_{L_{4,5}}}{\overset{u}{Q}_L} = \frac{\Pi_Q Q_{IT_4}}{\overset{u}{Q}_L} = \frac{3\Pi_Q}{2\Pi_Q +1}

The next step is to write the equations for the total head loss from the inlet tank to where the water exits the sand layers and enters the outlet system beginning with inlet trunk 4. This path is designated as path 6 because it goes through sand layer 6.

.. math::
   :label: Head_loss_Layer_6

     h_{L_6} = h_{L_{IT_4}} + h_{L_{Orifices_4}} + h_{L_{Sand_6}}

The head loss in the trunk and through the orifices is directly proportional to the square of the flow rate. The head loss through the sand is directly proportional to the flow rate. Thus we can write the equation in terms of the head losses that would be observed under uniform flow conditions.

.. math::
   :label: Head_loss_Layer_6uintermediate

     h_{L_6} = \left(\overset{u}{h}_{L_{IT_4}} + \overset{u}{h}_{L_{Orifices}}\right)\left(\frac{Q_{L_6}}{\overset{u}{Q}_L}\right)^2 + \overset{u}{h}_{L_{Sand}}\left(\frac{Q_{L_6}}{\overset{u}{Q}_L}\right)

The head loss through the orifices under ideal flow conditions is identical for all layers and thus there is no subscript on the orifice flow. The same is true for the head loss through each sand layer.
Now eliminate the unknown flow through layer 6, :math:`Q_{L_6}`, by substituting equations :eq:`Flow_Layer_6`.

.. math::
   :label: Head_loss_Layer_6u

     h_{L_6} = \left(\overset{u}{h}_{L_{IT_4}} + \overset{u}{h}_{L_{Orifices}}\right)\left( \frac{3}{2\Pi_Q +1}\right)^2 + \overset{u}{h}_{L_{Sand}}\left( \frac{3}{2\Pi_Q +1}\right)

Repeat the equation development for paths through sand layers 4 and 5 that begin by flowing in trunk 3.

.. math::
   :label: Head_loss_Layer_45

     h_{L_{4,5}} = h_{L_{IT_3}} + h_{L_{Orifices_3}} + h_{L_{Sand_{4,5}}}

Write the head loss equation :eq:`Head_loss_Layer_45` in terms of the flow through sand layers 4 and 5 (equation :eq:`Flow_Layer_45`)

.. math::
   :label: Head_loss_Layer_45uintermediate

     h_{L_{4,5}} = \left(\overset{u}{h}_{L_{IT_3}} + \overset{u}{h}_{L_{Orifices}}\right)\left(\frac{Q_{L_{4,5}}}{\overset{u}{Q}_L}\right)^2 + \overset{u}{h}_{L_{Sand_{4,5}}}\left(\frac{Q_{L_{4,5}}}{\overset{u}{Q}_L}\right)

Substitute the flow ratios through sand layers 4 and 5 from equation :eq:`Flow_Layer_45`.

.. math::
   :label: Head_loss_Layer_45u

     h_{L_{4,5}} = \left(\overset{u}{h}_{L_{IT_3}} + \overset{u}{h}_{L_{Orifices}}\right)\left(\frac{3\Pi_Q}{2\Pi_Q +1}\right)^2 + \overset{u}{h}_{L_{Sand}}\left(\frac{3\Pi_Q}{2\Pi_Q +1}\right)

Now we recognize that the flow through trunk 3 is double the flow through trunk 4 and the head loss scales with the square of the flow. Given that these trunks are now all the same size we know that

.. math::
   :label: Head_loss_IT4_and_IT3

     \overset{u}{h}_{L_{T_3}} = 4\overset{u}{h}_{L_{T_4}}

We can substitute equation :eq:`Head_loss_IT4_and_IT3` to eliminate :math:`\overset{u}{h}_{L_{T_3}}` from equation :eq:`Head_loss_Layer_45u`. The head loss into the filter and through the sand layers must be identical regardless of which path is taken because the outlet systems are identical. Set equation :eq:`Head_loss_Layer_6u` equal to equation :eq:`Head_loss_Layer_45u` to solve for the maximum allowable head loss in trunk 4 during filtration.


.. math::
   :label: Head_loss_Inlet_Trunks_equal

    \left(4\overset{u}{h}_{L_{T_4}} + \overset{u}{h}_{L_{Orifices}}\right)\left(\frac{3\Pi_Q}{2\Pi_Q +1}\right)^2 + \overset{u}{h}_{L_{Sand}}\left(\frac{3\Pi_Q}{2\Pi_Q +1}\right) = \left(\overset{u}{h}_{L_{IT_4}} + \overset{u}{h}_{L_{Orifices}}\right)\left( \frac{3}{2\Pi_Q +1}\right)^2 + \overset{u}{h}_{L_{Sand}}\left( \frac{3}{2\Pi_Q +1}\right)

Simplify and solve for :math:`\overset{u}{h}_{L_{T_4}}`.

.. math::
   :label: Head_loss_Inlet_Trunks_equal_simplified1

    \left(4\overset{u}{h}_{L_{T_4}}\Pi_Q^2 + \overset{u}{h}_{L_{Orifices}}\Pi_Q^2\right)\left(\frac{3}{2\Pi_Q +1}\right)^2 + \overset{u}{h}_{L_{Sand}}\Pi_Q\left(\frac{3}{2\Pi_Q +1}\right) = \left(\overset{u}{h}_{L_{IT_4}} + \overset{u}{h}_{L_{Orifices}}\right)\left( \frac{3}{2\Pi_Q +1}\right)^2 + \overset{u}{h}_{L_{Sand}}\left( \frac{3}{2\Pi_Q +1}\right)

Divide by :math:`\frac{3}{2\Pi_Q +1}`.

.. math::
   :label: Head_loss_Inlet_Trunks_equal_simplified2

    \overset{u}{h}_{L_{T_4}}\left(4\Pi_Q^2 - 1\right)\left(\frac{3}{2\Pi_Q +1}\right) = \overset{u}{h}_{L_{Orifices}}\left(1-\Pi_Q^2\right)\left( \frac{3}{2\Pi_Q +1}\right) +\overset{u}{h}_{L_{Sand}}(1-\Pi_Q)

.. math::
    :label: Head_loss_Inlet_Trunks_equal_simplified3

     \overset{u}{h}_{L_{T_4}} =   \frac{ \overset{u} {h}_{L_{sand}}\left( \frac{2\Pi_Q +1}{3}  \right) \left(1 - \Pi_Q\right)   + \overset{u} {h}_{L_{Orifices}}\left(1- \Pi_Q^2 \right)}{4\Pi_Q^2 -1}

The head loss through the orifices during filtration flow is small relative to the head loss through the sand because the orifice head loss during filtration flow must be 1/36th the head loss during backwash. Thus we can simplify :eq:`Head_loss_Inlet_Trunks_equal_simplified3` to obtain.

.. math::
    :label: Head_loss_Inlet_Trunks_equal_simplified4

     \overset{u}{h}_{L_{T_4}} =  \overset{u} {h}_{L_{sand}}  \frac{\left( \frac{2\Pi_Q +1}{3}  \right) \left(1 - \Pi_Q\right)}{4\Pi_Q^2 -1}


A plot of equation :eq:`Head_loss_Inlet_Trunks_equal_simplified4` is shown in

.. _figure_Ratio_HL_Trunk4_HL_sand:

.. figure:: Images/Ratio_HL_Trunk4_HL_sand.png
    :width: 400px
    :align: center
    :alt: Ratio HL Trunk4 HL sand

    The allowable head loss in trunk 4 during filtration is a small fraction of the head loss through the sand. This constraint sets the minimum allowable trunk diameter for the filters given a target flow distribution between sand layers.

Given the constraint on head loss through trunk 4 (equation :eq:`Head_loss_Inlet_Trunks_equal_simplified4`) the maximum flow rate for each available trunk diameter can be obtained using the `python function for the pipe diameter given a flow and a head loss <https://aguaclara.github.io/aguaclara/core/physchem.html#aguaclara.core.physchem.diam_pipe>`_. The array of pipes
