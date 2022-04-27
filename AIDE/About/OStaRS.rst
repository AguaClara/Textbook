.. raw:: html
    <embed>
       <link rel="canonical" href="https://aguaclara.github.io/Textbook/AIDE/About/OStaRS.html" />
       <script src="https://hypothes.is/embed.js" async></script>
    </embed>


.. list-table::
   :widths: 60 50 30
   :header-rows: 0

   * - |ACRlogowithname|
     - |textbook|
     - |donate|

.. _title_Open_Stacked_Rapid_Sand_Filter_Configurable_Component:

*****************************************************
Open Stacked Rapid Sand Filter Configurable Component
*****************************************************

.. _figure_OStaRS:

.. figure:: OStaRS.png
    :width: 350px
    :align: center
    :alt: Location of the Entrance Tank

    The open stacked rapid sand filter uses hydraulic controls to ensure steady flow through the filter media and an innovative system to inject and extract water from the sand bed to create six filters working in parallel.


.. _figure_OStaRSinPlant:

.. figure:: OStaRSinPlant.png
    :width: 350px
    :align: center
    :alt: Location of the StaRS filter

    The open stacked rapid sand filter (outlined in red) is .


The entrance tank has four main functions:
==========================================

  #. Remove trash and debris that could potentially clog the diffusers in the inlet manifold to the clarifier.
  #. Remove grit and sand that would otherwise settle in the flocculator.
  #. Measure the flow rate entering the plant using a Linear Flow Orifice Meter.
  #. Automatically vary the chemical feed rates as the plant flow rate changes with the chemical doser.

Generate New Models of the Entrance Tank
========================================

Edit the configurations to create new models of the entrance tank. Some models may fail because the constraints can't all be met.

.. _figure_configOStaRS:

.. figure:: configET.png
    :width: 400px
    :align: center
    :alt: Location of the Entrance Tank

    The configuration options for the Entrance Tank.

.. csv-table:: Entrance tank configurations.
   :header: "Configuration", "Description"
   :align: left
   :widths: 50, 100

   "Flow (L/s)", "The maximum flow rate sets the size of the entrance tank. Vary it to see how the dimensions change."
   Minimum temperature (˚C), The flow is turbulent throughout the entrance tank and thus temperature doesn’t have a significant effect on the design.


Additional information is available in the chapter on `Entrance Tank Design <https://aguaclara.github.io/Textbook/Filtration/Filtration_Design.html>`_


.. |donate| image:: donate.png
  :target: https://www.aguaclarareach.org/donate-now
  :height: 40

.. |textbook| image:: textbook.png
  :target: https://aguaclara.github.io/Textbook/AIDE/AIDE.html
  :height: 40

.. |ACRlogowithname| image:: ACRlogowithname.png
  :target: https://www.aguaclarareach.org/
  :height: 40
