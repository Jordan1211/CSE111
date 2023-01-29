from sentences import get_determiner,get_noun,get_verb
from pytest import approx
import pytest

def test_get_determiner():
    """Test the get_determiner function by calling it and
    comparing the values it returns to the expected values.
    """
    assert get_determiner(5) == 2
    
def test_get_noun():
    """Test the get_noun function by calling it and
    comparing the values it returns to the expected values.
    """
    assert get_noun(5) == 2
    
def test_get_verb():
    """Test the get_verb function by calling it and
    comparing the values it returns to the expected values.
    """
    assert get_verb(5) == 2

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])