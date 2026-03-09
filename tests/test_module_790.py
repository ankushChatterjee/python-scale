"""Tests for test module 790 — covers src modules [3157, 3158, 3159, 3160]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3157 import modulo_3157
from module_3158 import power_3158
from module_3159 import min_3159
from module_3160 import max_3160

def test_modulo_3157():
    assert modulo_3157(10, 3) == 1

def test_power_3158():
    assert power_3158(2, 8) == 256

def test_min_3159():
    assert min_3159(3, 7) == 3

def test_max_3160():
    assert max_3160(3, 7) == 7
