"""Tests for test module 1044 — covers src modules [4173, 4174, 4175, 4176]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4173 import modulo_4173
from module_4174 import power_4174
from module_4175 import min_4175
from module_4176 import max_4176

def test_modulo_4173():
    assert modulo_4173(10, 3) == 1

def test_power_4174():
    assert power_4174(2, 8) == 256

def test_min_4175():
    assert min_4175(3, 7) == 3

def test_max_4176():
    assert max_4176(3, 7) == 7
