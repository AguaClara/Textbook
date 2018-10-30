************
Gas Transfer
************



================
Gas Transfer}


------------------
Introduction}

Exchange of gases between aqueous and gaseous phases is an essential element of many environmental processes. Wastewater treatment plants require enhanced transfer of oxygen into activated sludge tanks to maintain aerobic degradation. Water treatment plants require gas transfer to dissolve chlorine gas or ozone. Gas transfer can also be used to remove unwanted volatile chemicals such as carbon tetrachloride, tetrachloroethylene, trichloroethylene, chloroform, bromodichloromethane, and bromoform from water (Zander et al., 1989). Exchange of a dissolved compound with the atmosphere is controlled by the extent of mixing in the aqueous and gaseous phase, the surface area of the interface, the concentration of the compound in the two phases, and the equilibrium distribution of the compound. Technologies that have been developed to enhance gas transfer include: aeration diffusers, packed-tower air stripping, and membrane stripping. Each of these technologies creates a high interface surface area to enhance gas transfer.


------------------
Theory}

Oxygen transfer is important in many environmental systems. Oxygen transfer is controlled by the partial pressure of oxygen in the atmosphere (0.21 atm) and the corresponding equilibrium concentration in water (approximately 10 mg/L). According to Henry's Law, the equilibrium concentration of oxygen in water is proportional to the partial pressure of oxygen in the atmosphere.

Natural bodies of water may be either supersaturated or undersaturated with oxygen depending on the relative magnitude of the sources and sinks of oxygen. Algae can be a significant source of oxygen during active photosynthesis and can produce supersaturation. Algae also deplete oxygen levels during the night.

 \includegraphics*[width=2.92in, height=2.25in, keepaspectratio=false]{image1}

 Figure  1-1. Dissolved oxygen concentrations in equilibrium with the atmosphere.

At high levels of supersaturation dissolved gas will form microbubbles that eventually coalesce, rise, and burst at the water surface. The bubbles provide a very efficient transfer of supersaturated dissolved gas to the gaseous phase, a process that can be observed when the partial pressure of carbon dioxide is decreased by opening a carbonated beverage. Bubble formation by supersaturated gasses also occurs in the environment when cold water in equilibrium with the atmosphere is warmed rapidly. The equilibrium dissolved oxygen concentration decreases as the water is warmed (Figure 1-1).

Supersaturation of dissolved gases can also occur when water carrying gas bubbles from a waterfall or spillway plunges into a deep pool. The pressure increases with depth in the pool and gasses carried deep into the pool dissolve in the water. When the water eventually approaches the surface the pressure decreases and the dissolved gases come out of solution and form bubbles. Bubble formation by supersaturated gases can kill fish (similar to the ``bends'' in humans) as the bubbles form in the bloodstream.


^^^^^^^^^^^^^^^^^^^^^
Gas Transfer Coefficient}

The gas transfer rate can be modeled as the product of a driving force (the difference between the equilibrium concentration and the actual concentration) and an overall volumetric gas transfer coefficient (a function of the geometry, mixing levels of the system and the solubility of the compound). In equation form
.. math::


\frac{dC}{dt} =\hat{k}_{v,l} \left(C^{*} -C\right) 1.1

where C is the dissolved gas concentration, C* is the equilibrium dissolved gas concentration, and $\hat{k}_{v,l} $ is the overall volumetric gas transfer coefficient . Although $\hat{k}_{v,l} $ has dimensions of 1/T, it is a function of the interface surface area (A), the liquid volume (V), the oxygen diffusion coefficient in water (D), and the thickness of the laminar boundary layer (?) through which the gas must diffuse before the much faster turbulent mixing process can disperse the dissolved gas throughout the reactor.
.. math::


\hat{k}_{v,l} =f(D,\delta ,A,V) 1.2

\includegraphics*[width=2.98in, height=1.57in, keepaspectratio=false]{image2}

 Figure  1-2. Single film model of interphase mass transfer of oxygen.

 The overall volumetric gas transfer coefficient is system specific and thus must be evaluated separately for each system of interest (Weber and Digiano, 1996).

A schematic of the gas transfer process is shown in Figure 1-2. Fickian diffusion controls the gas transfer in the laminar boundary layer. The oxygen concentration in the bulk of the fluid is assumed to be homogeneous due to mixing and the oxygen concentration above the liquid is assumed to be that of the atmosphere.

The gas transfer coefficient will increase with the interface area and the diffusion coefficient and will decrease with the reactor volume and the thickness of the boundary layer. The \textit{functional} form of the relationship is given by

.. math::

    \hat{k}_{v,l} =\frac{AD}{V\delta }  1.3



