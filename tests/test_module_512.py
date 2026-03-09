"""Tests for test module 512 — covers src modules [2045, 2046, 2047, 2048]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2045 import modulo_2045
from module_2046 import power_2046
from module_2047 import min_2047
from module_2048 import max_2048

def test_modulo_2045():
    assert modulo_2045(10, 3) == 1

def test_power_2046():
    assert power_2046(2, 8) == 256

def test_min_2047():
    assert min_2047(3, 7) == 3

def test_max_2048():
    assert max_2048(3, 7) == 7
