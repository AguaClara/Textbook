.. _title_Grand Challenges:

*******************
AguaClara Treatment
*******************

Grand Challenges
================

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

.. _heading_The_AguaClara_Treatment_Train:

Design Evolution
================

During the later half of the 20th century surface water treatment technologies evolved slowly. The slow evolution was likely a product of the regulatory environment, the high cost of water treatment infrastructure, and the low profit margin. The high cost of municipal scale water treatment infrastructure made experiments at scale infeasible and thus there was no mechanism to introduce disruptive innovations. With little opportunity for a significant return on investment there was little incentive to invest in the research and development that could have advanced the technologies. A final disincentive was the widely held belief that surface water treatment was a mature field with little opportunity for significant advancement. The advances of the latter half of the 20th century focused primarily on mechanization and automation (Supervisory Control and Data Acquisition - SCADA).

Design standards such as the `Great Lakes - Upper Mississippi River Board 10 States Standards <http://10statesstandards.com/>`_ are evolving very slowly and retain an empirical approach to design. The empirical design methodology is a direct result of two confounding factors. The physics of particle interactions based on diffusion, fluid shear, and gravity are complex and given the challenges of characterizing surface water particle suspensions it was natural to assume that a mathematical description of the processes would be intractable.

Mechanized and automated water treatment plants performed reasonably well in communities with ready access to technical support services and supply chains that could reliably deliver replacement parts. In the global south municipal water treatment plants haven't faired as well. In 2012, one of the main water treatment plants serving Kathmandu, Nepal had failed chlorine pumps and were using a red garden hose to siphon chlorine from the stock tank. They crimped the end of the hose to control the flow rate of the chlorine solution.

.. _figure_Kathmandu_chemical_feed_room:

.. figure:: ../Images/Kathmandu_chemical_feed_room.png
    :width: 300px
    :align: center
    :alt: Kathmandu chemical feed room

    Failed chlorine dosing system bypassed with a red tube that siphons the chlorine solution at a plant in Kathmandu, Nepal in 2012.

The ingenious and simple chemical dosing system that uses a siphon to completely bypass the failed pumps begs the question of whether design engineers could have invented a better option than the short lived pumps that they specified. We will investigate a gravity powered chemical dosing system that is far more reliable than chemical dosing pumps and that borrows from the simplicity of the garden hose solution used by the Nepali plant operators.

Chemical dosing systems are particularly vulnerable and their failures make plant operation very challenging. Providing the right coagulant dose is critical for efficient removal of particle and dissolved organics. Chemical dosing systems commonly rely on pumps and those pumps require regular maintenance and have relatively short mean times between failures.

.. _figure_Kathmandu_alum_dosing:

.. figure:: ../Images/Kathmandu_alum_dosing.jpg
    :width: 300px
    :align: center
    :alt: Kathmandu alum dosing

    Alum dosing system based on the rate that 25 kg blocks of alum are placed in the inlet channel of the plant.

The AguaClara Cornell program was founded in 2005 with the goal of creating a new generation of sustainable technologies that would perform well even in the rugged settings of rural communities. The goal wasn't simply to create technologies that would work for communities with very limited resources. The goal was to create the next generation of technologies that would both perform well in communities with limited resources and would be the highest performing technologies on multiple metrics for all communities.

For the past several decades surface water treatment technologies have been considered "mature" and when I (Monroe) took a design course on drinking water treatment in 1985 I had the impression that there was little room for further innovation. This perspective is remarkable given that with the exception of lamellar sedimentation there were no equations describing the core treatment processes.

Empirical design guidelines don't provide insight into how designs could be optimized or even what the performance of a water treatment plant will be.

.. _heading_Design_for_the_Context:

Stakeholder Influence
=====================

