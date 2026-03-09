"""Tests for test module 1816 — covers src modules [7261, 7262, 7263, 7264]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7261 import modulo_7261
from module_7262 import power_7262
from module_7263 import min_7263
from module_7264 import max_7264

def test_modulo_7261():
    assert modulo_7261(10, 3) == 1

def test_power_7262():
    assert power_7262(2, 8) == 256

def test_min_7263():
    assert min_7263(3, 7) == 3

def test_max_7264():
    assert max_7264(3, 7) == 7
