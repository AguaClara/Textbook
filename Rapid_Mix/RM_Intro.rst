.. _title_Rapid_Mix_Introduction:

************************
Rapid Mix Introduction
************************

This chapter is currently home for the prerequisites of successful flocculation. Those prerequisites include:
 - ensuring that the pH is in the correct range for coagulant nanoparticle formation after the coagulant has been added to the raw water.
 - increasing the coagulant dose to account for the coagulant interactions with dissolved species that effectively cover some of the coagulant nanoparticle surfaces.
 - increasing the coagulant dose to account for the available surface area of suspended particles to achieve
 - If there are multiple treatment trains, mixing the coagulant with the raw water so that parallel treatment trains receive the same concentration of coagulant (perhaps the conventional role of rapid mix)
 - transporting the coagulant nanoparticles to attach to suspended particles


Rapid mix is the term commonly used to describe the processes that occur between the coagulant addition to the raw water and the flocculation process. The processes that occur are not well understood and thus design guidelines have been empirical.

“In summary, little is known about rapid mix, much less any sensitivity to scale. However, the models and data reviewed suggest the need to be on the lookout for certain effects. From what is presently known, it can be speculated that since coagulant precipitation is sensitive to both micro- and macro-mixing, scale-up must consider not only energy dissipation rate, but also the reaction injection point and the contacting method.” - `Mixing in Coagulation and Flocculation 1991 page 292 <https://books.google.com/books/about/Mixing_in_coagulation_and_flocculation.html?id=dkFSAAAAMAAJ>`_.

Although the processes have not been well characterized, the energy that is invested for rapid mix processes is significant. In many cases the amount of energy used isn't practical for gravity powered water treatment plants. The high energy consumption of rapid mix units has led some municipal water treatment plant operators to experiment with turning off rapid mix units. They have found that at least under some conditions there is no indication that the energy used in rapid mix improved plant performance. Thus there is a need to understand the physical and chemical processes that occur when a concentrated liquid coagulant is added to water.

Rapid mix sets the stage for aggregation of both suspended particles and dissolved substances. Particle and dissolve substance aggregation is mediated by coagulant nanoparticles. The nanoparticles attach to raw water particles as well as to some dissolved species. After the nanoparticles have been mixed with the raw water and have attached to raw water particles the next process, flocculation, can begin.  :ref:`Flocculation <title_Flocculation_Introduction>` is the process of producing collisions between particles to create flocs (aggregates of particles).

Coagulant nanoparticle application includes multiple steps that must occur before the raw water particles can begin to aggregate. The sticky nanoparticles can be aluminum :math:`(Al^{+3})` or iron :math:`(Fe^{+3})` based and in either case the nanoparticles are formed from precipitated hydroxide species (:math:`Al(OH)_3` or :math:`Fe(OH)_3`). The series of events that are contained in the broad designation of “rapid mix” are:

  #. Liquid coagulant stock solution with a low pH is injected into the raw water
  #. Fluid Mixing: Turbulent eddies randomize the fluids (but don’t blend them)

     #. Large scale eddies mix the coagulant with the raw water by creating large fluid deformations. This stretching and turning of the raw water and coagulant is analogous to shuffling a deck of cards. The cards are randomized, but the cards maintain their identity. The original liquids retain their chemical composition. This step must be completed before any flow splitting for parallel treatment trains.
     #. Turbulent eddies disintegrate into smaller and smaller eddies.
     #. At a very small scale (Inner viscous length scale) viscosity becomes significant and the kinetic energy of the eddies begins to be converted to heat by viscosity.

  #. The coagulant is blended with the raw water by molecular diffusion
  #. The higher pH of the raw water causes the coagulant to begin to precipitate as :math:`Al_{12}AlO_4(OH)_{24}(H_2O)_{12}^{7+}`, an aluminum, Al, nanoparticle.
  #. The precipitating :math:`Al_{13}` molecules aggregates with other nearby :math:`Al_{13}` molecules to form aluminum hydroxide nanoparticles. It is also possible that the nanoparticles are already formed in the coagulant stock suspension. Polyaluminum chloride stock solutions turn white in about a year at room temperature and this suggests that nanoparticles form in the stock solution.
  #. The Al nanoparticles attach to other dissolved species and suspended particles.
  #. Molecular diffusion causes some dissolved species and Al nanoparticles to aggregate.
  #. Fluid shear and molecular diffusion cause Al nanoparticles with attached formerly dissolved species to collide with inorganic particles (such as clay) and organic particles (such as viruses, bacteria, and protozoans).

These multiple steps cover a wide range of length scales and it is not clear at the onset which processes might be the rate limiting steps. We will develop time scale estimates for several of these steps to help identify which processes will likely require the most attention to design. Many of these transport processes are presumed to occur in parallel. :numref:`figure_transport_length_scales` shows the range of length scales.

.. _figure_transport_length_scales:

.. figure::    Images/rapid_mix_macro_to_nano_scale.png
    :width: 700px
    :align: center
    :alt: rapid mix macro to nano scale

    Transport of coagulant nanoparticles occurs over length scales ranging from meter to a fraction of a nanometer.


