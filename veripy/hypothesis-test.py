# -*- coding: utf-8 -*-
# @Author: cody
# @Date:   2016-12-01 19:07:10
# @Last Modified 2016-12-05
# @Last Modified time: 2016-12-05 15:55:56

"""
    This is where hypothesis will be taking its turn
    making sure that veripy.py behaves the way it
    should with the correct inputs.
"""

from hypothesis import (
    strategies as st,
    settings,
    Verbosity,
    given
)

from veripy import veripy

test_samples = 2048

with settings(
        verbosity=Verbosity.normal,
        min_satisfying_examples=test_samples,
        max_examples=test_samples):

    @given(arg_list=st.lists(min_size=1, elements=st.text()))
    def test_str(arg_list):
        try:
           veripy.str(*arg_list)
        except AssertionError:
            pass

    @given(arg_list=st.lists(min_size=1, elements=st.floats()))
    def test_float(arg_list):
        try:
           veripy.float(*arg_list)
        except AssertionError:
            pass

    @given(arg_list=st.lists(min_size=1, elements=st.integers()))
    def test_int(arg_list):
        try:
           veripy.int(*arg_list)
        except AssertionError:
            pass

    @given(arg_list=st.lists(min_size=1, elements=st.lists(
        min_size=1,
        elements=st.floats())))
    def test_list(arg_list):
        try:
           veripy.list(*arg_list)
        except AssertionError:
            pass

    @given(arg_list=st.lists(min_size=1, elements=st.lists(
        min_size=1,
        elements=st.tuples())))
    def test_tuple(arg_list):
        try:
           veripy.tuple(*arg_list)
        except AssertionError:
            pass

    if __name__ == "__main__":
        tests = [test_str, test_float, test_int, test_list, test_tuple]
        for t in tests:
            print("running ({} times) - {}".format(test_samples, t.__name__))
            t()
            print("success")
        print("done")
