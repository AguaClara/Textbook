.. raw:: html

    <embed>
       <link rel="canonical" href="https://aguaclara.github.io/Textbook/AIDE/AIDE.html" />
       <script src="https://hypothes.is/embed.js" async></script>
    </embed>

.. _title_AguaClara_Specifications:

**************************************
AguaClara Specifications
**************************************

This document specifies the design goals, the raw water quality
parameters, and the design and construction requirements for an
AguaClara drinking water treatment plant to treat water that may be
contaminated with particles, pathogens, and dissolved organics and
produce safe, potable drinking water.


General Outline
===============

A. Water Quality Parameter Requirements for AguaClara Treatment Plant Operation
#. Components of an AguaClara Plant

   1. Chemical Dosing System
   #. Entrance Tank
   #. Flocculators
   #. Clarifier including floc filter and plate settlers
   #. Stacked Rapid Sand Filters

AguaClara Plant Design Goals
============================

AguaClara drinking water treatment technologies remove turbidity and pathogens from raw water and to deactivate remaining
pathogens before distribution. AguaClara technologies are best suited for centralized water treatment in communities of at least 200 people. AguaClara technologies would not be appropriate for treatment of low-turbidity groundwater where the primary contamination issues are chemical, such as nitrate or heavy metals. AguaClara technologies are gravity-driven and do not require electricity. The AguaClara treatment systems installed in India use pumps to raise groundwater to the elevation necessary for filtration, chlorine application, and water distribution.

AguaClara treatment technologies include chemical dosing, rapid mix, flocculation, floc filter, plate settlers, filtration, and disinfection. An AguaClara treatment plant may be designed with all of these processes, or if raw water turbidity is low due to groundwater use, the treatment plant may be designed without flocculation, floc filter, and plate settlers.


Water Quality Parameters
------------------------

The tables below summarize the raw water quality parameters for which
AguaClara treatment technologies are appropriate.

.. _table_Water_Quality_Parameters:

.. csv-table:: Water Quality Parameters Treated by AguaClara Plants
   :header: "Water Quality Parameter", "Comments"
   :align: left

   Turbidity, "Raw water with turbidity up to 1,000 NTU can consistently be treated to less than 1 NTU."
   "Color/Dissolved Organic Matter (DOM)", "For raw water with high color or total organic matter content, pilot studies are recommended to confirm the efficacy of the coagulant and the ability of the flocs to settle."
   pH, "pH can be lowered to prevent calcium carbonate scaling in distribution piping or increased to reduce corrosion potential."
   Microbiological contamination, "The AguaClara treatment processes are designed to remove pathogens through particle removal and disinfection."

AguaClara plants are only designed to treat the water quality parameters listed above. All other parameters should be within acceptable ranges in the raw water or should be treated by other means.

Before beginning construction of an AguaClara treatment plant, bench-scale jar testing should be performed to confirm that polyaluminum chloride or another proposed coagulant is able to successfully form flocs that settle.


Chemical Dosing System
===================================================

#. Design goals for chemical dosing system

   #. The system will be capable of dosing chemicals for the following purposes. All materials shall be compatible with the chemicals being dosed.
   #. Disinfectant (normally sodium or calcium hypochlorite)
   #. Coagulant (typically polyaluminum chloride [PACl], but other coagulants such as alum can be used if justification is provided. Bench-scale jar testing should be performed to confirm that the proposed coagulant is able to successfully form flocs.)
   #. pH adjustment (if necessary)
   #. The chemical dosing system shall function by gravity and not depend on pumps or electrical power.
   #. The chemical dosing shall be flow-paced, meaning that the rate of chemical application is automatically adjusted proportional to the flow rate of water moving through the plant.
   #. The system shall be easily disassembled by the plant operator for cleaning with vinegar to remove calcium carbonate deposits.
   #. The chemical dose (mass chemical per volume water passing through the plant) shall be easily adjustable by the plant operator.