.. _heading_Chemistry_of_Coagulant_Nanoparticles:

Chemistry of Coagulant Nanoparticles
========================================

Aluminum based coagulants are commonly used in drinking water treatment plants. Less frequently iron based coagulants are used. These metals precipitate in water at neutral pH as :math:`Al(OH)_3` or :math:`Fe(OH)_3`. These precipitates form nanoparticles that are sticky. The origin of that stickiness is not well known, but one significant property of both precipitates is that they are both highly polar molecules. The `difference in electronegativity <https://en.wikipedia.org/wiki/Electronegativity>`_ (Pauling scale) between
 - Aluminum (1.61) and Oxygen (3.44) is 1.83
 - Iron (1.83) and Oxygen (3.44) is 1.61
 - Hydrogen (2.20) and Oxygen (3.44) is 1.24

Thus both aluminum and iron coagulants are more polar than water and it is possibly that it is their strong polarity that enables them to displace water that is bound to particles surfaces and then form bonds with that surface. In order to displace water molecules that are bound to the particles surfaces, the coagulants must have stronger bonds to particles surfaces than the polar water molecules and thus it seems likely that coagulants must be more polar than water.



.. _heading_pH_Effects_of_Adding_Coagulant:

pH Effects of Adding Coagulant
----------------------------------------

The coagulants used for drinking water treatment are acidic and thus result in a lowering of the pH of the treated water. The optimal pH for aluminum coagulant nanoparticle formation is between pH of 6.5 and 8.5. This is also the `pH range set by the EPA secondary standards for drinking water <https://www.epa.gov/dwstandardsregulations/secondary-drinking-water-standards-guidance-nuisance-chemicals>`__. Although many water sources are within this pH range, there are some waters with more extreme values of pH. The aluminum and iron based coagulants are also acidic and in some waters the pH may drop below the ideal range when adding the coagulant. When the pH is outside the acceptable range it is necessary to adjust the pH by adding either a base or an acid.

When aluminum sulfate (alum) to water it dissociates and then precipitates as :math:`Al(OH)_3`. In the process protons, :math:`H^+` are released and thus the pH (:math:`-log[H^+]`) decreases.

.. math:: Al_2(SO_4)_3 + 6H_2O\rightarrow 2Al(OH)_3 + 6H^+ + 3SO_4^{-2}

The release of these protons reduces the acid neutralizing capacity, ANC, (also known as alkalinity) of the water. ANC is traditionally measured with units of mg/L of :math:`CaCO_3` rather than eq/L.  :numref:`table_ANC_consumed_by_alum` shows the relationship between ANC measured as mg/L of :math:`CaCO_3` and alum (:math:`Al_2(SO_4)_3 \cdot 14H_2O`)



.. _table_ANC_consumed_by_alum:

.. csv-table:: Reduction in ANC caused by addition of alum.
   :header: "", "Alum", "Calcium Carbonate"
   :align: left

   Molecular Formula, :math:`Al_2(SO_4)_3 \cdot 14.3H_2O`, :math:`CaCO_3`
   Molecular mass, 600 g/mole, 100 g/mole
   eq/mole, 6,2
   Molecular mass/eq, 100 g/eq, 50 g/eq
   Simple guide, 1 mg/L alum consumes, 0.5 mg/L calcium carbonate ANC

Low ANC waters (See section on :ref:`heading_Buffering_Capacity_of_Natural_Waters`.) could have their ANC increased by addition of a base. A simpler approach is often to use a different coagulant that is less acidic.

Polyaluminum chloride (PACl) is another aluminum based coagulant that performs similarly to alum. PACl is manufactured by slowly titrating an acidic solution containing dissolved aluminum with a base (in the chemical plant) to produce a meta-stable and soluble polymeric aluminum. PACl consumes less alkalinity (ANC) because it is partially neutralized by the titration with a base. In addition, the aluminum mass fraction of PACl is higher than in alum because there are no attached water molecules. The mass of PACl required for flocculation is less than for alum due largely to the higher aluminum fraction. The lower mass of PACl required is an economic benefit when shipping is a significant cost of the coagulant.

There are many different molecular formulas given for PACl. The molecular formulas are either from the perspective of the chemical supplier or represent the composition of the PACl nanoparticles. The molecular formula from the chemical supplier represents the extent of neutralization and hence the replacement of chloride with hydroxide. In that case the PACl molecular formula is:

.. math:: [Al_n(OH)_mCl_{3n-m}]_x

The extent of the PACl titration with base is defined as basicity. Basicity is the ratio of hydroxyl equivalents to aluminum equivalents. Basicity of 1 would mean that the PACl does not produce any protons when it dissolves in water. Basicity of 0 means it produces 3 protons per Al (like alum). The equation for basicity is:

.. math:: Basicity = \left( \frac{m}{3n}\right)

