"""Tests for test module 1566 — covers src modules [6261, 6262, 6263, 6264]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6261 import modulo_6261
from module_6262 import power_6262
from module_6263 import min_6263
from module_6264 import max_6264

def test_modulo_6261():
    assert modulo_6261(10, 3) == 1

def test_power_6262():
    assert power_6262(2, 8) == 256

def test_min_6263():
    assert min_6263(3, 7) == 3

def test_max_6264():
    assert max_6264(3, 7) == 7