#. Linear Flow Orifice Meter (LFOM) or equivalent

   #. The plant entrance chamber shall be equipped with a device that will result in a linear relationship between the plant flow and the water level in the entrance chamber. The Linear Flow Orifice Meter (LFOM), which is a pattern of orifices through which flow exits the entrance chamber, is described below. An equivalent device, such as a Sutro weir, can also be used if demonstrated to function equivalently.
   #. The pattern of orifices shall be designed so that the water level in the entrance chamber (equal to the hydrostatic head pushing water through the offices) is linearly proportional to the total flow through the orifices (equal to the plant flow). An example of an LFOM is shown in :numref:`figure_spec_LFOM`. The orifices may be drilled in a flat plate or in the walls of a vertical pipe.
   #. The LFOM shall be capable of measuring flow ranging from 10 percent to 100 percent of the maximum plant design flow.
   #. To ensure that plant flow is measured with adequate resolution but avoid excessive head loss through the LFOM, the water level should change a minimum of 20 cm from no flow to the design flow rate.
   #. Depending on the plant flow, the LFOM may consist of orifices in one or multiple riser pipes or in a flat plate.

.. _figure_spec_LFOM:

.. figure:: ./About/Images/LFOM.png
    :width: 100px
    :align: center
    :alt: LFOM

    Example of a Linear Flow Orifice Meter



#. Chemical storage

   #. For each chemical, the plant shall include two or more storage tanks. The tank and fitting materials shall be compatible with the chemical. Storage tanks can be plastic or concrete, as long as they are confirmed to be compatible with the chemical being stored.
   #. The combined volume of all tanks used for a chemical shall allow for storage of sufficient chemical to supply the plant at maximum flow and maximum chemical dose for at least 48 hours.

#. Chemical dose controller

   #. The plant shall be equipped with a chemical dose controller
   configured as shown in Figure 2.

Figure 2: Chemical dose controller

2. Materials that will be in contact with chemicals must be compatible
   with the chemical and suitable for use with potable water.
3. Key components

#. Constant head tank

#. From the chemical storage tanks, the chemical passes via gravity to a
   constant head tank. The chemical enters the constant head tank via a
   float valve, which maintains a constant level of chemical in the
   constant head tank, providing a constant head to drive the chemical
   through the doser.
#. The chemical level in the constant head tank shall be level with the
   fulcrum of the dosing lever.
#. The vertical distance from the constant head tank level to the end of
   the dosing hose at max flow and max dose shall be 20 cm.

2. Dosingtubes

#. Chemical flows from the constant head tank into dosing tubes, which
   terminate in a free discharge at the dose slider on the doser lever.
#. The dosing tubes shall be straight, to minimize minor losses and
   maintain a nearly linear relationship between flow and driving head.
#. There shall be three dosing tubes functioning in parallel, and the
   diameter of the tubes shall be designed to provide laminar flow over
   the desired range of chemical flows. Given the laminar flow, the
   flowrate through the dosing tubes will be directly proportional to
   elevation difference between the chemical level in the constant head
   tank and the dose slider.
#. The plant shall have a spare set of dosing tubes on hand so that one
   set of tubes can be cleaned while the other set is in use.
#. Headloss through all other tubes and fittings other than the dosing
   tubes shall be minimal and far less than the headloss through the
   dosing tubes.

3. Lever

#. One end of the doser lever is connected to a float in the plant
   entrance chamber. The dose slider and thus the ends of the doser
   hoses are located on the other end of the lever.
#. For proper proportions relative to the variation entrance tank level,
   the doser lever shall be 60 cm long.

4. Function

#. The doser is designed so that the operator can select a chemical dose
   (mass of chemical per volume of water) by moving the dose slider to a
   specific position along the lever. The lever, LFOM and constant head
   tank then work together to adjust the chemical flow proportional to
   the plant flow to maintain a constant chemical dose.
#. When the plant flow is zero, the lever is horizontal and chemical
   flow is zero.
#. When plant flow increases, the water level in the entrance tank
   increases (due additional headloss through the LFOM), causing one end
   of the doser lever to rise. This, in turn, causes the other end of
   the lever, and the dose slider, to fall, increasing the elevation
   difference between the chemical level in the constant head tank and
   the dose slider. The greater driving head increases the chemical flow
   through the doser hose.