The lowest basicity commercial PACl formulations are about 10%. Most PACls are in the medium to high basicity range (50-70%). The highest stable basicity (83%) is aluminum chlorohydrate (:math:`Al_2(OH)_5Cl`) that is useful for treating water with very low ANC.

The ANC of the aluminum coagulant can be obtained from the number of protons it releases:

.. math:: ANC_{Al} = 3(Basicity-1)[Al] = \left(\frac{m}{n} - 3\right)[Al] = \Pi_{Al}[Al]

| where:
| :math:`\Pi_{Al}=\left(\frac{m}{n} - 3\right)` is ANC per mole of aluminum for the given coagulant


Thus the ANC of alum (with 0 hydroxides) is :math:`-3[Al]`. The method of calculating the :math:`ANC_{Al}` will be used to calculate the amount of base that must be added to achieve a target pH.

.. todo:: Add link to the pH_adjust function that is currently in the RM_Exmaples.rst sheet.

The molecular formula of the PACl nanoparticles is always some combination of Al, O, and H. One common molecular structure is a Keggin structure with 13 aluminum atoms. This molecule has a tetrahedral Al atom in the center of the cluster coordinated to 4 oxygen atoms. The molecular formula of the Keggin structured aluminum molecule is

.. math:: AlO_4Al_{12}(OH)_{24}(H_2O)_{12}^{7+}

The attached water molecules are sometimes omitted. Coagulant nanoparticles are presumably created by aggregation of these Keggin structure molecules.

.. _heading_Buffering_Capacity_of_Natural_Waters:

Buffering Capacity of Natural Waters
----------------------------------------

When acid is added to a water containing bicarbonate, :math:`HCO_3^-`, one of the potential reactions is for a proton to combine with :math:`HCO_3^-` to form carbonic acid, :math:`{H_2}CO_3`. If a base is added to water the reaction will proceed in the opposite direction. Carbonic acid, :math:`{H_2}CO_3`, is chemical indistinguishable from dissolved carbon dioxide, :math:`CO_{2_{aq}}` and the total of carbonic acid and dissolved carbon dioxide is represented as :math:`{H_2}CO_3^{\star}`. The reaction of bicarbonate to form carbonic acid removes one proton from solution and thus the concentration of protons doesn’t increase as fast as we might have first expected as acid is added to the water.

The reactions of carbonate species with protons provides pH buffering capacity that must be considered when calculating the effect of acid or base addition. Since carbonates are the dominant buffering agents in natural waters it is essential to account for their influence on pH.

The effect of acid or base addition to a water containing carbonates (or other weak acids and bases) can be modeled using the equation for :ref:`Acid Neutralizing Capacity <heading_Acid_Neutralizing_Capacity_(ANC)_or_Alkalinity>`.

.. _heading_pH_Range_for_Precipitation_of_Coagulant_Nanoparticles:

pH Range for Precipitation of Coagulant Nanoparticles
------------------------------------------------------

A critical property of coagulants is that in order to act as an adhesive between particles they must be solid phase at neutral pH. Both Al(III) and Fe(III) have low solubility at neutral pH and thus meet this requirement. The pH region of low solubility sets the range of pH where flocculation is effective. :numref:`figure_Al_solubility` shows the solubilty of aluminum as a function of pH.

.. _figure_Al_solubility:

.. figure::    Images/Al_solubility.png
    :width: 600px
    :align: center
    :alt: Al solubility

    Solubility of aluminum as a function of pH. Figure adapted from `Pernitsky and Edzwald <http://dx.doi.org/10.2166/aqua.2006.062>`_.

Research is needed to quantify flocculation performance in continuous flow floc/floc blanket/plate settler systems as a function of pH.

The aluminum concentration range used for flocculation ranges from approximately 0.4 - 10 mg/L and is strongly influenced by the concentration of dissolved organic matter and the concentration of suspended solids. The flocculation and floc blanket capacity to produce collisions between suspended particles also influences the required aluminum concentration.

.. _heading_pH_Adjustment_in_Water_Treatment_Plants:

pH Adjustment in Water Treatment Plants
----------------------------------------

In drinking water treatment plant operation it is sometimes necessary to add a base (or acid) to increase (or decrease) the pH of the raw water. The added coagulant tends to reduce the pH. The carbonate system is most important in understanding how the base will adjust the pH because the reaction between carbonic acid and bicarbonate occurs around pH 6.3, the pK (negative log of the dissociation constant is the pH where that reaction is centered) for that reaction. Carbon dioxide exchange with the atmosphere is insignificant in drinking water treatment unit processes unless there is an aeration stage. Thus we can use the ANC equation for the case with no :math:`CO_2` exchange with the atmosphere.

In the section, :ref:`heading_pH_Adjustment` we evaluate the case where we add a base that will increase the ANC of the raw water and it might also increase the total carbonate concentration. We calculate how much of that base to add to reach a target pH.

.. _Fluid_Mixing:

Fluid Mixing
========================================

