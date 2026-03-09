"""Tests for test module 1066 — covers src modules [4261, 4262, 4263, 4264]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4261 import modulo_4261
from module_4262 import power_4262
from module_4263 import min_4263
from module_4264 import max_4264

def test_modulo_4261():
    assert modulo_4261(10, 3) == 1

def test_power_4262():
    assert power_4262(2, 8) == 256

def test_min_4263():
    assert min_4263(3, 7) == 3

def test_max_4264():
    assert max_4264(3, 7) == 7
