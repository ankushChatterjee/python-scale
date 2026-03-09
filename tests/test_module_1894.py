"""Tests for test module 1894 — covers src modules [7573, 7574, 7575, 7576]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7573 import modulo_7573
from module_7574 import power_7574
from module_7575 import min_7575
from module_7576 import max_7576

def test_modulo_7573():
    assert modulo_7573(10, 3) == 1

def test_power_7574():
    assert power_7574(2, 8) == 256

def test_min_7575():
    assert min_7575(3, 7) == 3

def test_max_7576():
    assert max_7576(3, 7) == 7
