import function
from inputs.datasets import *

def test_on_first_input():
    assert function.maxOfList(list_1) == 33
def test_on_second_input():
    assert function.maxOfList(list_2) == 55