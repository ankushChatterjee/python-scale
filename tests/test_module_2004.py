"""Tests for test module 2004 — covers src modules [8013, 8014, 8015, 8016]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8013 import modulo_8013
from module_8014 import power_8014
from module_8015 import min_8015
from module_8016 import max_8016

def test_modulo_8013():
    assert modulo_8013(10, 3) == 1

def test_power_8014():
    assert power_8014(2, 8) == 256

def test_min_8015():
    assert min_8015(3, 7) == 3

def test_max_8016():
    assert max_8016(3, 7) == 7