Tours of water treatment plants suggest that it is common for designs to be driven by the vender goal of a stable revenue stream for replacement parts rather than by a goal of meeting the client's needs. Mandatory software upgrades, mechanical valves, chemical pumps, mixing units provide a steady demand for proprietary components. Financers often prefer projects that can be implemented quickly either because they have target expenditures for a fiscal year or because loan repayment begins when the facility is turned over to the client.

Design for the client would strive to reduce capital, operating, and maintenance expenses. Clients also place a high value on reliability, ease of maintenance, and the ability to handle repairs with their staff. Design for the context would account for the capabilities of local and national supply chains. A key design consideration is to ensure that the treatment capabilities of the treatment plant match the variable water quality of the proposed water source. There are numerous slow sand filtration plants installed in the global south that are attempting to treat water sources that can not be effectively treated by slow sand filtration. The cost of the failure to consider the client and the context is born by the communities who end up with water treatment systems that aren't able to provide reliable safe water.

Design for the client requires empathy and a commitment to listen to and learn from plant operators. It also requires attention to detail and watching how plant operators interact with water treatment plants. Empathy leads to the goal of creating a work environment that makes it easy for the plant operators to do their routine tasks. This isn't just to make the plant operators work easy. A plant that is designed with the plant operator in mind will also engender pride and that pride will lead to better plant performance.

An example of design for the operator is the elevation of the walkways in AguaClara plants. Conventional plants often have walkways that are above the tanks. That places the operator's eyes several meters above the water surface and makes it difficult to see particles and flocs in the water. AguaClara plants have the walkways approximately 50 cm below the top of the tanks. This makes it easy for the plant operator to look into the tanks for quick visual inspections.

.. _figure:

.. figure:: ../Images/Improvised_ladder_access_to_sed_tank.jpg
    :width: 300px
    :align: center
    :alt: Improvised ladder access to sed tank

    A plant operator built a makeshift ladder to enable easier access to the flocculation and sedimentation tanks in a package plant. This ladder considerably shortened the distance between the coagulant dose controls and the flocculator. The ladder also makes it possible to look closely at the water to see the size of the flocs.

.. _heading_Design_Bifurcations:

Design Choices
==============

Seemingly small decisions can have a profound effect on the evolution of design. Often these decisions have a clear logic and a simple analysis would suggest that the decision must be the right one. It is common for design choices to have multiple consequences that can turn a seemingly great choice into a poor performer.

.. _heading_walls_and_a_roof:

Built for Operation
-------------------

Traditionally in tropical and temperate climates, flocculation and sedimentation units are built without an enclosing building because they aren't in danger of freezing. Without protection from the sun the materials used for plant construction must be UV resistant and thus plastic can't be used. This requires use of heavier and more expensive materials such stainless steel and aluminum. Metal plate settlers are heavy and thus they can't be easily removed by the plant operator.

Without the ability to gain access to a sedimentation tank from above, conventional sedimentation tank cleaning must be done by providing operator access below the plate settlers. This in turn requires that the space below the plate settlers be tall enough to accommodate a plant operator. Thus sedimentation tanks that are built in the open have to be deeper than sedimentation tanks that are built under a roof and they are more difficult to maintain because the operator has to enter the tank through a waterproof access port. Operator access to the space below the stainless steel or aluminum plate settlers is through a port in the side of the tank (see the video :numref:`figure_Cleaning_a_Sed_Tank_with_fixed_plates`).


.. _figure_Cleaning_a_Sed_Tank_with_fixed_plates:

.. figure:: http://img.youtube.com/vi/TSh-ZNqaW8Y/0.jpg
    :width: 300px
    :align: center
    :alt: Cleaning a Sed Tank with fixed plates
    :target: http://www.youtube.com/watch?v=TSh-ZNqaW8Y

    Plant operators opening hatch below plate settlers in a traditional sedimentation tank.

AguaClara sedimentation tanks are designed to be taken off line one at a time so the water treatment plant can continue to operate during maintenance. Two plant operators can quickly open a sedimentation tank by removing the plastic plate settlers (see the video :numref:`figure_Removing_Plate_Settlers`). The zero settled sludge design of the AguaClara sedimentation tanks also reduces the need for cleaning.

