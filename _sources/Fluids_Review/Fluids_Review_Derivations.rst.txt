.. _fluids_review_derivations:

***************************************************
Fluids Review Derivations
***************************************************



.. _minor_loss_equation_derivation:

Minor Loss Equation
====================
This section contains the derivation of the minor loss equation using the following image as a reference. The derivation begins with a slightly simplified energy equation across the control volume show. Our energy equation begins with :math:`h_P` and :math:`h_T` having been
eliminated.

.. _minor_loss_pipe:
.. figure:: Images/minor_loss_pipe.png
    :width: 700px
    :align: center
    :alt: Example of flow expansion resulting in a minor loss

    Example of a minor loss due to a flow expansion

.. math::

    \frac{p_{in}}{\rho g} + {z_{in}} + \frac{\bar v_{in}^2}{2g} = \frac{p_{out}}{\rho g} + z_{out} + \frac{\bar v_{out}^2}{2g} + h_L

Since the elevations of the ‘in’ and ‘out’ references are the same, we can eliminate :math:`z_{in}` and :math:`z_{out}`. As we are considering such a small length of pipe, we will neglect the major loss component of head loss. Thus, :math:`h_L = h_e`. The following three equations are all the same, simply rearranged to solve for :math:`h_e`.

.. math::

    \frac{p_{in}}{\rho g} + \frac{\bar v_{in}^2}{2g} = \frac{p_{out}}{\rho g} + \frac{\bar v_{out}^2}{2g} + h_e

.. math::

    \frac{p_{in} - p_{out}}{\rho g} = \frac{\bar v_{out}^2 - \bar v_{in}^2}{2g} + h_e

.. math::

    h_e = \frac{p_{in} - p_{out}}{\rho g} + \frac{\bar v_{in}^2 - \bar v_{out}^2}{2g}

This last equation to determine :math:`h_e` has four variables, and we would like it to have just one or two. Thus, we will invoke conservation of momentum in the horizontal direction across our control volume to remove some variables. The difference in momentum from the :math:`in` point to the :math:`out` point is result of the pressure difference between each end of the control volume. We will be considering the pressure at the centroid of our control surfaces, and we will neglect shear along the pipe walls. After these assumptions, our momentum equation becomes the following:

.. math::

    M_{in, \, x} + M_{out, \, x} = F_{p_{in, \, x}} + F_{p_{out, \, x}}

| Such that:
| :math:`M_{x}` = momentum flowing through the control volume in the x-direction
| :math:`F_{p_x}` = force due to pressure acting on the boundaries of the control volume in the x-direction

Recall that momentum is mass times velocity, :math:`m\bar v` with units of :math:`\frac{[M][L]}{[T]}`, for solid bodies. Since we consider water flowing through a pipe, there is not one singular mass. Instead, there is a mass flow rate, or a mass per time indicated by :math:`\rho Q` (:math:`\frac{[M]}{[T]}`). Applying the continuity equation :math:`Q = \bar v A` and multiplying :math:`\rho Q` by :math:`\bar v` to obtain the correct units, we get to the following equation for the momentum of a fluid flowing through a pipe, :math:`M = \rho \bar v^2 A`. The pressure force is simply the pressure at the centroid of the flow multiplied by the area the pressure is acting upon, :math:`p A`. To ensure correct sign convention, we will make each side of the equation negative for reasons discussed shortly. Since :math:`\bar v_{in} > \bar v_{out}`, the left hand side becomes :math:`M_{out} - M_{in}`. The reduction in velocity from :math:`in` to :math:`out` causes an increase in pressure, therefore :math:`p_{in} - p_{out}` will be negative. With these substitutions, the conservation of momentum equation becomes as follows:

.. math::

    \rho \bar v_{out}^2 A_{out} - \rho \bar v_{in}^2 A_{in} = p_{in} A_{out} - p_{out} A_{out}

