Rapid Mix Derivations
=====================

:math:`t_{eddy}`
~~~~~~~~~~~~~~~~

Eddy turnover time, :math:`t_{eddy}`, is the time it takes for the eddy to travel a distance equal to its length-scale. We assume that the energy of the large eddy is dissipated into smaller length scales in the time :math:`t_{eddy}`:

.. math:: t_{eddy} \approx \frac{L_{eddy}}{v_{eddy}}

The rate of energy loss to smaller scales is

.. math::  \bar\varepsilon \approx\frac{v_{eddy}^2}{t_{eddy}}

Combining the two equations

.. math::  \bar\varepsilon \approx\frac{v_{eddy}^3}{L_{eddy}}

We can use this equation to estimate the eddy velocity given an energy dissipation rate.

.. math:: v_{eddy} \approx \left( \bar\varepsilon \, L_{eddy} \right)^\frac{1}{3}

Now we can solve for the eddy turnover time which is a measure of the mixing time at the eddy scale.

.. math::
    \color{purple}{
      t_{eddy} \approx \frac{L_{eddy}}{\left( \bar\varepsilon \, L_{eddy} \right)^\frac{1}{3}} \approx \left( \frac{L_{eddy}^2}{ \bar\varepsilon }\right)^\frac{1}{3}
    }

:math:`t_{coagulant, \, application}`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Collision Rates
^^^^^^^^^^^^^^^

.. math:: {\rlap{\kern.08em--}V_{\rm{Cleared}}} \approx \pi d_{Clay} L_{Diff_{NC}} v_r t_c

Where :math:`\rlap{\kern.08em--}V_{Occupied} = \Lambda_{Clay}^3`. Solve for :math:`t_c`:

.. math:: t_c = \frac{\Lambda_{NC}^3}{\pi d_{Clay} L_{Diff_{NC}} v_r}

This is the average time for a clay particle to have the entire volume of water that it occupies sweep past the clay particle.
:math:`v_r \approx \Lambda_{Clay} G`

.. math:: t_c = \frac{\Lambda_{Clay}^3}{\pi d_{Clay} L_{Diff_{NC}} \Lambda_{Clay} G}

Where :math:`t_c = \frac{dN_c}{dt}`:

.. math:: dN_c = \pi d_{Clay} L_{Diff_{NC}}{\Lambda^{-2}_{Clay}} G dt

Collision Rate and Particle Removal
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A fraction of the remaining coagulant nanoparticles are removed during the time required for one sweep past the clay particle.

.. math:: \frac{dn_{NC}}{ - k \, n_{NC}} = dN_c

.. math:: \frac{dn_{NC}}{ - k \, n_{NC}} = \pi d_{Clay} L_{Diff_{NC}}{\Lambda^{-2}_{Clay}} G dt

Integrate the coagulant transport model
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Integrate from the initial coagulant nanoparticle concentration to the concentration at time t.

.. math:: \int \limits_{n_{NC_0}}^{n_{NC}} n_{NC}^{- 1} \, dn_{NC}  =  - \pi d_{Clay} L_{Diff_{NC}} \Lambda^{-2}_{Clay} G \, k  \int \limits_0^t {dt}

Use pC notation to be consistent with how we describe removal efficiency of other contaminants.

.. math:: 2.3 p C_{NC} = \pi d_{Clay}\,  L_{Diff_{NC}}\,  \Lambda^{-2}_{Clay}\,  G k  t

Solve for the time required to reach a target efficiency of application of coagulant nanoparticles to clay.

.. math::

  \color{purple}{
     t_{coagulant, \, application} = \frac{2.3p C_{NC} \, \Lambda_{Clay}^2}{\pi G k \, d_{Clay}\,  L_{Diff_{NC}} }
   }

:math:`G_{coagulant, \, application}`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. math::   \Delta h =   \frac{G^2 \nu \theta}{g}

Replace :math:`\theta` with t.

.. math::   \Delta h =  \frac{G^2 \nu}{g} \frac{2.3p C_{NC} \, \Lambda_{Clay}^2}{\pi G k \, d_{Clay}\,  L_{Diff_{NC}} }

