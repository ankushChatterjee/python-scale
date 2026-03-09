"""Tests for test module 1814 — covers src modules [7253, 7254, 7255, 7256]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7253 import modulo_7253
from module_7254 import power_7254
from module_7255 import min_7255
from module_7256 import max_7256

def test_modulo_7253():
    assert modulo_7253(10, 3) == 1

def test_power_7254():
    assert power_7254(2, 8) == 256

def test_min_7255():
    assert min_7255(3, 7) == 3

def test_max_7256():
    assert max_7256(3, 7) == 7
