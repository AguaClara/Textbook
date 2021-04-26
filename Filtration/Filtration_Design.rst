.. _title_Filtration_Design:


********************************
Stacked Rapid Sand Filter Design
********************************

Introduction
============

The hydraulic design of both the enclosed and open stacked rapid sand filter is complicated by the number of parallel flows, the manifolds in series, and the need to handle both backwash and filter modes. The design requires careful attention to weir hydraulics to achieve the target backwash flows when the plant is operating at less than full capacity. The siphon system has a tight design constraint to ensure that the siphon doesn't trigger prematurely.

There are two possible constraints on the trunk size. Either the trunk size is dictated by backwash flow distribution requirements or the trunk size is dictated by the need to have uniform flow distribution between filter layers and hence to have exactly twice the flow rate through the inner inlets.

There are 4 levels of flow distribution in StaRS filters.

  * between filters: will be handled by design of the weirs into the filter inlet boxes
  * between sand layers: easily obtained by simply requiring that inlet head losses be identical in the 4 inlets under conditions of the target flow and accounting for the fact that the inner inlets have double the flow of the outer inlets.
  * between branches (trunkPortQ_pi): aided considerably by the head loss through the sand and is helped by increasing the head loss though the orifices. Suggest using a value of 0.9 for this constraint. This constraint will be combined with a maximum permissible head loss during backwash to determine the required diameter of the trunk lines and will be combined with the equal trunk head loss constraint to obtain the diameter of the orifices.
  * between orifices (branchPortQ_pi): made less important by the winged design that allows correcting flow in the winged space before the water enters the sand bed. Suggest using a value of 0.8 for this constraint. This constraint will determine the required diameter of the branches.


The clean bed sand head loss and including the head loss right at the point where the water enters the sand helps with the flow distribution between branches and between orifices. We are not currently including the benefit of the high velocity at the point where the water enters the sand.


Design Steps
============

#. Apply a maximum head loss during backwash and flow distribution between filter layers during filtration to set the maximum velocity in the trunk during backwash


Trunk Diameter
-----------------------

The first design step is to calculate the diameter of the trunk lines which is set by the filtration flow distribution between layers and the head loss required to ensure flow distribution through the orifices within a branch. The maximum acceptable inlet head loss during backwash sets the required depth of the open filter box and so is an important constraint for O-StaRS. Both the inner and outer inlet head loss during filtration is :math:`\frac{1}{N_{layers}^2}` times the backwash inlet head loss because the head loss is proportional to the flow ratio squared and because we will set the inlet head losses to be identical during filtration.

To simplify the analysis we will neglect major losses and calculate the minor losses using the trunk velocity during backwash. If the branch area is large compared with the trunk diameter, then the flow distribution between the branches is set by the head loss through the orifices and we can treat this as a single flow distribution problem rather than having two flow distribution events (branches and then orifices) in series.

We will also use the manifold velocity to obtain the minor loss coefficients for the orifices. This will simplify the analysis. The minor loss coefficient associated with the orifices, :math:`K_{e_{innerOrifices}}`, can be obtained from the minor loss equation written for port exit head loss. All of the kinetic energy in the port jet is lost.

The head loss through a port or orifice can be expressed in the minor loss equation form.

.. math::
  :label: eq_he_port

  h_{e_{P_{inner}}} = \frac{\bar v_{P_{inner}}^2}{2g} = K_{e_{innerOrifices}}\frac{\bar v_{T_{inner}}^2}{2g}

where the port velocity :math:`\bar v_{P}` is the *contracted* velocity out of the port. Substitute equation :eq:`eq_he_port` into equation :eq:`Manifold_max_v_with_hl_series`.

Incorrect assumption
====================

Below we assumed that the flow distribution between branches sets the orifice diameter. We made this assumption when we used equation :eq:`Manifold_max_v_with_hl_series`. That turns out to not be the controlling constraint. The sand head loss is sufficient to get good flow distribution between branches. It isn't clear what sets the required port velocity or the orifice area. Could be...

 * distribution between layers (sand head loss is greater than the port head loss because the port head loss is limited to about 2 cm if we assume 72 cm of head loss during backwash and the sand head loss is about 5 cm.)
 * distribution between branches (same reason as above)
 * distribution between inner inlet ports during filtration
 *  distribution between outer inlet ports during backwash
 * distribution between slots on outlet branches

