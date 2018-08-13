.. _title_Rapid_Mix_Theory_and_Future_Work:

********************************
Rapid Mix Theory and Future Work
********************************


Our understanding of rapid mix is currently quite speculative. This is an area that requires substantial research. We have anecdotal evidence that the process of transporting coagulant nanoparticles to suspended particle surfaces may be a slow, rate-limiting process. Dissolved organic matter may influence the rate of coagulant nanoparticle transport by effectively increasing the size of the coagulant nanoparticles and thus reducing the diffusion rate.

Developing a fundamental understanding of the mixing and transport processes that occur between coagulant addition and flocculation is a very high priority for the AguaClara program.



.. _heading_Diffusion_and_Shear_Transport_Coagulant_Nanoparticles_to_Clay:

Diffusion and Shear Transport Coagulant Nanoparticles to Clay
================================================================

The time required for shear and diffusion to transport coagulant nanoparticles to clay has previously been assumed to be a rapid process.
.. todo:: Find references for time required for coagulant attachment to suspended particles.

Our analysis suggests that this critical step may require significant time especially given our effort to reduce the time allotted for flocculation.

  - Turbulent eddies, viscous shear, and diffusion blends the coagulant with the raw water sufficiently (:ref:`in a few seconds<heading_Mixing_time>`) so that the coagulant precipitates and forms nanoparticles.
  - Dissolved organic molecules diffuse to the coagulant nanoparticles and adhere to the nanoparticle surface.
  - The coagulant nanoparticles are transported to suspended particle surfaces by a combination of diffusion and fluid shear.

The following is a very preliminary estimate of the time required for attachment of the nanoparticles to the clay particles. This analysis includes multiple simplifying assumptions and there is a reasonable possibility that some of those assumptions are wrong. However, the core assumptions that coagulant nanoparticles are transported to clay particles by a combination of fluid deformation (shear) and molecular diffusion is reasonable.

The following analysis is similar to the collision analysis that was developed in the AguaClara flocculation model. The core idea is that viscous shear dominated fluid deformation causes relative motion between the coagulant nanoparticles and the clay particles (or other suspended particles) with which they eventually will collide. The collision between these particles that are very different in size is difficult to achieve because there is a viscous layer of fluid around the clay particles that the clay particle drags with it as it rotates in deforming fluid. The coagulant nanoparticle that

The volume of the suspension that is cleared of nanoparticles is proportional to a collision area defined by a ring around the clay particle with width of the diameter of the nanoparticle diffusion band. This diffusion band is the length scale over which diffusion is able to transport coagulant particles to the clay surface during the time that the nanoparticles are sliding past the clay particle.



.. _figure_Coagulant_nanoparticle_clay_collisions:

.. figure:: Images/Coagulant_nanoparticle_clay_collisions.png
    :width: 400px
    :align: center
    :alt: Coagulant nanoparticle clay collisions

    Fluid deformation moves coagulant nanoparticles close to clay particles and diffusion helps transport the nanoparticles the last nanometers toward a successful collision.

The volume cleared is proportional to the area of this ring. Here we assume that the :math:`L_{Diff_{NC}} << d_{Clay}`

.. math::  \propto \pi \, d_{Clay} \, L_{Diff_{NC}}

The volume cleared is proportional to time

.. math::  \propto t

The volume cleared is proportional to the relative velocity between clay and nanoparticles. This relative velocity is in the viscous layer of fluid in the ring surrounding the clay particle.

.. math::  \propto v_r

Combining the previous three equations we obtain.

.. math::  \bar v_{\rm{Cleared}} = \pi  d_{Clay} \, L_{Diff_{NC}}  v_r  t

Use dimensional analysis to get a relative velocity for the long range transport controlled by shear.

.. math:: v_r = f \left( \varepsilon ,\nu ,\Lambda_{Clay} \right)

.. math:: v_r = \Lambda_{Clay} f \left( \varepsilon ,\nu \right)

.. math:: v_r \approx \Lambda_{Clay} G

.. math::

  \Lambda_{Clay} = [L]
  \, \, \, \, \, \, \,
  \varepsilon = \frac{[L]^2}{[T]^3}
  \, \, \, \, \, \, \,
  \nu = \frac{[L]^2}{[T]}

.. _heading_Collision_Rates:

Collision Rates
===============

