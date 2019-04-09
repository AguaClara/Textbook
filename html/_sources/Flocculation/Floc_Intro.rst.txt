.. _title_Flocculation_Introduction:

**************************
Flocculation Introduction
**************************


Flocculation transform inorganic (clays such as `kaolinite, smectite, etc. and metallic oxy-hydroxides such as goethite and gibbsite <https://www.sciencedirect.com/science/article/pii/S0048969708010103>`_) and organic (viruses, bacteria and protozoa) primary particles into flocs (particle aggregates). Flocculation doesn’t remove any particles from suspension. Instead it causes particle aggregation and then floc blankets, lamellar sedimentation, and sand filtration will be used to separate those flocs from the water. Sedimentation can remove flocs more easily than it can remove primary particles because flocs have a higher terminal sedimentation velocity. Floc blankets and sand filtration rely primarily on capture based on interception and interception is much more efficient when the particles are larger. Thus the purpose of flocculation is to join **all** of the primary particles together into flocs (See movie in :numref:`figure_Collisions_in_Sequence`).

.. _figure_Collisions_in_Sequence:

.. figure:: Images/Collisions_in_Sequence.png
   :target: https://youtu.be/NIgP56htShw
   :width: 400px
   :align: center
   :alt: Random walk toward a collision

   Clay particles with attached coagulant nanoparticles collide due to fluid deformation. They grow in size quickly. The challenge is to catch the last few primary particles that failed to participate in the aggregation process.

Given that hydraulic flocculators approach plug flow conditions it is reasonable to assume that at any given location in the flocculator there is a predominance of one size of flocs. Thus collisions between similar sized flocs are most likely because that is what is present. There is also a hydrodynamic reason why similar sized flocs are favored which we will discuss later. For simplicity of modeling let's assume that flocs repeatedly double in size as suggested by the movie in :numref:`figure_Collisions_in_Sequence`. In that case, the number of primary particles in a floc is given by

.. math::
   :label: eq_n_primary_of_n_collisions

   n_{primary} = 2^{n_{collisions}}

If we assume (and we will show this assumption to be wrong in the next step) that the floc volume is directly proportional to the total volume of the primary particles in the floc, then we can rearrange :eq:`eq_n_primary_of_n_collisions` to solve for the number of sequential collisions required to increase the number of primary particles by a factor of 1000,000,000.

.. math::
   :label: n_collisions_not_fractal

    n_{collisions} = \frac{log(n_{primary})}{log(2)}

.. code:: python

    from aide_design.play import*
    n_primary = 1000000000
    n_collisions = np.log10(n_primary)/np.log10(2)
    print(n_collisions)

30 sequential collisions would be required to produce a floc that contains 1 billion primary particles.

Flocs are Fractals
==================

As flocs combine they don't coalesce like mist turning into rain drops. Instead they form loose aggregates that contain a higher and higher fraction of water in the voids between the solid primary particles.

Although the obvious flocculation advantage is that it produces larger aggregates that are easier to remove, it is also **possible** (this is a hypothesis that needs testing) that a difference in a physical property between primary particles and flocs plays a role in enhanced removal of flocs in floc blankets and filters. For example, the many relatively weak connection points between the primary particles in the flocs enables the flocs to deform. It is possible that deformation plays an important role right at the moment of collision. Presumably the bond strength required to lock the colliding particles together is less if the particles can deform as they are colliding.

The size change produced by flocculation is dramatic. Clay particles and pathogens have sizes that are order :math:`\mu m` and they combine to form flocs that are order :math:`mm`. A thousand fold increase in diameter suggests a billion fold increase in volume.



.. _figure_Flocs_are_fractals:

.. figure:: Images/Flocs_are_fractals.png
   :target: https://youtu.be/tAAC-KY8ZgA
   :width: 400px
   :align: center
   :alt: Flocs are fractals

   The amount of water contained within a volume defined by the floc increases as the flocs grows.

Flocculation is (or used to be) a Slow Process
==============================================

One of the mysteries of flocculation has been why it is such a slow process, requiring 30 minutes according to conventional design, and yet it appears to be a very rapid process. Plant operators observe that with high raw water turbidities that they can see flocculation progressing after about 0.5 minutes of flocculation. We can estimate the collision potential, :math:`G\theta` that corresponds to making visible flocs.

.. math:: \bar G = \sqrt{ \frac{g h_e}{\theta \nu}}

.. code:: python

    from aide_design.play import*
    from aguaclara_research.play import*
    HL_floc = 43*u.cm
    HRT = 8 * u.min
    Temperature =20 * u.degC
    G_floc = ((pc.gravity*HL_floc/(HRT*pc.viscosity_kinematic(Temperature)))**0.5).to_base_units()
    print(G_floc)
    Gt_floc = G_floc*HRT
    HRT_floc_visible = 0.5*u.min
    Gt_floc_visible = (G_floc*HRT_floc_visible).to_base_units()
    print(Gt_floc_visible)

Here initial flocculation is visible at a :math:`G\theta` of less than 3000. Given that flocculation is visible at this low collision potential, it is unclear why recommended :math:`G\theta` are as high as 100,000. This is one of the great mysteries that motivated the search for a flocculation model that was based on hypotheses that were consistent with laboratory and field observations.

Surface Charge Hypothesis
=========================

