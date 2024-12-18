.. _title_Chemical_Dosing:

*************************
Chemical Dosing
*************************

.. add design information from textbook where it exists 

General Chemical Dosing
-----------------------

Purpose and Description
^^^^^^^^^^^^^^^^^^^^^^^

The coagulation and disinfection processes require the precise dosage of coagulant to the plant influent and calcium hypochlorite to the plant effluent. To carry out this process without pumps, the AguaClara plant uses a hydraulic dosing system.

The main components of the system are:

* Tanks to store the coagulant and chlorine stock solutions
* An elevated platform to support the chemical storage tanks at the correct elevation for gravity powered dosing
* A flow measurement calibration column for each chemical
* A pair of constant level tanks (CLTs) with float valves that maintain a constant level for both chemical solutions
* Two dosing tube modules that provide the necessary relationship between pressure drop and chemical flow rates for each chemical
* A chemical doser (the balance) that connects the water level in the plant's entrance tank to the level at the outlet of the chemical dosing system

This system has the characteristic of maintaining a constant chemical **dosage** even as the flow rate through the plant varies. The plant operator can vary the chemical dosage directly, without doing any calculations, and without having to manipulate the system every time the flow rate in the plant changes. The AguaClara dosing system provides the added benefit of automatically turning off the chemical flow when there is no flow in the plant. This provides security against contamination with excess chemicals and chemical waste in the event that the plant is shut down inadvertently as may occur if the transmission line is damaged.

Chemical Flow Path
^^^^^^^^^^^^^^^^^^
The liquid chemical stock solutions are prepared and stored in the chemical stock tanks, on the chemical platform. Chemicals exit the stock tanks through a sloped tube settler to remove sediment and then continue on to the constant level tanks (CLT). The CLT uses a float valve to provide a relatively constant chemical level. The chemicals exit the CLT and flow to a set of dosing tubes that serve as linear resistors with head loss proportional to the chemical flow rate. The chemicals continue to the dose controller where the operator can set the chemical dosages by adjusting the position of a slider. The chemicals leaving the dose controller are then routed to the chemical drip locations. The coagulant (along with chemicals used for pH adjustment if necessary) is dripped into the LFOM and the chlorine is dripped into the filter exit tank.

Specifications
^^^^^^^^^^^^^^
.. _table_Chemical_Dosing_General_Specifications:
.. csv-table:: Chemical Dosing General Specifications
   :header: "Parameter", "Value"
   :align: left
   :widths: 70 30
   :class: wraptable

   Plant maximum flow rate,  :sub:`($..et.lfom.Qm_max) no-sub`
   Maximum head loss thru doser tubes, :sub:`($..doserTubes.HL_max) no-sub`
   Coagulant stock concentration, :sub:`($..chemPipes.coagStockC) no-sub`
   Coagulant maximum dose, :sub:`($..chemPipes.coagDoseCm_max) no-sub`
   Coagulant maximum flow rate, :sub:`($..chemPipes.coagQu_max) no-sub`
   Chlorine stock concentration, :sub:`($..chemPipes.chlorineStockC) no-sub`
   Chlorine maximum dose, :sub:`($..chemPipes.chlorineDoseCm_max) no-sub`
   Chlorine maximum flow rate, :sub:`($..chemPipes.chlorineQu_max) no-sub`

Chemical Stock Tanks
--------------------
Purpose and Description
^^^^^^^^^^^^^^^^^^^^^^^
The chemical stock tanks are used to store the following chemicals: coagulant, chlorine, and if necessary, chemicals used for pH adjustment. There are two storage tanks for each chemical.

.. photo here

.. csv-table:: Chemical Platform Overview
   :header: "Key", "Description"
   :align: left
   :widths: 20 80
   :class: wraptable

   "1", "Chemical stock platform"
   "2", "Coagulant stock tanks"
   "3", "Chlorine stock tanks"

If applicable, stock tanks used for pH adjustment will also be located on the chemical platform.

