"""Tests for test module 2294 — covers src modules [9173, 9174, 9175, 9176]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9173 import modulo_9173
from module_9174 import power_9174
from module_9175 import min_9175
from module_9176 import max_9176

def test_modulo_9173():
    assert modulo_9173(10, 3) == 1

def test_power_9174():
    assert power_9174(2, 8) == 256

def test_min_9175():
    assert min_9175(3, 7) == 3

def test_max_9176():
    assert max_9176(3, 7) == 7
