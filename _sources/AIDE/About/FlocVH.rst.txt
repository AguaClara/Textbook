.. raw:: html

    <embed>
       <link rel="canonical" href="https://aguaclara.github.io/Textbook/AIDE/About/FlocVH.html" />
       <script src="https://hypothes.is/embed.js" async></script>
    </embed>


.. list-table::
   :widths: 60 50 30
   :header-rows: 0

   * - |ACRlogowithname|
     - |textbook|
     - |donate|

.. _title_Flocculator_VH_Configurable_Component:

********************************************
Flocculator VH Configurable Component
********************************************

.. _figure_FlocVH:

.. figure:: ./Images/FlocVH.png
    :width: 180px
    :align: center
    :alt: Location of the Entrance Tank

    The flocculator use baffles to create a flow path with 180˚ bends. The flow contracts as it goes around the bend, expands, generates turbulence, and then deforms the fluid as viscosity converts the turbulent kinetic energy into heat. The fluid deformation causes collisions between particles.


.. _figure_FlocVHinPlant:

.. figure:: ./Images/FlocVHinPlant.png
    :width: 150px
    :align: center
    :alt: Location of the Entrance Tank

    The flocculator (outlined in red) is where the raw water particles collide and grow into flocs.

The flocculator has three design constraints:
=============================================

  #. Deform the fluid so there are sufficient collision opportunities for particles.
  #. Maintain a flow expansion geometric ratio (flow width to distance between expansions) that is greater than 4.
  #. Limit the velocity gradient so that flocs can grow large enough to be captured by the plate settlers in the clarifier.

Generate New Models of the Flocculator
========================================

Edit the configurations to create new models of the flocculator. Some models may fail because the constraints can't all be met. Send us |feedback| to share how you are using the Flocculator VH model and to give us suggestions for how to make these models easier to use.

.. _figure_configFloc:

.. figure:: ./Images/configFlocVH.png
    :width: 300px
    :align: center
    :alt: Flocculator configuration

    The configuration options for the Flocculator.

.. csv-table:: Flocculator VH configurations.
   :header: "Configuration", "Description"
   :align: left
   :widths: 50, 100

   "",""
   "Flow (L/s)", "The maximum flow rate sets the size of the flocculator. Vary it to see how the dimensions change."
   "",""
   Minimum temperature (˚C), The water viscosity increases for low temperatures and thus more energy is required (greater head loss) to achieve the same total fluid deformation.
   "",""
   Water depth at exit (m), The flocculator is built on the same slab as the clarifier and the elevation of the water leaving the flocculator must match the water level at the entrance of the clarifier.
   "",""
   Collision potential (Gt), The collision potential is created by the total fluid deformation in the flocculator.
   "",""
   Velocity gradient (1/s), The velocity gradient influences the size of the flocs leaving the flocculator. High velocity gradients all require more energy input (more head loss).


Additional information is available in the chapter on `Flocculator Design <https://aguaclara.github.io/Textbook/Flocculation/Floc_Design.html>`_


.. |donate| image:: ./Images/donate.png
  :target: https://www.aguaclarareach.org/donate-now
  :height: 40

.. |textbook| image:: ./Images/textbook.png
  :target: https://aguaclara.github.io/Textbook/AIDE/AIDE.html
  :height: 40

.. |ACRlogowithname| image:: ./Images/ACRlogowithname.png
  :target: https://www.aguaclarareach.org/
  :height: 40

.. |feedback| image:: ./Images/feedback.png
  :target: https://docs.google.com/forms/d/e/1FAIpQLSdYHVinzW-xZskW74rpZ_7prHAqjLQDwadCNiRP39nyu7NHMw/viewform?
  :height: 25
