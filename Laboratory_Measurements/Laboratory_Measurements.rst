
******************************************
Laboratory Measurements and Procedures
******************************************


Introduction
=============

Measurements of masses, volumes, and preparation of chemical solutions of known composition are essential laboratory skills. The goal of this exercise is to gain familiarity with these laboratory procedures. You will use these skills repeatedly throughout the semester.

Theory
======

Many laboratory procedures require preparation of chemical solutions. Most chemical solutions are prepared on the basis of mass of solute per volume of solution (grams per liter or moles per liter). Preparation of these chemical solutions requires the ability to accurately measure both mass and volume.

Preparation of dilutions is also frequently required. Many analytical techniques require the preparation of known standards. Standards are generally prepared with concentrations similar to that of the samples being analyzed. In environmental work many of the analyses are for hazardous substances at very low concentrations (mg/L or �g/L levels). It is difficult to accurately weigh a few milligrams of a chemical with an analytical balance. Often dry chemicals are in crystalline or granular form with each crystal weighing several milligrams making it difficult to get close to the desired weight. Thus it is often easier to prepare a low concentration standard by diluting a higher concentration stock solution. For example, 100 mL of a 10 mg/L solution of NaCl could be obtained by first preparing a 1 g/L NaCl solution (100 mg in 100 mL). One mL of the 1 g/L stock solution would then be diluted to 100 mL to obtain a 10 mg/L solution.

Absorption spectroscopy is one analytical technique that can be used to measure the concentration of a compound. Solutions that are colored absorb light in the visible range. The resulting color of the solution is from the light that is transmitted. According to Beer's law the attenuation of light in a chemical solution is related to the concentration and the length of the path that the light passes through.

.. math::

    \log \left(\frac{P_o }{P} \right)=\varepsilon bc

where c is the concentration of the chemical species, b is the distance the light travels through the solution, :math:`\varepsilon` is a constant, :math:`P_o` is the intensity of the incident light, and :math:`P` is the intensity of the transmitted light. Absorption, A, is defined as:

.. math::



.. math::

    A=\log \left(\frac{P_{o} }{P} \right)

In practice placePo is the intensity of light through a reference sample (such as deionized water) and thus accounts for any losses in the walls of the sample chamber. From equation 2.1 and 2.2 it may be seen that absorption is directly proportional to the concentration of the chemical species.

.. math::

    A=\varepsilon bc



.. _figure_Spectrophotometer:

.. figure:: Images/Spectrophotometer.png
    :width: 300px
    :align: center
    :alt: Spectrophotometer light path

    Diagram of light path in diode array spectrophotometer




One instrument you may use to measure absorbance is a Hewlett Packard (HP) model 8452A diode array spectrophotometer. The diode array spectrophotometer uses a broad-spectrum source of incident light from a deuterium lamp. The light passes through the sample, 1 cm path length, and is split by a grating into a spectrum of light that is measured by an array of diodes. Each diode measures a bandwidth of 2 nm with 316 diodes covering the range from 190 nm to 820 nm. The wavelengths of light and their colors are given in Table 2-1. The light path for the diode array spectrophotometer is shown in :numref:`figure_Spectrophotometer`.

The HP 8452A spectrophotometer has a photometric range of 0.002 - 3.3 absorbance units. In practice absorbance measurements greater than 2.5 are not very meaningful as they indicate that 99.7\% of the incident light at that wavelength was absorbed. Conversely, an absorbance of 0.002 means that 0.5\% of the incident light at that wavelength was absorbed.

When measuring samples of known concentration the Spectrophotometer software (see Appendix A - Diode Array UV Visible Spectrophotometer) calculates the relationship between absorbance and concentration at a selected wavelength. The slope (m), intercept (b), and correlation coefficient (r) are calculated using equations 2.4 through 2.6.

The slope of the best fit line is

.. math::

    m=\frac{\sum xy -{\textstyle\frac{\sum x \sum y }{n}} }{\sum x^{2}  -\frac{\left(\sum x \right)^{2} }{n} }

