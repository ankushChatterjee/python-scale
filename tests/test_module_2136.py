"""Tests for test module 2136 — covers src modules [8541, 8542, 8543, 8544]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8541 import modulo_8541
from module_8542 import power_8542
from module_8543 import min_8543
from module_8544 import max_8544

def test_modulo_8541():
    assert modulo_8541(10, 3) == 1

def test_power_8542():
    assert power_8542(2, 8) == 256

def test_min_8543():
    assert min_8543(3, 7) == 3

def test_max_8544():
    assert max_8544(3, 7) == 7
