# PyCurve

This is a program I wrote to help me quickly curve test grades, with options!
I honestly over engineered something because I was bored but this has become
really handy for me.

## Using PyCurve

Grades to be curved need to be in a csv file located within the *files* folder 
within the project folder.

All output files will be placed in the *curved_grades* folder within the
project folder.

## Features

PyCurve will perform a few different curves that are common for exams.
1.) Square Root Curve -> sqrt(grade) * 10

2.) Max Score Curve -> Will find the top score and determine what range it falls
in between. It will then subtract the grade score from the top of the range.
For example -> a grade of 75 falls in between 70-80. 80 - 75 = 5.
So 5 will be added to all the scores. (I don't use this that often, usually if everyone
does very well.)

3.) 10 point bump -> This essentially bumps most grades by a letter grade, but 
won't help out those who bomb a quiz or a test as much as a square root curve.
This is the most common method I use if I end up curving a test.

## Upcoming Features

I am planning on adding more functionality and possibly making this run on a 
webapp with a gui. It depends on how much time I have or how much of a demand
there is for this. (Probably none since it doesn't take me long to do my curves
by hand.)

Thank you and I appreciate any feedback or critiques on how to better write this.

John

