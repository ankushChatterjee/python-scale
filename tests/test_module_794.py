"""Tests for test module 794 — covers src modules [3173, 3174, 3175, 3176]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3173 import modulo_3173
from module_3174 import power_3174
from module_3175 import min_3175
from module_3176 import max_3176

def test_modulo_3173():
    assert modulo_3173(10, 3) == 1

def test_power_3174():
    assert power_3174(2, 8) == 256

def test_min_3175():
    assert min_3175(3, 7) == 3

def test_max_3176():
    assert max_3176(3, 7) == 7
