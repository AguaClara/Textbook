.. raw:: html

    <embed>
       <link rel="canonical" href="https://aguaclara.github.io/Textbook/Introduction/Design_Evolution.html" />
       <script src="https://hypothes.is/embed.js" async></script>
    </embed>

.. _title_Design_Evolution:

****************
Design Evolution
****************


Introduction
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

The AguaClara program was founded in 2005 with the goal of creating a new generation of sustainable technologies that would perform well even in the rugged settings of rural communities. The goal wasn't simply to create technologies that would work for communities with very limited resources. The goal was to create the next generation of technologies that would both perform well in communities with limited resources and would be the highest performing technologies on multiple metrics for all communities.

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

.. figure:: ../Images/Improvised_ladder_access_to_clarifier.jpg
    :width: 300px
    :align: center
    :alt: Improvised ladder access to sed tank

    A plant operator built a makeshift ladder to enable easier access to the flocculation and clarifiers in a package plant. This ladder considerably shortened the distance between the coagulant dose controls and the flocculator. The ladder also makes it possible to look closely at the water to see the size of the flocs.

.. _heading_Design_Bifurcations:

Design Choices
==============

Seemingly small decisions can have a profound effect on the evolution of design. Often these decisions have a clear logic and a simple analysis would suggest that the decision must be the right one. It is common for design choices to have multiple consequences that can turn a seemingly great choice into a poor performer.

The Cost of Empirical Design
----------------------------

The current design process for water treatment plant relies on previous designs and a fragmented design approach. Each unit process is treated as independent without a full ability to account for interdependencies. There is limited ability to optimize the design and very little ability to predict how raw water quality changes will influence performance and even less ability to use raw water quality parameters to guide the design.

* Pilot studies are required to assess treatability.
* No design integration and much less optimization between processes. For example, we don't know how to optimize the design of a flocculator to minimize the filtered water turbidity.
* Few physics-based equations that can predict the performance of unit processes given the raw water characteristics.


.. _heading_walls_and_a_roof:

Built for Operation
-------------------

Traditionally in tropical and temperate climates, flocculators and clarifiers are built without an enclosing building because they aren't in danger of freezing. Without protection from the sun the materials used for plant construction must be UV resistant and thus plastic can't be used. This requires use of heavier and more expensive materials such stainless steel and aluminum. Metal plate settlers are heavy and thus they can't be easily removed by the plant operator.

Without the ability to gain access to a clarifier from above, conventional clarifier cleaning must be done by providing operator access below the plate settlers. This in turn requires that the space below the plate settlers be tall enough to accommodate a plant operator. Thus clarifiers that are built in the open have to be deeper than clarifiers that are built under a roof and they are more difficult to maintain because the operator has to enter the tank through a waterproof access port. Operator access to the space below the stainless steel or aluminum plate settlers is through a port in the side of the tank (see the video :numref:`figure_Cleaning_a_Clarifier_with_fixed_plates`).


.. _figure_Cleaning_a_Clarifier_with_fixed_plates:

.. figure:: http://img.youtube.com/vi/TSh-ZNqaW8Y/0.jpg
    :width: 300px
    :align: center
    :alt: Cleaning a Sed Tank with fixed plates
    :target: http://www.youtube.com/watch?v=TSh-ZNqaW8Y

    Plant operators opening hatch below plate settlers in a traditional clarifier.

AguaClara clarifiers are designed to be taken off line one at a time so the water treatment plant can continue to operate during maintenance. Two plant operators can quickly open a clarifier by removing the plastic plate settlers (see the video :numref:`figure_Removing_Plate_Settlers`). The zero settled sludge design of the AguaClara clarifiers also reduces the need for cleaning.

.. _figure_Removing_Plate_Settlers:

.. figure:: http://img.youtube.com/vi/vZ2f6mduEls/0.jpg
    :width: 300px
    :align: center
    :alt: Removing Plate Settlers from an AguaClara Clarification tank
    :target: http://www.youtube.com/watch?v=vZ2f6mduEls

    Plant operator removing plate settlers from an AguaClara clarifier.

There is another major consequence of building water treatment plants in a secure enclosed building. Many water treatment plants will operate around the clock and that requires plant operators to spend the night at the facility. Having a secure facility provides improved safety for the plant operator. That improved safety is very important for some potential operators and thus providing that safety will increase potential diversity.

.. _heading_Mechanized_or_Smart_Hydraulics:

Smart Hydraulics
----------------

Dramatically different designs are also created when we choose gravity power and smart hydraulics rather than mechanical mixers, pumps, and mechanical controls for each of the unit processes. It appears that use of electricity in drinking water treatment plants became the popular choice about 100 years ago. Many gravity powered plants have been converted to use mechanical mixers for rapid mix and flocculation. That choice may not have been well founded from a water quality or performance perspective.

.. todo:: Research the history of the conversion from hydraulic to mechanical rapid mix and flocculation to see what evidence was used to support the decision.

Automated plants often move the controls far away from the critical observation locations in the plant. This might be appropriate or necessary in some cases, but it has the disadvantage of making it more difficult for operators to directly observe what is happening in the plant. Direct observations are critical because even highly mechanized water treatment plants are not yet equipped with enough sensors to enable rapid troubleshooting from the control room.

AguaClara plants have a layout that places the coagulant dose controls within a few steps of the best places to observe floc formation in the flocculator. This provides plant operators with rapid feedback that is critical when the raw water changes rapidly at the beginning of a high runoff event. As operators spend time observing the processes in the plant they begin to associate cause and effect and can make operational changes to improve performance. For example, gas bubbles that carry flocs to the surface can indicate sludge accumulation in a clarifier. Rising flocs without gas bubbles can indicate a poor inlet flow distribution for a clarifier or density differences caused by temperature differences.

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
 #. Simple orifice for hydraulic rapid mix or simply rely on the mixing generated by the water exiting the linear flow orifice meter.

Flocculation
------------
 #. Obstacles between baffles when required to create a more uniform distribution of energy dissipation rate and a more efficient use of available energy
 #. Plastic modules that can easily be removed from channels for maintenance
 #. Compact vertical flow flocculators for low flow plants

Floc Filter and Plate Settlers
------------------------------
 #. Four channel inlet/outlet system that enables

     #. dumping flocculated water that doesn't meet specifications
     #. taking one clarifier offline by placing a pipe stub in the inlet and a cap on the outlet
     #. dumping settled water that doesn't meet specifications

 #. Inlet manifold with flow diffusers that straighten the flow into a continuous line jet
 #. Inlet manifold is offset from center to force jet to all go in a consistent direction through the jet reverser
 #. Jet reverser that efficiently reverses the direction of the incoming water to be able to resuspend settled flocs that are sliding down the inclines
 #. Floc filter that is stable and that reduces the clarified turbidity. The floc filter coupled with the jet reverser system produces a very uniform vertical flow into the plate settlers and thus eliminates large scale flow circulation that commonly results in excess flow through some of the plate settlers.
 #. Zero settled sludge in the main part of the clarifier
 #. Hydraulically cleaned with no moving parts
 #. Floc Hopper that consolidates the floc slurry prior to draining.


Filtration
----------
 #. Sand drain system to empty sand from filter hydraulically
 #. Wing and orifice system to inject water into the filter bed
 #. Stacked Rapid Sand Filtration system that has the same flow rate for filtration and for backwash
 #. Uses settled water for backwash to eliminate need for pumps and clearwells and to eliminate failure mode of inadequate supply of filtered water for backwash.
 #. Air valve control system to trigger mode change from backwash to filtration and from filtration to backwash
 #. No valves needed on inlet and outlet pipes