.. _figure_Removing_Plate_Settlers:

.. figure:: http://img.youtube.com/vi/vZ2f6mduEls/0.jpg
    :width: 300px
    :align: center
    :alt: Removing Plate Settlers from an AguaClara Sedimentation tank
    :target: http://www.youtube.com/watch?v=vZ2f6mduEls

    Plant operator removing plate settlers from an AguaClara sedimentation tank.

There is another major consequence of building water treatment plants in a secure enclosed building. Many water treatment plants will operate around the clock and that requires plant operators to spend the night at the facility. Having a secure facility provides improved safety for the plant operator. That improved safety is very important for some potential operators and thus providing that safety will increase potential diversity.

.. _heading_Mechanized_or_Smart_Hydraulics:

Smart Hydraulics
----------------

Dramatically different designs are also created when we choose gravity power and smart hydraulics rather than mechanical mixers, pumps, and mechanical controls for each of the unit processes. It appears that use of electricity in drinking water treatment plants became the popular choice about 100 years ago. Many gravity powered plants have been converted to use mechanical mixers for rapid mix and flocculation. That choice may not have been well founded from a water quality or performance perspective.

.. todo:: Research the history of the conversion from hydraulic to mechanical rapid mix and flocculation to see what evidence was used to support the decision.

Automated plants often move the controls far away from the critical observation locations in the plant. This might be appropriate or necessary in some cases, but it has the disadvantage of making it more difficult for operators to directly observe what is happening in the plant. Direct observations are critical because even highly mechanized water treatment plants are not yet equipped with enough sensors to enable rapid troubleshooting from the control room.

AguaClara plants have a layout that places the coagulant dose controls within a few steps of the best places to observe floc formation in the flocculator. This provides plant operators with rapid feedback that is critical when the raw water changes rapidly at the beginning of a high runoff event. As operators spend time observing the processes in the plant they begin to associate cause and effect and can make operational changes to improve performance. For example, gas bubbles that carry flocs to the surface can indicate sludge accumulation in a sedimentation tank. Rising flocs without gas bubbles can indicate a poor inlet flow distribution for a sedimentation tank or density differences caused by temperature differences.

.. todo:: Show the plan view of an AguaClara plant.

.. _heading_AguaClara_Innovations:

AguaClara Inventions
=====================

The AguaClara treatment train consists of the following processes
 - flow measurement
 - metering of the coagulant (and chlorine) that will cause particles to stick together
 - mixing of the coagulant with the raw water
 - flocculation where the water is deformed to cause particle collisions
 - floc filter where large flocs settle through water that is flowing upward causing collisions between small particles carried by the upward flowing water and the large flocs
 - lamellar sedimentation where gravity causes particles to settle to an inclined plate and then slide back down into the floc filter
 - stacked rapid sand filtration where particles collide with previously deposited particles in a sand filter bed
 - disinfection with chlorine to inactivate any pathogens that escaped the previous unit processes

Plant layout
------------
 #. Compact layout with processes sharing common walls when possible
 #. Walkways set at optimal elevation for observation and maintenance of processes
 #. Open tanks used whenever possible to simplify maintenance
 #. Building enclosure to protect the entire plant from UV and for security

Chemical dosing
---------------
 #. Linear flow orifice meter to both measure the plant flow rate and to turn the entrance tank water surface into a flow sensor input for the chemical dosing system.
 #. Gravity powered semi-automated dosing system that delivers a constant dose even when plant flow rate changes.
 #. Slider on a calibrated scale for intuitive changes in chemical dose

Rapid mix
---------
 #. Simple orifice for hydraulic rapid mix

Flocculation
------------
 #. Obstacles between baffles to create a more uniform distribution of energy dissipation rate and a more efficient use of available energy
 #. Plastic modules that can easily be removed from channels for maintenance
 #. Compact vertical flow flocculators for low flow plants

