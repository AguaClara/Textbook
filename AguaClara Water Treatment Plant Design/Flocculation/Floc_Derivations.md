# Flocculation <br> Derivations
## Design Equations for the Flocculator
This document contains the derivation for the minimum allowable width of a flocculator channel based on the requirements that $3 < \Pi_{H_eS} < 6$ and that we maintain the $\bar G$ that serves as a basis for design. The final parameter derived is $W_{Min, \, \Pi_{H_eS}}$.

### Width
Our two restrictions are:
- Ensuring that we maintain the $\bar G$ we get based on our input parameters
- Ensuring that $3 < \frac{H_e}{S} < 6$

First, we begin by setting the two equations for energy dissipation rate, $\bar \varepsilon  = \nu \bar G^2$ and $\bar \varepsilon = \frac{g h_{L_{floc}}}{\theta}$ equal to each other to bring $\bar G$ into the equation.

$$\nu \bar G^2 = \frac{g h_{L_{floc}}}{\theta}$$

##### **Very Important Note:**
For the following steps, we will consider the flow through _**a single flow expansion $H_e$, not through the entire flocculator**_. This could be from baffle to obstacle, obstacle to baffle, obstacle to obstacle, or baffle to baffle depending on how many obstacles are in the design. This means that we are briefly redefining $\theta$ to be the time it takes for the flow to fully expand after a flow contraction. $\theta$ no longer represents the time it takes for the flow to go through the entire flocculator.

From here we make three subsequent substitutions: first $h_{L_{floc}} = K \frac{\bar v^2}{2g}$, then $\theta = \frac{H_e}{\bar v}$, and finally $\bar v = \frac{Q}{WS}$

$$\nu \bar G^2 = K \frac{\bar v^2}{2 \theta}$$

$$\nu \bar G^2 = K \frac{\bar v^3}{2 H_e}$$

$$\nu \bar G^2 = \frac{K}{2 H_e} \left( \frac{Q}{WS} \right)^3$$

Now we can solve this equation for channel width, $W$.

$$W = \frac{Q}{S}\left( \frac{K}{2 H_e \nu \bar G^2} \right)^\frac{1}{3}$$

From here, we can define $\Pi_{H_eS} = \frac{H_e}{S}$ and substitute $S = \frac{H_e}{\Pi_{H_eS}}$ into the previous equation for $W$ to get $W_{Min, \, \Pi_{H_eS}}$:

$$\color{purple}{
W_{Min, \, \Pi_{H_eS}} = \frac{\Pi_{H_eS}Q}{H_e}\left( \frac{K}{2 H_e \nu \bar G^2} \right)^\frac{1}{3}
}$$

This equation represents the absolute smallest width of a flocculator channel if we consider the lowest value of $\Pi_{H_eS}$ and the highest possible value of $H_e$:  
$H_e = H$, this implies that there are no obstacles between baffles  
$\Pi_{H_eS} = 3$
