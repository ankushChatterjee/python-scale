"""Tests for test module 1538 — covers src modules [6149, 6150, 6151, 6152]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6149 import modulo_6149
from module_6150 import power_6150
from module_6151 import min_6151
from module_6152 import max_6152

def test_modulo_6149():
    assert modulo_6149(10, 3) == 1

def test_power_6150():
    assert power_6150(2, 8) == 256

def test_min_6151():
    assert min_6151(3, 7) == 3

def test_max_6152():
    assert max_6152(3, 7) == 7
