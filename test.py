# -*- coding: utf-8 -*-
# @Author: cody
# @Date:   2016-12-01 11:32:54
# @Last Modified 2016-12-01
# @Last Modified time: 2016-12-01 11:35:11

"""
These are the examples used on the README's table.
"""

from require import require

if __name__ == "__main__":
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
