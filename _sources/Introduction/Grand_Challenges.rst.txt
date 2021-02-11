.. _title_Grand Challenges:

****************
Grand Challenges
****************

Introduction
============

We are providing these innovation topics as a continuation of the journey begun by the AguaClara program at Cornell University in 2005. Our goal then and now was to develop improved and new technologies that would be resilient and accessible for the millions of small communities that don't currently have safe water on tap. We recognized the unserved gap between city and household-scale water systems where neither governments nor non governmental organizations had high performing solutions for treating contaminated water sources for municipal water supplies. The technology gap became the motivation for research funded by the National Science Foundation and the United States Environmental Protection Agency and collaborative innovation with a growing list of partner organizations who design/build/operate/train/transfer the technologies to communities. The feedback and learning by doing guides the research process so that we focus on real problems with a high potential for dramatic improvements over existing technologies.

Magnitude of the Challenge
--------------------------

A significant fraction of the global population needs Safe Water on Tap.

* Some three in ten people (2.3 billion) lack access to safe and readily available water at home (or maybe it is 5 in 10…)
* Additional 1.2 billion from population growth gives 3.5 billion need water by 2030
* 267 million people per year!
* 800,000 L/s per year of new installed capacity (assuming 3 mL/s per person)
* Water for 18 New York Cities per year! (new capacity installation rate!)
* Aging infrastructure for cities needs to be rehabilitated or replaced

Motivating Hypotheses
---------------------

1. We can develop new and improved solutions fastest by working as a collaborative community where we share freely what we are learning.
2. The path to providing more communities with sustainable Safe Water on Tap is to discover the physics of the core drinking water treatment technologies so that we can both begin to optimize the design of those technologies and invent new technologies.
3. Innovation is accelerated by rapidly deploying the new technologies, evaluating their performance, learning from the plant operators, and then by using that feedback to guide research.

The Cost of Empirical Design
----------------------------

The current design process for water treatment plant relies on previous designs and a fragmented design approach. Each unit process is treated as independent without a full ability to account for interdependencies. There is no ability to optimize the design and very little ability to predict the impact of changes in raw water quality.

* Pilot studies are required to assess treatability.
* No design integration and much less optimization between processes. For example, we don't know how to optimize the design of a flocculator to minimize the filtered water turbidity.
* Few physics-based equations that can predict the performance of unit processes given the raw water characteristics.


Research Topics
---------------
The scope of research needed to save our planet and improve the well-being of our neighbors extends well beyond our focus on water. The current research topics represents what we have identified as critical gaps in our knowledge that have the potential to revolution the constraints that we have assumed over the past century of drinking water and wastewater treatment. The research topics will expand as more universities join this effort to rethink, reimagine, and then reinvent how we manage water and wastewater towns and villages.

Drinking Water Treatment
========================

The potential to make a dramatic improvement in the quality of life of communities will guide our journey. The following research questions are the outgrowth of research and innovation by the AguaClara Cornell program. Although the AguaClara program invented numerous technologies and contributed to a new understanding of the physics of drinking water treatment, there are still many unanswered questions.

* Why is reducing the turbidity to less than 0.01 NTU not currently possible for most surface water treatment plants that rely on flocculation, sedimentation and sand filtration? Or stated another way, what controls the particle removal efficiency of surface water treatment plants?
* How can we take measurements of raw water quality and use that to optimize the design of a water treatment plant? This will require creating the models that describe the physics of each unit process and that is a recurring theme of the research introduced below.
* How can we invent new and improved technologies that enable communities to reliably produce high quality drinking water without needing to rely on expensive, expendable proprietary components.

Fractal Floc Model
------------------

The fractal floc model (FFM) will describe floc properties (density, bond strength, and surface properties) as a function of composition and floc diameter. The FFM will provide the missing connection between raw water quality and design and performance of treatment processes.
The FFM will build the average floc in a series of ordered steps that capture the order in which these processes occur in flocculation. The first step is adsorption of dissolved species (DS) to the coagulant nanoparticles (CNP) to form a CNP-DS aggregate. The CNP-DS aggregates then attaches to the primary particles (PP) in the suspension to form PP-CNP-DS aggregates. The PP-CNP-DS aggregates then combine to form flocs.

The primary particles could include powdered activated carbon (PAC) or biochar that is added to aid in the removal of dissolved species. In that case the dissolved species will partition between adsorption to the PAC or biochar and to the coagulant nanoparticles.