.. photo here

The valves with the orange handles are compatible with chlorine and other chemicals, and have chemical-resistant o'rings.

.. csv-table:: Chemical Platform - Bottom View
   :header: "Key", "Description"
   :align: left
   :widths: 20 80
   :class: wraptable

   "4", "Chemical pipes - tank to CLT"
   "5", "Chemical drain pipes"
   "6", "Valve for chemical drainage"
   "7", "Union to connect chemical piping to CLT"
   "8", "Pipe clamping hangers"


.. photo here

.. csv-table:: Chemical Platform - Section View
   :header: "Key", "Description"
   :align: left
   :widths: 20 80
   :class: wraptable

   "9", "Through-wall adaptor for chemical tank to CLT piping"
   "10", "Tube settler"
   "11", "Through-wall adaptor for chemical tank to drain piping"

Specifications
^^^^^^^^^^^^^^
.. csv-table:: Chemical Platform Specifications
   :header: "Key", "Parameter", "Value"
   :align: left
   :widths: 20 80
   :class: wraptable

   "1", "Chemical stock platform", ""
   "", "Width", "INPUTVALUE"
   "", "Length", "INPUTVALUE"
   "", "Distance between top of plant floor and top of platform floor", "INPUTVALUE"
   "2", "Coagulant tank volume", "INPUTVALUE"
   "3", "Chlorine tank volume", "INPUTVALUE"
   "4", "Soda ash tank volume", "INPUTVALUE"
   "5-11", "Dose and drain plumbing size", "INPUTVALUE"
   "", "Height of stock tanks above constant head tanks", "INPUTVALUE"
   "", "Maximum head loss through the float valve orifice", "INPUTVALUE"


All of the chemical feed and drain piping uses a nominal diameter of ND.CoagPiping. The piping that connects to the constant level tanks begins at a bulkhead fitting set at an elevation of B.StockOutlet higher than the bottom of the stock tanks to prevent sediment from entering the pipes. 


Constant Level Tanks
--------------------

Purpose and Description
^^^^^^^^^^^^^^^^^^^^^^^
The constant level tank (CLT) system provides convenient central controls for selection of stock tank, flow calibration, purging sediment, and selection of which of the duplicate chemical feed systems to use. The system has built in redundancy with duplicate systems for dosing each chemical to facilitate routine cleaning and maintenance. The dosing system controls are centralized around the constant level tanks (see :numref:`figure_clt_overview`).

.. _figure_clt_overview:

.. figure:: Images/clt_overview.png
    :width: 400px
    :align: center
    :alt: constant level tank overview

    Overview of the constant level tank module mounted on the side of the chemical stock tank platform.

.. csv-table:: CLT Overview Figure Key
   :header: "Key", "Description"
   :align: left
   :widths: 20 80
   :class: wraptable

   "1", "Chlorine stock tank volume and flow calibration column sight tube"
   "2", "Constant level tank"
   "3", "Dosing tube module"

The constant level tanks prevent the changing chemical levels in the stock tanks from influencing the flow rate through the dosing system. Float valves maintain a relatively constant level of chlorine and coagulant. The float valves are sized to provide up to the maximum chemical flow rate of :sub:`($..chemPipes.chemQu_max) no-sub` given the minimum head provided by stock tanks (:sub:`($..floatvalveHL_bod) no-sub`).

.. _figure_clt_details:

.. figure:: Images/clt_details.png
    :width: 300px
    :align: center
    :alt: constant level tank details

    Constant level tank with associated valves and dosing tubes. The valves with orange handles are compatible with chlorine and have chlorine resistant o'rings.
    .. add something about soda ash here as well

