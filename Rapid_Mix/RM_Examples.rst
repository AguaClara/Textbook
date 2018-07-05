.. _rapid_mix_examples:

***************************************************
Rapid Mix Appendix C: Examples
***************************************************

Carbonate reactions, buffering, and pH
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The coagulants used for drinking water treatment are acidic and thus result in a lowering of the pH of the treated water. The optimal pH for aluminum coagulant nanoparticle formation is between pH of 6.5 and 8.5. This is also the `pH range set by the EPA secondary standards for drinking water <https://www.epa.gov/dwstandardsregulations/secondary-drinking-water-standards-guidance-nuisance-chemicals>`__. Although many water sources are within this pH range, there are some waters with more extreme values of pH. The aluminum and iron based coagulants are also acidic and in some waters the pH may drop below the ideal range when adding the coagulant. When the pH is outside the acceptable range it is necessary to adjust the pH by adding either a base or an acid.

When acid is added to a water containing bicarbonate, :math:`HCO_3^-`, one of the potential reactions is for a proton to combine with :math:`HCO_3^-` to form carbonic acid, :math:`{H_2}CO_3`. If a base is added to water the reaction will proceed in the opposite direction. Carbonic acid, :math:`{H_2}CO_3`, is chemical indistinguishable from dissolved carbon dioxide, :math:`CO_{2_{aq}}` and the total of carbonic acid and dissolved carbon dioxide is represented as :math:`{H_2}CO_3^{\star}`. The reaction of bicarbonate to form carbonic acid removes one proton from solution and thus the concentration of protons doesn’t increase as fast as we might have first expected as acid is added to the water.

The reactions of carbonate species with protons provides pH buffering capacity that must be considered when calculating the effect of acid or base addition. Since carbonates are the dominant buffering agents in natural waters it is essential to account for their influence on pH.

Carbonic acid and Bicarbonate
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. math:: {H_2}CO_3^{\star} \overset {K_1} \longleftrightarrow {H^+} + HCO_3^-
   :label: carbonate

Where:
 | :math:`K_1` is the dissociation constant defined below.

.. math:: {K_1} = \frac{{\left[ {{H^ + }} \right]\left[ {HCO_3^ - } \right]}}{{\left[ {{H_2}CO_3^{\star} } \right]}}

Where the [ ] indicates concentration in mole/L. We will use the p function, :math:`p(x)=-log_{10}(x)`, to define the dissociation constant.

.. math:: p{K_1} = 6.3

At the point of equal concentrations of bicarbonate and carbonic acid the dissociation constant, :math:`K_1`, is equal to the hydrogen ion concentration, :math:`H^ +`. Thus we have equal concentrations at :math:`p{K_1} = pH`. This reaction is “centered” at pH = 6.3 and thus there is maximum buffering due to this reaction at pH = 6.3.

Bicarbonate and Carbonate
~~~~~~~~~~~~~~~~~~~~~~~~~

.. math:: HCO_3^ - \overset {{K_2}} \longleftrightarrow {H^ + } + CO_3^{ - 2}

.. math:: {K_2} = \frac{{\left[ {{H^ + }} \right]\left[ {CO_3^{ - 2}} \right]}}{{\left[ {HCO_3^ - } \right]}}

.. math:: p{K_2} = 10.3

Total concentration of carbonates
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The total concentration of carbonate species is given by

.. math:: {C_T} = \left[ {{H_2}CO_3^{\star} } \right] + \left[ {HCO_3^ - } \right] + \left[ {CO_3^{ - 2}} \right]

 Where: :math:`{C_T}` is the total concentration of carbonates.

The total concentration of carbonates, :math:`{C_T}`, is useful because it is conservative even though the individual species concentrations change as pH changes. ### Alpha notation The alpha notation is used to show the concentration dependence on pH and to make the equations simpler.

.. math:: \left[ {{H_2}CO_3^{\star} } \right] = {\alpha_0}{C_T}

