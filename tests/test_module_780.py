"""Tests for test module 780 — covers src modules [3117, 3118, 3119, 3120]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3117 import modulo_3117
from module_3118 import power_3118
from module_3119 import min_3119
from module_3120 import max_3120

def test_modulo_3117():
    assert modulo_3117(10, 3) == 1

def test_power_3118():
    assert power_3118(2, 8) == 256

def test_min_3119():
    assert min_3119(3, 7) == 3

def test_max_3120():
    assert max_3120(3, 7) == 7
