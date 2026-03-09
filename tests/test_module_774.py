"""Tests for test module 774 — covers src modules [3093, 3094, 3095, 3096]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3093 import modulo_3093
from module_3094 import power_3094
from module_3095 import min_3095
from module_3096 import max_3096

def test_modulo_3093():
    assert modulo_3093(10, 3) == 1

def test_power_3094():
    assert power_3094(2, 8) == 256

def test_min_3095():
    assert min_3095(3, 7) == 3

def test_max_3096():
    assert max_3096(3, 7) == 7
