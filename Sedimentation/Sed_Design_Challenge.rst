.. _title_Sedimentation_Design_Challenge:

******************************
Sedimentation Design Challenge
******************************

Designing a sedimentation tank requires selecting several key design parameters. The upflow velocity sets the plan view area of the sedimentation tank and thus directly controls the cost of the concrete tank. The capture velocity sets the required area of the plate settlers and thus sets their cost. The maximum velocity gradient sets the maximum velocity exiting the diffuser ports and that in turn sets the maximum velocity in the inlet manifold and hence the diameter of the inlet manifold.

We know that performance deteriorates as the flow rate increases in a flocculation/sedimentation systems. To improve the performance of AguaClara plants at maximum flow we are exploring reducing the maximum velocity gradient in the flocculator and the inlet to the sedimentation tank. If we reduce the maximum velocity gradient to 100 Hz the inlet manifold for a 6 L/s plant increases to 10" nominal diameter and that pipe costs a significant fraction of the total sedimentation tank materials.

Equation :eq:`G_of_vc_and_floc_props` reveals that there is a tradeoff between the velocity gradient entering the sedimentation tank and the capture velocity of the plate settlers.


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
#. What is the ID of an 8" pipe with an SDR of 41? Use the queryPipeWithFittingDim function. Note that it returns a map with many parameters.
#. Increase the velocity gradient for the diffuser until the inlet pipe switches from 10" to 8". You can see the change in the minimum required pipe ID by using the variable table with this input (#sedPlastic.inletManifold.manifold). The variable table is another custom table option at the same location as the bill of materials. You can see how much you have to adjust the velocity gradient based on the value of the minimum required pipe ID. What is the minimum velocity gradient that results in an 8" ND inlet manifold?
#. Use Equation :eq:`G_of_vc_and_floc_props` to calculate the maximum capture velocity that can be used given a water temperature of 5°C and assuming that the maximum allowable value of :math:`\zeta = 4.9 \cdot \frac{mm^8}{s^6}`.
#. Change the capture velocity in the designOverrides and find the new cost of the 6 L/s sedimentation tank with an 8" inlet manifold.
#. Explain why the cost decreased.
#. How many plate settlers are in this sedimentation tank (see if you can find this value in the design map using the variable table)?
#. What is the flow rate between two plates? Note that the number of spaces between plates is one less than the number of plates!
#. What is the plan view area of the entrance into the space between two plate settlers? We will use this to calculate the vertical component of the velocity entering the plate settlers.
#. What is the vertical velocity entering the plate settlers? You'll need to use continuity to figure this out.
#. Why is this velocity greater than the upflow velocity in the sed tank in the section where the walls are vertical?
#. What is the capture velocity of these plate settlers (see Equation :eq:`vc_of_vz_plate`)?
#. Is the calculated capture velocity better than or worse than the design capture velocity?
