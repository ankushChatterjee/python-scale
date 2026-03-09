"""Tests for test module 8 — covers src modules [29, 30, 31, 32]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_29 import modulo_29
from module_30 import power_30
from module_31 import min_31
from module_32 import max_32

def test_modulo_29():
    assert modulo_29(10, 3) == 1

def test_power_30():
    assert power_30(2, 8) == 256

def test_min_31():
    assert min_31(3, 7) == 3

def test_max_32():
    assert max_32(3, 7) == 7
