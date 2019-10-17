.. _title_hydraulics_intro:

********************************************
Hydraulics Introduction
********************************************

The hydraulic controls provide the basis for efficient and robust water treatment plant operation. Water must move through unit processes and between unit processes and the flow passages must be designed to meet various constraints. One constraint is that water that is carrying a significant amount of sediment (flocculator and sedimentation tank inlet) must have sufficient velocity and turbulence levels to minimize sedimentation.  A more challenging constraint is that the flow must be divided equally between parallel processes. Flow distribution through parallel paths is a key hydraulic design constraint for all municipal scale water treatment plants. The parallel path constraint only goes away for laboratory scale processes where there is a single tube settler and a filter with a single layer of sand. A schematic illustrating the electrical circuit analogy is shown in :numref:`_figure_circuit`.

Municipal water treatment plants

.. _figure_circuit:

.. figure:: Images/circuit.png
    :width: 400px
    :align: center
    :alt: Sedimentation tank flow circuit

    The flow through a sedimentation tank is analogous to an electrical circuit with wires and resistors. Identical resistors in parallel paths help improve flow distribution between the paths. Differences in piezometric head (think voltage) in the manifolds that connect to multiple parallel paths.



Inlet Manifold Flow Distribution
================================

There is disagreement in the literature about the physics of manifolds. One school of thought postulates that the flow out of the ports exiting a manifold are controlled by the total energy of the flow inside the manifold. The other school of thought postulates that the flow of water out of the ports is controlled by the difference in piezometric head between the manifold and the receiving reservoir. These two approaches are mutually exclusive and make completely different predictions about how manifolds will perform especially for the case where head loss in the manifold is small compared with the pressure recovery caused by the gradual flow expansion in the manifold.

Fortunately it is relatively easy to check the physics to see which approach is correct. A venturi (gradual flow contraction in a pipe) is used to generate a low pressure region in a pipe by converting pressure into kinetic energy. Venturis can be used to generate low pressure inside the pipe and then pull fluid **into** the pipe even though the total energy of the fluid in the pipe far exceeds the energy of the fluid that was outside of the pipe! This proves that flow out of a manifold is due to the difference in piezometric head and NOT due to the difference in total energy.

If manifolds were built using pitot type exits with the exit facing upstream and into the flow of the fluid then the exit from the manifold would be based on the total energy. The manifolds that we use in water treatment plants do not have pitot tube style ports and thus our analysis of manifolds is based on piezometric head.

Flow distribution from ports exiting a manifold is controlled by the change in piezometric head inside the manifold and the change in piezometric head as the water exits through a port. The reason that the flow from each port is not identical is because of changes in piezometric head in the manifold. These changes are caused by major losses due to shear on the manifold walls and due to pressure recovery as the velocity in the manifold decreases. The control volume is shown in :numref:`_figure_inlet_manifold`

.. math::
   :label: energy_cv_manifold

    \frac{p_{M_1}}{\rho g}+z_{M_1}+\frac{\bar v_{M_1}^2}{2 g}=\frac{p_{M_n}}{\rho g}+z_{M_n}+\frac{\bar v_{M_n}^2}{2g} + h_{L}

The sum of the pressure and elevation term is the piezometric head, :math:`\Psi`. Fluid will move in the direction of decreasing piezometric head. Note that fluid does NOT always move from high pressure to low pressure nor does it always move from high elevation to low elevation. You can prove this to yourself by placing a vertical pipe in a swimming pool!

.. math::
   :label: piezometric_head_defined

    \Psi = \frac{p}{\rho g}+z

The energy control volume equation :eq:`energy_cv_manifold` can be simplified with the definition of piezometric head (equation :eq:`piezometric_head_defined`).

.. math::
   :label: piezometric_cv_manifold

    \Psi_{M_1}+\frac{\bar v_{M_1}^2}{2 g}=\Psi_{M_n}+\frac{\bar v_{M_n}^2}{2 g}+h_{L}

The change in piezometric head is the important parameter and is given by

.. math::
   :label: delta_piezometric_cv_manifold

    \Delta\Psi_M = \frac{\bar v_{M_1}^{2}-\bar v_{M_n}^{2}}{2 g} - h_{L}

.. _figure_inlet_manifold:

.. figure:: Images/inlet_manifold.png
    :width: 400px
    :align: center
    :alt: Sedimentation tank flow circuit

    The piezometric head can either increase due to conversion of kinetic energy to pressure or the piezometric head can decrease due to major losses.

For short :math:`f\frac{L}{d}<<1`, straight (minor loss coefficient = 0), inlet manifolds the change in piezometric head, :math:`\Delta\Psi_M` is equal the initial velocity head.

.. math::
   :label: delta_piezometric_is_velocity_head

    \Delta\Psi_M = \frac{\bar v_{M_1}^{2}}{2 g}

To simplify analysis we assume the middle port gets the average flow (this isn’t quite right because the velocity is squared) and the average piezometric head, :math:`\bar \Psi_M`. The first port has mean piezometric head – ½ delta piezometric head and the last port has an increase in the piezometric head.

