from funcs_for_tests import *
from datasets import *

def test_on_first_input():
    assert minOfList(list_1) == 1

def test_on_second_input():
    assert minOfList(list_2) == 0