.. math:: {\rlap{\kern.08em--}V_{\rm{Cleared}}} \approx \pi d_{Clay} L_{Diff_{NC}} v_r t_c

Where :math:`\rlap{\kern.08em--}V_{Occupied} = \Lambda_{Clay}^3`. Solve for :math:`t_c`:

.. math:: t_c = \frac{\Lambda_{NC}^3}{\pi d_{Clay} L_{Diff_{NC}} v_r}

This is the average time for a clay particle to have the entire volume of water that it occupies sweep past the clay particle.
:math:`v_r \approx \Lambda_{Clay} G`

.. math:: t_c = \frac{\Lambda_{Clay}^3}{\pi d_{Clay} L_{Diff_{NC}} \Lambda_{Clay} G}

Where :math:`t_c = \frac{dN_c}{dt}`:

.. math:: dN_c = \pi d_{Clay} L_{Diff_{NC}}{\Lambda^{-2}_{Clay}} G dt

.. _heading_Collision_Rate_and_Particle_Removal:

Collision Rate and Particle Removal
-----------------------------------

A fraction of the remaining coagulant nanoparticles are removed during the time required for one sweep past the clay particle.

.. math:: \frac{dn_{NC}}{ - k \, n_{NC}} = dN_c

.. math:: \frac{dn_{NC}}{ - k \, n_{NC}} = \pi d_{Clay} L_{Diff_{NC}}{\Lambda^{-2}_{Clay}} G dt

.. _heading_Integrate_the_coagulant_transport_model:

Integrate the coagulant transport model
---------------------------------------

Integrate from the initial coagulant nanoparticle concentration to the concentration at time t.

.. math:: \int \limits_{n_{NC_0}}^{n_{NC}} n_{NC}^{- 1} \, dn_{NC}  =  - \pi d_{Clay} L_{Diff_{NC}} \Lambda^{-2}_{Clay} G \, k  \int \limits_0^t {dt}

Use pC notation to be consistent with how we describe removal efficiency of other contaminants.

.. math:: 2.3 p C_{NC} = \pi d_{Clay}\,  L_{Diff_{NC}}\,  \Lambda^{-2}_{Clay}\,  G k  t

Solve for the time required to reach a target efficiency of application of coagulant nanoparticles to clay.

.. math::

    t_{coagulant, \, application} = \frac{2.3p C_{NC} \, \Lambda_{Clay}^2}{\pi G k \, d_{Clay}\,  L_{Diff_{NC}} }


Coagulant nanoparticle application
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. math::   \Delta h =   \frac{G^2 \nu \theta}{g}

Replace :math:`\theta` with t.

.. math::   \Delta h =  \frac{G^2 \nu}{g} \frac{2.3p C_{NC} \, \Lambda_{Clay}^2}{\pi G k \, d_{Clay}\,  L_{Diff_{NC}} }

.. math:: L_{Diff} \approx \left( \frac{2k_B T d_{Clay}}{3 \pi \,\mu  \, d_{NC} G}\right)^\frac{1}{3}

.. math::   \Delta h =  \frac{G^2 \nu}{g} \frac{2.3p C_{NC} \, \Lambda_{Clay}^2}{\pi G k \, d_{Clay}} \left( \frac{3 \pi \,\mu  \, d_{NC} G}{2k_B T d_{Clay}}\right)^\frac{1}{3}

Solve for the velocity gradient.

.. math::   \Delta h =  \frac{G^\frac{4}{3} \nu}{g} \frac{2.3p C_{NC} \, \Lambda_{Clay}^2}{\pi k \, d_{Clay}} \left( \frac{3 \pi \,\mu  \, d_{NC} }{2k_B T d_{Clay}}\right)^\frac{1}{3}

.. math::


    G_{coagulant, \, application} =  d_{Clay}\left(\frac{\pi k \,g\Delta h }{2.3p C_{NC} \, \Lambda_{Clay}^2 \nu} \right)^\frac{3}{4} \left( \frac{2k_B T }{3 \pi \,\mu  \, d_{NC} }\right)^\frac{1}{4}


Diffusion band thickness
------------------------

The time required for shear to transport all of the fluid past the clay so that diffusion can transport the coagulant nanoparticles to the clay surface is significant.

.. math:: D_{Diffusion} = \frac{k_B T}{3 \pi \, \mu \, d_P}

