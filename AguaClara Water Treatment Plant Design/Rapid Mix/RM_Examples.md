# Appendix C: Examples



### Carbonate reactions, buffering, and pH
The coagulants used for drinking water treatment are acidic and thus result in a lowering of the pH of the treated water. The optimal pH for aluminum coagulant nanoparticle formation is <font color="red">between pH of 6.5 and 8.5</font>. This is also the [pH range set by the EPA secondary standards for drinking water](https://www.epa.gov/dwstandardsregulations/secondary-drinking-water-standards-guidance-nuisance-chemicals). Although many water sources are within this pH range, there are some waters with more extreme values of pH. The aluminum and iron based coagulants are also acidic and in some waters the pH may drop below the ideal range when adding the coagulant. When the pH is outside the acceptable range it is necessary to adjust the pH by adding either a base or an acid.

When acid is added to a water containing bicarbonate, $HCO_3^-$, one of the potential reactions is for a proton to combine with $HCO_3^-$ to form carbonic acid, ${H_2}CO_3$. If a base is added to water the reaction will proceed in the opposite direction. Carbonic acid, ${H_2}CO_3$, is chemical indistinguishable from dissolved carbon dioxide, $CO_{2_{aq}}$ and the total of carbonic acid and dissolved carbon dioxide is represented as ${H_2}CO_3^{\star}$. The reaction of bicarbonate to form carbonic acid removes one proton from solution and thus the concentration of protons doesn't increase as fast as we might have first expected as acid is added to the water.

The reactions of carbonate species with protons provides pH buffering capacity that must be considered when calculating the effect of acid or base addition. Since carbonates are the dominant buffering agents in natural waters it is essential to account for their influence on pH.

### Carbonic acid and Bicarbonate
$${H_2}CO_3^{\star} \overset {K_1} \longleftrightarrow {H^+} + HCO_3^- $$
Where:
$K_1$ is the dissociation constant
$${K_1} = \frac{{\left[ {{H^ + }} \right]\left[ {HCO_3^ - } \right]}}{{\left[ {{H_2}CO_3^{\star} } \right]}}$$

$$p{K_1} = 6.3$$

The

### Bicarbonate and Carbonate
$$HCO_3^ - \overset {{K_2}} \longleftrightarrow {H^ + } + CO_3^{ - 2}$$

$${K_2} = \frac{{\left[ {{H^ + }} \right]\left[ {CO_3^{ - 2}} \right]}}{{\left[ {HCO_3^ - } \right]}}$$

$$p{K_2} = 10.3$$

### Total concentration of carbonates

$${C_T} = \left[ {{H_2}CO_3^{\star} } \right] + \left[ {HCO_3^ - } \right] + \left[ {CO_3^{ - 2}} \right]$$

### Alpha notation

$$\left[ {{H_2}CO_3^{\star} } \right] = {\alpha_0}{C_T}$$

$$\left[ {HCO_3^ - } \right] = {\alpha_1}{C_T}$$

$$\left[ {CO_3^{ - 2}} \right] = {\alpha_2}{C_T}$$

Acid Neutralizing Capacity (ANC) $${\text{ANC}} = [HCO_3^ - {\text{] + 2[CO}}_3^{ - 2}{\text{] + [O}}{{\text{H}}^{\text{ - }}}{\text{] - [}}{{\text{H}}^{\text{ + }}}{\text{]}}$$ ANC in alpha notation $$ANC = {C_T}({\alpha_1} + 2{\alpha_2}) + \frac{{{K_w}}}{{\left[ {{H^ + }} \right]}} - \left[ {{H^ + }} \right]$$

Alpha equations for the carbonate system
$${\alpha_{\text{0}}} = \frac{1}{{1 + \frac{{{K_1}}}{{[{H^ + }]}} + \frac{{{K_1}{K_2}}}{{{{[{H^ + }]}^2}}}}}$$

$${\alpha_{\text{0}}} = \frac{1}{{1 + \frac{{{K_1}}}{{[{H^ + }]}}\left( {1 + \frac{{{K_2}}}{{[{H^ + }]}}} \right)}}$$

$${\alpha_{\text{1}}} = \frac{1}{{\frac{{[{{\rm H}^ + }]}}{{{{\rm K}_1}}} + 1 + \frac{{{{\rm K}_2}}}{{[{{\rm H}^ + }]}}}}$$

$${\alpha_{\text{2}}} = \frac{1}{{\frac{{{{[{{\rm H}^ + }]}^2}}}{{{{\rm K}_1}{{\rm K}_2}}} + \frac{{[{{\rm H}^ + }]}}{{{{\rm K}_2}}} + 1}}$$

$${\alpha_{\text{2}}} = \frac{1}{{1 + \frac{{[{{\rm H}^ + }]}}{{{{\rm K}_2}}}\left( {1 + \frac{{[{{\rm H}^ + }]}}{{{{\rm K}_1}}}} \right)}}$$

Acid neutralizing capacity for the case where the system is not exchanging $CO_2$ with the atmosphere

$$ANC = {C_T}({\alpha_1} + 2{\alpha_2}) + \frac{{{K_w}}}{{\left[ {{H^ + }} \right]}} - \left[ {{H^ + }} \right]$$

Acid neutralizing capacity for the case where the system is in equilibrium with atmospheric $CO_2$

$$ANC = \frac{{{P{C{O_2}}}{K_H}}}{{{\alpha_0}}}({\alpha_1} + 2{\alpha_2}) + \frac{{{K_w}}}{{\left[ {{H^ + }} \right]}} - \left[ {{H^ + }} \right]$$

In drinking water treatment operation it is sometimes necessary to add a base to increase the pH of the raw water. The carbonate system is most important in understanding how the base will adjust the pH because the reaction between carbonic acid and bicarbonate occurs around pH 6.3, the pK for that reaction. Exchange with the atmosphere is insignificant in drinking water treatment unit processes unless there is a aeration stage. Thus we can use the ANC equation for the case with no $CO_2$ exchange with the atmosphere.

We will add a base that will increase the ANC of the raw water and it might also increase the total carbonate concentration. Our goal is to calculate how much of that base to add to reach a target pH.

Where
* $B$ is concentration of base in mole/liter
* $\Pi_{ANC}$ is ANC per mole of base
* $\Pi_{CO_3^{-2}}$ is mole of carbonate per mole of base



$$ANC_0 + \Pi_{ANC}B = ({C_{T_0}}+ \Pi_{CO_3^{-2}}B)({\alpha_1} + 2{\alpha_2}) +  \frac{{{K_w}}}{{\left[ {{H^ + }} \right]}} - \left[ {{H^ + }} \right]$$

Now we solve for $B$, the concentration of base that must be added to reach a target pH.

$$ (\Pi_{ANC} -\Pi_{CO_3^{-2}}({\alpha_1} + 2{\alpha_2}) )B= {C_{T_0}}({\alpha_1} + 2{\alpha_2}) +  \frac{{{K_w}}}{{\left[ {{H^ + }} \right]}} - \left[ {{H^ + }} \right] - ANC_0$$

$$ B= \frac{{C_{T_0}}({\alpha_1} + 2{\alpha_2}) +  \frac{{{K_w}}}{{\left[ {{H^ + }} \right]}} - \left[ {{H^ + }} \right] - ANC_0}{\Pi_{ANC} -\Pi_{CO_3^{-2}}({\alpha_1} + 2{\alpha_2})}$$

# Solution steps to find the required $Na_2CO_3$ dose
We will use the acid neutralizing capacity (reported as calcium carbonate alkalinity) and the pH from the sample analysis to estimate the total concentration of carbonates. We will not use the sample analysis carbonate concentrations because they can not be correct given that the pH is not equal to 7.

For $Na_2CO_3$
* $\Pi_{ANC}$ = 2 because we are adding $CO_3^{-2}$ which is multiplied by two in the ANC equation
* $\Pi_{CO_3^{-2}}$ = 1 because there is one mole of $CO_3$ per mole of $Na_2CO_3$

##Manzaragua Water Treatment Plant
The Mazaragua AguaClara plant consists of two 1 L/s plants operating in parallel. The plant is located in the municipality of Guinope, the department of El Paraiso, Honduras.

The plant performed very poorly from the first day of operation. The first attempted fix was to double the flocculator residence time by increasing the number of flocculator pipes (3 inch diameter by 1.5 m long) from 12 to 24. This improved performance, but the plant continued to perform poorly. A raw water sample was analyzed on May 30, 2018 and the following results were obtained.

<center><img src="https://raw.githubusercontent.com/AguaClara/CEE4540_Master/master/AguaClara%20Water%20Treatment%20Plant%20Design/Rapid%20Mix/Images/Manzaragua_Water_Analysis.jpg" width=600></center>


### Table 1. Water quality analysis
| Parameter | Units | Standard | Results |
| - | - | :-: | :-: |
| Turbidity | NTU | 5 | 71 |
| Color | color units | 15 | 150 |
| pH | pH | 6.5 - 8.5 | 5.91 |
| Conductivity | $\mu s/cm$ | 400 | 69.15 |
| Alkalinity | $mg/L$ as $CaCO_3$ | - | 24.5 |
| Bicarbonates | $mg/L$ as $CaCO_3$ | - | 24.5 |
| Carbonates | $mg/L$ as $CaCO_3$ | - | 0 |
| Hardness | $mg/L$ as $CaCO_3$ | 400 | 15.68 |

This water has high color which suggests a high concentration of dissolved organic matter. The pH is a clear problem because the pH is too low for the coagulant nanoparticles to precipitate. As this pH a significant fraction of the coagulant will remain soluble.

Our goal is to determine how much $Na_2CO_3$ will need to be added to raise the pH. <font color="red">We do not have data on the optimal pH for treating high color water with PACl and so we will use pH 7 as the target. </font> We will need a separate calculation to estimate how much additional $Na_2CO_3$ will need to be added to balance the PACl acidity.

At circumneutral pH (pH close to 7) the buffering capacity of the water is dominated by carbonate chemistry and specifically by the equilibrium between ${H_2}CO_3^{\star}$ and $HCO_3^- $. From the water analysis the total concentration of carbonates is 24.5 mg/L as $CaCO_3$.


Equations describing carbonate chemistry are given below.


The solution steps are as follows:
1) Find total carbonate concentration, $C_{T_0}$, of the raw water sample using the ANC equation for the case where the system is not exchanging $CO_2$ with the atmosphere.
1) Solve for the required concentration of base, $B$.


