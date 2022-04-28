.. raw:: html
    <embed>
       <link rel="canonical" href="https://aguaclara.github.io/Textbook/AIDE/About/LFOM.html" />
       <script src="https://hypothes.is/embed.js" async></script>
    </embed>


.. list-table::
   :widths: 60 50 30
   :header-rows: 0

   * - |ACRlogowithname|
     - |textbook|
     - |donate|

.. _title_Linear_Flow_Orifice_Meter_Configurable_Component:

************************************************
Linear Flow Orifice Meter Configurable Component
************************************************

.. _figure_LFOM:

.. figure:: LFOM.png
    :width: 150px
    :align: center
    :alt: Linear Flow Orifice Meter

    The Linear Flow Orifice Meter measures the flow of water through the plant and creates a linear relationship between plant flow rate and the depth of water in the entrance tank.


.. _figure_LFOMinPlant:

.. figure:: LFOMinET.png
    :width: 500px
    :align: center
    :alt: Location of the Linear Flow Orifice Meter

    The Linear Flow Orifice Meter (outlined in red) is located in the entrance tank.

Generate New Models of the Linear Flow Orifice Meter
====================================================

Edit the configurations to create new models of the Linear Flow Orifice Meter.

.. _figure_configLFOM:

.. figure:: configLFOM.png
    :width: 300px
    :align: center
    :alt: Linear Flow Orifice Meter configuration

    The configuration options for the Linear Flow Orifice Meter.

.. csv-table:: Linear Flow Orifice Meter configurations.
   :header: "Configuration", "Description"
   :align: left
   :widths: 50, 100

   "Flow (L/s)", "The maximum flow rate sets the size of the Linear Flow Orifice Meter. Vary it to see how the dimensions change."
   Minimum temperature (˚C), The flow is turbulent throughout the Linear Flow Orifice Meter and thus temperature doesn’t have a significant effect on the design.
   Water elevation range (m), Change in water elevation in the entrance tank that corresponds to the flow varying from 0 L/s up to the maximum design flow rate.
   Maximum drill diameter (m), Used to limit the drill bit size required to fabricate the LFOM.
   Maximum nominal diameter (inch), Used to set a maximum pipe size. For higher flow rates the LFOM will increase the water elevation range so the pipe can carry more flow.


Additional information is available in *The Physics of Water Treatment* in the section on `Linear Flow Orifice Meter <https://aguaclara.github.io/Textbook/Flow_Control_and_Measurement/FCM_Design.html#linear-flow-orifice-meter-lfom>`_


.. |donate| image:: donate.png
  :target: https://www.aguaclarareach.org/donate-now
  :height: 40

.. |textbook| image:: textbook.png
  :target: https://aguaclara.github.io/Textbook/AIDE/AIDE.html
  :height: 40

.. |ACRlogowithname| image:: ACRlogowithname.png
  :target: https://www.aguaclarareach.org/
  :height: 40
