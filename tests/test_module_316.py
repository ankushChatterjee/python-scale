"""Tests for test module 316 — covers src modules [1261, 1262, 1263, 1264]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1261 import modulo_1261
from module_1262 import power_1262
from module_1263 import min_1263
from module_1264 import max_1264

def test_modulo_1261():
    assert modulo_1261(10, 3) == 1

def test_power_1262():
    assert power_1262(2, 8) == 256

def test_min_1263():
    assert min_1263(3, 7) == 3

def test_max_1264():
    assert max_1264(3, 7) == 7
