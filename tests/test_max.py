import funcs_for_tests
from datasets import *

def test_on_first_input():
    assert funcs_for_tests.n.maxOfList(list_1) == 33
def test_on_second_input():
    assert funcs_for_tests.maxOfList(list_2) == 55