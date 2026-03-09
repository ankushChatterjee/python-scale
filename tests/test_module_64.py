"""Tests for test module 64 — covers src modules [253, 254, 255, 256]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_253 import modulo_253
from module_254 import power_254
from module_255 import min_255
from module_256 import max_256

def test_modulo_253():
    assert modulo_253(10, 3) == 1

def test_power_254():
    assert power_254(2, 8) == 256

def test_min_255():
    assert min_255(3, 7) == 3

def test_max_256():
    assert max_256(3, 7) == 7
