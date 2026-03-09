"""Tests for test module 1788 — covers src modules [7149, 7150, 7151, 7152]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7149 import modulo_7149
from module_7150 import power_7150
from module_7151 import min_7151
from module_7152 import max_7152

def test_modulo_7149():
    assert modulo_7149(10, 3) == 1

def test_power_7150():
    assert power_7150(2, 8) == 256

def test_min_7151():
    assert min_7151(3, 7) == 3

def test_max_7152():
    assert max_7152(3, 7) == 7
