"""Tests for test module 318 — covers src modules [1269, 1270, 1271, 1272]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1269 import modulo_1269
from module_1270 import power_1270
from module_1271 import min_1271
from module_1272 import max_1272

def test_modulo_1269():
    assert modulo_1269(10, 3) == 1

def test_power_1270():
    assert power_1270(2, 8) == 256

def test_min_1271():
    assert min_1271(3, 7) == 3

def test_max_1272():
    assert max_1272(3, 7) == 7
