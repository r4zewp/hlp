from function import *
from tests.datasets import *

def test_on_first_input():
    assert sumOfList(list_1) == 66

def test_on_second_input():
    assert sumOfList(list_2) == 182