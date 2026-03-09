"""Tests for test module 544 — covers src modules [2173, 2174, 2175, 2176]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2173 import modulo_2173
from module_2174 import power_2174
from module_2175 import min_2175
from module_2176 import max_2176

def test_modulo_2173():
    assert modulo_2173(10, 3) == 1

def test_power_2174():
    assert power_2174(2, 8) == 256

def test_min_2175():
    assert min_2175(3, 7) == 3

def test_max_2176():
    assert max_2176(3, 7) == 7