#. Because the entrance chamber level (due to the LFOM) is directly
   proportional to the plant flow rate, the dose slider elevation is
   directly proportional to the entrance chamber level, and the chemical
   flow is directly proportional to the dose slider elevation, the
   chemical flow is directly proportional to the plant flow.

.. _h.5t3pyasbwbfv:

Flocculator (\ `Link to textbook chapter <https://www.google.com/url?q=https://aguaclara.github.io/Textbook/Flocculation/Floc_Design.html&sa=D&source=editors&ust=1651247616944605&usg=AOvVaw0u8pZUHQ0K2e-DLOKc_Ui2>`__\ )\ `[e] <#cmnt5>`__
============================================================================================================================================================================================================================================

#. Design Goals: The AguaClara flocculator is a hydraulic flocculator
   that can be designed as either a horizontal or vertical flocculator.
   The AguaClara flocculator is designed with the following goals:

#. Velocity gradient and residence time to aggregate individual
   particles and small flocs into flocs large enough to settle out in
   the sedimentation tanks. The product of velocity gradient (G) and
   residence time (ϴ) isa dimensionless numberknown as collision
   potential or Gϴ.
#. Minimize retention time to reach a design Gϴ of approximately 37,000.
   This determines the minimum total volume of the flocculator. The
   design volume of the flocculator may be larger due to construction
   constraints, such as making the length of the flocculator the same as
   the length of the sedimentation tanks or keeping the flocculator
   channels wide enough to fit a human body for ease of cleaning and
   maintenance. 
#. Minimize “dead zones” in the flocculator and reduce the opportunity
   for short circuiting of the flocculator.
#. Facilitate the draining of sludge and maintenance manually by one
   person

2. Flow paths

#. The length of the flocculator channels is determined by the length of
   the sedimentation tanks plus the inlet and outlet channels for the
   sedimentation tanks.
#. The width of each flocculation channel is determined by material
   constraints and to facilitate cleaning and maintenance.The
   flocculator baffles are made of polycarbonate sheets, so the width of
   the channel should be no larger than the width of a polycarbonate
   sheet. The width of the channel should be no smaller than50 cm so an
   operator can safely enter the tank. Large plants treating more than
   100 L/s may be designed with horizontal flocculation channels and may
   use ferrocement baffles, but they should still be easily drained and
   cleaned.
#. The depth of the flocculation channels is determined by construction
   constraints and to minimize the planview area of the flocculators and
   thus the plant.
#. The overall volume of theflocculator is determined by the individual
   constraints on each dimension of the flocculator, but the collision
   potential,Gϴ, of the flocculator must be at least 37,000.
#. The velocity gradient G for each flocculator baffle is calculated
   based on minor losses through the baffles as detailed in
   the\ `Flocculator section of the AguaClara
   textbook <https://www.google.com/url?q=https://aguaclara.github.io/Textbook/Flocculation/Floc_Design.html&sa=D&source=editors&ust=1651247616946772&usg=AOvVaw1yJJNCLMdNbfgFWwcUsxyP>`__\  linked
   above.\ `[f] <#cmnt6>`__\  Otherobstacles can also be added to the
   flocculator to increaseheadloss under low flow conditions.
#. The ports between flocculator channels should be designed with the
   same velocity gradient constraints as the baffles so that the port
   improves flocculation without breaking flocs.

#. Port between channels to maintain energy dissipation rate

3. Flocculator Channel Construction

#. The walls of the flocculation channels should be vertical,
   maintaining the channel width along both the length and height of
   each flocculator channel.
#. The floor of each flocculation channel should be sloped toward the
   drain channel, and one or more drain valves should be installed to
   periodically remove sludge from the flocculator. The slope and valves
   also allow the flocculation channels to be completely emptied for
   more in-depth maintenance.
#. The drain valve or valves to drain the flocculation
   channel\ `[g] <#cmnt7>`__\ :sup:`\ `\ `[h] <#cmnt8>`__\ :sup:`\ `\ `[i] <#cmnt9>`__\ smust
   be large enough to empty the flocculation channels in a reasonable
   time.