.. math:: L_{Diff} \approx \left( \frac{2k_B T d_{Clay}}{3 \pi \,\mu  \, d_{NC} G}\right)^\frac{1}{3}

.. math::   \Delta h =  \frac{G^2 \nu}{g} \frac{2.3p C_{NC} \, \Lambda_{Clay}^2}{\pi G k \, d_{Clay}} \left( \frac{3 \pi \,\mu  \, d_{NC} G}{2k_B T d_{Clay}}\right)^\frac{1}{3}

Solve for the velocity gradient.

.. math::   \Delta h =  \frac{G^\frac{4}{3} \nu}{g} \frac{2.3p C_{NC} \, \Lambda_{Clay}^2}{\pi k \, d_{Clay}} \left( \frac{3 \pi \,\mu  \, d_{NC} }{2k_B T d_{Clay}}\right)^\frac{1}{3}

.. math::

   \color{purple}{
     G_{coagulant, \, application} =  d_{Clay}\left(\frac{\pi k \,g\Delta h }{2.3p C_{NC} \, \Lambda_{Clay}^2 \nu} \right)^\frac{3}{4} \left( \frac{2k_B T }{3 \pi \,\mu  \, d_{NC} }\right)^\frac{1}{4}
   }

Table of :math:`G`, :math:`\varepsilon`, and :math:`h_L` for Different Geometries Derivations



These are the derivations for the equations that `appear in the table containing equations for :math:`G`, :math:`\varepsilon`, and :math:`h_L`. ### Straight pipe (wall shear) The average energy dissipation rate, :math:`\bar\varepsilon`, in a control volume with residence time :math:`\theta` is

.. math::  \bar\varepsilon = \frac{gh_{\rm{L}}}{\theta}

The residence time can be expressed as a function of length and average velocity.

.. math::  \theta = \frac{L}{\bar v}

For straight pipe flow the only head loss is due to wall shear and thus we have the Darcy Weisbach equation.

.. math::

   \color{purple}{
     h_{{\rm f}} = {{\rm f}} \frac{L}{D} \frac{\bar v^2}{2g}
     }

Combining the 3 previous equations we obtain the energy dissipation rate for pipe flow

.. math::

   \color{purple}{
     \bar\varepsilon = \frac{{\rm f}}{2} \frac{\bar v^3}{D}
   }

The average velocity gradient was defined by Camp and Stein as

.. math::  G_{CS} = \sqrt{\frac{\bar \varepsilon}{\nu}}

where this approximation neglects the fact that square root of an average is not the same as the average of the square roots.

.. math::

   \color{purple}{
     G_{CS} = \left(\frac{{\rm f}}{2\nu} \frac{\bar v^3}{D} \right)^\frac{1}{2}
   }

or in terms of flow rate, we have:

.. math::   G_{CS} = \left(\frac{\rm{32f}}{ \pi^3\nu} \frac{Q^3}{D^7} \right)^\frac{1}{2}

Straight Pipe Laminar
~~~~~~~~~~~~~~~~~~~~~

Laboratory scale apparatus is often limited to laminar flow where viscosity effects dominate. The equations describing laminar flow conditions always include viscosity. For the case of laminar flow in a straight pipe, we have:

.. math:: {\rm f} = \frac{64}{Re}

Reynolds number is defined as

.. math:: Re= \frac{\bar vD}{\nu}

The Darcy Weisbach head loss equation simplifies to the Hagen–Poiseuille equation for the case of laminar flow.

.. math::

   \color{purple}{
     h_{{\rm f}} = \frac{32\nu L\bar v}{gD^2}
     }

and thus the energy dissipation rate in a straight pipe under conditions of laminar flow is

.. math::

   \color{purple}{
     \bar\varepsilon =32\nu \left( \frac{\bar v}{D} \right)^2
   }

The Camp-Stein velocity gradient in a long straight laminar flow tube is thus

.. math::  G_{CS}^2 =32 \left( \frac{\bar v}{D} \right)^2

.. math::

   \color{purple}{
     G_{CS} =4\sqrt2 \frac{\bar v}{D}
   }

Our estimate of :math:`G_{CS}` based on :math:`\bar \varepsilon` is an overestimate because it assumes that the energy dissipation is completely uniform through the control volume. The true spatial average velocity gradient, :math:`\bar G`, for laminar flow in a pipe is (`Gregory, 1981<https://doi.org/10.1016/0009-2509(81)80126-1>`__),

