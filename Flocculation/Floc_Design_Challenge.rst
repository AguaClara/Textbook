.. _title_Flocculation_Design_Challenge:

*****************************
Flocculation Design Challenge
*****************************

The largest AguaClara hydraulic flocculator that has been built (as of 2022) has a maximum flow rate of 60 L/s and uses the Horizontal-Vertical geometry. For flows greater than 100 L/s the Horizontal-Horizontal geometry becomes viable. The simplest option for the Horizontal-Horizontal geometry is to use the same material for the baffles as for the tank walls and to use a simple tank with a flat bottom (rather than sloping the bottom to attempt to match the water surface slope). Your task will be to create that design.

You may recall that the baffle loss coefficient is a function of the H/S ratio. We will sidestep that issue with this design by simply using an H/S ratio that is larger than 6.

Our design approach requires that everything about the design works when we change the input flow rate. That means that we always use calculated values for all dimensions.

Learning Objectives
===================

* Design a hydraulic flocculator for plants with flows greater than about 100 L/s and up to about 10,000 L/s! The maximum flow rate is only limited by the depth of water that the tank walls in our parts database can withstand and by the size of pipes in our parts database that can be used for the drains.)
* Explore design constraints and identify the most cost efficient options.
* Build on what you've learned previously to create the design without having every step detailed in the directions
* Compare the cost of your design with the AguaClara Horizontal-Vertical Flocculator
* Learn how to use the pipeline feature to add a drain system to the flocculator

Design steps
============

In the following FS means FeatureStudio and PS means PS.
As you are developing code **create it in small pieces and verify as you go that there are no errors** in the FeatureScript notices. This is important! And it will save you time!

1. FS: We have provided a the skeleton of a function (flowDimensions) where you can add code. Use it to calculate the flocculator flow dimensions. Note that the function takes the design map as an input and returns the design map (with more parameters defined). Thus every parameter that you define as design.x will be returned by this function. We have provided recommended names for the parameters that you will be calculating in () below. After each step you can check the value that is being calculated by opening the variable table in the PS. In this function calculate the following:
    1. :math:`K_{baffle}` from the *vena contracta* for the case when :math:`\Pi_{H_eS}>6` (design.baffleK_min). Our best estimate for the *vena contracta* is from sluice gates where the geometry is very similar to flow around a baffle and thus use a value of 0.6 for a 90 degree bend. Remember that the fluid change in direction is twice as large for a baffle than for a sluice gate and thus it contracts by this much twice!
    1. viscosity (design.NU)
    1. the baffle spacing (design.S), :math:`S`, assuming the flow passage is square (see Equation :eq:`floc_baffle_spacing_squareGeometry`)
    1. the baffle spacing for the case (if statement here!) where the target outlet water height is greater than the calculated design.S. Use Equation :eq:`floc_baffle_spacing_const_PiHS`
    1. the distance between expansions (design.He), :math:`H_e`
    1. the residence time (design.baffleSpaceTI) in one baffle space.
    1. the average velocity (design.V) of the water in the flocculator for fully expanded flow
    1. the head loss for one baffle (baffleHL)
1. FS: Calculate these additional values. These can be added in the HHflocPreDesigner function.
    1. the required residence time for the entire flocculator (design.TI_bod) based on the required design.GT_min.
    1. the number of baffle spaces (design.baffleSpacesN) given the required residence time in each baffle space. Use the ceil function to round up.
    1. the active residence time based on the number of baffle spaces (design.TI_active). Note that this time does not include the extra time that results from head loss increasing the water level.
    1. the total head loss that takes into account the fraction of the design flow that the flocculator is currently treating, design.Q_pi (design.HL_total). You will need to derive an equation for this.
    1. the height of the tank walls (design.H).
    1. the total volume of water in the flocculator (design.VOL_total) taking into account the extra triangle of water caused by head loss. You don't need to take into account the water in the ports through the baffle walls. If this isn't clear you can postpone this until after you've created the flocculator tank and the water surface.
