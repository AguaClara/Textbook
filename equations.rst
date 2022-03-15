.. _equations:

**************************
Equation Quick Reference
**************************

.. _table_dimension_table:

.. csv-table:: Equations
    :header: Number, Name, Equation, Python
    :align: center

    :eq:`eq_laminar_terminal_velocity`, Particle terminal velocity, :math:`\bar v_t = \frac{D_{particle}^2 g}{18 \nu} \frac{\rho_p - \rho_w}{\rho_w}`, 2
    :eq:`continuity_equation`, Continuity, :math:`Q = \bar v A`, 2
    :eq:`reynolds_number_equation`, Reynold's Number, :math:`{\rm Re} = \frac{\bar vD}{\nu} = \frac{4Q}{\pi D\nu} = \frac{\rho \bar vD}{\mu}`, `[+] <https://aguaclara.github.io/aguaclara/core/physchem.html#aguaclara.core.physchem.re_pipe>`_
    :eq:`bernoulli_equation`, Bernoulli, :math:`\frac{p_1}{\rho g} + {z_1} + \frac{v_1^2}{2g} = \frac{p_2}{\rho g} + {z_2} + \frac{v_2^2}{2g}`, 2
    :eq:`energy_equation`, Control Volume Energy, :math:`\frac{p_{1}}{\rho g} + z_{1} + \frac{\bar v_{1}^2}{2g} = \frac{p_{2}}{\rho g} + z_{2} + \frac{\bar v_{2}^2}{2g} + h_L`, 2
    :eq:`darcy_weisbach`, Darcy-Weisbach, :math:`h_{\rm{f}}  = {\rm{f}} \frac{L}{D} \frac{\bar v^2}{2g}` , `[+] <https://aguaclara.github.io/aguaclara/core/physchem.html#aguaclara.core.physchem.headloss_major_pipe>`_
    :eq:`swamee_jain`, Swamee-Jain, :math:`{\rm{f}} = \frac{0.25} {\left[ \log \left( \frac{\epsilon }{3.7D} + \frac{5.74}{{\rm Re}^{0.9}} \right) \right]^2}`, `[+] <https://aguaclara.github.io/aguaclara/core/physchem.html#aguaclara.core.physchem.fric_pipe>`_
    :eq:`hagen_poiseuille`, Hagen-Poiseuille, :math:`h_{\rm{f}} = \frac{128\mu L Q}{\rho g\pi D^4}`, 2
    :eq:`orifice_equation`, Orifice, :math:`Q = \Pi_{vc} A_{or} \sqrt{2g\Delta h}`, `[+] <https://aguaclara.github.io/aguaclara/core/physchem.html#aguaclara.core.physchem.flow_orifice>`_
    :eq:`minor_loss_equation`, Minor loss, :math:`{ {\rm{ \mathbf{Third form:} }} \quad h_e = \left( \frac{A_{out}}{A_{in}} -1 \right)^2 \frac{\bar v_{out}^2}{2g} = K_e \frac{\bar v_{out}^2}{2g} \quad {\rm where} \quad K_e = \left( \frac{A_{out}}{A_{in}} - 1 \right)^2 }`, `[+] <https://aguaclara.github.io/aguaclara/core/physchem.html#aguaclara.core.physchem.headloss_minor_pipe>`_
    :eq:`V_floc_of_n_cp`, Fractal floc volume, :math:`\rlap{-} V_{floc} = \rlap{-} V_{cp} n_{cp}^\frac{3}{\Pi_{fractal}}`, 3
    :eq:`vt_of_floc`, Floc terminal velocity, :math:`v_t = \frac{D_{cp}^2g}{18\nu}\frac{\rho_{cp} - \rho_{H_2O}}{\rho_{H_2O}} \left( \frac{D_{floc}}{D_{cp}} \right) ^{\Pi_{fractal}-1}`, 3
    :eq:`Gmax_of_d_floc`, Max floc velocity gradient, :math:`G_{max} = \frac{4F_{bond}}{3 \pi \mu D_{floc_{max}}^2}`, 3
    :eq:`G_Camp_Stein`, Camp-Stein velocity, :math:`G_{CS} = \sqrt{\frac{P}{\rho \nu \rlap{-}V}}`, `[+] <https://aguaclara.github.io/aguaclara/core/physchem.html#aguaclara.core.physchem.g_cs_ergun>`_
    :eq:`einstein_diffusion`, Einstein’s diffusion, :math:`D_{Diffusion} = \frac{k_B T}{3 \pi \mu D_P}`, 4
    :eq:`cdc_tube_Q_max`, Linear CDC, :math:`Q_{Max Tube} = \frac{\pi D^2}{4} \sqrt{\frac{2 h_L g \Pi_{Error}}{\sum{K} }}`, 6
    :eq:`Q_tank_with_valve`, Tank with a valve, :math:`\frac{Q}{Q_0} = 1 - \frac{1}{2} \frac{t}{t_{Design}} \frac{h_{Tank}}{h_0}`, 6
    :eq:`power_of_Q_h`, Mechanical power, :math:`P = \rho g Q \Delta h`, 7
    :eq:`Q_max_served_per_injection_port`, Flow per chemical injection port, :math:`Q_{mixer} = g h_e t_{eddy}^2 \bar v_{exp}`, 7
    :eq:`Gtheta_of_hL`, Collision potential, :math:`G_{CS} \theta = \sqrt{\frac{g h_L \theta}{\nu}}`, 8
    :eq:`W_min_HVFloc`, Channel width, :math:`W_{Min \Pi_{H_eS}} = \frac{\Pi_{H_eS}Q}{H_e}\left( \frac{K}{2 H_e \nu G_{CS}^2} \right)^\frac{1}{3}`, 8
    :eq:`floc_He_max_const_K`, Distance between expansions, :math:`H_{e_{Max}} = \left[ \frac{K}{2 \nu G_{CS}^2} \left( \frac{Q \Pi_{{HS}_{Max}}}{W_{channel}} \right)^3 \right]^\frac{1}{4}`, 8
    :eq:`Floc_baffle_spacing_of_K`, Baffle spacing, :math:`S = \left( \frac{K}{2 H_e G_{CS}^2 \nu } \right)^\frac{1}{3} \frac{Q}{W_{channel}}`, 8
    :eq:`max_sed_tank_jet_velocity_of_G`, Maximum jet velocity , :math:`\frac{\bar v_{M_1}}{\bar v_{P}} = \sqrt{\frac{2(1 - \Pi_{Q}^2)}{\Pi_{Q}^2 + 1}}`, 9
    :eq:`Q_tube_settler`, Tube settler flow, :math:`Q_{Tube}=\frac{\bar v_{c}\pi D^2}{4} \left(\frac{L}{D} \cos \alpha +\sin \alpha \right)`, 9
    :eq:`Plate_S_min_of_fractal`, Minimum plate settler spacing, :math:`S_{min} \approx \frac{3 \bar v_{z_{Plate}}}{\sin^2 \alpha} \left( \frac{18 \nu}{g D_{cp}} \frac{\rho_{H_2O}}{\rho_{cp} - \rho_{H_2O}} \right)`, 9
    :eq:`plate_settler_headloss`, Plate settler head loss, :math:`h_L = 2 \frac{\mu}{\rho g} \left( \frac{6 \bar v_{z_{Plate}}}{S sin^2 \alpha cos\alpha} \right) \left( \frac{ \bar v_{z_{Plate}}}{\bar v_c} -1 \right)`, 9
    :eq:`floc_filter_head_loss`, Floc filter head loss, :math:`h_L = H_{ff} \left( \frac{\rho_{clay}}{\rho_{H_2O}} - 1 \right) \frac{C_{clay}}{\rho_{clay}}`, 9
    :eq:`eq_carman_kozeny`, `Clean bed head los, :math:`\frac{h_l}{H_{FiSand}} = 36 k \frac{\left( 1 - \phi_{FiSand} \right)^2}{\phi_{FiSand}^3} \frac{\nu \bar v_a}{g D_{60}^2}`, 10
    :eq:`headloss_bw_sand`, `Backwash head loss, :math:`h_{l_{FiBw}} = H_{FiSand} \left( 1 - \phi_{FiSand} \right)  \left( \frac{\rho_{Sand}}{\rho_{Water}} - 1 \right)`, 10
    :eq:`minimum_fluidization_velocity_sand`, Fluidization velocity, :math:`\bar v_{MinFluidization} = \frac{\phi_{FiSand}^3 g D_{60}^2}{36 k \nu \left( 1 - \phi_{FiSand} \right)} \left( \frac{\rho_{Sand}}{\rho_{Water}} - 1 \right)`, 10
    :eq:`sharp_weir_q_of_channel_depth`, Sharp crested weir, :math:`Q = \Pi_{vc}\frac{2}{3} \sqrt{2g} w \left(H_{channel}\right)^\frac{3}{2}`, 11