Need to figure out which of the last three constraints controls. Given that the outer orifices have much higher head loss to get equal flow distribution between layers it will be the inner orifices that need to have their head loss set by a flow distribution requirement.

The inner inlet flow distribution requirement is that the flow from the branch into the wing area be reasonably uniform so that the velocity in the wing area is low. We will need to do some more analysis of this flow, but we can assume initially that a flow distribution value of 0.8 using equation :eq:`Manifold_max_v_no_hl_series` will be adequate. We need a relationship between trunk and branch velocity. Branch velocity is limited to ensure that the branch head loss is reasonable and for flow distribution between orifices.

Branch flow constraint

 * branch velocity equal to trunk velocity on inner inlets. (let's try this)
 *


.. math::
  :label: Manifold_max_v_with_hl_sand

  \frac{\bar v_{P}}{\bar v_{B_1}} = \sqrt{\frac{\Pi_{Q}^2 + 1}{2(1 - \Pi_{Q}^2)}}

   \frac{\bar v_{T_{inner}}^2}{2g}= \frac{\bar v_{B_{inner}}^2}{2g} = \left(K_{e_{innerOrifices}}\frac{\bar v_{T_{inner}}^2}{2g} + h_{l_{sand}}\right)\frac{2(1 - \Pi_{Q}^2)}{\Pi_{Q}^2 + 1}

We have two unknowns, the manifold velocity and the orifice minor loss coefficient that scales with the manifold velocity. The second relationship we can apply is the maximum head loss that we are willing to accommodate during backwash. Given that the inner and outer inlets have the same head loss during filtration,  the backwash head loss is :math:`N_{layer}^2` times either the inner or outer filtration head loss.

.. math::
  :label:

  h_{e_{outerInlet_{Bw}}} = N_{layer}^2 h_{e_{innerInlet_{Fi}}} =  N_{layer}^2 \left(K_{e_{trunk}} + K_{e_{branch}} + K_{e_{innerOrifices}}\right)\frac{\bar v_{T_{inner}}^2}{2g}

We now have two equations in two unknowns and can solve for whichever term we choose. Arbitrarily we will eliminate :math:`K_{e_{innerOrifices}}` by first solving the previous equation for :math:`K_{e_{innerOrifices}}`.

.. math::
  :label: K_e_innerOrifices

    K_{e_{innerOrifices}} = \frac{2 g h_{e_{outerInlet_{Bw}}}}{N_{layer}^2 \bar v_{T_{inner}}^2} - K_{e_{trunk}} - K_{e_{branch}}

Now solve equation :eq:`Manifold_max_v_with_hl_sand` for the manifold velocity

.. math::
  :label:

   \frac{\bar v_{T_{inner}}^2}{2g} -  \left(K_{e_{innerOrifices}}\frac{\bar v_{T_{inner}}^2}{2g} \right)\frac{2(1 - \Pi_{Q}^2)}{\Pi_{Q}^2 + 1} = h_{l_{sand}}\frac{2(1 - \Pi_{Q}^2)}{\Pi_{Q}^2 + 1}

Now eliminate :math:`K_{e_{innerOrifices}}` in equation :eq:`Manifold_max_v_with_hl_sand`.


.. math::
  :label:

   \frac{\bar v_{T_{inner}}^2}{2g} -  \left( \frac{2 g h_{e_{outerInlet_{Bw}}}}{N_{layer}^2 \bar v_{T_{inner}}^2}\frac{\bar v_{T_{inner}}^2}{2g} - \left(K_{e_{trunk}} + K_{e_{branch}}\right)\frac{\bar v_{T_{inner}}^2}{2g} \right)\frac{2(1 - \Pi_{Q}^2)}{\Pi_{Q}^2 + 1} = h_{l_{sand}}\frac{2(1 - \Pi_{Q}^2)}{\Pi_{Q}^2 + 1}


Simplify more!

.. math::
  :label:

   \frac{\bar v_{T_{inner}}^2}{2g}\left(\frac{\Pi_{Q}^2 + 1}{2(1 - \Pi_{Q}^2)} +   \left(K_{e_{trunk}} + K_{e_{branch}}\right)\right)  = h_{l_{sand}} +\frac{ h_{e_{outerInlet_{Bw}}}}{N_{layer}^2}


Simplify more!

.. math::
  :label: v_M_inner

   \bar v_{T_{inner}} = \left[\frac{2g\left(h_{l_{sand}} +\frac{ h_{e_{outerInlet_{Bw}}}}{N_{layer}^2}\right)}{\frac{\Pi_{Q}^2 + 1}{2(1 - \Pi_{Q}^2)} +   K_{e_{trunk}} + K_{e_{branch}}}\right]^\frac{1}{2}



Inner trunk branch orifice spacing
----------------------------------

The orifice diameter will be constrained by the wing fabrication. Apply conservation of mass to obtain the port velocity to filter velocity ratio. Each port serves an area equal to the branch spacing times the port spacing.

.. math::
  :label: v_port_inner_to_v_Fi

  \frac{\bar v_{P_{inner}}}{2 v_{Fi}} = \frac{B_{branch} B_{orifice_{inner}}}{\Pi_{vc}\frac{\pi}{4} D_{orifice}^2}

where the factor of 2 is because the inner trunks serve two layers of sand. The orifice diameter for the inner inlets is also constrained by the required minor loss coefficient of the orifices given by equation :eq:`K_e_innerOrifices`. The relationship between the minor loss coefficient :math:`K_{e_{innerOrifices}}` and the port velocity is obtained by setting the minor head loss equation equal for the two velocities used.

The :math:`K_{e_{innerOrifices}}` is a minor loss coefficient for the orifices scaled to the velocity of the manifold. All of the kinetic energy is lost when flowing through the orifice and thus the minor loss coefficient scaled to the contracted orifice velocity is equal to 1. Solve equation :eq:`eq_he_port` for the :math:`\bar v_{P_{inner}}`.

.. math::
  :label: v_P_inner_to_v_M_inner

  \bar v_{P_{inner}} = \sqrt{K_{e_{innerOrifices}}} \bar v_{T_{inner}}

Combine equation :eq:`v_P_inner_to_v_M_inner` and :eq:`v_port_inner_to_v_Fi`
Solve for orifice spacing.

.. math::
  :label: B_orifice_inner

  B_{orifice_{inner}} = \frac{ \bar v_{T_{inner}} \Pi_{vc}\pi D_{orifice}^2 \sqrt{K_{e_{innerOrifices}}}}{8 v_{Fi} B_{branch}}


Outer trunk branch orifice spacing
----------------------------------

The outer trunk branch orifices must be designed so that the head loss during filtration is identical between inner and outer inlets. This will result spacing between the outer branch orifices that is more than double that of the inner branch orifices. The derivation is similar to that used to obtain equation :eq:`B_orifice_inner`. Equate the head loss in the inner and outer inlets during filtration. We will use the velocity in the inner trunks as our reference velocity. First the head loss from the inlet box to the orifices in the outer inlets is given by

.. math::
  :label: he_outer

  h_{e_{outerInlet_{Fi}}} = \left(K_{e_{trunk}} + K_{e_{branch}} + K_{e_{outerOrifices}}\right)\frac{1}{4}\frac{\bar v_{T_{inner}}^2}{2g}


Now the inner inlets

.. math::
  :label: he_inner

  h_{e_{innerInlet_{Fi}}} = \left(K_{e_{trunk}} + K_{e_{branch}} + K_{e_{innerOrifices}}\right)\frac{\bar v_{T_{inner}}^2}{2g}

where the factor of 4 difference is because the velocity in the outer inlets is half the inner inlets because each inner inlet serves 2 filter layers.

Set the head loss for the inner and outer inlets to be equal.

.. math::
  :label:

  \left(K_{e_{trunk}} + K_{e_{branch}} + K_{e_{outerOrifices}}\right)\frac{1}{4}\frac{\bar v_{T_{inner}}^2}{2g}
   = \left(K_{e_{trunk}} + K_{e_{branch}} + K_{e_{innerOrifices}}\right)\frac{\bar v_{T_{inner}}^2}{2g}

Eliminate the identical terms and solve for :math:`K_{e_{outerOrifices}}`.

.. math::
  :label: K_e_outerOrifices

  K_{e_{outerOrifices}}
  = 3K_{e_{trunk}} + 3K_{e_{branch}} + 4K_{e_{innerOrifices}}

Apply conservation of mass to obtain the port velocity to filter velocity ratio. Each port serves an area equal to the branch spacing times the port spacing.

.. math::
  :label: v_port_outer_to_v_Fi

  \frac{\bar v_{P_{outer}}}{v_{Fi}} = \frac{B_{branch} B_{orifice_{outer}}}{\Pi_{vc}\frac{\pi}{4} D_{orifice}^2}

The orifice diameter for the outer inlets is also constrained by the required minor loss coefficient of the orifices given by equation :eq:`K_e_outerOrifices`. The relationship between the minor loss coefficient :math:`K_{e_{outerOrifices}}` and the port velocity is obtained by setting the minor head loss equation equal for the two velocities used.

The :math:`K_{e_{outerOrifices}}` is a minor loss coefficient for the orifices scaled to the velocity of the manifold. All of the kinetic energy is lost when flowing through the orifice and thus the minor loss coefficient scaled to the contracted orifice velocity is equal to 1. Solve equation :eq:`eq_he_port` for the :math:`\bar v_{P_{outer}}`.

.. math::
  :label: v_P_outer_to_v_M_inner

  \bar v_{P_{outer}} = \sqrt{K_{e_{outerOrifices}}} \frac{\bar v_{T_{inner}}}{2}

Combine equation :eq:`v_P_outer_to_v_M_inner` and :eq:`v_port_outer_to_v_Fi`
Solve for port spacing.

.. math::
  :label: B_orifice_outer

  B_{orifice_{outer}} = \frac{\bar v_{T_{inner}} \Pi_{vc}\pi D_{orifice}^2 \sqrt{K_{e_{outerOrifices}}} }{8 v_{Fi} B_{branch}}

Use a combination of equations :eq:`K_e_outerOrifices` and :eq:`B_orifice_outer` to find the outer orifice spacing.


Inner branch diameter
---------------------
The branch diameter for inner and upper inlets is set by the

 * flow distribution between ports in the inner inlets

 * or by the goal of keeping the branch head loss low

Also, max branch length


Outer branch diameter
---------------------
Also, max branch diameter






JUNK BELOW
==========


Simplify more!

.. math::
 :label: Manifold_max_v_with_hl_sand_of_K_orifice

  \bar v_{T_{inner}} =\sqrt{\frac{2gh_{l_{sand}}}{\frac{\Pi_{Q}^2 + 1}{2(1 - \Pi_{Q}^2)} -  \left(K_{e_{innerOrifices}}\right)}}

Now eliminate :math:`K_{e_{innerOrifices}}` in equation :eq:`Manifold_max_v_with_hl_sand`.

.. math::
 :label:

  \bar v_{T_{inner}} =\sqrt{\frac{2gh_{l_{sand}}}{\frac{\Pi_{Q}^2 + 1}{2(1 - \Pi_{Q}^2)} + K_{e_{trunk}} + K_{e_{branch}} -   \frac{2 g h_{e_{outerInletBw}}}{N_{layer}^2 \bar v_{T_{inner}}^2}}}


Now solve for :math:`\bar v_{T_{inner}}`.

.. math::
 :label: Manifold_max_v_with_hl_sand_of_K_orifice

  {\bar v_{T_{inner}}}^2 =\frac{2gh_{l_{sand}}}{\frac{\Pi_{Q}^2 + 1}{2(1 - \Pi_{Q}^2)} + K_{e_{trunk}} + K_{e_{branch}} -   \frac{2 g h_{e_{outerInletBw}}}{N_{layer}^2 \bar v_{T_{inner}}^2}}

The head loss thru the sand is a function of the filter layer thickness. The filter layer thickness will need to increase for trunk lines that are larger than about 6 inches. This creates a need to iterate to obtain a solution. We will simplify this by neglecting the conservative effect of increasing the filter layer depth.

Next solve for the orifice loss coefficient using equation :eq:`K_e_innerOrifices`.






whatis worng

.. math::
  :label:

  \frac{2 g h_{e_{outerInletBw}}}{N_{layer}^2 \bar v_{T_{inner}}^2} - K_{e_{trunk}} - K_{e_{branch}}














where :math:`K_{e_{trunk}}` is the minor loss coefficient for all of the inlet trunks. The inlet trunks will be designed to have the same number of elbows. It is possible that we can design this so that the :math:`K_{e_{branch}}` is small by having the branch area larger than the trunk area.

 We want the head loss to be a function of the manifold velocity. The relationship between port and manifold velocity is given by equation :eq:`Manifold_max_v_no_hl_series`. Substitute equation :eq:`Manifold_max_v_no_hl_series` into equation :eq:`eq_he_port` to obtain an equation that is only a function of the manifold velocity.

.. math::
  :label: eq_he_port_of_v_manifold

  h_{e_P} = \frac{\Pi_{Q}^2 + 1}{2\left(1 - \Pi_{Q}^2\right)}\frac{\bar v_{M_1}^2}{2g}

By analogy with the minor loss head loss equation we obtain the minimum minor loss coefficient scaled with the manifold velocity for the orifices in the top and bottom (outer) inlets.

.. math::
  :label: eq_Ke_outerOrifices

  K_{e_{outerOrifices}} =\frac{\Pi_{Q}^2 + 1}{2\left(1 - \Pi_{Q}^2\right)}

Solve equation :eq:`eq_he_inlet_Bw` for the maximum manifold velocity and substitute equation :eq:`eq_Ke_outerOrifices`.

.. math::
  :label: v_max_manifold

  \bar v_{M_{Bw}} = \sqrt{\frac{2 g h_{e_{inlet_{Bw}}}}{K_{e_{trunk}} + K_{e_{branch}} + \frac{\Pi_{Q}^2 + 1}{2\left(1 - \Pi_{Q}^2\right)}}}

Given a filter flow rate, equation :eq:`v_max_manifold` can be used to find the minimum diameter of the trunks. Alternatively, the maximum flow rate for each available manifold diameter can be calculated.

Backwash Inlet Orifice Area and Spacing
---------------------------------------

The port contracted velocity is given by solving equation :eq:`Manifold_max_v_no_hl_series` for the port velocity. We'd like the port velocity during filtration since the other inlet manifolds will be designed based on filtration velocity and backwash manifold velocity (from equation :eq:`v_max_manifold`).

.. math::
  :label: port_contracted_v

   \bar v_{P_{Fi}} = \frac {\bar v_{M_{Bw}}}{N_{layer}}\sqrt{\frac{\Pi_{Q}^2 + 1}{2(1 - \Pi_{Q}^2)}}

The ratio of the active filter area to the orifice vena contracta area is equal to the ratio of the contracted port velocity during filtration to the filtration velocity. This ratio is the same during backwash.

Apply conservation of mass to obtain the port velocity to filter velocity ratio. Each port serves an area equal to the branch spacing times the port spacing.

.. math::
  :label: v_port_to_v_Fi

  \frac{\bar v_{P_{Fi}}}{v_{Fi}} = \frac{B_{branch} B_{orifice_{outer}}}{\Pi_{vc}\frac{\pi}{4} D_{orifice}^2}

Then the orifice diameter for the bottom and top inlets is given by

.. math::
  :label: D_outerPort_ofVport

  D_{orifice} = \sqrt{\frac{v_{Fi}}{\bar v_{P_{Fi}}}\frac{B_{branch} B_{orifice_{outer}}}{\Pi_{vc}\frac{\pi}{4} }}

Eliminate port velocity by substituting equation :eq:`port_contracted_v`

.. math::
  :label: D_outerPort

  D_{orifice} = 2\sqrt{\frac{v_{Fi}N_{layer}}{\bar v_{M_{Bw}}}\frac{B_{branch} B_{orifice_{outer}}}{\pi\Pi_{vc} }}\left(\frac{2(1 - \Pi_{Q}^2)}{\Pi_{Q}^2 + 1}\right)^{\frac{1}{4}}

We also need this equation solved for the orifice spacing because the orifice diameter is tightly constrained in the wing inlet design.

.. math::
  :label: B_outerPort

  B_{orifice_{outer}} = D_{orifice}^2  \frac{\bar v_{M_{Bw}}}{v_{Fi}N_{layer}}  \frac{\pi\Pi_{vc} }{4 B_{branch} } \left(\frac{\Pi_{Q}^2 + 1}{2(1 - \Pi_{Q}^2)}\right)^{\frac{1}{2}}

Inner Inlet Orifice Area and Spacing
------------------------------------

The inner inlets each serve two sand layers and thus have twice the flow rate of the outer (top and bottom) inlets. The head loss must be the same for the various inlets to optimize flow division between filter layers. The inner trunk minor losses will be higher due to the higher flow rate and thus the orifice head loss for the inner inlets must be less than the orifice head loss for the outer inlets.

Let's use the head loss constraint during filtration and see what we get. First the head loss from the inlet box to the orifices in the outer inlets is given by

.. math::
  :label:

  h_{e_{outerInlet_{Fi}}} = \left(K_{e_{trunk}} + K_{e_{branch}} + K_{e_{outerOrifices}}\right)\frac{\bar v_{M_{Bw}}^2}{2g N_{layer}^2}

where the factor of :math:`N_{layer}` comes from the fact that the velocity in the outer inlets during filtration is :math:`1/N_{layer}` the velocity during backwash.

Now the inner inlets

.. math::
  :label:

  h_{e_{innerInlet_{Fi}}} = \left(K_{e_{trunk}} + K_{e_{branch}} + K_{e_{innerOrifices}}\right)\frac{2\bar v_{M_{Bw}}^2}{g N_{layer}^2}

where the factor of 4 difference is because the velocity in the inner inlet is double the outer inlets because each inner inlet serves 2 filter layers.

The manifold - port flow distribution constraint (equation :eq:`v_max_manifold`) is not required during filtration. This is because the sand provides additional head loss in series and because the outlet system has a matching piezometric head distribution such that the difference in piezometric head is uniform across the filter bed. Thus the only constraint for the inner inlets is that there be uniform flow distribution between sand bed layers and thus the head loss for the various paths from inlet box to sand bed must be identical. This will give a required relationship between the inner and outer orifice Ke.

.. math::
  :label:

  \left(K_{e_{trunk}} + K_{e_{branch}} + K_{e_{outerOrifices}}\right)\frac{\bar v_{M_{Bw}}^2}{2g N_{layer}^2} = \left(K_{e_{trunk}} + K_{e_{branch}} + K_{e_{innerOrifices}}\right)\frac{2\bar v_{M_{Bw}}^2}{g N_{layer}^2}

Eliminate the identical terms.

.. math::
  :label:

  \left(K_{e_{trunk}} + K_{e_{branch}} + K_{e_{outerOrifices}}\right) = 4\left(K_{e_{trunk}} + K_{e_{branch}} + K_{e_{innerOrifices}}\right)

Solve for :math:`K_{e_{innerOrifices}}`.

.. math::
  :label:

 K_{e_{innerOrifices}} = \frac{K_{e_{outerOrifices}} - 3K_{e_{trunk}} - 3K_{e_{branch}}}{4}

The value of :math:`K_{e_{innerOrifices}}` should be calculated based on the actual value of :math:`K_{e_{outerOrifices}}` given the orifice diameter and spacing used. FOr now we will assume that we will not do any rounding in the spacing of the orifices and thus we can use the value obtained from :eq:`eq_Ke_outerOrifices`.


.. math::
  :label: eq_Ke_innerOrifices

  K_{e_{innerOrifices}} = \frac{\frac{\Pi_{Q}^2 + 1}{2\left(1 - \Pi_{Q}^2\right)} - 3K_{e_{trunk}} - 3K_{e_{branch}}}{4}

The :math:`K_{e_{innerOrifices}}` is a minor loss coefficient for the orifices scaled to the velocity of the manifold. All of the kinetic energy is lost when flowing through the orifice and thus the minor loss coefficient scaled to the contracted orifice velocity is equal to 1 (see equation :eq:`eq_he_port`). Set the minor head loss equation to be equal for the two choices of velocity.

.. math::
  :label:

  \frac{\bar v_{P}^2}{2g} = K_{e_{innerOrifices}}\frac{2\bar v_{M_{Bw}}^2}{g N_{layer}^2}

where the factor of :math:`2^2` is because the flow through an inner manifolds is double the flow though the outer manifolds. Solve for port velocity.

.. math::
  :label:

  \bar v_{P} = \frac{2\bar v_{M_{Bw}}}{N_{layer}} \sqrt{K_{e_{innerOrifices}}}

The next step is to solve for the distance between orifices. This is identical to the method we used to find equation :eq:`B_outerPort`. The ratio of filter velocity to port velocity is given by equation :eq:`v_port_to_v_Fi`.

.. math::
  :label:

  v_{Fi} \frac{B_{branch} B_{orifice_{inner}}}{\Pi_{vc}\frac{\pi}{4} D_{orifice}^2} = \frac{2\bar v_{M_{Bw}}}{N_{layer}} \sqrt{K_{e_{innerOrifices}}}

Solve for the orifice spacing, :math:`B_{orifice}`.

.. math::
  :label: B_innerPort

  B_{orifice_{inner}}  = \frac{\bar v_{M_{Bw}}\Pi_{vc}\pi D_{orifice}^2}{2 v_{Fi} N_{layer} B_{branch}} \sqrt{K_{e_{innerOrifices}}}


Find:

* backwash branch ID
* other branch ID
* max length of a branch given an ID
* algorithm to set filter box dimensions.

old stuff
=========

#. Calculate array of maximum filter flows given available trunk sizes and given constraint of maximum allowable head loss in the trunk line during backwash. Note that the outer inlet trunk minor loss coefficient is set (by adding a flow restriction at the inlet to the trunk line) to be 4 times the minor loss coefficient for the inner inlet trunks so that during filtration they have the same head loss when the outer trunks have 1/2 the flow of the inner trunks.
#. Select the trunk size that gives a number of filters equal to or less than the minimum number of filters required for operation and maintenance.
#. Calculate filter flow given minimum number of filters
#. Calculate the orifice head loss required to provide uniform flow to the sand bed during backwash. This is based on the required ratio of port to manifold velocity (see Equation :eq:`Manifold_max_v_no_hl_series`).
#. Design the branches based on manifold flow distribution requirements
#. Set the siphon drain time (assuming no inflow!) to equal the time required to refill the filter box after backwash.
#. Design the siphon pipe given the constraint on drain time
#. Design the siphon air valve given volume of air in the siphon
#. Calculate all elevations
#. Design backwash flow control weirs



Potential Changes to the Filter Design
======================================

* Have the siphon manifold exit straight through the side of the filter (perhaps in line with the other inlets and outlets) and then elbow up to the required elevation and elbow and Tee back down again. This would make the siphon install inside the filter be a single straight pipe instead of the large assembly that is currently used. This will have the additional advantage that the connection between this drain manifold and the pipe stub in the wall doesn't have to be leak tight! The connection could be a wrap of stainless steel and two hose clamps.
* Switch to gravity exclusion zones that include orifices to get uniform flow distribution without risk of sand scour.
* Simplest design to fabricate will have identical trunk lines for all inlets
* Change the inlet and outlet boxes so that all of the inlet trunks have only one elbow
* Outlet trunks each have 2 elbows


Maximum Trunk Flows
===================

The trunks are constrained to both provide similar flow to each filter layer and to provide similar flow to each branch within the sand bed. Providing the same flow to each filter layer during filtration is the key constraint that determines the size of the trunk lines. The most challenging flow distribution is between middle inlets that carry flow for two layers and the top and bottom inlets that carry flow for one sand layer. This flow distribution is ensured by making the head loss through the outer inlet trunks to be equal to the head loss through the inner inlet trunks when the outer inlet trunks have 1/2 the flow of the inner inlet trunks.

.. _figure_Filter_Max_Q_given_ND:

.. figure:: Images/Filter_Max_Q_given_ND.png
    :width: 400px
    :align: center
    :alt: Trunk flows

    The flows through the inlet trunks of stacked rapid sand filters are not identical and this requires a careful hydraulic design.


The flow distribution within the filter bed to ensure complete fluidization of the sand bed during backwash can be achieved by increasing the head loss through the flow control orifices in the branches. Calculating this required head loss is the second step in designing the filter inlet piping.
