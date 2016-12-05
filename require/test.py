# -*- coding: utf-8 -*-
# @Author: cody
# @Date:   2016-12-01 11:32:54
# @Last Modified 2016-12-05
# @Last Modified time: 2016-12-05 13:25:04

"""
These are the examples used on the README's table that are
used to test the basic functionality of prequire.
"""

from prequire import prequire

if __name__ == "__main__":

    #--------------------------------------------------------
    #   Test that singular arguments work correctly
    #--------------------------------------------------------

    prequire.function(lambda: "hello")
    prequire.type(type(0))
    prequire.str("hello world")
    prequire.float(0.0)
    prequire.int(3)
    prequire.list(['hello world'])
    prequire.dict({"hello": "world"})
    prequire.tuple((1, 2, 3, 4))
    prequire.bytearray(bytearray("hello world"))
    prequire.not_empty([1, 2, 3, 4])
    prequire.is_empty([])
    prequire.iterable(range(4))
    prequire.contains_only([1, 2, 3, 4], int)
    prequire.any_of(4, int, float)

    #--------------------------------------------------------
    #   test that each method can take multiple arguments
    #--------------------------------------------------------

    prequire.function(lambda: "hello", lambda: "world")
    prequire.type(type(0), type("hi"))
    prequire.str("hello", "world")
    prequire.float(0.0, 5.4)
    prequire.int(3, 17)
    prequire.list(['hello'], ['world'])
    prequire.dict({"hello": 1}, {"world": 2})
    prequire.tuple((1, 2), (3, 4))
    prequire.bytearray(bytearray("hello"), bytearray("world"))
    prequire.not_empty([1, 2], [3, 4])
    prequire.is_empty([], {})
    prequire.iterable(range(4), "hello")

    print("success")
