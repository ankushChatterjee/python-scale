"""Tests for test module 2066 — covers src modules [8261, 8262, 8263, 8264]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8261 import modulo_8261
from module_8262 import power_8262
from module_8263 import min_8263
from module_8264 import max_8264

def test_modulo_8261():
    assert modulo_8261(10, 3) == 1

def test_power_8262():
    assert power_8262(2, 8) == 256

def test_min_8263():
    assert min_8263(3, 7) == 3

def test_max_8264():
    assert max_8264(3, 7) == 7