Fluid mixing is the process by which large scale eddies distribute packets of the coagulant stock throughout the raw water. The term “Rapid mix” is probably best used to describe this process. Traditional methods of achieving this fluid mixing include various methods of generating intense turbulence. Fluid mixing is able to rapidly blend the coagulant with the raw water in a matter of a few seconds. The equations describing the fluid mixing process are presented in the section on :ref:`heading_Estimates_of_time_required_for_mixing_processes`.

.. _figure_Backmix:

.. figure:: Images/Backmix.jpg
    :width: 200px
    :align: center
    :alt: Backmix

    Backmix: a mechanical rapid mixer that has a relatively long residence time in a completely mixed flow reactor.

.. _figure_Inline:

.. figure:: Images/Inline.jpg
    :width: 400px
    :align: center
    :alt: Inline

    Inline: a mechanical rapid mixer that has a short residence time in a completely mixed flow reactor that is often built into a pipe.

.. _figure_hydraulic_jump:

.. figure:: Images/hydraulic_jump.jpg
    :width: 200px
    :align: center
    :alt: hydraulic jump

    Hydraulic jump: a hydraulic rapid mixer uses the flow expansion downstream from supercritical open channel flow.

The hydraulic jump in :numref:`figure_hydraulic_jump` uses a flow expansion to generate mixing in an open channel and that suggests that a flow expansion could also be used to generate mixing in a closed conduit. AguaClara rapid mix units consist of an orifice in the bottom of the Linear Flow Orifice Meter (:ref:`heading_lfom`) where the water enters the flocculator (see :numref:`figure_Rapid_mix_orifice`). However, given that fluid mixing is so easy to attain it is unclear if the energy used in the rapid mix orifice is necessary.

.. _figure_Rapid_mix_orifice:

.. figure:: Images/Rapid_mix_orifice.png
    :width: 400px
    :align: center
    :alt: Rapid mix orifice

    The orifice creates a high velocity jet that generates mixing as it expands in the contact chamber prior to flocculation.

.. _heading_Conventional_Mechanical_Rapid_Mix:

Conventional Mechanical Rapid Mix
---------------------------------


.. _heading_Conventional_Maximum_Velocity_Gradients:

Maximum Velocity Gradients
--------------------------

.. code:: python

    Mix_HRT = np.array([0.5,15,25,35,85])*u.s
    Mix_G = np.array([4000,1500,950,850,750])/u.s
    Mix_CP = np.multiply(Mix_HRT, np.sqrt(Mix_G))
    Mix_Gt = np.multiply(Mix_HRT, Mix_G)
    Mix_EDR = (Mix_G**2*pc.viscosity_kinematic(Temperature))

    fig, ax = plt.subplots()
    ax.plot(Mix_G.to(1/u.s),Mix_HRT.to(u.s),'o')
    ax.yaxis.set_major_formatter(FormatStrFormatter('%.f'))
    ax.xaxis.set_major_formatter(FormatStrFormatter('%.f'))
    ax.set(xlabel='Velocity gradient (Hz)', ylabel='Residence time (s)')
    fig.savefig(imagepath+'Mechanical_RM_Gt')
    plt.show()

.. _figure_Mechanical_RM_Gt:

.. figure:: Images/Mechanical_RM_Gt.png
    :width: 400px
    :align: center
    :alt: Mechanical RM Gt

    Mechanical rapid mix units use a wide range of velocity gradients and residence times.

Conventional rapid mix units use mechanical or potential energy to generate intense turbulence to begin the mixing process. Conventional design is based on the use of :math:`\bar G` (an average velocity gradient) as a design parameter. We don’t yet know what the design objective is for rapid mix and thus it isn’t clear which parameters matter. We hypothesize that both velocity gradients that cause deformation of the fluid and time for molecular diffusion are required to ultimately transport coagulant nanoparticles to the surfaces of clay particles.

The velocity gradient can be obtained from the rate at which mechanical energy is being dissipated and converted to heat by viscosity.

.. math::  \varepsilon = G^2 \nu

where :math:`\varepsilon` is the energy dissipation rate, :math:`G` is the velocity gradient, and :math:`\nu` is the kinematic viscosity of water. We can estimate the power input required to create a target energy dissipation rate for a conventional design by noting that power is simple the energy dissipation rate times the mass of water in the rapid mix unit.

.. math:: P = \bar\varepsilon \rlap{\kern.08em--}V \rho

.. math::  P = \bar G^2 \nu \rlap{\kern.08em--}V \rho

We can relate reactor volume to a hydraulic residence time, :math:`\theta`, and volumetric flow rate, Q.

.. math::  P = \rho \bar G^2 \nu Q \theta

This equation is perfectly useful for estimating electrical motor sizing requirements for mechanical rapid mix units. For gravity powered hydraulic rapid mix units it would be more intuitive to use the change in water surface elevation, :math:`\Delta h` instead of power input.

.. math:: P = \rho g Q \Delta h

Combining the two equations we obtain.

.. math::   \Delta h =   \frac{G^2 \nu \theta}{g}

.. _Table_Conventional_Rapid_Mix_Design_Values:

