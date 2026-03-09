"""Tests for test module 2038 — covers src modules [8149, 8150, 8151, 8152]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8149 import modulo_8149
from module_8150 import power_8150
from module_8151 import min_8151
from module_8152 import max_8152

def test_modulo_8149():
    assert modulo_8149(10, 3) == 1

def test_power_8150():
    assert power_8150(2, 8) == 256

def test_min_8151():
    assert min_8151(3, 7) == 3

def test_max_8152():
    assert max_8152(3, 7) == 7
