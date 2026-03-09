"""Tests for test module 1774 — covers src modules [7093, 7094, 7095, 7096]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7093 import modulo_7093
from module_7094 import power_7094
from module_7095 import min_7095
from module_7096 import max_7096

def test_modulo_7093():
    assert modulo_7093(10, 3) == 1

def test_power_7094():
    assert power_7094(2, 8) == 256

def test_min_7095():
    assert min_7095(3, 7) == 3

def test_max_7096():
    assert max_7096(3, 7) == 7
