"""Tests for test module 1918 — covers src modules [7669, 7670, 7671, 7672]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7669 import modulo_7669
from module_7670 import power_7670
from module_7671 import min_7671
from module_7672 import max_7672

def test_modulo_7669():
    assert modulo_7669(10, 3) == 1

def test_power_7670():
    assert power_7670(2, 8) == 256

def test_min_7671():
    assert min_7671(3, 7) == 3

def test_max_7672():
    assert max_7672(3, 7) == 7
