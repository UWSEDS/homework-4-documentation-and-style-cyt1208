"""this module is created to test the function in HW2 and some dataframe properties."""

import unittest
import pandas as pd
import numpy as np


def test_create_dataframe(data, column_names):
    """ data is the input dataframe, column_names is a list of names of all the columns."""
    data_column = data.columns.tolist()
    column_check = False
    type_check = True
    if len(column_names) == len(data_column):
        for values in data_column:
            if values in column_names:
                column_check = True
            else:
                column_check = False
                break
    if column_check:
        for names in column_names:
            try:
                type_reference = type(data[names][0].item())
            except AttributeError:
                type_reference = type(data[names][0])
            for item in data[names]:
                if type_reference != type(item):
                    type_check = False
                    break
    if column_check & type_check:
        if len(data.index.tolist()) >= 10:
            return True
    return False


class UnitTests(unittest.TestCase):
    """unittests for hw3."""
    def test_hw2(self):
        """ unittest for hw2 function."""
        data_frame = pd.DataFrame({'A': [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
                                   'B': [2.1, 2.5, 6.8, 2.3, 4.2, 5.3, 7.4, 8.4, 3.5, 9.3],
                                   'C': ['s', 'd', 'r', 'w', 'r', 'd', 'v', 's', 'c', 'g']})
        self.assertTrue(test_create_dataframe(data_frame, ['A', 'B', 'C']))

    def test_check_correct_type(self):
        """ Check that all columns have values of the correct type."""
        data_frame = pd.DataFrame({'A': [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
                                   'B': [2.1, 2.5, 6.8, 2.3, 4.2, 5.3, 7.4, 8.4, 3.5, 9.3],
                                   'C': ['s', 'd', 'r', 'w', 'r', 'd', 'v', 's', 'c', 'g']})
        column_names = data_frame.columns.tolist()
        type_check = True
        for name in column_names:
            try:
                type_reference = type(data_frame[name][0].item())
            except AttributeError:
                type_reference = type(data_frame[name][0])
            for value in data_frame[name]:
                if type_reference != type(value):
                    type_check = False
                    break
        self.assertTrue(type_check)

    def test_nan_values(self):
        """ Check for nan values."""
        nan_check = False
        data_frame = pd.DataFrame({'A': [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
                                   'B': [2.1, 2.5, 6.8, 2.3, 4.2, 5.3, 7.4, 8.4, 3.5, 9.3],
                                   'C': ['s', 'd', 'r', 'w', 'r', 'd', 'v', 's', 'c', 'g']})
        for value in data_frame:
            nan_check = value is np.nan or value != value
        self.assertFalse(nan_check)

    def test_rows(self):
        """ Verify that the dataframe has at least one row."""
        data_frame = pd.DataFrame({'A': [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
                                   'B': [2.1, 2.5, 6.8, 2.3, 4.2, 5.3, 7.4, 8.4, 3.5, 9.3],
                                   'C': ['s', 'd', 'r', 'w', 'r', 'd', 'v', 's', 'c', 'g']})
        self.assertTrue(len(data_frame.index.tolist()) >= 1)
