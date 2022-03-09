.. _title_Sedimentation_Design_Challenge:

******************************
Sedimentation Design Challenge
******************************

Designing a sedimentation tank requires selecting several key design parameters. The upflow velocity sets the plan view area of the sedimentation tank and thus directly controls the cost of the concrete tank. The capture velocity sets the required area of the plate settlers and thus sets their cost. The maximum velocity gradient sets the maximum velocity exiting the diffuser ports and that in turn sets the maximum velocity in the inlet manifold and hence the diameter of the inlet manifold.

Learning Objectives
===================

* Make the connections between raw water characteristics, flocculator design, and sedimentation tank design.
* Learn the power of combining the constraints imposed by physics with the cost of materials to guide the design.

Design Exploration
==================

Create a copy of the `Sedimentation Template <https://cad.onshape.com/documents/c4c06fe11682a7c27d053171/w/aa02f5c9a6b4328cc182f0e1/e/631cfc4aba85cf4609d01ce8>`_. This workspace includes a feature studio called overrides that has the default inputs for the design and a convenient place to add and edit overrides to the defaults. You will use that to modify the design. The Design Analysis feature studio is where you can do calculations and answer the questions.

The rendering time for the design is significantly faster if rep is set to false. When rep is false the part studio only shows single parts in most cases. Although all of the replicated parts aren't shown, the cost calculations are still correct. You can verify this by setting rep to true and then check to see if the Bill of Materials is the same.

Use a temperature of 5°C, design the tank for APP, and an SDR_max of 41.

#. What is the total cost of the plastic in the default design for a 6 L/s sedimentation tank? Use the Bill of Material and simply copy the total cost and paste it into your answer. It would be cool to make a cost function that could be called in FeatureScript for a part studio that would make it easy to change inputs and compare costs, but we don't have that figured out yet!
#. What is the cost of the inlet manifold pipe? Note that this does not include the elbow and coupling that are designed as part of the channel system in the sedimentation tank.
#. Use Equation :eq:`G_of_vc_and_floc_props`, the design defaults for capture velocity and inlet manifold maximum velocity gradient, and a water temperature of 5°C to calculate the value of :math:`\zeta_{breakup}` that is implicitly used in the design of the sedimentation tank. Create new variables for capture velocity and velocity gradient so those values don't change as we make changes to the design inputs (design.inletManifold.diffuser.G_bod and design.captureVm_bod). Note that this value is smaller than the value of :math:`\zeta_{breakup} = 50 \cdot \frac{mm^8}{s^6}` that was experimentally determined for a kaolin suspension. We are still learning how :math:`\zeta_{breakup}` controls the design of diffusers and plate settlers. We know that surface waters that contain dissolved organics will have core particle densities that are lower than kaolin clay and thus based on Equation :eq:`G_of_vc_and_floc_props` the value of :math:`\zeta_{breakup}` will be reduced significantly.
#. What is the ID of an 8" pipe with an SDR of 41? Use the queryPipeWithFittingDim function. Note that it returns a map with many parameters.
#. Increase the velocity gradient for the diffuser (in the const designOverrides in the overrides tab) until the inlet pipe switches from 10" to 8". You can see the change in the minimum required pipe ID by using the variable table with this input (#sedPlastic.inletManifold.manifold). The variable table is another custom table option at the same location as the bill of materials. You can see how much you have to adjust the velocity gradient based on the value of the minimum required pipe ID. Given that you are finding this value by iteration provide an answer that is within 10 Hz of the actual value. What is the minimum velocity gradient that results in an 8" ND inlet manifold?
#. Use Equation :eq:`G_of_vc_and_floc_props` to calculate the maximum capture velocity that can be used given a water temperature of 5°C and assuming that the maximum allowable value of :math:`\zeta_{breakup}` is the implicit default value you calculated in step 3.
#. Change the capture velocity in the designOverrides and find the new cost of the 6 L/s sedimentation tank with an 8" inlet manifold.
#. Explain why the cost decreased from the initial value even though this new design has the same value for  :math:`\zeta_{breakup}`.
#. How many plate settlers are in this sedimentation tank (see if you can find this value in the design map using the variable table)?
#. What is the flow rate between two plates? Note that the number of spaces between plates is one less than the number of plates!
#. What is the plan view area of the entrance into the space between two plate settlers? We will use this to calculate the vertical component of the velocity entering the plate settlers.
#. What is the vertical velocity entering the plate settlers? You'll need to use continuity to figure this out.
#. Why is this velocity greater than the upflow velocity in the sed tank in the section where the walls are vertical?
#. What is the capture velocity of these plate settlers (see Equation :eq:`vc_of_vz_plate`)?
#. Is the calculated capture velocity better than or worse than the design capture velocity?
