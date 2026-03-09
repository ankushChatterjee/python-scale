"""Tests for test module 2274 — covers src modules [9093, 9094, 9095, 9096]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9093 import modulo_9093
from module_9094 import power_9094
from module_9095 import min_9095
from module_9096 import max_9096

def test_modulo_9093():
    assert modulo_9093(10, 3) == 1

def test_power_9094():
    assert power_9094(2, 8) == 256

def test_min_9095():
    assert min_9095(3, 7) == 3

def test_max_9096():
    assert max_9096(3, 7) == 7
