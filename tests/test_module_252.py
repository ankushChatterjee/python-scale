"""Tests for test module 252 — covers src modules [1005, 1006, 1007, 1008]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1005 import modulo_1005
from module_1006 import power_1006
from module_1007 import min_1007
from module_1008 import max_1008

def test_modulo_1005():
    assert modulo_1005(10, 3) == 1

def test_power_1006():
    assert power_1006(2, 8) == 256

def test_min_1007():
    assert min_1007(3, 7) == 3

def test_max_1008():
    assert max_1008(3, 7) == 7