The intercept of the line is

.. math::

    \rm b\; }={\rm \; }\bar{y}-{\rm m}\bar{x}

The correlation coefficient is defined as

.. math::

    r=\frac{\sum xy -{\textstyle\frac{\sum x \sum y }{n}} }{\sqrt{\left(\sum x^{2}  -\frac{\left(\sum x \right)^{2} }{n} \right)\left(\sum y^{2}  -\frac{\left(\sum y \right)^{2} }{n} \right)} }  2.6

where x is the concentration of the solute (methylene blue in this exercise), y is the absorbance, and n is the number of samples.

Experimental Objectives
-----------------------

To gain proficiency in:

 1. Calibrating and using electronic balances
 1. Using signal conditioning boxes and data acquisition software
 1. Digital pipetting
 1. Preparing a solution of known concentration
 1. Preparing dilutions
 1. Measuring concentrations using a UV-Vis spectrophotometer


Experimental Methods
--------------------

Mass Measurements
^^^^^^^^^^^^^^^^^

Mass can be accurately measured with an electronic analytical balance. Perhaps because balances are so easy to use it is easy to forget that they should be calibrated on a regular basis. It is recommended that balances be calibrated once a week, after the balance has been moved, or if excessive temperature variations have occurred. In order for balances to operate correctly they also need to be level. Most balances come with a bubble level and adjustable feet. Before calibrating a balance verify that the balance is level.

The environmental laboratory is equipped with balances manufactured by Ohaus.  As part of this exercise, we will calibrate the Ohaus Scout Pro balance (200 g) as follows:

 1. Start with the balance off.
 1. Press and hold the ON/ZERO key until the screen reads 'MENU'.
 1. Releasing the ON/ZERO key will take you to calibration mode indicated by '.C.A.L.' on the screen.
 1. Press the ON/ZERO key to indicate 'Yes' to calibration.
 1. The balance will acquire the zero value (and read -- C -).
 1. Once the zero value is obtained, the balance screen will blink -- 200 g -- indicating that the 200 g mass will be used for the calibration.
 1. Place the 200 g calibration mass on the pan (handle the calibration mass using a cotton glove or tissue paper) and press ON/ZERO key.
 1. The balance will calibrate to the mass added. Remove the mass when the screen reads '200.00 g' indicating the calibration is complete.
 1. )Measure the mass of a second calibration mass of different size (e.g., 100 g) to confirm calibration.
 1. Record relevant data in the attached spreadsheet.

Dry chemicals can be weighed in disposable plastic "weighing boats" or other suitable containers. It is often desirable to subtract the weight of the container in which the chemical is being weighed. The weight of the chemical can be obtained either by weighing the container first and then subtracting, or by "zeroing" the balance with the container on the balance.


Temperature Measurement and ProCoDA
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We will use a data acquisition system designed and fabricated in CEE at Cornell University. Each group has their own ProCoDA box and associated power supply and USB cable. The power supply and USB cable must be plugged into the ProCoDA box and then into the AC power on your lab bench and a USB port on your lab bench computer, respectively.

Use a thermistor to measure the temperature of distilled water. The thermistors are usually hanging on the rack to the right of the fume hoods (you should have one on your bench today). The thermistor has a 4-mm diameter metallic probe. Plug the thermistor into the red signal-conditioning box. The conditioned signal is connected to the ProCoDA box using a red cable. Connect the red cable to one of the sensor ports on the top row of the ProCoDA box.

 1. Monitor the thermistor using the ProCoDA II software.  The software can be found in the desktop folder named 'ProCoDA II'.
 1. Open ProCoDA II
 1. Navigate to the Configuration tab
 1. Click the 'volt' button to select and configure your sensor (thermistor).
 1. Click 'insert sensor' to add a sensor to your list.  As the semester goes on, we will run experiments that require several sensors to be added here.  For now, we will use the single thermistor.
 1. Now you need to tell the software where your sensor is plugged in.  In the 'channels' pull-down menu, select the address of your sensor.  All addresses begin with a Dev/ai prefix.
 1. Finally, you need to tell the software to convert the signal into temperature units.  This is done with a calibration file.  Click 'open calibration file' (it looks like a regular open folder icon) and select the calibration file named thermistor.smc.
 1. You should now be reading temperature in units of degrees Celsius. Verify that you are monitoring the correct temperature probe by holding the temperature probe in your hand and warming it up.  Does the temperature reading respond?
 1. Place the probe in a 100-mL plastic beaker full of distilled water. Wait at least 15 seconds to allow the probe to equilibrate with the solution.
 1. Record this temperature in the attached spreadsheet.