Floc Filter and Plate Settlers
------------------------------
 #. Four channel inlet/outlet system that enables

     #. dumping flocculated water that doesn't meet specifications
     #. taking one sedimentation tank offline by placing a pipe stub in the inlet and a cap on the outlet
     #. dumping settled water that doesn't meet specifications

 #. Inlet manifold with flow diffusers that straighten the flow into a continuous line jet
 #. Inlet manifold is offset from center to force jet to all go in a consistent direction through the jet reverser
 #. Jet reverser that efficiently reverses the direction of the incoming water to be able to resuspend settled flocs that are sliding down the inclines
 #. Zero settled sludge in the main part of the sedimentation tank
 #. Hydraulically cleaned sedimentation tank with no moving parts
 #. Floc Hopper that consolidates the floc slurry prior to draining.
 #. Floc filter that is stable and that reduces the clarified turbidity

Filtration
----------
 #. Sand drain system to empty sand from filter hydraulically
 #. Wing and orifice system to inject water into the filter bed
 #. Stacked Rapid Sand Filtration system that has the same flow rate for filtration and for backwash
 #. Uses settled water for backwash to eliminate need for pumps and clearwells and to eliminate failure mode of inadequate supply of filtered water for backwash.
 #. Air valve control system to trigger mode change from backwash to filtration and from filtration to backwash
 #. No valves needed on inlet and outlet pipes


Drinking Water Treatment
========================

The potential to make a dramatic improvement in the quality of life of communities will guide our journey. The following research questions are the outgrowth of research and innovation by the AguaClara Cornell program. Although the AguaClara program invented numerous technologies and contributed to a new understanding of the physics of drinking water treatment, there are still many unanswered questions.

* Why is reducing the turbidity to less than 0.01 NTU not currently possible for most surface water treatment plants that rely on flocculation, sedimentation and sand filtration? Or stated another way, what controls the particle removal efficiency of surface water treatment plants?
* How can we take measurements of raw water quality and use that to optimize the design of a water treatment plant? This will require creating the models that describe the physics of each unit process and that is a recurring theme of the research introduced below.
* How can we invent new and improved technologies that enable communities to reliably produce high quality drinking water without needing to rely on expensive, expendable proprietary components?

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

Floc Filter
-----------

AguaClara invented the zero settled sludge sedimentation tank and the required `geometry to maintain a stable fluidized floc suspension <https://ascelibrary.org/doi/abs/10.1061/%28ASCE%29EE.1943-7870.0000773>`_ that provides primary filtration. The addition of primary filtration in clarifiers improves their `particle removal efficiency <https://iwaponline.com/aqua/article/59/5/312/29069/Parameters-affecting-steady-state-floc-blanket>`_, eliminates the need for mechanized sludge removal, and dramatically reduces mean flows that commonly result in poor floc capture. Although it is known that the primary filtration process enhances particle removal, the physics of primary filtration have been elusive and are currently an AguaClara Cornell NSF research project. Experiments conducted starting in January of 2021 suggest that fluidized flocs have a finite capacity to capture particles. That insight paves the way for a new research project to optimize the design and operation of primary filters and answer a new series of questions.

1. Why do flocs in the floc filter have a finite capacity to capture incoming particles and flocs?
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

Comparison with Croton Water Treatment Plant
---------------------------------------------

As AguaClara technologies extend to larger and larger cities one of the criticisms could be that the technologies are somehow limited to small scale facilities. To address this question we will compare AguaClara unit processes with one of the most recent large scale water treatment plants, the `Croton Water Treatment Plant <../_static/references/Croton-WFP.pdf>`_ (CWTP) in NYC.

The CWTP is designed to treat `290 mgd <https://www.hazenandsawyer.com/work/projects/croton-wtp/>`_ (million gallons per day) which is equivalent to 12,700 L/s. The final cost of the project was $3.2bn. The cost per L/s of treatment capacity was thus $250,000. This is approximately 25 times more expensive than AguaClara water treatments. Of course, AguaClara water treatment plants haven't been constructed underground in the middle of a major city! Nonetheless, the factor of 25 suggests that AguaClara technologies have a significant cost advantage.

