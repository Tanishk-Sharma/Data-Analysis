# Remove NULL Values

This is one of the simplest tasks that Data Analysts need to perform on any data set before beginning to work on them.
This is necessary to filter out the bad data for reasons like:

* throwing unpredictable errors while processing
* messing up our calculations
* destination data store (Database/Data Warehouse) may not support inserting NULL values and throw errors.

In this program, we remove rows containing NULL values.
The part removing columns containing NULL values is commented out for now.
Feel free to uncomment it and try it out.

Logging has been included in this file so you won't see any output on the command line.

## How to run the script

The script takes the source csv file name from the command line itself.
Example: $ python NULL_remove.py my_csv_file.csv

:star: This script covers one important problem I faced!
Read more about it in this <a href="https://tanishkblog2020.wordpress.com/2020/11/10/problem-of-floating-point-precision-in-pandas/">blog article</a>.
