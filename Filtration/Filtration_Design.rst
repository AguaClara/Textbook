.. _title_Filtration_Design:


********************************
Stacked Rapid Sand Filter Design
********************************

Nomenclature
============

B - branch

P - port (or orifice)

T - trunk


Introduction
============

The hydraulic design of both the enclosed and open stacked rapid sand filter is complicated by the number of parallel flows, the manifolds in series, and the need to handle both backwash and filter modes. The design requires careful attention to weir hydraulics to achieve the target backwash flows when the plant is operating at less than full capacity. The siphon system has a tight design constraint to ensure that the siphon doesn't trigger prematurely.

There are two possible constraints on the trunk size. Either the trunk size is dictated by backwash flow distribution requirements or the trunk size is dictated by the need to have uniform flow distribution between filter layers and hence to have exactly twice the flow rate through the inner inlets.

There are 4 levels of flow distribution in StaRS filters. The direction of the design (top-down or bottom-up) is determined by the fact that when there is head loss in series that all of the head loss helps to achieve flow distribution. Thus the head loss through the orifices will be a required part of the design of the branches and that head loss will be an input for the trunk design. Thus we need to start at the bottom and work up.

 * between orifices (branchPortQ_pi): made less important by the winged design that allows correcting flow in the winged space before the water enters the sand bed. This flow distribution does not benefit from the head loss through the sand. Suggest using a value of 0.8 for this constraint because of the balancing provided by the wings. The flow distribution constraint only provides a ratio of the port and branch velocities. The constraint for the maximum velocity allowable is either set by head loss or by the strength of the branch to span its length and not bend to much at the initiation of backwash. Either of those constraints can be converted into a maximum velocity for the inner branches and that will be used as an input to the design.

  * The velocity constraint will determine the maximum length of a branch given its diameter.
  * Use equation :eq:`manifold_max_v_no_hl_series` combined with the maximum branch velocity constraint to calculate the port velocity. Calculate the required branch diameter given the length (or vice versa).
  * The orifice diameter will be selected based on constructability and not being too small to risk clogging (between 4 and 10 mm)
  * Calculate the orifice spacing for the inner branches based on mass conservation and the maximum port velocity.
  *  Calculate the maximum length of the branches given mass conservation and the maximum branch velocity.

 * between branches (trunkPortQ_pi): aided considerably by the head loss through the sand and is helped by the head loss though the orifices. Suggest using a value of 0.9 for this constraint. This constraint will be combined with a maximum permissible head loss during backwash to determine the required diameter of the trunk lines and will be combined with the equal trunk head loss constraint to obtain the diameter of the orifices.

  * Use equation :eq:`manifold_max_v_with_hl_series` to solve for the maximum trunk velocity.
  * Use the fact that the head loss is the same for outer and inner inlets to determine the :math:`K_{e_{outerOrifices}}`.

 * between sand layers: easily obtained by simply requiring that inlet head losses be identical in the 4 inlets under conditions of the target flow and accounting for the fact that the inner inlets have double the flow of the outer inlets.
 * between filters: will be handled by design of the weirs into the filter inlet boxes

The clean bed sand head loss and including the head loss right at the point where the water enters the sand helps with the flow distribution between branches and between orifices. We are not currently including the benefit of the high velocity at the point where the water enters the sand.

Design Steps
============


Inner Trunk
-----------

The diameter of the trunk lines is set by the filtration flow distribution between ports in the inner trunks and the maximum acceptable inlet head loss during backwash. The backwash head loss constraint is directly connected to the head loss during filtration because the velocity in the backwash trunk changes by a factor of the number of filter layers. The backwash inlet head loss sets the required depth of the open filter box and so is an important constraint for O-StaRS. Both the inner and outer inlet head loss during filtration is :math:`\frac{1}{N_{layers}^2}` times the backwash inlet head loss because the head loss is proportional to the flow ratio squared and because we will set the inlet head losses to be identical during filtration.

The equation for flow distribution between branches with additional head loss in series is :eq:`Manifold_max_v_with_hl_series`.

.. math::
  :label: Trunk_to_branch_flow_distribution

   \frac{\bar v_{T_{innerMax}}^2}{2g}=  \left(h_{e_{B_{inner}}} + h_{e_{P_{inner}}} + h_{l_{sand}} \right)\Pi_{\Psi_B}


The head loss through the inner ports or orifices required to achieve reasonable flow distribution into the winged area of the inlet branches can be expressed in the minor loss equation form. The flow distribution constraint is given by equation :eq:`Manifold_max_v_no_hl_series`.

