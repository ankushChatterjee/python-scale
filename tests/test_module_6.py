"""Tests for test module 6 — covers src modules [21, 22, 23, 24]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_21 import modulo_21
from module_22 import power_22
from module_23 import min_23
from module_24 import max_24

def test_modulo_21():
    assert modulo_21(10, 3) == 1

def test_power_22():
    assert power_22(2, 8) == 256

def test_min_23():
    assert min_23(3, 7) == 3

def test_max_24():
    assert max_24(3, 7) == 7
