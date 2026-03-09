"""Tests for test module 1504 — covers src modules [6013, 6014, 6015, 6016]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6013 import modulo_6013
from module_6014 import power_6014
from module_6015 import min_6015
from module_6016 import max_6016

def test_modulo_6013():
    assert modulo_6013(10, 3) == 1

def test_power_6014():
    assert power_6014(2, 8) == 256

def test_min_6015():
    assert min_6015(3, 7) == 3

def test_max_6016():
    assert max_6016(3, 7) == 7
