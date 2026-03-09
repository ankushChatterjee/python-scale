"""Tests for test module 1544 — covers src modules [6173, 6174, 6175, 6176]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6173 import modulo_6173
from module_6174 import power_6174
from module_6175 import min_6175
from module_6176 import max_6176

def test_modulo_6173():
    assert modulo_6173(10, 3) == 1

def test_power_6174():
    assert power_6174(2, 8) == 256

def test_min_6175():
    assert min_6175(3, 7) == 3

def test_max_6176():
    assert max_6176(3, 7) == 7
