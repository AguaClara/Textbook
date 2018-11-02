.. _title_ProCoDA:

*********************************************
ProCoDA: Process Control and Data Acquisition
*********************************************


.. |config_calibrate_pump| image:: Images/config_calibrate_pump.png
.. |config_data_state_log| image:: Images/config_data_state_log.png
.. |config_edit_rules| image:: Images/config_edit_rules.png
.. |config_Logging_data_short_exp| image:: Images/config_Logging_data_short_exp.png
.. |Config_open_save_export| image:: Images/Config_open_save_export.png
.. |config_select_daq| image:: Images/config_select_daq.png
.. |config_sensors| image:: Images/config_sensors.png
.. |config_share_data| image:: Images/config_share_data.png
.. |DO_controls| image:: Images/DO_controls.png
.. |DO_set_barometric| image:: Images/DO_set_barometric.png
.. |DO_set_to_saturation| image:: Images/DO_set_to_saturation.png
.. |DO_zero| image:: Images/DO_zero.png
.. |Gran_accept_pH| image:: Images/Gran_accept_pH.png
.. |Gran_change_increment| image:: Images/Gran_change_increment.png
.. |Gran_end_titration| image:: Images/Gran_end_titration.png
.. |Gran_get_titration_values| image:: Images/Gran_get_titration_values.png
.. |Gran_incremental_titrant| image:: Images/Gran_incremental_titrant.png
.. |Gran_save| image:: Images/Gran_save.png
.. |Gran_start| image:: Images/Gran_start.png
.. |Logging_data| image:: Images/Logging_data.png
.. |Mode_of_operation| image:: Images/Mode_of_operation.png
.. |open_method| image:: Images/open_method.png
.. |photometer_open_save_export| image:: Images/photometer_open_save_export.png
.. |photometer_read_blank| image:: Images/photometer_read_blank.png
.. |photometer_read_dark| image:: Images/photometer_read_dark.png
.. |pH_add_buffer| image:: Images/pH_add_buffer.png
.. |pH_clear_buffers| image:: Images/pH_clear_buffers.png
.. |pH_controls| image:: Images/pH_controls.png
.. |pH_edit_buffers| image:: Images/pH_edit_buffers.png
.. |ProCoDA.pptx| image:: Images/ProCoDA.pptx.png
.. |sensor_clear_offsets| image:: Images/sensor_clear_offsets.png
.. |sensor_copy| image:: Images/sensor_copy.png
.. |sensor_delete| image:: Images/sensor_delete.png
.. |sensor_DO| image:: Images/sensor_DO.png
.. |sensor_edit_calibration| image:: Images/sensor_edit_calibration.png
.. |sensor_insert| image:: Images/sensor_insert.png
.. |sensor_linear_offsets| image:: Images/sensor_linear_offsets.png
.. |sensor_no_range_error| image:: Images/sensor_no_range_error.png
.. |sensor_open_calibration_file| image:: Images/sensor_open_calibration_file.png
.. |sensor_pH| image:: Images/sensor_pH.png
.. |sensor_photometer| image:: Images/sensor_photometer.png
.. |sensor_position_system| image:: Images/sensor_position_system.png
.. |sensor_range_error| image:: Images/sensor_range_error.png
.. |sensor_save_calibration_file| image:: Images/sensor_save_calibration_file.png
.. |sensor_set_to_value| image:: Images/sensor_set_to_value.png
.. |sensor_set_to_zero]| image:: Images/sensor_set_to_zero].png


The software combines 3 elements: sensors (inputs from the real world), set points (inputs from the plant operator and calculated values based on sensors and other set points), and logic (rules that govern how the plant should operate given the sensor data and set points). The software contains a graphical user interface where you can edit, save, and open files containing sensor information and files containing the set point and logic information.

.. _heading_ProCoDA_Sensors:

Sensors
=======

.. _heading_ProCoDA_Temperature_Measurement:

Temperature Measurement
-----------------------

#. Navigate to the Configuration tab
#. Click the 'volt' button to select and configure your sensor (thermistor).
#. Click 'insert sensor' to add a sensor to your list.  As the semester goes on, we will run experiments that require several sensors to be added here.  For now, we will use the single thermistor.
#. Now you need to tell the software where your sensor is plugged in.  In the 'channels' pull-down menu, select the address of your sensor.  All addresses begin with a Dev/ai prefix.
#. Finally, you need to tell the software to convert the signal into temperature units.  This is done with a calibration file.  Click 'open calibration file' (it looks like a regular open folder icon) and select the calibration file named thermistor.smc.
#. You should now be reading temperature in units of degrees Celsius. Verify that you are monitoring the correct temperature probe by holding the temperature probe in your hand and warming it up.  Does the temperature reading respond?


.. _heading_ProCoDA_pH_Measurement:

