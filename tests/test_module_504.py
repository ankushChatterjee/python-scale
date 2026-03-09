"""Tests for test module 504 — covers src modules [2013, 2014, 2015, 2016]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2013 import modulo_2013
from module_2014 import power_2014
from module_2015 import min_2015
from module_2016 import max_2016

def test_modulo_2013():
    assert modulo_2013(10, 3) == 1

def test_power_2014():
    assert power_2014(2, 8) == 256

def test_min_2015():
    assert min_2015(3, 7) == 3

def test_max_2016():
    assert max_2016(3, 7) == 7