#. The flocculation channels should have sufficient lighting for the
   operator to observe floc formation. The operator should also have a
   flashlight to observe floc formation during power outages.

4. Baffles

#. The flocculation baffles must be constructed to be removable. A
   baffle module should be raisable by one operator working alone so
   that water can flow beneath the baffle and drain from the flocculator
   channel. Large flocculators may have baffle modules that require more
   than one person to completely remove from the flocculator channel.
#. The flocculation baffles should be constructed from polycarbonate
   sheets, and the frame for holding together baffle modules should be
   made from PVC. Other materials may be used if justification is
   provided, including the use of ferrocement baffles for horizontal
   flocculators in large plants.
#. Baffle modules may also include other PVC obstacles to increase
   flocculation efficiency and reduce the volume and residence time of
   the flocculator.

.. _h.t42tt5e2keml:

Sedimentation Tank (\ `Link to textbook chapter <https://www.google.com/url?q=https://aguaclara.github.io/Textbook/Sedimentation/Sed_Intro.html&sa=D&source=editors&ust=1651247616948836&usg=AOvVaw0htlhpNQ4oE5AXmDvdhsKY>`__\ )
================================================================================================================================================================================================================================

#. Design Goals: The AguaClara sedimentation tank is a high-rate
   vertical flow sedimentation tank that is designed with the following
   goals:

#. To produce a stable floc blanket (suspended layer of flocs) that acts
   like a primary filter that reduces the settled water turbidity
#. To provide evenly distributed low-velocity flow through the plate
   settlers
#. To prevent accumulation of sludge that would tend to become anaerobic
   and release both dissolved organics (taste and odor issues) and
   methane bubbles that would carry flocs to the top of the
   sedimentation tank
#. To remove the solids without requiring power or moving mechanical
   parts
#. To provide a mechanism for the operator to dump poorly flocculated
   water before it enters the sedimentation tank. This is important to
   reduce the recovery time when there is a flocculation failure.
#. To ensure easy operation and maintenance.
#. To be able to take any sedimentation tank offline for maintenance
   while the other sedimentation tanks continue to operate.

2. Influent Channel: Flocculated water enters a pipe in the bottom of
   the influent channel. Water flows down the pipe, through a 90-degree
   bend, into the influent manifold.

3. Influent manifold:Water exits the influent manifold through a series
   of orifices and diffusers in the bottom of the pipe. The end of the
   influent manifold is capped.

4. Diffusers:The orifices and diffusers point down to the bottom of the
   sedimentation bay and extend along the length of the pipe at regular
   intervals to ensure that water is evenly distributed within the bay.
   Diffusers are designed to introduce 1 cm of head loss to uniformly
   increase the head loss through all flow paths in the sedimentation
   tank.

8. Diffusersare shaped so that one end is a circular pipe that fits into
   the influent manifold orifice, and the other end is deformed to the
   shape of a thin rectangle. This deformation is done to create a line
   jet entering the jet reverser in the bottom of the sedimentation
   tank.

5. Jet reverser:The jet reverser consists of a longitudinally-cut
   half-pipe that is laid in the bottom of the bay. It functions as a
   way to keep flocs suspended in the sedimentation tank by ensuring
   that any sludge that settles will be propelled back up by the force
   of the diffuser jet.

#. The diffusers are offset from the jet reverser centerline. This is
   intentionally done to promote the resuspension of flocs, which form a
   floc blanket for primary filtration.
#. Currently, AguaClara plants use an upflow velocity of 1 mm/s.

6. Primary Filtration (Floc Blanket):Floc blankets improve the
   performance of a sedimentation tank and reduce settled water
   turbidity by a factor of 10.

#. The line jet from the diffusers enters the jet reverser to force flow
   up through the sedimentation bay. The vertical upward jet momentum is
   used to resuspend flocs that have settled to the bottom of the
   sedimentation tank. The resuspended flocs form a fluidized bed which
   is called a floc blanket. The bed is fluidized because flocs are kept
   in suspension by the upflowing water.
#. For a floc blanket to form, a sedimentation system requires that:

#. All flocs are returned to the bottom of the sedimentation tank.
#. All settled flocs are resuspended by incoming water.

