"""Tests for test module 816 — covers src modules [3261, 3262, 3263, 3264]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3261 import modulo_3261
from module_3262 import power_3262
from module_3263 import min_3263
from module_3264 import max_3264

def test_modulo_3261():
    assert modulo_3261(10, 3) == 1

def test_power_3262():
    assert power_3262(2, 8) == 256

def test_min_3263():
    assert min_3263(3, 7) == 3

def test_max_3264():
    assert max_3264(3, 7) == 7
