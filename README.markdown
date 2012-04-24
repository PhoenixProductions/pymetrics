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