.. csv-table:: Typical values for conventional rapid mix residence time and average velocity gradients
   :header:  "Residence Time (s)","Velocity gradient G (1/s)","Energy dissipation rate (W/kg)","Equivalent height (m)"

   "0.5","4000","16","0.8"
   "10 - 20","1500","2.25","2.3 - 4.6"
   "20 - 30","950","0.9","1.8 - 2.8"
   "30 - 40","850","0.72","2.2 - 2.9"
   "40 - 130","750","0.56","2.3 - 7.5"

From Environmental Engineering: A Design Approach by Sincero and
Sincero. 1996. page 267.

Rotating propellers can either be installed in open tanks or enclosed in pipes. From a mixing and fluids perspective it doesn’t make any difference whether the tank is open to the atmosphere or not. The parameters of interest are the rate of fluid deformation and the residence time in the mixing zone.

.. _heading_Mixing_time:

Mixing time
-----------

The time required for mixing in a turbulent environment is a function of the rate that kinetic energy is being dissipated as heat (the energy dissipation rate) and the length scale of the eddies. Given that turbulent energy is passed from large eddies to smaller and smaller eddies, the amount of energy that is being transferred at any given length scale is independent of scale. The result (see equation :eq:`eq_t_eddy`) is that the time required for mixing is dominated by the time required for the largest eddies to turn over (:numref:`figure_Eddy_turnover_times`).

.. _figure_Eddy_turnover_times:

.. figure:: Images/Eddy_turnover_time.png
    :width: 400px
    :align: center
    :alt: Eddy turnover time

    Eddy turnover times as a function of length scale for a range of energy dissipation rates.

The eddy turnover times are longest for the largest eddies and this analysis suggests that it only takes a few seconds for turbulent eddies to mix from the scale of the flow down to the inner viscous length scale.

The large scale mixing time is critical for the design of water treatment plants for the case where the flow is split into multiple treatment trains after coagulant addition. In this case it is critical that the coagulant be mixed equally between all of the treatment trains and thus the mixing times shown in the previous graph represent a minimum time between where the coagulant is added and where the flow is divided into the parallel treatment trains.

It is likely this process of mixing from the scale of the flow down to the inner viscous length scale is commonly referred to as “rapid mix.” Here we showed that this mixing is indeed rapid and is really only a concern in the case where the coagulant injection point is very close to the location where the flow is split into multiple treatment trains.

Fluid deformation dominated by viscous shear and molecular diffusion finish the process of blending the coagulant nanoparticles with the water. We show in :ref:`Fluid_Deformation_by_Shear` that the time required by fluid deformation and molecular diffusion to finish the blending process is approximately equal to 1/G where G is the velocity gradient. Given that velocity gradients in rapid mix units are typically greater than a thousand Hz the time required to finish the blending is approximately 1 ms.

Thus the time required for mixing the coagulant nanoparticles with the fluid typically only requires a few seconds and will be accomplished whether or not the rapid mix unit is turned on. The turbulent eddies from the water flowing a the channel or pipe between the coagulant injection point and the flocculator in most cases will be sufficient to achieve the fluid mixing. However, the step of the :ref:`coagulant nanoparticles attaching to the suspended particles<heading_Diffusion_and_Shear_Transport_Coagulant_Nanoparticles_to_Clay>` may be aided by the high energy of the rapid mix unit.

.. _heading__Coagulant_Nanoparticle_Interactions:

Coagulant Nanoparticle Interactions
========================================

Coagulant nanoparticles are sticky and can attach to suspended particles as well as to each other. Some dissolved substances also adsorb to coagulant nanoparticles. The development of models to describe these interactions has been impeded by the charge neutralization hypothesis that failed to account for the size of the coagulant nanoparticles and by the complexity of modeling all of these competing processes. Although the model describing removal of dissolved organic matter is still nascent, it is possible that a simplified approach that separates fast and slow processes will enable a sequential model.

Interactions between the various suspended and dissolved substances (see :numref:`figure_Particle_sizes`) can occur simultaneously as soon as the coagulant is blended with the raw water. The rates of these interactions are controlled by the transport processes of fluid deformation and molecular diffusion. Molecular diffusion is fastest for small particles and fluid deformation is most effective for larger particles. Thus the fastest process is hypothesized to be the diffusion of low mass molecules to the coagulant nanoparticles. Transport of the coagulant nanoparticles to attach to suspended solids is expected to be a slower process. Transport of suspended particles to collide with other suspended particles (flocculation) is even slower.

.. _figure_Particle_sizes:

.. figure:: Images/Particle_sizes.png
    :width: 400px
    :align: center
    :alt: Particle sizes

    The size range of particles and nanoparticles that are important in drinking water treatment ranges from approximately a nanometer (for example arsenic :math:`HAsO_4^{2-}`) to thousands of nanometers for clay and protozoa.

.. _heading_Dissolved_Organic_Matter_and_Coagulant:

Dissolved Organic Matter
----------------------------------------

