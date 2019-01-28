***************************
Flocculation Model Solution
***************************

.. code:: python

  import aguaclara.core.physchem as pc
  from aguaclara.core.units import unit_registry as u

  import aguaclara.research.floc_model as fm

  import numpy as np
  import matplotlib.pyplot as plt



.. todo:: Review this file after the new AguaClara code is released.

Many of the fractal floc equations are available in the ``floc_model.py`` file in the aguaclara repository. Look through ```floc_model.py`` <https://github.com/AguaClara/aguaclara/blob/master/aguaclara/research/floc_model.py>`_ within the aguaclara repository. The following constants are defined in that file. NTU has been defined as an approximate empirical relationship between the concentration of kaolin clay and the turbidity, such that 1 NTU is equivalent to 1.7 mg/L. The diameter of a primary clay particle is assumed to be 7 micrometers. The fractal dimension for flocs is defined as ``DIM_FRACTAL`` and is equal to 2.3. We are using PACl as a coagulant for this analysis, so you shall call ``fm.PACl``, when a function within ``floc_model.py`` requires ‘coag’ as an input.

Whenever possible, use variables defined within ``floc_model.py`` instead of redefining them. Relevant variables defined in ``floc_model.py`` include: 1. ``DIM_FRACTAL`` with an estimated value of 2.3.

1. ``PACl``
2. ``Clay``


1)
~~~

Estimate the diameter of the flocs that interact with the tip of the impeller of the mechanical flocculator analyzed above. We don’t yet have a good model to predict maximum floc size as a function of velocity gradient or energy dissipation rate. We have a rough estimate, ``fm.diam_floc_max(EDRmax)`` based on a small amount of data.

.. code:: python

    ratio_prop_vel = 0.75
    pi_plate = 0.04
    vel_prop = 3 * u.ft/u.s
    height_prop = 3 * u.cm

    ed_rate_prop_max = pi_plate * ((ratio_prop_vel *  vel_prop)**3 / height_prop).to(u.mW/u.kg)

    #answer
    diam_floc_mech = fm.diam_floc_max(ed_rate_prop_max).to(u.um)
    print('The diameter of the flocs that interact with the impeller is', diam_floc_mech, '.')
    x=fm.DIM_FRACTAL
    x
The diameter of the flocs that interact with the impeller is 127 um.


2)
~~~

Estimate the terminal sedimentation velocity in mm/s of the flocs that interact with the tip of the impeller of the mechanical flocculator analyzed above. Use the function ``fm.vel_term_floc``. You may assume that the flocs were made from a particle suspension that had 1.5 mg/L of aluminum and 100 NTU of clay.

Note: AguaClara has defined the unit NTU as ``u.NTU``.

.. code:: python

    #answer
    conc_Al = 1.5 * u.mg/u.L
    conc_clay=100*u.NTU
    vel_term_floc_tip = fm.vel_term_floc(conc_Al, conc_clay, fm.PACl,
                                           fm.Clay, fm.DIM_FRACTAL,
                                           diam_floc_mech, temp_design).to(u.mm/u.s)

    print('The terminal velocity of flocs that interact with the impeller tip is estimated to be', vel_term_floc_tip)

The terminal velocity of flocs that interact with the impeller tip is estimated to be 0.738 mm/s


3)
~~~

Would these flocs be captured by a conventional design for a sedimentation tank `(10 State Standards) <http://10statesstandards.com/waterrev2012.pdf>`__ with a capture velocity of 1.2 m/hr? The capture velocity is a property of the sedimentation tank. If the floc settles faster than the capture velocity, then theoretically the floc will be captured by the sedimentation tank.

.. code:: python

    #answer
    vel_capture_10_state = (1.2 * u.m/u.hr).to(u.mm/u.s)
    print('The 10 State Standards capture velocity is', vel_capture_10_state)
    print("The 10 State Standards sedimentation tank would capture the flocs that are able to survive the energy dissipation rate at the tip of the propeller. ")

The 10 State Standards capture velocity is 0.333 mm/s
The 10 State Standards sedimentation tank would capture the flocs that are able to survive the energy dissipation rate at the tip of the propeller.