7. Sloped bottom geometry:The AguaClara sedimentation tank bottom
   geometry prevents sludge accumulation while also ensuring good flow
   distribution.

3. Theslope on either side of the diffusers is at a 50 degree angle
   above horizontal. The bottom geometry allows for smooth flow
   expansion to the entire plan view area of the bay, and ensures that
   all flocs that settle are transported to the jet reverser. The
   diffusers do not touch the bottom of the tank so that flocs on both
   sides of the diffuser can fall into the jet reverser for
   resuspension. Thus, there is no accumulation of settled flocs in the
   main sedimentation basin.

8. Floc Hopper: The floc hopper provides an opportunity for floc
   consolidation. The floc weir controls the depth of the floc blanket
   because as the floc blanket grows, it will eventually reach the top
   of the floc weir. Because flocs are more dense than water, the flocs
   “spill” over the edge of the floc weir which allows the floc blanket
   to stay a constant height while sludge accumulates and consolidates
   in the floc hopper. There is a manual valve at the drain of the floc
   hopper. Operators can open the floc hopper drain valve whenever they
   want to easily drain the sludge. The floc hopper allows for a
   self-cleaning sedimentation tank. Operators only have to clean the
   sedimentation tank once every three to six months because there is no
   stagnant accumulation of anoxic sludge.

9. Plate Settlers: After flowing through the floc blanket, flocs reach
   the plate settlers. Plate settlers are sloped surfaces that provide
   additional settling area for flocs, thereby increasing the effective
   settling area of the sedimentation unit without increasing the plan
   view area. AguaClara plate settlers are sloped at 60 degrees. The
   spacing between plates is 2.5 cm.

#. Material of construction - Clear polycarbonate sheets, to allow
   operators to observe floc formation in the sedimentation tank
#. PVC Frame - A PVC frame is constructed in the sedimentation tanks.
   The polycarbonate sheet modules are placed on top of the PVC frame.  

3. Plate SettlerDesign Parameters:

+-----------------+-----------------+-----------------+-----------------+
| Parameter       | Determined by:  | Determines      | Value           |
+-----------------+-----------------+-----------------+-----------------+
| Upflow velocity | Floc blanket    | Plan view area  | 1 mm/s          |
|                 |                 | of tank         |                 |
+-----------------+-----------------+-----------------+-----------------+
| Capture         | Target          | Particle size   | 0.12 mm/s       |
| velocity        | turbidity       | distribution    |                 |
+-----------------+-----------------+-----------------+-----------------+
| Plate angle     | Self-cleaning   | Plate settler   | 60 deg          |
|                 | requirements    | length          |                 |
+-----------------+-----------------+-----------------+-----------------+
| Plate spacing   | Clogging and    | Plate settler   | 2.5 cm          |
|                 | floc rollup     | length          |                 |
|                 | constraints     |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| Plate settler   | Upflow velocity | Tank depth      | Calculated for  |
| length          |                 |                 | each plant      |
|                 | Capture         |                 |                 |
|                 | velocity        |                 |                 |
|                 |                 |                 |                 |
|                 | Plate angle     |                 |                 |
|                 |                 |                 |                 |
|                 | Plate spacing   |                 |                 |
+-----------------+-----------------+-----------------+-----------------+

10. Submerged Effluent Manifold:The submerged effluent manifold,
    sometimes called a launder, collects settled water from the
    sedimentation tank. It is a horizontal pipe that extends along the
    length of the tank and is located above the plate settlers but below
    the surface of the water. The submerged pipe has orifices drilled
    into its top; water enters the pipe through the orifices and the
    pipe leads out of the sedimentation tank.

11. Exit Weir:The submerged effluent manifold transports water from the
    sedimentation tank to a channel that runs perpendicular to the
    sedimentation bays. The channel collects water from all of the
    sedimentation bays. Water leaves this channel by flowing over a
    small wall, called the exit weir. The height of the exit weir
    controls the water levels in the flocculator and sedimentation tank.

12. Effluent Channel: After the water flows over the exit weir, it is
    collected in the effluent channel. The effluent channel has pipes
    embedded in the bottom of it which lead the settled water to the
    filter inlet box.