Equation 1.1 can be integrated with appropriate initial conditions to obtain the concentration of oxygen as a function of time. However, care must be taken to ensure that the overall volumetric gas transfer coefficient is not a function of the dissolved oxygen concentration. This dependency can occur where air is pumped through diffusers on the bottom of activated sludge tanks. Rising air bubbles are significantly depleted of oxygen as they rise through the activated sludge tank and the extent of oxygen depletion is a function of the concentration of oxygen in the activated sludge. Integrating equation 1.1 with initial conditions of C = C0 at t = t0
\[\int _{C_{0} }^{C}\frac{dC}{C^{*} -C}  =\int _{t_{0} }^{t}\hat{k}_{v,l} dt  1.4

\[\ln \frac{C^{*} -C}{C^{*} -C_{0} } =-\hat{k}_{v,l} (t-t_{0} ) 1.5

Equation 1.5 can be evaluated using linear regression so that $\hat{k}_{v,l} $ is the slope of the line.

The simple gas transfer model given in equation 1.5 is appropriate when the gas transfer coefficient is independent of the dissolved gas concentration. This requirement can be met in systems where the gas bubbles do not change concentration significantly as they rise through the water column. This condition is met when the water column is shallow, the bubbles have large diameters, or the difference between the concentration of dissolved gas and the equilibrium concentration is small.


\paragraph{Oxygen Transfer Efficiency}

An important parameter in the design of aeration systems for the activated sludge process is the energy cost of compressing air to be pumped though diffusers. The pumping costs are a function of the pressure and the airflow rate. The pressure is a function of the hydrostatic pressure (based on the depth of submergence of the diffusers) and the head loss in the pipes and through the diffuser. The required airflow rate is a function of the BOD of the wastewater and the efficiency with which oxygen is transferred from the gas phase to the liquid phase. This oxygen transfer efficiency (OTE) is a function of the type of diffuser, the diffuser depth of submergence, as well as temperature and ionic strength of the activated sludge. Oxygen transfer is a remarkably inefficient process; only a small fraction of the oxygen carried by the rising bubbles diffuses into the activated sludge. The most efficient systems use membrane diffusers and achieve an OTE of approximately 10\%.

The manufacturer typically provides oxygen transfer efficiency for a specific diffuser. In this laboratory we will measure oxygen transfer efficiency for the aeration stone that we will be using in an activated sludge tank. The molar transfer rate of oxygen through the diffuser is
\[\dot{n}_{gas\; o_{2} } =\frac{Q_{air} P_{air} f_{O_{2} } }{RT}  1.6\]
where $f_{O_{2} } $is the molar fraction of air that is oxygen \eqref{GrindEQ__0_21_}, $Q_{air} $ is the volumetric flow rate of air into the diffuser, $P_{air} $is the air pressure immediately upstream from the diffuser, $R$ is the universal gas constant and $T$is absolute temperature. If the airflow rate is already given with units of moles/s then the molar transfer rate of oxygen can be obtained by multiplying by the molar fraction of air that is oxygen.

The molar rate of dissolution into the aqueous phase is
\[\dot{n}_{aq\; o_{2} } =\frac{V}{MW_{O_{2} } } \frac{dC}{dt}  1.7\]
where $MW_{O_{2} } $ is the molecular weight of oxygen, $V$is the reactor volume, and $\frac{dC}{dt} $is the change in aqueous oxygen concentration with time. The rate of change of oxygen concentration is a function of the dissolved oxygen concentration and is a maximum when the dissolved oxygen concentration is zero. Oxygen transfer efficiency could be measured for any dissolved oxygen concentration. A better method of analysis is to substitute the right side of equation 1.1 for $\frac{dC}{dt} $.

.. math::

    \dot{n}_{aq\; o_{2} } =\frac{V\hat{k}_{v,l} \left(C^{*} -C\right)}{MW_{O_{2} } }  1.8\]

The oxygen transfer efficiency is the ratio of equation 1.8 to equation 1.6.
\[OTE=\frac{\hat{k}_{v,l} \left(C^{*} -C\right)VRT}{MW_{O_{2} } Q_{air} P_{air} f_{O_{2} } }  1.9\]

Measurement of OTE using equation 1.9 requires that the gas transfer coefficient, air flow rate, air pressure, and the air temperature be measured. (P${}_{air}$ and Q${}_{air}$ have to correlate and in this experiment the best combination is atmospheric pressure and the flow rate given by the pump.)

If the molar airflow rate is controlled then OTE is based on the ratio of equation 1.8 to the molar transfer rate of supplied oxygen.
\[OTE=\frac{\dot{n}_{aq\; o_{2} } }{f_{O_{2} } \dot{n}_{air} } =\frac{V\hat{k}_{v,l} \left(C^{*} -C\right)}{f_{O_{2} } \dot{n}_{air} MW_{O_{2} } }  1.10\]

\paragraph{Deoxygenation}

To measure the reaeration rate it is necessary to first remove the oxygen from the reactor. This can be accomplished by bubbling the solution with a gas that contains no oxygen. Nitrogen gas is typically used to remove oxygen from laboratory reactors. Alternately, a reductant can be used. Sulfite is a strong reductant that will reduce dissolved oxygen in the presence of a catalyst.
\[{\rm O}_{{\rm 2}} +{\rm 2SO}_{{\rm 3}}^{-{\rm 2}} \stackrel{{\rm cobalt}}{\longrightarrow}{\rm 2SO}_{{\rm 4}}^{-{\rm 2}}  1.11\]
The mass of sodium sulfite required to deoxygenate 1 mg of oxygen is calculated from the stoichiometry of equation 1.11.
\[\frac{{\rm mole\; O}_{{\rm 2}} }{{\rm 32000\; mg\; O}_{{\rm 2}} } \cdot \frac{{\rm 2\; mole\; Na}_{{\rm 2}} {\rm SO}_{{\rm 3}} }{{\rm mole\; O}_{{\rm 2}} } \cdot \frac{{\rm 126,000\; mg\; Na}_{{\rm 2}} {\rm SO}_{{\rm 3}} }{{\rm mole\; Na}_{{\rm 2}} {\rm SO}_{{\rm 3}} } =\frac{{\rm \; 7.875\; mg\; Na}_{{\rm 2}} {\rm SO}_{{\rm 3}} }{{\rm mg\; O}_{{\rm 2}} }  1.12\]



 If complete deoxygenation is desired a 10\% excess of sulfite can be added. The sulfite will continue to react with oxygen as oxygen is transferred into the solution. The oxygen concentration can be measured with a dissolved oxygen probe or can be estimated if the temperature is known and equilibrium with the atmosphere assumed (Figure 1-1).




------------------
Experimental Objectives}