These flocs would be removed easily in an AguaClara sedimentation tank (capture velocity of 0.12 mm/s). However, our use of the empirical equation to predict the size of these flocs is questionable because we are extrapolating way beyond the original data. We need more experiments to characterize the size of flocs as a function of the velocity gradient.

4)
~~~

Estimate the average distance between primary clay particles at the beginning and end of flocculation given an initial turbidity of 100 NTU and a target effluent unflocculated clay concentration at the end of flocculation of less than 1 NTU. Of course, the clay concentration is actually constant in flocculation since particles are not actually being removed. But here we are referring to the primary clay particles that have escaped aggregation and thus are still unattached.

You can do this by figuring it out empirically (brownie points!) or by looking for a function that finds average distance between particles.

A little extra to think about (not necessary to answer): The AguaClara floccuation model assumes that primary clay particles mostly attach to other primary clay particles and not to larger flocs (aggregates of clay particles). Can you think of why this is?

.. code:: python

    #answer
    init_sep_dist_clay = fm.sep_dist_clay(100 * u.NTU, fm.Clay).to(u.mm)
    final_sep_dist_clay = fm.sep_dist_clay(1 * u.NTU, fm.Clay).to(u.mm)
    print('The average distance between clay particles at 100 NTU is', init_sep_dist_clay)
    print('The average distance between clay particles at 1 NTU is', final_sep_dist_clay)

The average distance between clay particles at 100 NTU is 0.141 mm
The average distance between clay particles at 1 NTU is 0.654 mm

5)
~~~

What is the inner viscous length scale in the mechanical flocculator at the maximum energy dissipation rate? Given that this is a very high energy dissipation rate for flocculation, it corresponds to a very small inner viscous length scale. This means that eddies are able to survive down to a small size before viscosity damps their motion. If the separation distance between clay particles that haven’t turned into flocs is less than this inner viscous scale, then it is reasonable to assume that all flocculation is dominated by viscosity. The function within ``floc_model.py`` that does this is confusingly named
``lamba_vel()``.

.. code:: python

    #answer
    print('The inner viscous length scale is', fm.lambda_vel(ed_rate_prop_max, temp_design).to(u.mm))

The inner viscous length scale is 2.39 mm


6)
~~~

Below is a graph showing the inner viscous length scale that divides flows that are dominated by inertia (eddies) from flows where viscosity is significant. **Add the data point** representing the maximum energy dissipation rate vs the maximum clay separation distance at the end of flocculation for the mechanical flocculator you have been designing.

.. code:: python

    #This code is provided to help you make your graph

    #Creates the array for energy dissipation rates (EDRs)
    x = np.logspace(np.log10(1),4)*u.mW/u.kg

    plt.figure('Inner Viscous Scale', (6,6))
    plt.title('Inner Viscous Scale vs Energy Dissipation Rate')

    ax.set(ylabel='Inner Viscous Scale (mm)')
    ax.set(xlabel='Energy Dissipation Rate(mW/kg)')

    plt.yscale('log')
    plt.xscale('log')

    plt.grid(b=True, which='major', color='k', linestyle='-', linewidth=1)
    plt.grid(b=True, which='minor', color='k', linestyle='-', linewidth=0.5)

    #fm.lambda_vel, which returns the inner viscous length scale,
    #is being applied to the array of EDRs for our design temperature
    y = fm.lambda_vel(x,temp_design)
    ax.plot(x, y.to(u.mm), 'r')

    #------------------------------------------------------------------------
    #----------------------------YOUR CODE BELOW-----------------------------
    #------------------------------------------------------------------------
    #answer
    ax.plot(ed_rate_prop_max.to(u.mW/u.kg), final_sep_dist_clay.to(u.mm), 'ko')



    print(final_sep_dist_clay)
    print(ed_rate_prop_max)

    plt.show()

0.6541789493547243 millimeter
    422.57902694348155 milliwatt / kilogram


7)
~~~

According to the plot and analysis above, are the collisions between clay particles at a concentration of 1 NTU dominated by inertia or by viscosity? Explain why!