For step 1 we need to solve the ANC equation for the carbonate concentration.

$$ C_{T_0} = \frac{ANC_0  - \frac{{{K_w}}}{{\left[ {{H^ + }} \right]}} + \left[ {{H^ + }} \right]}{\alpha_1 + 2\alpha_2}  $$

We eventually should add the effect of the coagulant to this analysis so the required base concentration can be calculated given the raw water alkalinity, raw water pH, and coagulant dose.

```Python
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
def Base_adjust(pH_0,ANC_0,Pi_ANC,Pi_CO3,pH_target):
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

C_Na2CO3 = Base_adjust(pH_0,ANC_0,Pi_ANC_Na2CO3,Pi_CO3_Na2CO3,pH_target)
C_Na2CO3
(C_Na2CO3 * m_Na2CO3).to(u.mg/u.L)
C_NaHCO3 = Base_adjust(pH_0,ANC_0,Pi_ANC_NaHCO3,Pi_CO3_NaHCO3,pH_target)
C_NaHCO3
(C_NaHCO3 * m_NaHCO3).to(u.mg/u.L)
C_NaOH = Base_adjust(pH_0,ANC_0,Pi_ANC_NaOH,Pi_CO3_NaOH,pH_target)
C_NaOH
(C_NaOH * m_NaOH).to(u.mg/u.L)


pH_graph = np.linspace(6,7,50)
C_Na2CO3 = Base_adjust(pH_0,ANC_0,Pi_ANC_Na2CO3,Pi_CO3_Na2CO3,pH_graph)
C_NaHCO3 = Base_adjust(pH_0,ANC_0,Pi_ANC_NaHCO3,Pi_CO3_NaHCO3,pH_graph)
C_NaOH = Base_adjust(pH_0,ANC_0,Pi_ANC_NaOH,Pi_CO3_NaOH,pH_graph)

fig, ax = plt.subplots()

ax.plot(pH_graph,C_NaHCO3)
ax.plot(pH_graph,C_Na2CO3)
ax.plot(pH_graph,C_NaOH)
imagepath = 'AguaClara Water Treatment Plant Design/Rapid Mix/Images/'
ax.set(xlabel='pH target', ylabel='Base concentration (mmole/L)')
ax.legend(["sodium bicarbonate","sodium carbonate","sodium hydroxide"])
fig.savefig(imagepath+'mole_base_for_target_pH')
plt.show()
fig, ax = plt.subplots()

ax.plot(pH_graph,(C_Na2CO3*m_Na2CO3).to(u.mg/u.L))
ax.plot(pH_graph,(C_NaOH*m_NaOH).to(u.mg/u.L))

imagepath = 'AguaClara Water Treatment Plant Design/Rapid Mix/Images/'
ax.set(xlabel='pH target', ylabel='Base concentration (mg/L)')
ax.legend(["sodium carbonate","sodium hydroxide"])
fig.savefig(imagepath+'mg_base_for_target_pH')
plt.show()
```
