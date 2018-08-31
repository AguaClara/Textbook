
******************************************
Laboratory Measurements and Procedures
******************************************


Introduction
=============

Measurements of masses, volumes, and preparation of chemical solutions of known composition are essential laboratory skills. The goal of this exercise is to gain familiarity with these laboratory procedures. You will use these skills repeatedly throughout the semester.

Theory
========

Many laboratory procedures require preparation of chemical solutions. Most chemical solutions are prepared on the basis of mass of solute per volume of solution (grams per liter or moles per liter). Preparation of these chemical solutions requires the ability to accurately measure both mass and volume.

Preparation of dilutions is also frequently required. Many analytical techniques require the preparation of known standards. Standards are generally prepared with concentrations similar to that of the samples being analyzed. In environmental work many of the analyses are for hazardous substances at very low concentrations (mg/L or �g/L levels). It is difficult to accurately weigh a few milligrams of a chemical with an analytical balance. Often dry chemicals are in crystalline or granular form with each crystal weighing several milligrams making it difficult to get close to the desired weight. Thus it is often easier to prepare a low concentration standard by diluting a higher concentration stock solution. For example, 100 mL of a 10 mg/L solution of NaCl could be obtained by first preparing a 1 g/L NaCl solution (100 mg in 100 mL). One mL of the 1 g/L stock solution would then be diluted to 100 mL to obtain a 10 mg/L solution.

Absorption spectroscopy is one analytical technique that can be used to measure the concentration of a compound. Solutions that are colored absorb light in the visible range. The resulting color of the solution is from the light that is transmitted. According to Beer's law the attenuation of light in a chemical solution is related to the concentration and the length of the path that the light passes through.
\[\log \left(\frac{P_{o} }{P} \right)=\varepsilon bc 2.1\]
where c is the concentration of the chemical species, b is the distance the light travels through the solution, ? is a constant, placePo is the intensity of the incident light, and P is the intensity of the transmitted light. Absorption, A, is defined as:
\[A=\log \left(\frac{P_{o} }{P} \right) 2.2\]
In practice placePo is the intensity of light through a reference sample (such as deionized water) and thus accounts for any losses in the walls of the sample chamber. From equation 2.1 and 2.2 it may be seen that absorption is directly proportional to the concentration of the chemical species.
\[A=\; \varepsilon bc 2.3\]

\begin{tabular}{|p{0.7in}|p{0.9in}|} \hline
\multicolumn{2}{|p{1in}|}{Table 2-1. Wavelengths of light\textbf{}} \\ \hline
\textbf{color} & \textbf{wavelength (nm)} \\ \hline
ultra violet & 190-380 \\ \hline
violet & 380-450 \\ \hline
blue & 450-490 \\ \hline
green & 490-560 \\ \hline
yellow & 560-590 \\ \hline
orange & 590-630 \\ \hline
red & 630-760 \\ \hline
\end{tabular}


.. _figure_Spectrophotometer:

.. figure:: Images/Spectrophotometer.png
    :width: 300px
    :align: center
    :alt: Spectrophotometer light path

    Diagram of light path in diode array spectrophotometer

\includegraphics*[width=2.66in, height=1.97in, keepaspectratio=false]{image1}

\noindent Figure  2-1. Diagram of light path in diode array spectrophotometer.

One instrument you may use to measure absorbance is a Hewlett Packard (HP) model 8452A diode array spectrophotometer. The diode array spectrophotometer uses a broad-spectrum source of incident light from a deuterium lamp. The light passes through the sample, 1 cm path length, and is split by a grating into a spectrum of light that is measured by an array of diodes. Each diode measures a bandwidth of 2 nm with 316 diodes covering the range from 190 nm to 820 nm. The wavelengths of light and their colors are given in Table 2-1. The light path for the diode array spectrophotometer is shown in :numref:`figure_Spectrophotometer`.

