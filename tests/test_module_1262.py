"""Tests for test module 1262 — covers src modules [5045, 5046, 5047, 5048]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5045 import modulo_5045
from module_5046 import power_5046
from module_5047 import min_5047
from module_5048 import max_5048

def test_modulo_5045():
    assert modulo_5045(10, 3) == 1

def test_power_5046():
    assert power_5046(2, 8) == 256

def test_min_5047():
    assert min_5047(3, 7) == 3

def test_max_5048():
    assert max_5048(3, 7) == 7