.. math::
  :label: eq_he_port

  h_{e_{P_{inner}}} = \frac{\bar v_{P_{inner}}^2}{2g} = \frac{\bar v_{B_{inner}}^2}{2g}\frac{1}{\Pi_{\Psi_P}

where the port velocity :math:`\bar v_{P_{inner}}` is the *contracted* velocity out of the orifice.

The branch entrance loss is given by

.. math::
  :label: he_branch

  h_{e_{B_{inner}}} = K_{e_B}\frac{\bar v_{B_{innerMax}}^2}{2g}

The minor loss associated with entering the branch is given by equation :eq:`he_branch`). The :math:`h_{l_{series}}` is the sum of the orifice head loss (see equation :eq:`eq_he_port`) and the head loss through the sand. Making those substitutions into equation :eq:`Trunk_to_branch_flow_distribution` we obtain

.. math::
  :label: Trunk_max_v_flow_distribution

   \bar v_{T_{innerMax}}^2 =  \Pi_{\Psi_B}\left[\bar v_{B_{innerMax}}^2\left(K_{e_B} + \frac{1}{\Pi_{\Psi_P}}\right) + 2gh_{l_{sand}} \right]

This is a constraint on the maximum branch velocity assuming that the port velocity is set to achieve flow distribution to the wings within a branch (rather than setting the port velocity to achieve flow distribution between branches).

This shows that the trunk velocity is limited by the branch velocity even without applying the head loss constraint. However, even if the branch velocity approaches zero, the trunk velocity can still be quite high because of the balancing effect of the sand head loss. This constraint ends up not being useful because flow division between branches is not a critical constraint.

The head loss constraint is

.. math::
  :label:

  h_{e_{outerInlet_{Bw}}} = N_{layer}^2 h_{e_{innerInlet}} = N_{layer}^2 \left(h_{e_{T_{inner}}} + h_{e_{B_{inner}}} + h_{e_{P_{inner}}} \right)


The trunk entrance and elbow losses are given by

.. math::
  :label: he_T_inner

  h_{e_{T_{inner}}} = K_{e_T}\frac{\bar v_{T_{innerMax}}^2}{2g}

Substitute with minor loss relationships.

.. math::
  :label: he_T_inner_of_V

  2gh_{e_{outerInlet_{Bw}}} = N_{layer}^2 \left(K_{e_T}\bar v_{T_{innerMax}}^2 + K_{e_B}\bar v_{B_{innerMax}}^2 + \bar v_{B_{innerMax}}^2\frac{1}{\Pi_{\Psi_P}} \right)

Solve for :math:`\bar v_{T_{innerMax}}`.

.. math::
  :label: V_trunk_of_he

  \bar v_{T_{innerMax}} = \sqrt{\frac{2gh_{e_{outerInlet_{Bw}}}}{K_{e_T} N_{layer}^2} -\frac{\bar v_{B_{innerMax}}^2}{K_{e_T}}\left(K_{e_B} + \frac{1}{\Pi_{\Psi_P}} \right)}

The head loss constraint reveals that we can achieve the highest trunk velocity by setting the branch velocity to zero! This is because the branch head loss is not needed to achieve flow distribution between branches. Thus we will design the branches to have low velocities to increase the flow that can be achieved with a given size trunk. First define a dimensionless ratio of branch to trunk kinetic energy that will be used as a user specified constraint to allow the exploration of the tradeoff.

.. math::
  :label: Branch_Trunk_Pi

  \bar v_{B_{innerMax}}^2 = \Pi_{BT} \bar v_{T_{innerMax}}^2

Use equation :eq:`Branch_Trunk_Pi` to eliminate :math:`\bar v_{B_{innerMax}}` in equation :eq:`he_T_inner_of_V`.

.. math::
  :label: he_T_inner_of_V

  2gh_{e_{outerInlet_{Bw}}} = N_{layer}^2 \left(K_{e_T}\bar v_{T_{innerMax}}^2 + K_{e_B}\Pi_{BT} \bar v_{T_{innerMax}}^2 + \Pi_{BT} \bar v_{T_{innerMax}}^2\frac{1}{\Pi_{\Psi_P}} \right)

solve for :math:`\bar v_{T_{innerMax}}`.

.. math::
  :label: V_trunk_of_HE_BW

  \bar v_{T_{innerMax}} = \sqrt{\frac{2gh_{e_{outerInlet_{Bw}}}}{N_{layer}^2 \left[K_{e_T} + \Pi_{BT}\left(K_{e_B} + \frac{1}{\Pi_{\Psi_P}} \right)\right]}}

Inner branch
------------

