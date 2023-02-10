.. raw:: html

    <embed>
       <link rel="canonical" href="https://aguaclara.github.io/Textbook/Operation/Coagulant_Automation.html" />
       <script src="https://hypothes.is/embed.js" async></script>
    </embed>

.. _title_Coagulant_Automation:

********************
Coagulant Automation
********************

Automating the coagulant dose is difficult because it hasn't been clear what measurement to use that could be driven to a target value by varying the coagulant dose and that would then provide the desired plant performance. Based on the previous understanding of coagulant neutralizing the negative charge of raw water particles, many water treatment plants have attempted to use streaming current meters to set the coagulant dose. That method doesn't work well because it is the fractional coverage of the primary particles with sticky coagulant nanoparticles that sets the attachment efficiency and that does not require a neutral surface charge.

The concentration of primary particles exiting the flocculator could be used to guide the coagulant dose. The flocculated suspension can not be sampled directly with a particle counter because the particle concentration is too high. Given that we are only interested in the concentration of primary particles, we can use a tube settler to quickly reduce the particle concentration of the sample line going to the particle counter while still enabling an accurate count of the primary particle concentration.


.. _figure_TubeSettlerFlocMonitor:

.. figure:: ../Images/TubeSettlerFlocMonitor.png
   :width: 400px
   :align: center
   :alt: TubeSettlerFlocMonitor

   Proposed particle counter monitoring of flocculation performance.


The relationship between attachment efficiency and primary particle concentration after flocculation is given by Equation :eq:`CpofGtlamSim`. For the simple case of no coagulant demand by dissolved organic matter it is reasonable to assume that the attachment efficiency is proportional to the ratio of the coagulant dose to the raw water turbidity.

.. math::
  :label: coverageofdoseandntu

  \alpha \propto \frac{C_{coag}}{C_{turbidity}}.

All of the primary particle properties and plant design terms can be treated as a single unknown, :math:`K_u`. Thus Equation :eq:`CpofGtlamSim` simplifies to

.. math::
  :label: cpofcoagdoseandturbidity

  C_{P} = \frac{ K_u}{\left( \frac{C_{coag}}{C_{turbidity}} \right)^\frac{3}{2}}.

We can use Equation :eq:`cpofcoagdoseandturbidity` to estimate the value of :math:`K_u`. There is a time lag, :math:`\theta` between a change in coagulant dose and particle count change related to the residence time in the rapid mix, flocculator, and tube settler. The turbidity and coagulant dose for this equation are the values at time :math:`t-\theta`.

.. math::
  :label: K_u

  K_{u_t} = C_{P_t}\left( \frac{C_{coag_{t-\theta}}}{C_{turbidity_{t-\theta}}} \right)^\frac{3}{2}

where :math:`C_{P_t}` is the concentration of primary particles measured at time t.

Now that we have an estimate of the constant, :math:`K_u`, we can estimate the new coagulant dose that will be required to drive the concentration of primary particles to the target level. The target level will be set such that the plant performance meets both regulatory and operational efficiency goals.

Equation :eq:`cpofcoagdoseandturbidity` can be solved for the coagulant dose

.. math::
  :label: coagdoseofCpKuandturbidity

  C_{coag_{goal_t}}  =C_{turbidity_t}\left( \frac{K_{u_t}}{C_{P_{goal}}} \right)^\frac{2}{3}

Combining Equations :eq:`K_u` and :eq:`coagdoseofCpandturbidity` we obtain a simple method to set the correct coagulant dose given current performance.

.. math::
  :label: coagdoseofCpandturbidity

  C_{coag_{goal_t}}  =C_{coag_{t-\theta}}\left( \frac{C_{P_t}}{C_{P_{goal}}} \right)^\frac{2}{3}\left( \frac{C_{turbidity_t}}{C_{turbidity_{t-\theta}}} \right)

If the particle count is too high the coagulant dose will be increased. The coagulant dose will also be increased if the raw water turbidity increases. In this system the flocculator and tube settler system is providing continuous guidance on how to optimize the coagulant dose. Small errors in the model or in measurements will be self correcting because the value of :math:`K_u` will be continuously updated.