Pipette Technique
^^^^^^^^^^^^^^^^^

 1. Use Figure 2-2 to estimate the mass of 990 :math:`\mu L` of distilled water (at the measured temperature).
 1. Use a 100-1000 :math:`\mu L` digital pipette to transfer 990 :math:`\mu L` of distilled water to a tared weighing boat on either the AdventurerPro or Galaxy analytical balance. Record the mass of the water and compare with the expected value (Figure 2-2). Repeat this step if necessary until your pipetting error is less than 2\%, then measure the mass of 5 replicate 990 :math:`\mu L` pipette samples. Calculate the mean (:math:`\bar{x}` defined in equation 2.7), standard deviation (s defined in equation 2.8), and coefficient of variation, :math:`\frac{s}{\bar{x}}`, for your measurements. The coefficient of variation (c.v.) is a good measure of the precision of your technique. For this test a c.v. :math:`\mathrm{<}`1\% should be achievable.

.. math::

    \bar{x}={\rm \; }\frac{\sum x }{n}  2.7

.. math::

    {\rm s\; }={\rm \; }\sqrt{\frac{\sum x^{2}  -\frac{(\sum x )^{2} }{n} }{n-1} }  2.8


Note that these functions are defined in most coding environments and that the predefined functions should be used.

 \includegraphics*[width=2.84in, height=2.11in, keepaspectratio=false]{image2}

 Figure  2-2. Density of water vs. temperature.

See :numref:`figure_mountain` for a typical mountain view.

.. _figure_Density_vs_temperature:

.. figure:: Images/Density_vs_temperature.png
    :width: 300px
    :align: center
    :alt: Density of water vs. temperature

    Density of water vs. temperature.


Measure Density
^^^^^^^^^^^^^^^

 1. Weigh a 100 mL volumetric flask with its cap (use either the \textit{Scout Pro 200 g} or the \textit{Galaxy} analytical balance).
 1. Prepare 100 mL of a 1 M solution of sodium chloride in the weighed flask. You can also dissolve the NaCl in a clean beaker and transfer to the volumetric flask.  Make sure to mix the solution and then verify that you have \textbf{exactly 100 mL} of solution. Note that the combined \textbf{volume of NaCl and water decreases} as the salt dissolves.
 1. Weigh the flask (with its cap) plus the sodium chloride solution and calculate the density of the 1 M NaCl solution.

Prepare red dye standards of several concentrations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

 1. A red dye stock solution of 1 g/L has been prepared. Use it to prepare 100 mL of each of the following concentrations: 1 mg/L, 2 mg/L, 3 mg/L, 4 mg/L, and 5 mg/L.  Record your calculations in the attached spreadsheet.
 1. Note any errors in transfer of mass as you prepare these dilutions (the color will make it easy to see).

Measure a standard curve and an unknown
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

 .. todo:: need to create a method here!


