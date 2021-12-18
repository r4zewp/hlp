from tests.funcs_for_tests import fileOpening


def test_valid_file_reading_one():
    assert fileOpening("inputs/input_4.txt") == [1,1,1,1,2,3,4,5]
    
def test_valid_file_reading_one():
    assert fileOpening("inputs/input_5.txt") == [1,1,1,1,2,3,4,5,1,1,1,1,2,3,4,5,1,1,1,1,2,3,4,5]