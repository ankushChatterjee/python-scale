"""Tests for test module 38 — covers src modules [149, 150, 151, 152]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_149 import modulo_149
from module_150 import power_150
from module_151 import min_151
from module_152 import max_152

def test_modulo_149():
    assert modulo_149(10, 3) == 1

def test_power_150():
    assert power_150(2, 8) == 256

def test_min_151():
    assert min_151(3, 7) == 3

def test_max_152():
    assert max_152(3, 7) == 7
