"""Tests for test module 788 — covers src modules [3149, 3150, 3151, 3152]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3149 import modulo_3149
from module_3150 import power_3150
from module_3151 import min_3151
from module_3152 import max_3152

def test_modulo_3149():
    assert modulo_3149(10, 3) == 1

def test_power_3150():
    assert power_3150(2, 8) == 256

def test_min_3151():
    assert min_3151(3, 7) == 3

def test_max_3152():
    assert max_3152(3, 7) == 7
