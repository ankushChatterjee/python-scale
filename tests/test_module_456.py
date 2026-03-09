"""Tests for test module 456 — covers src modules [1821, 1822, 1823, 1824]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1821 import modulo_1821
from module_1822 import power_1822
from module_1823 import min_1823
from module_1824 import max_1824

def test_modulo_1821():
    assert modulo_1821(10, 3) == 1

def test_power_1822():
    assert power_1822(2, 8) == 256

def test_min_1823():
    assert min_1823(3, 7) == 3

def test_max_1824():
    assert max_1824(3, 7) == 7