The floc properties calculated by the FFM will enable prediction of the terminal size and concentration of flocs in the Fluidized Floc Primary Filter, the head loss per pore in the Granular Media Secondary Filter, and the optimal coagulant dose. The FFM will be a core component of unit process models because the floc properties must be understood in order to model the floc behavior.

Kevin Sarmiento (M.S. candidate at Cornell University) is currently taking the lead on developing the FFM.

Flocculation
------------

The `AguaClara Hydraulic Flocculation Model <https://www.liebertpub.com/doi/full/10.1089/ees.2017.0332>`_ is the first flocculation model that can predict the relationship between coagulant dose, flocculator design, and settled water turbidity. That model has been `extended to include the effects of humic acid <https://www.liebertpub.com/doi/abs/10.1089/ees.2018.0405>`_ and given that the physics-based model explains both clay and humic acid it would seem reasonable to expect that other particulate and dissolved substances could be added to the model.

The flocculation model opens up many opportunities for further research. The model does not yet predict the floc size distribution. We hypothesize that the floc size distribution is set by floc aggregation that is controlled by fluid deformation that transports flocs toward collisions, by boundary layers that develop around flocs that are rotating in the deforming fluid, and by the ratio of shear forces to coagulant nanoparticle bond strength that determines the likelihood of attachment after a collision between flocs.

An enabling measurement will be particle size and count in a flocculating suspension. Particle counters are frequently used on high quality water and are not able to measure particles in the concentrated suspensions encountered in flocculators. There are at least two options for measuring the floc size distribution in the flocculation process.

1. The AguaClara Cornell program developed an `image based system of floc sizing <https://www.liebertpub.com/doi/10.1089/ees.2015.0311>`_ that uses a 1 cm square sample cell and that uses image analysis to eliminate flocs that are blurry and hence aren't in the target analysis volume.
2. The floc suspension could be diluted and then sent through a commercial particle counter.

There are challenges associated with both strategies and a review of the literature may uncover additional options.

Fluidized Floc Primary Filtration
---------------------------------

AguaClara invented the zero settled sludge sedimentation tank and the required `geometry to maintain a stable fluidized floc suspension <https://ascelibrary.org/doi/abs/10.1061/%28ASCE%29EE.1943-7870.0000773>`_ that provides primary filtration. The addition of primary filtration in clarifiers improves their `particle removal efficiency <https://iwaponline.com/aqua/article/59/5/312/29069/Parameters-affecting-steady-state-floc-blanket>`_, eliminates the need for mechanized sludge removal, and dramatically reduces mean flows that commonly result in poor floc capture. Although it is known that the primary filtration process enhances particle removal, the physics of primary filtration have been elusive and are currently an AguaClara Cornell NSF research project. Experiments conducted starting in January of 2021 suggest that fluidized flocs have a finite capacity to capture particles. That insight paves the way for a new research project to optimize the design and operation of primary filters and answer a new series of questions.

1. Why do flocs in the primary filter have a finite capacity to capture incoming particles and flocs?
2. Could flocs that have reached their capacity be rejuvenated? This has the potential to dramatically improve the particle capture efficiency of the primary filter.
3. What is the optimal floc size distribution in the flocculator effluent to achieve the lowest concentration of primary particles exiting the sedimentation tank?
4. How could flocs that have reached their full capacity be selectively removed from the primary filter?

Sedimentation
-------------

Although we don't currently see research into plate settlers as a priority, it is likely that we will circle around to research to determine the optimal design of plate settlers to maximize performance of the subsequent granular media filtration. The design of plate settlers is a function of the properties of the flocs given the raw water composition and the amendments added for treatment. AguaClara experience with highly colored, low turbidity water at Gracias, Honduras indicates that surface waters with those characteristics produce low density flocs that are difficult to remove by sedimentation. The minimum density of flocs given the raw water characteristic will be the critical design for sedimentation tanks and will determine if amendments to increase floc density are required for efficient gravity-based separation.

Granular Media Secondary Filtration
-----------------------------------
The goal of this research is to develop a physics-based model of depth filtration of fractal flocs. The depth filtration model (DFM) will characterize the active filtration zone that migrates downstream as fractal flocs are intercepted at flow constrictions and as the deposition constrictions reach their minimum diameter. The proposed DFM will connect the interactions between pore geometry evolution caused by fractal floc deposition to the changing flow pattern that causes an increase in interception and an increase in fluid drag on flocs that ultimately prevents attachment when the pore reaches its minimum size. Laboratory experiments will be conducted to test hypotheses and guide the model development.

