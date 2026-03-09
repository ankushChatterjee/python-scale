"""Tests for test module 2040 — covers src modules [8157, 8158, 8159, 8160]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8157 import modulo_8157
from module_8158 import power_8158
from module_8159 import min_8159
from module_8160 import max_8160

def test_modulo_8157():
    assert modulo_8157(10, 3) == 1

def test_power_8158():
    assert power_8158(2, 8) == 256

def test_min_8159():
    assert min_8159(3, 7) == 3

def test_max_8160():
    assert max_8160(3, 7) == 7