The final spacing between clay particles is still smaller than the inner viscous length scale at which eddies are damped by viscosity. This suggests that all collisions in flocculation are dominated by viscosity.


Real-world considerations of flocculation
=========================================

Now that you have an augmented understanding of flocculation theory, we can consider a few ways in which the theory applies to real-world flocculators.

In this section, there are no calculations for you to do or code for you to write - everything has been provided for you. This was done to shorten this design challenge while still detailing relevant and important information.

 **There are two conceptual questions for you to answer at the end of the section.** Read through and focus on understanding the concepts before you try to answer the questions.

Coagulant distribution in a reactor
-----------------------------------

The flocculation model accounts for loss of coagulant nanoparticles to the reactor walls. The loss of coagulant nanoparticles is assumed to scale with the area of the flocculator walls divided by the total area of clay and flocculator walls. This loss is significant for low turbidity and small scale flocculators, such as the 1 liter per second flocculator AguaClara recently designed.

Here we will consider a flocculator built out of pipe, not one contained within a rectangular reactor. The ``diam_tube`` parameter is the flocculator diameter and is needed to estimate how much of the coagulant is lost to the walls of the flocculator. We will assume the flocculator tube is for the 1 L/s plant and has a diameter of 7.5 cm

We will evaluate the situation where the turbidity is 10 NTU and the coagulant dose is 1 mg/L of aluminum. The code below does the following:

-  Estimates the fraction of coagulant nanoparticles lost to the flocculator walls.
-  Estimates the fraction of the clay surface area that is coated with nanoparticles.

.. code:: python

    diam_tube = 7.5 * u.cm
    conc_clay = 100*u.NTU
    conc_Al = 0.5*u.mg/u.L


    #fm.ratio_area_clay_total() returns fraction (between 0 and 1) that represents the surface area of
    #the clay particle over the sum of the surface area of the clay and reactor walls

    wall_loss = 1 - fm.ratio_area_clay_total(conc_clay, fm.Clay, diam_tube, fm.RATIO_HEIGHT_DIAM)
    print('The fraction of the coagulant lost to the walls is', wall_loss)

    #fm.gamma_coag() returns the fraction of clay that is covered by coagulant. This is a very hard parameter
    #to actually measure, so this is just an estimate.

    fraction_coated = fm.gamma_coag(conc_clay,conc_Al, fm.PACl,
                                      fm.Clay, diam_tube, fm.RATIO_HEIGHT_DIAM)
    print('The fraction of the clay surface area that is is coated is', fraction_coated)

Time scale of flocculation
--------------------------

Now we want to estimate the average time required for an initial successful collision between two primary clay particles that are partially coated with coagulant nanoclusters. Note that for the first collision, the current floc size is the same as the clay size. We will use the average energy dissipation rate for the mechanical flocculator as found above.

.. code:: python

    ed_rate_mech_ave = 6.4*u.mW/u.kg

    time_first_collision = fm.time_col_laminar(ed_rate_mech_ave, 10*u.degC,
                                                 conc_Al, conc_clay, fm.PACl,
                                                 fm.Clay, fm.Clay.Diameter, diam_tube,
                                                 fm.DIM_FRACTAL, fm.RATIO_HEIGHT_DIAM).to(u.s)

    print('The time required for the first succesful collision is', time_first_collision)

This collision time is quite fast and is the origin of the question, “why does flocculation require 30 minutes?” as mandated in the Ten State Standards.

AguaClara flocculation model
----------------------------

We will now briefly consider an AguaClara flocculator design with an average energy dissipation rate of approximately 11 mW/kg and a residence time of 8.1 minutes. The design temperature is 15 degC.

Below is a calculation for the Gt value of this flocculator.

.. code:: python

    #answer
    ed_rate_floc_aguaclara = 11*u.mW/u.kg
    time_floc_aguaclara = 8.1*u.minute
    temp_design_aguaclara = 15*u.degC

    #This equation for G can be found in the course slides (all equations you see in design challenges can be found in the slides)
    G_floc_aguaclara = np.sqrt(ed_rate_floc_aguaclara/pc.viscosity_kinematic(temp_design_aguaclara))
    Gtime_floc_aguaclara = (G_floc_aguaclara*time_floc_aguaclara).to(u.dimensionless)
    print('The AguaClara Gt value is', Gtime_floc_aguaclara)