.. _h.ggwoxbjnaipq:

Stacked Rapid Sand Filter\ `[j] <#cmnt10>`__\  (\ `Link to textbook chapter <https://www.google.com/url?q=https://aguaclara.github.io/Textbook/Filtration/Filtration_Design.html&sa=D&source=editors&ust=1651247616960747&usg=AOvVaw0y-IYAyrh60-_Urf_L14lV>`__\ )
=================================================================================================================================================================================================================================================================

#. Description

Stacked Rapid Sand, StaRS, filters were invented in 2010 by the
AguaClara Cornell program in response to the need for a new technology
that would both eliminate the need for backwash pumps and not require
the construction of 6 filters for small towns. As shown in the figure
below, StaRS filters use six 20 cm deep layers of sand with the layers
stacked vertically. The six layers give a total sand depth of 1.2 m.

2. Operation:

#. The filter operates with the same design flow rate for both backwash
   and filtration modes and uses settled water for backwash. This
   eliminates the startup problem for rapid sand filters that do not
   have an initial source of backwash water.
#. Filtration Mode:

3. Backwash Mode:

3. Design Goals

#. Stacked Rapid Sand (StaRS) filters were developed to eliminate the
   need for backwash pumps and minimize the plan area required.
#. The filters should be designed so that the process of emptying the
   sand from the filter, removing the modules, cleaning the modules,
   replacing the modules, and replacing the sand is as easy as possible.
#. The filters should be able to be backwashed at the beginning of the
   filtration cycle if needed.
#. During backwash, all outlets and all inlets besides the bottom most
   inlet must be closed so all flow enters through the bottom inlet and
   flows out through the backwash pipe.
#. The plant shall have a minimum of two StaRS filters so that one of
   the StaRS filters can be in operation while the other is offline for
   maintenance or repairs.

4. Configurations:

#. Open StaRS (OStaRS) - used for flow rates greater than 8 L/s

#. Minimum plan view area of 85 cm x 85 cm (minimum size that can be
   constructed with a human working inside the filter)

2. Enclosed StaRS (EStaRS) filters - used for lower flow rates

#. Does not require excavation because filter is operated under vacuum
   for backwash
#. Assembled using PVC pipe as the body of the filter
#. Inner plumbing accessed through openings in the top and bottom of the
   main filter body

Enclosed Stacked Rapid Sand Filters (EStaRS) (Left)

Open Stacked Rapid Sand Filters (OStaRS) (Right)

5. Sand -StaRS filters use (6) six 20 cm deep layers of sand (no
   dual-media required) with the layers stacked vertically. The six
   layers give a total sand depth of 1.2 m.

#. Grain size\ `[k] <#cmnt11>`__

6. Filter Modules

#. Each layer of sand sits in between an inlet and outlet filter module.
   Each module consists of a large diameter trunk inlet/outlet pipe,
   which branches off into rows of smaller branch pipes. The branch
   pipes are supported along the filter walls by receptor pipes.

2. Inlet Filter Module

#. Small holes (orifices) are drilled into the inlet branches. The
   orifice diameter is selected based on constructability and not being
   too small to risk clogging (between 4 and 10 mm).
#. During filtration mode, water flows into the inlet filter modules
   through the inlet trunk and into the branches. Water flows out of the
   branches through small holes and into the sand layer.
#. During the transition from the backwash to filtration modes, water
   flows back into the inlet pipes. The “wings,” PVC pipes cut
   longitudinally are affixed to the inlet branches to prevent sand from
   flowing into the inlet pipe. Wings are only included on the inlet
   filter modules.

3. Outlet filter module

#. The slots in the outlet branches should be designed so they are small
   enough\ `[l] <#cmnt12>`__\ to prevent sand from passing through. The
   filter modules shall be adequately supported to limit deflection of
   any of the module pipes to 2 millimeters or less to prevent
   significant opening or closing of the slots.
#. During filtration mode, water flows from the filter media into the
   slots and then through the branches and into the trunk pipes.
#. During backwash mode, the outlet trunks are closed or isolated and
   water does not flow through the outlet modules.

