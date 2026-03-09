"""Tests for test module 678 — covers src modules [2709, 2710, 2711, 2712]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2709 import modulo_2709
from module_2710 import power_2710
from module_2711 import min_2711
from module_2712 import max_2712

def test_modulo_2709():
    assert modulo_2709(10, 3) == 1

def test_power_2710():
    assert power_2710(2, 8) == 256

def test_min_2711():
    assert min_2711(3, 7) == 3

def test_max_2712():
    assert max_2712(3, 7) == 7
