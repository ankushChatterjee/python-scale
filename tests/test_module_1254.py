"""Tests for test module 1254 — covers src modules [5013, 5014, 5015, 5016]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5013 import modulo_5013
from module_5014 import power_5014
from module_5015 import min_5015
from module_5016 import max_5016

def test_modulo_5013():
    assert modulo_5013(10, 3) == 1

def test_power_5014():
    assert power_5014(2, 8) == 256

def test_min_5015():
    assert min_5015(3, 7) == 3

def test_max_5016():
    assert max_5016(3, 7) == 7
