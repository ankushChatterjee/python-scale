"""Tests for test module 1456 — covers src modules [5821, 5822, 5823, 5824]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5821 import modulo_5821
from module_5822 import power_5822
from module_5823 import min_5823
from module_5824 import max_5824

def test_modulo_5821():
    assert modulo_5821(10, 3) == 1

def test_power_5822():
    assert power_5822(2, 8) == 256

def test_min_5823():
    assert min_5823(3, 7) == 3

def test_max_5824():
    assert max_5824(3, 7) == 7
