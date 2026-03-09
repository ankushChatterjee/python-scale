"""Tests for test module 16 — covers src modules [61, 62, 63, 64]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_61 import modulo_61
from module_62 import power_62
from module_63 import min_63
from module_64 import max_64

def test_modulo_61():
    assert modulo_61(10, 3) == 1

def test_power_62():
    assert power_62(2, 8) == 256

def test_min_63():
    assert min_63(3, 7) == 3

def test_max_64():
    assert max_64(3, 7) == 7