The DFM will be used to optimize the design and operation of rapid sand filters that continue to be the most common final particle removal process in drinking water treatment plants. The model will be used to create optimized designs of sand filters used in sustainable, gravity-powered, drinking water treatment facilities constructed through collaboration with AguaClara implementation partners in Honduras, Nicaragua, Colombia. Feedback to the design process will be provided from monitoring community-scale treatment plants and from informal conversations with engineers, technicians, and plant operators.

Research questions for granular media filtration:

1. Is the ratio of coagulant nanoparticle bond strength to the drag force on a primary particle a reasonable characterization of the ability of a flow constriction to capture a primary particle?
2. Is the velocity distribution at the entrance to a forming flow constriction reasonably modeled as uniform?
3. How much of a change in flow can a fully formed flow constriction withstand before the fluid forces exceed its strength and how does the constriction fail? Specifically, what size flocs do ruptured flow constrictions shed?
4. What size of flocs is optimal for producing partially formed flow constrictions that are then able to efficiently capture primary particles?

Disinfection
------------
After more than 100 years of chlorination it may be time to review the public health trade-off compared with alternatives that don't have the negative health impacts associated with chlorine. The water treatment industry has long assumed that chlorination is an essential barrier required to fully protect public health. An analysis of the underlying assumptions for requiring a chlorine residual reveals that the residual would only provide protection for recontamination events with a maximum carbon concentration of about 1 mg/L. Thus it is unlikely that a chlorine residual would provide protection against recontamination. A pathogen by pathogen analysis of the protection provided by chlorine vs the protection provided by the particle removal processes suggests that chlorine is most effective against organisms that have high infective doses and thus the particle removal processes may already provide sufficient protection. The challenge of taking on the emotionally charged questions associated with chlorination will require a thoughtful strategy and may not be amenable to scientific research.

Wastewater Treatment
====================

Although AguaClara began with a focus on drinking water treatment, we have always been keenly aware that adequate wastewater treatment is absolutely essential to reduce harm to the environment and harm to downstream communities.

One of the core ideas of the AguaClara design process is that reactor geometry and hydraulic design are critical to obtain the target performance. Environmental engineers have tended to focus on the microbiology and chemistry of unit processes and have sometimes neglected the interactions between fluids, particles, and reactor geometry. We hypothesize that it will be possible to significantly improve on the conventional UASB design by inventing a anaerobic digester that accounts for the interactions between fluids, particles, and reactor geometry. Similarly, we hypothesize that it will be possible to dramatically improve the design of ultra low energy atmospheric oxygen transfer into aerobic reactors.

Wastewater treatment generally requires more land, capital, and energy than drinking water treatment and thus is out of reach for most towns and villages. The result is that the majority of human waste reaches the environment with little or no treatment. Drinking water treatment is currently beyond the reach of many towns and villages and wastewater treatment isn't even on the horizon. Thus we need innovations that are better by a factor of 10 or more. The treatment technologies must have retention times measured in minutes rather than hours or days and must also reduce moving parts and reduce energy consumption. Thus critical questions are:

1. why are wastewater treatment processes so slow?
2. what is the nature of the rate limiting step?
3. how could the rate be dramatically increased?

.. _heading_Anaerobic_Pulsed_Bed:

Anaerobic Pulsed Bed
====================

Anaerobic digestion has the advantage of not requiring aeration and the disadvantage of requiring long residence times. Presumably it is the bacteria that require a long residence time and not the water and thus these residence times must be decoupled by using sedimentation or a fixed film process.

Upflow Anaerobic Sludge Blanket digestors that don't use a recycle line have an upflow velocity that is far lower than is required to fluidize the bed of granules that form. Flow through the resulting settled bed of sludge must be highly nonuniform and the result is that much of the settled bed is likely contributing little to the treatment process.

Flow uniformity and contact with all of the solids could be achieved with a fluidized bed. The velocity required for a fluidized bed would require a very tall reactor given the assumed requirements for residence time. Presumably the residence time requirement is based on the poor flow distribution in the settled sludge. Nonetheless, for reasonable depth reactors it will be difficult to operate a once through fluidized bed.

The hydraulic solution to this problem is to use pulsed flow with a pulse having a volume equal to perhaps 1-5 cm of depth in the reactor. The pulse will completely lift the settled bed of sludge and the sludge will then fall through the water column. This lift and drop cycle is expected to have much more uniform flow of water through the sludge bed then would be achieved by a stagnant bed that would rapidly develop preferential flow paths.

