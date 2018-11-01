***********************************************
Nutrient Removal with Sequencing Batch Reactors
***********************************************


Process Control
===============

An introduction to automated process control is available in pages 1681 to 1703 of (Metcalf \& Eddy, Tchobanoglous et al. 2003).


Sensors
-------

Sensors that are can be used to monitor the status of the sequencing batch reactor include pressure, temperature, dissolved oxygen, pH, and turbidity. The pressure sensors are quite versatile and can be used to measure airflow, water flow, volume of water in the reactor, as well as head loss through the course bubble diffuser.


Airflow Control
^^^^^^^^^^^^^^^

The Process Control software can be configured to control the flow of air into the sequencing batch reactor. The control algorithm is based on the theoretical relationship between head loss and flow rate for the air flowing into the accumulator. We can empirically measure the head loss coefficient and then use the theoretical relationship to determine what fraction of time the influent valve should be open to obtain the desired flow rate. We can use the change in pressure in the accumulator when the influent valve is open to determine how fast air was flowing into the accumulator. In order to develop an appropriate head loss model we need to know if the flow into the accumulator is laminar or turbulent.

.. math::

  {\rm Re}=\frac{\rho VD}{\mu }
\end{equation}
\begin{equation} \label{1.3}
{\rm Re}=\frac{4\rho Q}{\pi d\mu }
\end{equation}
If we hold pressure and temperature constant and then take the derivative of the ideal gas law we obtain.
\begin{equation} \label{1.4}
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
\begin{equation} \label{1.7}
{\rm Re}=\frac{4\dot{n}M_{gas} }{\pi d\mu }
\end{equation}
For the air flow controller used in the lab the following values are obtained



 $\dot{n}$ max flow is about 10,000 ?M/s??$M_{gas} $ is 0.029 kg/M, and$\mu $ is 1.8x10${}^{-5}$ Ns/m${}^{2}$.
\begin{equation} \label{1.8}
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
where

 Multiplying terms and noting that the supply pressure is relatively constant, but that the accumulator pressure varies as it charges according to the ideal gas law we obtain.
\begin{equation} \label{1.12}
\frac{dn}{dt} =\frac{\pi D^{2} }{4\sqrt{KM_{gas} RT} } \sqrt{P_{s}^{2} -\frac{n^{2} R^{2} T^{2} }{V^{2} } }
\end{equation}
Separating terms and integrating from an initial condition with n${}_{1}$ moles to a final condition with n${}_{2}$ moles in the accumulator.
\begin{equation} \label{1.13}
\frac{\rlap{--}V}{RT} \int _{n_{1} }^{n_{2} }\frac{dn}{\sqrt{\frac{P_{s}^{2} V^{2} }{R^{2} T^{2} } -n^{2} } }  =\int _{0}^{t}\frac{\pi D^{2} }{4\sqrt{KM_{gas} RT} } dt
\end{equation}
After integrating we obtain the following equation.
\begin{equation} \label{1.14}
\frac{\rlap{--}V}{RT} \left(\sin ^{-1} \frac{n_{2} RT}{P_{s} V} -\sin ^{-1} \frac{n_{1} RT}{P_{s} V} \right)=\frac{\pi D^{2} t}{4\sqrt{KM_{gas} RT} }
\end{equation}
\begin{equation} \label{1.15}
t=\frac{4\sqrt{KM_{gas} RT} }{\pi D^{2} } \left(\sin ^{-1} \frac{n_{2} RT}{P_{s} V} -\sin ^{-1} \frac{n_{1} RT}{P_{s} V} \right)\frac{\rlap{--}V}{RT}
\end{equation}
Since we will be measuring the pressure in the accumulator we can now substitute that pressure for the terms containing moles of air to obtain an equation that is in a linear form such that a single term containing K and D can be obtained by linear regression.
\begin{equation} \label{1.16}
t=\frac{4\sqrt{KM_{gas} RT} }{\pi D^{2} } \left(\sin ^{-1} \frac{P_{a_{2} } }{P_{s} } -\sin ^{-1} \frac{P_{a_{1} } }{P_{s} } \right)\frac{\rlap{--}V}{RT}
\end{equation}

 \includegraphics*[width=3.66in, height=2.40in, keepaspectratio=false]{image1} Taking a data set obtained by filling the accumulator, finding the unknown term $\frac{4\sqrt{KM_{gas} RT} }{\pi D^{2} } $ by linear regression and then plotting the resulting model next to the data we obtain the graph in Figure \eqref{ZEqnNum363682}.

The final step is to calculate the fraction of time that the valve must be open in order to obtain a desired flow rate into the accumulator. Take the target air flow rate $\dot{n}_{t\arg et} $ and divide by the molar flow rate given by equation \eqref{ZEqnNum773701} to get the fraction of time the valve must be open to get the desired average flow rate.
\begin{equation} \label{ZEqnNum820776}
f_{valve} =\frac{\dot{n}_{t\arg et} }{\dot{n}} =\frac{\dot{n}_{t\arg et} }{\frac{\pi D^{2} }{4\sqrt{KM_{gas} RT} } \sqrt{P_{s}^{2} -P_{a}^{2} } }
\end{equation}

