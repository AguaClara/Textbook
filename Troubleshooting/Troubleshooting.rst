
Can we make some sort of a diagnostic guide based on symptoms? Make the following into a giant table.





Problems
---------


Temperature fluctuations

Calcium from calcium hypochlorite combines with carbonate in the water to form low solubility calcium carbonate.


Solutions
---------

Drip chlorine into water rather than injecting it to eliminate formation of precipitate at the injection point

Use valves at the end of the pipeline to control transmission line flow rate rather than upstream control. Review the transmission line to ensure that all sections of the line have flow controlled by limiting available driving head. Air entrainment occurs when the available head exceeds the head required to transmit the target flow.

.. _table_Troubleshooting:

.. csv-table:: Table of symptoms, problems, and solutions for AguaClara plant operation.
   :header: "Observation", "Problem", "Solution"
   :align: left

   Air bubbles, Air entrainment in the transmission line and transport to a high pressure zone in the pipeline where the air is dissolved in the water. ,
   Bubbles in sedimentation tanks,
   Bubbles in EStaRS, water entering the plant is supersaturated with air and EStaRS filters operate at very low pressure (compared with OStaRS), eliminate air entrainment in transmission line
    , , add a unit process (TBD) that removes excess dissolved air
   Rising flocs,
   Short filter runtimes, poor performance of floc/sed system
   Gradual increase in post backwash head loss in filters,
   Scale deposition in the distribution system,
   Clogging of chlorination system tubes and formation of precipitate at the injection point,


High head loss after backwash in EStaRS
=======================================

The 60 cm diameter EStaRS filters at El PODA had a very high head loss of 43 cm within a few minutes of ending backwash. The maximum available head is only 50 cm and thus filter runs lasted only a few hours. El PODA was the 2nd site where 60 cm diameter EStaRS filters were used. Given that the filter backwashed just fine without excess head required it appeared that the inlet system was performing as expected and did not have excessive head loss.

The key insight was that the top two layers of sand stopped producing filter water soon after beginning a filter run. A complete stoppage means that clogging ISN'T the issue! Clogging would decrease the flow rate, but it wouldn't stop flow because the clogging would have to be absolute to stop the flow.

The failure was that the water traveling horizontally in the branches and trunk carries air bubbles to the vertically downward flowing pipe (see a photo here). The air accumulates in that pipe and the water falls through the air losing energy like a waterfall. Water completely stops flowing through the layers of the filter that exit through that trunk line when the height of the air is equal to the available energy driving water through the StaRS filter.

There are two improvements required at El PODA. First, the transmission line must be operated with downstream flow control to prevent air entrapment and compression. That will likely be sufficient to solve the problem of air in the filters. The second improvement is to add manual air release valves to the top of each of the trunk lines so that operates can expel air during filtration. Note that these air vents must have a valve that is closed during backwash because the filter is under negative pressure during backwash and would suck air into the filter through those vents if they were open.

Slime at Las Vegas
==================
Iron bacteria slime showed up with application of hydrochloric acid at Las Vegas. The acid was needed to slightly reduce the pH to reduce the amount of encrustation in the distribution system. The addition of acid was correlated with the growth of a slime in the flocculator and sedimentation tanks. It was hypothesized that this slime was iron oxidizing bacteria (see :numref:`figure_Las_Vegas_Slime`).

.. _figure_Las_Vegas_Slime:

.. figure:: Images/Las_Vegas_Slime.jpg
   :width: 400px
   :align: center
   :rotate: right
   :alt: Oxygenation_vs_time

   The slime at Las Vegas showed up in the flocculator and sedimentation tanks.

Iron oxidizing bacteria need oxygen and reduced iron. The Las Vegas water source is a stream that is clearly groundwater given its propensity to deposit calcium carbonate on everything in the stream. Thus the stream water is likely poor in oxygen.

We are adding oxygen at the LFOM. That oxygen can chemically oxidize the iron, but the rate of oxidation is a function of pH (see :numref:`figure_Oxygenation_vs_time`). When we decrease the pH it slows the oxidation of iron and thus keeps a higher concentration of reduced iron available for bacteria to oxidize. Thus the LFOM adds oxygen needed by the iron oxidizing bacteria and the acid prevents the iron from being chemically oxidized.

`The rate of iron oxidation is strongly pH dependent <https://njaes.rutgers.edu/pubs/fs516/>`_
At pH 7.0, 90% Fe+2 oxidation requires 1 hour at 21°C and 10 hours at 5°C.
At pH 8.0, 90% Fe+2 oxidation occurs in 30 seconds.
At pH 6.0 it requires 100 hours.

.. _figure_Oxygenation_vs_time:

.. figure:: Images/Oxygenation_vs_time.png
   :width: 400px
   :align: center
   :alt: Oxygenation_vs_time

   The time required for oxidation is strongly dependent on pH. From `Lenntech <http://www.lenntech.com/iron-bacteria.htm>`_.

For several reasons, routine chemical disinfectants that effectively wipe out other bacteria are only modestly successful against iron bacteria. Iron bacteria build up in thick layers, each forming a slime around bacterial cells that keeps disinfectants from penetrating beyond the surface cells. Chemical reactions occur far slower at the cool temperatures common in wells, and bacterial cell need a long exposure to the chemical for the treatment to be effective. Even if chlorine kills all the bacterial cells in the water, those in the groundwater can be drawn in by pumping or drift back into the well. `Read more about chlorine and iron oxidizing bacteria <http://www.lenntech.com/iron-bacteria.htm#ixzz4ehUFJwO6>`_


Proposed solutions
------------------

 - Move the acid addition point to the end of the plant. This will allow chemical oxidation and removal of the iron. Note that once the iron is oxidized it precipitates as Fe(OH)3 and that is a wonderful coagulant. This is why the Las Vegas plant was shown to produce clean water even without addition of a coagulant!
 - Move chlorination to the rapid mix. This might work, but given the chlorine resistance of the slime and the disadvantages of prechlorination for production of disinfection by-products, we don't recommend this.
