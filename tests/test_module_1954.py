"""Tests for test module 1954 — covers src modules [7813, 7814, 7815, 7816]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7813 import modulo_7813
from module_7814 import power_7814
from module_7815 import min_7815
from module_7816 import max_7816

def test_modulo_7813():
    assert modulo_7813(10, 3) == 1

def test_power_7814():
    assert power_7814(2, 8) == 256

def test_min_7815():
    assert min_7815(3, 7) == 3

def test_max_7816():
    assert max_7816(3, 7) == 7
