"""Tests for test module 1794 — covers src modules [7173, 7174, 7175, 7176]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7173 import modulo_7173
from module_7174 import power_7174
from module_7175 import min_7175
from module_7176 import max_7176

def test_modulo_7173():
    assert modulo_7173(10, 3) == 1

def test_power_7174():
    assert power_7174(2, 8) == 256

def test_min_7175():
    assert min_7175(3, 7) == 3

def test_max_7176():
    assert max_7176(3, 7) == 7