The next improvement in this simple model is to add a correction factor for dissolved organic matter. The dissolved organic matter effectively inactivates some of the coagulant. The dissolved organic matter is measured as absorbance at 254 nm. The amount of coagulant that is tied up with dissolved organic matter is

.. math::
  :label: UV_coag_consumed

  C_{coag_{DOM}}  = A_{254nm} K_{DOM}


Equation :eq:`K_u` becomes

.. math::
  :label: K_u_UV

  K_{u_t} = C_{P_t}\left( \frac{C_{coag_{t-\theta}} - A_{254nm_{t-\theta}} K_{DOM}}{C_{turbidity_{t-\theta}}} \right)^\frac{3}{2}

The dissolved organic matter simply reduces the amount of coagulant that is available to make the inorganic particles sticky. The required coagulant dose can be obtained from Equation :eq:`coagdoseofCpKuandturbidity`.

.. math::
  :label: coagdoseofCpKuUVandturbidity

  C_{coag_{goal_t}}  =C_{turbidity_t}\left( \frac{K_{u_t}}{C_{P_{goal}}} \right)^\frac{2}{3} + A_{254nm_t} K_{DOM}


Combining Equations :eq:`K_u_UV` and :eq:`coagdoseofCpKuUVandturbidity` we obtain a simple method to set the correct coagulant dose given current performance.

.. math::
  :label: coagdoseofCpUVandturbidity

  C_{coag_{goal_t}}  = \left(C_{coag_{t-\theta}} - A_{254nm_{t-\theta}} K_{DOM}\right) \left( \frac{C_{P_t}}{C_{P_{goal}}} \right)^\frac{2}{3}\left( \frac{C_{turbidity_t}}{C_{turbidity_{t-\theta}}} \right) + A_{254nm_t} K_{DOM}

We need a method to estimate :math:`K_{DOM}`. The simplest assumption is that :math:`K_{DOM}` is constant over time. The experimental results obtained by Yingda Du (see :numref:`figure_floc_model_HA` `by Yingda Du, et al., 2019 <https://www.liebertpub.com/doi/abs/10.1089/ees.2018.0405>`_) suggest that approximately 1 mg/L of aluminum is required to tie up 12 mg/L of humic acid.  The humic acid concentration was based on the dry weight and humic acid is approximately 48% carbon. Thus 6 mg of humic acid as carbon require 1 mg/L of aluminum. The absorbance at 254 nm was measured by `Rodrigues. et al., 2008 <https://core.ac.uk/reader/55618110?utm_source=linkout>`_  to be 0.055(humic acid as carbon in mg/L). Thus :math:`0.33A_{254nm}` is expected to consume 1 mg/L of aluminum where :math:`A_{254nm}` is the UV 254 absorbance in a 1 cm sample cell. The remaining required conversion is from the concentration of aluminum to the coagulant dose as measured at the water treatment plant.

It would also be possible to use recent operating data to find the best estimates of both :math:`K_{DOM}` and :math:`K_u`. In any case the effect of adding the dissolved organic matter components to the model will be to reduce the magnitude of the coagulant fluctuations because a significant part of the coagulant dose is not affected by the primary particle concentration.

Linearized Two Parameter Dosing Model
=====================================

Parameter estimation
--------------------

The first step is to develop a method to estimate the unknown parameters using recently acquired performance data at the water treatment plant. The two fitting parameters, :math:`K_{DOM}` and :math:`K_u`, can be estimated using recent data and linear regression. Equation :eq:`CpofGtlamSim` can be modified to account for the coagulant dose required to tie up the dissolved organic matter.

.. math::
  :label: cpofcoagdoseandturbiditywithDOM

  C_{P} = \frac{ K_u}{\left( \frac{C_{coag} - C_{coag_{DOM}}}{C_{raw_{NTU}}} \right)^\frac{3}{2}}.

The concentration of primary particles after sedimentation, :math:`C_{P}` can be approximated by a measurement of the clarified water turbidity, :math:`C_{clarified_{NTU}}`. The time lag between raw and clarified measurements is the residence time, :math:`\theta` for rapid mix, flocculation, and clarification processes.

