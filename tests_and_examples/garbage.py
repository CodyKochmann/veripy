# -*- coding: utf-8 -*-
# @Author: cody
# @Date:   2016-12-15 17:05:43
# @Last Modified 2016-12-16
# @Last Modified time: 2016-12-16 13:25:22

"""
    Automated negative testing against the
    type checkers in veripy.
"""

from random import choice
from hypothesis import strategies as st
from veripy import veripy

# =====================================
#     basic settings of the script
# =====================================
# VERBOSITY levels
# 0 - quiet
# 1 - info
# 2 - truly verbose
VERBOSITY = 1
TESTS_TO_RUN_ON_EACH_MODULE = 10**3


# validate the settings
veripy.int(VERBOSITY, TESTS_TO_RUN_ON_EACH_MODULE)
assert VERBOSITY<3 and VERBOSITY>=0, "VERBOSITY can be 0, 1, or 2"
assert TESTS_TO_RUN_ON_EACH_MODULE>0, "you need at least 1 test on each module"

def all_strategies():
    """ pragmatically generates all strategies that produce
        random, testable outputs """
    for method_name in st.__all__:
        strategy_code = "st.{}()".format(method_name)
        test_code = "{}.example()".format(strategy_code)
        try:
            exec(test_code)
            yield eval(strategy_code)
        except:
            pass

# convert all_strategies to a list so it
# can work with random.choice properly

def garbage(how_much_garbage=64):
    """ returns a random example from one of hypothesis' stratigies """
    strats = list(all_strategies())
    veripy.int(how_much_garbage)
    veripy.not_empty(strats)
    for i in range(how_much_garbage):
        yield choice(strats).example()

def pass_fail(f, fail=False, *args):
    """ runs f(args) and if fail is false,
        returns true if an AssertionError
        raises or if fail is True, returns
        True if the assertion never fires
        and no other exception is raised.
    """
    veripy.function(f)
    assert isinstance(fail, bool)
    veripy.tuple(args)
    veripy.not_empty(args)
    failed = False
    try:
        # attempt the assertion
        f(*args)
    except AssertionError as e:
        """ if the assertion fires and its not suppose
            to fire, the assertion will be raised """
        if not fail:
            raise e
        failed = True
    except Exception as e:
        """ if any other Exceptions fire, they are raised here """
        raise e
    """ success is determined by whether or not the assertion
        behaved the way it was predetermined to """
    success = failed == fail
    return success


def test_modules():
    """ generates the target modules to test and the
        type each is "suppose" to succeed on """
    modules_to_test = [
        "type",
        "str",
        "float",
        "int",
        "list",
        "dict",
        "tuple",
        "bytearray",
        "file"
    ]
    for mod_name in modules_to_test:
        test_type = eval(mod_name)
        veripy.type(type(test_type))
        test_function = eval("veripy.{}".format(mod_name))
        veripy.function(test_function)
        yield test_type, test_function


for expected_type, module in test_modules():
    veripy.type(expected_type)
    veripy.function(module)
    module_name = "veripy.{}".format(module.__name__)
    if VERBOSITY:
        print("running {} tests on {}".format(
            TESTS_TO_RUN_ON_EACH_MODULE,
            module_name
        ))

    def test_f(i):
        """ test function to send to pass_fail """
        module(i)

    for i in garbage(TESTS_TO_RUN_ON_EACH_MODULE):
        # determine if this input is suppose to fail
        fail = type(i) != expected_type

        # special case for booleans with veripy.int
        # not sure if this should happen or not :/
        if module_name == "veripy.int" and type(i) is bool:
            fail = not fail

        if VERBOSITY > 1:
            # this line cant use format() since hypothesis spits out
            # strings with crazy encoding every now and then
            print("testing:", module_name, "with:", i)

        # if the output of pass_fail is False
        if not pass_fail(test_f, fail, i):
            raise Exception("failed running {} with: {}".format(
                module_name,
                i
            ))
        elif VERBOSITY > 1:
            print("success")

print("done")
