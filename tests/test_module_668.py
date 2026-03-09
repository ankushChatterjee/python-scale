"""Tests for test module 668 — covers src modules [2669, 2670, 2671, 2672]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2669 import modulo_2669
from module_2670 import power_2670
from module_2671 import min_2671
from module_2672 import max_2672

def test_modulo_2669():
    assert modulo_2669(10, 3) == 1

def test_power_2670():
    assert power_2670(2, 8) == 256

def test_min_2671():
    assert min_2671(3, 7) == 3

def test_max_2672():
    assert max_2672(3, 7) == 7