Coagulant coverage fraction of a particle
-----------------------------------------

This section solves the integrated flocculation model for :math:`\Gamma`. We simplify the model by recognizing that the spacing between particles at the end of the flocculation process is much greater than the initial particle spacing. This means that the raw water turbidity drops out of the equation. The value of the rate constant for collisions is k = 0.24. We start with the equation below:

.. math:: \Gamma = \frac{3}{2}\cdot \frac{\Lambda^2 }{\mathit{k} \pi d_{p}^2 Gt }

We then estimate the required coagulant coverage of clay, :math:`\Gamma`, for the AguaClara flocculator to achieve a 2 NTU settled water turbidity when starting with a raw water that is 50 NTU.

Note that the specified flocculation model applies to both hydraulic and mechanical flocculators.

.. code:: python

    #Fitting constant/Sedimentation tank factor
    k = 0.24

    #gamma_aguaclara_design uses functions in floc_model.py to solve the equation in the problem statement
    conc_clay_goal = 2 * u.NTU
    gamma_aguaclara_design = (3/2) * (fm.sep_dist_clay(conc_clay_goal, fm.Clay)**2
                               / (k * np.pi * (fm.Clay.Diameter * u.m)**2
                                  * Gtime_floc_aguaclara
                                 )
                              ).to(u.dimensionless)

    print('The Gamma value is', gamma_aguaclara_design)

Residence time and coagulant coverage
-------------------------------------

If you doubled the residence time of the flocculator, the required coagulant coverage of clay changes according to the model. By doubling the residence time, the required coagulant coverage is reduced by a factor of 2.

Modeling flocculation in the presence of humic acid, with pC\* as the performance metric
----------------------------------------------------------------------------------------

The flocculation model predicts the settled water turbidity given the composition of the raw water, the flocculator characteristics, and a fitting parameter that must be a function of the sedimentation tank characteristics. This fitting parameter is k, which is the same as the rate constant for collisions described above. The model is far from complete - it doesn’t yet describe the effects of floc blankets. Below we have created a plot showing model predictions for a range of coagulant and humic acid (dissolved organic matter) concentrations. The plot uses our approximation for pC\* described in class and shown below:

.. math::

   pC^*=\frac{3}{2}log{(\frac{2}{3}\pi k \frac{d_p^{2}}{\Lambda_0^{2}}Gt\alpha + 1)}

.. code:: python

    #Define the range of coagulant. This is necessary to create plots of pC* as a function of coagulant dose.
    coag_graph = np.linspace(0.01, 2.5, 100) * u.mg/u.L

    # Graph results of a particular NTU. Note that you can change this value to see how the graph responds.
    # A change here even changes the graph title changes!
    plot_NTU = 50*u.NTU

    plt.figure(str(plot_NTU), (6,6))
    plt.title(str(plot_NTU)+' Graph for Various Humic Acid Concentrations')
    ax.set(ylabel='pC*')
    ax.set(xlabel='coagulant dosage (mg/L)')

    # Create an array of humic acid concentrations
    plot_humic_acid = np.linspace(0,15,6)*u.mg/u.L

    # Create a function that only has inputs for the values that we will change between plots.
    #All other variables are taken from predefined values. This simplifies the function call for use in generating the plots.
    def plot_pC(conc_humic_acid):
        k = 0.24
        # The energy dissipation rate for aguaclara designs
        ed_rate = 11*u.mW/u.kg
        #The inner diameter of the flocculator tube is important because a significant fraction of the
        #coagulant ends up attaching to the flocculator walls
        tube_diam = 3/8 * u.inch
        time_floc = 8.1 * u.minute
        temp = 15 * u.degC
        #pc_viscous is the solution for the equation in the problem statement. It returns pC*
        plot_pC = fm.pc_viscous(ed_rate, temp, time_floc, tube_diam,
                                plot_NTU, coag_graph, conc_humic_acid,
                                fm.HumicAcid, fm.PACl, fm.Clay,
                                k, fm.RATIO_HEIGHT_DIAM)
        return plot_pC

    x = coag_graph.to(u.mg/u.L)

    ax.plot(x, plot_pC(plot_humic_acid[0]), 'r',
             x, plot_pC(plot_humic_acid[1]), 'b',
             x, plot_pC(plot_humic_acid[2]), 'g',
             x, plot_pC(plot_humic_acid[3]), 'm',
             x, plot_pC(plot_humic_acid[4]), 'c',
             x, plot_pC(plot_humic_acid[5]), 'y')

    #We can use the array of humic acid concentrations to directly create the legend!
    plt.legend(plot_humic_acid, loc = 'best')
    plt.show()

