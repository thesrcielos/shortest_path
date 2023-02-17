# About this repo

Simple python project to show a way to take experiental execution time to compare a set of algorithms (three in this case) in fair way.

## Twisted Sort

First even then odd sorting algorithms.

### Problem statement
​
The sample problem is to take a list of integers with at least one element and sort them with the following criteria:

* First it will be the even numbers (those who are divisible by 2 with no reminder), then it will be the odd numbers
* The even numbers should be sorted in ascending order, and the odd numbers should be sorted in descending order
* The algorithm will only sort positive numbers

### Examples

* For `3 1 9` the output should be `9 3 1`

* For `1 9 8 2 3 4 5 7 6` the output should be `2 4 6 8 9 7 5 3 1`

* For `8 2 4` the output should be `2 4 8`

* For `10 90 80 20 30 40 50 70 60` the output should be `10 20 30 40 50 60 70 80 90`

* For `11 91 81 21 31 41 51 71 61` the output should be `91 81 71 61 51 41 31 21 11`

* For `11 92 83 24 35 46 57 78 69` the output should be `24 46 78 92 83 69 57 35 11`



# Python version
Python 3.11.0
​
# Running locally and testing

* Note: This instructions are for mac. Windows or linux may require some changes. 
* A good idea for this project, is to use a virtual environment, you could set up one with: [virtualenv](https://virtualenv.pypa.io/en/latest/).
* To create the virtual environment: `virtualenv env`
* To activate it:`source env/bin/activate`
* To install dependencies: `pip3 install -r requirements.txt`
* To run unit testing: `./test.sh`
* To try a default example, run: `: ./run.sh`. In the file ./run.sh is just an example, you can modify it. Theck the `app.py` file to get to understand how it works.

# Current coverage

Make sure you have "coverage" in your requirements.txt file and run pip install. Then run `coverage run -m unittest discover` and after that run `coverage report` to get the following table:

```
Name                            Stmts   Miss  Cover
---------------------------------------------------
test/__init__.py                    0      0   100%
test/test_algorithms.py            24      1    96%
test/test_data_generator.py        29      1    97%
twistedsort/__init__.py             0      0   100%
twistedsort/algorithms.py          27      3    89%
twistedsort/constants.py            2      0   100%
twistedsort/data_generator.py       9      1    89%
---------------------------------------------------
TOTAL                              91      6    93%
```

# Code beautifier
This code has been beautify using black: https://github.com/psf/black. 
The command to use is `black . -l 120`.
