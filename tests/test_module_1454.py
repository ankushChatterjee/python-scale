"""Tests for test module 1454 — covers src modules [5813, 5814, 5815, 5816]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5813 import modulo_5813
from module_5814 import power_5814
from module_5815 import min_5815
from module_5816 import max_5816

def test_modulo_5813():
    assert modulo_5813(10, 3) == 1

def test_power_5814():
    assert power_5814(2, 8) == 256

def test_min_5815():
    assert min_5815(3, 7) == 3

def test_max_5816():
    assert max_5816(3, 7) == 7
