"""Tests for test module 30 — covers src modules [117, 118, 119, 120]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_117 import modulo_117
from module_118 import power_118
from module_119 import min_119
from module_120 import max_120

def test_modulo_117():
    assert modulo_117(10, 3) == 1

def test_power_118():
    assert power_118(2, 8) == 256

def test_min_119():
    assert min_119(3, 7) == 3

def test_max_120():
    assert max_120(3, 7) == 7