.. math:: L_{Diff} \approx \sqrt{D_{Diffusion} t_{Diffusion}}

The time for nanoparticles to diffuse through the boundary layer around the clay particle is equal to the distance they travel around the clay particle divided by their velocity. The distance they travel scales with :math:`d_{Clay}` and their average velocity scales with the thickness of the diffusion layer/2 \* the velocity gradient.

.. math:: t_{Diffusion} = \frac{ 2d_{Clay}} {L_{Diff} G}

.. math:: L_{Diff} \approx \left( \frac{2k_B T d_{Clay}}{3 \pi \,\mu  \, d_{NC} G}\right)^\frac{1}{3}

Let’s estimate the thickness of the diffusion band

.. code:: python

    T_graph = np.linspace(0,30,4)*u.degC
    G = np.arange(50,5000,50)*u.Hz

    def L_Diff(Temperature,G):
      return (((2*u.boltzmann_constant*Temperature * fm.Clay.Diameter*u.m)/(3 * np.pi *pc.viscosity_dynamic(Temperature)* (fm.PACl.Diameter*u.m)*G))**(1/3)).to_base_units()

    fig, ax = plt.subplots()
    for i in range(len(T_graph)):
      ax.semilogx(G,L_Diff(T_graph[i],G).to(u.nm))

    ax.legend(T_graph)
    ax.yaxis.set_major_formatter(FormatStrFormatter('%.f'))
    ax.xaxis.set_major_formatter(FormatStrFormatter('%.f'))
    ax.set(xlabel='Velocity gradient (Hz)', ylabel='Diffusion band thickness ($nm$)')
    fig.savefig(imagepath+'Diffusion_band_thickness')
    plt.show()

.. _figure_Diffusion_band_thickness:

.. figure:: Images/Diffusion_band_thickness.png
    :width: 400px
    :align: center
    :alt: Diffusion band thickness

    Molecular diffusion band thickness as a function of velocity gradient. This length scale marks the transition between transport by fluid deformation and by diffusion.

Using the equation for :math:`L_{Diff}` above, we can solve for  the time required to reach a target efficiency of application of coagulant nanoparticles to clay:

.. math:: t_{coagulant, \, application} = \frac{2.3p C_{NC} \, \Lambda_{Clay}^2}{\pi G k \, d_{Clay}\,  L_{Diff_{NC}} }

The time required for the coagulant to be transported to clay surfaces is strongly dependent on the turbidity as indicated by the average spacing of clay particles, :math:`\Lambda_{Clay}`. As turbidity increases the spacing between clay particles decreases and the time required for shear to transport coagulant nanoparticles to the clay decreases. Increasing the shear also results in faster transport of the coagulant nanoparticles to clay surfaces. The times required are strongly influenced by the size of the coagulant nanoparticles because larger nanoparticles diffuse more slowly.

Below we estimate the time required to achieve 80% attachment of nanoparticles in a 10 NTU clay suspension.

.. code:: python

    """I needed to attach units to material properties due to a bug in floc_model. This will need to be fixed when floc_model is updated."""
    def Nano_coag_attach_time(pC_NC,C_clay,G,Temperature):
      """We assume that 70% of nanoparticles attach in the average time for one collision."""
      k_nano = 1-np.exp(-1)
      num=2.3*pC_NC*(fm.sep_dist_clay(C_clay,fm.Clay))**2
      den = np.pi * G* k_nano * fm.Clay.Diameter*u.m * L_Diff(Temperature,G)
      return (num/den).to_base_units()

    C_Al = 2 * u.mg/u.L
    C_clay = 10 * u.NTU
    pC_NC = -np.log10(1-0.8)
    """apply 80% of the coagulant nanoparticles to the clay"""

    G = np.arange(50,5000,10)*u.Hz

    fig, ax = plt.subplots()

    for i in range(len(T_graph)):
      ax.semilogx(G,Nano_coag_attach_time(pC_NC,C_clay,G,T_graph[i]))

    ax.semilogx(Mix_G.to(1/u.s),Mix_HRT.to(u.s),'o')
    ax.legend([*T_graph, "Conventional rapid mix"])
    """* is used to unpack T_graph so that units are preserved when adding another legend item."""
    ax.yaxis.set_major_formatter(FormatStrFormatter('%.f'))
    ax.xaxis.set_major_formatter(FormatStrFormatter('%.f'))
    ax.set(xlabel='Velocity gradient (Hz)', ylabel='Nanoparticle attachment time (s)')
    fig.savefig(imagepath+'Coag_attach_time')
    plt.show()

