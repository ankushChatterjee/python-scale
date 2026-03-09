"""Tests for test module 416 — covers src modules [1661, 1662, 1663, 1664]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1661 import modulo_1661
from module_1662 import power_1662
from module_1663 import min_1663
from module_1664 import max_1664

def test_modulo_1661():
    assert modulo_1661(10, 3) == 1

def test_power_1662():
    assert power_1662(2, 8) == 256

def test_min_1663():
    assert min_1663(3, 7) == 3

def test_max_1664():
    assert max_1664(3, 7) == 7
