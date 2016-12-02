# -*- coding: utf-8 -*-
# @Author: cody
# @Date:   2016-11-30 14:28:01
# @Last Modified 2016-12-02
# @Last Modified time: 2016-12-02 12:42:19

# force assertions to be enabled
try:
    assert False
    exit("Error: enable assertions to use {}".format(__file__))
except AssertionError:
    pass


class require:
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
        """ assertion that mandates a iterable object """
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
        assert test, "recieved: {} and needed one of these: {}".format(
            type(i),
            args
        )