The HP 8452A spectrophotometer has a photometric range of 0.002 - 3.3 absorbance units. In practice absorbance measurements greater than 2.5 are not very meaningful as they indicate that 99.7\% of the incident light at that wavelength was absorbed. Conversely, an absorbance of 0.002 means that 0.5\% of the incident light at that wavelength was absorbed.

When measuring samples of known concentration the Spectrophotometer software (see Appendix A - Diode Array UV Visible Spectrophotometer) calculates the relationship between absorbance and concentration at a selected wavelength. The slope (m), intercept (b), and correlation coefficient (r) are calculated using equations 2.4 through 2.6.

The slope of the best fit line is
\[m=\frac{\sum xy -{\textstyle\frac{\sum x \sum y }{n}} }{\sum x^{2}  -\frac{\left(\sum x \right)^{2} }{n} }  2.4\]
The intercept of the line is
\[{\rm b\; }={\rm \; }\bar{y}-{\rm m}\bar{x} 2.5\]
The correlation coefficient is defined as
\[r=\frac{\sum xy -{\textstyle\frac{\sum x \sum y }{n}} }{\sqrt{\left(\sum x^{2}  -\frac{\left(\sum x \right)^{2} }{n} \right)\left(\sum y^{2}  -\frac{\left(\sum y \right)^{2} }{n} \right)} }  2.6\]
where x is the concentration of the solute (methylene blue in this exercise), y is the absorbance, and n is the number of samples.

\noindent
\subsection{Experimental Objectives}

To gain proficiency in:

\noindent \begin{enumerate}
\item 1) )Calibrating and using electronic balances

\noindent \item 2) )Using signal conditioning boxes and data acquisition software

\noindent \item 3) )Digital pipetting

\noindent \item 4) )Preparing a solution of known concentration

\noindent \item 5) )Preparing dilutions

\noindent \item 6) )Measuring concentrations using a UV-Vis spectrophotometer
\end{enumerate}

\noindent
\subsection{Experimental Methods}

\noindent
\paragraph{Mass Measurements}

Mass can be accurately measured with an electronic analytical balance. Perhaps because balances are so easy to use it is easy to forget that they should be calibrated on a regular basis. It is recommended that balances be calibrated once a week, after the balance has been moved, or if excessive temperature variations have occurred. In order for balances to operate correctly they also need to be level. Most balances come with a bubble level and adjustable feet. Before calibrating a balance verify that the balance is level.

The environmental laboratory is equipped with balances manufactured by Ohaus.  As part of this exercise, we will calibrate the Ohaus Scout Pro balance (200 g) as follows:

\noindent \begin{enumerate}
\item 1) )Start with the balance off.

\noindent \item 2) )Press and hold the ON/ZERO key until the screen reads 'MENU'.

\noindent \item 3) )Releasing the ON/ZERO key will take you to calibration mode indicated by '.C.A.L.' on the screen.

\noindent \item 4) )Press the ON/ZERO key to indicate 'Yes' to calibration.

\noindent \item 5) )The balance will acquire the zero value (and read -- C -).

\noindent \item 6) )Once the zero value is obtained, the balance screen will blink -- 200 g -- indicating that the 200 g mass will be used for the calibration.

\noindent \item 7) )Place the 200 g calibration mass on the pan (handle the calibration mass using a cotton glove or tissue paper) and press ON/ZERO key.

\noindent \item 8) )The balance will calibrate to the mass added. Remove the mass when the screen reads '200.00 g' indicating the calibration is complete.

\noindent \item 9) )Measure the mass of a second calibration mass of different size (e.g., 100 g) to confirm calibration.

\noindent \item 10) )Record relevant data in the attached spreadsheet.
\end{enumerate}

Dry chemicals can be weighed in disposable plastic "weighing boats" or other suitable containers. It is often desirable to subtract the weight of the container in which the chemical is being weighed. The weight of the chemical can be obtained either by weighing the container first and then subtracting, or by "zeroing" the balance with the container on the balance.

