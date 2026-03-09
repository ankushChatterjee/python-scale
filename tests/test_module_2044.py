"""Tests for test module 2044 — covers src modules [8173, 8174, 8175, 8176]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8173 import modulo_8173
from module_8174 import power_8174
from module_8175 import min_8175
from module_8176 import max_8176

def test_modulo_8173():
    assert modulo_8173(10, 3) == 1

def test_power_8174():
    assert power_8174(2, 8) == 256

def test_min_8175():
    assert min_8175(3, 7) == 3

def test_max_8176():
    assert max_8176(3, 7) == 7
