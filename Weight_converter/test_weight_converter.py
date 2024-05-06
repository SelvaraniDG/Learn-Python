import unittest

from weight_converter import kg_to_lbs, lbs_to_kg

def test_kg_to_lbs():
    assert kg_to_lbs(0) == 0.0
    assert kg_to_lbs(1) == 2.20462
    
def test_lbs_to_kg():
    assert lbs_to_kg(0) == 0.0
    assert lbs_to_kg(2.20462) == unittest.approx(1)