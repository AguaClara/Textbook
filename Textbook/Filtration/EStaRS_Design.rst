.. raw:: html

    <embed>
       <link rel="canonical" href="https://aguaclara.github.io/Textbook/Filtration/EStaRS_Design.html" />
       <script src="https://hypothes.is/embed.js" async></script>
    </embed>

.. _title_estars:

*****************************************
Enclosed Stacked Rapid Sand Filter Design
*****************************************



The Enclosed Stacked Rapid Sand filter, EStaRS, is a compact filter built inside a pipe. Open Stacked Rapid Sand, OStaRS, construction methods require that a person be able to work inside the filter to finish the waterproofing of the concrete walls and to install the pipe modules for the inlets and outlets. The minimum filter area for OStaRS is approximately 1 square meter. Given a backwash velocity of 11 mm/s that corresponds to a minimum flow of about 11 L/s. It is always best to have at least 2 filters operating in parallel so that the filters can be backwashed when the plant is operating at less than 50% of the design flow rate. Thus EStaRS filters will be used for plants with flows less than about 20 L/s.

* Use standard caps on the top and bottom of the filter body.
* Use clamp on fittings to split the filter body at two places between layers.
* Use clamp on fittings on trunks to enable removal.
* Use trunks that are 2" ND so that the molded ends of the branches have something to prevent them from rotating.
* Join branches across trunk with an upper and lower strap that is clamped in place with hose clamps.
* use band clamps on inside of filter to connect trunks
* weld a pipe stub to pass through the filter body for the trunks

The EStaRS filters should be modular with one pipe connection to attach to the settled water source and another pipe connection to attach to the finished water. The flow division between filters could be an LFOM for each filter in the inlet tank. To make a filter modular the inlet and outlet tanks need to be integrated into the filter module.

The inlet and outlet tanks could be separate or connected and they could be rectangular PVC tanks or PVC pipes.

Previous problems with EStaRS filters included air entrainment and fabrication problems with the filter internal piping. Corrugated pipes that are available for filter body diameters greater than 60 centimeters that are available in Honduras have very thin inner walls that are not thick enough for strong welds. This requires use of a gasket seal for passing the trunk lines through the filter body. The corrugated pipes are also more difficult to attach the required end caps on the filter body. For these reasons we do not recommend using corrugated pipes for the filter body. Smooth walled PVC pipe is available in sizes up to 60 cm in diameter (ND = 24") and is the material of choice for the filter body.

Air entrainment may be a problem in the inlet pipes. If air is carried into the filter the head loss through the filter will increase rapidly. Byron Zuniga reports that he was unable to get an effective backwash at the San Juan Guarita plant based on the observation that the head loss increased rapidly after backwash even though there was no evidence of turbidity release during backwash. This observation is consistent with air being entrained in the inlet pipes and carried into the filter where it rapidly fills the pores of the sand and thus prevents water from flowing through those pores.

The solution to air entrainment is to design the inlet pipes to act like tube settlers so that the air can return to the inlet tank.

We need a method to measure the flow rate entering the filters. The slot weir in the OStaRS filter could be used to measure the flow and would have a nonlinear scale. An alternative that the operators would readily understand would be to replace the slot weir with an LFOM.

The 4 EStaRS that are in operation in Central America as of 2021 have winged pipes with orifices for the inlets. There are no reports of problems with sand entering the inlet pipes and thus that appears to be a success. This does require the use of a gate valve for the backwash pipe to ensure that the transition from backwash to filtration mode doesn't happen too quickly. During this transition there is reverse flow from the filter into the inlet pipes and if that flow rate is too high it could carry sand into the inlet branches.

Air venting from trunks
=======================

The trunks are initially filled with air.
The trunks must have a water seal that is as low as the siphon water seal (is this the constraint?) to ensure that air is never sucked into the filter during backwash.
The trunk entry into the filter body is thus at a local high point and air that accumulates in the top of the trunk and the top of the branches has no way to get out.
There must be a vent on the top of the trunks where they enter the filter body.

Vent options
------------

1) tube straight up to top of inlet tank (will suck air during backwash)
1) tube that connects into the top of the filter body (during filtration air will travel up the tubes and vent into the top of the filter body. During backwash water will take this shortcut to bypass the sand. It could work if the tubes are small enough that the bypass during backwash is small)
1) Use sloped section of trunk line to act as tube settler to remove bubbles that are entrained in the inlet. This doesn't solve the problem of air that is in the local high spot of trunks.

It seems that the only option is to connect the air release tubes to the top of the filter.

Elevation considerations
========================

The head loss through the sand during backwash is equal to the settled depth of sand. This means that the water level in the top inlet pipe will drop by an amount equal to the depth of the sand. That means that the bottom of the inlet tank must be ABOVE the top of the sand + the OD of the trunk + head loss in the backwash trunk inlet.

Rectangular tank option
=======================

As of 2024 the best option for fabricating EStaRS filters seems to be from HDPE sheets welded together to create rectangular tanks. The rectangular tank option eliminates the challenges of providing support to the branches in the round EStaRS

Structural Analysis of Rectangular tank 


Equation for deflection of simple beam with uniform loading with sliding support. This will be a conservative analysis because the ends of the PVC sheet continue across the next support and thus there is an additional constraint at the support points. The PVC is not able to rotate at the support points. 
[equation source](https://ocw.nthu.edu.tw/ocw/upload/8/258/Chapter_9-98.pdf)

$$\delta = \frac{5qL^4}{384EI}$$

E is the modulus of elasticity, Young's modulus or the tensile modulus and is the material's stiffness

For a rectangle
$$I_x = \frac{b h^3}{12}$$
where b is the width of the rectangle and h is the height. h is thus the thickness, t, of the PVC.

Pressure is force per area or force per length per width
$$ P = \frac{F}{A} = \frac{q}{b}$$

Now combine the previous 3 equations to get deflection, $\delta$ as a function of the pressure and substitute t for h.

$$\delta = \frac{5PbL^4}{384E}\frac{12}{b t^3}$$

As expected b cancels out

$$\delta = \frac{5P L^4}{32E h^3}$$

Pressure is a function of depth
$$ P = \rho g \bar h_w$$

Substituting into the deflection equation we obtain

$$\delta = \frac{5 \rho g \bar h_w L^4}{32E t^3}$$

Solve for the allowed span between supports, W.

$$W = \left(\frac{32E t^3\delta}{5 \rho g \bar h_w }\right)^{1/4} $$

We need an equation that calculates the elevation of the next horizontal support, $h_{w_{i+1}}$ given the elevation of a horizontal support, $h_{w_i}$ and the angle of the wall relative to the horizontal, $\theta$.

$$ \bar h_w = \frac{h_{w_i} + h_{w_{i+1}}}{2}$$

$$ W = \frac{h_{w_{i+1}} - h_{w_i}}{sin(\theta)}$$

We will use a system of 3 equations and iteration to solve at each step. First assume that $h_{w_{i+1}}$ = $h_{w_i}$, solve for W, then calculate a new $h_{w_{i+1}}$ and repeat.

Rearrange previous equation to get $h_{w_{i+1}}$ as a function of W.

$$ h_{w_{i+1}} = W sin(\theta) + h_{w_i} $$