pH Measurement
--------------

 #. Open the ProCoDA II software.
 #. Navigate to the Configuration tab and select the volts button.
 #. Insert a new sensor at the bottom of the sensor list using the insert sensor button.
 #. Select the appropriate channel based on in which sensor port you plugged you pH probe.
 #. Select pH Cal.
 #. The pH probe should never be dry and is therefore stored with a small vial of pH 4.0 buffer screwed onto the tip.  Unscrew the storage vial cap and place the vial in a place where it will not be tipped over (the cap can stay on the probe).
 #. Rinse the pH probe with DI water (use a squeeze bottle) into a beaker.
 #. To calibrate the pH probe, we will use three pH buffer solutions with known pH (red=4.0, yellow=7.0, and blue=10.0).  After rinsing the pH probe, place it into the pH=4.0 buffer.  Stir gently and wait for the pH reading on the software to stabilize.  Once stabilized, press the add buffer button.  Rinse the pH probe with DI water and repeat for the pH=7.0 and pH=10.0 buffer solutions.
 #. When you have tested all calibration buffers, hit, OK. And OK again.

.. _heading_ProCoDA_Gran_Plot:

Gran Plot
---------




 #. Open the ProCoDA II software in the ProCoDA II folder on the desktop.
 #. Connect and calibrate your pH probe as you did in the Acid Precipitation laboratory.
 #. The Gran technique is used to measure acid or base neutralizing capacity.  To begin a Gran analysis, navigate to configuration, select volts, select pH cal, and click on |Launch_gran_plot|.
 #. You will be prompted for the normality of titrant and the volume of sample.  You can also choose to measure ANC (acid neutralizing capacity) or BNC (base neutralizing capacity). If you are measuring BNC you will need to titrate with a strong base. After entering the normality of acid (or base) and the sample volume the computer will suggest an incremental volume of titrant that will produce a good Gran plot. Smaller incremental titrant volumes can be used, but will require more time to titrate the sample. After entering the values, exit the dialog box by clicking on the OK button. It will look like this:
 |Get_titration_values|
 #. The Gran Plot analysis uses 3 controls: |Incremental_titrant|, |Accept_pH_value|, and |End_titration|. The "incremental titrant added" is the amount of acid added since the previous time the |Accept_pH_value| button was clicked. For the first data point if no titrant was added the "incremental titrant added" should be set to zero. For subsequent readings, change the incremental titrant added to the volume you are adding, add the titrant with a digital pipette, wait for the pH to stabilize and then click on |Accept_pH_value|. Any amount of titrant can be added at each step, but it is important that below pH 5 the titrant volumes be smaller than the recommended value so that sufficient data points are obtained in the linear region.
 #. There is no way to delete unwanted data points after they are accepted. Therefore, make sure you only press the enter button once after each addition of titrant.
 #. Continue adding titrant until a line is fit through the linear region of the data. When the line is drawn through the linear region press |End_titration|. Note that |End_titration| accepts the last data point and ends the titration. |End_titration| is pressed after the last addition of acid INSTEAD of pressing |Accept_pH_value|}!
 #. The equivalent volume (:math:`V_e`) is given in the same units as were used for the titrant and sample volumes. The equivalent volume is the abscissa intercept of the line fit to the data in the region of constant slope. The ANC is given in equivalents per liter.
 #. If desired the titration data can be saved in a format that can be read by spreadsheet programs by selecting  |Save_gran|. You will be prompted for a file name and location.

.. _heading_ProCoDA_Dissolved_Oxygen:

Dissolved Oxygen
----------------

When using the DO probe make sure that there *aren't any air bubbles* on the probe membrane. If you are aerating the sample place the probe as far from the air bubbles as possible. Air bubbles on the membrane will cause inaccurate readings.

 #. Connect a DO probe to one of the sensor ports on the ProCoDA box using the gold signal conditioning box.
 #. Navigate to the ProCoDA Configuration tab and select \includegraphics*[width=0.34in, height=0.34in, keepaspectratio=false]{image3} to configure the dissolved oxygen channel(s). Select the DO probe from the sensor list and point the channel to the correct sensor port.
 #. Use the dissolved oxygen calibration VI \includegraphics*[width=0.34in, height=0.34in, keepaspectratio=false]{image4} to calibrate the DO probe.
 #. Enter the temperature of the sample. This can be measured by using a thermistor or a thermometer. A good estimate is :math:`22^\circ C`.
 #. If you have typed in your location in the Configuration Tab, you can get the actual barometric pressure for Ithaca, New York by selecting \includegraphics*[width=1.89in, height=0.21in, keepaspectratio=false]{image5}
 #. Place the probe in oxygen saturated water (use the air jet on your bench to bubble air into water in a 4L container).  The voltage from the DO probe should be between 0.17 and 0.23 volts if the probe is working correctly. If the voltage is lower than 0.17 it may be time to replace the membrane or the solution may not be saturated with oxygen.
 #. Select \includegraphics*[width=1.12in, height=0.21in, keepaspectratio=false]{image6}to calibrate the DO sensor.
 #. Select OK \includegraphics*[width=0.91in, height=0.25in, keepaspectratio=false]{image7}when you are satisfied with the calibration.
 #. If desired you may save the calibration for later use \includegraphics*[width=0.25in, height=0.24in, keepaspectratio=false]{image8}. However, it is not necessary to save the calibration to use the calibration in the current session.~~If you want to save the calibration, save it in your Group folder on the S:/ drive.~~


.. _heading_ProCoDA_Meters:

Meters
======

 Turbidimeters, electronic balances, etc. that communicate with ProCoDA through a USB or serial port.

.. _heading_ProCoDA_Logging_Data:

Logging Data
============
