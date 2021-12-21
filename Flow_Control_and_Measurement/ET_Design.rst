.. _title_entrance_tank_design:

**************************************
Entrance Tank Design
**************************************

The water treatment plant must be protected from potentially damaging materials that could be carried from the watershed to the plant by the water. Typically there will be a large opening trash rack at the water source to prevent damage to the transmission line that carries water to the plant. There may also be a small sedimentation tank to remove sand and gravel before the water enters the transmission line. The trash rack and removal of sand and gravel is important for protection of the water treatment plant, but these protections are generally not sufficient. Excessive grit has historically caused maintenance challenges in some AguaClara plants by settling in the flocculator and the channel leading the sedimentation tanks. Steep mountain streams often overwhelm the sand and gravel removal system during storm events and thus depending on the watershed characteristics additional protection is required at the water treatment plant.  

The specific design characteristics of a water treatment plant dictate the potential failure modes and hence the required protection.

The entrance tank has multiple functions in a drinking water treatment plant.

#. Remove air bubbles to reduce splashing, turbulence, and unsteady motion of the chemical feed surface tracking lever system
#. Remove grit to prevent grit accumulation in the flocculator
#. Remove leaves and other debris to prevent clogging of the diffusers in the sedimentation tank inlet
#. Dissipate kinetic energy of the water prior to facilitate accurate measurement of the water level used for flow measurement
#. Measure the flow rate so that operators can make adjustments to the incoming flow rate and respond to changes in water demand
#. Inject the coagulant and any other amendments required for flocculation

As shown in Figure _, the entrance tank consists of several components: an influent pipe, a trash rack, an overflow pipe to prevent flows larger than the design flow rate from overwhelming the plant, the Liner Flow Orifice Meter (LFOM), and depending on the water quality characteristics, a grit chamber. The Chemical Dose Controller (CDC) lever arm and float sit between the trash rack and the LFOM. 

