"""Tests for test module 1294 — covers src modules [5173, 5174, 5175, 5176]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5173 import modulo_5173
from module_5174 import power_5174
from module_5175 import min_5175
from module_5176 import max_5176

def test_modulo_5173():
    assert modulo_5173(10, 3) == 1

def test_power_5174():
    assert power_5174(2, 8) == 256

def test_min_5175():
    assert min_5175(3, 7) == 3

def test_max_5176():
    assert max_5176(3, 7) == 7
