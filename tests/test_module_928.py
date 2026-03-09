"""Tests for test module 928 — covers src modules [3709, 3710, 3711, 3712]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3709 import modulo_3709
from module_3710 import power_3710
from module_3711 import min_3711
from module_3712 import max_3712

def test_modulo_3709():
    assert modulo_3709(10, 3) == 1

def test_power_3710():
    assert power_3710(2, 8) == 256

def test_min_3711():
    assert min_3711(3, 7) == 3

def test_max_3712():
    assert max_3712(3, 7) == 7
