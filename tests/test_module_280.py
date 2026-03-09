"""Tests for test module 280 — covers src modules [1117, 1118, 1119, 1120]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1117 import modulo_1117
from module_1118 import power_1118
from module_1119 import min_1119
from module_1120 import max_1120

def test_modulo_1117():
    assert modulo_1117(10, 3) == 1

def test_power_1118():
    assert power_1118(2, 8) == 256

def test_min_1119():
    assert min_1119(3, 7) == 3

def test_max_1120():
    assert max_1120(3, 7) == 7
