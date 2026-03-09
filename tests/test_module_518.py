"""Tests for test module 518 — covers src modules [2069, 2070, 2071, 2072]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2069 import modulo_2069
from module_2070 import power_2070
from module_2071 import min_2071
from module_2072 import max_2072

def test_modulo_2069():
    assert modulo_2069(10, 3) == 1

def test_power_2070():
    assert power_2070(2, 8) == 256

def test_min_2071():
    assert min_2071(3, 7) == 3

def test_max_2072():
    assert max_2072(3, 7) == 7
