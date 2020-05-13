import pytest
from day1b import getfuel, totalfuel

def test_mass14():
    returnvalue = getfuel(14)
    assert returnvalue == 2

def test_mass1969():
    returnvalue = getfuel(1969)
    assert returnvalue == 966

def test_mass100756():
    returnvalue = getfuel(100756)
    assert returnvalue == 50346

def test_sumis51314():
    testmasses = [14,1969,100756]
    returnvalue = totalfuel( testmasses )
    assert returnvalue == 51314