The CWTP has 48 flocculators and 48 dissolved air flotation processes working in parallel. The flow per unit is thus 265 L/s. The current maximum size of the AguaClara Open Stacked Rapid Sand (OStaR) ilter is 20 L/s. It would be possible to design larger OStaR filters by simply including multiple sets of inlet/outlet trunk lines into a single filter box. The CWTP filters appear to have 6 outlet trunk lines per filter and thus the flow per trunk line is 44 L/s.

The CWTP uses 2 stage mechanical flocculators with a total residence time of 4.8 minutes and a velocity gradient of 100 Hz. This residence time is much shorter than conventional design requirements, about half of the residence time used by the AguaClara plants built around 2017, significantly larger than the 90 second residence time used in the AguaClara 1 L/s plants.

CWTP uses dissolved air flotation tanks that are located on top of the rapid sand filters.

The filter approach velocity (the velocity of water before it enters the sand bed) for CWTP is 4.42 mm/s. This is significantly higher than the 1.85 mm/s filtration velocity currently used in StaRS filters. StaRS filters are a stack of 6 filters and the net filtration velocity is 11 mm/s. Thus by that metric the StaRS filters are significantly smaller than the CWTP filters.

.. code:: python

   #the unit registry has been imported above and does not need to be imported again
   import aguaclara
   import aguaclara.core.physchem as pc
   from aguaclara.core.units import unit_registry as u
   Q_Croton =(290 *u.Mgal/u.day).to(u.L/u.s)
   Cost_Croton = 3.2 * 10**9 * u.USD
   Cost_per_Lps = Cost_Croton/Q_Croton
   Cost_per_Lps
   N_DAF = 48
   Q_per_unit = Q_Croton/N_DAF
   Q_per_unit/6
   (15.9 * u.m/u.hr).to(u.mm/u.s)

[SECTIONS BELOW TO BE MOVED OUT OF CHAPTER]

Wastewater Treatment
====================

Although AguaClara began with a focus on drinking water treatment, we have always been keenly aware that adequate wastewater treatment is absolutely essential to reduce harm to the environment and harm to downstream communities.

One of the core ideas of the AguaClara design process is that reactor geometry and hydraulic design are critical to obtain the target performance. Environmental engineers have tended to focus on the microbiology and chemistry of unit processes and have sometimes neglected the interactions between fluids, particles, and reactor geometry. We hypothesize that it will be possible to significantly improve on the conventional UASB design by inventing a anaerobic digester that accounts for the interactions between fluids, particles, and reactor geometry. Similarly, we hypothesize that it will be possible to dramatically improve the design of ultra low energy atmospheric oxygen transfer into aerobic reactors.

Wastewater treatment generally requires more land, capital, and energy than drinking water treatment and thus is out of reach for most towns and villages. The result is that the majority of human waste reaches the environment with little or no treatment. Drinking water treatment is currently beyond the reach of many towns and villages and wastewater treatment isn't even on the horizon. Thus we need innovations that are better by a factor of 10 or more. The treatment technologies must have retention times measured in minutes rather than hours or days and must also reduce moving parts and reduce energy consumption. Thus the critical questions are:

1. Why are wastewater treatment processes so slow?
2. What is the nature of the rate limiting step?
3. How could the rate be dramatically increased?

.. _heading_Anaerobic_Pulsed_Bed:

Anaerobic Pulsed Bed
====================

Anaerobic digestion has the advantage of not requiring aeration and the disadvantage of requiring long residence times. Presumably it is the bacteria that require a long residence time and not the water and thus these residence times must be decoupled by using sedimentation or a fixed film process.

