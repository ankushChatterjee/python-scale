"""Tests for test module 12 — covers src modules [45, 46, 47, 48]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_45 import modulo_45
from module_46 import power_46
from module_47 import min_47
from module_48 import max_48

def test_modulo_45():
    assert modulo_45(10, 3) == 1

def test_power_46():
    assert power_46(2, 8) == 256

def test_min_47():
    assert min_47(3, 7) == 3

def test_max_48():
    assert max_48(3, 7) == 7
