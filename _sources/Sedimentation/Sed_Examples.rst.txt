.. _title_Sedimentation_Examples:

***************************************
Sedimentation Examples
***************************************

These are a few short examples of calculations required for sedimentation tank design. More examples can be found in the :ref:`Sedimentation Design Solution <heading_Sed_Design_Challenge_Solution>`.

Tube Settler Design
===============================

Design a tube settler for a laboratory scale sedimentation tank. The vertical section of the sedimentation tank, :math:`v_{S,V}`, has a net upflow velocity of 3 mm/s. This velocity is maintained in the tube settler, :math:`v_{\alpha}`. The target capture velocity is 0.2 mm/s. The tube settler diameter is 2.54 cm.

.. math:: \frac{\bar v_{S,V}}{v_c} = \frac{L}{D} \cos \alpha \sin \alpha + \sin ^2 \alpha

.. math:: \bar v_{S,V} = \bar v_\alpha\sin \alpha

Solve for the length of the tube settler.

.. math:: L = \frac{D}{\cos \alpha}\left(\frac{\bar v_\alpha}{\bar v_c} - \sin \alpha\right)


.. code:: python

  from aguaclara.core.units import unit_registry as u

  import numpy as np

  v_alpha = 3 * u.mm/u.s
  v_c = 1 * u.mm/u.s
  D = 2.54 * u.cm
  alpha = 60 * u.deg

  def L_settler(D,alpha,v_alpha,v_c):
   return D/np.cos(alpha)*(v_alpha/v_c - np.sin(alpha))

  print(L_settler(D,alpha,v_alpha,1*u.mm/u.s))
  print(L_settler(D,alpha,v_alpha,0.2*u.mm/u.s))

The tube settler above the floc hopper needs to be 72 cm long. The tube settler should provide a capture velocity of at least 1 mm/s prior to the floc hopper. Thus there should be 11 cm below the floc hopper.

.. _heading_flow_thru_diffuser:

Determining flow through a diffuser
====================================

What is the flow rate of a single diffuser in the bottom of the sedimentation tank? Consider a sedimentation tank that is 6 m long, 1 m wide and 2 m deep, with an upflow velocity of 1 mm/s and a diffuser spacing of 5 cm.

What is this question really asking? This question is asking us to understand that each diffuser "serves" a specific cross-sectional area of the sedimentation tank; all of the diffusers together serve the entire area of the sedimentation tank. So, let's imagine a single diffuser serving a slice of a sedimentation tank. With this in mind, we can easily solve this using :math:`Q = vA`. The area, :math:`A`, is the slice of the sedimentation tank that we are serving. We are told that the tank is 1 m wide, so :math:`W_{tank} = 1` m. The length of the slice is dictated by the spacing of the diffusers, :math:`B_{diff}`, so :math:`B_{diff} = 5` cm.

.. math:: A = B_{diff}W_{tank}

.. math:: A = 5cm * 1m

.. math:: A = 50,000mm^2

The problem statement includes that :math:`v_{S,V} = 1` mm/s. Plugging into our flow equation,

.. math:: Q_{diff} = v_{S,V}A

.. math:: Q_{diff} = (1 \frac{mm}{s})(50,000mm^2)

.. math:: Q_{diff} = 50,000 \frac{mm^3}{s}

.. math:: Q_{diff} = 50 \frac{mL}{s}

The flow rate of each diffuser is :math:`50 \frac{mL}{s}`.

Identify Failure Modes from Old Design
==================================================

Look at a proposed design for the bottom of the sedimentation tank, shown in :numref:`figure_failure_mode_example`. This design has an influent manifold at the bottom of the tank. Water flows upwards from the influent manifold. At one end of the influent manifold, there is a drain port. Above the influent manifold, there is a single slot that extends the length of the sedimentation tank. There are no diffusers in this design.

.. _figure_failure_mode_example:

.. figure:: Images/failure_mode_example.png
    :height: 300px
    :align: center
    :alt: Proposed sedimentation tank design.

    Proposed sedimentation tank design.

What are the failure modes for this design?

Some issues are:

- flocs can settle in the influent manifold, specifically at the end of the influent manifold pipe;
- the upflow line jet may be impacted and bent by settling flocs, allowing for floc settling on one side of the tank;
- without diffusers, there may not be uniform flow distribution from one end of the sedimentation tank to the other;
- without diffusers, there will be large flow circulations inside the sedimentation tank.

This design has never been built and never will be. Understanding what the problems are with this design will help us design better in the future.

Comments, Corrections, or Questions
====================================

This textbook is an ever-evolving project. If you find any errors while you are reading, or if you find something unclear, please let the authors know. Write your comment in `this Github issue <https://github.com/AguaClara/Textbook/issues/86>`_ and it will be addressed as soon as possible. Please look at other comments before writing your own to avoid duplicate comments.