7. Backwash Siphon

#. The siphon should be designed so that it is triggered when the
   filters are ready to be backwashed.

8. Backwash Flow Control Weirs

#. The backwash flow control weirs ensure there is adequate flow to
   backwash one filter at all times
#. Removing the flow control weir in front of the desired backwash
   filter will create the desired backwash flow rate for the filter,
   while evenly distributing the remaining flow rate to the other
   filters

9. Sand Dump Pipe

#. A sand dump pipe shall be installed in the filter box to allow for
   the filter media to be removed when the filter is in backwash mode
   and the media bed is expanded.
#. The sand dump pipe must be designed so that if the flow of the sand
   slurry is stopped, that the sand doesn’t collect at one location in
   the pipe and cause a clog.

.. container:: c28

   `[a] <#cmnt_ref1>`__\ Does anyone know where the images in the
   technical brochure are saved? They could be very useful for this
   specifications
   document: https://static1.squarespace.com/static/59836e25f5e231bc4fdb06a4/t/5f88c82efce9e23ae01b0f81/1602799666422/Technical+Overview+2020.pdf

.. container:: c28

   `[b] <#cmnt_ref2>`__\ They are saved here - let me know if you can
   access
   this: https://drive.google.com/drive/folders/1wB1Cl_ocSZjxW_SR1Ehl4ysVYgmq_dgU?usp=sharing

.. container:: c28

   `[c] <#cmnt_ref3>`__\ moved list of specs under IP responsibility
   here for
   now: https://docs.google.com/document/d/1tlV2dqH6ysCXvLNj6YlXxYpzU2dlrW-g9VDNqO3JvFQ/edit?usp=sharing

.. container:: c28

   `[d] <#cmnt_ref4>`__\ should get someone who doesn't know anything
   about AguaClara plants to read through this and make sure it makes
   sense

.. container:: c28

   `[e] <#cmnt_ref5>`__\ @walker.grimshaw@gmail.com
   @ctsang@aguaclarareach.org 

   I reviewed the flocculator section. All looks great to me, except I
   think some more work is needed to clean up the end of the Flow paths
   section (2d-2f). I could probably spend some time on that section
   tomorrow or this weekend depending on how you're feeling Walker. Just
   let me know.

.. container:: c28

   `[f] <#cmnt_ref6>`__\ @monroews@gmail.com the textbook mentions that
   we don't want high local G values that will shear flocs, and we
   address this with Gmax/Gcs and H/S. Is there a Gmax value that we
   always want to be below though, in case other designers approach this
   differently?

.. container:: c28

   `[g] <#cmnt_ref7>`__\ @walker.grimshaw@gmail.com
   @mwebershirk@aguaclarareach.org 

   Does each flocculation channel always need to have its own separate
   drain pipe and valve, or can the drain pipes all lead to one larger
   drain pipe with a big valve on it? I'm guessing you need separate
   valves because with a combined manifold you'd get short-circuiting.
   If so, might be good to emphasize that here.

.. container:: c28

   `[h] <#cmnt_ref8>`__\ I actually don't think it would be a problem to
   have a sort of manifold with one large valve to drain the
   flocculation channels for maintenance. Since the plant would be
   offline when draining the flocculators, I think any kind of short
   circuiting would be fine, and the water level will remain at the same
   level in each channel.

.. container:: c28

   `[i] <#cmnt_ref9>`__\ But even if the combined large-diameter valve
   is shut, won't the manifold still be connecting the floc channels to
   one another? Seems to me you could still get short-circuiting, which
   would only be limited by the headloss through the drain pipes?

.. container:: c28

   `[j] <#cmnt_ref10>`__\ @mwebershirk@aguaclarareach.org - We made some
   assumptions based on the changes to the textbook, can you give this
   section a quick read through to make sure we explained everything
   correctly? Thanks!

   \_Assigned to Monroe Weber-Shirk\_

.. container:: c28

   `[k] <#cmnt_ref11>`__\ Question for APP - Specifications for sand
   grain size

.. container:: c28

   `[l] <#cmnt_ref12>`__\ Question for APP - size of slots?
