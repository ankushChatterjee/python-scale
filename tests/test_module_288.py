"""Tests for test module 288 — covers src modules [1149, 1150, 1151, 1152]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1149 import modulo_1149
from module_1150 import power_1150
from module_1151 import min_1151
from module_1152 import max_1152

def test_modulo_1149():
    assert modulo_1149(10, 3) == 1

def test_power_1150():
    assert power_1150(2, 8) == 256

def test_min_1151():
    assert min_1151(3, 7) == 3

def test_max_1152():
    assert max_1152(3, 7) == 7
