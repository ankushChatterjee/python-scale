"""Tests for test module 2166 — covers src modules [8661, 8662, 8663, 8664]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8661 import modulo_8661
from module_8662 import power_8662
from module_8663 import min_8663
from module_8664 import max_8664

def test_modulo_8661():
    assert modulo_8661(10, 3) == 1

def test_power_8662():
    assert power_8662(2, 8) == 256

def test_min_8663():
    assert min_8663(3, 7) == 3

def test_max_8664():
    assert max_8664(3, 7) == 7
