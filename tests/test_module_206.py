"""Tests for test module 206 — covers src modules [821, 822, 823, 824]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_821 import modulo_821
from module_822 import power_822
from module_823 import min_823
from module_824 import max_824

def test_modulo_821():
    assert modulo_821(10, 3) == 1

def test_power_822():
    assert power_822(2, 8) == 256

def test_min_823():
    assert min_823(3, 7) == 3

def test_max_824():
    assert max_824(3, 7) == 7
