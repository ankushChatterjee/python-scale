"""Tests for test module 530 — covers src modules [2117, 2118, 2119, 2120]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2117 import modulo_2117
from module_2118 import power_2118
from module_2119 import min_2119
from module_2120 import max_2120

def test_modulo_2117():
    assert modulo_2117(10, 3) == 1

def test_power_2118():
    assert power_2118(2, 8) == 256

def test_min_2119():
    assert min_2119(3, 7) == 3

def test_max_2120():
    assert max_2120(3, 7) == 7