.. math:: \bar G = \frac{8}{3}\frac{\bar v}{D}

Our estimate of :math:`G_{CS}` for the case of laminar flow in a pipe is too high by a factor of :math:`\frac{3}{\sqrt2}`.

As a function of flow rate we have

.. math::  \bar v=\frac{Q}{A} = \frac{4Q}{\pi D^2}

.. math::  G_{CS} =\frac{16\sqrt2}{\pi} \frac{Q}{D^3}

Parallel plates Laminar
~~~~~~~~~~~~~~~~~~~~~~~

Flow between parallel plates occurs in plate settlers in the sedimentation tank. We will derive the velocity gradient at the wall using the Navier Stokes equation.

  .. _Parallel_Plate_schematic:
  .. figure::    Images\Parallel_Plate_schematic.png
     :width: 700px
     :align: center
     :alt: Parallel plate schematic

     A fluid flowing from left to right due to a pressure gradient results in wall shear on the parallel plates. This flow profile is for the case when :math:`\frac{dp}{dx}` is negative.


We start with the Navier-Stokes equation written for flow in the x direction.

.. math:: \frac{y^2}{2} \frac{dp}{dx} + Ay + B = \mu u

where :math:`u` is the velocity in the x direction.

Apply the no slip condition at bottom plate.

.. math:: u=0 \quad at \quad y=0

Thus the constant :math:`B=0`.

Apply the no slip condition at top plate.

.. math:: u=0 \quad at \quad y=S

Thus the constant :math:`A = \frac{- S}{2} \frac{dp}{dx}`

Substitute the values for constants :math:`A` and :math:`B` into the original equation.

.. math:: \frac{y^2}{2} \frac{dp}{dx} - \frac{S}{2} \frac{dp}{dx} y = \mu \,u

Simply the equation to obtain

.. math:: u = \frac{y \left( y - S \right)}{2 \mu} \frac{dp}{dx}

We need a relationship between average velocity and :math:`\frac{dp}{dx}`. We can obtain this by integrating from 0 to
:math:`S`.

.. math::

   {\bar v } = \frac{q}{S}
   = \frac{1}{S}\int\limits_0^S u dy
   = \frac{1}{S} \int\limits_0^S
   \left(
     \frac{y^2 - S y}{2 \mu} \left( \frac{dp}{dx} \right)
   \right) dy

.. math:: \bar v = - \frac{S^2}{12 \mu} \frac{dp}{dx}

Solving for :math:`\frac{dp}{dx}`

.. math:: \frac{dp}{dx} = - \frac{12 \mu \bar v}{S^2}

From the Navier Stokes equation after integrating once we get

.. math:: \mu \,\left( \frac{du}{dy} \right) = y \frac{dp}{dx} + A

Substituting our boundary condition,
:math:`A = \frac{- S}{2} \frac{dp}{dx}` we obtain

.. math:: \frac{du}{dy}_{y = 0} = - \frac{S}{2 \mu} \frac{dp}{dx}

Substituting the result for :math:`\frac{dp}{dx}` we obtain

.. math:: \frac{du}{dy}_{y = 0} = \frac{6 \bar v}{S}

Therefore in velocity gradient notation we have

.. math:: G_{wall} = \frac{6 \bar v}{S}

The energy dissipation rate at the wall

.. math:: \varepsilon_{wall} = G_{wall}^2 \nu

.. math:: \varepsilon_{wall} = \left( \frac{6 \bar v}{S}\right)^2 \nu

Head loss due to shear on the plates is obtained from a force balance on a control volume between two parallel plates as shown in :numref:`Parallel_Plate_schematic`.

A force balance on a control volume gives

