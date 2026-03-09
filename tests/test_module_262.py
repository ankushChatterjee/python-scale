"""Tests for test module 262 — covers src modules [1045, 1046, 1047, 1048]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1045 import modulo_1045
from module_1046 import power_1046
from module_1047 import min_1047
from module_1048 import max_1048

def test_modulo_1045():
    assert modulo_1045(10, 3) == 1

def test_power_1046():
    assert power_1046(2, 8) == 256

def test_min_1047():
    assert min_1047(3, 7) == 3

def test_max_1048():
    assert max_1048(3, 7) == 7
