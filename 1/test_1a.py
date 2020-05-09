import pytest
import day1a

def test_mass12():
    returnvalue = getfuel(12)
    assert returnvalue == 2

def test_mass14():
    returnvalue = getfuel(14)
    assert returnvalue == 2

def test_mass1969():
    returnvalue = getfuel(1969)
    assert returnvalue == 654

def test_mass100756():
    returnvalue = getfuel(100756)
    assert returnvalue == 33583

def test_sumis34241():
    testmasses = [12,14,1969,100756]
    returnvalue = totalfuel( testmasses )
    assert returnvalue == 34241
