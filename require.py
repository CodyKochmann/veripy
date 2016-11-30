# -*- coding: utf-8 -*-
# @Author: cody
# @Date:   2016-11-30 14:28:01
# @Last Modified 2016-11-30
# @Last Modified time: 2016-11-30 16:11:16

# force assertions to be enabled
try:
    assert False
    exit("Error: enable assertions to use {}".format(__file__))
except AssertionError:
    pass

class require:
    @classmethod
    def __needed(self,type_needed,obj_recieved):
        self.type(type_needed)
        return "\n\n\targ needs to be {}, not {}\n".format(type(type_needed),type(obj_recieved))

    #============================================================
    # assertions for types of objects
    #============================================================

    @classmethod
    def function(self,i):
        """ assertion that mandates a function """
        assert callable(i), self.__needed(callable,i)
    @classmethod
    def type(self,i):
        """ assertion that mandates a 'type' object """
        assert isinstance(i, type), self.__needed(type(),i)
    @classmethod
    def str(self,i):
        """ assertion that mandates a str """
        assert isinstance(i, str), self.__needed(str(),i)
    @classmethod
    def float(self,i):
        """ assertion that mandates a float """
        assert isinstance(i, float), self.__needed(float(),i)
    @classmethod
    def int(self,i):
        """ assertion that mandates a int """
        assert isinstance(i, int), self.__needed(int(),i)
    @classmethod
    def list(self,i):
        """ assertion that mandates a list """
        assert isinstance(i, list), self.__needed(list(),i)
    @classmethod
    def dict(self,i):
        """ assertion that mandates a dict """
        assert isinstance(i, dict), self.__needed(dict(),i)
    @classmethod
    def tuple(self,i):
        """ assertion that mandates a tuple """
        assert isinstance(i, tuple), self.__needed(tuple(),i)
    @classmethod
    def bytearray(self,i):
        """ assertion that mandates a bytearray """
        assert isinstance(i, bytearray), self.__needed(bytearray(),i)

    #============================================================
    # assertions for content in the objects
    #============================================================

    @classmethod
    def not_empty(self,i):
        """ assertion that mandates the length is not 0 """
        # test that it supports len()
        len(i)
        assert len(i), "the given {} can not be empty".format(type(i))
    @classmethod
    def is_empty(self,i):
        """ assertion that mandates an empty object with length of 0 """
        # test that it supports len()
        len(i)
        assert len(i) == 0, "the given {} must be empty".format(type(i))

    #============================================================
    # assertions for iterables
    #============================================================

    @classmethod
    def iterable(self,i):
        """ assertion that mandates a iterable object """
        def is_iterable(i):
            output = False
            try:
                iter(i)
                output = True
            except:
                pass
            return output
        assert is_iterable(i), "iterable object required, found: {}".format(type(i))

    @classmethod
    def contains_only(self,i,mandated_type):
        """ assertion that mandates every instance in an iterable object is a certain type """
        self.iterable(i)
        self.not_empty(i)
        self.type(mandated_type)
        for x in i:
            assert isinstance(x, mandated_type), "found: {} required: {}".format(type(x),mandated_type)

    #============================================================
    # assertions for content in the objects
    #============================================================

    @classmethod
    def any_of(self,i,*args):
        """ assertion that mandates that the object is one of any of the given types """
        self.tuple(args)
        self.not_empty(args)
        self.contains_only(args,type)
        assert any(isinstance(i, t) for t in args), "recieved: {} and needed one of these: {}".format(type(i),args)

