# UCSB_Grades

University of California, Santa Barbara Grades from Fall 2015 to Spring 2022

## How to Update the file

1. Email a Freedom of Information Act Request to [the person in charge](https://www.policy.ucsb.edu/information-stewardship/information-practices/public-records)  
2. Update the `UCSB Grades.csv` file
3. Run the `make_csvs.py` script
4. Make a pull request

## [Sample FOIA email](https://www.law.berkeley.edu/wp-content/uploads/2017/04/Sample-PRA-Request.pdf)

## Make smaller CSVs

To convert a large `UCSB Grades.csv` file to smaller files
by quarter and subject area, run this script:

```
python3 make_csvs.py
```
