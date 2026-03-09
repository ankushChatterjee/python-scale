"""Tests for test module 1284 — covers src modules [5133, 5134, 5135, 5136]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5133 import modulo_5133
from module_5134 import power_5134
from module_5135 import min_5135
from module_5136 import max_5136

def test_modulo_5133():
    assert modulo_5133(10, 3) == 1

def test_power_5134():
    assert power_5134(2, 8) == 256

def test_min_5135():
    assert min_5135(3, 7) == 3

def test_max_5136():
    assert max_5136(3, 7) == 7
