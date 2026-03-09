"""Tests for test module 1320 — covers src modules [5277, 5278, 5279, 5280]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5277 import modulo_5277
from module_5278 import power_5278
from module_5279 import min_5279
from module_5280 import max_5280

def test_modulo_5277():
    assert modulo_5277(10, 3) == 1

def test_power_5278():
    assert power_5278(2, 8) == 256

def test_min_5279():
    assert min_5279(3, 7) == 3

def test_max_5280():
    assert max_5280(3, 7) == 7
