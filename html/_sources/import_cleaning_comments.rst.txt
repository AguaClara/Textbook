Comments on changes made while cleaning import statements:

Something in the unit registry creation process has broken, and units.py cannot find unit_definitions.txt to import the additional units (NTU, USD, HNL). As such, code that uses those units does not currently work. This affects the following files:

Introduction/Introduction.rst - I have commented out lines 415-417 so that no errors are thrown.
