.. _title_Rapid_Mix_Design:

*******************
Rapid Mix Design
*******************

As of 2018 the design for AguaClara rapid mix units has been based on the goal of achieving a target energy dissipation rate. This in turn was based on the assumption that it was important to rapidly mix the coagulant with the water, perhaps to minimize the self-aggregation of coagulant nanoparticles. We don't yet have any experimental evidence that rapid mixing is important and it is quite likely that the energy dissipation rate found in the hydraulic flocculator is sufficient to provide the required mixing.

The following example is provided with a good deal of skepticism as to whether the design criteria have any influence on flocculation performance. The design requirements for fluid mixing of the coagulant is an area that needs research.

Orifice Diameter to obtain Target Mixing
=========================================

The following equations need to be re-derived based on new definition of :math:`\Pi_{JetRound}`

.. math::  A_{Orifice} \Pi_{vc} = A_{Jet}

.. math::  D_{Orifice} \sqrt{\Pi_{vc}} = D_{Jet}

.. math::  \varepsilon_{Max} \cong \frac{ \left( \Pi_{JetRound} \frac{4Q}{\pi D_{Jet}^2} \right)^3}{D_{Jet}}

.. math::  D_{Orifice} \cong \left( \frac{4 Q \Pi_{JetRound}}{\varepsilon_{Max}^{\frac{1}{3}} \pi} \right)^{\frac{3}{7}} \frac{1}{\sqrt{\Pi_{vc} }}

**Off-slide**

.. math::

   \varepsilon_{Max} \cong  \frac{ \left( \Pi_{Jet} \frac{4 Q_{Jet}}{\pi} \right)^3 }{D_{Orifice}^7 \sqrt{\Pi_{vc}^7} }

Rapid Mix Head Loss
===================

.. math::  D_{Orifice} \cong \left( \frac{4 Q \Pi_{JetRound}}{\varepsilon_{Max}^{\frac{1}{3}} \pi} \right)^{\frac{3}{7}}

.. math:: \bar v_{Jet} \cong \frac{\left( D_{Jet} \, \varepsilon_{Max} \right)^{\frac{1}{3}}}{\Pi_{JetRound}}

.. math:: h_e = \frac{ \left( D_{Jet} \, \varepsilon_{Max} \right)^{\frac{2}{3}}}{ 2g \Pi_{JetRound}^2}

.. math:: h_e = \frac{ \left( \frac{4 \Pi_{JetRound} Q \varepsilon_{Max}^2}{\pi} \right)^{\frac{2}{7}}}{2 g \Pi_{JetRound}^2}

**Off-slide**

.. math:: Q = \frac{D_{Jet}^{\frac{7}{3}} \pi \varepsilon_{Max}^{\frac{1}{3}}}{4 \Pi_{Jet}}

.. code:: python

 """ importing """
 from aide_design.play import*
 D=24 * u.inch
 V = 11 * u.mm/u.s
 Q= (V*D**2*u.pi/4).to(u.L/u.s)
 Q
 
