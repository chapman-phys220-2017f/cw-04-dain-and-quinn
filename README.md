# PHYS220 CW 4

**Author(s):** **Dain and Quinn**

[![Build Status](https://travis-ci.org/chapman-phys220-2017f/cw-04-dain-and-quinn.svg?branch=master)](https://travis-ci.org/chapman-phys220-2017f/cw-04-dain-and-quinn)

## Specification

1. With your partner, go through the [slides](http://slides.com/profdressel/numpy-and-pandas-overview/) that introduce the `numpy` and `pandas` libraries and how to use them. Use the Jupyter notebook `slides.ipynb` in the current repository to test code as you read through slides to make sure you understand.
1. With your partner, go through the python code in the repository showing the reference list implementation of the Gaussian function: $$g(x) = \frac{1}{\sqrt{2\pi}} \exp\left( -\frac{x^2}{2} \right).$$ Make sure you understand how the python module is formatted, how its command line arguments are used, how docstrings work and connect to the python help system, how the testing functions work, and how to load the code and use it in the notebook. Verify that running `nosetests3` in a terminal runs the tests and produces output you expect.
1. Complete the `numpy` array implementation of the Gaussian function in the module and verify its tests work. Plot the function in the notebook to verify it reproduces the list. Benchmark the performance in the notebook and compare it to the performance of the reference list implementation. Hint: Use array vectorization, meaning avoid all explicit for loops in favor of functions inside `numpy` that automatically distribute (map over) arrays.
1. Create both list and array implementations of the "sinc" function: $$ \text{sinc}(x) = \frac{\sin(x)}{x}.$$ Follow the style of the Gaussian function implementations for reference. Plot and benchmark the implementations in the notebook. Comment on how many points are needed per period of the "sinc" to obtain an accurate plot.
1. Create both list and array implementations of a frequency-chirped sine wave: $$\text{sinf}(x) = \sin\left(\frac{1}{x}\right).$$ What difficulties are there in implementing this function? Comment on the how many points per period will be necessary to obtain an accurate plot.


Pro-tip: using git to manage conflicts on Jupyter notebooks is a pain. I recommend delegating one person from your group to edit the notebook, to avoid merge conflicts.

## Assessment

We learned about the efficiency of numpy. We can see how much better it is at handling large amounts of data. The vectorize function is really cool. It helped us create tests for our code which will definitely be helpful in the future.  



## Honor Pledge

I pledge that all the work in this repository is my own with only the following exceptions:

* Content of starter files supplied by the instructor; we heavily borrowed code from Dr. Dressel 

Signed,

**Dain Miller and Quinn Gates**
