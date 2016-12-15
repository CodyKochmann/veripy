# -*- coding: utf-8 -*-
# @Author: cody
# @Date:   2016-11-30 14:28:01
# @Last Modified 2016-12-15
# @Last Modified time: 2016-12-15 11:59:32

from os.path import (
    isfile,
    isdir
)

from logging import warning

# force assertions to be enabled
try:
    assert False
    warning(" 'veripy' does not support running with assertions disabled")
except AssertionError:
    pass


class veripy:
    @classmethod
    def __needed(self, type_needed, obj_recieved):
        return "\n\n\targ needs to be {}, not {}\n".format(
            type(type_needed),
            type(obj_recieved)
        )

    # ===========================================
    #      assertions for types of objects
    # ===========================================

    @classmethod
    def function(self, *args):
        """ assertion that mandates a function """
        self.tuple(args)
        self.not_empty(args)
        for i in args:
            assert callable(i), self.__needed(callable, i)

    @classmethod
    def type(self, *args):
        """ assertion that mandates a 'type' object """
        self.tuple(args)
        self.not_empty(args)
        for i in args:
            assert isinstance(i, type), self.__needed(type(str), i)

    @classmethod
    def str(self, *args):
        """ assertion that mandates a str """
        self.tuple(args)
        self.not_empty(args)
        for i in args:
            assert isinstance(i, str), self.__needed(str(), i)

    @classmethod
    def float(self, *args):
        """ assertion that mandates a float """
        self.tuple(args)
        self.not_empty(args)
        for i in args:
            assert isinstance(i, float), self.__needed(float(), i)

    @classmethod
    def int(self, *args):
        """ assertion that mandates a int """
        self.tuple(args)
        self.not_empty(args)
        for i in args:
            assert isinstance(i, int), self.__needed(int(), i)

    @classmethod
    def list(self, *args):
        """ assertion that mandates a list """
        self.tuple(args)
        self.not_empty(args)
        for i in args:
            assert isinstance(i, list), self.__needed(list(), i)

    @classmethod
    def dict(self, *args):
        """ assertion that mandates a dict """
        self.tuple(args)
        self.not_empty(args)
        for i in args:
            assert isinstance(i, dict), self.__needed(dict(), i)

    @classmethod
    def tuple(self, *args):
        """ assertion that mandates a tuple """
        assert isinstance(args, tuple), self.__needed(tuple(), args)
        self.not_empty(args)
        for i in args:
            assert isinstance(i, tuple), self.__needed(tuple(), i)

    @classmethod
    def bytearray(self, *args):
        """ assertion that mandates a bytearray """
        self.tuple(args)
        self.not_empty(args)
        for i in args:
            assert isinstance(i, bytearray), self.__needed(bytearray(), i)

    # ===============================================
    #      assertions for content in the objects
    # ===============================================

    @classmethod
    def not_empty(self, *args):
        """ assertion that mandates the length is not 0 """
        assert isinstance(args, tuple), self.__needed(tuple(), args)
        assert len(args), "the given {} can not be empty".format(type(args))
        for i in args:
            # test that it supports len()
            len(i)
            assert len(i), "the given {} can not be empty".format(type(i))

    @classmethod
    def is_empty(self, *args):
        """ assertion that mandates an empty object with length of 0 """
        self.tuple(args)
        self.not_empty(args)
        for i in args:
            # test that it supports len()
            len(i)
            assert len(i) == 0, "the given {} must be empty".format(type(i))

    # ===================================
    #      assertions for iterables
    # ===================================

    @staticmethod
    def __is_iterable(i):
        """ boolean test to see if the argument is iterable """
        output = False
        try:
            iter(i)
            output = True
        except:
            pass
        return output

    @classmethod
    def iterable(self, *args):
        """ asserts that the given arguments are iterable """
        self.tuple(args)
        self.not_empty(args)
        for i in args:
            assert self.__is_iterable(i), "needed: iterable found: {}".format(
                type(i))

    @classmethod
    def contains_only(self, i, mandated_type):
        """ assertion that mandates every instance
            in an iterable object is a specified type
        """
        self.iterable(i)
        self.not_empty(i)
        self.type(mandated_type)
        for x in i:
            test = isinstance(x, mandated_type)
            assert test, "found: {} required: {}".format(
                type(x),
                mandated_type)

    # ================================================
    #      assertions for content in the objects
    # ================================================

    @classmethod
    def any_of(self, i, *args):
        """ assertion that mandates that the object
            is one of any of the given types
        """
        self.tuple(args)
        self.not_empty(args)
        self.contains_only(args, type)
        test = any(isinstance(i, t) for t in args)
        assert test, "recieved: {} instead of: {}".format(
            type(i),
            args
        )

    # =====================================================
    #      assertions for paths, directories and files
    # =====================================================

    @classmethod
    def file(self, *args):
        """ assertion for file objects """
        self.tuple(args)
        self.not_empty(args)
        e = lambda i: "\n\n\targ needs to be file, not {}\n".format(
            type(i)
        )
        for i in args:
            assert isinstance(i, file), e(i)

    @classmethod
    def file_path(self, *args):
        """ asserts the args are paths to actual files """
        self.tuple(args)
        self.not_empty(args)
        self.contains_only(args, str)
        e = lambda i: "\n\n\tinvalid file path: {}\n".format(i)
        for i in args:
            assert isfile(i), e(i)

    @classmethod
    def dir_path(self, *args):
        """ asserts the args are paths to directories """
        self.tuple(args)
        self.not_empty(args)
        self.contains_only(args, str)
        e = lambda i: "\n\n\tinvalid directory path: {}\n".format(i)
        for i in args:
            assert dir(i), e(i)
