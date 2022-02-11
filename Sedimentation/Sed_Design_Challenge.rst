.. _title_Sedimentation_Design_Challenge:

******************************
Sedimentation Design Challenge
******************************

Designing a sedimentation tank requires selecting several key design parameters. The upflow velocity sets the plan view area of the sedimentation tank and thus directly controls the cost of the concrete tank. The capture velocity sets the required area of the plate settlers and thus sets their cost. The maximum velocity gradient sets the maximum velocity exiting the diffuser ports and that in turn sets the maximum velocity in the inlet manifold and hence the diameter of the inlet manifold.

We know that performance deteriorates as the flow rate increases in a flocculation/sedimentation systems. To improve the performance of AguaClara plants at maximum flow we are exploring reducing the maximum velocity gradient in the flocculator and the inlet to the sedimentation tank. If we reduce the maximum velocity gradient to 100 Hz the inlet manifold for a 6 L/s plant increases to 10" nominal diameter and that pipe costs about 33% (depending on the SDR or pipe wall thickness that is selected) of the total sedimentation tank materials.

:eq:`G_of_vc_and_fractal_of_2` reveals that


Learning Objectives
===================

* Make the connections between raw water characteristics, flocculator design, and sedimentation tank design.
* Learn the power of combining the constraints imposed by physics with the cost of materials to guide the design.


Design steps
============

#. Create a copy of the `sedimentor part studio <https://www.aguaclarareach.org/>`_. This workspace includes many part studios and feature studios to create the many subcomponents that are then all connected together in the top level AguaClarifier part studio.
#. Use the your sedimentor part studio to design a 12 L/s sedimentation tank. Use the defaults for all of the other inputs. You can do this by pasting "{}" in the overrides, then copy the default overrides from the FeatureScript notices, paste them into a `JSON formatter <https://jsonformatter.org/>`_, and then edit the flow to be 12.
#. What is the total cost of the sedimentation tank

#. What fraction of that cost is the d?
Use the Inlet Manifold part studio to increase the velocity gradient in the diffuser until the inlet pipe switches from 10" to 8".
#. jet reversers alternative design
#.


Notes for setting up the Challenge
==================================
Each team can create their own copy of the sedimentor.