.. csv-table:: CLT Details Figure Key
   :header: "Key", "Description"
   :align: left
   :widths: 20 80
   :class: wraptable

   "1", "Coagulant stock tank volume and flow calibration column sight tube"
   "2", "Valve to select constant level tank and dosing tube set"
   "3", "Float valve to provide constant level of coagulant"
   "4", "Constant level tank"
   "5", "Air vent to discharge bubbles from dosing tubes"
   "6", "Valve to select which stock tank to use"
   "7", "Dosing tubes to provide linear relationship between chemical flow rate and head loss"
   "8", "Valve to drain constant level tank (for cleaning with vinegar)"
   "9", "Sediment trap to capture particles from the stock tank"
   "10", "Valve to purge the sediment trap"
   "11", "Connection to feed line to the doser"
   "12", "Valve to drain the line going to the doser (for cleaning with vinegar)"

There is a pair of constant level tanks for each chemical feed. The specifications for each tank is given in :numref:`table_Constant_Level_Tank_Specifications`.

Specifications
^^^^^^^^^^^^^^
.. _table_Constant_Level_Tank_Specifications:

.. csv-table:: Constant level tank specifications
   :header: "Parameter", "Value"
   :align: left
   :widths: 50 50
   :class: wraptable

   Minimum head provided by stock tanks,  :sub:`($..floatvalveHL_bod) no-sub`
   Maximum head loss through the float valve orifice,  :sub:`($..floatValve.HL_max) no-sub`
   Float valve orifice diameter, :sub:`($..floatValve.orificeD) no-sub`
   Tank inner length, :sub:`($..clt.tankL) no-sub`
   Tank inner width, :sub:`($..clt.tankW) no-sub`
   Tank depth, :sub:`($..clt.tankH) no-sub`
   Tank fluid depth, :sub:`($..clt.tankHW) no-sub`


Dosing Tubes
------------

Purpose and Description
^^^^^^^^^^^^^^^^^^^^^^^
Dosing tubes use laminar flow in a long straight small diameter tube to establish a linear relationship between head loss and flow rate. The velocity in the tubes is limited to ensure that minor losses that scale with velocity squared remain less than :sub:`($..doserTubes.minorHL_pi) no-sub` of the maximum head loss, :sub:`($..doserTubes.HL_max) no-sub`, is from minor losses. 

The number of dosing tubes is increased as needed to ensure that the maximum allowable tube velocity is not exceeded. The dosing tubes are mounted in a module 
.. was there more to this story?

.. _figure_dosing_tube_module:

.. figure:: Images/dosing_tube_module.png
    :width: 300px
    :align: center
    :alt: constant level tank details

    The dosing tubes are assembled in a module to facilitate cleaning and replacement.

.. csv-table:: Dosing Tubes Figure Key
   :header: "Key", "Description"
   :align: left
   :widths: 20 80
   :class: wraptable

   "1", "Reducer"
   "2", "Union"
   "3", "Part of union that is glued to the pipe shield and disk"
   "4", "Dosing tubes"
   "5", "Pipe shield that maintains the dosing tubes in tension"
   "6", "PVC disk that is glued to the union and that has slightly undersized holes for the dosing tubes"
   "7", "Isometric view of the union showing that the dosing tubes are visible above the disk"

Specifications
^^^^^^^^^^^^^^^
The coagulant dosing tube specifications are given below.

.. _table_Coagulant_Dosing_Tube_Specifications:

.. csv-table:: Coagulant dosing tube specifications
   :header: "Parameter", "Value"
   :align: left
   :widths: 50 50
   :class: wraptable

   Number of tubes per module,  :sub:`($..coagDoserTube.N) no-sub`
   Tube inner diameter, :sub:`($..coagDoserTube.tube.ID) no-sub`
   Tube outer diameter, :sub:`($..coagDoserTube.tube.OD) no-sub`
   Tube length, :sub:`($..coagDoserTube.tube.L) no-sub`
   Pipe guard length, :sub:`($..coagDoserTube.shell.pipe.L) no-sub`
  
The chlorine dosing tube specifications are given below.

.. _table_Chlorine_Dosing_Tube_Specifications:

