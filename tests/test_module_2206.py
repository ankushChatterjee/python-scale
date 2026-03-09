"""Tests for test module 2206 — covers src modules [8821, 8822, 8823, 8824]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8821 import modulo_8821
from module_8822 import power_8822
from module_8823 import min_8823
from module_8824 import max_8824

def test_modulo_8821():
    assert modulo_8821(10, 3) == 1

def test_power_8822():
    assert power_8822(2, 8) == 256

def test_min_8823():
    assert min_8823(3, 7) == 3

def test_max_8824():
    assert max_8824(3, 7) == 7