There is a lot to learn from this graph!!!!!! It appears that for any given coagulant dose, humic acid concentration significantly affects pC*. Additionally, notice the diminishing returns of adding more coagulant. This effect appears to be independent of humic acid concentration (see the red curve).

Modeling flocculation in the presence of humic acid, with settled water turbidity as the performance metric
-----------------------------------------------------------------------------------------------------------

We will now display a similar plot which shows settled water turbidity instead of pC*. Our initial turbidity is 10 NTU, and we will four curves for separate humic acid concentrations.

.. code:: python

    #answer
    plot_NTU = 10*u.NTU

    plt.figure(str(plot_NTU), (6,6))
    plt.title(str(plot_NTU)+' Graph')
    ax.set(ylabel='Settled water turbidity (NTU)')
    ax.set(xlabel='coagulant dosage (mg/L)')

    def plot_conc_clay(conc_clay, conc_nat_org_mat):
        k = 0.24
        ed_rate = 11*u.mW/u.kg
        #The inner diameter of the flocculator tube is important because a significant fraction of the
        #coagulant ends up attaching to the flocculator walls
        tube_diam = 3/8 * u.inch
        conc_clay = plot_NTU
        time_floc = 8.1 * u.minute
        temp = 15 * u.degC
        #s_t calls on fm.pc_viscous() like the previous cell of code, but also uses the fm.invp()
        #function to turn pC* back into units of settled water turbididty.
        s_t = fm.invp(fm.pc_viscous(ed_rate, temp, time_floc, tube_diam,
                   conc_clay, coag_graph, conc_nat_org_mat, fm.HumicAcid, fm.PACl, fm.Clay,
                                k, fm.RATIO_HEIGHT_DIAM),conc_clay)

        return s_t

    #Creates array of humic acid concentrations. This was done in the previous code cell with np.linspace,
    #but because we don't want evenly spaced concentrations here we input our desired values manually
    plot_humic_acid = np.array([0,1,5,20])*u.mg/u.L

    x = coag_graph.to(u.mg/u.L)
    ax.plot(x, plot_conc_clay(plot_NTU, plot_humic_acid[0]), 'r',
             x, plot_conc_clay(plot_NTU, plot_humic_acid[1]), 'b',
             x, plot_conc_clay(plot_NTU, plot_humic_acid[2]), 'g',
             x, plot_conc_clay(plot_NTU, plot_humic_acid[3]), 'y')

    plt.legend(plot_humic_acid, loc = 'best')
    plt.show()

Looking at the interactions between coagulant, clay, and humic acid from this perspective yields even more fun discoveries! For increasing humic acid concentration, more coagulant is required to even begin the process of flocculation.

8)
~~~

Why does the AguaClara flocculation model predict that adding 1 mg/L of aluminum has no effect on turbidity when the humic acid concentration is 20 mg/L?


At low concentrations of coagulant every coagulant nanoparticle surface is completely coated with humic acid and thus they aren’t sticky at all.


9)
~~~

It is tempting to assume that all the coagulant dosed gets attached to clay particles. However, if a plant operator were to make this assumption, their plant would produce low-quality water.

Identify and explain two significant reasons as to why this assumption fails.


1. Coagulant is lost to the walls of the reactors
2. Coagulant is lost to humic acid
   (Students need to write more than this)
