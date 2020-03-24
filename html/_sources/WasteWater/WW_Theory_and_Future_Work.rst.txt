.. _title_WasteWater_Theory_and_Future_Work:

*********************************
WasteWater Theory and Future Work
*********************************

Although AguaClara began with a focus on drinking water treatment, we have always been keenly aware that adequate wastewater treatment is absolutely essential to reduce harm to the environment and harm to downstream communities.

One of the core ideas of the AguaClara design process is that reactor geometry and hydraulic design are critical to obtain the target performance. Environmental engineers have tended to focus on the microbiology and chemistry of unit processes and have sometimes neglected the interactions between fluids, particles, and reactor geometry. We hypothesize that it will be possible to significantly improve on the conventional UASB design by inventing a anaerobic digester that accounts for the interactions between fluids, particles, and reactor geometry. Similarly, we hypothesize that it will be possible to dramatically improve the design of ultra low energy atmospheric oxygen transfer into aerobic reactors.

.. _heading_UASB:

Anaerobic Pulsed Bed
============================

Upflow anaerobic settled bed (UASB) are conventionally known as upflow anaerobic sludge blanket reactors. The word "blanket" is frequently used in the field of water and wastewater treatment to refer to a fluidized bed of suspended particles (see floc blanket). Unfortunately that definition is not clearly communicated by the term "blanket" and this has led to confusion of the fundamental mechanisms at play in UASB reactors.

Fluidized bed reactors required inlet and bottom geometry configurations that prevent settled particles from accumulating anywhere on the bottom of the reactor. Many UASB reactors have flat bottoms and the inlets are not designed to ensure continuous resuspension of settled particles. Thus the use of the term  "blanket" for conventional UASB reactors is a misnomer.

UASB reactors typically require hydraulic residence times of x to y hours and have a height of z meters. The result is a maximum upflow velocity of z/y mm/s. This upflow velocity is orders of magnitude lower than the terminal velocity of the particles and thus it is clear that UASB reactors are primarily settled beds of sludge.

The flow distribution through settled sludge is very unlikely to be uniform. The flow is likely to erode a mostly vertical path the shortest distance between the inlet and the top of the settled sludge. There doesn't appear to be any mechanism that would lead to the idealized uniform flow distribution. Thus conventional UASB reactors are evidently plagued by short circuiting with actual hydraulic residence times a fraction of the design value. (Cite literature in support of this hypothesis.) This leads to short-circuiting and formation of preference flow patterns in sludge bed which in turn leads to dead zones in the sludge as well as improper treatment (`Pena, 2006 <https://doi.org/10.1016/j.watres.2005.11.021>`_)

The upflow velocity required to maintain a fully fluidized bed of the anaerobic granules is approximately (cite AguaClara UASB research by Cho, et al. who measured the sedimentation velocity of anaerobic granules) x mm/s. At this velocity the height of the reactor would need to be x m in order to achieve the target hydraulic residence time of y hrs. This is not a practical design for community scale reactors and thus it would be advantageous to invent an alternate system for providing more uniform flow through the solids that contain the microorganisms in a UASB reactor.

Our proposed solution to this mismatch between required upflow velocity for a fluidized bed and target hydraulic residence time is to use a pulsed flow inlet. The pulsed flow will be designed to lift the entire settled bed off of the floor of the UASB reactor so that the influent wastewater is uniformly distributed to the bottom of the reactor. We hypothesize that the settled bed will then break apart and settled into the band of fresh wastewater that is on the bottom of the reactor. With this proposed mechanism it is clear that a critical parameter is the depth of wastewater that should be injected with each pulse. It is likely that this depth of fresh wastewater should be
 - a small fraction of the depth of the UASB (perhaps less than 10% to ensure that no fresh wastewater can jet through the entire UASB in the time that the sludge settled again)
 - large enough to provide a flow passage underneath the lifted bed without requiring flow velocities that are so high that the bed is scoured near the inlet jet. This translates to larger than a minimum ratio of fresh wastewater depth per pulse/inlet spacing.

Research is needed to characterize settled bed behavior under pulsed flow.
 - How does a settled bed form as suspended solids gradually settle for the cases of continuous and pulsed flows?
 - What is the actual hydraulic residence time distribution in the bed for the case of continuous and pulsed flows?
 - What are the failure modes for the pulsed system?
 - What is the optimal pulsed height (volume of pulse/area of reactor)?
 - How does the optimal pulsed height scale inlet spacing and bed depth? It will be difficult to conduct experiments at full scale and thus these experiments will require careful consideration of scaling effects. Full scale validation will be very helpful if we can develop a method.

 All of this research will be aided by using transparent reactor walls to facilitate direct observation of the settled solids.

.. _heading_String_Digester:

String Digester (SD)
============================

Trickling filters are an old wastewater treatment technology that is much more energy efficient than the activated sludge process.

.. todo:: Provide calculations to prove this statement. Find electricity consumption for aeration and convert it to an equivalent height that the wastewater must be pumped



The measured hydraulic residence time for trickling filters is very short. This suggests that with proper design the ASD could be very compact. `Hinton and Stense (1991) <https://www-sciencedirect-com.proxy.library.cornell.edu/science/article/pii/0043135491901179>`_ measured the residence time per unit length to be 30 seconds/meter. Thus for a 4 meter deep trickling filter the residence time would be 120 seconds. If this is accurate, then we may be able to achieve a compact design if we can pack stainless steel cables close together (order 4 mm spacing) AND achieve uniform flow distribution. In addition, `Hinton and Stense (1991) <https://www-sciencedirect-com.proxy.library.cornell.edu/science/article/pii/0043135491901179>`_ used a hydraulic application rate of 4 m/hr (1.1 mm/s). This velocity confirms that a compact, well-designed ASD may be smaller than AguaClara sedimentation tanks that traditionally have operated at 1 mm/s.

Modular plastic trickling filter media are typically manufactured with the `following specific surface areas <http://dx.doi.org/10.2175/106143010X12681059117210>`_:

- 223 :math:`m^2/m^3` as high density
- 138 :math:`m^2/m^3` as medium density
- 100 :math:`m^2/m^3` as low density

Vertical-flow media require an average hydraulic approach velocities greater than 1.8 m/h (0.5 mm/s) to maximize BOD5 removal efficiency. Shallow towers using cross-flow media have used hydraulic approach velocities in the range 0.4 to 1.1 m/h (0.1 to 0.3 mm/s) (`Daigger and Boltz, 2011 <http://dx.doi.org/10.2175/106143010X12681059117210>`_)

`Crine et al. (1990) <https://doi.org/10.2166/wst.1990.0149>`_ found that the wetted area-to-specific-surface-area ratio ranged from 0.2 to 0.6 with the lowest values for high-density random pack trickling filter media. This confirms that conventional trickling filters are unable to efficiently wet all biofilm surfaces and thus the trickling filters must be substantially over-designed (by a factor of 2 to 5) to accommodate this poor wetting efficiency.

If we take the hydraulic approach velocity of 0.5 mm/s and divide by the wetted area-to-specific-surface-area ratio of 0.6 we obtain 0.83 mm/s, a velocity that is comparable to the upflow velocity in an AguaClara sedimentation tank. Thus a well designed String Digester could be quite compact.

.. todo:: Compare with activated sludge tank hydraulic approach velocity (depth/HRT)

There is extensive literature on design of trickling filters for removal of various nutrients and integration into multi-process treatment trains. Control of biofilm thickness seems to be a recurring issue and thus may be an important research area for the String Digester.
