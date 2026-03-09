"""Tests for test module 314 — covers src modules [1253, 1254, 1255, 1256]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1253 import modulo_1253
from module_1254 import power_1254
from module_1255 import min_1255
from module_1256 import max_1256

def test_modulo_1253():
    assert modulo_1253(10, 3) == 1

def test_power_1254():
    assert power_1254(2, 8) == 256

def test_min_1255():
    assert min_1255(3, 7) == 3

def test_max_1256():
    assert max_1256(3, 7) == 7
