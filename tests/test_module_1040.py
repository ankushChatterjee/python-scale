"""Tests for test module 1040 — covers src modules [4157, 4158, 4159, 4160]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4157 import modulo_4157
from module_4158 import power_4158
from module_4159 import min_4159
from module_4160 import max_4160

def test_modulo_4157():
    assert modulo_4157(10, 3) == 1

def test_power_4158():
    assert power_4158(2, 8) == 256

def test_min_4159():
    assert min_4159(3, 7) == 3

def test_max_4160():
    assert max_4160(3, 7) == 7