In some AguaClara plants, the entrance tank, flocculators, and sedimentation tanks are separated by walkways. However, a more space efficient approach would be to arrange the entrance tank in a channel next to the flocculator as shown in figure _ (emw - figure out how to link). This avoids the need for buried pipes to carry water underneath the walkway from one component to the other and simplifies construction. 

 .. _figure_Plant_Layout_Option: (emw_add image to folder https://github.com/Emily-Wood/AguaClara/blob/master/Plant%20Layout%20Option%202.PNG?raw=true)

.. figure:: ../Images/ET_Diagram_Labeled.png
    :width: 900px
    :align: center
    :alt: Layout of entrance tank alongside plant treatment train

    A space efficient layout of the entrance tank alongside the flocculators. The entrance tank may extend the full length of the flocculator and then get wider as needed to meet grit removal requirements. 

Trash Rack Design
===============================

The trash rack is specifically designed to remove low density debris that could easily be carried through the plant and clog any small flow passages. In an AguaClara plant there are critical flow passages in the sedimentation tank inlet manifold diffusers and in the flow injection system in the stacked rapid sand filters. The inlet manifold diffusers have flared nozzles which currently have a minimum dimension of about 4 mm. This sets a requirement that the opening dimension for the trash rack be less than the opening size of the inlet manifold nozzles.

The minimum trash rack area is set by a goal of minimizing head loss through the plant while maintaining a trash rack size that is reasonably compact. We recommend that the trash rack be designed to reach a terminal head loss of 5 cm when it is 90% clogged. The design follows directly from that constraint. The guiding equation is the orifice equation with the simple addition of the fractions of the area that is actually available for the water to flow through the trash rack. The area is reduced by the porosity, the vena contracta, and the clogging.

.. math::
  :label: trashrack_flow

   Q = (1-\Pi_{clogged})\Pi_{vc} \phi A_{trashrack}\sqrt{2gh}

where :math:`\phi_{trashrack}` is the fraction of clean trash rack that is open, :math:`\Pi_{vc}` is the vena contracta coefficient, :math:`\Pi_{clogged}` is the clogged fraction of the trash rack. The ideal trash rack has a high porosity and a large vena contracta coefficient. The vena contracta coefficient is set by the geometry of the entrance into the opening through the trash rack. If the entrance has a sharp edge, then the vena contract coefficient will have a value of approximately 0.62. If the entrance is rounded then the vena contracta could approach 1.0. Thus the idea trash rack will have rounded openings.

Solve for the area of the trash rack

.. math::
  :label: trashrack_area

   A_{trashrack} = \frac{Q}{(1-\Pi_{clogged})\Pi_{vc} \phi \sqrt{2gh}}

Set the fraction clogged to between 80 and 90%. Vena contracta coefficient is 0.62 for sharp edged orifices and could be 1 for round wire.
Porosity varies widely depending on the fabrication method.
For AguaClara plants recommend a head loss of 5 cm max.

Also of interest is the effective velocity taking into account the whole area of the trash rack.

.. math::
  :label: trashrack_velocity

   v_{trashrack} = \frac{Q}{A_{trashrack} } = (1-\Pi_{clogged})\Pi_{vc} \phi \sqrt{2gh}

The trash rack characteristic velocity is 50 mm/s for 50% porosity, 90% clogged, vena contracta of 1 and a maximum head loss of 5 cm.

Grit Chamber Design
===============================

The length of the entrance tank may be extended to function as additional grit removal capacity for watersheds where sediment has the potential to produce harmful amounts of sand and gravel during storm events. As of 2021, plant operators at only two AguaClara plants, Gracias and Agalteca, have reported maintenance issues due to grit carryover. The grit chamber is located on the effluent side of the trash racks and is lined with a series of hoppers to faciliate cleaning. To remove settled grit from the entrance tank, the plant operator can remove the pipe stub blocking the drain at the bottom of each hopper, allowing water to pull the grit into the drain channel below. 

The entrance tank can be treated as a grit chamber to capture large particles, preventing them from settling in the flocculator or inlet channel to the sedimentation tank. In this calculation we will use 0.1 mm as the critical particle size, as recommended by Kawamure (pg. 416) [emw - need to site this]. The overall strategy to determine appropriate dimensions of the entrance tank is follows: 

With the addition of a grit chamber to the design, it is possible that the entrance tank will extend to the full length of a flocculator channel and then get wider to meet its minimum plan-view area requirement.

1. Use the appropriate Stokes Law for laminar or turbulent flow to determine the corresponding critical velocity of the particle. (See this chapter for a review on Stokes law) [emq - link to fluids chapter]
2. Calculate the required plan-view area of the entrance tank
3. Determine the ideal length and width of the entrance tank
4. Calculate the required entrance tank depth

Recall that Stokes Law tells us the terminal veloctity of a particle settling under laminar flow, and can be calculated as follows: 

.. math::
  :label: grit_criticalVelocity
  
  v_c = ((rho_p - rho_H20)*ac.GRAVITY*d_p**2)/(18*nu*rho_H20)
  
  where d\ :sub:'p' is the minimum particle diameter to be removed (Kawamura recommends 0.1 mm). 
  
  As a check, calculate the Reynolds number to confirm that flow is in the laminar regime for Stokes' Law to be valid
  
  .. math::
  :label: grit_Re
  
  Re = v_c*d_p/nu
  
  The required plan view area to capture the minimum particle size is:
  
   .. math::
  :label: planViewA
  
  A = Q/v_c
  
  The next step is to determine the optimal dimensions of the entrance tank. For constructibility purposes, the entrance tank must not be smaller than 50 cm. Here we will assume that the entrance tank is the same length as the flocculator for ease of construction; however designing to minimize the plan view area of the entrance tank is another valid assumption. 
  
   .. math::
  :label: width_ET
  
  w_ET = max(area/length_flocculator, w_min)
  
  We previosuly calculated the active area of the trash rack, and so the required depth of the entrance tank is the active area of the trash rack divided by the entrance tank width, with additional freeboard added. 
  
 Grit Chamber Hopper Design
===============================

The minimum slope of each hopper is determined by the angle of repose for wet sand (approximately 45 degrees). 

 Drain Channel Design
===============================

When a plant operator removes the pipe stubs in the hoppers, water and grit drain from the entrance tank and empty into a concrete channel. This channel has a sloped bottom to encourage grit to flow towards the exit. The size and slope of this channel has been arbitrarily chosen in the Onshape design for demonstration purposes. These parameters should be defined explicitly after considering implications for construction and maintenance. There is concern that a narrow drain channel would be difficult to construct if a person cannot fit inside. The drain channel could be replaced with a large pipe buried in the ground and connected to the hopper drains by vertical PVC pipes. 

 Linear Flow Orifice Meter (LFOM)
===============================

The LFOM is located at the very end of the entrance tank. It is supported by concrete in the shape of an inverted L. Below the LFOM, there is a port in the concrete which allows water to flow to the flocculator. The length of the LFOM pipe and the height of its supported concrete can be adjusted to facilitate easier fabrication. See [insert chapter] for LFOM design.

 Overflow Pipe Design
===============================


###############################

Below is content that still needs to be organized:

###############################

Determine the required entrance tank depth

# Calculate the trash rack approach velocity assuming a trash rack made with parallel wires
S = 0.005 * u.m # trash rack opening size
D = 0.002 * u.m # trash rack wire diameter
PO_pi = 0.80 # the fraction of trash rack openings that are clogged when the trash rack is at its maximum allowable clogging and headloss
HL_max = 0.05 * u.m # the maximum headloss allowed in the trash rack due to clogging
PO = S / (D + S) # clean trashrack porosity given opening size and wire diameter
V = (1 - PO_pi) * PO * (2* ac.GRAVITY * HL_max)**0.5 # Approach velocity for the trash racks

# Calculate the required entrance tank depth
A = q/V
depth = A/w_ET
print('The required entrance tank depth is ', depth)

----------------------------

## Example 4: Analyze the Kinetic Energy in the Entrance Tank at the Gracias, Honduras Plant

# Initialization: Run this code block first
!pip install aguaclara
from aguaclara.core.units import unit_registry as u
import aguaclara as ac
import numpy as np

# global variables
q = (60 * u.L/u.s).to(u.m**3/u.s)
T = 20 * u.degC
rho_H20 = ac.density_water(T)
rho_p = 2650 *u.kg/u.m**3 # density of sand
nu = ac.viscosity_kinematic_water(T) # kinematic viscosity
mu = nu*rho_H20 # dynamic viscosity of 
w_flocculator = 0.60 * u.m # the width of one flocculator at Gracias (inner width ie. does not include thickness of the concrete)
length_flocculator = 7.10 * u.m # the length of one flocculator channel at Gracias (inner length ie. does not include thickness of the concrete)
depth_flocculator = 2.17 * u.m  # at Gracias (flocculator design code say 2.08)

### Calculate the kinetic energy and velocity exiting the influent pipe at Gracias
ID = 0.2 * u.m # inner diameter of influent pipe at Gracias
a = 0.25*np.pi*ID**2
v_influent = q/a
KE_influent = v_influent**2/(2*ac.GRAVITY)

print('The velocity exiting the influent pipe is ', v_influent)
print('The kinetic energy exiting the influent pipe is ', KE_influent.to(u.cm))