Pre-Laboratory Questions
------------------------

 1. You need 100 mL of a 1 �M solution of zinc that you will use as a standard to calibrate an atomic adsorption spectrophotometer. Find a source of zinc ions combined either with chloride or nitrate (you can use the internet or any other source of information). What is the molecular formula of the compound that you found? Zinc disposal down the sanitary sewer is restricted at Cornell and the solutions you prepare may need to be disposed of as hazardous waste. As an environmental engineering student you strive to minimize waste production. How would you prepare this standard using techniques readily available in the environmental laboratory so that you minimize the production of solutions that you don't need? Note that we have pipettes that can dispense volumes between 10 ?L and 1 mL and that we have 100 mL and 1 L volumetric flasks. Include enough information so that you could prepare the standard without doing any additional calculations. Consider your ability to accurately weigh small masses. Explain your procedure for any dilutions. Note that the stock solution concentration should be an easy multiple of your desired solution concentration so you don't have to attempt to pipette a volume that the digital pipettes can't be set for such as 13.6 ?L.
 1. The density of sodium chloride solutions as a function of concentration is approximately :math:`0.6985C + \rho_{water}`. What is the density of a 1 M solution of sodium chloride?


Data Analysis and Questions
---------------------------

Submit one spreadsheet containing the data sheet, exported absorbance data, graphs and answers to the questions.


 1. Fill out the Excel data sheet available from the course syllabus. Make sure that all calculated values are entered in the spreadsheet as equations. Failure to use the spreadsheet to do the calculations will not receive full credit. Note that this is likely the only assignment that we will do using Excel. All remaining analysis for the course will be done in Atom!
 1. Create a graph of absorbance at 660 nm vs. concentration of methylene blue in Atom using the exported data file. Does absorbance at 660 nm increase linearly with concentration of methylene blue?
 1. Plot ? as a function of wavelength for each of the standards on a single graph. Note that the path length is 1 cm. Make sure you include units and axis labels on your graph. If Beer's law is obeyed what should the graph look like?
 1. Did you use interpolation or extrapolation to get the concentration of the unknown?
 1. )What colors of light are most strongly absorbed by methylene blue?
 1. What measurement controls the accuracy of the density measurement for the NaCl solution? What density did you expect (see prelab 2)? Approximately what should the accuracy be?
 1. Don't forget to write a brief paragraph on conclusions and on suggestions using Markdown.
 1. Verify that your report and graphs meet the requirements as outlined in the course materials.


Lab Prep Notes
--------------

 Table 2-2. Reagent list.

\begin{tabular}{|p{0.7in}|p{0.7in}|p{0.7in}|} \hline
\textbf{\newline Description} & \textbf{\newline Supplier} & \textbf{Catalog number} \\ \hline
NaCl & Fisher Scientific &  BP358-1  \\ \hline
Methylene blue & Fisher Scientific & M291-25 \\ \hline
\end{tabular}

Table 2-3. Equipment list

\begin{tabular}{|p{1.1in}|p{1.1in}|p{0.8in}|} \hline
\textbf{\newline Description} & \textbf{\newline Supplier} & \textbf{Catalog number} \\ \hline
Calibra 100-1095 �L & Fisher Scientific & 13-707-5 \\ \hline
Calibra 10-109.5 �L & Fisher Scientific & 13-707-3 \\ \hline
DI 100 analytical toploader & Fisher Scientific & 01-913-1A \\ \hline
DI-800 Toploader & Fisher Scientific & 01-913-1C \\ \hline
100 mL volumetric & Fisher Scientific & 10-198-50B \\ \hline
UV-Vis spectrophotometer & Hewlett-Packard Company & 8452A \\ \hline
\end{tabular}

Table 2-4. Methylene Blue Stock Solution

\begin{tabular}{|p{0.6in}|p{0.5in}|p{0.6in}|p{0.5in}|} \hline
\textbf{Description} & \textbf{MW (g/M)} & \textbf{conc. (g/L)} & \textbf{100 mL} \\ \hline
C16H18N3SCl & 319.87 & 1 & 100.0 mg \\ \hline
\end{tabular}




Setup
^^^^^
 1. Prepare stock methylene blue solution and distribute to student workstations in 20 mL vials.
 1. )Prepare 100 mL of unknown in concentration range of standards. Divide into two bottles (one for each spectrophotometer).
 1. Verify that spectrophotometers are working (prepare a calibration curve as a test).
 1. Verify that balances calibrate easily.
 1. Disassemble, clean, and lubricate all pipettes.