The objectives of this lab are to:

 \begin{enumerate}
\item 1) )Illustrate the dependence of gas transfer on gas flow rate.

 \item 2) )Develop a functional relationship between gas flow rate and gas transfer.

 \item 3) )Measure the oxygen transfer efficiency of a course bubble diffuser.

 \item 4) )Explain the theory and use of dissolved oxygen probes.
\end{enumerate}

A small reactor that meets the conditions of a constant gas transfer coefficient will be used to characterize the dependence of the gas transfer coefficient on the gas flow rate through a simple diffuser. The gas transfer coefficient is a function of the gas flow rate because the interface surface area (\textit{i.e.}, the surface area of the air bubbles) increases as the gas flow rate increases.


------------------
Dissolved Oxygen Probes}


\paragraph{Theory}

The dissolved oxygen probes make use of the fact that an applied potential of 0.8 V can reduce O${}_{2}$ to H${}_{2}$O:

\begin{tabular}{|p{0.8in}|p{2.7in}|p{0.6in}|} \hline
 & 4 e${}^{-}$ + 4 H${}^{+}$ + O${}_{2}$ $\mathrm{\to}$ 2 H${}_{2}$O &  \\ \hline
\end{tabular}

The cell is separated from solution by a gas permeable membrane that allows O${}_{2}$ to pass through. The concentration of O${}_{2}$ in the cell is kept very low by reduction to H${}_{2}$O. The rate at which oxygen diffuses through the gas permeable membrane is proportional to the difference in oxygen concentration across the membrane. The concentration of oxygen in the cell is $\mathrm{\approx}$0 and thus the rate at which oxygen diffuses through the membrane is proportional to the oxygen concentration in the solution.

Oxygen is reduced to water at a silver (Ag) cathode of the probe. Oxygen reduction produces a current that is measured by the meter.


\paragraph{Calibration}

A calibration routine is available in the ProCoDA II software. Follow the instructions in the software and use the help as needed. The calibration steps include the following:

