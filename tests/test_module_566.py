"""Tests for test module 566 — covers src modules [2261, 2262, 2263, 2264]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2261 import modulo_2261
from module_2262 import power_2262
from module_2263 import min_2263
from module_2264 import max_2264

def test_modulo_2261():
    assert modulo_2261(10, 3) == 1

def test_power_2262():
    assert power_2262(2, 8) == 256

def test_min_2263():
    assert min_2263(3, 7) == 3

def test_max_2264():
    assert max_2264(3, 7) == 7