Dissolved organic matter (DOM) includes humic substances, fulvic acids, and other organic molecules. The distinction between dissolved and particulate organic matter is somewhat arbitrary and often 450 nm is used as the transition.  The dissolved organic matter could also be referred to as macromolecules or as nanoparticles.

Because of its small size the DOM has a large surface per unit mass. Water that contains high DOM concentrations requires much higher coagulant dosages to achieve effective flocculation. Removal of DOM is a high priority for drinking water treatment plants because DOM both interferes with disinfection processes and produces disinfection by products. A significant fraction of DOM can be removed by coagulant nanoparticles.

.. todo:: cite William's paper with model for flocculation of humic acid and clay suspension.


.. _heading_Suspended_Solids_and_Coagulant:

Suspended Solids
----------------------------------------

Suspended solids include both organic and inorganic particles. Organic particles of concern include virus, bacteria, and protozoa. Inorganic particles include clay and other minerals. Naturally occurring suspended solids tend to have negative surface charge at neutral pH. The negative surface charge effectively prevents particle aggregation and thus these particles can remain suspended for a very long time.

.. _heading_Pathogens_and_Coagulant:

Pathogens
---------

Virus particles readily attach to coagulant nanoparticles (see `"Effects of Floc-Virus Association on Chlorine Disinfection Efficiency by Shinichiro Ohgaki and Prasang Mongkonsiri <https://link-springer-com.proxy.library.cornell.edu/chapter/10.1007/978-3-642-76093-8_5>`_) and this attachment makes it possible to efficiently remove virus particles by flocculation followed by sedimentation. Bacteria (cite Yolanda Brook paper when it is published) and protozoans (need reference) are also removed by flocculation by coagulant nanoparticles.

.. _heading_Rate_Estimates_for_Coagulant_Nanoparticle_Transport_to_Suspended_Solids:

Rate Estimates for Coagulant Nanoparticle Transport to Suspended Solids
------------------------------------------------------------------------

Coagulant nanoparticles require significant time to attach to the surfaces of suspended solids. The time required is estimated in :ref:`heading_Diffusion_and_Shear_Transport_Coagulant_Nanoparticles_to_Clay`. It is quite possible that this stage of the rapid mix/flocculation process has been overlooked in the past. Transport of the nanoparticles to the suspended solids is accomplished by a combination of fluid deformation and diffusion.



.. _heading_EDR_G_and_mixing:

Energy Dissipation Rate, Velocity Gradient, and Mixing
======================================================

In addition to the general fluids review (:ref:`title_review_fluid_mechanics`), there are a few extra fluid dynamics concepts that are important to know in order to understand drinking water treatment and AguaClara’s approach to it. These concepts are primarily focused on the relationships between:
 - Turbulence
 - Viscosity
 - Shear
 - Velocity Gradients (:math:`G`),which serve as a measure of fluid deformation
 - Energy Dissipation Rate (EDR, :math:`\varepsilon`)

Knowledge of these concepts and how they interact is critical to understand rapid mix, flocculation, filtration, and disinfection. These concepts and their interactions first become relevant in rapid mix, the step in which the coagulant gets added to the raw water.

The two concepts that were not covered in the previous chapter, :ref:`title_review_fluid_mechanics`, are velocity gradient :math:`G` and energy dissipation rate :math:`\varepsilon`. While these will be very thoroughly described over the course of this introduction, a brief and simple explanation is included to help get the ball rolling.

Understanding :math:`G` and :math:`\varepsilon`
-----------------------------------------------

:math:`G`, or velocity gradient, is a measure of fluid deformation. It is defined by how quickly one point of water along one streamline moves in comparison to another point on another streamline (:math:`v_A` compared to :math:`v_B`, for example), taking into account the distance between the streamlines, :math:`\Delta h`. A visual example of a velocity gradient is shown in the image below:

.. _figure_Velocity_gradient_image:

.. figure:: Images/Velocity_gradient_image.jpg
    :width: 700px
    :align: center
    :alt: Velocity gradient image

    Velocity gradients cause relative velocities of fluid elements. Those relative velocities form the basis of particle collisions that are essential for the flocculation process.


**Note on terminology:** “Fluid deformation” is equivalent to “velocity gradient,” and the two terms can be used interchangeably. They are different ways of thinking about the same concept. Thus, :math:`G` is the measure of both terms.

:math:`\varepsilon`, or energy dissipation rate, is the rate that the kinetic energy of the fluid is being converted to heat. EDR is a very useful concept because the last step of converting kinetic energy into heat is accomplished by viscosity (:math:`\nu`). This kinetic energy being dissipated by viscosity is the energy associated with velocity gradients (:math:`G`). Thus, through EDR there is a direct connection between :math:`\nu` and :math:`G`. This connection will be further covered later on in this introduction.

As mentioned above, EDR and velocity gradients play an important role in mixing and in causing suspended particles to collide with each other, both of which are important topics in flocculation. Their use is not limited to flocculation, they are also helpful in understanding failure modes of plate settlers and terminal head loss of sand filters

.. todo:: Add links to textbook sections for plate settlers and filtration