When using the DO probe make sure that there \textbf{aren't any air bubbles} on the probe membrane. If you are aerating, the sample place the probe as far from the air bubbles as possible. Air bubbles on the membrane will cause inaccurate readings. \textbf{\textit{Note that you do not need to calibrate the DO probe at the beginning of the lab. Build the full setup and then calibrate when it says to calibrate.}}

\begin{enumerate}
\item  Connect a DO probe to the data acquisition system using the gold signal conditioning box.

\item  Navigate to the Configuration tab and enter you Location in the bottom left corner, then select \includegraphics*[width=0.34in, height=0.34in, keepaspectratio=false]{image3} to configure the dissolved oxygen channel(s). Select the DO probe from the sensor list and point the channel to the correct sensor port.

\item  Use the dissolved oxygen calibration VI \includegraphics*[width=0.34in, height=0.34in, keepaspectratio=false]{image4} to calibrate the DO probe.

\item  Enter the temperature of the sample. This can be measured by using a thermistor or a thermometer. A good estimate is 22�C.

\item  If you have typed in your location in the Configuration Tab, you can get the actual barometric pressure for Ithaca, New York by selecting \includegraphics*[width=1.89in, height=0.21in, keepaspectratio=false]{image5}

\item  Place the probe in oxygen saturated water (use the air jet on your bench to bubble air into water in a 4L container).  The voltage from the DO probe should be between 0.17 and 0.23 volts if the probe is working correctly. If the voltage is lower than 0.17 it may be time to replace the membrane or the solution may not be saturated with oxygen.

\item  Select \includegraphics*[width=1.12in, height=0.21in, keepaspectratio=false]{image6}to calibrate the DO sensor.

\item  Select OK \includegraphics*[width=0.91in, height=0.25in, keepaspectratio=false]{image7}when you are satisfied with the calibration.

\item  If desired you may save the calibration for later use \includegraphics*[width=0.25in, height=0.24in, keepaspectratio=false]{image8}. However, it is not necessary to save the calibration to use the calibration in the current session.~~If you want to save the calibration, save it in your Group folder on the S:/ drive.~~
\end{enumerate}


------------------
Experimental Methods}

 \includegraphics*[width=4.33in, height=1.91in, keepaspectratio=false]{image9} The reactors are 4 L containers (Figure 1-3). The DO probe should be placed in a location so as to minimize the risk of air bubbles lodging on the membrane on the bottom of the probe. The aeration stone is connected to a source of regulated air flow. A 7-kPa pressure sensor (optional) can be used to measure the air pressure immediately upstream from the diffuser stone. A 200-kPa pressure sensor is used to measure the air pressure in the accumulator.


\paragraph{Initial Setup}

 \begin{enumerate}
\item 1) )Assemble the apparatus (don't forget the 1.5 mm x 5 cm restriction).

 \item 2) )Install the head loss orifice as close to the valve as possible (plug it directly into the valve!).

 \item 3) )The ProCoDA II software will be used to control the air flow rate for the aeration experiment. The software will use external code to calculate the calibration constant for the flow restriction, to control valve 1 (the air supply valve), and to regulate the flow of air into the accumulator. The calibration uses the ideal gas law to determine the flow rate as a function of the difference in pressure between the source and the accumulator. Once this calibration is obtained a separate code will set the fraction of time that valve 1 needs to be open to obtain the desired flow rate of air.
\end{enumerate}

 The software combines 3 elements: sensors (inputs from the real world), set points (inputs from the plant operator and calculated values based on sensors and other set points), and logic (rules that govern how the plant should operate given the sensor data and set points). The software contains a graphical user interface where you can edit, save, and open files containing sensor information and files containing the set point and logic information.

 A method file containing the configuration necessary to control airflow is available at S:{\textbackslash}Courses{\textbackslash}4530{\textbackslash} GasTransfer2.pcm. Open the file, using the \includegraphics*[width=0.25in, height=0.24in, keepaspectratio=false]{image10} on the Configuration tab. You will need to adjust the channels for the accumulator pressure and the DO probe to match where you plugged them in your ProCoDA box. You will also need to make sure that your valves are connected to the correct ports on the ProCoDA box.

 \begin{enumerate}
\item 4) )Navigate to the Process Operation tab.

 \item 5) )Set the \textbf{\textit{operator selected state}} to ``toggle.''  The solenoid valves should click rhythmically if they are working properly.

 \item 6) )Install a membrane on the oxygen probe.

 \item 7) )Add 4 L of tap water to the reactor.

 \item 8) )Set the \textbf{\textit{mode of operation}} to automatic operation and the \textbf{\textit{operator selected state}} to ``prepare to calibrate.'' The software should quickly cycle through the calibration step and then begin attempting to control the air flow rate to the target value.  Note:  the purpose of the ``prepare to calibrate'' state is to void the accumulator of any pressure.  The state will not change to ``calibrate'' until the pressure drops below a predefined threshold.  To speed this up, you may disconnect the tubing at the top of your needle valve.  Once the solenoid clicks signaling the state change to ``calibrate,'' you must quickly reconnect the tube.

 \item 9) Set the stirrer speed to achieve a vortex on the surface of the water.

 \item 10) Calibrate the DO probe if you haven't already. Use 22�C as the temperature.
\end{enumerate}


\paragraph{Test the air flow controller}

In the following test, the air flow controller should provide a constant flow of air into the accumulator. You can assess how well the air flow controller is working based on the slope of the pressure as a function of time.

 \begin{enumerate}
