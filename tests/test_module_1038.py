"""Tests for test module 1038 — covers src modules [4149, 4150, 4151, 4152]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4149 import modulo_4149
from module_4150 import power_4150
from module_4151 import min_4151
from module_4152 import max_4152

def test_modulo_4149():
    assert modulo_4149(10, 3) == 1

def test_power_4150():
    assert power_4150(2, 8) == 256

def test_min_4151():
    assert min_4151(3, 7) == 3

def test_max_4152():
    assert max_4152(3, 7) == 7
