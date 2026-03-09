"""Tests for test module 1924 — covers src modules [7693, 7694, 7695, 7696]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7693 import modulo_7693
from module_7694 import power_7694
from module_7695 import min_7695
from module_7696 import max_7696

def test_modulo_7693():
    assert modulo_7693(10, 3) == 1

def test_power_7694():
    assert power_7694(2, 8) == 256

def test_min_7695():
    assert min_7695(3, 7) == 3

def test_max_7696():
    assert max_7696(3, 7) == 7
