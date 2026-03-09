"""Tests for test module 1314 — covers src modules [5253, 5254, 5255, 5256]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5253 import modulo_5253
from module_5254 import power_5254
from module_5255 import min_5255
from module_5256 import max_5256

def test_modulo_5253():
    assert modulo_5253(10, 3) == 1

def test_power_5254():
    assert power_5254(2, 8) == 256

def test_min_5255():
    assert min_5255(3, 7) == 3

def test_max_5256():
    assert max_5256(3, 7) == 7
