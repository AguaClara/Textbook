.. _equations:

**************************
Equations
**************************

.. _table_dimension_table:

.. csv-table:: Equation formats
    :header: Number, Name, Equation, Function
    :widths: 10, 30, 60, 10
    :align: center

    1, `Particle terminal velocity <https://aguaclara.github.io/Textbook/Introduction/Introduction.html#equation-eq-laminar-terminal-velocity>`_, :math:`\bar v_t = \frac{D_{particle}^2 g}{18 \nu} \frac{\rho_p - \rho_w}{\rho_w}`, 2
    2, `Continuity <https://aguaclara.github.io/Textbook/Review/Review_Fluid_Mechanics.html#equation-continuity-equation>`_, :math:`Q = \bar v A`, 2
    7, `Reynold's Number <https://aguaclara.github.io/Textbook/Review/Review_Fluid_Mechanics.html#equation-reynolds-number-equation>`_, :math:`{\rm Re} = \frac{\bar vD}{\nu} = \frac{4Q}{\pi D\nu} = \frac{\rho \bar vD}{\mu}`, `[+] <https://aguaclara.github.io/aguaclara/core/physchem.html#aguaclara.core.physchem.re_pipe>`_
    8, `Bernoulli <https://aguaclara.github.io/Textbook/Review/Review_Fluid_Mechanics.html#equation-bernoulli-equation>`_, :math:`\frac{p_1}{\rho g} + {z_1} + \frac{v_1^2}{2g} = \frac{p_2}{\rho g} + {z_2} + \frac{v_2^2}{2g}`, 2
    10, `Energy <https://aguaclara.github.io/Textbook/Review/Review_Fluid_Mechanics.html#equation-energy-equation>`_, :math:`\frac{p_{1}}{\rho g} + z_{1} + \frac{\bar v_{1}^2}{2g} = \frac{p_{2}}{\rho g} + z_{2} + \frac{\bar v_{2}^2}{2g} + h_L`, 2
    11, `Darcy-Weisbach <https://aguaclara.github.io/Textbook/Review/Review_Fluid_Mechanics.html#equation-darcy-weisbach>`_, :math:`h_{\rm{f}}  = {\rm{f}} \frac{L}{D} \frac{\bar v^2}{2g}` , `[+] <https://aguaclara.github.io/aguaclara/core/physchem.html#aguaclara.core.physchem.headloss_major_pipe>`_
    14, `Swamee-Jain <https://aguaclara.github.io/Textbook/Review/Review_Fluid_Mechanics.html#equation-swamee-jain>`_, :math:`{\rm{f}} = \frac{0.25} {\left[ \log \left( \frac{\epsilon }{3.7D} + \frac{5.74}{{\rm Re}^{0.9}} \right) \right]^2}`, `[+] <https://aguaclara.github.io/aguaclara/core/physchem.html#aguaclara.core.physchem.fric_pipe>`_
    18, `Hagen-Poiseuille <https://aguaclara.github.io/Textbook/Review/Review_Fluid_Mechanics.html#equation-hagen-poiseuille>`_, :math:`h_{\rm{f}} = \frac{128\mu L Q}{\rho g\pi D^4}`, 2
    35, `Orifice <https://aguaclara.github.io/Textbook/Review/Review_Fluid_Mechanics.html#equation-orifice-equation>`_, :math:`Q = \Pi_{vc} A_{or} \sqrt{2g\Delta h}`, `[+] <https://aguaclara.github.io/aguaclara/core/physchem.html#aguaclara.core.physchem.flow_orifice>`_
    67, `Minor loss <https://aguaclara.github.io/Textbook/Review/Review_Fluid_Mechanics_Derivations.html#equation-minor-loss-equation>`_, :math:`{ {\rm{ \mathbf{Third form:} }} \quad h_e = \left( \frac{A_{out}}{A_{in}} -1 \right)^2 \frac{\bar v_{out}^2}{2g} = K_e \frac{\bar v_{out}^2}{2g} \quad {\rm where} \quad K_e = \left( \frac{A_{out}}{A_{in}} - 1 \right)^2 }`, `[+] <https://aguaclara.github.io/aguaclara/core/physchem.html#aguaclara.core.physchem.headloss_minor_pipe>`_
    68, `Fractal floc volume <https://aguaclara.github.io/Textbook/Flocs_Fractals_and_Forces/FFF_Intro.html#equation-v-floc-of-n-cp>`_, :math:`\rlap{-} V_{floc} = \rlap{-} V_{cp} n_{cp}^\frac{3}{\Pi_{fractal}}`, 3
    87, `Floc terminal velocity <https://aguaclara.github.io/Textbook/Flocs_Fractals_and_Forces/FFF_Intro.html#equation-vt-of-floc>`_, :math:`v_t = \frac{D_{cp}^2g}{18\nu}\frac{\rho_{cp} - \rho_{H_2O}}{\rho_{H_2O}} \left( \frac{D_{floc}}{D_{cp}} \right) ^{\Pi_{fractal}-1}`, 3
    94, `Max floc velocity gradient <https://aguaclara.github.io/Textbook/Flocs_Fractals_and_Forces/FFF_Intro.html#equation-gmax-of-d-floc>`_, :math:`G_{max} = \frac{4F_{bond}}{3 \pi \mu D_{floc_{max}}^2}`, 3
    122, `Camp-Stein velocity gradient <https://aguaclara.github.io/Textbook/Fluid_Deformation_and_Energy_Dissipation/FDED_Intro.html#equation-fluid-deformation-and-energy-dissipation-fded-intro-4>`_, :math:`G_{CS} = \sqrt{\frac{P}{\rho \nu \rlap{-}V}}`, `[+] <https://aguaclara.github.io/aguaclara/core/physchem.html#aguaclara.core.physchem.g_cs_ergun>`_
    149, `Einstein’s diffusion <https://aguaclara.github.io/Textbook/Fluid_Deformation_and_Energy_Dissipation/FDED_Derivations.html#equation-fluid-deformation-and-energy-dissipation-fded-derivations-21>`_, :math:`D_{Diffusion} = \frac{k_B T}{3 \pi \mu D_P}`, 4
    279, `Linear CDC <https://aguaclara.github.io/Textbook/Flow_Control_and_Measurement/FCM_Design.html#equation-flow-control-and-measurement-fcm-design-0>`_, :math:`Q_{Max Tube} = \frac{\pi D^2}{4} \sqrt{\frac{2 h_L g \Pi_{Error}}{\sum{K} }}`, 6
    284, `Tank with a valve <https://aguaclara.github.io/Textbook/Flow_Control_and_Measurement/FCM_Design.html#equation-flow-control-and-measurement-fcm-design-5>`_, :math:`\frac{Q}{Q_0} = 1 - \frac{1}{2} \frac{t}{t_{Design}} \frac{h_{Tank}}{h_0}`, 6
    336, `Mechanical power <https://aguaclara.github.io/Textbook/Rapid_Mix/RM_Intro.html#equation-rapid-mix-rm-intro-4>`_, :math:`P = \rho g Q \Delta h`, 7
    343, `Mixer flow rate <https://aguaclara.github.io/Textbook/Rapid_Mix/RM_Design.html#equation-rapid-mix-rm-design-5>`_, :math:`Q_{mixer} = g h_e t_{eddy}^2 \bar v_{exp}`, 7
    353, `Diffusion layer thickness <https://aguaclara.github.io/Textbook/Rapid_Mix/RM_Theory_and_Future_Work.html#equation-rapid-mix-rm-theory-and-future-work-1>`_, :math:`L_{Diff} \approx \left( \frac{2k_B T d_{Clay}}{3 \pi \mu  d_{CN} G}\right)^\frac{1}{3}`, 7
    375, `Coagulant nanoparticle application <https://aguaclara.github.io/Textbook/Rapid_Mix/RM_Theory_and_Future_Work.html#equation-rapid-mix-rm-theory-and-future-work-23>`_, :math:`t_{coagulant application} = \frac{2.3p C_{CN} \Lambda_{Clay}^2}{\pi G k d_{Clay} L_{Diff_{CN}} }`, 7
    407, `AguaClara floc model <https://aguaclara.github.io/Textbook/Flocculation/Floc_Model.html#equation-pclam>`_, :math:`p{C^\star}=\frac{3}{2}\log_{10}\left[\frac{2}{3}\left(\frac{6}{\pi}\right)^{2/3}k\pi\bar{\alpha}\bar G_{CS}\theta\phi_0^{2/3}+1\right]`, 8
    420, `Terminal floc velocity <https://aguaclara.github.io/Textbook/Flocculation/Floc_Design.html#equation-flocculation-floc-design-0>`_, :math:`\bar v_t = \frac{D_{particle}^2 g}{18 \nu} \frac{\rho_p - \rho_w}{\rho_w}`, 8
    426, `Collision potential <https://aguaclara.github.io/Textbook/Flocculation/Floc_Design.html#equation-flocculation-floc-design-5>`_, :math:`G_{CS} \theta = \sqrt{\frac{g h_L \theta}{\nu}}`, 8
    440, `Channel width <https://aguaclara.github.io/Textbook/Flocculation/Floc_Design.html#equation-flocculation-floc-design-19>`_, :math:`W_{Min \Pi_{H_eS}} = \frac{\Pi_{H_eS}Q}{H_e}\left( \frac{K}{2 H_e \nu G_{CS}^2} \right)^\frac{1}{3}`, 8
    445, `Height between expansions <https://aguaclara.github.io/Textbook/Flocculation/Floc_Design.html#equation-flocculation-floc-design-24>`_, :math:`H_{e_{Max}} = \left[ \frac{K}{2 \nu G_{CS}^2} \left( \frac{Q \Pi_{{HS}_{Max}}}{W_{channel}} \right)^3 \right]^\frac{1}{4}`, 8
    449, `Baffle spacing <https://aguaclara.github.io/Textbook/Flocculation/Floc_Design.html#equation-floc-baffle-spacing>`_, :math:`S = \left( \frac{K}{2 H_e G_{CS}^2 \nu } \right)^\frac{1}{3} \frac{Q}{W_{channel}}`, 8
    473, `Jet velocity <https://aguaclara.github.io/Textbook/Sedimentation/Sed_Design.html#equation-max-sed-tank-jet-velocity>`_, :math:`\bar v_{Jet} = \left(\frac{\tau_{max}}{\rho}\right)^\frac{1}{2} \left( \frac{\bar v_{z_{fb}} W_{Sed}}{\nu \Pi_{JetPlane}}\right)^\frac{1}{4}`, 9
    495, `Tube settler flow <https://aguaclara.github.io/Textbook/Sedimentation/Sed_Derivations.html#equation-sedimentation-sed-derivations-11>`_, :math:`Q_{Tube}=\frac{\bar v_{c}\pi D^2}{4} \left(\frac{L}{D} \cos \alpha +\sin \alpha \right)`, 9
    531, `Floc sedimentation velocity <https://aguaclara.github.io/Textbook/Sedimentation/Sed_Derivations.html#equation-sedimentation-sed-derivations-47>`_, :math:`v_{Slide} = \bar v_{z_{Plate}} \left[ \left( \frac{3D_{cp}}{Ssin^2\alpha} \right)^{\Pi_{fractal} - 1} \left( \frac{18 v_{z_{Plate}} \Phi \nu }{D_{cp}^2g} \frac{\rho_`, 9
    539, `Plate settler head loss <https://aguaclara.github.io/Textbook/Sedimentation/Sed_Derivations.html#equation-sedimentation-sed-derivations-55>`_, :math:`h_L = 2 \frac{\mu}{\rho g} \left( \frac{6 \bar v_{z_{Plate}}}{S sin^2 \alpha cos\alpha} \right) \left( \frac{ \bar v_{z_{Plate}}}{\bar v_c} -1 \right)`, 9
    549, `Floc filter head loss <https://aguaclara.github.io/Textbook/Sedimentation/Sed_Derivations.html#equation-sedimentation-sed-derivations-65>`_, :math:`h_L = H_{fb} \left( \frac{\rho_{clay}}{\rho_{H_2O}} - 1 \right) \frac{C_{clay}}{\rho_{clay}}`, 9
    560, `Diffuser width <https://aguaclara.github.io/Textbook/Sedimentation/Sed_Derivations.html#equation-sedimentation-sed-derivations-76>`_, :math:`W_{diff_min} = \frac{\bar v_{z_{fb}}W_{Sed}B_{diff}}{(\sqrt{2gh_{L_jet}})S_{diff}}`, 9
    621, `Backwash porosity <https://aguaclara.github.io/Textbook/Filtration/Filtration_Intro.html#equation-backwash-porosity>`_, :math:`\phi_{FiSandBw} = \frac{\phi_{FiSand} H_{FiSand} A_{Fi} + \left( H_{FiSandBw} - H_{FiSand} \right) A_{Fi}}{H_{FiSandBw} A_{Fi}}`, 10
    623, `Clean bed head loss <https://aguaclara.github.io/Textbook/Filtration/Filtration_Intro.html#equation-eq-carman-kozeny>`_, :math:`\frac{h_l}{H_{FiSand}} = 36 k \frac{\left( 1 - \phi_{FiSand} \right)^2}{\phi_{FiSand}^3} \frac{\nu \bar v_a}{g D_{60}^2}`, 10
    627, `Backwash head loss <https://aguaclara.github.io/Textbook/Filtration/Filtration_Intro.html#equation-filtration-filtration-intro-3>`_, :math:`h_{l_{FiBw}} = \frac{\rho_{Sand} - \rho_{Water}}{\rho_{Water}} \left( 1 - \phi_{FiSand} \right) H_{FiSand}\\or\\h_{l_{FiBw}} = H`, 10
    629, `Fluidization velocity <https://aguaclara.github.io/Textbook/Filtration/Filtration_Intro.html#equation-minimum-fluidization-velocity-sand>`_, :math:`\bar v_{MinFluidization} = \frac{\phi_{FiSand}^3 g D_{60}^2}{36 k \nu \left( 1 - \phi_{FiSand} \right)} \left( \frac{\rho_{Sand}}{\rho_{Water}} - 1 \right)`, 10
    701, `Sharp crested weir <https://aguaclara.github.io/Textbook/Hydraulics/Hydraulics_Intro.html#equation-sharp-weir-q-of-channel-depth>`_, :math:`Q = \Pi_{vc}\frac{2}{3} \sqrt{2g} w \left(H_{channel}\right)^\frac{3}{2}`, 11


