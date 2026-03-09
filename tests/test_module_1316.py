"""Tests for test module 1316 — covers src modules [5261, 5262, 5263, 5264]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5261 import modulo_5261
from module_5262 import power_5262
from module_5263 import min_5263
from module_5264 import max_5264

def test_modulo_5261():
    assert modulo_5261(10, 3) == 1

def test_power_5262():
    assert power_5262(2, 8) == 256

def test_min_5263():
    assert min_5263(3, 7) == 3

def test_max_5264():
    assert max_5264(3, 7) == 7
