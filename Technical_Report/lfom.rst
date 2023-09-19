.. _title_LFOM:

****
LFOM
****

.. replace_keywords::

    This is a test with !KEYWORD1! and !KEYWORD2! in a block.

This is an inline test :replace_keywords_inline:`with !KEYWORD1! and !KEYWORD2!`.
Another inline test: :sub:`(hi) no-sub`

Test a table
------------

.. _table_LFOM_Specifications:

.. csv-table:: LFOM Specifications. (et.lfom)
   :header: "Parameter", "value", "AIDE variable name"
   :align: left
   :widths: 40 30 30

   Nominal pipe diameter, #ND#, ND
   Number of rows, !rowN!, rowN
   Max flow rate, !Qm_max!, Qm_max
   Head loss at max flow, !HL_max!, HL_max
   Orifices in each row starting from bottom row, !orificeNPerRow!, orificeNPerRow
   Elevation of each row from zero flow datum, !orificeHPerRow!, orificeHPerRow




Linear Flow Orifice Meter (LFOM)
--------------------------------

The LFOM is a weir shape cut into a pipe. It was meant to imitate `the Sutro Weir <https://confluence.cornell.edu/display/AGUACLARA/LFOM+sutro+weir+research>`_ while being far easier to build. The LFOM is a pipe with rows of holes, or orifices, drilled into it. There are progressively fewer holes per row as you move up the LFOM, as the shape is meant to resemble half a parabola on each side. The size of all holes is the same, and the amount of holes per row are precisely calculated. Water in the entrance tank flows into and down the LFOM, towards the rapid mix orifice and flocculator.

.. _figure_sutro_v_lfom:

.. figure:: ../Images/sutro_v_lfom.png
    :width: 600px
    :align: center
    :alt: A sutro weir and an LFOM

    On the left is a sutro weir. On the right is AguaClara's approximation of the sutro weir's geometery. This elegant innovation is called a linear flow orifice meter, or LFOM for short.

The LFOM does one thing and serves two purposes.

What it does:

**The LFOM creates a linear relationship between water level in the entrance tank and the flow out of the entrance tank.** *It does not control the flow through the plant*. If the LFOM were replaced with a hole in the bottom of the entrance tank, the same flow rate would go through the plant, the only difference being that the water level in the entrance tank would scale with flow squared :math:`h \propto Q^2` instead of :math:`h \propto Q`. For example, if an LFOM has 10 rows of holes and has been designed for a plant whose maximum flow rate is 10 L/s, then the operator knows that the number of rows submerged in water is equal to the flow rate of the plant in L/s. So if the water were up to the third row of holes, there would be 3 L/s of water flowing through the plant.

Why it is useful:

#. Allows the operator to measure the flow through the plant quickly and easily, explained above.
#. Allows for the Linear Chemical Dose Controller, which will be explained next, to automatically adjust the flow of coagulant/chlorine into the plant as the plant flow rate changes. This means the operator would only need to adjust the flow of coagulant when there is a change in turbidity or organic matter.

This is best understood with examples. By shaping a weir differently, different relationships between :math:`Q` and :math:`h` are formed:
* In the case of a `rectangular weir <https://swmm5.files.wordpress.com/2016/09/image00124.jpg>`_, :math:`Q \propto h^{\frac{3}{2}}`
* In the case of a `v-notch weir <https://swmm5.files.wordpress.com/2016/09/image0096.jpg>`_, :math:`Q \propto h^{\frac{5}{2}}`
* In the case of a `Sutro weir <http://www.engineeringexcelspreadsheets.com/wp-content/uploads/2012/11/Sutro-Weir-Diagram1.jpg>`_ and thus LFOM, :math:`Q \propto h`.


Before the water level reaches the second row of holes, the LFOM is simulating a rectangular weir, and thus :math:`h \not\propto Q`. The Sutro weir also experiences this problem. Similarly, if the water level exceeds the topmost row of the LFOM’s orifices, the linearity also breaks down. The entire LFOM begins to act like an orifice, the exponent of :math:`Q` in :math:`h \propto Q` becomes greater than 1. This is because the LFOM approaches orifice behavior, and for orifices, :math:`h \propto Q^2`.

The diameter of the LFOM pipe is set by the velocity of the falling water inside the LFOM at the bottom of the bottom row of orifices. This velocity is obtained by summing up all of the momentum of the falling water and dividing by the total flow for the case where the LFOM is operating at maximum capacity. The Sutro weir equations (not yet provided here) can be integrated to obtain an equation for the falling velocity of the water inside the LFOM. This maximum vertical velocity of the falling water sets the minimum flow area of the LFOM and hence continuity can be used to obtain the minimum pipe diameter.

.. math::
  :label: LFOM_V_max

    V_{max} = \frac{4}{3 \pi} \sqrt{2gh_L}
