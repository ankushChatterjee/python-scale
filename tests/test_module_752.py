"""Tests for test module 752 — covers src modules [3005, 3006, 3007, 3008]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3005 import modulo_3005
from module_3006 import power_3006
from module_3007 import min_3007
from module_3008 import max_3008

def test_modulo_3005():
    assert modulo_3005(10, 3) == 1

def test_power_3006():
    assert power_3006(2, 8) == 256

def test_min_3007():
    assert min_3007(3, 7) == 3

def test_max_3008():
    assert max_3008(3, 7) == 7
