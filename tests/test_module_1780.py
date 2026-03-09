"""Tests for test module 1780 — covers src modules [7117, 7118, 7119, 7120]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7117 import modulo_7117
from module_7118 import power_7118
from module_7119 import min_7119
from module_7120 import max_7120

def test_modulo_7117():
    assert modulo_7117(10, 3) == 1

def test_power_7118():
    assert power_7118(2, 8) == 256

def test_min_7119():
    assert min_7119(3, 7) == 3

def test_max_7120():
    assert max_7120(3, 7) == 7
