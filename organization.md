## "Constants"
- 6 filter layers
- 75 cm of head max + signal for backwash (diff for plantita/ostars)
- sand layers are 20 cm (except for estars for plantita, then 15cm)
- branch spacing is 1/2 sand layer height
- max orifice size is 1/4"
- possible orifice sizes are 1/16, 1/8, 3/16, 1/4 inch
- drains must be large enough so they flow can exit with 10cm head
- head loss in orifices <5 cm (from dec-18 comments)
- head loss in sand is 1.2 m (because of the depth of the sand)

## Inputs
- plant flow

## Outputs
- number of filters --> amt of materials
- sizes of filters (this is a complex output) (most generally, an output could look like: 3 2ft estars)

## Conditions that must be met + things that are true
- inlet/outlet pipes must touch the floor
- for now the exits are slotted pipes
- inlets have wings
- branches go through trunks (thus trunk area matters so the branches don't act like valves)
- entrance tank contains: settled water inlet, four filter inlet pipes, overflow pipe, drain pipe (can overflow go back to sed tank?)
- exit tank contains: plant exits, three filter outlets, drain
- even flow across all branches
- even flow in all trunks
- even flow between filters
- air vent on filter body
- sand drain on filter body (only open if you want a big mess!)
- max flow is the backwash flow is the design flow is the flow a size if set for! 

## Need algorithms that:
- take in flow and return number/size (the big one)
    - plant flow --> \[array of pipe diameters] --> \[Q_filter for one filter of each diameter] --> \[Qplant/QFi (N_filt)]
    - then select the lowest number greater than 2 to the the number of filters chosen of a diameter 
    - this is the same algorithm that the tubes in the chemical dosing system use
    - diameters: (1, 1.5, 2, 3); flows: (.764, 1.608, 3.07, 7.024)
    - determine if we use 1.5 ft!
- take in size of filter and output dimensions for all components
  - diameters for all pipes
  - spacing of components
  - entrance and exit tank sizes
  - orifice conditions (number, diameter, spacing)
    - N_orifice*A_orifice = A_orificetotal
    - Q_filter/A_orificetotal = V_orifice **this is what needs to be limited to keep orifice headloss small!**
    - maximum orifice size is 1/4" 
    - should spacing be half the distance of the branch spacing to keep the relative spacing even between "level"; 5cm?
    - number of orifices depends on length of branches which is totally from geometry --> (slightly fewer orifices on BW level)
    - maximum orifice velocity comes from the ratio of the PR to the HL_sand
  - lengths for pipes (trunks, branches, heights of tanks, inlet + outlet piping)
  - amt of pipe for inlet wings
  - number of branches f(velocity) 
