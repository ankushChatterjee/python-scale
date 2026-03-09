"""Tests for test module 1004 — covers src modules [4013, 4014, 4015, 4016]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4013 import modulo_4013
from module_4014 import power_4014
from module_4015 import min_4015
from module_4016 import max_4016

def test_modulo_4013():
    assert modulo_4013(10, 3) == 1

def test_power_4014():
    assert power_4014(2, 8) == 256

def test_min_4015():
    assert min_4015(3, 7) == 3

def test_max_4016():
    assert max_4016(3, 7) == 7
