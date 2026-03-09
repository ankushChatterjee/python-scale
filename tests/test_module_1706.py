"""Tests for test module 1706 — covers src modules [6821, 6822, 6823, 6824]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6821 import modulo_6821
from module_6822 import power_6822
from module_6823 import min_6823
from module_6824 import max_6824

def test_modulo_6821():
    assert modulo_6821(10, 3) == 1

def test_power_6822():
    assert power_6822(2, 8) == 256

def test_min_6823():
    assert min_6823(3, 7) == 3

def test_max_6824():
    assert max_6824(3, 7) == 7