We will begin by defining the concept of energy dissipation rate for a control volume. In a control volume that does not include pumps, turbines or other external energy sources or sinks, the mechanical energy lost is indicated by a change in elevation and quantified as :math:`g h_L`. That mechanical energy is lost in the time that the fluid is in the control volume, :math:`\theta`.

.. math::  \bar\varepsilon \theta = g h_L

This equation simply states that the average rate of energy dissipation times the time over which that dissipation occurs is equal to the total lost mechanical energy. The dimensions of :math:`\varepsilon` are:

.. math::  \varepsilon = \frac{[m^3]}{[s^3]} = {\rm \frac{W}{kg}}

These dimensions can be understood as a velocity squared per time, otherwise known as a rate of kinetic energy loss (recall that kinetic energy is :math:`{\rm Ke} = \frac{\bar v^2}{2g}`, or :math:`{\rm Ke} \propto \bar v^2`), or as power per unit mass, which would be :math:`{\rm  \frac{W}{kg}}`.

Velocity gradients are central to flocculation because they cause the deformation of the fluid, and this results in particle collisions. Consider a real-world example via the image below: if everyone on a sidewalk is walking in the same direction at exactly the same velocity, then there will never be any collisions between people (top). If, however, people at one side of the sidewalk stand still and people walk progressively faster as a function of how far they are away from the zero velocity side of the sidewalk, then there will be many collisions between the pedestrians (see :numref:`figure_Pedestrians_on_sidewalk`). Indeed, the rate of collisions is proportional to the velocity gradient.

.. _figure_Pedestrians_on_sidewalk:

.. figure:: Images/Pedestrians_on_sidewalk.jpg
    :width: 700px
    :align: center
    :alt: Pedestrians on sidewalk

    Pedestrians walking on a sidewalk serve as a model for velocity gradients.

Common Flow Geometries that Dissipate Energy
============================================

Water treatment plants at research and municipal scales deploy a wide range of flow geometries. The following list includes the flow geometries that are commonly used for mixing processes.

  -  Straight pipe (wall shear) - [uncommon, but included for completeness]
  -  Coiled tube (wall shear and expansions) - [research scale mixing]
  -  Series of expansions (expansions) - [hydraulic flocculators]
  -  Mechanical mixing - [mechanical rapid mix and flocculators]
  -  Between flat plates (wall shear) - [plate settlers]
  -  Round jet - (expansion) - [hydraulic rapid mix]
  -  Plane jet - (expansion) - [inlet into sedimentation tank]
  -  Behind a flat plate - (expansion) - [mechanical mixers]

The following tables can serve as a convenient reference to the equations describing head loss, energy dissipation rates, and velocity gradients in various flow geometries that are commonly encountered in water treatment plants. The :ref:`heading_Equations_Varying_Flow_Geometries` are available as a reference.

.. _table_Control_volume_equations:

.. csv-table:: Table of equations for control volume averaged values of head loss, energy dissipation rate, and the Camp-Stein velocity gradient.
   :header: "Geometry", ":math:`h_L`", "Energy dissipation rate",":math:`G_{CS}(\bar v)`",":math:`G_{CS}(Q)`"
   :align: left

   "Straight pipe",":math:`h_{{\rm f}} = {{\rm f}} \frac{L}{D} \frac{\bar v^2}{2g}`", ":math:`\bar\varepsilon = \frac{{\rm f}}{2} \frac{\bar v^3}{D}`",":math:`G_{CS} = \left(\frac{{\rm f}}{2\nu} \frac{\bar v^3}{D} \right)^\frac{1}{2}`",":math:`G_{CS} = \left(\frac{\rm{32f}}{ \pi^3\nu} \frac{Q^3}{D^7} \right)^\frac{1}{2}`"
   "Straight pipe laminar",":math:`h_{{\rm f}} = \frac{32\nu L\bar v}{ g D^2}`",":math:`\bar\varepsilon =32\nu \left( \frac{\bar v}{D} \right)^2`",":math:`G_{CS} =4\sqrt2 \frac{\bar v}{D}`",":math:`G_{CS} =\frac{16\sqrt2}{\pi} \frac{Q}{D^3}`"
   "Parallel plates laminar",":math:`h_{{\rm f}} = 12\frac{ \nu L \bar v }{gS^2}`",":math:`\bar\varepsilon = 12 \nu \left(\frac{ \bar v}{S} \right)^2`",":math:`G_{CS} = 2\sqrt{3}\frac{ \bar v}{S}`","-"
   "Coiled tube laminar",":math:`h_{L_{coil}} = \frac{32\nu L\bar v}{ g D^2} \left[ 1 + 0.033\left(log_{10}De\right)^4 \right]`",":math:`\bar\varepsilon = 32\nu \left( \frac{\bar v}{D} \right)^2 \left[ 1 + 0.033\left(log_{10}De\right)^4 \right]`",":math:`G_{CS_{coil}} = 4\sqrt2 \frac{\bar v}{D}\left[ 1 + 0.033\left(log_{10}De\right)^4 \right]^\frac{1}{2}`","-"
   "Porous media",:math:`h_f = f_{\phi} \frac{L}{D_{sand}} \frac{v_a^2}{2g} \frac{(1-\phi)}{\phi^3}`,:math:`\bar\epsilon = \frac{f_{\phi}}{2} \frac{v_a^3}{D_{sand}} \frac{(1-\phi)}{\phi^4}`,:math:`G_{CS} = \left(\frac{f_{\phi}}{2\nu} \frac{v_a^3}{D_{sand}} \frac{(1-\phi)}{\phi^4}\right)^{\frac{1}{2}}`,"-"
   "Expansions",":math:`h_e = K\frac{\bar v_{out}^2}{2g}`",":math:`\bar\varepsilon = K\frac{\bar v_{out}^3}{2H}`",":math:`G_{CS} = \bar v_{out}\sqrt{\frac{K\bar v_{out}}{2H\nu}}`","-"

