"""Tests for test module 1024 — covers src modules [4093, 4094, 4095, 4096]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4093 import modulo_4093
from module_4094 import power_4094
from module_4095 import min_4095
from module_4096 import max_4096

def test_modulo_4093():
    assert modulo_4093(10, 3) == 1

def test_power_4094():
    assert power_4094(2, 8) == 256

def test_min_4095():
    assert min_4095(3, 7) == 3

def test_max_4096():
    assert max_4096(3, 7) == 7
