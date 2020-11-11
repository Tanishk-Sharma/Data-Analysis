# Floating Point error

Ok, now this was a real head scratcher which I faced one day during work. 
The task was a very simple data cleaning job. Fetch data from a source csv file, remove null rows and put the data back into a target csv file. 

But here comes the problem – one of the columns had floating point numbers which just changed altogether in the target csv file.

Logging has been included in this file so you won't see any output on the command line.

## How to run the script

The script takes the source csv file name from the command line itself.
Example: $ python NULL_remove.py my_csv_file.csv

:star: Read more about the problem in this <a href="https://tanishkblog2020.wordpress.com/2020/11/10/problem-of-floating-point-precision-in-pandas/" target="_blank">blog article</a>.

Sample CSV File: <a href="https://support.spatialkey.com/spatialkey-sample-csv-data/">Sacramento real estate transactions file</a>  
