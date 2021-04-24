.. _title_Filtration_Design:


********************************
Stacked Rapid Sand Filter Design
********************************

Introduction
============

The hydraulic design of both the enclosed and open stacked rapid sand filter is complicated by the number of parallel flows, the manifolds in series, and the need to handle both backwash and filter modes. The design requires careful attention to weir hydraulics to achieve the target backwash flows when the plant is operating at less than full capacity. The siphon system has a tight design constraint to ensure that the siphon doesn't trigger prematurely.

There are two possible constraints on the trunk size. Either the trunk size is dictated by backwash flow distribution requirements or the trunk size is dictated by the need to have uniform flow distribution between filter layers and hence to have exactly twice the flow rate through the inner inlets.

An analysis of the design reveals that the extra orifice head loss required to achieve the flow distribution between inner and outer trunks during filtration is greater than the head loss required to achieve uniform flow from the orifices during backwash.

Design Steps
============

#. Apply a maximum head loss during backwash and flow distribution between filter layers during filtration to set the maximum velocity in the trunk during backwash


Backwash Trunk Diameter
-----------------------

The first design step is to calculate the diameter of the trunk lines which is set by the backwash flow distribution requirement. The maximum acceptable head loss during backwash sets the required depth of the open filter box and so is an important constraint for O-StaRS. To simplify the analysis we will neglect major losses and calculate the minor losses using the trunk velocity during backwash.

If the branch area is large compared with the trunk diameter, then the flow distribution between the branches is set by the head loss through the orifices and we can treat this as a single flow distribution problem rather than having two flow distribution events (branches and then orifices) in series.

The total head loss in the inlet trunk and branches during backwash is

.. math::
  :label: eq_he_inlet_Bw

  h_{e_{inlet_{Bw}}} = \left(K_{e_{trunk}} + K_{e_{branch}} + K_{e_{outerOrifices}}\right)\frac{\bar v_{M_{Bw}}^2}{2g}

where :math:`K_{e_{trunk}}` is the minor loss coefficient for all of the inlet trunks. The inlet trunks will be designed to have the same number of elbows. It is possible that we can design this so that the :math:`K_{e_{branch}}` is small by having the branch area larger than the trunk area. The minor loss coefficient associated with the orifices, :math:`K_{e_{outerOrifices}}`, can be obtained from the minor loss equation written for port exit head loss. All of the kinetic energy in the port jet is lost.

The head loss through a port can be expressed in the minor loss equation form.

.. math::
  :label: eq_he_port

  h_{e_P} = \frac{\bar v_{P}^2}{2g}

where the port velocity :math:`\bar v_{P}` is the *contracted* velocity out of the port. We want the head loss to be a function of the manifold velocity. The relationship between port and manifold velocity is given by equation :eq:`Manifold_max_v_no_hl_series`. Substitute equation :eq:`Manifold_max_v_no_hl_series` into equation :eq:`eq_he_port` to obtain an equation that is only a function of the manifold velocity.

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
