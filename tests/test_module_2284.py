"""Tests for test module 2284 — covers src modules [9133, 9134, 9135, 9136]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9133 import modulo_9133
from module_9134 import power_9134
from module_9135 import min_9135
from module_9136 import max_9136

def test_modulo_9133():
    assert modulo_9133(10, 3) == 1

def test_power_9134():
    assert power_9134(2, 8) == 256

def test_min_9135():
    assert min_9135(3, 7) == 3

def test_max_9136():
    assert max_9136(3, 7) == 7
