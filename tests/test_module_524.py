"""Tests for test module 524 — covers src modules [2093, 2094, 2095, 2096]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2093 import modulo_2093
from module_2094 import power_2094
from module_2095 import min_2095
from module_2096 import max_2096

def test_modulo_2093():
    assert modulo_2093(10, 3) == 1

def test_power_2094():
    assert power_2094(2, 8) == 256

def test_min_2095():
    assert min_2095(3, 7) == 3

def test_max_2096():
    assert max_2096(3, 7) == 7