Note that the area term attached to :math:`p_{in}` is actually :math:`A_{out}` instead of :math:`A_{in}`, as one might think. This is because :math:`A_{out} = A_{in}`. We chose our control volume to start a
few millimeters into the larger pipe, which means that the cross-sectional area does not change over the course of the control volume.

By dividing both sides of the equation by :math:`A_{out} \rho g`, we obtain the following equation, which contains the very same pressure term as our adjusted energy equation above. This is why we chose a negative sign convention.

.. math::

    \frac{p_{in} - p_{out}}{\rho g} = \frac{\bar v_{out}^2 - \bar v_{in}^2 \frac{A_{in}}{A_{out}}}{g}

Now, we combine the adjusted energy, momentum, and continuity equations:

.. math::

    {\rm{Energy \, equation:}} \,\,\,  h_e = \frac{p_{in} - p_{out}}{\rho g} + \frac{\bar v_{in}^2 - \bar v_{out}^2}{2g}

.. math::

    {\rm{Momentum \, equation:}} \,\,\, \frac{p_{in} - p_{out}}{\rho g} = \frac{\bar v_{out}^2 - \bar v_{in}^2 \frac{A_{in}}{A_{out}}}{g}

.. math::

    {\rm{Continuity \, equation:}} \,\,\, \frac{A_{in}}{A_{out}} = \frac{\bar v_{out}}{\bar v_{in}}

To obtain an equation for minor losses with just two variables, :math:`\bar v_{in}` and :math:`\bar v_{out}`.

.. math::

    h_e = \frac{\bar v_{out}^2 - \bar v_{in}^2\frac{\bar v_{out}}{\bar v_{in}}}{g} + \frac{\bar v_{in}^2 - \bar v_{out}^2}{2g}

To combine the two terms, the numerator and denominator of the first term, :math:`\frac{\bar v_{out}^2 - \bar v_{in}^2\frac{\bar v_{out}}{\bar v_{in}}}{g}` will be multiplied by :math:`2` to become :math:`\frac{2 \bar v_{out}^2 - 2 \bar v_{in}^2\frac{\bar v_{out}}{\bar v_{in}}}{2 g}`. The equation then looks like:

.. math::

    h_e = \frac{\bar v_{out}^2 - 2 \bar v_{in} \bar v_{out} + \bar v_{in}^2}{2g}


.. _final_minor_loss_equations:

Final Forms of the Minor Loss Equation
-----------------------------------------
Factoring the numerator yields to the first ‘final’ form of the minor loss equation:

.. math::

    {\rm{ \mathbf{First \, form:} }} \,\,\, h_e = \frac{\left( \bar v_{in}  - \bar v_{out} \right)^2}{2g}

From here, the two other forms of the minor loss equation can be derived by solving for either :math:`\bar v_{in}` or :math:`\bar v_{out}` using the ubiquitous continuity equation :math:`\bar v_{in} A_{in} = \bar v_{out} A_{out}`:

.. math::

    {\rm{ \mathbf{Second \, form:} }} \,\,\, h_e = \frac{\bar v_{in}^2}{2g}{\left( {1 - \frac{A_{in}}{A_{out}}} \right)^2} = \frac{\bar v_{in}^2}{2g} K_e^{'}, {\rm \, \, \, where \, \, \,} K_e^{'} = \left( 1 - \frac{A_{in}}{A_{out}} \right)^2

.. math::
 :label: minor_loss_equation

    \color{purple}{
    {\rm{ \mathbf{Third \, form:} }} \,\,\, h_e = \frac{\bar  v_{out}^2}{2g}{\left( {\frac{A_{out}}{A_{in}}} -1 \right)^2} = \frac{\bar v_{out}^2}{2g} K_e, {\rm \, \, \, where \, \, \,} K_e = \left( \frac{A_{out}}{A_{in}} - 1 \right)^2
    }

.. note:: You will often see :math:`K_e^{'}` and :math:`K_e` used without the :math:`e` subscript, they will appear as :math:`K^{'}` and :math:`K`.

Being familiar with these three forms and how they are used will be of great help throughout the class. The third form is the one that is most commonly used.