\item 1) )Set the \textbf{\textit{mode of operation}} to ``Manual Locked in State.''

 \item 2) )Set the \textbf{\textit{operator selected state}} to off

 \item 3) )Open the accumulator cap to empty the accumulator.

 \item 4) )Close the accumulator cap.

 \item 5) )Close the needle valve.

 \item 6) )We can set the air flow rate based on our calibration be navigating to the Configuration tab and selecting edit rules. We want to control the air flow rate, so select air flow rate from the set points and variables list. Set the air flow rate to a value of 200u (200 ?M/s).

 \item 7) )Begin logging data from the 200kPa pressure sensor (accumulator pressure) at a 1 s interval using the datalog button on the configuration tab. Data is being logged when the icon is green.

 \item 8) )Navigate back to process operation tab and set the \textbf{\textit{operator selected state}} to aerate.

 \item 9) )End logging data when the accumulator pressure is approximately equal to the source pressure.

 \item 10) )Analyze the data to see if the airflow rate is close to the expected value. This can be done using the data obtained and the ideal gas law.  Plot the accumulator air pressure as a function of time.  The slope of the best fit linear line is in units of Pa/s.  The volume of the accumulator is 1 liter.  Solving the ideal gas law for n gives a result in units of moles/s. You set the air flow rate for 200 ?M/s and that is what you are expecting from this calculation.

 \item 11) )If the error is greater than 20\% look for leaks and recalibrate the airflow controller.
\end{enumerate}


\paragraph{Measure the Gas Transfer}

\begin{enumerate}
\item \textbf{ }Call the instructor and/or TA to check the system configuration.

\item  The instructor or TA will add 1 mg CoCl2� 6H2O (note this only needs to be added once because it is the catalyst). A stock solution of CoCl2� 6H2O (100 mg/mL -- thus add 10 ?L) has been prepared to facilitate measurement of small cobalt doses. (Use gloves when handling cobalt!)

\item  Prepare to record the dissolved oxygen concentration using ProCoDA software. Use 5-second data intervals and log the data to S:{\textbackslash}Courses{\textbackslash}4530{\textbackslash}Group \#{\textbackslash}gastran\_flowrate{\textbackslash} for later analysis. Include the actual flow rate in the file name.

\item  Set the airflow rate to the desired flow rate.  Each group will investigate six flowrates.  The instructor will assign the flowrates on the day of the lab exercise.

\item  Set the \textbf{\textit{operator selected state}} to aerate.

\item  Set the needle valve so the pressure in the accumulator is approximately 75\% of the source pressure.

\item  Wait until the accumulator pressure reaches steady state.

\item  Turn the air off by changing the operator selected state to ``OFF.''

\item  Add enough sodium sulfite to deoxygenate the solution. A stock solution of sodium sulfite (100 mg/mL) has been prepared to facilitate measurement of small sulfite doses. Calculate this dose based on the measured dissolved oxygen concentration. (4 L of water at C${}_{oxygen}$ mg O${}_{2}$/L = 4 C${}_{oxygen}$ mg O${}_{2}$, therefore add 4\eqref{GrindEQ__7_875_}(C${}_{oxygen}$) mg sodium sulfite or 4\eqref{GrindEQ__7_875_}(C${}_{oxygen}$)/100 mL of stock solution.)

\item  Turn the air on by changing the \textbf{\textit{operator selected state}} to ``Aerate.''

\item  Monitor the dissolved oxygen concentration until it reaches 50\% of saturation value or 10 minutes (whichever is shorter).

\item  Repeat steps 3-11 to collect data from at least two additional flow rates.

\item  Consolidate the files into one spreadsheet file with a separate sheet for each flow rate.

\item  Collect data from the whole class to analyze the full spectrum of flow rates investigated.
\end{enumerate}




------------------
Pre-Laboratory Questions}

 \begin{enumerate}
\item 1) )Calculate the mass of sodium sulfite needed to reduce all the dissolved oxygen in 4 L of pure water in equilibrium with the atmosphere and at 30$\mathrm{{}^\circ}$C.

 \item 2) )Describe your expectations for dissolved oxygen concentration as a function of time during a reaeration experiment.  Assume you have added enough sodium sulfite to consume all of the oxygen at the start of the experiment. What would the shape of the curve look like?

 \item 3) )Why is $\hat{k}_{v,l} $ not zero when the gas flow rate is zero? How can oxygen transfer into the reactor even when no air is pumped into the diffuser?

 \item 4) )Describe your expectations for $\hat{k}_{v,l} $ as a function of gas flow rate. Do you expect a straight line? Why?

 \item 5) )A dissolved oxygen probe was placed in a small vial in such a way that the vial was sealed. The water in the vial was sterile. Over a period of several hours the dissolved oxygen concentration gradually decreased to zero. Why? (You need to know how dissolved oxygen probes work to answer this!)
