.. _title_Adsorption_Introduction:

**************************
Adsorption Introduction
**************************


Removal of a dissolved contaminant by adsorption is one of our best available options for removing many dissolved contaminants.

Granular Activated Carbon (GAC)
===============================

GAC can be placed in a column and designed as a porous media filtration system. The removal mechanism, adsorption, is very different from filtration of flocs and there is no need to backwash the bed of GAC since it is removed dissolved species rather than suspended solids. GAC columns can be configured with 2 or more columns in series so that a first column in the series can be fully loaded with the contaminant before taking it off line for replacement of the GAC. The new GAC column is then plumbed so that it is the last column in the series.

Powdered Activated Carbon (PAC)
===============================

PAC

The equation for PAC capacity is from https://doi.org/10.1021/es970833y.

.. math::

  C_{1,0}-q_{1} C_{\mathrm{c}}-\frac{q_{1}}{q_{1}+q_{2}}\left(\frac{n_{1} q_{1}+n_{2} q_{2}}{n_{1} K_{1}}\right)^{n_{1}}=0

.. math::

  C_{2,0}-q_{2} C_{\mathrm{c}}-\frac{q_{2}}{q_{1}+q_{2}}\left(\frac{n_{1} q_{1}+n_{2} q_{2}}{n_{2} K_{2}}\right)^{n_{2}}=0

Where
 - :math:`q_{i}` is the equilibrium solid-phase concentration of adsorbate i (μmol/g)
 - :math:`C_{i,0}` the initial concentration of adsorbate i (μmol/L)
 - :math:`C_c` is the PAC dose (g/L),
 - :math:`K_i` and :math:`1/n_i` are the single-solute Freundlich isotherm constants for adsorbate i.

.. math::

  q_{1}=\frac{C_{1,0}}{C_{\mathrm{c}}+\frac{1}{q_{2}}\left(\frac{n_{2} q_{2}}{n_{1} K_{1}}\right)^{n_{1}}}

This approach makes it possible to model adsorption of a trace organic by accounting for the effect of a single equivalent background compound (EBC). This model should make it possible to estimate the mass of PAC required per liter of water given characteristics of the EBC and the target contaminant.


References
==========

Environ. Sci. Technol.199832111694-1698
Publication Date:April 24, 1998
https://doi.org/10.1021/es970833y

Atrazine removal by powdered activated carbon in floc blanket reactors Carlos Campos(M) Vernon L Snoeyink Benito Mariñas(M) I Baudin1 J.M Lainé
https://doi.org/10.1016/S0043-1354(00)00169-X
