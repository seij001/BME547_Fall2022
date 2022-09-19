import pytest

@pytest.mark.parametrize("input_one, expected", 
#needs to be the string version of the exact parameters of function
[(85, "Normal"), #These are test cases I want, tuple of arguments
(50, "Borderline Low"),
(30, "Low")])
def test_check_HDL(input_one, expected):
    from blood_calculator import check_HDL
    answer = check_HDL(input_one) #the variable name doesn't need to be answer
    assert answer == expected

'''
def test_check_HDL_BorderlineLow():
    from blood_calculator import check_HDL
    answer = check_HDL(50)
    expected = "Borderline Low"
    assert answer == expected

def test_check_HDL_Low():
    from blood_calculator import check_HDL
    answer = check_HDL(30)
    expected = "Low"
    assert answer == expected
'''
