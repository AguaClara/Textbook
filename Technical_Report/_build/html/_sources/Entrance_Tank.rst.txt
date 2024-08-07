.. _title_Entrance_Tank:

*************
Entrance Tank
*************

:sub:`($..lfom.rowN) no-sub`


The entrance tank (see :numref:`figure_spec_ET_Diagram_Labeled`) has multiple functions in a drinking water treatment plant.

#. Remove air bubbles to reduce splashing, turbulence, and unsteady motion of the chemical feed surface tracking lever system
#. Remove grit to prevent accumulation in the flocculator
#. Remove leaves and other debris to prevent clogging of the diffusers in the clarifier inlet
#. Dissipate kinetic energy to keep the water level steady for accurate flow measurement
#. Measure the incoming flow rate with the Linear Flow Orifice Meter (LFOM) so that operators can make adjustments and respond to changes in water demand
#. Inject the coagulant and any other amendments required for flocculation

.. _figure_spec_ET_Diagram_Labeled:

.. figure:: ../Textbook/Images/ET_Diagram_Labeled.png
    :width: 900px
    :align: center
    :alt: entrance tank diagram

    Cross-section of an entrance tank. Chemical dosing system not shown.


Trash Rack
==========

The trash rack is designed to remove any particles that would be large enough to obstruct downstream processes. The smallest flow dimensions are the diffusers in the clarifier with a width of :sub:`($..inletManifold.diffuser.slotW) no-sub` and the orifices in the stacked rapid sand filter inlet branches with a diameter of :sub:`($..filter.fiPipes.branch.inlet.portD) no-sub`. The spacing between the trashrack wires is :sub:`($..trashRack.Sm) no-sub`.

The trash rack area shall be sufficient such that it can be at least :sub:`($..et.trashRack.PO_pi) no-sub` clogged before exceeding the maximum available head loss of :sub:`($..et.trashRack.HL_max) no-sub` in the entrance tank.

.. _table_Trash_Rack_Specifications:

.. csv-table:: Trash Rack Specifications.
   :header: "Parameter", "value"
   :align: left
   :widths: 50 50

   Channel width, :sub:`($..trashRack.W) no-sub`
   Trash rack height, :sub:`($..et.trashRack.L) no-sub`
   Fractional open area, :sub:`($..et.trashRack.PO) no-sub`
   Downstream water depth, :sub:`($..et.trashRack.downstreamHW) no-sub`
   Clean head loss, :sub:`($..et.trashRack.HL_min) no-sub`
   Maximum head loss, :sub:`($..et.trashRack.HL_max) no-sub`
   Wire or cable diameter, :sub:`($..et.trashRack.Dm) no-sub`
   Open space between wires, :sub:`($..et.trashRack.Sm) no-sub`


Sediment and Grit Removal
=========================

Water enters the plant on the left side of the entrance tank shown in :numref:`figure_spec_ET_Diagram_Labeled` and flows  the top of the inverted pyramidal traps, or hoppers, at the bottom of the tank. The first hopper contains an overflow pipe to waste any water entering the plant in excess of the plant flow rate. The overflow pipe has a nominal diameter of :sub:`($..et.overflow.ND) no-sub` inches, sized to handle the total plant flow rate. A drain pipe stub is installed in each hopper, allowing the operator to . The ND.EtFlowControl nominal diameter drain is designed to handle the drain the full plant flow rate if needed.

Large particulates settle out into the hoppers, and collect near the drains at the bottom. When the water reaches the end of the tank, it flows through the orifices of the riser pipe, which acts as a linear flow orifice meter (LFOM). It is designed for a capture velocity of W.EtCapture to remove these particulates. A length of L.Et is assigned to the entrance tank to correspond to the sedimentation tank length plus enough space to fit the float of the chemical dose controller and the rapid mix pipes. The width, W.Et, is then assigned to ensure the minimum desired capture velocity is met while still allowing enough space for a person to fit inside and construct the tank. The depth of the tank is then determined such that the velocity in the upper rectangular portion of the tank does not exceed the velocity in the flocculator, V.Floc, while ensuring the depth is sufficiently small that the drains are easy to access. In this case, the tank has a height of H.Et.

To allow for easy maintenance, N.EtHoppers hoppers must be built into the entrance tank, at an angle of AN.EtSlope, forcing sediments to slide to the bottom where the ND.EtDrain drains are located. When too much sediment has accumulated, the upper drain pipes must be removed until the sludge is flushed out. Directly below the entrance tank, there is a drain channel to collect the waste.
As the raw water flows from the first hopper to the subsequent ones, it must pass through two trash racks, preventing large debris from entering the treatment process. Having two trash racks allows the plant to run with a grit screen even while the operator cleans one of them. The trash racks are made of rebar and slide into two slots built into the entrance tank wall. The center-to-center distance between the rebar, B.EtRebar m, is set to ensure that debris large enough to clog the orifices in the linear flow orifice meter downstream (LFOM) are kept out.

Suspended particulates in the water settle out over the length of the entrance tank into the hoppers below. When enough sludge has accumulated at the bottom, the hopper stops can be removed to flush out the debris down into the drain channel below, and they can then be replaced to resume normal operation. The ND.EtDrain in nominal diameter hopper stop is L.EtDrainStopper m long, ensuring the top of the pipe is above the maximum water height in the tank. Table 3 summarizes the entrance tank design specifications below.

Number of rows of orifices, :sub:`($..et.lfom.rowN) no-sub`


.. include:: lfom.rst