.. math::
   :label: Piezo_ports

    \Psi_{M_1} = \bar \Psi_{M} - \frac{1}{2}\Delta \Psi_M

    \Psi_{M_n} = \bar \Psi_{M} + \frac{1}{2}\Delta \Psi_M

where the piezometric head at each port is also proportional to the port velocity squared. A design constraint for a manifold is the target ratio of flow from port one, :math:`Q_{P_1}`, divided by the flow from the last port, :math:`Q_{P_n}`.


.. math::
   :label: Pi_Q_ports

    \Pi_{Q} = \frac{Q_{P_1}}{Q_{P_n}}=\sqrt{\frac{\Psi_{M_1}}{\Psi_{M_n}}}

Substitute equations :eq:`Piezo_ports` into equation :eq:`Pi_Q_ports` to obtain the relationship between piezometric head and the flow distribution ratio.

.. math::
   :label: Pi_Q_ports2

    \Pi_{Q}^2 = \frac{\bar \Psi_{M} - \frac{1}{2}\Delta \Psi_M}{\bar \Psi_{M} + \frac{1}{2}\Delta \Psi_M}

This equation shows that the flow distribution will approach 1 when :math:`\bar \Psi_{M}` is much larger than :math:`\Delta \Psi_M`. This can be achieved by having the manifold velocities be small compared with the port velocities. Solving for the change in piezometric head in the manifold we obtain the relationship between change in piezometric head and uniformity of port flow.

.. math::
   :label: Pi_Q_ports3

    \Delta \Psi_M = 2\bar \Psi_{M}\frac{1 - \Pi_{Q}^2}{\Pi_{Q}^2 + 1}

The energy equation also yields an equation for the change in piezometric head (see equation :eq:`delta_piezometric_cv_manifold`) and we can equate those two to

.. math::
   :label: Energy_and_Pi_Q

    \frac{\bar v_{M_1}^{2}-\bar v_{M_n}^{2}}{2 g} - h_{L} = 2\bar \Psi_{M}\frac{1 - \Pi_{Q}^2}{\Pi_{Q}^2 + 1}


If head loss in the manifold is small, then we have

.. math::
   :label: Energy_and_Pi_Q_no_manifold_hl

    \frac{\bar v_{M_1}^{2}}{2 g} = 2\bar \Psi_{M}\frac{1 - \Pi_{Q}^2}{\Pi_{Q}^2 + 1}

The average piezometric head in the manifold is also influenced by any head loss that is in series with the port head loss. Here we assume that the piezometric head datum is in the receiving tank. If the receiving tank is a filter, then there could be head loss through the sand on the way to the outlet of the filter. This head loss in series will help provide more uniform flow out of the manifold if there aren't any paths for flow to blend between the first and last ports. This is the case for division of flow between sand layers in a stacked rapid sand filter where the head loss through the sand plays a key role in helping to divide the flow evenly between the 6 layers of sand. The average piezometric head in the manifold, :math:`\bar \Psi_{M}` is equal to the head from the port kinetic energy plus any downstream head loss.

.. math::
   :label: Manifold_piezometric_head_port_KE_and_HL

    \bar \Psi_M \cong \frac{\bar v_{P}^{2}}{2 g} + h_{l_{series}} \cong h_{e_{port}} + h_{l_{series}}


The port head loss is given by :math:`\bar v_{P} = \sqrt{2gh_e}` where the port velocity is the true contracted velocity if there is a *vena contracta*. If the head loss in series, :math:`h_{l_{series}}`, is significant, then equations :eq:`Energy_and_Pi_Q_no_manifold_hl` and :eq:`Manifold_piezometric_head_port_KE_and_HL` combine to produce

.. math::
   :label: Manifold_max_v_with_hl_series

    \bar v_{M_1}= 2\sqrt{g (h_{e_{port}} + h_{l_{series}})\frac{1 - \Pi_{Q}^2}{\Pi_{Q}^2 + 1}}

If their is no additional head loss in series to improve flow distribution, then equation :eq:`Manifold_max_v_with_hl_series` simplifies to

.. math::
   :label: Manifold_max_v_no_hl_series

    \frac{\bar v_{P}}{\bar v_{M_1}} = \sqrt{\frac{\Pi_{Q}^2 + 1}{2(1 - \Pi_{Q}^2)}}

Equation :eq:`Manifold_max_v_no_hl_series` can be used to determine the required diameter of inlet manifolds in sedimentation tanks or to determine the required port velocity for the backwash manifold in the StaRS filters.

Inlet Channel with Rectangular Weir Flow Distribution
=====================================================

In plants with flow rates large enough to use open stacked rapid sand filters the settled water is delivered to those filters through an open channel. The water exits the channel by flowing across a rectangular weir. As is the case in a manifold pipe the water in the channel is decelerating and thus the piezometric head is increasing in the direction of flow. This increase in piezometric head is equivalent to the increase in the depth of water in the channel. This increase in water depth results in more water flowing across the final weir exiting the channel.

