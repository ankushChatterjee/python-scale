"""Tests for test module 454 — covers src modules [1813, 1814, 1815, 1816]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1813 import modulo_1813
from module_1814 import power_1814
from module_1815 import min_1815
from module_1816 import max_1816

def test_modulo_1813():
    assert modulo_1813(10, 3) == 1

def test_power_1814():
    assert power_1814(2, 8) == 256

def test_min_1815():
    assert min_1815(3, 7) == 3

def test_max_1816():
    assert max_1816(3, 7) == 7
