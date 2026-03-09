"""Tests for test module 294 — covers src modules [1173, 1174, 1175, 1176]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1173 import modulo_1173
from module_1174 import power_1174
from module_1175 import min_1175
from module_1176 import max_1176

def test_modulo_1173():
    assert modulo_1173(10, 3) == 1

def test_power_1174():
    assert power_1174(2, 8) == 256

def test_min_1175():
    assert min_1175(3, 7) == 3

def test_max_1176():
    assert max_1176(3, 7) == 7