.. _figure_Coag_attach_time:

.. figure:: Images/Coag_attach_time.png
    :width: 400px
    :align: center
    :alt: Coag attach time

    An estimate of the time required for 80% of the coagulant nanoparticles to attach to clay particles given a raw water turbidity of 10 NTU.


.. _heading_Energy_Tradeoff_for_Coagulant_Transport:

Energy Tradeoff for Coagulant Transport
-----------------------------------------

.. math::   \Delta h =   \frac{G^2 \nu \theta}{g}

.. code:: python

    Nano_attach_time = Nano_coag_attach_time(pC_NC,C_clay,G,Temperature)

    def HL_coag_attach(pC_NC,C_clay,G,Temperature):
      return (G**2*pc.viscosity_kinematic(Temperature)*Nano_attach_time/u.gravity).to(u.cm)

    fig, ax = plt.subplots()

    for i in range(len(T_graph)):
      ax.loglog(G,HL_coag_attach(pC_NC,C_clay,G,T_graph[i]))

    ax.legend(T_graph)
    ax.yaxis.set_major_formatter(FormatStrFormatter('%.f'))
    ax.xaxis.set_major_formatter(FormatStrFormatter('%.f'))
    ax.set(xlabel='Velocity gradient (Hz)', ylabel='Head loss (cm)')
    fig.savefig(imagepath+'Coag_attach_head_loss')
    plt.show()

.. _figure_Coag_attach_head_loss:

.. figure:: Images/Coag_attach_head_loss.png
    :width: 400px
    :align: center
    :alt: Coag attach head loss

    The total energy required to attach coagulant nanoparticles to raw water inorganic particles increases rapidly with the velocity gradient used in the rapid mix process.

There is an economic tradeoff between reactor volume and energy input. The reactor volume results in a higher capital cost and the energy input requires both higher operating costs and higher capital costs. This provides an opportunity to optimize rapid mix design once we have a confirmed model characterizing the process.

The total potential energy used to operate an AguaClara plant is approximately 2 m. This represents the difference in elevation between where the raw water enters the plant and where the filtered water exits the plant. If we assume that the rapid mix energy budget is a fraction of that total and thus for subsequent analysis we will assume somewhat arbitrarily that the energy available to attach the coagulant nanoparticles to the raw water particles is 50 cm.

We solve the coagulant transport model,
:math:`t_{coagulant, \, application} = \frac{2.3p C_{NC} \, \Lambda_{Clay}^2}{\pi G k \, d_{Clay}\, L_{Diff_{NC}} }`,
for G given a head loss.

.. math:: G_{coagulant, \, application} =  d_{Clay}\left(\frac{\pi k \,g\Delta h }{2.3p C_{NC} \, \Lambda_{Clay}^2 \nu} \right)^\frac{3}{4} \left( \frac{2k_B T }{3 \pi \,\mu  \, d_{NC} }\right)^\frac{1}{4}

.. code:: python

    """find G for target head loss"""
    HL_nano_transport = np.linspace(10,100,10)*u.cm
    def G_max_head_loss(pC_NC,C_clay,HL_nano_transport,Temperature):
      k_nano = 1-np.exp(-1)
      num = u.gravity * HL_nano_transport * np.pi * k_nano
      den= 2.3 * pC_NC * (fm.sep_dist_clay(C_clay,fm.Clay))**2 * pc.viscosity_kinematic(Temperature)
      num2 = 2 * u.boltzmann_constant * Temperature
      den2 = 3 * np.pi * pc.viscosity_dynamic(Temperature) * (fm.PACl.Diameter*u.m)
      return fm.Clay.Diameter*u.m*((((num/den)**(3) * (num2/den2)).to_base_units())**(1/4))
    """Note the use of to_base_units BEFORE raising to the fractional power.
    This prevents a rounding error in the unit exponent."""

    G_max = G_max_head_loss(pC_NC,C_clay,20*u.cm,Temperature)
    print(G_max)

    """The time required?"""
    Nano_attach_time = Nano_coag_attach_time(pC_NC,C_clay,G_max,Temperature)
    print(Nano_attach_time)
    print(G_max*Nano_attach_time)