.. math:: 2 \tau L W = -\Delta P W S

.. math:: \Delta P = -\frac{2 \tau L}{S}

The equation relating shear and velocity gradient is

.. math:: \tau = \nu \rho \frac{du}{dy} = \nu \rho G

The velocity gradient at the wall is

.. math:: G_{wall} = \frac{6 \bar v}{S}

.. math:: \tau  = \nu \rho \frac{6 \bar v}{S}

Substituting into the force balance equation

.. math:: \Delta P = -\frac{2 \nu \rho 6 \bar v L}{S^2}

The head loss for horizontal flow at uniform velocity simplifies too

.. math:: h_{{\rm f}} = \frac{-\Delta P}{\rho g}

.. math::

   \color{purple}{
     h_{{\rm f}} = 12\frac{ \nu \bar v L}{gS^2}
     }

The average energy dissipation rate is

.. math::  \bar\varepsilon = \frac{gh_{\rm{L}}}{\theta}

.. math::

   \color{purple}{
     \bar\varepsilon = 12 \nu \left(\frac{  \bar v}{S} \right)^2
     }

The Camp-Stein velocity gradient for laminar flow between parallel plates is

.. math::

     \color{purple}{
     G_{CS} = 2\sqrt{3}\frac{  \bar v}{S}
     }

Coiled tubes (laminar flow)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Coiled tubes are used as flocculators at laboratory scale. The one shown below is a doubled coil. A single coil would only go around one cylinder

` <https://confluence.cornell.edu/display/AGUACLARA/Laminar+Tube+Floc?preview=/10422268/258146480/ReportLaminarTubeFlocSpring2014.pdf>`__


  .. _Tube_flocculator_AC:
  .. figure::    Images/Tube_flocculator_AC.JPG
     :width: 700px
     :align: center
     :alt: Parallel plate schematic

     The double coiled flocculator creates secondary currents that oscillate in direction. This may be helpful in creating much more mixing than would occur in a straight laminar flow pipe.

The ratio of the coiled to straight friction factors is given by `Mishra and Gupta <https://doi.org/10.1021/i260069a017>`__

The Dean number is defined as:

.. math:: De = Re\left(\frac{D}{D_c}\right)^\frac{1}{2}

where :math:`D` is the inner diameter of the tube and :math:`D_c` is the diameter of the coil. Note that the tubing coils are actually helixes and that for the tubing diameters and coil diameters used for flocculators that the helix doesn’t significantly change the radius of curvature.

.. math:: \frac{{\rm f}_{coil}}{{\rm f}} = 1 + 0.033\left(log_{10}De\right)^4

.. math:: h_{L_{coil}} = h_{{\rm f}} \left[ 1 + 0.033\left(log_{10}De\right)^4 \right]

where :math:`h_{{\rm f}} = \frac{32\nu L\bar v}{ g D^2}`. Note that we switch from major losses to total head loss here because the head loss from flowing around the coil is no longer simply due to shear on the
wall.

.. math::

     \color{purple}{
     h_{L_{coil}} = \frac{32\nu L\bar v}{ g D^2} \left[ 1 + 0.033\left(log_{10}De\right)^4 \right]
     }

The average energy dissipation rate is

.. math::

     \color{purple}{
     \bar\varepsilon = 32\nu \left( \frac{\bar v}{D} \right)^2 \left[ 1 + 0.033\left(log_{10}De\right)^4 \right]
     }

The average velocity gradient is proportional to the square root of the head loss and thus we obtain

.. math::


     G_{CS_{coil}} = G_{CS}\left[ 1 + 0.033\left(log_{10}De\right)^4  \right]^\frac{1}{2}

where :math:`G_{CS} =4\sqrt2 \frac{\bar v}{D}` for laminar flow in a straight pipe.

.. math::

   \color{purple}{
     G_{CS_{coil}} = 4\sqrt2 \frac{\bar v}{D}\left[ 1 + 0.033\left(log_{10}De\right)^4  \right]^\frac{1}{2}
   }

Expansions
~~~~~~~~~~