Use equation :eq:`Branch_Trunk_Pi` to solve for the maximum branch velocity given the results from equation :eq:`V_trunk_of_HE_BW`.

Given the constraint of maximum branch velocity use the relationship between port velocity and branch velocity given by equation :eq:`Manifold_max_v_no_hl_series` to solve for the port velocity.

.. math::
  :label: v_port_inner_branch

  \bar v_{P_{innerMax}} = \bar v_{B_{innerMax}}\sqrt{\frac{1}{\Pi_{\Psi_P}}

The orifice diameter will be constrained by the wing fabrication. Apply conservation of mass to obtain the port velocity to filter velocity ratio. Each port serves an area equal to the branch spacing times the port spacing.

.. math::
  :label: v_port_inner_to_v_Fi

  \frac{\bar v_{P_{innerMax}}}{2 v_{Fi}} = \frac{B_{branch} B_{orifice_{inner}}}{\Pi_{vc}\frac{\pi}{4} D_{orifice}^2}

where the factor of 2 is because the inner trunks serve two layers of sand. Combine equations :eq:`v_port_inner_branch` and :eq:`v_port_inner_to_v_Fi` and solve for the center to center spacing of the orifices.

.. math::
  :label: B_orifice_inner

  B_{orifice_{inner}} = \frac{\bar v_{B_{innerMax}}\Pi_{vc}\pi D_{orifice}^2}{8 v_{Fi}B_{branch}}\sqrt{\frac{1}{\Pi_{\Psi_P}}

We will assume that the user sets the target branch diameter as an input. The maximum length of a branch is set by mass conservation and the flow required to serve the filter area corresponding to the length of the branch.

.. math::
  :label: L_branch_max_conserveQ

  2 v_{Fi} L_{branch_{max}} B_{branch} = \bar v_{B_{innerMax}} A_{pipe}

Solve for :math:`L_{branch_{max}}`.

.. math::
  :label: L_branch_max

   L_{branch_{max}} = \frac{\bar v_{B_{innerMax}} A_{pipe}}{2 v_{Fi}  B_{branch}}

Solve for the minimum pipe ID.

.. math::
  :label: D_branch_min

 D_{branch_{min}}= \sqrt\frac{8 v_{Fi}  B_{branch} L_{branch}}{\pi \bar v_{B_{innerMax}}}



At this stage in the design process we have set the flow rate through the filter, the trunk and branch diameters (except for the backwash branches), the length of the branches, and the orifice spacing on the inner inlets.

Outer branch
------------

The outer trunk branch orifices must be designed so that the head loss during filtration is identical between inner and outer inlets. This will result spacing between the outer branch orifices that is more than double that of the inner branch orifices. The derivation is similar to that used to obtain equation :eq:`B_orifice_inner`. Equate the head loss in the inner and outer inlets during filtration. We will use the maximum velocity in the inner trunks as our reference velocity. Note that the results would be the same if we used the actual velocity in the inner trunks because the velocity will drop out of the equation in the end. First the head loss from the inlet box to the orifices in the inner inlets is given by

.. math::
  :label: he_T_inner_of_V_draft

  2gh_{e_{innerInlet}} = \left(K_{e_T}\bar v_{T_{inner}}^2 + K_{e_B}\bar v_{B_{inner}}^2 + \bar v_{B_{inner}}^2\frac{1}{\Pi_{\Psi_P}} \right)

Substitute equation :eq:`Branch_Trunk_Pi` to eliminate :math:`\bar v_{B_{inner}}`.

.. math::
  :label: he_T_inner_of_V

  2gh_{e_{innerInlet}} = \left[K_{e_T} + \Pi_{BT}\left( K_{e_B}  + \frac{1}{\Pi_{\Psi_P}}\right) \right]\bar v_{T_{inner}}^2

The orifices for the outer inlets are not constrained by the flow distribution to the ports. Thus the factor :math:`\frac{1}{\Pi_{\Psi_P}}` does not apply. The unknown that we are solving for is port velocity which we will obtain from the ratio between port and branch kinetic energy.

.. math::
  :label: Port_Branch_Pi

  \bar v_{P_{outer}}^2 = \Pi_{PB_{outer}} \bar v_{B_{outer}}^2


The head loss in the outer inlet is given by

.. math::
  :label: he_T_outer_of_V

  2gh_{e_{outerInlet}} = \left(K_{e_T} + K_{e_B}\Pi_{BT}  + \Pi_{BT} \Pi_{PB_{outer}} \right)\frac{1}{4}\bar v_{T_{inner}}^2

where the factor of 4 difference is because the velocity in the outer inlets is half the inner inlets because each inner inlet serves 2 filter layers. Now set the inner and outer head loss to be equal.

.. math::
  :label: he_inner_equal_he_outer

  \left(K_{e_T} + K_{e_B}\Pi_{BT}  + \Pi_{BT} \Pi_{PB_{outer}} \right)\frac{1}{4}\bar v_{T_{inner}}^2 = \left(K_{e_T} + K_{e_B}\Pi_{BT}  + \Pi_{BT} \frac{1}{\Pi_{\Psi_P}} \right)\bar v_{T_{inner}}^2

Simplify and solve for the unknown, :math:`\Pi_{PB}`.

.. math::
  :label: Pi_PB_outer

  \Pi_{PB_{outer}}= \left(3\frac{K_{e_T}}{\Pi_{BT}} + 3K_{e_B}  + 4\frac{1}{\Pi_{\Psi_P}} \right)

Apply conservation of mass to obtain the port velocity to filter velocity ratio. Each port serves an area equal to the branch spacing times the port spacing.

.. math::
  :label: v_port_outer_to_v_Fi

  \frac{\bar v_{P_{outer}}}{v_{Fi}} = \frac{B_{branch} B_{orifice_{outer}}}{\Pi_{vc}\frac{\pi}{4} D_{orifice}^2}

We need an equation for :math:`\bar v_{P_{outer}}` as a function of :math:`\bar v_{T_{inner}}`.

.. math::
  :label:

  \frac{1}{4} \bar v_{T_{innerMax}}^2 = \bar v_{T_{outerMax}}^2

.. math::
  :label:

  \bar v_{B_{outerMax}}^2 = \Pi_{BT} \bar v_{T_{outerMax}}^2

.. math::
  :label:

  \bar v_{P_{outerMax}}^2 = \Pi_{PB_{outer}} \bar v_{B_{outerMax}}^2

Combine the previous 3 equations to obtain

.. math::
  :label: v_P_outer_of_v_T_inner

  \bar v_{P_{outerMax}} = \frac{\bar v_{T_{innerMax}}}{2} \sqrt{\Pi_{PB_{outer}}  \Pi_{BT}}

The orifice spacing should be designed based on the maximum inner trunk velocity rather than the actual inner trunk velocity so that the branches have the same design for all filters. Otherwise the orifice spacing would be different for every design and that would only make fabrication needlessly confusing.

Substitute equation :eq:`v_P_outer_of_v_T_inner` into equation :eq:`v_port_outer_to_v_Fi` and solve for :math:`B_{orifice_{outer}}`.

.. math::
  :label: B_orifice_outer

  B_{orifice_{outer}} = \frac{\bar v_{T_{innerMax}} \Pi_{vc} \pi D_{orifice}^2 \sqrt{\Pi_{PB_{outer}}  \Pi_{BT}} }{8 v_{Fi} B_{branch}}

The backwash branches have an additional constraint. Those branches have two additional challenges. First, during backwash the sand doesn't provide head loss to help equalize flow. Second, the velocity is :math:`N_{layer}` faster than during filtration. We will ensure that the flow is reasonably distributed by applying the flow distribution requirement without any additional head loss in series. We will use the orifice spacing that is used for the outer inlets.


Uncouple backwash and filtration head losses
============================================

The flow rate through the filter is severely limited if we keep the constraint that the head loss in the backwash inlet and in the inner inlets be the same. We can uncouple the head loss during the two states by having a removable orifice that can be added to the backwash inlet pipe during filtration.

Design inputs discussion
------------------------

We could start with a filter width (required by the control system) or a structural constraint given a nominal diameter of the branches. If we start with these two constraints, overall filter width and ND of the branches the branch velocity can be calculated from mass conservation. The complication is that the trunks create an inactive zone in the filter whose width will be a function of the diameter of the trunk and an iterative solution may be required.

A design goal might be to use identical branches for filters of different sizes. That would require setting the branch length as an input rather than the filter width. This might be reasonable and in any case the maximum branch length is a function of the branch ND.

Design steps:

 * find the maximum velocity in the outlet branches to get flow distribution through the slots using the filter clean bed head loss. assume branch length and branch ND (or an array of paired options)
 * calculate branch velocity from mass conservation
 * calculate max trunk velocity using equation :eq:`V_trunk_of_he`
 * size the trunk, then calculate number of filters, flow per filter, filter width, filter length



What are the failure modes as we increase the velocity in the trunk?

  * port velocities may have to increase if the sand head loss isn't sufficient to ensure flow distribution between branches. Higher port velocities could erode the sand under the wing.
  * increased inlet head loss requires a deeper filter and deeper inlet and outlet control boxes. It would seem reasonable to limit this head loss to something less than 20 cm given that the dirty bed head loss for the filter is approximately 80 cm.
  * outlet branches have a maximum velocity to achieve flow distribution through the slots.

Outlet branch
-------------
The velocity in the outlet branches must be limited to prevent the change in piezometric head in the branch from causing significant differences in the velocity through the slots. The head loss through the filter bed helps keep this flow uniform. We could increase the head loss through the slots to make this flow more uniform, but that is a big failure mode because it is already too easy for these slots to clog over time and thus that problem would be made even worse. Instead we should be designing the outlet branches to have as much slot area as is structurally possible.

Flow distribution through the slots is described by equation :eq:`Manifold_max_v_with_hl_series`. We will neglect the head loss through the slots because if done well it will be small compared with the head loss through the sand. We can check this assumption later!

The maximum outlet branch velocity is

.. math::
  :label: outlet_branch_V_max

   \bar v_{B_{outletMax}}= \sqrt{2gh_{l_{sand}}\Pi_{\Psi}}

This velocity is approximately 0.6 m/s and may be high enough so that it may not be a constraint. It isn't necessary that the flow distribution be extremely uniform given that as the sand bed head loss increases the flow distribution will improve. It will be included in the design code to ensure that we don't miss this constraint.

Inlet branch
-------------
Use mass conservation to determine the velocity in the branch given the branch length, ID, spacing and the filter velocity. The following equation could be corrected for the dead end length. The entire OD of the trunk should be counted as inactive.

.. math::
  :label: branch_V

  v_{B} = \frac{8 v_{Fi} B_{B} L_{B}}{\pi D_{B}^2}

The orifice diameter will be constrained by the wing fabrication. Apply conservation of mass to obtain the port velocity to velocity ratio. Each port serves an area equal to the branch spacing times the port spacing.

.. math::
  :label: v_P_to_v_Fi

  \frac{\bar v_{P}}{N_{sided} v_{Fi}} = \frac{B_{B} B_{P}}{\Pi_{vc}\frac{\pi}{4} D_{P}^2}

where :math:`N_{sided}` is 2 for inner trunks that serve two layers of sand. Combine equations :eq:`v_port_inner_branch` and :eq:`v_port_inner_to_v_Fi` and solve for the center to center spacing of the ports.

.. math::
  :label: B_orifice_inner

  B_{P_{inner}} = \frac{\bar v_{B}\Pi_{vc}\pi D_{P}^2}{8 v_{Fi}B_{B}}\sqrt{\frac{1}{\Pi_{\Psi_P}}

Trunk diameter
--------------

The head loss for the inner inlets is

.. math::
  :label:

  h_{e_{innerInlet}} = \left(h_{e_{T_{inner}}} + h_{e_{B_{inner}}} + h_{e_{P_{inner}}} \right)


The trunk entrance and elbow losses are given by

.. math::
  :label: he_T_inner

  h_{e_{T_{inner}}} = K_{e_T}\frac{\bar v_{T_{innerMax}}^2}{2g}

Substitute with minor loss relationships.

.. math::
  :label: he_T_inner_of_V

  2gh_{e_{innerInlet}} = \left(K_{e_T}\bar v_{T_{innerMax}}^2 + K_{e_B}\bar v_{B_{inner}}^2 + \bar v_{B_{inner}}^2\frac{1}{\Pi_{\Psi_P}} \right)

Solve for :math:`\bar v_{T_{innerMax}}`.

.. math::
  :label: V_trunk_of_he

  \bar v_{T_{innerMax}} = \sqrt{\frac{1}{K_{e_T}}\left[2g  h_{e_{innerInlet}} -\bar v_{B_{inner}}^2\left(K_{e_B} + \frac{1}{\Pi_{\Psi_P}} \right)\right]}

Use equation :eq:`V_trunk_of_he`to find the maximum trunk velocity. Use that constraint and the plant flow rate to find the trunk diameter, the number of filters, the filter flow rate, filter width, and filter length.

At this stage in the design process we have set the flow rate through the filter, the trunk and branch diameters (except for the backwash branches), the length of the branches, and the orifice spacing on the inner inlets.

Outer branch
------------

The outer trunk branch orifices must be designed so that the head loss during filtration is identical between inner and outer inlets. This will result spacing between the outer branch orifices that is more than double that of the inner branch orifices. The derivation is similar to that used to obtain equation :eq:`B_orifice_inner`. Equate the head loss in the inner and outer inlets during filtration. We will use the maximum velocity in the inner trunks as our reference velocity. Note that the results would be the same if we used the actual velocity in the inner trunks because the velocity will drop out of the equation in the end.

The head loss from the inlet box to the orifices in the inner inlets is given by equation :eq:`he_T_inner_of_V`. The head loss in the top inlet is similar. We will likely treat the backwash inlet as a separate design. The unknown we are solving for is the port velocity for the top inlet. That port velocity is not constrained by flow distribution and so we will enter it directly in the head loss equation knowing that all of the port kinetic energy is lost.

.. math::
  :label: he_T_top_of_V

  2gh_{e_{topInlet}} = \left(K_{e_T}\bar v_{T_{top}}^2 + K_{e_B}\bar v_{B_{top}}^2 + \bar v_{P_{top}}^2 \right)

Assuming that we use the same size branches and trunks for the top and inner inlets, then the velocities in the top trunk and branch are 1/2 of the velocities in the inner trunk and branch.

.. math::
  :label:

  \left(K_{e_T}\bar v_{T_{inner}}^2 + K_{e_B}\bar v_{B_{inner}}^2 + \bar v_{B_{inner}}^2\frac{1}{\Pi_{\Psi_P}} \right) = \frac{1}{4} \left(K_{e_T}\bar v_{T_{inner}}^2 + K_{e_B}\bar v_{B_{inner}}^2 \right) + \bar v_{P_{top}}^2

Solve for the port velocity, :math:`v_{P_{top}}`.

.. math::
  :label: V_P_outer


  \bar v_{P_{top}} = \sqrt{\frac{3}{4} \left(K_{e_T}\bar v_{T_{inner}}^2 + K_{e_B}\bar v_{B_{inner}}^2\right) +  \frac{\bar v_{B_{inner}}^2}{\Pi_{\Psi_P}}}

The port spacing can be obtained from equation :eq:`B_P_top`.

.. math::
  :label: v_P_to_v_Fi

  B_{P_{top}} = \frac{\Pi_{vc} \pi D_{P}^2\bar v_{P_{top}}}{4 v_{Fi}B_{B}}

Backwash inlet
--------------
The backwash inlet design is dominated by the flow distribution under backwash conditions when there is no head loss after the ports to promote flow distribution. Flow distribution can always be improved by increasing the port velocity and hence head loss and thus the maximum head loss is a second constraint.

The backwash branch requires some flow distribution to ensure that the sand bed fluidizes along the entire length of the pipe. This raises the question of what happens when the sand bed begins fluidizing and part of the branch is in fluidized sand and part of the branch is buried in settled sand. Either the interface between the settled sand and the fluidized sand moves into the settled sand and the bed is slowly completely fluidized or the interface moves toward the fluidized sand and much of the sand bed never fluidizes. The sand bed will form the angle of repose and thus the toe of the solid sand bed will be narrow. This toe is likely eroded by the water. Given that water velocity leaving the wing is much higher than is needed to fluidize the sand (because the wing is narrower than the spacing of the branches) there is plenty of fluid energy to erode the toe of the sand and fluidize it.

Another possible mechanism is erosion of the sand under the wing based on the high horizontal velocity of the water in the wing as the water travels in the direction of the pipe axis toward the fluidized bed.

In either case, it appears that the wing design results in high velocity at the toe of and settled sand that can then rapidly erode and fluidize the entire bed. This suggests that the flow uniformity from the orifices into the winged space does not need to be great and so a factor of 0.8 is likely reasonable in equation :eq:`Manifold_max_v_with_hl_series`.

The backwash inlet design is driven by the need for flow distribution at the port and branch levels and thus there are required relationships between port and branch and between branch and trunk velocities. In addition the total head loss will be a design constraint and thus we have 3 equations (2 flow distribution and 1 head loss) and 3 unknown velocities.

.. math::
  :label: v_P_to_v_B_BW

  \bar v_{P_{BW}}^2 = \frac{\bar v_{B_{BW}}^2}{\Pi_{\Psi_{P_{BW}}}}

Flow distribution between the trunk and branches is more important than the flow distribution into the wings because a whole branch could remain unfluidized if it received significantly less water. Thus a higher flow distribution criteria of perhaps 0.9 could be applied to the trunk-branch system. The port head loss is available to help achieve this flow distribution. Thus equation :eq:`Manifold_max_v_with_hl_series` applies.

.. math::
  :label: v_B_to_v_T_BW_draft

  \bar v_{T_{BW}}= \sqrt{2 g (h_{e_{B}} + h_{e_{P}})\Pi_{\Psi_{B_{BW}}}}

where

.. math::
  :label:

  h_{e_{B}} = K_{e_{B}}\frac{\bar v_{B_{BW}}^2}{2g}

and

.. math::
  :label:

  h_{e_{P}} = \frac{\bar v_{P_{BW}}^2}{2g}

Substitute to obtain a relationship between the three velocities.

.. math::
  :label: v_B_to_v_T_BW

  \bar v_{T_{BW}}^2= \left( K_{e_{B}}\bar v_{B_{BW}}^2 + \bar v_{P_{BW}}^2\right)\Pi_{\Psi_{B_{BW}}}

Eliminate the port velocity by substituting equation :eq:`v_P_to_v_B_BW` and solve for :math:`\bar v_{B_{BW}}^2`.

.. math::
  :label: v_B_to_v_T_BW

  \bar v_{B_{BW}}^2 = \bar v_{T_{BW}}^2 \frac{1}{\left( K_{e_{B}} + \frac{1}{\Pi_{\Psi_{P_{BW}}}} \right)\Pi_{\Psi_{B_{BW}}}}


The total head loss in the backwash inlet will be a design constraint.

.. math::
  :label: he_T_BW_of_V_draft1

  2gh_{e_{BW}} = \left(K_{e_T}\bar v_{T_{BW}}^2 + K_{e_B}\bar v_{B_{BW}}^2 + \bar v_{P_{BW}}^2 \right)

Substitute to obtain an equation for the maximum trunk velocity.

.. math::
  :label: he_T_BW_of_V_draft2

  2gh_{e_{BW}} = \left[K_{e_T}\bar v_{T_{BW}}^2 + \bar v_{B_{BW}}^2\left(K_{e_B} + \frac{1}{\Pi_{\Psi_{P_{BW}}}}\right) \right]

Substitute again to eliminate the branch velocity.

.. math::
  :label: he_T_BW_of_V_draft3

  2gh_{e_{BW}} = \bar v_{T_{BW}}^2\left[K_{e_T} +  \frac{1}{\Pi_{\Psi_{B_{BW}}}} \right]

Solve for the maximum trunk velocity.

.. math::
  :label: v_T_BW

  \bar v_{T_{BWmax}} = \sqrt\frac{2gh_{e_{BW}}}{K_{e_T} +  \frac{1}{\Pi_{\Psi_{B_{BW}}}}}

The backwash trunk may be the same diameter as the other trunk lines or it may be larger depending on the maximum velocities calculated from equations :eq:`V_trunk_of_he` and :eq:`v_T_BW`.

The maximum branch velocity is now obtained by solving equation :eq:`v_B_to_v_T_BW` for :math:`\bar v_{T_{BW}}`.

.. math::
  :label: v_B_of_v_T_BW

  \bar v_{T_{BW}} = \bar v_{B_{BW}} \sqrt{\left( K_{e_{B}} + \frac{1}{\Pi_{\Psi_{P_{BW}}}} \right)\Pi_{\Psi_{B_{BW}}}}

The branch minimum area is from equation :eq:`branch_V`.

.. math::
  :label: branch_A

  A_{B} = \frac{N_{layer} v_{Fi} B_{B} L_{B}}{v_{B}}

The port velocity is obtained from equation :eq:`v_P_to_v_B_BW` and the backwash port spacing is obtained by rewriting :eq:`v_P_to_v_Fi` to include the relationship that the backwash velocity is the filtration velocity times the number of filter layers.

.. math::
  :label: v_P_to_v_Fi

  B_{P_{bw}} = \frac{\Pi_{vc} \pi D_{P}^2\bar v_{P_{BW}}}{4 v_{Fi} N_{layer} B_{B}}

Backwash Flow Control Orifice
-----------------------------

The head loss through the backwash inlet system must be increased during filtration to match the head loss of the other inlets under conditions of ideal flow distribution between the filter layers. The orifice will likely be placed right on the inlet and thus this orifice will replace the entrance loss. The unknown is the inner diameter of the orifice. We know the expanded area (trunk area) and velocity and thus we can use the third form of the expansion head loss equation :eq:`minor_loss_equation`.

.. math::
  :label: bw_orifice_draft


     h_{e_{orifice}} = \left( \frac{A_{T}}{\Pi_{vc}A_{orifice}} -1 \right)^2 \, \frac{\bar v_{T_{bw}}^2}{2g} \, \, = \, \, K_e \frac{\bar v_{T_{bw}}^2}{2g}

Solve for the area of the orifice, :math:`A_{orifice}`.

.. math::
  :label: bw_orifice_draft


     D_{orifice} =  \frac{D_{T}}{\left[\Pi_{vc}\left( \frac{\sqrt{2gh_{e_{orifice}}}}{\bar v_{T_{bw}}} + 1\right)\right]^\frac{1}{2}}


Backwash Siphon
===============

Backwash Initiation Forces
==========================

At the beginning of backwash the sand is clogged and thus it requires more pressure to achieve the flow through the sand required to fluidize the sand. Instead, it is likely that one or more layers of sand begin to lift as a unit before falling apart and beginning to fluidize. During that transition the forces of the sand to lift the internal piping of the filter are quite large. We had structural failures in several of the early StaRS filters before we recognized the importance of a strong cable system to prevent the filter piping from lifting.

The maximum hydrostatic force acting on the bottom of the filter occurs when the inlet box is still full of water when the filter water depth is reduced by the siphon. The force in excess of the weight of the sand and water in the filter is equal to the height of water in the inlet box that is in excess of the backwash height of about 10 cm. This excess height is approximately equal to the terminal head loss through the filter during filtration, :math:`HL_{fi_{max}}`. The width of the filter bed that is contributing force to the dead end pipe is equal to 1/2 of the length of the branches. This force most likely acts uniformly on two layers of sand and associated piping at a time. The top two layers fluidize first when the water first stops going through the top inlet and thus all of the water is passing up through the top two layers. Thus the force is most likely shared by an inlet module and an outlet module.

There are two factors of 2 that show up in the equation. First, the total force is distributed between two layers. Second, half of the force from one side of the filter is carried by the trunk. Thus the force per unit length of the dead end pipe, :math:`\omega`, in one module is

.. math::
  :label:

  \omega = \rho g h_{l_{sand_{max}}} \frac{L_{branch}}{4}

The total force acting upward that must be resisted by the hold down devices is

.. math::
  :label:

  F_{up} = \rho g h_{l_{sand_{max}}} \frac{Q_{Fi}}{v_{Fi} N_{layer}}

Dead End Pipe Support Spacing
=============================

The optimal spacing of the supports allows the same deflection at the ends of the pipes (cantilever beam) and in the middle of the supports (beam simply supported at both ends). In both cases the load is uniformly distributed along the pipe (see `Beam Deflection Formulae <../_static/references/Beam_Deflection_Formulae.pdf>`_).

.. math::
  :label: cantelever

  \delta_{max} = \frac{\omega L_{cantilever}^4}{8EI}

The equivalent equation for a beam with simply supported ends is

.. math::
  :label: supported_at_both_ends

  \delta_{max} = \frac{5\omega L_{both}^4}{384EI}

We'd like the deflection to be the same in the cantelever ends of the dead end pipe as in the middle sections of the pipe where it is simply supported. Set the deflections to be the same.

.. math::
  :label: draft

  \frac{5\omega L_{both}^4}{384EI} = \frac{\omega L_{cantilever}^4}{8EI}

Solve for the ratio of the length of the respective beams

.. math::
  :label: draft

  \frac{ L_{cantilever}}{L_{both}} = \left(\frac{5 }{48}\right)^\frac{1}{4} = 0.57

This result is a bit surprising until we recognize that the cantelever beam is not allowed to rotate at the point where it is connected while the simple beam was allowed to rotate. The simple conclusion from all of this is that the cantelever sections can be 1/2 the length of the simply supported sections of the dead end pipe.

We previously supported the Dead End pipe at the ends. That wasn't optimal. With the new StaRS design it is possible to make larger filters and it isn't get clear what the optimal ratio of width to length of the filters will be. In any case, the length of the dead end pipe is likely to be significantly longer than in our previous designs for the highest flow rates. It will be necessary to ensure that the deflection isn't too large.

The deflection of the dead end pipe is given by equation :eq:`supported_at_both_ends`. The area moment of inertia, :math:`I` is

.. math::
  :label: pipe_Ix_of_OD_ID

  I = \frac{\pi}{4}\left(OD^4 - ID^4\right)

The standard diameter ratio for PVC pipes is

.. math::
  :label: SDR

  \Pi_{SDR} = \frac{OD}{t}

Substituting equation :eq:`SDR` into equation :eq:`pipe_Ix_of_OD_ID`

.. math::
  :label:

  I = \frac{\pi}{4}\left[OD^4 - \left(\Pi_{SDR}t - t\right)^4\right]

simplifying

.. math::
  :label:

  I = \frac{\pi}{4}OD^4\left[1 - \left(1-\frac{1}{\Pi_{SDR}}\right)^4\right]

If we set a maximum deflection, then we can solve equation :eq:`supported_at_both_ends` for the maximum length between supports.

.. math::
  :label: supported_at_both_ends

  L_{both} = \left(\frac{384EI\delta_{max}}{5\omega}\right)^{\frac{1}{4}}
