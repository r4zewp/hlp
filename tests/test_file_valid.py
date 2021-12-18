from tests.funcs_for_tests import fileOpening


def test_valid_file_reading():
    assert fileOpening("inputs/input_4.txt") == [1,1,1,1,2,3,4,5]