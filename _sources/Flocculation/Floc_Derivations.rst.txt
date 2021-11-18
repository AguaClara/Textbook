.. _title_Flocculation_Derivations:

*************************
Flocculation Derivations
*************************

.. _heading_Design_Equations_for_the_Flocculator:

Design Equations for the Flocculator
====================================

This document contains the derivation for the minimum allowable width of
a flocculator channel based on the requirements that
:math:`3 < \Pi_{H_eS} < 6` and that we maintain the :math:`\bar G` that
serves as a basis for design. The final parameter derived is
:math:`W_{Min, \, \Pi_{H_eS}}`.

Width
-----

Our two restrictions are: 

#. Ensuring that we maintain the :math:`\bar G` we get based on our input parameters.
#. Ensuring that :math:`3 < \frac{H_e}{S} < 6`

First, we begin by setting the two equations for energy dissipation rate, :math:`\bar \varepsilon = \nu \bar G^2` and :math:`\bar \varepsilon = \frac{g h_{L_{floc}}}{\theta}` equal to each other to bring :math:`\bar G` into the equation.

.. math:: \nu \bar G^2 = \frac{g h_{L_{floc}}}{\theta}

For the following steps, we will consider the flow through a single flow expansion :math:`H_e`, not through the entire flocculator. This could be from baffle to obstacle, obstacle to baffle, obstacle to obstacle, or baffle to baffle depending on how many obstacles are in the design. This means that the residence time is the time between expansions, :math:`\theta_e`, and the head loss is for one expansion, :math:`h_{L_{e}}`.

From here we make three subsequent substitutions: first
:math:`h_{L_{e}} = K \frac{\bar v^2}{2g}`, then
:math:`\theta_e = \frac{H_e}{\bar v}`, and finally
:math:`\bar v = \frac{Q}{WS}`

.. math:: \nu \bar G^2 = K \frac{\bar v^2}{2 \theta_e}

.. math:: \nu \bar G^2 = K \frac{\bar v^3}{2 H_e}

.. math:: \nu \bar G^2 = \frac{K}{2 H_e} \left( \frac{Q}{WS} \right)^3

Now we can solve this equation for channel width, :math:`W`.

.. math:: W = \frac{Q}{S}\left( \frac{K}{2 H_e \nu \bar G^2} \right)^\frac{1}{3}

From here, we can define :math:`\Pi_{H_eS} = \frac{H_e}{S}` and
substitute :math:`S = \frac{H_e}{\Pi_{H_eS}}` into the previous equation
for :math:`W` to get :math:`W_{Min, \, \Pi_{H_eS}}`:

.. math::


   W_{Min, \, \Pi_{H_eS}} = \frac{\Pi_{H_eS}Q}{H_e}\left( \frac{K}{2 H_e \nu \bar G^2} \right)^\frac{1}{3}


| This equation represents the absolute smallest width of a flocculator
  channel if we consider the lowest value of :math:`\Pi_{H_eS}` and the
  highest possible value of :math:`H_e`:
| :math:`H_e = H`, this implies that there are no obstacles between
  baffles
| :math:`\Pi_{H_eS} = 3`