.. math:: \left[ {HCO_3^-} \right] = {\alpha_1}{C_T}

.. math:: \left[ {CO_3^{-2}} \right] = {\alpha_2}{C_T}

Acid Neutralizing Capacity (ANC) or Alkalinity
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Acid neutralizing capacity or alkalinity is the ability of a water sample to react with and neutralize an input of acid. The units of ANC are equivalents (or protons) per liter. Bicarbonate, :math:`HCO_3^-`, can react with one proton, :math:`H^+`, and thus each mole of :math:`HCO_3^-` provides one equivalent per liter of ANC. The other terms in the equation have similar explanations.

.. math:: {\text{ANC}} = [HCO_3^ - {\text{] + 2[CO}}_3^{ - 2}{\text{] + [O}}{{\text{H}}^{\text{ - }}}{\text{] - [}}{{\text{H}}^{\text{ + }}}{\text{]}}

Note that carbonic acid and dissolved carbon dioxide are not in the ANC equation because they have no ability to neutralize protons.

We can write the ANC equation using alpha notation

.. math:: ANC = {C_T}({\alpha_1} + 2{\alpha_2}) + \frac{{{K_w}}}{{\left[ {{H^ + }} \right]}} - \left[ {{H^ + }} \right]

The alphas are each a function of the proton concentration and the dissociation constants of the carbonate reactions.

.. math:: {\alpha_{\text{0}}} = \frac{1}{{1 + \frac{{{K_1}}}{{[{H^ + }]}} + \frac{{{K_1}{K_2}}}{{{{[{H^ + }]}^2}}}}}

.. math:: {\alpha_{\text{0}}} = \frac{1}{{1 + \frac{{{K_1}}}{{[{H^ + }]}}\left( {1 + \frac{{{K_2}}}{{[{H^ + }]}}} \right)}}

.. math:: {\alpha_{\text{1}}} = \frac{1}{{\frac{{[{{\rm H}^ + }]}}{{{{\rm K}_1}}} + 1 + \frac{{{{\rm K}_2}}}{{[{{\rm H}^ + }]}}}}

.. math:: {\alpha_{\text{2}}} = \frac{1}{{\frac{{{{[{{\rm H}^ + }]}^2}}}{{{{\rm K}_1}{{\rm K}_2}}} + \frac{{[{{\rm H}^ + }]}}{{{{\rm K}_2}}} + 1}}

.. math:: {\alpha_{\text{2}}} = \frac{1}{{1 + \frac{{[{{\rm H}^ + }]}}{{{{\rm K}_2}}}\left( {1 + \frac{{[{{\rm H}^ + }]}}{{{{\rm K}_1}}}} \right)}}

For completeness we include acid neutralizing capacity for the case where the system is in equilibrium with atmospheric carbon dioxide,
:math:`CO_2`.

.. math:: ANC_{atm\,equilibrium} = \frac{{{P{C{O_2}}}{K_H}}}{{{\alpha_0}}}({\alpha_1} + 2{\alpha_2}) + \frac{{{K_w}}}{{\left[ {{H^ + }} \right]}} - \left[ {{H^ + }} \right]

pH Adjustment
-------------

In drinking water treatment plant operation it is sometimes necessary to add a base (or acid) to increase (or decrease) the pH of the raw water. The carbonate system is most important in understanding how the base will adjust the pH because the reaction between carbonic acid and bicarbonate occurs around pH 6.3, the pK for that reaction. Carbon dioxide exchange with the atmosphere is insignificant in drinking water treatment unit processes unless there is a aeration stage. Thus we can use the ANC equation for the case with no :math:`CO_2` exchange with the atmosphere.

We will evaluate the case where we add a base that will increase the ANC of the raw water and it might also increase the total carbonate concentration. Our goal is to calculate how much of that base to add to reach a target pH. The final ANC after base addition is given by
.. math:: ANC_1 = ANC_0 + \Pi_{ANC}C_B

