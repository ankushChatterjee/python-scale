"""Tests for test module 1956 — covers src modules [7821, 7822, 7823, 7824]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7821 import modulo_7821
from module_7822 import power_7822
from module_7823 import min_7823
from module_7824 import max_7824

def test_modulo_7821():
    assert modulo_7821(10, 3) == 1

def test_power_7822():
    assert power_7822(2, 8) == 256

def test_min_7823():
    assert min_7823(3, 7) == 3

def test_max_7824():
    assert max_7824(3, 7) == 7
