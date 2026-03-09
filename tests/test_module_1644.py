"""Tests for test module 1644 — covers src modules [6573, 6574, 6575, 6576]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6573 import modulo_6573
from module_6574 import power_6574
from module_6575 import min_6575
from module_6576 import max_6576

def test_modulo_6573():
    assert modulo_6573(10, 3) == 1

def test_power_6574():
    assert power_6574(2, 8) == 256

def test_min_6575():
    assert min_6575(3, 7) == 3

def test_max_6576():
    assert max_6576(3, 7) == 7
