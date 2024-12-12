.. raw:: html

    <embed>
       <link rel="canonical" href="https://aguaclara.github.io/Textbook/Filtration/EStaRS_Design.html" />
       <script src="https://hypothes.is/embed.js" async></script>
    </embed>

.. _title_estars:

*****************************************
Enclosed Stacked Rapid Sand Filter Design
*****************************************



The Enclosed Stacked Rapid Sand filter, EStaRS, is a compact filter built inside a rectangular tank. Open Stacked Rapid Sand, OStaRS, construction methods require that a person be able to work inside the filter to finish the waterproofing of the concrete walls and to install the pipe modules for the inlets and outlets. The minimum filter area for OStaRS is approximately 1 square meter. Given a backwash velocity of 11 mm/s that corresponds to a minimum flow of about 11 L/s. It is always best to have at least 2 filters operating in parallel so that the filters can be backwashed when the plant is operating at less than 50% of the design flow rate. Thus EStaRS filters will be used for plants with flows less than about 20 L/s.

The first EStaRS filters were built in corrugated pipes. Previous problems with EStaRS filters included air entrainment and fabrication problems with the filter internal piping. Corrugated pipes that are available for filter body diameters greater than 60 centimeters that are available in Honduras have very thin inner walls that are not thick enough for strong welds. This requires use of a gasket seal for passing the trunk lines through the filter body. The corrugated pipes are also more difficult to attach the required end caps on the filter body. For these reasons we do not recommend using corrugated pipes for the filter body. 

Air entrainment may be a problem in the inlet pipes. If air is carried into the filter the head loss through the filter will increase rapidly. Byron Zuniga reports that he was unable to get an effective backwash at the San Juan Guarita plant based on the observation that the head loss increased rapidly after backwash even though there was no evidence of turbidity release during backwash. This observation is consistent with air being entrained in the inlet pipes and carried into the filter where it rapidly fills the pores of the sand and thus prevents water from flowing through those pores. It isn't known how this problem was resolved. A possible solution to air entrainment is to design the inlet pipes to act like tube settlers so that the air can return to the inlet tank.

The 4 corrugated pipe EStaRS that were in operation in Central America as of 2021 have winged pipes with orifices for the inlets. There are no reports of problems with sand entering the inlet pipes and thus that appears to be a success. This does require the use of a gate valve for the backwash pipe to ensure that the transition from backwash to filtration mode doesn't happen too quickly. During this transition there is reverse flow from the filter into the inlet pipes and if that flow rate is too high it could carry sand into the inlet branches.

Air venting from trunks
=======================

The trunks are initially filled with air.
The trunks must have a water seal to ensure that air is never sucked into the filter during backwash.
The trunk entry into the filter body is thus at a local high point and air that accumulates in the top of the trunk and the top of the branches has no way to get out except by flowing into the sand. It is not yet know if this is a problem or if the initial venting into sand is sufficient.

Vent options
------------

If the air in the high points of the inlet and outlet piping is determined to be a problem, here are possible solutions.

 #. tube straight up to top of inlet tank (will suck air during backwash)
 #. tube that connects into the top of the filter body (during filtration air will travel up the tubes and vent into the top of the filter body. During backwash water will take this shortcut to bypass the sand. It could work if the tubes are small enough that the bypass during backwash is small)
 #. Use sloped section of trunk line to act as tube settler to remove bubbles that are entrained in the inlet. This doesn't solve the problem of air that is in the local high spot of trunks.

If a vent is needed it seems that the only option is to connect air release tubes to the top of the filter.

Elevation considerations
========================

The head loss through the sand during backwash is equal to the settled depth of sand. This means that the water level in the top inlet pipe will drop by an amount equal to the depth of the sand. That means that the bottom of the inlet tank must be ABOVE the top of the sand + the OD of the trunk + head loss in the backwash trunk inlet.

Rectangular tank
================

As of 2024 the best option for fabricating EStaRS filters seems to be from HDPE sheets welded together to create rectangular tanks. The rectangular tank option eliminates the challenges of providing support to the branches in the round EStaRS.

Structural analysis
-------------------

Sheet span
^^^^^^^^^^

The structural analysis begins by estimating the maximum distance between support rings, :math:`B_{ring}`, for a sheet of material that is exposed to a constant pressure. An arbitrary width section of the sheet is analyzed as if it were a simple beam. The moment of inertia, :math:`I`, for a rectangle is

.. math::
  :label: I_for_rectangle

   I = \frac{1}{12} bT_{sheet}^3

where 
 * :math:`b` is the arbitrary width of the sheet, 
 * :math:`T_{sheet}` is the sheet thickness. 

The maximum bending moment :math:`M` at the midpoint of a uniformly loaded beam with load :math:`w` per unit length and span :math:`B_{ring}` is:

.. math::
  :label: M_for_sheet

   M= \frac{wB_{ring}^2}{8}

where 
 * :math:`w` = total load per unit length due to water pressure
 * :math:`B_{ring}` = unsupported span of the beam.

The total load per unit length is given by 

.. math::
  :label: uniform_P_load

   w = Pb

where
 * :math:`P` = pressure obtained from statics
The stress in the beam is given by:

.. math::
  :label: stress_for_beam

   \sigma = \frac{Mc}{I}

