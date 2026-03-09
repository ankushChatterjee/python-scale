"""Tests for test module 1524 — covers src modules [6093, 6094, 6095, 6096]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6093 import modulo_6093
from module_6094 import power_6094
from module_6095 import min_6095
from module_6096 import max_6096

def test_modulo_6093():
    assert modulo_6093(10, 3) == 1

def test_power_6094():
    assert power_6094(2, 8) == 256

def test_min_6095():
    assert min_6095(3, 7) == 3

def test_max_6096():
    assert max_6096(3, 7) == 7
