.. raw:: html

    <embed>
       <link rel="canonical" href="https://aguaclara.github.io/Textbook/Clarification/Clarifier_Design_Challenge.html" />
       <script src="https://hypothes.is/embed.js" async></script>
    </embed>

.. _title_Clarification_Design_Challenge:

******************************
Clarification Design Challenge
******************************

Designing a clarifier requires selecting several key design parameters. The upflow velocity sets the plan view area of the clarifier and thus directly controls the cost of the concrete tank. The capture velocity sets the required area of the plate settlers and thus sets their cost. The maximum velocity gradient sets the maximum velocity exiting the diffuser ports and that in turn sets the maximum velocity in the inlet manifold and hence the diameter of the inlet manifold.

Create a copy of the `Clarifier Template <https://cad.onshape.com/documents/37c3642d5566cf6b172fe9ad/w/99df7cb12d54d9a652b7d74e/e/99b313b3d094d5a33a5f0cc9?configuration=G_max%3D140.0%3BQm_max%3D6.0%3BTEMP_min%3D5.0%3BcaptureVm%3D0.12%3Bip%3DAPP%3BplateAN%3D60.0%3BplateS%3D0.025%3Brep%3Dfalse%3BupVm%3D1.0&renderMode=0&uiState=640cb6f5fb8efc495ca8914b>`_. The design can be modified directly by editing the configuration inputs in the part studio. The Design Analysis feature studio is where you can do calculations and answer the questions. Note that there are questions related to the full `Clarifier <https://cad.onshape.com/documents/e05915c533ee7568c402981a/v/33d36b3cb7dffdb7c56f5574/e/3f94eabd115787bc33ae755d?configuration=G_max%3D140.0%3BQm_max%3D12.0%3BShow_Internal_Components%3Dtrue%3BTEMP_min%3D5.0%3BcaptureVm%3D0.12%3Bip%3DAPP%3BplateAN%3D60.0%3BplateS%3D0.025%3Brep%3Dfalse%3BrepBayInternals%3Dfalse%3BupVm%3D1.0&renderMode=0&uiState=640cbabd6038ca7b677baa1b>`_ in the function reflections of the Clarifier Template.


Learning Objectives
===================

* Play with the design and then reflecting on how the underlying physics is controlling the resulting design.
* Make the connections between raw water characteristics, flocculator design, and clarifier design.
* Learn the power of combining the constraints imposed by physics with the cost of materials to guide the design.


Playful Reflections
===================


#. Use the full clarifier to answer the following questions. Use the defaults as provided in the link and return to the link if you forget the defaults. Write the answers to these questions in the function reflections of the Clarifier Template.
    #. What do you initially think will happen to the total cost of the 0.8 mm polycarbonate sheets used for plate settlers if you were to increase the spacing of the plate settlers? (no wrong answers here!)
    #. Vary the Plate settler spacing from 1 cm to 5 cm and observe the cost of the 0.8 mm polycarbonate sheets. What do you observe and is it what you expected?
    #. Write a sentence or two to explain what you observed based on the underlying physics of the plate settlers. Remember that it is on the projected area (horizontal area) that particles can settle out. Refer to Equation :eq:`eq_vc_of_vz_plate` and also consider how the number of plate settlers changes as you vary the spacing.
    #. Why does the depth of the clarifier change when the plate settler spacing is changed? Watch the change in design carefully to see exactly which dimensions change.
    #. Reset the plate settler spacing to 2.5 cm. Now play with the plate settler angle. We haven't done any research on this parameter and different manufactures of plate settlers use slightly different angles. How much would the clarifier cost decrease if we decreased the plate settler angle from 60° to 55°?
    #. Identify at least 3 changes in the design as you decrease the flow from 12 L/s to 1 L/s.

Design Exploration 2
====================

This part of the design exploration focuses on the plastic components that fit inside each of the bays in a clarifier.
The rendering time for the design is significantly faster if replicate parts is set to false. When replicate parts is false the part studio only shows single parts in most cases. Although all of the replicated parts aren't shown, the cost calculations are still correct. You can verify this by setting replicate parts to true and then check to see if the Bill of Materials is the same.

Use the following values as the defaults for this design.

