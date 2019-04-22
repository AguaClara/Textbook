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

Diffuser Design
================

We will start our design of the sedimentation tank by considering the diffusers.

Calculate the maximum velocity of water leaving the diffuser based on the maximum head loss. Assume that the majority of head loss is the kinetic energy of the flow exiting the diffuser slot (this assumption will be checked later). Assume K=1.



Calculate the minimum inner width of the diffuser. Assume that the diffuser slot is continuous over the entire length of the sedimentation tank to get an initial estimate (it isn't actually continuous because it is made from many flattened diffuser pipes).

Define your answers as variables and then print those variables.

Given parameters:

.. code:: python

  from aguaclara.core.units import unit_registry as u

  import numpy as np

  #given sedimentation inlet maximum headloss
  headloss_sed_inlet_max = 1 * u.cm
  #given sedimentation tank up flow velocity
  V_sed_up = 1 * u.mm/u.s
  #given sedimentation tank width
  W_sed = 42 * u.inch

To find the maximum velocity based on maximum headloss we will use the minor loss equation.

.. math:: hl_{inlet} = K \frac{V_{jet}^{2}}{2g}

To find the minimum width based on the maximum velocity through the diffuser, we will use conservation of mass. Since it is an incompressible fluid the flow rate entering from the diffuser line jet must be equal to the flow rate up through the sedimentation tank.

.. math:: V_{jet}W_{diff} L_{sed} = V_{sed,up}W_{sed}L_{sed}

.. code:: python



  # minor loss equation with K=1
  V_diffuser_max = (np.sqrt((2 * g * headloss_sed_inlet_max))).to(u.m / u.s)
  print('The maximum velocity of the sed tank diffusers is',V_diffuser_max)

  # mass conservation
  W_diffuser_inner_min = ((V_sed_up / V_diffuser_max) * W_sed).to(u.mm)
  print('The minimum width of the sed tank diffusers is',W_diffuser_inner_min)


The maximum velocity of the sedimentation tank diffusers is 0.4429 meter / second
The minimum width of the sedimentation tank diffusers is 2.409 millimeter

Comments, Corrections, or Questions
====================================

This textbook is an ever-evolving project. If you find any errors while you are reading, or if you find something unclear, please let the authors know. Write your comment in `this Github issue <https://github.com/AguaClara/Textbook/issues/86>`_ and it will be addressed as soon as possible. Please look at other comments before writing your own to avoid duplicate comments.