The mechanism of particle-particle aggregation was thought to be controlled by an average surface charge. Apparently no one was able to develop a model of how that mechanism would influence particle attachment efficiency and the result was that no predictive models for flocculation were developed. There were several observations that were at odds with conventional explanations of flocculation.

    1. Efficient flocculation at coagulant dosages that led to positive surface charge. This led to a second flocculation mechanism that was called “sweep floc” and that was used to describe any observations that didn’t fit the charge neutralization flocculation hypotheses.
    2. Flocculation time for highly turbid suspensions was expected to proceed very rapidly and produce very low turbidity settled water. This expectation was not observed and led to the hypothesis that flocs were continually breaking up and producing primary particles or at least very small flocs.
    3. The floc break up hypotheses led to the expectation that high turbidity suspensions would have significantly higher settled water turbidity than low turbidity suspensions. This expectation was also not observed.

Evidence that the charge neutralization hypothesis doesn’t explain flocculation of surface waters has been accumulating for decades. *Sweep* flocculation has been proposed as an alternative "mechanism" that described common observations that didn’t fit the charge neutralization hypothesis. However, similar to the charge neutralization hypothesis, the *sweep* hypothesis didn’t result in the development of predictive equations to describe the process.

For example, in 1992 Ching, Tanaka, and Elimelech published their research on `Dynamics of coagulation of kaolin particles with ferric chloride <https://doi.org/10.1016/0043-1354(94)90007-8>`__. They found
that the electrophoretic mobility which is a measure of the clay particle surface charge was never neutralized at pH 7.8 and was neutralized at :math:`10\mu M` at pH 6.0. The results were interpreted by the authors to mean that some combination of sweep floc and charge patchiness was responsible for the observed results.

See :numref:`figure_Ching_Electrophoretic_Mobility_vs_Ferric_Chloride` showing that at pH 7.8 the ferric chloride was still negatively charged and yet succeeded in flocculating the water to almost the same extent as the ferric chloride  at ph 6.0 that was postively charged (see :numref:`figure_Ching_Residual_Turbidity_vs_Ferric_Chloride`).

.. _figure_Ching_Electrophoretic_Mobility_vs_Ferric_Chloride:

.. figure:: Images/Ching_Electrophoretic_Mobility_vs_Ferric_Chloride.png
    :width: 300px
    :align: center
    :alt: internal figure

    `Electrophoretic Mobility for final pH <https://doi.org/10.1016/0043-1354(94)90007-8>`__ (after coagulant addition) of 6.0 and 7.8 as a function of :math:`FeCl_3` dose


.. _figure_Ching_Residual_Turbidity_vs_Ferric_Chloride:

.. figure:: Images/Ching_Residual_Turbidity_vs_Ferric_Chloride.png
    :width: 300px
    :align: center
    :alt: internal figure

    `The settled water turbidity was almost independent of pH even though the electrophoretic mobility was quite different for the two pH values tested <https://doi.org/10.1016/0043-1354(94)90007-8>`__.


`At pH 6.0 the ferric hydroxide precipitates are positively charged and at pH 7.8 they are close to neutral <https://doi.org/10.1016/0043-1354(94)90007-8>`__. Thus it is apparent that neutralization of the clay surface charge can not explain these results.

Electrostatic charge neutralization hypothesis

The coagulant precipitate self aggregates – this is inconsistent with the positive charge that the electrostatic hypothesis asserts will prevent aggregation \* Electrostatic repulsion extends only a few nm from the surface of a particle – and the coagulant adhesive nanoparticles are many times larger than the reach of the repulsive electrostatic force. The hypothesis that London van der Waals forces result in attachment neglects to account for the presence of water in the system. Water molecules will also be attracted to surfaces by London van der Waals forces and thus there will be competition between the coagulant and water. Thus eliminating repulsion is NOT sufficient to produce a bond between the particles. (see `hydration repulsion, page 21 <https://vtechworks.lib.vt.edu/bitstream/handle/10919/30137/Chapter1.pdf?sequence=9>`__) ` "The theory of DLP was a great step forward in that it appeared to circumvent the whole intractable problem of many body forces through its use of measured bulk dielectric response functions. However, it must be stressed again that it is a perturbation theory. That is, it depends on the assumption that an intervening liquid between interacting surfaces has bulk liquid properties up to a molecular distance from the surfaces. This is thermodynamically inconsistent, being equivalent to the statement that surface energies (or alternatively, the positions of the Gibbs dividing surfaces) are changed infinitesimally with distance of separation. This limits the theory to large distances (Young–Laplace vs. Poisson again) where large is undefined." <https://doi.org/10.1016/S0001-8686(99)00008-1>`__


AguaClara Flocculation History
==============================

2005 - We used conventional guidelines based on velocity gradient to design the first low flow vertical flocculator

2010 - We designed using energy dissipation rate and accounted for the nonuniformity of the energy dissipation rate (:math:`\theta` = 15 minutes)

2015 – We added obstacles to decrease the distance between expansions to make all of our flocculators have maximum collision efficiency (:math:`\theta` = 8 minutes)

2016 – Learned that particle/floc collisions are dominated by viscous shear (not by turbulent eddies). Began designing flocculators based on a target head loss of 40 cm. Used a :math:`G\theta` of 37,000.

2017 - Designed a pipe flocculator for the 1 L/s plant with a :math:`G\theta` of 20,000 and a residence time of about 100 s.


#references `Coagulation and Flocculation in Water and Wastewater Treatment <https://www.iwapublishing.com/news/coagulation-and-flocculation-water-and-wastewater-treatment>`__,
iwapublishing
