class Require:
    def __init__(self):
        try:
            assert False
            exit("Error: enable assertions to use {}".format(__file__))
        except AssertionError:
            pass
    def __needed(self,type_needed,obj_recieved):
        return "\n\n\targ needs to be {}, not {}\n".format(type(type_needed),type(obj_recieved))
    def function(self,i):
        assert callable(i), self.__needed(callable,i)
    def str(self,i):
        assert isinstance(i, str), self.__needed(str(),i)
    def float(self,i):
        assert isinstance(i, float), self.__needed(float(),i)
    def int(self,i):
        assert isinstance(i, int), self.__needed(int(),i)
    def list(self,i):
        assert isinstance(i, list), self.__needed(list(),i)
    def dict(self,i):
        assert isinstance(i, dict), self.__needed(dict(),i)
    def bytearray(self,i):
        assert isinstance(i, bytearray), self.__needed(bytearray(),i)
    def any_of(self,i,*args):
        assert all(isinstance(x, type) for x in args), "Require.any_of() needs its arguments to be a 'type'"
        assert any(isinstance(i, t) for t in args), "recieved: {} and needed one of these: {}".format(type(i),args)
