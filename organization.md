## "Constants"
- 6 filter layers
- 75 cm of head max + signal for backwash (diff for plantita/ostars)
- sand layers are 20 cm (except for estars for plantita, then 15cm)
- branch spacing is 1/2 sand layer height
- max orifice size is 1/4"
- possible orifice sizes are 1/16, 1/8, 3/16, 1/4 inch
- drains must be large enough so they flow can exit with 10cm head
- head loss in orifices <5 cm (from dec-18 comments)
- head loss 

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
  - 1 LPS --> estars for plantita (smaler sand layers)
  - >1-3 4-1Ft
  - >3-6 2-2ft
  - >6-9 3-2ft
  - >9-12 4-2ft
  - >12-14 2-3ft
  - >14-21 3-3ft
  - (>16 OStaRS)
  - these based on max capacity of a single filter of each size.
- take 