\noindent
\paragraph{Temperature Measurement and ProCoDA}

We will use a data acquisition system designed and fabricated in CEE at Cornell University. Each group has their own ProCoDA box and associated power supply and USB cable. The power supply and USB cable must be plugged into the ProCoDA box and then into the AC power on your lab bench and a USB port on your lab bench computer, respectively.

Use a thermistor to measure the temperature of distilled water. The thermistors are usually hanging on the rack to the right of the fume hoods (you should have one on your bench today). The thermistor has a 4-mm diameter metallic probe. Plug the thermistor into the red signal-conditioning box. The conditioned signal is connected to the ProCoDA box using a red cable. Connect the red cable to one of the sensor ports on the top row of the ProCoDA box.

\noindent \begin{enumerate}
\item 1) )Monitor the thermistor using the ProCoDA II software.  The software can be found in the desktop folder named 'ProCoDA II'.

\noindent \item 2) )Open ProCoDA II

\noindent \item 3) )Navigate to the Configuration tab

\noindent \item 4) )Click the 'volt' button to select and configure your sensor (thermistor).

\noindent \item 5) )Click 'insert sensor' to add a sensor to your list.  As the semester goes on, we will run experiments that require several sensors to be added here.  For now, we will use the single thermistor.

\noindent \item 6) )Now you need to tell the software where your sensor is plugged in.  In the 'channels' pull-down menu, select the address of your sensor.  All addresses begin with a Dev/ai prefix.

\noindent \item 7) Finally, you need to tell the software to convert the signal into temperature units.  This is done with a calibration file.  Click 'open calibration file' (it looks like a regular open folder icon) and select the calibration file named thermistor.smc.

\noindent \item 8) )You should now be reading temperature in units of degrees Celsius. Verify that you are monitoring the correct temperature probe by holding the temperature probe in your hand and warming it up.  Does the temperature reading respond?

\noindent \item 9) )Place the probe in a 100-mL plastic beaker full of distilled water. Wait at least 15 seconds to allow the probe to equilibrate with the solution.

\noindent \item 10) )Record this temperature in the attached spreadsheet.
\end{enumerate}

\noindent
\paragraph{Pipette Technique}

\begin{enumerate}
\item \textbf{ }Use Figure 2-2 to estimate the mass of 990 �L of distilled water (at the measured temperature).

\item  Use a 100-1000 �L digital pipette to transfer 990 �L of distilled water to a tared weighing boat on either the \textit{AdventurerPro} or \textit{Galaxy} analytical balance. Record the mass of the water and compare with the expected value (Figure 2-2). Repeat this step if necessary until your pipetting error is less than 2\%, then measure the mass of 5 replicate 990 �L pipette samples. Calculate the mean ($\bar{x}$ defined in equation 2.7), standard deviation (s defined in equation 2.8), and coefficient of variation, s/$\bar{x}$, for your measurements. The coefficient of variation (c.v.) is a good measure of the precision of your technique. For this test a c.v. $\mathrm{<}$ 1\% should be achievable.
\[\bar{x}={\rm \; }\frac{\sum x }{n}  2.7\]
\[{\rm s\; }={\rm \; }\sqrt{\frac{\sum x^{2}  -\frac{(\sum x )^{2} }{n} }{n-1} }  2.8\]
\end{enumerate}
Note that these functions are available on most calculators and in Excel.

\noindent \includegraphics*[width=2.84in, height=2.11in, keepaspectratio=false]{image2}

\noindent Figure  2-2. Density of water vs. temperature.

See :numref:`figure_mountain` for a typical mountain view.

.. _figure_Density_vs_temperature:

.. figure:: Images/Density_vs_temperature.png
    :width: 300px
    :align: center
    :alt: Density of water vs. temperature

    Density of water vs. temperature.

