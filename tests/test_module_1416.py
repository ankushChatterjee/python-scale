"""Tests for test module 1416 — covers src modules [5661, 5662, 5663, 5664]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5661 import modulo_5661
from module_5662 import power_5662
from module_5663 import min_5663
from module_5664 import max_5664

def test_modulo_5661():
    assert modulo_5661(10, 3) == 1

def test_power_5662():
    assert power_5662(2, 8) == 256

def test_min_5663():
    assert min_5663(3, 7) == 3

def test_max_5664():
    assert max_5664(3, 7) == 7
