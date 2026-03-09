"""Tests for test module 762 — covers src modules [3045, 3046, 3047, 3048]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3045 import modulo_3045
from module_3046 import power_3046
from module_3047 import min_3047
from module_3048 import max_3048

def test_modulo_3045():
    assert modulo_3045(10, 3) == 1

def test_power_3046():
    assert power_3046(2, 8) == 256

def test_min_3047():
    assert min_3047(3, 7) == 3

def test_max_3048():
    assert max_3048(3, 7) == 7
