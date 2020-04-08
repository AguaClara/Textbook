.. _Sedimentation_Examples:


***************************************
Sedimentation Examples
***************************************


Design a tube settler for a laboratory scale sedimentation tank. The vertical section of the sedimentation tank has a net upflow velocity of 3 mm/s. This velocity is maintained in the tube settler, :math:`V_\alpha`. The target capture velocity is 0.2 mm/s. The tube settler diameter is 2.54 cm.

.. math:: \frac{\bar v_{\uparrow}}{v_c} = \frac{L}{D} \cos \alpha \sin \alpha + \sin ^2 \alpha

.. math:: \bar v_\uparrow = \bar v_\alpha\sin \alpha

Solve for the length of the tube settler.

.. math:: L = \frac{D}{\cos \alpha}\left(\frac{\bar v_\alpha}{\bar v_c} - \sin \alpha\right)


.. code:: python

 from aide_design.play import*
 v_alpha = 3 * u.mm/u.s
 v_c = 1 * u.mm/u.s
 D = 2.54 * u.cm
 alpha = 60 * u.deg

 def L_settler(D,alpha,v_alpha,v_c):
   return D/np.cos(alpha)*(v_alpha/v_c - np.sin(alpha))

 print(L_settler(D,alpha,v_alpha,1*u.mm/u.s))
 print(L_settler(D,alpha,v_alpha,0.2*u.mm/u.s))

The tube settler above the floc hopper needs to be 72 cm long. The tube settler should provide a capture velocity of at least 1 mm/s prior to the floc hopper. Thus there should be 11 cm below the floc hopper.  