.. csv-table:: Chlorine dosing tube specifications
   :header: "Parameter", "Value"
   :align: left
   :widths: 50 50
   :class: wraptable

   Number of tubes per module,  :sub:`($..chlorineDoserTube.N) no-sub`
   Tube inner diameter, :sub:`($..chlorineDoserTube.tube.ID) no-sub`
   Tube outer diameter, :sub:`($..chlorineDoserTube.tube.OD) no-sub`
   Tube length, :sub:`($..chlorineDoserTube.tube.L) no-sub`
   Pipe guard length, :sub:`($..chlorineDoserTube.shell.pipe.L) no-sub`
  

Chemical Dose Controller
--------------------
.. insert blurb about textbook

Purpose and Description
^^^^^^^^^^^^^^^^^^^^^^^
The chemical dose controller makes it easy and accurate to dose chemicals. The flow of chemicals automatically adjusts to changes in the plant flow rate to keep a constant dose, set by the operator. When a turbidity event occurs, the operator can change the dose of coagulant by moving the coagulant slider lower on the lever to increase the dose. The slider has labelled marks so the operator can record the dose accurately.

.. image of doser

.. sentence about soda ash

.. csv-table:: Chemical Dose Controller
   :header: "Key", "Description"
   :align: left
   :widths: 20 80
   :class: wraptable

   "1", "Doser slider"
   "2", "Lever"
   "3", "Float"
   "4", "Counterweight"
   "5", "Chemical pipes from CLT"
   "6", "Clamping hangers for chemical pipes from CLT"
   "7", "Tubes from CLT piping to doser"
   "8", "Tee connector between dosing and injection tubes"
   "9", "Tubes from doser to injection plumbing/points"

Specifications
^^^^^^^^^^^^^^
.. csv-table:: Chemical Dose Controller Specifications
   :header: "Key", "Parameter", "Value"
   :align: left
   :widths: 20 80
   :class: wraptable

   "5-6", "CLT to doser pipes plumbing size", "INPUTVALUE"
   "7-9", "Chemical tube size", "INPUTVALUE"


Injection Points
-----------------

Purpose and Description
^^^^^^^^^^^^^^^^^^^^^^^
The chemical must be injected into the flow of water within the plant. 
* Coagulant: The coagulant is dripped into the top of the LFOM in the entrance tank.
* Chlorine: The chlorine is dripped into the water exiting the filter on its way to the community water storage tank.
* pH adjustment: If pH adjustment is required, it will be dripped into the LFOM with the coagulant.

.. insert photo

Additional doser arm and injection points are added for pH adjustment.

.. csv-table:: Coagulant Injection Point
   :header: "Key", "Description"
   :align: left
   :widths: 20 80
   :class: wraptable

   "1", "Linear dose controller"
   "2", "Coagulant injection tube"
   "3", "LFOM"

.. insert photo

.. csv-table:: Chlorine Injection Point
   :header: "Key", "Description"
   :align: left
   :widths: 20 80
   :class: wraptable

   "4", "Tube from linear dose controller"
   "5", "Reducing adaptor"
   "6", "Piping to injection point"
   "7", "Drain channel"
   "8", "Clamping hangers"
   "9", "Union connector"
   "10", "PVC disc with hole for tube"
   "11", "Injection tube"
   "12", "In-filter straight connector for pipe encasing injection tube"
   "13", "Piping encasing injection tube"
   "14", "Exit pipe"
   "15", "Filter exit box"

Specifications
^^^^^^^^^^^^^^
.. csv-table:: Injection Point Specifications
   :header: "Key", "Parameter", "Value"
   :align: left
   :widths: 20 80
   :class: wraptable

   "2", "Coagulant injection tube ND", "INPUTVALUE"
   "4 & 11", "Chlorine injection tube ND", "INPUTVALUE"
   "6", "Plumbing to chlorine injection point ND", "INPUTVALUE"
   "12", "Piping encasing injection tube ND", "INPUTVALUE"