\noindent
\paragraph{Measure Density}

\noindent \begin{enumerate}
\item 1) )Weigh a 100 mL volumetric flask with its cap (use either the \textit{Scout Pro 200 g} or the \textit{Galaxy} analytical balance).

\noindent \item 2) )Prepare 100 mL of a 1 M solution of sodium chloride in the weighed flask. You can also dissolve the NaCl in a clean beaker and transfer to the volumetric flask.  Make sure to mix the solution and then verify that you have \textbf{exactly 100 mL} of solution. Note that the combined \textbf{volume of NaCl and water decreases} as the salt dissolves.

\noindent \item 3) )Weigh the flask (with its cap) plus the sodium chloride solution and calculate the density of the 1 M NaCl solution.
\end{enumerate}

\noindent
\paragraph{Prepare methylene blue standards of several concentrations}

\noindent \begin{enumerate}
\item 1) )A methylene blue stock solution of 1 g/L has been prepared. Use it to prepare 100 mL of each of the following concentrations: 1 mg/L, 2 mg/L, 3 mg/L, 4 mg/L, and 5 mg/L.  Record your calculations in the attached spreadsheet.

\noindent \item 2) )Note any errors in transfer of mass as you prepare these dilutions (the color will make it easy to see).
\end{enumerate}

\noindent
\paragraph{Measure a standard curve and an unknown}

\noindent \begin{enumerate}
\item 1) )See Appendix A - Diode Array UV Visible Spectrophotometer for instructions on using the UV-Vis Spectrophotometer software.

\noindent \item 2) )Transfer approximately 2 mL of distilled water into a sample cuvette.  This will be your reference sample.

\noindent \item 3) )Transfer approximately 2 mL of each methylene blue standard into a sample cuvette.

\noindent \item 4) )Measure the absorbance of the samples using the ``Spectrophotometer'' software.  The software can be found in the desktop folder named ``Runtimes.''

\noindent \item 5) )Open ``Spectrophotometer.''

\noindent \item 6) )Make sure the spectrophotometer is running and the lamp is ``ON.''

\noindent \item 7) )Place the cuvette containing distilled water into the sample well.

\noindent \item 8) )Select ``\textbf{measure reference}'' from the computer control palette.  Change the reference setup to ``Sample Cuvet'' and hit OK.  Follow the instructions as you are prompted.  This will measure the absorbance of the distilled water and the sample cuvette.  When finished, hit OK.

\noindent \item 9) )Measure the absorbance of the methylene blue standards. Analyze the 5 methylene blue standards plus the distilled water sample (0 mg/L methylene blue) as standards. Select ``\textbf{measure standards''} from the computer control palette. Fill in Your Name (group \#), General Description, and change the Setup parameters to Sample Cuvet.  Add units as mg/L.  Move the slider to add 6 standards to be measured and fill in the information for the six samples (starting with RO water and ending with the highest concentration of methylene blue).  Select OK and follow instructions as you are prompted.

\noindent \item 10) )Save the data as: S:{\textbackslash}Courses{\textbackslash}4530{\textbackslash}Group \#{\textbackslash}Lab 1 -- Fundamentals{\textbackslash}group\#\_blue

\noindent \item 11) )Measure the absorbance of a methylene blue solution of unknown concentration. Select 'measure samples' from the control palette. Fill in Your Name (group \#), General Description, and change the Setup parameters to Sample Cuvet.  Fill in a Description of the unknown and hit OK.  Follow instructions as you are prompted.

\noindent \item 12) )Save the data as: S:{\textbackslash}Courses{\textbackslash}4530{\textbackslash}Group \#{\textbackslash}Lab 1 -- Fundamentals{\textbackslash}group\#\_blue

\noindent \item 13) )Record its absorbance at 660 nm and the calculated concentration in the attached spreadsheet. These values are given in the digital displays in the bottom left of the window. (Note that for the data analysis you will recalculate the concentration using the sample and standard absorbances.)

