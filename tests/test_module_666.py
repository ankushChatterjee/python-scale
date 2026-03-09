"""Tests for test module 666 — covers src modules [2661, 2662, 2663, 2664]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2661 import modulo_2661
from module_2662 import power_2662
from module_2663 import min_2663
from module_2664 import max_2664

def test_modulo_2661():
    assert modulo_2661(10, 3) == 1

def test_power_2662():
    assert power_2662(2, 8) == 256

def test_min_2663():
    assert min_2663(3, 7) == 3

def test_max_2664():
    assert max_2664(3, 7) == 7
