"""Tests for test module 434 — covers src modules [1733, 1734, 1735, 1736]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1733 import modulo_1733
from module_1734 import power_1734
from module_1735 import min_1735
from module_1736 import max_1736

def test_modulo_1733():
    assert modulo_1733(10, 3) == 1

def test_power_1734():
    assert power_1734(2, 8) == 256

def test_min_1735():
    assert min_1735(3, 7) == 3

def test_max_1736():
    assert max_1736(3, 7) == 7
