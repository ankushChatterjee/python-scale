"""Tests for test module 1928 — covers src modules [7709, 7710, 7711, 7712]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7709 import modulo_7709
from module_7710 import power_7710
from module_7711 import min_7711
from module_7712 import max_7712

def test_modulo_7709():
    assert modulo_7709(10, 3) == 1

def test_power_7710():
    assert power_7710(2, 8) == 256

def test_min_7711():
    assert min_7711(3, 7) == 3

def test_max_7712():
    assert max_7712(3, 7) == 7
