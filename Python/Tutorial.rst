Best practices:

Import statements that may be required:

.. code:: python

    import aguaclara.core.physchem as pc
    from aguaclara.core.units import unit_registry as u
    import aguaclara.core.constants as con

    import numpy as np
    import matplotlib.pyplot as plt

    import aguaclara.research.floc_model as fm
    3*u.mg/u.L
    fm.


Useful hotkeys for executing code
---------------------------------

Hydrogen hotkeys are listed under Packages->Hydrogen, and are also detailed here.
Ctrl+Enter runs the currently selected line of code.
Shift+Enter works as Ctrl+Enter and also moves the selection to the next line of code.
Adding an Alt to the sequence will run the entire code block instead of a single line:
  Alt+Ctrl+Enter runs the current code block.
  Alt+Shift+Enter runs the current code block and moves the selection to the next block.
Alt+Ctrl+Shift+Enter runs all code in the current file.

Arrays and units
----------------

Use Numpy arrays rather than python lists to enable math with numbers and units.
When creating arrays with units remember that

 * Array elements don't have units!
 * Arrays can have units.

Therefore always attach units to the array after the array has been created.

We can use numpy linspace with a simple change to make it dimensionless. Usually linspace has
numpy.linspace(start, stop, num). We can change this to
numpy.linspace(start/stop, 1, num) * stop.
Of course, if start is zero, then this gets really simple!

Units can cause real confusion with arrays because linspace simply takes the magnitude
If start and stop have units we can make sure that the units don't cause us any problems. Below I used np.linspace to

.. code:: python
 n_rows = 10
 Flow = 20 * u.L/u.s
 Flow_array = np.linspace(1 / n_rows, 1,n_rows)*Flow
 print(Flow_array.magnitude,Flow_array.units)

 # create an array from 2 to 20 cm in 2 cm intervals
 unit_error_array = np.linspace(0,1*u.m/(100*u.cm),10) * 20 * u.cm
 unit_error_array
 # now fix it by making the units dimensionless first!
 unit_array = np.linspace(0,(1*u.m/(100*u.cm)).to(u.dimensionless),10) * 20 * u.cm
 unit_array


Plotting
--------

fig is a Figure instance—like a blank canvas
ax is an AxesSubplot instance—think of a frame for plotting in

fig, ax = plt.subplots()
ax.plot(x, y, 'r-', linewidth=2, label='sine function', alpha=0.6)
ax.legend(loc='upper center')
plt.show()

Before submitting a file for others to use, you need to verify that all of the dependencies are defined and that you didn't accidently delete a definition that is required. You can do this by placing your cursor in a python code section and then clicking on the python 3|idle in the toolbar at the bottom of the Atom window. Select restart Python 3 kernel. Then execute all of the python code in your document from top to bottom and make sure that all of the code performs as expected.