\end{enumerate}


------------------
Data Analysis}

This lab requires a significant amount of repetitive data analysis. Plan how you will organize the analysis to be as easy as possible.

\begin{enumerate}
\item  Calculate the air flow rate from testing the air flow controller and compare with the target value.

\item  Eliminate the data from each data set when the dissolved oxygen concentration was less than 0.5 mg/L. This will ensure that all of the sulfite has reacted.

\item  Plot a representative data set showing dissolved oxygen vs. time.

\item  Calculate $C^{*} $ based on the average water temperature, barometric pressure, and the following equation. $C^{*} =P_{O_{2} } {\mathop{e}\nolimits^{\left(\frac{1727}{T} -2.105\right)}} $ where T is in Kelvin, $P_{O_{2} } $ is the partial pressure of oxygen in atmospheres, and $C^{*} $is in mg/L. This equation is valid for 278 K$\mathrm{<}$T$\mathrm{<}$318 K.

\item  Estimate $\hat{k}_{v,l} $ using linear regression and equation 1.5 for each data set.

\item  Create a graph with a representative plot showing the linearized data, $\left(\ln \frac{C^{*} -C}{C^{*} -C_{0} } \right)$vs. time, and the best-fit line.

\item  Plot the reaeration model on the same graph as the dissolved oxygen vs. time data.  This is done by solving equation for C.

\item  Plot $\hat{k}_{v,l} $ as a function of airflow rate (?mole/s).

\item  Look at each dataset and if necessary (to make more linear plots) eliminate more data from the beginning (or end) of the dataset. You will be able to see when the oxygen level is affected by residual sulfite at the beginning of the experiments.

\item  Plot OTE as a function of airflow rate (?mole/s) with the oxygen deficit ($C^{*} -C$) set at 6 mg/L.

\item  Plot the molar rate of oxygen dissolution into the aqueous phase (?mole/s) as a function of airflow rate (?mole/s).

\item  Comment on results and compare with your expectations and with theory.

\item  Verify that your report and graphs meet the requirements.
\end{enumerate}


------------------
References}

 Weber, W. J. J. and F. A. Digiano. 1996. Process Dynamics in Environmental Systems. New York, John Wiley \& Sons, Inc.Zander, A. K.; M. J. Semmens and R. M. Narbaitz. 1989. ``Removing VOCs by membrane stripping'' American Water Works Association Journal 81\eqref{GrindEQ__11_}: 76-81.


------------------
\eject Lab Prep Notes}



\begin{tabular}{|p{0.7in}|p{0.7in}|p{0.7in}|} \hline
\multicolumn{3}{|p{1in}|}{Table 1-1. Reagent list\textbf{}} \\ \hline
\textbf{Description} & \textbf{Supplier} & \textbf{Catalog number} \\ \hline
Na2SO3 & Fisher Scientific & S430-500 \\ \hline
CoCl2� 6H2O & Fisher Scientific & C371-100 \\ \hline
\end{tabular}


\paragraph{Setup}

 \begin{enumerate}
\item 1) )Prepare the sodium sulfite immediately before class and distribute to groups in 15 mL PP bottles to minimize oxygen dissolution and reaction with the sulfite.
\end{enumerate}

\begin{tabular}{|p{0.4in}|p{0.3in}|p{0.3in}|p{0.3in}|p{0.3in}|p{0.4in}|} \hline
\multicolumn{6}{|p{1in}|}{Table 1-2. Stock solutions list} \\ \hline
\textbf{reagent} & M.W. & g/100 mL & mg/ mL & mL/\newline group & solubility g/L \\ \hline
Na2SO3 & 126.04 & 10 g & 100 & 10 & 125 \\ \hline
CoCl2� 6H2O & 237.92 & 10 g & 100 & 1 & 770 \\ \hline
\end{tabular}

\begin{enumerate}
\item 2) )The cobalt solution can be prepared anytime and stored long term. Distribute to student stations in 15 mL PP bottles.
\end{enumerate}

\begin{tabular}{|p{0.7in}|p{0.7in}|p{0.7in}|} \hline
\multicolumn{3}{|p{1in}|}{Table 1-3. Equipment list\textbf{}} \\ \hline
\textbf{Description} & \textbf{Supplier} & \textbf{Catalog number} \\ \hline
magnetic stirrer & Fisher Scientific & 11-500-7S \\ \hline
100-1095 �L pipette & Fisher Scientific & 13-707-5 \\ \hline
10-109.5 �L pipette & Fisher Scientific & 13-707-3 \\ \hline
15 mL PP bottles & Fisher Scientific & 02-923-8G \\ \hline
Solenoid valves &  &  \\ \hline
Stamp control boxes &  &  \\ \hline
Pressure sensors &  &  \\ \hline
1 L airflow accumulators &  &  \\ \hline
\end{tabular}

