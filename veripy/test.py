# -*- coding: utf-8 -*-
# @Author: cody
# @Date:   2016-12-01 11:32:54
# @Last Modified 2016-12-05
# @Last Modified time: 2016-12-05 15:55:33

"""
These are the examples used on the README's table that are
used to test the basic functionality of veripy.
"""

from veripy import veripy

if __name__ == "__main__":

    #--------------------------------------------------------
    #   Test that singular arguments work correctly
    #--------------------------------------------------------

    veripy.function(lambda: "hello")
    veripy.type(type(0))
    veripy.str("hello world")
    veripy.float(0.0)
    veripy.int(3)
    veripy.list(['hello world'])
    veripy.dict({"hello": "world"})
    veripy.tuple((1, 2, 3, 4))
    veripy.bytearray(bytearray("hello world"))
    veripy.not_empty([1, 2, 3, 4])
    veripy.is_empty([])
    veripy.iterable(range(4))
    veripy.contains_only([1, 2, 3, 4], int)
    veripy.any_of(4, int, float)

    #--------------------------------------------------------
    #   test that each method can take multiple arguments
    #--------------------------------------------------------

    veripy.function(lambda: "hello", lambda: "world")
    veripy.type(type(0), type("hi"))
    veripy.str("hello", "world")
    veripy.float(0.0, 5.4)
    veripy.int(3, 17)
    veripy.list(['hello'], ['world'])
    veripy.dict({"hello": 1}, {"world": 2})
    veripy.tuple((1, 2), (3, 4))
    veripy.bytearray(bytearray("hello"), bytearray("world"))
    veripy.not_empty([1, 2], [3, 4])
    veripy.is_empty([], {})
    veripy.iterable(range(4), "hello")

    print("success")