| where:
| :math:`ANC_1` is the final acid neutralizing capacity of the mixture after the base is added.
| :math:`C_B` is concentration of base in mole/liter  :math:`\Pi_{ANC}` is ANC per mole of base

The final carbonate concentration is given by

.. math:: C_{T_1} ={C_{T_0}}+ \Pi_{CO_3^{-2}}C_B

| where:
| :math:`C_{T_1}` is the final total carbonate concentration of the mixture after the base is added.
| :math:`\Pi_{CO_3^{-2}}` is mole of carbonate per mole of base (0 for :math:`NaOH` and 1 for :math:`Na_2CO_3`)

Substituting these values into the ANC equation we obtain

.. math:: ANC_0 + \Pi_{ANC}C_B = ({C_{T_0}}+ \Pi_{CO_3^{-2}}C_B)({\alpha_1} + 2{\alpha_2}) +  \frac{{{K_w}}}{{\left[ {{H^ + }} \right]}} - \left[ {{H^ + }} \right]

Now we solve for :math:`C_B`, the concentration of base that must be added to reach a target pH.

.. math::  (\Pi_{ANC} -\Pi_{CO_3^{-2}}({\alpha_1} + 2{\alpha_2}) )C_B= {C_{T_0}}({\alpha_1} + 2{\alpha_2}) +  \frac{{{K_w}}}{{\left[ {{H^ + }} \right]}} - \left[ {{H^ + }} \right] - ANC_0

.. math::  C_B= \frac{{C_{T_0}}({\alpha_1} + 2{\alpha_2}) +  \frac{{{K_w}}}{{\left[ {{H^ + }} \right]}} - \left[ {{H^ + }} \right] - ANC_0}{\Pi_{ANC} -\Pi_{CO_3^{-2}}({\alpha_1} + 2{\alpha_2})}

Note that the equations above can also be used for the case where acid is added to reduce the pH. In that case :math:`\Pi_{ANC}` will have a negative value.

Example: Find the required dose of several bases to raise the pH at the Manzaragua Water Treatment Plant
========================================================================================================

The Mazaragua AguaClara plant consists of two 1 L/s plants operating in parallel. The plant is located in the municipality of Guinope, the department of El Paraiso, Honduras.

  .. _Manzaragua_WTP:
  .. figure::    Images/Manzaragua_WTP.jpg
      :width: 700px
      :align: center
      :alt: Manzaragua WTP

      Manzaragua water treatment plant using two of the AguaClara 1 L/s plants in parallel.

The plant performed very poorly from the first day of operation. The first attempted fix was to double the flocculator residence time by increasing the number of flocculator pipes (3 inch diameter by 1.5 m long) from 12 to 24. This improved performance, but the plant continued to perform poorly. A raw water sample was analyzed on May 30, 2018 and the following results were obtained.

  .. _Manzaragua_Water_Analysis:
  .. figure::    Images/Manzaragua_Water_Analysis.jpg
      :width: 700px
      :align: center
      :alt: Manzaragua Water Analysis

      Water quality analysis for Manzaragua.

Table 1. Manzaragua water quality analysis
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------+--------------------------------+-----------+---------+
| Parameter    | Units                          | Standard  | Results |
+==============+================================+===========+=========+
| Turbidity    | NTU                            | 5         | 71      |
+--------------+--------------------------------+-----------+---------+
| Color        | color units                    | 15        | 150     |
+--------------+--------------------------------+-----------+---------+
| pH           | pH                             | 6.5 - 8.5 | 5.91    |
+--------------+--------------------------------+-----------+---------+
| Conductivity | :math:`\mu s/cm`               | 400       | 69.15   |
+--------------+--------------------------------+-----------+---------+
| Alkalinity   | :math:`mg/L` as :math:`CaCO_3` | -         | 24.5    |
+--------------+--------------------------------+-----------+---------+
| Bicarbonates | :math:`mg/L` as :math:`CaCO_3` | -         | 24.5    |
+--------------+--------------------------------+-----------+---------+
| Carbonates   | :math:`mg/L` as :math:`CaCO_3` | -         | 0       |
+--------------+--------------------------------+-----------+---------+
| Hardness     | :math:`mg/L` as :math:`CaCO_3` | 400       | 15.68   |
+--------------+--------------------------------+-----------+---------+