The average energy dissipation rate for a flow expansion really only has meaning if there is a defined control volume where the mechanical energy is lost. Hydraulic flocculators provide such a case because the same flow expansion is repeated and thus the mechanical energy loss can be assumed to happen in the volume associated with one flow expansion. In this case we have

.. math::

   \color{purple}{
     h_e =  K\frac{\bar v_{out}^2}{2g}
   }

In this equation :math:`K` represents the fraction of the kinetic energy that is dissipated.

If we define the length of the control volume (in the direction of flow) as :math:`H` then the residence time is

.. math:: \theta = \frac{H}{\bar v}

.. math::  \bar\varepsilon = \frac{gh_{\rm{e}}}{\theta}

Combining the previous equations we obtain

.. math::

   \color{purple}{
     \bar\varepsilon = K\frac{\bar v_{out}^3}{2H}
   }

.. math:: G_{CS} = \sqrt{\frac{\bar \varepsilon}{\nu}}

.. math::

   \color{purple}{
     G_{CS} = \bar v_{out}\sqrt{\frac{K\bar v_{out}}{2H\nu}}
   }

**Maximum velocity gradients**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Straight pipe (major losses)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The maximum velocity gradient in pipe flow occurs at the wall. This is true for both laminar and turbulent flow. In either case a force balance on a control volume of pipe gives us the wall shear and the wall shear can then be used to estimate the velocity gradient at the wall.


  .. _pipe_pressure_shear_force_balance:
  .. figure:: Images/pipe_pressure_shear_force_balance.png
      :width: 400px
      :align: center
      :alt: Pipe pressure and shear force balance

      A fluid flowing from left to right due to a pressure gradient results in wall shear.

A force balance for the case of steady flow in a round pipe requires that sum of the forces in the x direction must equal zero. Given a pipe with diameter, D, and length, L, we obtain

.. math::  \left(P_{in}- P_{out}\right)\frac{\pi D^2}{4} = \tau_{wall} \pi D L

.. math::  -\Delta P\frac{D}{4} = \tau_{wall} L

For this control volume the energy equation simplifies to

.. math:: -\Delta P=\rho g h_{{\rm f}}

The relationship between shear and velocity gradient is

.. math:: \tau_{wall} = \mu \frac{du}{dy}_{wall} = \nu \rho G_{wall}

Combining the energy equation, the force balance, and the relationship between shear and velocity gradient we obtain

.. math::  \rho g h_{{\rm f}}\frac{D}{4} = \nu \rho G_{wall} L

.. math::  G_{wall} = \frac{g h_{{\rm f}}D}{4\nu L}

This equation is valid for both laminar flow. For turbulent flow it is necessary to make the approximation that wall shear perpendicular to the direction of flow is insignificant in increasing the magnitude of the wall shear. We can substitute the Darcy Weisbach equation for head loss to obtain

.. math::

   \color{purple}{
     G_{wall} ={\rm f}  \frac{\bar v^2}{8\nu}
   }

The energy dissipation rate at the wall is

.. math:: \varepsilon_{wall} = G_{wall}^2 \nu

.. math::

   \color{purple}{
     \varepsilon_{wall} = \frac{1}{\nu}\left({\rm f}  \frac{\bar v^2}{8} \right)^2
     }

For laminar flow we can substitute :math:`{\rm f} = \frac{64}{{\rm Re}}` and the definition of the Reynolds number to obtain

.. math::

   \color{purple}{
     G_{wall} =  \frac{8\bar v}{D}
   }

This equation is useful for finding the velocity gradient at the wall of a tube settler.

The energy dissipation rate at the wall is

.. math:: \varepsilon_{wall} = G_{wall}^2 \nu

.. math::

   \color{purple}{
     \varepsilon_{wall} = \left(\frac{8\bar v}{D} \right)^2 \nu
     }

.. _coiled-tubes-laminar-flow-1:

