"""Tests for test module 2068 — covers src modules [8269, 8270, 8271, 8272]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8269 import modulo_8269
from module_8270 import power_8270
from module_8271 import min_8271
from module_8272 import max_8272

def test_modulo_8269():
    assert modulo_8269(10, 3) == 1

def test_power_8270():
    assert power_8270(2, 8) == 256

def test_min_8271():
    assert min_8271(3, 7) == 3

def test_max_8272():
    assert max_8272(3, 7) == 7
