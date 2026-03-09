"""Tests for test module 1818 — covers src modules [7269, 7270, 7271, 7272]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7269 import modulo_7269
from module_7270 import power_7270
from module_7271 import min_7271
from module_7272 import max_7272

def test_modulo_7269():
    assert modulo_7269(10, 3) == 1

def test_power_7270():
    assert power_7270(2, 8) == 256

def test_min_7271():
    assert min_7271(3, 7) == 3

def test_max_7272():
    assert max_7272(3, 7) == 7
