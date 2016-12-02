# -*- coding: utf-8 -*-
# @Author: cody
# @Date:   2016-12-01 19:07:10
# @Last Modified 2016-12-01
# @Last Modified time: 2016-12-01 20:05:06

"""
    This is where hypothesis will be taking its turn
    making sure that require.py behaves the way it
    should with the correct inputs.
"""

from hypothesis import (
    strategies as st,
    settings,
    Verbosity,
    given
)

from require import require

"""
require.function(lambda:"hello", lambda:"world")
require.type(type(0), type("hi"))
 require.str("hello", "world")
require.float(0.0, 5.4)
require.int(3, 17)
require.list(['hello'], ['world'])
require.dict({"hello": 1}, {"world": 2})
require.tuple((1, 2), (3, 4))
require.bytearray(bytearray("hello"), bytearray("world"))
require.not_empty([1, 2], [3, 4])
require.is_empty([], {})
require.iterable(range(4), "hello")
"""

@settings(verbosity=Verbosity.debug,min_satisfying_examples=1024,max_examples=1024)
@given(arg_list=st.lists(min_size=1,elements=st.text()))
def test_str(arg_list):
    try:
        require.str(*arg_list)
    except AssertionError, e:
        pass

@settings(verbosity=Verbosity.debug,min_satisfying_examples=1024,max_examples=1024)
@given(arg_list=st.lists(min_size=1,elements=st.floats()))
def test_float(arg_list):
    try:
        require.float(*arg_list)
    except AssertionError, e:
        pass

@settings(verbosity=Verbosity.debug,min_satisfying_examples=1024,max_examples=1024)
@given(arg_list=st.lists(min_size=1,elements=st.integers()))
def test_int(arg_list):
    try:
        require.int(*arg_list)
    except AssertionError, e:
        pass

@settings(verbosity=Verbosity.debug,min_satisfying_examples=1024,max_examples=1024)
@given(arg_list=st.lists(min_size=1,elements=st.lists(min_size=1, elements=st.floats())))
def test_list(arg_list):
    try:
        require.list(*arg_list)
    except AssertionError, e:
        pass


if __name__ == "__main__":
    test_str()
    test_float()
    test_int()
    test_list()