\begin{enumerate}
\item 3) )Verify that DO probes, membranes, and potassium chloride solutions are available at each station. Students will install the membranes.

 \item 4) )Provide clamps to mount DO probes on magnetic stirrers.
\end{enumerate}


\paragraph{Major elements of apparatus}

 \begin{enumerate}
\item ? �air flow hardware (built by students)

 \item ? �reactor hardware (built by students)

 \item ? �sensors (plugged in to ports by TA)

 \item ? �solenoid valves (already plugged in to ports by TA)

 \item ? �software
\end{enumerate}

\begin{tabular}{|p{0.3in}|p{0.9in}|} \hline
Group & Flows (?M/s) \\ \hline
1 & 200, 250, 300 \\ \hline
2 & 350, 400, 450 \\ \hline
3 & 500, 600, 700 \\ \hline
4 & 800, 900, 1000 \\ \hline
5 & 1200, 1500, 2000 \\ \hline
6 & 3000, 4000, 5000 \\ \hline
\end{tabular}


\paragraph{Class Plan}

 \begin{enumerate}
\item 1) )Show how to install membrane on DO probe.

 \item 2) )Show how to calibrate DO probe using Calibrator.
\end{enumerate}

\eject


------------------
Airflow Control}

 \includegraphics*[width=3.96in, height=1.71in, keepaspectratio=false]{image11} The ProCoDA software can be configured to control the flow of air into the reactor. The hardware required is shown in Figure 1.1. The control algorithm is based on the theoretical relationship between head loss and flow rate for the air flowing into the accumulator. We can empirically measure the head loss coefficient and then use the theoretical relationship to determine what fraction of time the influent valve should be open to obtain the desired flow rate. We can use the change in pressure in the accumulator when the influent valve is open to determine how fast air was flowing into the accumulator. In order to develop an appropriate head loss model we need to know if the flow into the accumulator is laminar or turbulent.
\begin{equation} \label{1.1}
{\rm Re}=\frac{\rho VD}{\mu }
\end{equation}
\begin{equation} \label{1.2}
{\rm Re}=\frac{4\rho Q}{\pi d\mu }
\end{equation}
If we hold pressure and temperature constant and then take the derivative of the ideal gas law we obtain.
\begin{equation} \label{1.3}
P\rlap{--}\dot{V}=\dot{n}RT
\end{equation}
and since change in volume with respect to time is a flow rate we have
\begin{equation} \label{ZEqnNum261903}
Q=\frac{\dot{n}RT}{P}
\end{equation}
Density of an ideal gas is given by
\begin{equation} \label{ZEqnNum758497}
\rho =\frac{PM_{gas} }{RT}
\end{equation}
Substituting these relationships into the equation for Reynolds number we obtain
\begin{equation} \label{1.6}
{\rm Re}=\frac{4\dot{n}M_{gas} }{\pi d\mu }
\end{equation}
For the air flow controller used in the lab the following values are obtained



 $\dot{n}$ max flow is about 10,000 ?M/s??$M_{gas} $ is 0.029 kg/M, and$\mu $ is 1.8x10${}^{-5}$ Ns/m${}^{2}$.
\begin{equation} \label{1.7}
{\rm Re}=\frac{4\left(10000\times 10^{-6} \frac{M}{s} \right)\left(0.029\frac{kg}{M} \right)}{\pi \left(1\times 10^{-3} m\right)\left(1.8\times 10^{-5} \frac{N\cdot s}{m^{2} } \right)} =20,500
\end{equation}
The flow into the air accumulator will almost certainly be turbulent and thus we can use the turbulent flow equations for minor losses to describe head loss. The equation for minor losses is:
\begin{equation} \label{ZEqnNum823776}
h_{minor} =K\frac{8Q^{2} }{g\pi ^{2} D^{4} }
\end{equation}
To use equation \eqref{ZEqnNum823776} for air we substitute pressure change for \textit{h${}_{minor}$}, equation \eqref{ZEqnNum261903} for flow rate, and equation \eqref{ZEqnNum758497} for density.
\begin{equation} \label{ZEqnNum122024}
\Delta p=K\frac{8M_{gas} RT\dot{n}^{2} }{\pi ^{2} D^{4} P}
\end{equation}
This change of pressure is occurring between the air supply and the accumulator. The pressure, P, in equation \eqref{ZEqnNum122024} helps determine the velocity of the air and thus head loss is a function of the pressure. The pressure varies between the pressure of the lab air supply, P${}_{s,}$ and the pressure in the air accumulator, placeStateP${}_{a.}$ As a reasonable first approximation we use the average pressure of the supply and the accumulator for P, the difference in pressure for ?p, and solve equation \eqref{ZEqnNum122024} for the molar flow rate.
\begin{equation} \label{ZEqnNum773701}
\dot{n}=\frac{\pi D^{2} }{4\sqrt{KM_{gas} RT} } \sqrt{\left(P_{s} -P_{a} \right)\left(P_{s} +P_{a} \right)}
\end{equation}
where $\dot{n}$ is the molar flow rate.