.. math::
  :label: 2paramCoagModelDraft0

  C_{clarified_{NTU_t}} = \frac{ K_{u_{t-\theta}}}{\left( \frac{C_{coag_{t-\theta}} - C_{coag_{DOM_{t-\theta}}}}{C_{raw_{NTU_{t-\theta}}}} \right)^\frac{3}{2}}.

Linearize the equation to obtain coagulant dose as a function of a measured value and unknown slope and intercept.

.. math::
  :label: 2paramCoagModelDraft1

  C_{clarified_{NTU_t}}^{-\frac{2}{3}} = \frac{C_{coag_{t-\theta}} - C_{coag_{DOM_{t-\theta}}}}{ C_{raw_{NTU_{t-\theta}}} K_{u_{t-\theta}}^{\frac{2}{3}}}

Separate terms and then solve for :math:`C_{coag}`. Replace :math:`K_{u_{t-\theta}}^{\frac{2}{3}}` with :math:`K_{u_{t-\theta}}^*`

.. math::
  :label: LinearizedCoagModel

  C_{coag_{t-\theta}} = K_{u_{t-\theta}}^* \frac{C_{raw_{NTU_{t-\theta}}}}{C_{clarified_{NTU_t}}^{\frac{2}{3}}} + C_{coag_{DOM_{t-\theta}}}

We now have an equation in the form y = mx + b where x is measured values, m and b are the fitting parameters, and y is the coagulant dose.

Coagulant Dose Algorithm
------------------------

The parameter :math:`K_{u_{t-\theta}}^*` is a property of the primary particles and the flocculation and clarification processes. The parameter :math:`C_{coag_{DOM}}` is controlled by the concentration of dissolved organic matter that adsorbs to the coagulant nanoparticles. Initial expectations are that :math:`K_{u_{t-\theta}}^*` changes less over time than the parameter :math:`C_{coag_{DOM}}`.

In any case "recent" data will be plotted in the linearized form as given by Equation :eq:`LinearizedCoagModel`. Linear regression will be used to obtain the two fitting parameters and

If :math:`K_{u_{t-\theta}}^*` is known from linear regression over a period of weeks, then the current :math:`C_{coag_{DOM}}` could be estimated from the previous hour of operation so that the recent dissolved organic matter concentration is used when setting the coagulant dose.

Data processing
---------------

#. Acquire data at some high rate (perhaps 1 s intervals)
#. Set the number of updates per hydraulic residence time (HRT) (perhaps 10) and average the incoming data to that update interval
#. Hold the averaged data in a buffer with each data set including a time stamp.

The coagulant dose can then be calculated as

.. math::
  :label: coagdoseofCpKu*UVandturbidity

  C_{coag_{goal_t}}  = C_{turbidity_t}K_{u_{t-\theta}}^* C_{P_{goal}}^\frac{-2}{3} + C_{coag_{DOM_{t-\theta}}}

Improved Linearized Model
=========================

We previously assumed that we could neglect the effect of the settled water turbidity in Equation :ref:`intdCPlam`. Here we don't make this assumption and linearize the model again. We begin with Equation :ref:`intdCPlam`, combine unknowns into a single constant, assume that the probability of attachment is proportional to the coagulant dose normalized by the concentration of primary particles, and replace primary particle concentration with turbidity.

.. math::
  :label:

	 \frac{3}{2\pi}\left(\rho_{P}\frac{\pi}{6}\right)^{2/3}\left(C_{clarified_{NTU_t}}^{-2/3}-C_{raw_{NTU_{t-\theta}}}^{-2/3}\right)=k\bar{\alpha}\tilde{G}\theta.

Replace alpha with the ratio of coagulant not tied up by dissolved organic matter to raw water turbidity.

.. math::
  :label:

	 \left(C_{clarified_{NTU_t}}^{-2/3}-C_{raw_{NTU_{t-\theta}}}^{-2/3}\right)=\frac{C_{coag_{t-\theta}} - C_{coag_{DOM_{t-\theta}}}}{C_{raw_{NTU_{t-\theta}}}}k\tilde{G}\theta \frac{2\pi}{3}\left(\frac{6}{\rho_{P}\pi}\right)^{2/3}

