.. _title_Clarifier:

*********
Clarifier
*********

Design information for the AguaClara clarifier is available in `the Clarifier Design chapter of The Physics of Water Treatment Design <https://aguaclara.github.io/Textbook/Clarification/Clarifier_Design.html>`_


Purpose and Description
=======================

The clarifier

.. _figure_dummy:

.. figure:: Images/turbid_water_sample.jpg
    :width: 100px
    :align: center
    :alt: turbid water sample

    The cloudy water in the bottle is caused by suspended particles. The goal of the flocculator is to increase the size of the particles so that they have a higher terminal velocity.

    ===  ============
    Key  Description
    ===  ============
     1   polycarbonate baffle 
     2   plastic washer
     3   spacer pipe that sets the spacing between baffles
     4   frame pipe that connects everything together
    ===  ============


Design Data
===========

.. _table_Clarifier_Civil_Construction_Parameters:

.. csv-table:: Clarifier Civil Construction Parameters.
    :header: "Parameter", "value"
    :align: left
    :widths: 50 50
    :class: wraptable

    
    Overall clarifier width, :sub:`($..plant.clarifier.OW) no-sub`
    Overall clarifier length, :sub:`($..clarifier.OL) no-sub`
    Height of clarifier measured from the bottom of the jet reverser, :sub:`($..clarifier.H ) no-sub`
    Number of clarifier chambers, :sub:`($..clarifier.bay.N) no-sub`
    Inside width of each chamber, :sub:`($..clarifier.bay.W) no-sub`
    Inside length of each chamber, :sub:`($..clarifier.bay.L) no-sub`
    Main chamber hopper angle, :sub:`($..clarifier.slopeAN) no-sub`
    **Channels**
    Channel wall height, :sub:`($..clarifier.channels.tank.H) no-sub`
    Inlet channel width, :sub:`($..clarifier.channels.inletPreWeirW) no-sub`
    Channel elevation increase per outlet,  :sub:`($..clarifier.channels.inletPreWeirDeltaH) no-sub`
    Flocculation failure waste channel width, :sub:`($..clarifier.channels.inletPostWeirW) no-sub`
    Flocculation failure weir height, :sub:`($..clarifier.channels.inletWeir.W) no-sub`
    Flocculation failure drain nominal diameter, :sub:`($..clarifier.channels.dump.ND) no-sub` inch
    Effluent collector channel width, :sub:`($..clarifier.channels.outletPreWeirW) no-sub`
    Effluent collector channel drain nominal diameter, :sub:`($..clarifier.channels.clarifiedPreWeirND) no-sub`
    Effluent manifold weir height, :sub:`($..clarifier.channels.outletWeirH) no-sub`
    Outlet channel width, :sub:`($..clarifier.channels.outletPostWeirW) no-sub`
    Outlet channel drain nominal diameter, :sub:`($..clarifier.channels.dump.ND) no-sub` inch

    **Floc Hopper**
    Floc hopper weir height, :sub:`($..clarifier.hoppers.concreteWeirH) no-sub`
    Floc hopper cone angle, :sub:`($..clarifier.hoppers.slopeAN) no-sub`
    Floc hopper cone height, :sub:`($..clarifier.hoppers.coneH) no-sub`
    Floc hopper cone top diameter, :sub:`($..clarifier.hoppers.hopperD) no-sub`
    Floc hopper access port nominal diameter, :sub:`($..clarifier.hopperPort.ND) no-sub`


    
.. _table_Clarifier_Hydraulic_Parameters:

.. csv-table:: Clarifier Hydraulic Parameters.
    :header: "Parameter", "value"
    :align: left
    :widths: 50 50
    :class: wraptable

    **Inlet Manifold**
    , :sub:`($..clarifier.hoppers.sludgeDrain.ND) no-sub`
    **Sludge drains**,
    Sludge drain nominal diameter, :sub:`($..clarifier.hoppers.sludgeDrain.ND) no-sub`
    Sludge bleed valve nominal diameter, :sub:`($..clarifier.hoppers.sludgeBleed.ND) no-sub`


.. _table_Clarifier_Plate_Settlers:

.. csv-table:: Clarifier Plate Settlers.
    :header: "Parameter", "value"
    :align: left
    :widths: 50 50
    :class: wraptable

    
    Sludge drain nominal diameter, :sub:`($..clarifier.hoppers.sludgeDrain.ND) no-sub`