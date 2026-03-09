"""Tests for test module 1318 — covers src modules [5269, 5270, 5271, 5272]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5269 import modulo_5269
from module_5270 import power_5270
from module_5271 import min_5271
from module_5272 import max_5272

def test_modulo_5269():
    assert modulo_5269(10, 3) == 1

def test_power_5270():
    assert power_5270(2, 8) == 256

def test_min_5271():
    assert min_5271(3, 7) == 3

def test_max_5272():
    assert max_5272(3, 7) == 7
