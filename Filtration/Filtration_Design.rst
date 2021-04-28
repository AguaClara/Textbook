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

The diameter of the trunk lines is set by the filtration flow distribution between branches in the inner trunks and the maximum acceptable inlet head loss during backwash. The backwash head loss constraint is directly connected to the head loss during filtration because the velocity in the backwash trunk changes by a factor of the number of filter layers. The backwash inlet head loss sets the required depth of the open filter box and so is an important constraint for O-StaRS. Both the inner and outer inlet head loss during filtration is :math:`\frac{1}{N_{layers}^2}` times the backwash inlet head loss because the head loss is proportional to the flow ratio squared and because we will set the inlet head losses to be identical during filtration.

The equation for flow distribution with additional head loss in series is :eq:`Manifold_max_v_with_hl_series`.

.. math::
  :label: Trunk_max_v_with_hl_series_of_he

   \frac{\bar v_{T_{innerMax}}^2}{2g}=  \left(h_{e_{B_{inner}}} + h_{e_{P_{inner}}} + h_{l_{sand}} \right)\Pi_{\Psi_B}


The :math:`h_{e_{port}}` the minor loss associated with entering the branch (see equation :eq:`he_branch`). The :math:`h_{l_{series}}` is the sum of the orifice head loss (see equation :eq:`eq_he_port`) and the head loss through the sand.

.. math::
  :label: Trunk_max_v_with_hl_series_of_V

   \bar v_{T_{innerMax}} =  \sqrt{\Pi_{\Psi_B}\left[\bar v_{B_{innerMax}}^2\left(K_{e_B} + \frac{1}{\Pi_{\Psi_P}}\right) + 2gh_{l_{sand}} \right]}

This shows that the trunk velocity is limited by the branch velocity even without applying the head loss constraint. However, even if the branch velocity approaches zero, the trunk velocity can still be quite high because of the balancing effect of the sand head loss. This constraint ends up not being useful because flow division between branches is not a critical constraint..

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

The minimum diameter of a branch is obtained from mass conservation.



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

The maximum length of a branch is set by mass conservation and the flow required to serve the filter area corresponding to the length of the branch.

.. math::
  :label: L_branch_max_conserveQ

  2 v_{Fi} L_{branch_{max}} B_{branch} = v_{B_{innerMax}} A_{pipe}

Solve for :math:`L_{branch_{max}}`.

.. math::
  :label: L_branch_max

   L_{branch_{max}} = \frac{v_{B_{innerMax}} A_{pipe}}{2 v_{Fi}  B_{branch}}

Solve for the minimum pipe ID.

.. math::
  :label: D_branch_min

 D_{branch_{min}}= \sqrt\frac{8 v_{Fi}  B_{branch} L_{branch}}{\pi v_{B_{innerMax}}}

The head loss through the inner ports or orifices can be expressed in the minor loss equation form.

.. math::
  :label: eq_he_port

  h_{e_{P_{inner}}} = \frac{\bar v_{P_{inner}}^2}{2g} = \frac{\bar v_{B_{inner}}^2}{2g}\frac{1}{\Pi_{\Psi_P}

where the port velocity :math:`\bar v_{P}` is the *contracted* velocity out of the orifice.

The branch entrance loss is given by

.. math::
  :label: he_branch

  h_{e_{B_{inner}}} = K_{e_B}\frac{\bar v_{B_{innerMax}}^2}{2g}

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

  2gh_{e_{innerInlet}} = \left(K_{e_T} + K_{e_B}\Pi_{BT}  + \Pi_{BT} \frac{1}{\Pi_{\Psi_P}} \right)\bar v_{T_{inner}}^2

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
  :label: v_port_outer_to_v_Fi

  B_{orifice_{outer}} = \frac{\bar v_{T_{innerMax}} \Pi_{vc} \pi D_{orifice}^2 \sqrt{\Pi_{PB_{outer}}  \Pi_{BT}} }{8 v_{Fi} B_{branch}}
