"""Tests for test module 1280 — covers src modules [5117, 5118, 5119, 5120]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5117 import modulo_5117
from module_5118 import power_5118
from module_5119 import min_5119
from module_5120 import max_5120

def test_modulo_5117():
    assert modulo_5117(10, 3) == 1

def test_power_5118():
    assert power_5118(2, 8) == 256

def test_min_5119():
    assert min_5119(3, 7) == 3

def test_max_5120():
    assert max_5120(3, 7) == 7