1. PS: Copy the overrides (everything inside the {}) from the FeatureScript notices into the overrides configuration (very top left of the PS window). This should result in no warning messages in the FeatureScript notices.

1. PS: Use the civil tank feature to draw the flocculator tank. Note that the civil tank has an option for ports that can be used to turn the internal tank walls into baffles. Initially set the port height to be the same as the tank wall height so that the ports effectively remove a section of the wall. You will have to think about geometry and the correspondence between the flow geometry in Equation :eq:`floc_baffle_spacing_const_PiHS` and the tank geometry required as inputs for the civil tank feature.

1. PS: Draw the water surface for the entire flocculator. To simplify this challenge make the assumption that the water slopes uniformly from one end of the flocculator to the other as it crosses the many baffles. There are many ways to approach this. We need a line that can then be "extruded" into a surface that will be normal to the sketch plane that the line was drawn on. To avoid needing a slanted plane you can create a sketch on the Front plane (assuming that you didn't move the tank after inserting). All you need is to define a line on the sketch that has the right starting and ending elevations. Then extrude it to create a surface. Note that the extrude tool can either create a solid or a surface so you'll need to select the surface option.

1. The water elevation in a flocculator is controlled by the water elevation in the downstream sedimentation tank because we can't have a sudden decrease in water elevation (a waterfall!) because that would break up the flocs. The water depth increases as we move upstream in the flocculator because potential energy is being lost to heat as the water is being deformed. This increase in water elevation results in the flow area increasing and the velocity decreasing as we move upstream. This would result in less energy loss in the upstream baffles. To remedy this situation and increase the strength of the tank, set the port height to be equal to the target width of the flow so that a beam extends over the top of the port. We don't know if this contraction will be exactly what is needed, but it should be close. This is an example where some computational fluid dynamics would be great to check if this solution behaves as we expect.

1. FS: Design two drains for the flocculator tank. These drains will work together to drain the tank in the specified time (design.drainTI).
    1. Create a drain function (same inputs and outputs as the flowDimension function) that you call from the HHflocPreDesigner.
    1. Calculate the average flow rate through each of the two drains that must be achieved to empty the tank in time design.drainTI. Use the total volume of water (including head loss) in the flocculator to calculate the required flow.
    1. Use the diamMinorPipe function to size the minimum inner diameter of the drain pipe (design.drainID). Use the very good approximation that the drain pipes must deliver twice the average flow given the initial head loss. You can assume that the head available to drive water through the drain is equal to the initial minimum depth of water in the flocculator (i.e. not counting the extra head available because of head loss in the flocculator that results in an increase in water depth).  This assumption will create a slightly conservative design. For the minor loss coefficient you can use minor loss coefficient constants that are already defined in FeatureScript. You can access these constants by starting to type "minor" and a list of options will appear. You can randomly select some loss coefficients initially and then return to this and select the correct coefficients after you have created the drain in the PS.
    1. Use the queryPipeWithFittingDim function to find a pipe in our parts database that meets the inner diameter requirement. Note that there are two versions of the queryPipeWithFittingDim function. Use the one that has 4 inputs. Use the genSDR for SDR and select and ELBOW_90 for the fitting shape (options show up when you "FittingShape."). This function returns the key dimensions of both the pipe and the elbow and places them in a map. Assign the output of the function to (design.drain).
    1. Use printMap(design.drain) to print the resulting map in FeatureNotices so you can see all the cool information that is returned. You'll be using this to sketch the pipelines for the drains next.

1. PS: Build the first drain using the pipeline feature. Add it to your custom features (`Pipeline Feature <https://cad.onshape.com/documents/89bad90758e5bb705cfe2c7f/v/e8a0a108bcf88a7f99d7048b/e/29b26e753604a86d7aebc0de>`_). You might want to learn how the pipeline works by playing with it first. To use pipeline feature, draw a simple sketch that specifies the route of the pipeline (using a series of line segments) and then the pipeline feature will create the pipes and fittings required to follow that route. Each vertex represents a fitting and each line represents a pipe. All lines that go to a vertex MUST end at the vertex because no pipes go right through fittings!  An elbow will be embedded in the floor of the flocculator with the top of the elbow flush with the top of the floor. A short pipe will connected to the horizontal outlet of the elbow and presumably that would dump into some sort of a drain channel in a full plant design. The drain will include a removable vertical pipe inside the flocculator that normally prevents water from entering the drain. To activate the drain that pipe stub will be removed by pulling it out of the elbow socket. The following steps get you started on this task. You will need to iterate to get everything dimensioned correctly!
    1. Create a new sketch, for the sketch plane click on the mate connector icon and then select a mate connector on the main flocculator slab (floor) that is in the front left corner of the slab (very near the origin).  and use a mate connector on the tank to position the first drain. Place the first drain very near the origin with the pipe centered between the tank wall and the first baffle and a distance gapS between the elbow outer diameter and the end wall.
    1. Draw a vertical line that comes up to the top of the tank (roughly) and goes down below the slab. Connect a horizontal line to the vertex below the slab. Close the sketch
    1. Use the pipeline feature to draw a pipeline using the sketch. Enter the pipe nominal diameter using the drain map.
    1. Your goal is to now adjust your design so the elbow is flush with the top of the slab, centered between tank wall and first baffle, gapS between elbow and the end wall, and with the top of the removable pipe level with the top of the tank walls. You can adjust the location of the sketch by moving the mate connector (inside sketch). Set dimensions on the sketch so that the vertex is at the right location so the elbow is flush with the top of the slab (axisL will be helpful here!).
1. PS: Build the second drain at the other end of the tank. In order to know how far to move the copy we need to know the dimensions of the flocculator tank. Happily that is easy.
    1. Open up the civil tank feature that you previously used and select "place design in context". This will create a map containing all of the dimensions of the tank.
    1. Use linear pattern to replicate the drain pipes so there is a second drain. You can simply select the 3 pipeline parts for the Entities to pattern. The direction can be set by the right plane.
    1. The distance for the 2nd drain is `tank.OW - #tank.W - 2*#tank.wallSide .T`. Enter that in the distance inside linear pattern.
    1. Set the instance count to 2 (if it isn't already) and if necessary flip the arrow to move the drain in the other direction. Viola!
    1. Use the `pipe hole <https://cad.onshape.com/documents/c35baaea9a3ba0044a66bc94>`_ feature to put holes in the concrete for the elbow.
1. Now we can explore how changing our design influences the geometry and the cost. You can edit the overrides directly or you can use `JSON formatter <https://jsonformatter.org/>`_
    1. What is the cost of a 100 L/s flocculator (on a per L/s basis) using the default values for all of the parameters? This is the base case for the various changes you will make.
    1. If you force the design to have taller walls it will result in a design that uses less plan view area. Set the wall height to 1.5 m ("outletHW_min": 1.5). Does the cost increase or decrease with taller walls?
    1. What other economic factors might make the flocculator with taller walls be the preferred option in a water treatment plant?
    1. Revert to the base case and then increase the flow rate to 1000 L/s. What happens to the number of baffles and to the cost per L/s?
    1. Revert to the base case and then increase PI_HS to 8. Does the cost increase or decrease? What do you conclude about the optimal value of PI_HS?
    1. Open the `HV Flocculator <https://cad.onshape.com/documents/edb0d8000bff37cc559ebe89/w/1070adceaa2f931d13443deb/e/16171bc5d51fe4caa0b06c4e>`_ and make sure the flow is set to 100 L/s. Which is more cost effective, the HV Flocculator or the HH Flocculator for the flow of 100 L/s? This could be an interesting challenge to figure out where these two competing designs have the same cost and hence where the transition between these designs should occur.
    1. Decrease the temperature to 0 Celsius. What happens to the design? Can you explain why? This is a key insight about flocculation!
    1. Change Q_pi to 0.5. What happens to the water level in the plant? Was the change more dramatic than you expected? Explain why the water level drops so much when the flow rate is 50% of the design flow.
    1. Reduce the basis of design velocity gradient to 50 Hz. What happens to the cost of the flocculator? Explain why this happens.
