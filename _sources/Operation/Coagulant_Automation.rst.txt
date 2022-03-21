.. raw:: html

    <embed>
       <link rel="canonical" href="https://aguaclara.github.io/Textbook" />
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

  C_{cp} = \frac{ K_u}{\left( \frac{C_{coag}}{C_{turbidity}} \right)^\frac{3}{2}}.

We can use Equation :eq:`cpofcoagdoseandturbidity` to estimate the value of :math:`K_u`. There is a time lag, :math:`\theta` between a change in coagulant dose and particle count change related to the residence time in the rapid mix, flocculator, and tube settler. The turbidity and coagulant dose for this equation are the values at time :math:`t-\theta`.

.. math::
  :label: K_u

  K_{u_t} = C_{cp_t}\left( \frac{C_{coag_{t-\theta}}}{C_{turbidity_{t-\theta}}} \right)^\frac{3}{2}

where :math:`C_{cp_t}` is the concentration of primary particles measured at time t.

Now that we have an estimate of the constant, :math:`K_u`, we can estimate the new coagulant dose that will be required to drive the concentration of primary particles to the target level. The target level will be set such that the plant performance meets both regulatory and operational efficiency goals.

Equation :eq:`cpofcoagdoseandturbidity` can be solved for the coagulant dose

.. math::
  :label: coagdoseofCpKuandturbidity

  C_{coag_{goal_t}}  =C_{turbidity_t}\left( \frac{K_{u_t}}{C_{cp_{goal}}} \right)^\frac{2}{3}

Combining Equations :eq:`K_u` and :eq:`coagdoseofCpandturbidity` we obtain a simple method to set the correct coagulant dose given current performance.

.. math::
  :label: coagdoseofCpandturbidity

  C_{coag_{goal_t}}  =C_{coag_{t-\theta}}\left( \frac{C_{cp_t}}{C_{cp_{goal}}} \right)^\frac{2}{3}\left( \frac{C_{turbidity_t}}{C_{turbidity_{t-\theta}}} \right)

The next improvement in this simple model would be to add a correction factor for dissolved organic matter. The dissolved organic matter would effectively inactivate a concentration of the coagulant.
