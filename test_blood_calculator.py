import pytest

@pytest.mark.parametrize("input_HDL, expected", 
#needs to be the string version of the exact parameters of function
[(85, "Normal"), #These are test cases I want, tuple of arguments
(50, "Borderline Low"),
(30, "Low")])
def test_check_HDL(input_HDL, expected):
    from blood_calculator import check_HDL
    answer = check_HDL(input_HDL) #the variable name doesn't need to be answer
    assert answer == expected

@pytest.mark.parametrize("input_LDL, expected", 
[(100, "Normal"),
(140, "Borderline High"),
(180, "High"),
(200, "Very High")])
def test_check_LDL(input_LDL, expected):
    from blood_calculator import check_LDL
    answer = check_LDL(input_LDL)
    assert answer == expected

@pytest.mark.parametrize("input_total, expected", 
[(150, "Normal"),
(210, "Borderline High"),
(300, "High")])
def test_check_total(input_total, expected):
    from blood_calculator import check_total
    answer = check_total(input_total)
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