Equation \eqref{ZEqnNum820776} assumes that inertial effects during flow startup are not significant. Application of equation  \eqref{ZEqnNum820776} results in slightly more air being delivered than requested. The reason for this error is that when the valve is closed the volume between the location of the head loss and the valve fills to the pressure of the source. This volume of air quickly discharges through the valve as soon as the valve is opened. This error can be minimized by using small valves and by keeping the head loss orifice as close to the valve as possible. It is also possible to correct for this error.
\begin{equation} \label{ZEqnNum251168}
f_{valve} =\frac{\dot{n}_{t\arg et} }{\dot{n}+\frac{n_{error} }{\Delta t_{\left(f_{valve} \right)} } } =\frac{\dot{n}_{t\arg et} }{\frac{\pi D^{2} }{4\sqrt{KM_{gas} RT} } \sqrt{P_{s}^{2} -P_{a}^{2} } +\frac{\left(P_{s} -P_{a} \right)\rlap{--}V_{valve} }{RT\Delta t_{\left(f_{valve} \right)} } }
\end{equation}

where $\Delta t_{\left(f_{valve} \right)} $ is the valve cycle time and $\rlap{--}V_{valve} $is the volume between the location of the head loss and the valve. The difficulty with equation \eqref{ZEqnNum251168} is that the valve cycle time is a function of $f_{valve} $. This difficulty can be overcome by using a shift register to store the previously calculated value of  $\Delta t_{\left(f_{valve} \right)} $. Since the algorithm is called many times per valve cycle the solution will easily converge.



 Equation \eqref{ZEqnNum251168} is used by the air flow control.vi calculate the fraction of time that the valve should be open.

The ability of the control algorithm to create a desired flow rate can be measured by setting the flow rate and closing the effluent valves from the accumulator. The result is that the accumulator will gradually fill and as it fills $f_{valve} $ will gradually increase so the flow rate into the accumulator remains constant. The slope of the pressure vs. time line is proportional to the flow rate.


Air Flow Control Calibration Procedure
--------------------------------------

 1. Set up the airflow control hardware (Figure \eqref{ZEqnNum586787}).
 1. Set the Process Controller to operator selected state.
 1. Set the state to ``empty accumulator.''
 1. If desired open the cap of the accumulator to rapidly release any stored air.
 1. Set the Process Controller to automatic mode.
 1. The process controller should quickly cycle through the calibration step and then begin attempting to control the air flow rate to the target value.


Algorithm to Measure the Oxygen Uptake Rate
===========================================

One of the objectives of a wastewater treatment plant is to reduce the Biochemical Oxygen Demand (BOD). The minimum national standard for secondary wastewater treatment is that the average 30-day concentration of BOD${}_{5}$ be less than 30 mg/L. Biochemical oxygen demand is difficult to measure since it takes 5 days for a test. The long test period also precludes the possibility of using BOD as a control parameter in operating a WWTP. Most WWTPs don't have the luxury of knowing the concentration of influent BOD. For the NRP the composition and properties of the synthetic feed are known. Thus it should be possible to estimate the BOD removal and the residual BOD by measuring the oxygen uptake rate. Temporarily increasing the oxygen concentration in the sequencing batch reactor, turning the airflow off, and then measuring the decrease in oxygen concentration with time can measure the oxygen uptake rate. The aeration rate with the airflow turned off is insignificant and thus the rate of oxygen consumption is equal to the rate of change of the oxygen concentration.

References
==========

 Cicek, N., J. P. Franco, et al. (1998). ``Using a Membrane bioreactor to reclaim wastewater.'' \underbar{Journal American Water Works Association} \textbf{90}\eqref{GrindEQ__11_}: 105-113.

 Metcalf \& Eddy, placeI., G. Tchobanoglous, et al. (2003). \underbar{Wastewater Engineering: Treatment and Reuse}. placeStateNew York, McGraw Hill.

 Rittmann, B. E. and P. L. McCarty (2001). \underbar{Environmental Biotechnology: Principles and Applications}. placeStateNew York, McGraw Hill.

 R. Mikler, W. Kramer, O. Doblhoff - Dier, K. Bayer (dateMonth4Day7Year199504/07/95) \underbar{Strategies For Optimal Dissolved Oxygen (Do) Control} http://www.boku.ac.at/iam/poster/doxygen.htm




------------------
Lab Setup}

For 6 weeks of operation of 4 plants prepare 20 L of  100x organic stock. Mix in a 20 L Jerrican and use a power mixer inserted through the opening to mix after the addition of \textbf{each} chemical. Store 100x stock in the walk in refrigerator on the 2${}^{nd}$ floor.


\end{document}
