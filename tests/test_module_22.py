"""Tests for test module 22 — covers src modules [85, 86, 87, 88]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_85 import modulo_85
from module_86 import power_86
from module_87 import min_87
from module_88 import max_88

def test_modulo_85():
    assert modulo_85(10, 3) == 1

def test_power_86():
    assert power_86(2, 8) == 256

def test_min_87():
    assert min_87(3, 7) == 3

def test_max_88():
    assert max_88(3, 7) == 7
