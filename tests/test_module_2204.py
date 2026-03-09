"""Tests for test module 2204 — covers src modules [8813, 8814, 8815, 8816]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8813 import modulo_8813
from module_8814 import power_8814
from module_8815 import min_8815
from module_8816 import max_8816

def test_modulo_8813():
    assert modulo_8813(10, 3) == 1

def test_power_8814():
    assert power_8814(2, 8) == 256

def test_min_8815():
    assert min_8815(3, 7) == 3

def test_max_8816():
    assert max_8816(3, 7) == 7
