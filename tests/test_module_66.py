"""Tests for test module 66 — covers src modules [261, 262, 263, 264]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_261 import modulo_261
from module_262 import power_262
from module_263 import min_263
from module_264 import max_264

def test_modulo_261():
    assert modulo_261(10, 3) == 1

def test_power_262():
    assert power_262(2, 8) == 256

def test_min_263():
    assert min_263(3, 7) == 3

def test_max_264():
    assert max_264(3, 7) == 7
