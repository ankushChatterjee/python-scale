"""Tests for test module 2174 — covers src modules [8693, 8694, 8695, 8696]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8693 import modulo_8693
from module_8694 import power_8694
from module_8695 import min_8695
from module_8696 import max_8696

def test_modulo_8693():
    assert modulo_8693(10, 3) == 1

def test_power_8694():
    assert power_8694(2, 8) == 256

def test_min_8695():
    assert min_8695(3, 7) == 3

def test_max_8696():
    assert max_8696(3, 7) == 7