Upflow anaerobic settled bed (UASB) are conventionally known as upflow anaerobic sludge blanket reactors. The word "blanket" is frequently used in the field of water and wastewater treatment to refer to a fluidized bed of suspended particles (see floc blanket). Unfortunately that definition is not clearly communicated by the term "blanket" and this has led to confusion of the fundamental mechanisms at play in UASB reactors.

Fluidized bed reactors required inlet and bottom geometry configurations that prevent settled particles from accumulating anywhere on the bottom of the reactor. Many UASB reactors have flat bottoms and the inlets are not designed to ensure continuous resuspension of settled particles. Thus conventional UASB reactors are often not fluidized beds and thus don't have the mass transfer efficiencies that they could have.

UASB reactors typically require hydraulic residence times hours and have a height of 4 or more meters. The result is a maximum upflow velocity that is orders of magnitude lower than the terminal velocity of the granules and thus it is clear that UASB reactors are primarily settled beds of stagnant sludge that is doing little to aid in the treatment of the wastewater.

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

All of this research will be aided by using transparent reactor walls to facilitate direct observation of the settled solids. Research on this topic is currently underway by Ruth Richardson and the AguaClara Cornell team with an EPA P3 grant.

.. _heading_String_Digester:

Aerobic String Digester (ASD)
=============================

Aerobic digestion requires transfer of oxygen to the bacteria that then oxidize the waste. The broad goal is to reduce the hydraulic residence time by having efficient transfer of nutrients from the flowing water to the microorganisms. If we rely on diffusion for the mass transport of oxygen, then the thickness of the water must be order 1 mm. The string digestor represents the obvious evolution from trickling filters to the appropriate length scale that will in turn allow the minimum reactor volume.

The strings will hang vertically and be spaced a few mm apart. The spacing is expected to be close to the typical water droplet diameter to ensure that once the water droplets attach to a string, that they follow the string the whole way to the bottom of the reactor.
Trickling filters are an old wastewater treatment technology that is much more energy efficient than the activated sludge process.

The measured hydraulic residence time for trickling filters is very short. This suggests that with proper design the ASD could be very compact. `Hinton and Stense (1991) <https://www-sciencedirect-com.proxy.library.cornell.edu/science/article/pii/0043135491901179>`_ measured the residence time per unit length to be 30 seconds/meter. Thus for a 4 meter deep trickling filter the residence time would be 120 seconds. If this is accurate, then we may be able to achieve a compact design if we can pack stainless steel cables close together (order 4 mm spacing) AND achieve uniform flow distribution. In addition, `Hinton and Stense (1991) <https://www-sciencedirect-com.proxy.library.cornell.edu/science/article/pii/0043135491901179>`_ used a hydraulic application rate of 4 m/hr (1.1 mm/s). This velocity confirms that a compact, well-designed ASD may be smaller than AguaClara sedimentation tanks that traditionally have operated at 1 mm/s.

Modular plastic trickling filter media are typically manufactured with the `following specific surface areas <https://pubmed.ncbi.nlm.nih.gov/21657190/>`_:

- 223 :math:`m^2/m^3` as high density
- 138 :math:`m^2/m^3` as medium density
- 100 :math:`m^2/m^3` as low density

Vertical-flow media require an average hydraulic approach velocities greater than 1.8 m/h (0.5 mm/s) to maximize BOD5 removal efficiency. Shallow towers using cross-flow media have used hydraulic approach velocities in the range 0.4 to 1.1 m/h (0.1 to 0.3 mm/s) (`Daigger and Boltz, 2011 <https://pubmed.ncbi.nlm.nih.gov/21657190/>`_)

`Crine et al. (1990) <https://doi.org/10.2166/wst.1990.0149>`_ found that the wetted area-to-specific-surface-area ratio ranged from 0.2 to 0.6 with the lowest values for high-density random pack trickling filter media. This confirms that conventional trickling filters are unable to efficiently wet all biofilm surfaces and thus the trickling filters must be substantially over-designed (by a factor of 2 to 5) to accommodate this poor wetting efficiency.

If we take the hydraulic approach velocity of 0.5 mm/s and divide by the wetted area-to-specific-surface-area ratio of 0.6 we obtain 0.83 mm/s, a velocity that is comparable to the upflow velocity in an AguaClara sedimentation tank. Thus a well designed String Digester could be quite compact.

.. todo:: Compare with activated sludge tank hydraulic approach velocity (depth/HRT)

There is extensive literature on design of trickling filters for removal of various nutrients and integration into multi-process treatment trains. Control of biofilm thickness seems to be a recurring issue and thus may be an important research area for the Aerobic String Digester.
