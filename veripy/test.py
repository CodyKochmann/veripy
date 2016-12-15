# -*- coding: utf-8 -*-
# @Author: cody
# @Date:   2016-12-01 11:32:54
# @Last Modified 2016-12-15
# @Last Modified time: 2016-12-15 12:20:47

"""
These are the examples used on the README's table that are
used to test the basic functionality of veripy.
"""

from veripy import veripy
from os import (
    listdir as ls,
    chdir as cd
)
from os.path import (
    isfile,
    isdir
)

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

    #--------------------------------------------------------
    #   test that file and path verification works
    #--------------------------------------------------------

    target_dir = "../"
    dir_listing = lambda: ("../{}".format(i) for i in ls(target_dir))

    file_paths = tuple(i for i in dir_listing() if isfile(i))
    dir_dirs = tuple(i for i in dir_listing() if isdir(i))
    dir_files = tuple(open(i,'r') for i in file_paths)

    # singular arguments
    for path in file_paths:
        veripy.file_path(path)
    for path in dir_dirs:
        veripy.dir_path(path)
    for file in dir_files:
        veripy.file(file)

    # multiple arguments
    veripy.file_path(*file_paths)
    veripy.dir_path(*dir_dirs)
    veripy.file(*dir_files)

    print("success")
