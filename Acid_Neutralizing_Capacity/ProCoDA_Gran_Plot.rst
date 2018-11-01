

Using ProCoDA Gran Plot
=======================

.. |ProCoDA_save_gran| image:: Images/ProCoDA_save_gran.png
.. |ProCoDA_launch_gran_plot| image:: Images/ProCoDA_launch_gran_plot.png
.. |ProCoDA_get_titration_values| image:: Images/ProCoDA_get_titration_values.png
.. |ProCoDA_incremental_titrant_added| image:: Images/ProCoDA_incremental_titrant_added.png
.. |ProCoDA_Accept_pH_Value| image:: Images/ProCoDA_Accept_pH_Value.png
.. |ProCoDA_End_Titration| image:: Images/ProCoDA_End_Titration.png


1. Open the ProCoDA II software in the ProCoDA II folder on the desktop.
1. Connect and calibrate your pH probe as you did in the Acid Precipitation laboratory.
1. The Gran technique is used to measure acid or base neutralizing capacity.  To begin a Gran analysis, navigate to configuration, select volts, select pH cal, and click on |ProCoDA_launch_gran_plot|.
1. You will be prompted for the normality of titrant and the volume of sample.  You can also choose to measure ANC (acid neutralizing capacity) or BNC (base neutralizing capacity). If you are measuring BNC you will need to titrate with a strong base. After entering the normality of acid (or base) and the sample volume the computer will suggest an incremental volume of titrant that will produce a good Gran plot. Smaller incremental titrant volumes can be used, but will require more time to titrate the sample. After entering the values, exit the dialog box by clicking on the OK button. It will look like this:
 |ProCoDA_get_titration_values|
1. The Gran Plot analysis uses 3 controls: |ProCoDA_incremental_titrant_added|, |ProCoDA_Accept_pH_Value|, and |ProCoDA_End_Titration|. The "incremental titrant added" is the amount of acid added since the previous time the |ProCoDA_Accept_pH_Value| button was clicked. For the first data point if no titrant was added the "incremental titrant added" should be set to zero. For subsequent readings, change the incremental titrant added to the volume you are adding, add the titrant with a digital pipette, wait for the pH to stabilize and then click on |ProCoDA_Accept_pH_Value|. Any amount of titrant can be added at each step, but it is important that below pH 5 the titrant volumes be smaller than the recommended value so that sufficient data points are obtained in the linear region.
 1. There is no way to delete unwanted data points after they are accepted. Therefore, make sure you only press the enter button once after each addition of titrant.
 1. Continue adding titrant until a line is fit through the linear region of the data. When the line is drawn through the linear region press |ProCoDA_End_Titration|. Note that |ProCoDA_End_Titration| accepts the last data point and ends the titration. |ProCoDA_End_Titration| is pressed after the last addition of acid INSTEAD of pressing |ProCoDA_Accept_pH_Value|}!
 1. The equivalent volume (:math:`V_e`) is given in the same units as were used for the titrant and sample volumes. The equivalent volume is the abscissa intercept of the line fit to the data in the region of constant slope. The ANC is given in equivalents per liter.
 1. If desired the titration data can be saved in a format that can be read by spreadsheet programs by selecting  |ProCoDA_save_gran|. You will be prompted for a file name and location.