Upflow Anaerobic Sludge Blanket digestors that don't use a recycle line have an upflow velocity that is far lower than is required to fluidize the bed of granules that form. Flow through the resulting settled bed of sludge must be highly nonuniform and the result is that much of the settled bed is likely contributing little to the treatment process.

Flow uniformity and contact with all of the solids could be achieved with a fluidized bed. The velocity required for a fluidized bed would require a very tall reactor given the assumed requirements for residence time. Presumably the residence time requirement is based on the poor flow distribution in the settled sludge. Nonetheless, for reasonable depth reactors it will be difficult to operate a once through fluidized bed.

The hydraulic solution to this problem is to use pulsed flow with a pulse having a volume equal to perhaps 1-5 cm of depth in the reactor. The pulse will completely lift the settled bed of sludge and the sludge will then fall through the water column. This lift and drop cycle is expected to have much more uniform flow of water through the sludge bed then would be achieved by a stagnant bed that would rapidly develop preferential flow paths.

Upflow anaerobic settled bed (UASB) are conventionally known as upflow anaerobic sludge blanket reactors. The word "blanket" is frequently used in the field of water and wastewater treatment to refer to a fluidized bed of suspended particles (see floc filter). Unfortunately that definition is not clearly communicated by the term "blanket" and this has led to confusion of the fundamental mechanisms at play in UASB reactors.

Fluidized bed reactors required inlet and bottom geometry configurations that prevent settled particles from accumulating anywhere on the bottom of the reactor. Many UASB reactors have flat bottoms and the inlets are not designed to ensure continuous resuspension of settled particles. Thus conventional UASB reactors are often not fluidized beds and thus don't have the mass transfer efficiencies that they could have.

UASB reactors typically require hydraulic residence times hours and have a height of 4 or more meters. The result is a maximum upflow velocity that is orders of magnitude lower than the terminal velocity of the granules and thus it is clear that UASB reactors are primarily settled beds of stagnant sludge that is doing little to aid in the treatment of the wastewater.

The flow distribution through settled sludge is very unlikely to be uniform. The flow is likely to erode a mostly vertical path the shortest distance between the inlet and the top of the settled sludge. There doesn't appear to be any mechanism that would lead to the idealized uniform flow distribution. Thus conventional UASB reactors are evidently plagued by short circuiting with actual hydraulic residence times a fraction of the design value. (Cite literature in support of this hypothesis.) This leads to short-circuiting and formation of preference flow patterns in sludge bed which in turn leads to dead zones in the sludge as well as improper treatment (`Pena, 2006 <https://doi.org/10.1016/j.watres.2005.11.021>`_)

The upflow velocity required to maintain a fully fluidized bed of the anaerobic granules is approximately (cite AguaClara UASB research by Cho, et al. who measured the sedimentation velocity of anaerobic granules) x mm/s. At this velocity the height of the reactor would need to be x m in order to achieve the target hydraulic residence time of y hrs. This is not a practical design for community scale reactors and thus it would be advantageous to invent an alternate system for providing more uniform flow through the solids that contain the microorganisms in a UASB reactor.

Our proposed solution to this mismatch between required upflow velocity for a fluidized bed and target hydraulic residence time is to use a pulsed flow inlet. The pulsed flow will be designed to lift the entire settled bed off of the floor of the UASB reactor so that the influent wastewater is uniformly distributed to the bottom of the reactor. We hypothesize that the settled bed will then break apart and settled into the band of fresh wastewater that is on the bottom of the reactor. With this proposed mechanism it is clear that a critical parameter is the depth of wastewater that should be injected with each pulse. It is likely that this depth of fresh wastewater should be

 - A small fraction of the depth of the UASB (perhaps less than 10% to ensure that no fresh wastewater can jet through the entire UASB in the time that the sludge settled again)
 - Large enough to provide a flow passage underneath the lifted bed without requiring flow velocities that are so high that the bed is scoured near the inlet jet. This translates to larger than a minimum ratio of fresh wastewater depth per pulse/inlet spacing.

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
