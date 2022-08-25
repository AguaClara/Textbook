.. raw:: html

    <embed>
       <link rel="canonical" href="https://aguaclara.github.io/Textbook/Fluids_and_Hydraulics/Manifold_Hydraulics.html" />
       <script src="https://hypothes.is/embed.js" async></script>
    </embed>

.. _title_plant_hydraulics:

****************
Plant Hydraulics
****************

Pipes that carry the plant flow rate are used for:

 * raw water from the source
 * linear flow orifice meter and connecting pipe from the entrance tank to the flocculator
 * bypass the plant taking the water from the entrance tank (by moving the linear flow orifice meter to the bypass socket) to the filter outlet tank where it is chlorinated
 * clarifier to filters
 * recycle backwash water to the entrance tank
 * finished water to distribution tank

See :cite:`plantHydraulics-kawamura2000integrated` recommends maximum velocities of about 2 m/s except where floc breakup is a concern. He also recommends that the plant hydraulics be designed to handle 1.2 to 1.5 of the plant design flow rate. If we use the less conservative factor we obtain a maximum plant pipe velocity of 1.7 m/s.

The bypass line requires a careful design because the elevation difference generally slightly more than 1 m and contains an entrance (K = 0.5), 6 elbows (K = 0.9), and an exit (K = 1). The minor loss equation gives a maximum velocity of 1.7 m/s without any additional safety factor.

The linear flow orifice (LFOM) is sized based on a maximum velocity of Equation :eq:`LFOM_V_max`. For the AguaClara standard LFOM head loss of 20 cm the maximum velocity is 0.84 m/s. With a safety factor of 1.2 this results in a maximum velocity of 0.7 m/s. Thus the LFOM requires a larger diameter pipe than the plant bypass line. Given the high cost of switching to larger pipes and fittings it is worth designing for the precise bypass line requirements rather than simple using the LFOM diameter for other pipes.

The plant bypass line, backwash recycle line and raw water pipes will all be designed using the bypass line nominal diameter. The bypass line will be designed based on the minor losses of the entrance, elbows, and exit as well as the total elevation difference between the entrance tank and the filter outlet tank.

Pipes used to connect the clarifier to the filter need to be designed in context because the head loss directly influences the overall plant head loss and hence the height of the building. In that case the head loss should be limited to about 0.1 m and ideally the pipe is a straight connection without any elbows. That results in a maximum velocity of about 1.1 m/s.

.. bibliography:: /references.bib
   :cited:
   :keyprefix: plantHydraulics-
