"""Tests for test module 1534 — covers src modules [6133, 6134, 6135, 6136]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6133 import modulo_6133
from module_6134 import power_6134
from module_6135 import min_6135
from module_6136 import max_6136

def test_modulo_6133():
    assert modulo_6133(10, 3) == 1

def test_power_6134():
    assert power_6134(2, 8) == 256

def test_min_6135():
    assert min_6135(3, 7) == 3

def test_max_6136():
    assert max_6136(3, 7) == 7
