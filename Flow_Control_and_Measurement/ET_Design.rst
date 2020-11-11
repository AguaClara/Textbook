.. _title_entrance_tank_design:

**************************************
Entrance Tank Design
**************************************

The water treatment plant must be protected from potentially damaging materials that could be carried from the watershed to the plant by the water. Typically there will be a large opening trash rack at the water source to prevent damage to the transmission line that carries water to the plant. There may also be a small sedimentation tank to remove sand and gravel before the water enters the transmission line. The trash rack and removal of sand and gravel is important for protection of the water treatment plant, but these protections are generally not sufficient. Steep mountain streams often overwhelm the sand and gravel removal system during storm events and thus depending on the watershed characteristics additional protection is required at the water treatment plant.

The specific design characteristics of a water treatment plant dictate the potential failure modes and hence the required protection. Failure modes and

The entrance tank has multiple functions in a drinking water treatment plant.

1. remove air bubbles to reduce splashing, turbulence, and unsteady motion of the chemical feed surface tracking lever system
1. remove grit to prevent grit accumulation in the flocculator
1. remove leaves and other debris to prevent clogging of the diffusers in the sedimentation tank inlet
1. dissipate kinetic energy of the water prior to facilitate accurate measurement of the water level used for flow measurement
1. measure the flow rate so that operators can make adjustments to the incoming flow rate and respond to changes in water demand
1. inject the coagulant and any other amendments required for flocculation

Trash Rack Design
===============================

The trash rack is specifically designed to remove low density debris that could easily be carried through the plant and clog any small flow passages. In an AguaClara plant there are critical flow passages in the sedimentation tank inlet manifold diffusers and in the flow injection system in the stacked rapid sand filters. The inlet manifold diffusers have flared nozzles with a minimum dimension that currently has a minimum value of about 4 mm. This sets a requirement that the opening dimension for the trash rack be less than the opening size of the inlet manifold nozzles.

The minimum trash rack area is set by a goal of minimizing head loss through the plant while maintaining a trash rack size that is reasonably compact. We recommend that the trash rack be designed to reach a terminal head loss of 5 cm when it is 90% clogged. The design follows directly from that constraint. The guiding equation is the orifice equation with the simple addition of the fractions of the area that is actually available for the water to flow through the trash rack. The area is reduced by the porosity, the vena contracta, and the clogging.

.. math::
   :label: trashrack_flow

   Q = (1-\Pi_{clogged})\Pi_{vc} \phi A_{trashrack}\sqrt{2gh}

where :math:`\phi_{trashrack}` is the fraction of clean trash rack that is open, :math:`\Pi_{vc}` is the vena contracta coefficient, :math:`\Pi_{clogged}` is the clogged fraction of the trash rack. The ideal trash rack has a high porosity and a large vena contracta coefficient. The vena contracta coefficient is set by the geometry of the entrance into the opening through the trash rack. If the entrance has a sharp edge, then the vena contract coefficient will have a value of approximately 0.62. If the entrance is rounded then the vena contracta could approach 1.0. Thus the idea trash rack will have rounded openings.

Solve for the area of the trash rack

.. math::
   :label: trashrack_area

   A_{trashrack} = \frac{Q}{(1-\Pi_{clogged})\Pi_{vc} \phi \sqrt{2gh}}

Set the fraction clogged to between 80 and 90%. Vena contracta coefficient is 0.62 for sharp edged orifices and could be 1 for round wire.
Porosity varies widely depending on the fabrication method.
For AguaClara plants recommend a head loss of 5 cm max.

Also of interest is the effective velocity taking into account the whole area of the trash rack.

.. math::
   :label: trashrack_velocity

   v_{trashrack} = \frac{Q}{A_{trashrack} } = (1-\Pi_{clogged})\Pi_{vc} \phi \sqrt{2gh}

The trash rack characteristic velocity is 50 mm/s for 50% porosity, 90% clogged, vena contracta of 1 and a maximum head loss of 5 cm.
