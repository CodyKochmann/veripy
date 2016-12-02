# -*- coding: utf-8 -*-
# @Author: cody
# @Date:   2016-12-01 11:32:54
# @Last Modified 2016-12-01
# @Last Modified time: 2016-12-01 12:13:18

"""
These are the examples used on the README's table.
"""

from require import require

if __name__ == "__main__":

    #--------------------------------------------------------
    #   Test that singular arguments work correctly
    #--------------------------------------------------------

    require.function(lambda:"hello")
    require.type(type(0))
    require.str("hello world")
    require.float(0.0)
    require.int(3)
    require.list(['hello world'])
    require.dict({"hello":"world"})
    require.tuple((1,2,3,4))
    require.bytearray(bytearray("hello world"))
    require.not_empty([1,2,3,4])
    require.is_empty([])
    require.iterable(range(4))
    require.contains_only([1,2,3,4], int)
    require.any_of(4, int, float)

    #--------------------------------------------------------
    #   test that each method can take multiple arguments
    #--------------------------------------------------------

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
