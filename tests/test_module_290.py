"""Tests for test module 290 — covers src modules [1157, 1158, 1159, 1160]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1157 import modulo_1157
from module_1158 import power_1158
from module_1159 import min_1159
from module_1160 import max_1160

def test_modulo_1157():
    assert modulo_1157(10, 3) == 1

def test_power_1158():
    assert power_1158(2, 8) == 256

def test_min_1159():
    assert min_1159(3, 7) == 3

def test_max_1160():
    assert max_1160(3, 7) == 7