According to the analysis above, the maximum velocity gradient that can be used to achieve 80% coagulant nanoparticle attachment using only 20 cm of head loss is 142 Hz. This requires a residence time of 100 seconds. These model results must be experimentally verified and it is very likely that the model will need to be modified.

The analysis of the time required for shear and diffusion to transport the coagulant nanoparticles the last few millimeters suggests that it is this last step that requires the most time. Indeed, the time required for coagulant nanoparticle attachment to raw water particles is comparable to the time that will be required for the next step in the processs, flocculation.

.. _heading_Coagulant_Attachment_Mechanism:

Coagulant Attachment Mechanism
===============================
We do not yet understand the origin of the bonds that form between coagulant nanoparticles, between a coagulant nanoparticle and suspended particles, and between coagulant nanoparticles and dissolved organic molecules. Historically the role of the coagulant was assumed to be to reduce the repulsive force between particles so that the particles could get close enough for Van der Waals forces to hold the particles together.

-  Surface charge neutralization hypothesis

   -  coagulant nanoparticles attach to each other
   -

-  Polar bonds

   -  Electronegativity reveals that the aluminum - oxygen bond is more polar than the hydrogen - oxygen bond
   -  The bond between a coagulant nanoparticle and a clay surface can potentially be stronger than the bond between a water molecule and the clay surface.


Rederivation of nanoparticle Attachment
=======================================

The volume cleared is proportional to the area of this ring. Here we assume that the :math:`L_{Diff_{NC}} << d_{Clay}`

.. math::  \propto \pi \, d_{Clay} \, L_{Diff_{NC}}

The volume cleared is proportional to time

.. math::  \propto t

The volume cleared is proportional to the relative velocity between clay and nanoparticles. This relative velocity is in the viscous layer of fluid in the ring surrounding the clay particle.

.. math::  \propto v_r

Combining the previous three equations we obtain.

.. math::  \bar v_{\rm{Cleared}} = \pi  d_{Clay} \, L_{Diff_{NC}}  v_r  t

Use dimensional analysis to get a relative velocity for the long range transport controlled by shear.

.. math:: v_r = f \left( \varepsilon ,\nu ,\Lambda_{Clay} \right)

.. math:: v_r = \Lambda_{Clay} f \left( \varepsilon ,\nu \right)

.. math:: v_r \approx \Lambda_{Clay} G

.. math::

  \Lambda_{Clay} = [L]
  \, \, \, \, \, \, \,
  \varepsilon = \frac{[L]^2}{[T]^3}
  \, \, \, \, \, \, \,
  \nu = \frac{[L]^2}{[T]}

.. _heading_Collision_Rates:

Rederived Collision Rates
=========================

.. math:: {\rlap{\kern.08em--}V_{\rm{Cleared}}} \approx \pi d_{Clay} L_{Diff_{NC}} v_r t_c

Where :math:`\rlap{\kern.08em--}V_{Occupied} = \Lambda_{Clay}^3`. Solve for :math:`t_c`:

.. math:: t_c = \frac{\Lambda_{NC}^3}{\pi d_{Clay} L_{Diff_{NC}} v_r}

This is the average time for a clay particle to have the entire volume of water that it occupies sweep past the clay particle.
:math:`v_r \approx \Lambda_{Clay} G`

.. math:: t_c = \frac{\Lambda_{Clay}^3}{\pi d_{Clay} L_{Diff_{NC}} \Lambda_{Clay} G}

Where :math:`t_c = \frac{dN_c}{dt}`:

.. math:: dN_c = \pi d_{Clay} L_{Diff_{NC}}{\Lambda^{-2}_{Clay}} G dt

.. _heading_Collision_Rate_and_Particle_Removal:

Collision Rate and Particle Removal
-----------------------------------

A fraction of the remaining coagulant nanoparticles are removed during the time required for one sweep past the clay particle.

.. math:: \frac{dn_{NC}}{ - k \, n_{NC}} = dN_c

.. math:: \frac{dn_{NC}}{ - k \, n_{NC}} = \pi d_{Clay} L_{Diff_{NC}}{\Lambda^{-2}_{Clay}} G dt
