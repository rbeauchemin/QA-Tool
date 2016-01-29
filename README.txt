This QA tool allows the user to bring in a csv with column 1 containing a host item,
and as many other columns contianing its recommendations. Find/Replace must be done
to qa_tool.py (open in any text editor) in order to replace the currently used .csv file with a new one.

These are run from command prompt (NOTE: Python inline tools can be installed without admin priviliges
through the free Enthought Canopy python package at https://www.enthought.com/products/canopy/)

Use case 1: Lookup a specific host by Catentry ID

python qa_tool.py 50100264

Use case 2: Go through it all

python qa_tool.py

