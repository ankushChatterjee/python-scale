"""Tests for test module 540 — covers src modules [2157, 2158, 2159, 2160]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2157 import modulo_2157
from module_2158 import power_2158
from module_2159 import min_2159
from module_2160 import max_2160

def test_modulo_2157():
    assert modulo_2157(10, 3) == 1

def test_power_2158():
    assert power_2158(2, 8) == 256

def test_min_2159():
    assert min_2159(3, 7) == 3

def test_max_2160():
    assert max_2160(3, 7) == 7