Create one grouping of constants.

.. math::
  :label:

	 \left(C_{clarified_{NTU_t}}^{-2/3}-C_{raw_{NTU_{t-\theta}}}^{-2/3}\right)=\frac{C_{coag_{t-\theta}} -C_{coag_{DOM_{t-\theta}}}}{C_{raw_{NTU_{t-\theta}}}}k\tilde{G}\theta \frac{2\pi}{3}\left(\frac{6}{\rho_{P}\pi}\right)^{2/3}

Replace constants with :math:`K_{u_{t-\theta}}^*`.

.. math::
  :label:

	 \left(C_{clarified_{NTU_t}}^{-2/3}-C_{raw_{NTU_{t-\theta}}}^{-2/3}\right)=\frac{C_{coag_{t-\theta}}-C_{coag_{DOM_{t-\theta}}}}{C_{raw_{NTU_{t-\theta}}}}K_{u_{t-\theta}}^*

Now solve for the coagulant dose with an equation of the form y = mx + b. The parameter  :math:`K_{u}^*` incorporates properties of the primary particles (density and diameter), the flocculator collision potential (:math:`\tilde{G}`), the coagulant nanoparticle properties (density and diameter), and the first order rate constant, k, that describes the conversion of primary particles into settleable flocs. One possible assumption is that :math:`K_{u}^*` can be treated as a constant.

.. math::
  :label: fullcoagdoseofCpKu*UVandturbidity

	 C_{coag_{t-\theta}} = \frac{1}{K_{u^*}}C_{raw_{NTU_{t-\theta}}}\left(C_{clarified_{NTU_t}}^{-2/3}-C_{raw_{NTU_{t-\theta}}}^{-2/3}\right)+C_{coag_{DOM_{t-\theta}}}

The coagulant demand of the DOM is obtained by rearranging Equation :eq:`fullcoagdoseofCpKu*UVandturbidity`.

.. math::
  :label: DOMcoagDemand

	 C_{coag_{DOM_{t-\theta}}} = C_{coag_{t-\theta}} - \frac{1}{K_{u^*}}C_{raw_{NTU_{t-\theta}}}\left(C_{clarified_{NTU_t}}^{-2/3}-C_{raw_{NTU_{t-\theta}}}^{-2/3}\right)

Given the estimate of the DOM coagulant demand at a previous time we can obtain an estimate of the required coagulant dose at time t. First rewrite Equation :eq:`fullcoagdoseofCpKu*UVandturbidity` for time t.

.. math::
  :label: targetfullcoagdoseofCpKu*UVandturbidity

	 C_{coag_{t}} = \frac{1}{K_u^*}C_{raw_{NTU_t}}\left(C_{clarified_{NTU_{t+\theta}}}^{-2/3}-C_{raw_{NTU_t}}^{-2/3}\right)+C_{coag_{DOM_t}}

If the coagulant DOM demand doesn't change significantly in the time used to update the coagulant dose, then Equation :eq:`DOMcoagDemand` can be used to eliminate :math:`C_{coag_{DOM_t}}` from Equation :eq:`targetfullcoagdoseofCpKu*UVandturbidity`.

The coagulant dosing system must include guardrails to ensure that the coagulant dose is within a reasonable range. There exists the possibility of a turbidimeter giving incorrect data that would result in a coagulant dose far outside a range that would ensure reasonable plant performance. The potential failures include:

 * settled water turbidity that is very low because the plant is starting up after an extended shutdown
 * faulty turbidimeter readings due to a dirty sample cell

To reduce the likelihood of a treatment failure the estimated DOM coagulant demand can be compared with a reasonable range and if it is out of that range the estimated DOM coagulant demand can be forced back into the reasonable range. To prevent an excessively low coagulant dose the DOM coagulant demand can be limited to positive values. If it is known that the DOM coagulant demand is always exceeds a larger value, that larger value can be used as a lower limit. The upper limit can be set based on observation of the raw water quality.   
