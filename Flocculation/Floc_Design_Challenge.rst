.. _title_Flocculation_Design_Challenge:

*****************************
Flocculation Design Challenge
*****************************

The largest AguaClara hydraulic flocculator has a maximum flow rate of 60 L/s and uses the Horizontal-Vertical geometry. For flows greater than 100 L/s the Horizontal-Horizontal geometry becomes viable. The simplest option for the Horizontal-Horizontal geometry is to use the same material for the baffles as for the tank walls and to use a simple tank with a flat bottom (rather than sloping the bottom to attempt to match the water surface slope). Your task will be to create that design.

You may recall that the baffle loss coefficient is a function of the H/S ratio. We will sidestep that issue with this design by simply using an H/S ratio that is larger than 6.

Learning Objectives
===================

* Design a hydraulic flocculator for plants with flows greater than about 100 L/s and up to about 10,000 L/s! (Only limited by the depth of water that the tank walls in our parts database can withstand and by the size of drain pipes.)
* Explore design constraints and identify the most cost efficient options.
* Build on what you've learned previously to create the design without having every step detailed in the directions
* Compare the cost of your design with the AguaClara Horizontal-Vertical Flocculator
* Learn how to use the pipeline feature to add a drain system to the flocculator

In the following FS means FeatureStudio and PS means PS.
As you are developing code create it in small pieces and verify as you go that there are no errors in the FeatureScript notices.

1) FS: Create a function (based on :eq:`K_baffle_min`) that calculates :math:`K_{baffle}` from the *vena contracta* for the case when :math:`\Pi_{H_eS}>6`. Our best estimate for the *vena contracta* is from sluice gates where the geometry is very similar to flow around a baffle and thus use a value of 0.6. The function can take :math:`\Pi_{H_eS}` as the only input and return :math:`K_{baffle}`. Remember that the fluid change in direction is twice as large for a baffle than for a sluice gate. What is the value of :math:`K_{baffle}`?

1) FS: Create a function that calculates the flocculator flow dimensions and takes the design map as an input and returns the design map (with more parameters defined). In this function calculate the following

  * viscosity (design.NU)
  * the design value for the velocity gradient (design.G_bod) given the :math:`HL_{bod}` (bod: basis of design)
  * the baffle spacing (design.S), :math:`S`, assuming the flow passage is square (see Equation :eq:`floc_baffle_spacing_squareGeometry`)
  * the baffle spacing for the case (if statement here!) where the target outlet water height is greater than the calculated design.S. Use Equation :eq:`floc_baffle_spacing_const_PiHS`
  * the distance between expansions (design.He), :math:`H_e`
  * the residence time (design.baffleSpaceTI) in one baffle space.
  * the average velocity (design.V) of the water in the flocculator for fully expanded flow
  * the head loss for one baffle (baffleHL)

1) FS: Calculate these additional values

  * the residence time for the entire flocculator (design.TI_bod) based on the required design.GT_min.
  * the number of baffle spaces (design.baffleSpacesN) given the residence time in each baffle space. Use the ceil function to round up.
  * the active residence time based on the number of baffle spaces. Note that this time does not include the extra time that results from head loss increasing the water level.
  * the total head loss that takes into account the fraction of the design flow that the flocculator is currently treating, design.Q_pi. You will need to derive an equation for this.
  * the height of the tank walls.
  * the volume (design.VOL) taking into account the extra triangle of water caused by head loss. You don't need to take into account the water in the ports through the baffle walls.

1) PS: Copy the overrides from the FeatureScript notices into the overrides configuration. This should result in no warning messages in the FeatureScript notices.
1) PS: Use the civil tank feature to draw the flocculator tank. Note that the civil tank has an option for ports that can be used to turn the internal tank walls into baffles. Initially set the port height to be the same as the tank wall height so that the ports effectively remove a

1) PS: Insert the Civil Tank feature.

1) PS: Draw the water surface for the entire flocculator. To simplify this challenge make the assumption that the water slopes uniformly from one end of the flocculator to the other as it crosses the many baffles.

1) The water elevation in a flocculator is controlled by the water elevation in the downstream sedimentation tank because we can't have a sudden decrease in water elevation (a waterfall!) because that would break up the flocs. The water depth increases as we move upstream in the flocculator because potential energy is being lost to heat as the water is being deformed. This increase in water elevation results in the flow area increasing and the velocity decreasing as we move upstream. This would result in less energy loss in the upstream baffles. To remedy this situation and increase the strength of the tank, set the port height to be equal to the target width of the flow so that a beam extends over the top of the port.

1) FS: Design a drain for the flocculator tank?

Part 2 - Part Studio Steps
==========================




# Below is draft of possible future assignment
Given a flocculator designed by AIDE (S, HE, Q, Nbaffles), calculate (V, theta, G, Gtheta, HL, VOL)

Compare cost of the flocculator as a function of HL
An important design constraint that is not well characterized is the maximum G that can be used. The maximum G determines the size of the flocs entering the sedimentation tank. If those flocs are too small to be captured by the plate settlers, then those flocs aren't effectively captured by the sedimentation tank and will contributed to the settled water turbidity. The sedimentation velocity of a floc (and hence its ability to be captured by the plate settlers) is a function of its size AND its density. Flocs that are made of clay and coagulant are more dense than flocs that are made of organic matter and coagulant. Your task is to explore how the flocculator design changes if the maximum velocity gradient is reduced from 200 Hz to 100 Hz and then to 50 Hz. Describe the changes in the flocculator and answer these questions for a vertical-horizontal flocculator.
1) When you vary G_max, should you keep theta constant or Gtheta constant? Explain why!
1) Why does the HE increase as G_max is decreased?
1) Why does the volume of the flocculator increase as G_max is decreased?
1) Does the number of baffles increase, decrease, or stay the same? Can you explain why? Find or derive an equation to calculate Gtheta for a single baffle to explain this!
1) How much does the cost of the flocculator change when G is reduced from 100 Hz to 50 Hz?