Coiled tubes (laminar flow)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The shear on the wall of a coiled tube is not uniform. The outside of the curve has a higher velocity gradient than the inside of the curve and there are secondary currents that results in wall shear that is not purely in the locally defined upstream direction. We do not have a precise equation for the wall shear. The best we can do currently is define an average wall shear in the locally defined direction of flow by combining
:math:`G_{{CS}_{wall_{coil}}} =\rm{f_{coil}} \frac{\bar v^2}{8\nu}` and
:math:`{\rm f}_{coil} = {\rm f} \left[ 1 + 0.033\left(log_{10}De\right)^4 \right]`
to obtain

.. math::

   \color{purple}{
     G_{{CS}_{wall_{coil}}} ={\rm f} \left[ 1 + 0.033 \left(log_{10}De \right)^4 \right]  \frac{\bar v^2}{8\nu}
   }

.. _expansions-1:

Expansions
~~~~~~~~~~

Flow expansions are used intentionally or unavoidable in multiple locations in hydraulically optimized water treatment plants. Rapid mix and hydraulic flocculation use flow expansions to generate fluid mixing and collisions between particles.

Round jet
~~~~~~~~~


`Baldyga, et al. 1995 <https://doi.org/10.1016/0009-2509(95)00049-B>`__

.. math:: \varepsilon_{Centerline} = \frac{50 D_{Jet}^3 \bar v_{Jet}^3}{ \left( x - 2 D_{Jet} \right)^4}



.. math::  \varepsilon_{Max} = \frac{\left( \frac{50}{\left( 5 \right)^4} \right) \bar v_{Jet}^3}{D_{Jet}}

.. math::

   \color{purple}{
     \varepsilon_{Max} = \Pi_{RoundJet} \frac{\bar v_{Jet} ^3}{D_{Jet}}
     }

.. math:: \Pi_{RoundJet} = 0.08

The maximum velocity gradient in a jet is thus

.. math::

   \color{purple}{
     G_{Max} = \bar v_{Jet} \sqrt{\frac{\Pi_{RoundJet} \bar v_{Jet} }{\nu D_{Jet}}}
     }

Below we plot the Baldyga et al. equation for the energy dissipation rate as a function of distance from the discharge location for the case of a round jet that is discharging into a large tank.


`.. plot:: Rapid_Mix/plots/Jet_EDR.py`
   `:include-source:`

   .. _Jet_centerline_EDR:
   .. figure:: Images/Jet_centerline_EDR.png
       :width: 400px
       :align: center
       :alt: Pipe pressure and shear force balance

       The centerline energy dissipation rate downstream from a round jet. The distance downstream is measured in units of jet diameters. The energy dissipation rate between the jet and 7 jet diameters is developing as the shear between the stationary fluid and the jet propagates toward the center of the jet and turbulence is generated.

Plane Jet
~~~~~~~~~

Plane jets occur in hydraulic flocculators and in the sedimentation tank inlet jet system. We haven’t been able to find a literature estimate of the maximum energy dissipation rate in a plane jet. Original measurements of a plane turbulent jet have been made by `Heskestad in 1965 <http://dx.doi.org/10.1115/1.3627309>`__ and it may be possible to use that data to get a better estimate of $:raw-latex:`\Pi`\_{JetPlane} $ from that source.

.. math:: \Pi_{\bar \epsilon}^{\epsilon_{Max}} = \frac{\varepsilon_{Max}}{\bar \varepsilon}

.. math::

   \color{purple}{
     \varepsilon_{Max} = \Pi_{JetPlane}  \frac{  \bar v_{Jet} ^3}{S_{Jet}}
     }

The maximum velocity gradient is thus

.. math::

   \color{purple}{
     G_{Max} = \bar v_{Jet}\sqrt{\frac{\Pi_{JetPlane} \bar v_{Jet}}{\nu S_{Jet}}}
     }

.. math:: \bar v = \frac{Q}{SW}

.. math:: \bar v_{Jet} = \frac{\bar v}{\Pi_{VCBaffle}}

.. math:: S_{Jet} = S \Pi_{VCBaffle}

The average hydraulic residence time for the fluid between two baffles
is

.. math:: \theta_B = \frac{H}{\bar v}

where :math:`H` is the depth of water. Substituting into the equation for :math:`\varepsilon_{Max}` to get the equation in terms of the average velocity :math:`\bar v` and flow dimension :math:`S`