The flow across the weirs into the filter inlet boxes is complicated by several factors. First, there must be a *vena contracta* as the flow changes direction to flow across the weir and thus the :math:`90^{\circ}` *vena contracta* coefficient should enter the equations. Second, the weirs as they are fabricated are neither sharp nor broad and thus it isn't clear which equations are best suited. Sharp crested weirs are known to have a reduced depth of flow above the weir due to the acceleration of water approaching the weir and this effect is normally ignored and then thrown into the weir coefficient. Given that our weirs do not have a rounded upstream edge required by broad crested weirs we will use the sharp crested weir equation.

Side Exit Sharp Crested Weir
----------------------------

.. math::
   :label: Sharp_weir_Q_of_channel_depth

   Q = \Pi_{vc}\frac{2}{3} \sqrt{2g} w \left(H_{channel}\right)^\frac{3}{2}


where :math:`H_{channel}` is the height of the water in the channel above the top of the weir. (see equation 10.30 in Fundamentals of Fluid Mechanics, Fifth Edition by Munson, Young, and Okiishi)

Inlet Channel Design for Equal Filter Flow
------------------------------------------

We will simplify this manifold problem by assuming that the average water height in the channel above the weirs corresponds to the average flow across the weirs and that the upstream depth is decreased by 1/2 of the channel velocity head and the downstream depth is increased by 1/2 the channel velocity head.



The ratio of flows from the first filter and the last filter in the channel is given by

.. math::
   :label: Sharp_weir_flow_ratio_messy

   \Pi_{Q_{weir}} = \frac{Q_{Filter_1}}{Q_{Filter_n}} = \frac{\Pi_{vc}\frac{2}{3} \sqrt{2g} w \left(\bar H_{channel} - \frac{\bar v_{M_1}^2}{4g}\right)^\frac{3}{2}}{\Pi_{vc}\frac{2}{3} \sqrt{2g} w \left(\bar H_{channel} + \frac{\bar v_{M_1}^2}{4g}\right)^\frac{3}{2}}


where :math:`\bar H_{channel}` is the average height of water in the channel relative to the top of the weir. Equation :eq:`Sharp_weir_flow_ratio_messy` simplifies to

.. math::
   :label: Sharp_weir_flow_ratio1

   \Pi_{Q_{weir}} = \frac{ \left(\bar H_{channel} - \frac{\bar v_{M_1}^2}{4g}\right)^\frac{3}{2}}{\left(\bar H_{channel} + \frac{\bar v_{M_1}^2}{4g}\right)^\frac{3}{2}}

The slower the velocity in the channel the more uniform the flow distribution will be between the filters. Solve for the velocity in the

.. math::
   :label: Sharp_weir_flow_ratio2

    \bar H_{channel}\Pi_{Q_{weir}}^\frac{2}{3} + \frac{\bar v_{M_1}^2}{4g}\Pi_{Q_{weir}}^\frac{2}{3}= { \bar H_{channel} - \frac{\bar v_{M_1}^2}{4g}}

Simplify more!

.. math::
   :label: Inlet_Channel_v_max

     \bar v_{M_1} =  2\sqrt{g\bar H_{channel}\frac{\left(1-\Pi_{Q_{weir}}^\frac{2}{3}\right)}{\left(\Pi_{Q_{weir}}^\frac{2}{3} + 1\right)}}

Backwash Weir Slot Design
-------------------------

The goal of the backwash weir slot is to provide close to the design flow rate to a filter while it is in backwash mode. To accomplish this the wide gate weir is opened and the weir slot controls the flow of water into the inlet box. During backwash the water level in the inlet box is much lower and thus the backwash weir slot can extend deep into the box. The design constraint for this slot is that it must deliver the design flow when the water level in the inlet channel is at the design flow height and it must deliver at least 80% of the design flow  when their is no flow going to any of the other filters. The difference in water level between the two cases is :math:`H_{channel}` because this is the height of water flowing over the wide weir at the design flow rate. The height of the slot, :math:`H_{slot}`, is measured relative to the design flow water level in the inlet channel.

This design will result in more water available for backwash than is absolutely needed and if it turns out that too much water is directed to this filter than the bottom of the slot can be elevated by adding a few stop logs.

The equation is based on the sharp crested weir (Equation :eq:`Sharp_weir_Q_of_channel_depth`). The head loss through the gate weir should be subtracted from both the top and bottom terms

.. math::
   :label: Flow_ratio_backwash

     \Pi_{Q_{BW}} = \frac{Q_{BW_{min}}}{Q_{BW_{max}}} = \frac{\Pi_{vc}\frac{2}{3} \sqrt{2g} w \left(H_{slot} - H_{channel} - HL_{Gate}\right)^\frac{3}{2}}{\Pi_{vc}\frac{2}{3} \sqrt{2g} w \left(H_{slot}- HL_{Gate}\right)^\frac{3}{2}}

Simplify and solve for :math:`H_{slot}`.

.. math::
   :label: Flow_ratio_backwash

     H_{slot} = \frac{H_{channel}}{1-\Pi_{Q_{BW}}^\frac{2}{3}} + HL_{Gate}