Multiplying terms and noting that the supply pressure is relatively constant, but that the accumulator pressure varies as it charges according to the ideal gas law we obtain.
\begin{equation} \label{1.11}
\frac{dn}{dt} =\frac{\pi D^{2} }{4\sqrt{KM_{gas} RT} } \sqrt{P_{s}^{2} -\frac{n^{2} R^{2} T^{2} }{V^{2} } }
\end{equation}
Separating terms and integrating from an initial condition with n${}_{1}$ moles to a final condition with n${}_{2}$ moles in the accumulator.
\begin{equation} \label{1.12}
\frac{\rlap{--}V}{RT} \int _{n_{1} }^{n_{2} }\frac{dn}{\sqrt{\frac{P_{s}^{2} V^{2} }{R^{2} T^{2} } -n^{2} } }  =\int _{0}^{t}\frac{\pi D^{2} }{4\sqrt{KM_{gas} RT} } dt
\end{equation}
After integrating we obtain the following equation.
\begin{equation} \label{1.13}
\frac{\rlap{--}V}{RT} \left(\sin ^{-1} \frac{n_{2} RT}{P_{s} V} -\sin ^{-1} \frac{n_{1} RT}{P_{s} V} \right)=\frac{\pi D^{2} t}{4\sqrt{KM_{gas} RT} }
\end{equation}
\begin{equation} \label{1.14}
t=\frac{4\sqrt{KM_{gas} RT} }{\pi D^{2} } \left(\sin ^{-1} \frac{n_{2} RT}{P_{s} V} -\sin ^{-1} \frac{n_{1} RT}{P_{s} V} \right)\frac{\rlap{--}V}{RT}
\end{equation}
Since we will be measuring the pressure in the accumulator we can now substitute that pressure for the terms containing moles of air to obtain an equation that is in a linear form such that a single term containing K and D can be obtained by linear regression.
\begin{equation} \label{1.15}
t=\frac{4\sqrt{KM_{gas} RT} }{\pi D^{2} } \left(\sin ^{-1} \frac{P_{a_{2} } }{P_{s} } -\sin ^{-1} \frac{P_{a_{1} } }{P_{s} } \right)\frac{\rlap{--}V}{RT}
\end{equation}

 \includegraphics*[width=2.97in, height=1.94in, keepaspectratio=false]{image12} Taking a data set obtained by filling the accumulator, finding the unknown term $\frac{4\sqrt{KM_{gas} RT} }{\pi D^{2} } $ by linear regression and then plotting the resulting model next to the data we obtain the graph in Figure \eqref{ZEqnNum363682}.

The final step is to calculate the fraction of time that the valve must be open in order to obtain a desired flow rate into the accumulator. Take the target air flow rate $\dot{n}_{t\arg et} $ and divide by the molar flow rate given by equation \eqref{ZEqnNum773701} to get the fraction of time the valve must be open to get the desired average flow rate.
\begin{equation} \label{ZEqnNum820776}
f_{valve} =\frac{\dot{n}_{t\arg et} }{\dot{n}} =\frac{\dot{n}_{t\arg et} }{\frac{\pi D^{2} }{4\sqrt{KM_{gas} RT} } \sqrt{P_{s}^{2} -P_{a}^{2} } }
\end{equation}

Equation \eqref{ZEqnNum820776} assumes that inertial effects during flow startup are not significant. Application of equation \eqref{ZEqnNum820776} results in slightly more air being delivered than requested. The reason for this error is that when the valve is closed the volume between the location of the head loss and the valve fills to the pressure of the source. This volume of air quickly discharges through the valve as soon as the valve is opened. This error can be minimized by using small valves and by keeping the head loss orifice as close to the valve as possible.

  Equation \eqref{ZEqnNum820776} is used by the air flow control.vi to calculate the fraction of time that the valve should be open. The ability of the control algorithm to create a desired flow rate can be measured by setting the flow rate and closing the effluent valves from the accumulator. The result is that the accumulator will gradually fill and as it fills $f_{valve} $ will gradually increase so the flow rate into the accumulator remains constant. The slope of the pressure vs. time line is proportional to the flow rate.




\end{document}