where:
 * :math:`c` = distance to the outermost fiber from the neutral axis
For a sheet we have:

.. math::
  :label: sheet_distance_outermost_fiber

   c = \frac{T_{sheet}}{2}

The stress in the sheet can be obtained by substituting equations :eq:`I_for_rectangle`, :eq:`M_for_sheet`, :eq:`uniform_P_load`, :eq:`sheet_distance_outermost_fiber` into :eq:`stress_for_beam` to obtain:
 
.. math::
  :label: stress_for_beam2

   \sigma = \frac{\frac{T_{sheet}}{2}}{\frac{1}{12} bT_{sheet}^3} \frac{PbB_{ring}^2}{8}

As expected the arbitrary width of the beam section of the wall drops out of the equation. Simplifying we obtain:

.. math::
  :label: stress_for_beam3

   \sigma = \frac{3PB_{ring}^2}{4T_{sheet}^2}

The maximum span, :math:`B_{ring}`, is thus

.. math::
  :label: max_ring_B

   B_{ring_{max}} = T_{sheet}\sqrt{\frac{4 \sigma}{3P}}

Equation  :eq:`max_ring_B` sets the maximum distance between support rings for a tank. 

Maximum unsupported depth
^^^^^^^^^^^^^^^^^^^^^^^^^

The maximum depth of water not requiring a support ring can be calculated by replacing the pressure term with the depth of water and solving equation :eq:`max_ring_B` for the depth of water. In this case the beam length, :math:`B_{ring_{max}}`, is equal to the tank width, :math:`W_{tank}`.

.. math::
  :label: max_unsupported_width

   W_{tank} = T_{sheet}\sqrt{\frac{4 \sigma}{3\rho g H_{water}}}

Solving equation :eq:`max_unsupported_width` for the water depth we obtain:

.. math::
  :label: max_unsupported_depth

   H_{water} =  \frac{4 \sigma T_{sheet}^2}{3\rho g W_{tank}^2}

Support rings
^^^^^^^^^^^^^

The support rings will extend around the perimeter of the filter. Each support ring carries the load based on the pressure at the ring elevation. That pressure is applied over the spacing of the support rings to create the load per length of the beam. 


.. math::
  :label: I_for_beam

   I = \frac{1}{12} W_{beam}H_{beam}^3

where 
 * :math:`W_{beam}` is the width of the beam, 
 * :math:`H_{beam}` is the beam height. 

The maximum bending moment, :math:`M`, at the midpoint of a uniformly loaded beam with load, :math:`w`, per unit length and span, :math:`W_{tank}`, is:

.. math::
  :label: M_for_beam

   M= \frac{wW_{tank}^2}{8}

where 
 * :math:`w` = total load per unit length due to water pressure
 * :math:`W_{tank}` = unsupported span of the beam.

The total load per unit length is given by 

.. math::
  :label: ring_uniform_P_load

   w = PB_{ring}

where:
 * :math:`B_{ring}` = the center to center spacing of the beams


For a beam the distance to the outermost fiber from the centroid is:

.. math::
  :label: beam_distance_outermost_fiber

   c = \frac{H_{beam}}{2}

The stress in the ring beam can be obtained by substituting equations :eq:`I_for_beam`, :eq:`M_for_beam`, :eq:`ring_uniform_P_load`, :eq:`beam_distance_outermost_fiber` into equation :eq:`stress_for_beam` to obtain:
 
.. math::
  :label: stress_for_ring_beam_mess

   \sigma = \frac{\frac{H_{beam}}{2}}{\frac{1}{12} W_{beam}H_{beam}^3} \frac{PB_{ring}W_{tank}^2}{8}

Simplifying equation :eq:`stress_for_ring_beam_mess` we obtain:

.. math::
  :label: stress_for_ring_beam

   \sigma = \frac{3 P B_{ring} W_{tank}^2}{4 W_{beam} H_{beam}^2}

The most efficient use of material would be to make this ring beam as tall as possible. The minimum thickness of the beam could be the sheet thickness used for the tank. Begin by solving for the beam height, :math:`H_{beam}`.

.. math::
  :label: ring_beam_height

    H_{beam}=  W_{tank} \sqrt{\frac{3 P B_{ring} }{4 W_{beam} \sigma}} 

If the beam height is limited by other constraints then we can increase the beam width,  :math:`W_{beam}`.

.. math::
  :label: ring_beam_width

   W_{beam} = \frac{3 P B_{ring} W_{tank}^2}{4 \sigma H_{beam}^2}

Solution strategy
-----------------

Beginning at the bottom of the filter:

 #. Calculate the pressure at the very bottom taking into account that the sand water mix has a specific gravity of approximately 2 for silica sand with a porosity of 0.4.
 #. Use equation :eq:`max_ring_B` to find the maximum ring spacing. Determine a ring spacing that can fit between inlet and outlet pipes.
 #. Determine the actual elevation of the first ring.
 #. Calculate the pressure at the elevation of the first ring.
 #. Use equation :eq:`ring_beam_height` to find the required ring beam height.
 #. If necessary double or triple the beam thickness based on equation  :eq:`ring_beam_width`.
 
 Repeat calculations for each subsequent ring beam until you reach the location where no ring supports are needed as defined by equation :eq:`max_unsupported_depth`.