* design the components for Agua Para el Pueblo (APP).
* flowrate = 6 L/s
* maximum velocity gradient (in the inlet manifold and jet reverser) = 140 1/s
* minimum temperature = 5°C
* upflow velocity (at the top of the floc filter) of 1 mm/s
* plate settler capture velocity of 0.12 mm/s
* plate settler angle = 60°

Note that the default flow rate for the clarifier was 12 L/s while the default flow rate for the plastic component is for 6 L/s. That is because the clarifier defaults to two bays for 6 L/s and thus to get a bay that is for 6 L/s requires a total clarifier flow of 12 L/s.

You can use the Variable Table in the custom tables to browse the map of design variables.
With MapToDisplay empty, you can see all of the top level entries in the design map. To browse deeper in the map enter

.. _figure_VariableTable:

.. figure:: ../Images/VariableTable1.png
    :height: 300px
    :align: center
    :alt: Custom variable table.

    Browsing the top level variable of the design map.

To browse the map of settler, simply type #settler in the MapToDisplay.

.. _figure_VariableTable2:

.. figure:: ../Images/VariableTable2.png
    :height: 300px
    :align: center
    :alt: Custom variable table.

    Browsing the next level deeper of the design map.

To browse further simply append the name of the next variable using dot notation (for example #settler.module.pipe).

Answer the following questions.

#. What is the total cost of the plastic for the default design? Use the Bill of Material and simply copy the total cost and paste it into your answer. It would be cool to make a cost function that could be called in FeatureScript for a part studio that would make it easy to change inputs and compare costs, but we don't have that figured out yet!
#. What is the cost of the inlet manifold pipe as listed in the Bill of Materials? Note that this does not include the elbow and coupling that are designed as part of the channel system in the clarifier.
#. Use Equation :eq:`G_of_vc_and_floc_props`, the design defaults for capture velocity and inlet manifold maximum velocity gradient, and a water temperature of 5°C to calculate the value of :math:`\xi_{breakup}` that is implicitly used in the design of the clarifier. Create new variables for capture velocity and velocity gradient so those values don't change as we make changes to the design inputs (design.G_bod and design.captureVm_bod). Note that this value is smaller than the value of :math:`\xi_{breakup} = 50 \cdot \frac{mm^8}{s^6}` that was experimentally determined for a kaolin suspension. We are still learning how :math:`\xi_{breakup}` controls the design of diffusers and plate settlers. We know that surface waters that contain dissolved organics will have core particle densities that are lower than kaolin clay and thus based on Equation :eq:`G_of_vc_and_floc_props` the value of :math:`\xi_{breakup}` will be reduced significantly.
#. Increase the maximum velocity gradient (in the configuration inputs of the part studio) until the inlet pipe switches from 8" ND to 6" ND. What is the minimum velocity gradient that results in an 6" ND inlet manifold? Given that you are finding this value by iteration provide an answer that is within 10 Hz of the actual value.
#. Use Equation :eq:`G_of_vc_and_floc_props` to calculate the maximum capture velocity given this new velocity gradient and assuming that the maximum allowable value of :math:`\xi_{breakup}` is the implicit default value you calculated in step 3.
#. Explain why the plate settler design has to change to counteract the change in the velocity gradient.
#. Change the capture velocity (in the configuration inputs of the part studio) and find the new cost of the 6 L/s clarifier with an 6" inlet manifold.
#. Explain why the cost decreased from the initial value even though this new design has the same value for  :math:`\xi_{breakup}`.
#. How many plate settlers are in this clarifier? You can browse the design map using the custom Variable Table (in the same location as the Bill of Materials).
#. What is the flow rate between two plates? Note that the number of spaces between plates is one less than the number of plates!
#. What is the plan view area of the entrance into the space between two plate settlers? We will use this to calculate the vertical component of the velocity entering the plate settlers.
#. What is the vertical velocity entering the plate settlers? You'll need to use continuity to figure this out.
#. Why is this velocity greater than the upflow velocity in the clarifier in the section where the walls are vertical? You can look at the side view of the clarifier to understand why the water has to speed up when it transitions from the top of the floc filter to the plate settlers.
#. We will check how close the design is to the specifications that were given initially. What is the capture velocity of these plate settlers (see Equation :eq:`vc_of_vz_plate`)?
#. Is the calculated capture velocity better than or worse than the design capture velocity?
