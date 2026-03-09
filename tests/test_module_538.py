"""Tests for test module 538 — covers src modules [2149, 2150, 2151, 2152]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2149 import modulo_2149
from module_2150 import power_2150
from module_2151 import min_2151
from module_2152 import max_2152

def test_modulo_2149():
    assert modulo_2149(10, 3) == 1

def test_power_2150():
    assert power_2150(2, 8) == 256

def test_min_2151():
    assert min_2151(3, 7) == 3

def test_max_2152():
    assert max_2152(3, 7) == 7
