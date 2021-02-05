.. _title_Grand Challenges:

****************
Grand Challenges
****************

.. _heading_A_Different_Kind_of_Textbook:

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

Motivating hypotheses
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

The [AguaClara Hydraulic Flocculation Model](https://www.liebertpub.com/doi/full/10.1089/ees.2017.0332) is the first flocculation model that can predict the relationship between coagulant dose, flocculator design, and settled water turbidity. That model has been [extended to include the effects of humic acid](https://www.liebertpub.com/doi/abs/10.1089/ees.2018.0405) and given that the physics-based model explains both clay and humic acid it would seem reasonable to expect that other particulate and dissolved substances could be added to the model.

The flocculation model opens up many opportunities for further research. The model does not yet predict the floc size distribution. We hypothesize that the floc size distribution is set by floc aggregation that is controlled by fluid deformation that transports flocs toward collisions, by boundary layers that develop around flocs that are rotating in the deforming fluid, and by the ratio of shear forces to coagulant nanoparticle bond strength that determines the likelihood of attachment after a collision between flocs.

An enabling measurement will be particle size and count in a flocculating suspension. Particle counters are frequently used on high quality water and are not able to measure particles in the concentrated suspensions encountered in flocculators. There are at least two options for measuring the floc size distribution in the flocculation process.
1. The AguaClara Cornell program developed an [image based system of floc sizing](https://www.liebertpub.com/doi/10.1089/ees.2015.0311) that uses a 1 cm square sample cell and that uses image analysis to eliminate flocs that are blurry and hence aren't in the target analysis volume.
2. The floc suspension could be diluted and then sent through a commercial particle counter.
There are challenges associated with both both strategies and a review of the literature may uncover additional options.

Fluidized Floc Primary Filtration
---------------------------------

AguaClara invented the zero settled sludge sedimentation tank and the required `geometry to maintain a stable fluidized floc suspension<https://ascelibrary.org/doi/abs/10.1061/%28ASCE%29EE.1943-7870.0000773>`_ that provides primary filtration. The addition of primary filtration in clarifiers improves their `particle removal efficiency<https://iwaponline.com/aqua/article/59/5/312/29069/Parameters-affecting-steady-state-floc-blanket>`_, eliminates the need for mechanized sludge removal, and dramatically reduces mean flows that commonly result in poor floc capture. Although it is known that the primary filtration process enhances particle removal, the physics of primary filtration have been elusive and are currently an AguaClara Cornell NSF research project. Experiments conducted starting in January of 2021 suggest that fluidized flocs have a finite capacity to capture particles. That insight paves the way for a new research project to optimize the design and operation of primary filters and answer a new series of questions.
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
After more than 100 years of chlorination it may be time to review the public health trade-off compared with alternatives that don't have the negative health impacts associated with chlorine.
The water treatment industry has long assumed that chlorination is an essential barrier required to fully protect public health. An analysis of the underlying assumptions for requiring a chlorine residual reveals that the residual would only provide protection for recontamination events with a maximum carbon concentration of about 1 mg/L. Thus it is unlikely that a chlorine residual would provide protection against recontamination. A pathogen by pathogen analysis of the protection provided by chlorine vs the protection provided by the particle removal processes suggests that chlorine is most effective against organisms that have high infective doses and thus the particle removal processes may already provide sufficient protection. The challenge of taking on the emotionally charged questions associated with chlorination will require a thoughtful strategy and may not be amenable to scientific research.

Wastewater Treatment
====================

Wastewater treatment generally requires more land, capital, and energy than drinking water treatment and thus is out of reach for most towns and villages. The result is that the majority of human waste reaches the environment with little or no treatment. Drinking water treatment is currently beyond the reach of many towns and villages and wastewater treatment isn't even on the horizon. Thus we need innovations that are better by a factor of 10 or more. The treatment technologies must have retention times measured in minutes rather than hours or days and must also reduce moving parts and reduce energy consumption. Thus critical questions are:
1. why are wastewater treatment processes so slow?
2. what is the nature of the rate limiting step?
3. how could the rate be dramatically increased?

## Upflow Anaerobic Pulsed Fluidized Bed Reactor
Upflow Anaerobic Sludge Blanket digestors that don't use a recycle line have an upflow velocity that is far lower than is required

## String Digestor