.. math:: \varepsilon_{Max}= \frac{\Pi_{JetPlane}}{S \Pi_{VCBaffle}} \left( \frac{ \bar v}{\Pi_{VCBaffle}} \right)^3

From the control volume analysis the average energy dissipation rate is

.. math:: \bar \varepsilon = K \frac{\bar v^2}{2} \frac{1}{\theta_B} = \frac{K}{2} \frac{\bar v^3}{H_e}

where :math:`K` is the minor loss coefficient for flow around the end of a baffle with a :math:`180^\circ` turn.

Substitute the values for :math:`\bar \varepsilon` and
:math:`\varepsilon_{Max}` to obtain the ratio,
:math:`\Pi_{\bar \epsilon}^{\epsilon_{Max}}`

.. math:: \Pi_{\bar \epsilon}^{\epsilon_{Max}} = \frac{\Pi_{JetPlane}}{\Pi_{VCBaffle}^4} \frac{2 H_e}{K S}

:math:`\Pi_{\bar \varepsilon}^{\varepsilon_{Max}}` has a value of 2 for
:math:`H_e/S<5` (CFD analysis and `Haarhoff, 2001 <https://search-proquest-com.proxy.library.cornell.edu/docview/1943098053?accountid=10267>`__)
The transition value for :math:`H_e/S` is at 5 (from CFD analysis, our weakest assumption).

We also have that :math:`\Pi_{\bar \varepsilon}^{\varepsilon_{Max}}` has a value of
:math:`\frac{\Pi_{JetPlane}}{\Pi_{VCBaffle}^4} \frac{2 H_e}{K S}` for
:math:`H_e/S>5`. Thus we can solve for :math:`\Pi_{JetPlane}` at
:math:`H_e/S=5`

.. math::

   \Pi_{JetPlane} = \left(
     \Pi_{\bar \epsilon}^{\epsilon_{Max}} \Pi_{VCBaffle}^4 \frac{K}{2} \frac{S}{H_e}
     \right)

.. math:: \Pi_{JetPlane} = 0.0124

.. code:: python

    x=con.RATIO_VC_ORIFICE**2
    Ratio_Jet_Plane = 2*con.RATIO_VC_ORIFICE**8 * con.K_MINOR_FLOC_BAFFLE/2/5
    Ratio_Jet_Plane

    con.RATIO_VC_ORIFICE**8*con.K_MINOR_FLOC_BAFFLE/Ratio_Jet_Plane

Behind a flat plate
~~~~~~~~~~~~~~~~~~~

A flat plate normal to the direction of flow could be used in a hydraulic flocculator. In vertical flow flocculators it would create a space where flocs can settle and thus it is not a recommended design.

The impellers used in mechanical flocculators could be modeled as a rotating flat plate. The energy dissipation rate in the wake behind the flat plate is often quite high in mechanical flocculators and this may be responsible for breaking previously formed flocs.

Ariane Walker-Horn modeled the flat plate using Fluent in 2015.

Figure x. The energy dissipation rate and streamlines for a 1 m wide plate in two dimensional flow with an approach velocity of :math:`1 m/s`. The maximum energy dissipation rate was approximately :math:`0.04 W/kg`.

.. math::

   \color{purple}{
     \varepsilon _{Max} = \Pi_{Plate}\frac{\bar v^3}{W_{Plate}}
     }

The maximum velocity gradient is thus

.. math::

   \color{purple}{
     G_{Max} = \bar v\sqrt{\frac{\Pi_{Plate} \bar v}{\nu W_{Plate}}}
     }

.. math:: \Pi_{Plate} = \frac{ \left( \varepsilon_{Max} W_{Plate} \right)}{\bar v^3}

.. code:: python

    """CFD analysis setup used by Ariane Walker-Horn in 2015"""
    EDR_Max = 0.04*u.W/u.kg
    v = 1*u.m/u.s
    W = 1*u.m
    Ratio_Jet_Plate = (EDR_Max * W/v**3).to_base_units()
    print(Ratio_Jet_Plate)
