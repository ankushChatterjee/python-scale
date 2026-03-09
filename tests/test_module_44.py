"""Tests for test module 44 — covers src modules [173, 174, 175, 176]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_173 import modulo_173
from module_174 import power_174
from module_175 import min_175
from module_176 import max_176

def test_modulo_173():
    assert modulo_173(10, 3) == 1

def test_power_174():
    assert power_174(2, 8) == 256

def test_min_175():
    assert min_175(3, 7) == 3

def test_max_176():
    assert max_176(3, 7) == 7
