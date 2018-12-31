This is some dummy text

.. code:: python

    from aguaclara.core import constants as con
    import aguaclara.core.physchem as pc
    from aguaclara.core.units import unit_registry as u
    import aguaclara.core.utility as ut
    import numpy as np
    import matplotlib.pyplot as plt

    WaterElevationNormalized = np.linspace(-1,2,100)
    DiamOrifice = 5*u.cm
    WaterElevation = WaterElevationNormalized*DiamOrifice

    #Here we initialize some empty numpy arrays of the same size and type as WaterElevationNormalized
    HorizontalOrificeFlows = np.empty_like(WaterElevationNormalized)
    VerticalOrificeFlows = np.empty_like(WaterElevationNormalized)

    #Here we need to populate the arrays we created above.
    # Our graphing library, pyplot, cannot handle units, so we need to remove
    # them from each element as we insert it into the array.
    # While the code looks somewhat ugly, this is the best place to remove units;
    # we are removing them after all calculations have been made to minimize the
    # severity of floating-point errors.
    for i in range(len(WaterElevation)):
      HorizontalOrificeFlows[i] = (pc.flow_orifice(DiamOrifice, WaterElevation[i], con.VC_ORIFICE_RATIO).to(u.L/u.s).magnitude)
      VerticalOrificeFlows[i] = (pc.flow_orifice_vert(DiamOrifice, WaterElevation[i], con.VC_ORIFICE_RATIO).to(u.L/u.s).magnitude)

    fig, ax = plt.subplots()
    ax.plot(WaterElevationNormalized, HorizontalOrificeFlows, 'r-', WaterElevationNormalized, VerticalOrificeFlows, 'b-')

    ax.set(xlabel='Normalized height of water above center of the orifice')
    ax.set(ylabel='Flow rate through the orifice (L/s)')
    ax.legend(['Horizontal Orientation', 'Vertical orientation'])
    ax.grid(True)
    fig.savefig('Flow_Control_and_Measurement/Images/Horizontal_vs_Vertical_Orifice_Orientation')
    plt.show()

This is more dummy text