This water has high color which suggests a high concentration of dissolved organic matter. The pH is a clear problem because the pH is too low for the coagulant nanoparticles to precipitate. As the water sample pH of 5.91 a significant fraction of the coagulant will remain soluble.

Our goal is to determine how much base will need to be added to raise the pH. We do not have data on the *optimal* pH for treating high color water with PACl and so we will use pH 7 as the target. We will need a separate calculation to estimate how much additional :math:`Na_2CO_3` will need to be added to balance the PACl acidity.

At circumneutral pH (pH close to 7) the buffering capacity of the water is dominated by carbonate chemistry and specifically by the equilibrium between :math:`{H_2}CO_3^{\star}` and $HCO_3^- $. We will use the acid neutralizing capacity (reported as calcium carbonate alkalinity) and the pH from the sample analysis to estimate the total concentration of carbonates. We will not use the sample analysis carbonate concentrations because they can not be precisely correct.

The solution steps are as follows: 1) Find total carbonate concentration, :math:`C_{T_0}`, of the raw water sample using the ANC equation for the case where the system is not exchanging :math:`CO_2` with the atmosphere. 1) Solve for the required concentration of base, :math:`C_B`.

For step 1 we need to solve the ANC equation for the carbonate concentration.

.. math::  C_{T_0} = \frac{ANC_0  - \frac{{{K_w}}}{{\left[ {{H^ + }} \right]}} + \left[ {{H^ + }} \right]}{\alpha_1 + 2\alpha_2}

.. todo:: We eventually should add the effect of the coagulant to this analysis so the required base concentration can be calculated given the raw water alkalinity, raw water pH, and coagulant dose.

Table 2. ANC and carbonate values for several bases and acids.

+-----------------------+-----------------------+-----------------------+
| Base/Acid             | :math:`\Pi_{ANC}`     | :math:`\Pi_{CO_3^{-2} |
|                       |                       | }`                    |
+=======================+=======================+=======================+
| :math:`Na_2CO_3` or   | 2                     | 1                     |
| :math:`CaCO_3`        |                       |                       |
+-----------------------+-----------------------+-----------------------+
| :math:`NaHCO_3`       | 1                     | 1                     |
+-----------------------+-----------------------+-----------------------+
| :math:`NaOH`          | 1                     | 0                     |
+-----------------------+-----------------------+-----------------------+
| :math:`HCl` or        | -1                    | 0                     |
| :math:`HNO_3`         |                       |                       |
+-----------------------+-----------------------+-----------------------+
| :math:`H_2SO_4`       | -2                    | 0                     |
+-----------------------+-----------------------+-----------------------+

For :math:`Na_2CO_3` \* :math:`\Pi_{ANC}` = 2 because we are adding
:math:`CO_3^{-2}` which is multiplied by two in the ANC equation because
:math:`CO_3^{-2}` can react with two protons. \* :math:`\Pi_{CO_3^{-2}}`
= 1 because there is one mole of :math:`CO_3` per mole of
:math:`Na_2CO_3`

Below is the code used to calculate the required base addition.

.. todo:: This code needs to move to aguaclara_research. Then the short code snippits can be doc tested.