The equations used to convert between columns in the table above are:

.. math::

   \bar\varepsilon = \frac{gh_{\rm{L}}}{\theta} \qquad\qquad
   G_{CS} = \sqrt{\frac{\bar \varepsilon}{\nu}} \qquad\qquad
   \bar v=\frac{4Q}{\pi D}

Note that the velocity gradient is independent of viscosity (and hence temperature) for laminar flow. This is because the total amount of fluid deformation is simply based on geometry. The no slip condition, the diameter, and the length of the flow passage set the total fluid deformation. Of course, if temperature decreases and viscosity increases the amount of energy required to push the fluid through the flow passage will increase (head loss is proportional to viscosity for laminar flow).

For turbulent flow and for flow expansions the amount of fluid deformation decreases as the viscosity increases and the total energy required to send the flow through the reactor is almost independent of the viscosity. The “almost” is because for wall shear under turbulent conditions there is a small effect of viscosity that is buried inside the friction factor.

.. _table_EDR_G_max_equations:

.. csv-table:: Equations for maximum (wall) energy dissipation rates and wall velocity gradients.
   :header: "Geometry", "Energy dissipation rate at the wall", "Velocity gradient at the wall"
   :align: left

   "Straight pipe", ":math:`\varepsilon_{wall} = \frac{1}{\nu}\left({\rm f}  \frac{\bar v^2}{8} \right)^2`", ":math:`G_{wall} ={\rm f}  \frac{\bar v^2}{8\nu}`"
   "Straight pipe laminar", ":math:`\varepsilon_{wall} = \left(\frac{8\bar v}{D} \right)^2 \nu`", ":math:`G_{wall} =  \frac{8\bar v}{D}`"
   "parallel plates laminar
   ", ":math:`\varepsilon_{wall} = 36\left( \frac{\bar v}{S}\right)^2 \nu`", ":math:`G_{wall} = \frac{6 \bar v}{S}`"
   "Coiled pipe laminar", "-", ":math:`G_{CS_{wall_{coil}}} ={\rm f} \left[ 1 + 0.033\left(log_{10}De\right)^4 \right]\frac{\bar v^2}{8\nu}`"


.. _table_EDR_G_equations:

.. csv-table:: Equations for maximum energy dissipation rates and velocity gradients for flow expansions.
   :header: "Geometry", ":math:`\Pi_{Jet}`", "Maximum energy dissipation rate", "Maximum velocity gradient"
   :align: left

   "Round jet", "0.08", ":math:`\varepsilon_{Max} = \Pi_{JetRound}\frac{   \bar v_{Jet} ^3}{D_{Jet}}`", ":math:`G_{Max} = \bar v_{Jet} \sqrt{\frac{\Pi_{JetRound} \bar v_{Jet} }{\nu D_{Jet}}}`"
   "Plane jet", "0.0124", ":math:`\varepsilon_{Max} = \Pi_{JetPlane} \frac{  \bar v_{Jet} ^3}{S_{Jet}}`", ":math:`G_{Max} = \bar v_{Jet}\sqrt{\frac{\Pi_{JetPlane} \bar v_{Jet}}{\nu S_{Jet}}}`"
   "Behind a flat plate", "0.04", ":math:`\varepsilon _{Max} = \Pi_{Plate}\frac{\bar v^3}{W_{Plate}}`", ":math:`G_{Max} = \bar v\sqrt{\frac{\Pi_{Plate} \bar v}{\nu W_{Plate}}}`"

For mechanical mixing where an impeller or other stirring device is adding shaft work to a control volume we have

.. math::  \bar\varepsilon = \frac{P}{m} = \frac{P}{\rho \rlap{-}V}

| where
| :math:`P` = power input into the control volume
| :math:`m` = mass of fluid in the control volume
| :math:`\rlap{-}V` = volume of the control volume
| :math:`\rho` = density of the fluid

The Camp-Stein velocity gradient for a mechanically mixed reactor is

.. math::  G_{CS} = \sqrt{\frac{P}{\rho \nu \rlap{-}V}}
