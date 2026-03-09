"""Tests for test module 178 — covers src modules [709, 710, 711, 712]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_709 import modulo_709
from module_710 import power_710
from module_711 import min_711
from module_712 import max_712

def test_modulo_709():
    assert modulo_709(10, 3) == 1

def test_power_710():
    assert power_710(2, 8) == 256

def test_min_711():
    assert min_711(3, 7) == 3

def test_max_712():
    assert max_712(3, 7) == 7
