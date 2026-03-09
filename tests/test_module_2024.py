"""Tests for test module 2024 — covers src modules [8093, 8094, 8095, 8096]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8093 import modulo_8093
from module_8094 import power_8094
from module_8095 import min_8095
from module_8096 import max_8096

def test_modulo_8093():
    assert modulo_8093(10, 3) == 1

def test_power_8094():
    assert power_8094(2, 8) == 256

def test_min_8095():
    assert min_8095(3, 7) == 3

def test_max_8096():
    assert max_8096(3, 7) == 7
