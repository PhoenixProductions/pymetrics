This is a simple set of python scripts to allow for 
(simplified) natural language entry of personal metrics for 
analysis (see Stephen Wolfram's article for origin idea).

It is split into 3 parts:
* a raw data collector (metricsparser.py)
* a pre-parser which collates activities into "item" logs
* an analyser which will produce some outputs from the data.

Data capture
============
Run metricsparsers.py
At the prompt you can enter an item to be tracked:
>ate

This will record a single "ate" action at the current time

You can add a "what" option:
>ate burger
This records that you "ate 1 burger" at the current time

You can provide a quantifier:
>ate 3 burger 
(note the "what" is singular)

You can specify the time that the action took place:
>ate 3 burger @ 1200

This always assumes the current date.

The script appends a text line to the end of a file named "data" 
in the current directory.
This should make it ok for running on something like dropbox.
The file is opened and then closed every time so shouldn't cause 
too many issues with locking.

It should be possible to run the data logging script on multiple machines 
at once, and use the DataExtractor.py script to process the logs into a 
shared location (e.g. Dropbox) so that data can be captured from 
multiple machines (e.g. Home and work)

Item Logs
=========
The DataExtractor.py script parses a raw log file and splits each 
action in to separate files (normally in analysis/ directory).

In addition the script rotates the data file it processes out of the way 
so that future runs of the script would not re-process (and thus skew) the data

By default DataExtractor.py expects the name of the data log to process

You can specify the location that the item logs via the --out option. 
This defaults to ~/Dropbox/metrics/analysis at present.

Plans
=====
* Specify default locations:
** Raw Data file location
** Location of "analysis" files
* Analyser
** Probably will be a single script that will run sub-scripts to 
produce appropriate output reports.
