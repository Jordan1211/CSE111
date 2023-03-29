import pytest
from project import calculate_area

def test_calculate_area():
    """Verify that the calculate_area function works correctly."""
    # Verify that the calculate function runs and sets the correct value.
    assert calculate_area(25,25,4,120) == 2800.93
    assert calculate_area(10,25,8,102) == 1379.63


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])