.. code:: python

    from aide_design.play import*
    from aguaclara_research.play import*
    import aguaclara_research.Environmental_Processes_Analysis as epa

    """define molecular weights"""
    m_Ca = 40.078*u.g/u.mol
    m_C = 12.011*u.g/u.mol
    m_O = 15.999*u.g/u.mol
    m_Na = 22.99*u.g/u.mol
    m_H = 1.008*u.g/u.mol
    m_CaCO3 = m_Ca+m_C+3*m_O
    m_Na2CO3 = 2*m_Na+m_C+3*m_O
    m_NaHCO3 = m_Na+m_H+m_C+3*m_O
    m_NaOH = m_Na+m_O+m_H

    """Raw water characteristics"""
    pH_0 = 5.91
    ANC_0 = (24.5 * u.mg/u.L/m_CaCO3).to(u.mmol/u.L)
    ANC_0

    def total_carbonates_closed(pH, ANC):
        """This function calculates total carbonates for a closed system given pH and ANC

        Parameters
        ----------
        pH : float
            pH of the sample
        ANC: float
            acid neutralizing capacity of the sample
        Returns
        -------
        The total carbonates of the sample
        Examples
        --------
        >>> total_carbonates_closed(1*u.mmol/u.L,8)
        1.017 mole/liter
        """
        return (ANC - epa.Kw/epa.invpH(pH) + epa.invpH(pH)) / (epa.alpha1_carbonate(pH) + 2 * epa.alpha2_carbonate(pH))


    CT_0 = total_carbonates_closed(pH_0,ANC_0)


    """ calculate the amount of base that must be added to reach a target pH"""
    def pH_adjust(pH_0,ANC_0,Pi_ANC,Pi_CO3,pH_target):
      """This function calculates the required base (or acid) to adjust the pH to a target value. The buffering capacity is assumed to be completely due to carbonate species. The initial carbonate concentration is calculated based on the initial pH and the initial ANC.

      Parameters
      ----------
      pH_0: float
          pH of the sample
      ANC_0: float
          acid neutralizing capacity (Alkalinity) of the sample in eq/L.
      Pi_ANC: float
        equivalents of ANC per mole of base (or acid)
      Pi_CO3: float
        mole of carbonate per mole of base (or acid)
      pH_target: float
        pH goal
      Returns
      -------
      The required concentration of base (or acid) in millimoles/L
      Examples
      --------
      >>> pH_adjust(5.91,0.2*u.mmol/u.L,1,1,7)
      2.2892822041250924 millimole/liter
      """
      CT_0 = total_carbonates_closed(pH_0,ANC_0)
      B_num = CT_0 * (epa.alpha1_carbonate(pH_target) + 2 * epa.alpha2_carbonate(pH_target)) + epa.Kw/epa.invpH(pH_target) - epa.invpH(pH_target) - ANC_0
      B_den = Pi_ANC - Pi_CO3*(epa.alpha1_carbonate(pH_target) + 2 * epa.alpha2_carbonate(pH_target))
      return (B_num/B_den).to(u.mmol/u.L)

    """target pH"""
    pH_target = 7

    Pi_ANC_Na2CO3 = 2
    Pi_CO3_Na2CO3 = 1

    Pi_ANC_NaHCO3 = 1
    Pi_CO3_NaHCO3 = 1

    Pi_ANC_NaOH = 1
    Pi_CO3_NaOH = 0

    C_Na2CO3 = pH_adjust(pH_0,ANC_0,Pi_ANC_Na2CO3,Pi_CO3_Na2CO3,pH_target)

    C_NaHCO3 = pH_adjust(pH_0,ANC_0,Pi_ANC_NaHCO3,Pi_CO3_NaHCO3,pH_target)
    C_NaOH = pH_adjust(pH_0,ANC_0,Pi_ANC_NaOH,Pi_CO3_NaOH,pH_target)

    """Display results in a pandas table"""
    base = ["NaOH","NaHCO3","Na2CO3"]
    myindex = ["[mmoles/L]","[mg/L]"]
    row1 = [C_Na2CO3.magnitude,C_NaHCO3.magnitude,C_NaOH.magnitude]
    row2 = [(C_Na2CO3*m_Na2CO3).to(u.mg/u.L).magnitude,(C_NaHCO3*m_NaHCO3).to(u.mg/u.L).magnitude,(C_NaOH*m_NaOH).to(u.mg/u.L).magnitude]
    df = pd.DataFrame([row1,row2],index=myindex,columns=base)
    print(df.round(2))

    """Graph the base concentration required as a function of the target pH"""
    pH_graph = np.linspace(6,7,50)
    C_Na2CO3 = pH_adjust(pH_0,ANC_0,Pi_ANC_Na2CO3,Pi_CO3_Na2CO3,pH_graph)
    C_NaHCO3 = pH_adjust(pH_0,ANC_0,Pi_ANC_NaHCO3,Pi_CO3_NaHCO3,pH_graph)
    C_NaOH = pH_adjust(pH_0,ANC_0,Pi_ANC_NaOH,Pi_CO3_NaOH,pH_graph)

    fig, ax = plt.subplots()

    ax.plot(pH_graph,C_NaHCO3)
    ax.plot(pH_graph,C_Na2CO3)
    ax.plot(pH_graph,C_NaOH)
    imagepath = 'Rapid_Mix/Images/'
    ax.set(xlabel='pH target', ylabel='Base concentration (mmole/L)')
    ax.legend(["sodium bicarbonate","sodium carbonate","sodium hydroxide"])
    fig.savefig(imagepath+'mole_base_for_target_pH')
    plt.show()

    fig, ax = plt.subplots()
    ax.plot(pH_graph,(C_Na2CO3*m_Na2CO3).to(u.mg/u.L))
    ax.plot(pH_graph,(C_NaOH*m_NaOH).to(u.mg/u.L))
    ax.set(xlabel='pH target', ylabel='Base concentration (mg/L)')
    ax.legend(["sodium carbonate","sodium hydroxide"])
    fig.savefig(imagepath+'mg_base_for_target_pH')
    plt.show()