\noindent \item 14) )Select the export function to save your data in an Excel readable format.
\end{enumerate}

\noindent
\subsection{Pre-Laboratory Questions}

\noindent \begin{enumerate}
\item 1) )You need 100 mL of a 1 �M solution of zinc that you will use as a standard to calibrate an atomic adsorption spectrophotometer. Find a source of zinc ions combined either with chloride or nitrate (you can use the internet or any other source of information). What is the molecular formula of the compound that you found? Zinc disposal down the sanitary sewer is restricted at Cornell and the solutions you prepare may need to be disposed of as hazardous waste. As an environmental engineering student you strive to minimize waste production. How would you prepare this standard using techniques readily available in the environmental laboratory so that you minimize the production of solutions that you don't need? Note that we have pipettes that can dispense volumes between 10 ?L and 1 mL and that we have 100 mL and 1 L volumetric flasks. Include enough information so that you could prepare the standard without doing any additional calculations. Consider your ability to accurately weigh small masses. Explain your procedure for any dilutions. Note that the stock solution concentration should be an easy multiple of your desired solution concentration so you don't have to attempt to pipette a volume that the digital pipettes can't be set for such as 13.6 ?L.

\noindent \item 2) )The density of sodium chloride solutions as a function of concentration is approximately 0.6985C + 998.29 (kg/m${}^{3}$) (C is kg of salt/m${}^{3}$). What is the density of a 1 M solution of sodium chloride?
\end{enumerate}

\noindent
\subsection{Data Analysis and Questions}

Submit one spreadsheet containing the data sheet, exported absorbance data, graphs and answers to the questions.



\noindent \begin{enumerate}
\item 1) )Fill out the Excel data sheet available from the course syllabus. Make sure that all calculated values are entered in the spreadsheet as equations. Failure to use the spreadsheet to do the calculations will not receive full credit. Note that this is likely the only assignment that we will do using Excel. All remaining analysis for the course will be done in Atom!

\noindent \item 2) )Create a graph of absorbance at 660 nm vs. concentration of methylene blue in Atom using the exported data file. Does absorbance at 660 nm increase linearly with concentration of methylene blue?

\noindent \item 3) )Plot ? as a function of wavelength for each of the standards on a single graph. Note that the path length is 1 cm. Make sure you include units and axis labels on your graph. If Beer's law is obeyed what should the graph look like?

\noindent \item 4) )Did you use interpolation or extrapolation to get the concentration of the unknown?

\noindent \item 5) )What colors of light are most strongly absorbed by methylene blue?

\noindent \item 6) )What measurement controls the accuracy of the density measurement for the NaCl solution? What density did you expect (see prelab 2)? Approximately what should the accuracy be?

\noindent \item 7) )Don't forget to write a brief paragraph on conclusions and on suggestions using Markdown.

\noindent \item 8) )Verify that your report and graphs meet the requirements as outlined in the course materials.
\end{enumerate}

\noindent
\paragraph{Data Sheet}

\noindent 523486575\includegraphics*[width=4.50in, height=8.59in, keepaspectratio=false]{image3}523486575MWMonroe Weber-Shirk523486575660824645Change MB stock to 1 g/L.

\noindent
\subsection{Lab Prep Notes}

\noindent Table 2-2. Reagent list.

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



\noindent
\paragraph{Setup}

\noindent \begin{enumerate}
\item 1) )Prepare stock methylene blue solution and distribute to student workstations in 20 mL vials.

\noindent \item 2) )Prepare 100 mL of unknown in concentration range of standards. Divide into two bottles (one for each spectrophotometer).

\noindent \item 3) )Verify that spectrophotometers are working (prepare a calibration curve as a test).

\noindent \item 4) )Verify that balances calibrate easily.

\noindent \item 5) )Disassemble, clean, and lubricate all pipettes.
\end{enumerate}
