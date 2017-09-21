#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###
# Name: Dain Miller and Quinn Gates
# Student ID: 2254735 and
# Email: mille480 and 
# Course: PHYS220/MATH220/CPSC220 Fall 2017
# Assignment: Classwork 4
###

"""Classwork 04 Test Functions
This suite of functions tests the functionality of the CW04 solutions.
"""

import nose
import numpy as np
import cw04

def test_gauss_list():
    """test_gauss_list()
    Tests whether Gaussian values are correct for domain points -1, 0, and 1,
    using the reference list implementation.
    """
    x,g = cw04.gen_gaussian_list(-1,1,3)
    desired = [0.24197072451914337, 0.3989422804014327, 0.24197072451914337]
    print("Obtained:",g)
    print("Desired:",desired)
    # For comparing floating point values, nose has useful helper functions
    # to ensure they are equal up to a numerical precision tolerance
    nose.tools.assert_almost_equal(g, desired)

def test_gauss_array():
    """test_gauss_array()
    Tests whether Gaussian values are correct for domain points -1, 0, and 1,
    using the numpy array implementation.
    """
    x,g = cw04.gen_gaussian_array(-1,1,3)
    desired = np.array([0.24197072451914337, 0.3989422804014327, 0.24197072451914337])
    print("Obtained:",g)
    print("Desired:",desired)
    # Numpy has built-in testing functions to iterate over arrays and compare
    # values up to certain tolerances
    np.testing.assert_almost_equal(g, desired)