The analysis reveals that the choice of base matters. The most efficient (on a mass or mole basis) base is :math:`NaOH` because it doesn't add any carbonates that don't fully react with the hydrogen ions. The decision about which base to use will be influenced by economics, operator safety, and by whether additional carbonate buffering simplifies plant operation with changing raw water quality.



  .. _Calcium bases:
  .. csv-table:: Calcium base.
     :header:  "Chemical name",   "common name",  "Chemcal formula"
     :widths: 20, 20, 20

     "calcium carbonate","limestone or chalk",":math:`CaCO_3`"
     "calcium hydroxide","slaked lime or hydrated lime",":math:`Ca(OH)_2`"
     "calcium oxide","quicklime",":math:`CaO`"

The calcium bases are relatively inexpensive and have the disadvantage of lower solubility than sodium bases. Calcium carbonate has a low solubility, carbon dioxide is present in the atmosphere, and thus calcium carbonate precipitation limits the concentration that can be used for chemical feeds.

    .. _mole_base_for_target_pH:
    .. figure::    Images/mole_base_for_target_pH.png
        :width: 700px
        :align: center
        :alt: mole base for target pH

        Dose of three bases (in mole/L) required to achieve a target pH for the Manzaragua water. Carbonates provide more buffering and less change in the pH compared with :math:`NaOH`.

    .. _mg_base_for_target_pH:
    .. figure::    Images/mg_base_for_target_pH.png
        :width: 700px
        :align: center
        :alt: mg base for target pH

        Dose of two bases (in mg/L) required to achieve a target pH for the Manzaragua water. Carbonates provide more buffering and less change in the pH compared with :math:`NaOH`.

The required dose for each of the bases is summarized below.
   .. _Base_table:
   .. csv-table:: Dose of each base required to change the pH of the Manzaragua water to 7.
      :header:  "units",   ":math:`NaOH`",  ":math:`NaHCO_3`",  ":math:`Na_2CO_3`"
      :widths: 20, 20, 20, 20

      "[mmoles/L]",  "0.45",     "2.8",    "0.53"
      "[mg/L]",     "47.21",   "235.0",   "21.19"
