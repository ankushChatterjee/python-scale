"""Tests for test module 1030 — covers src modules [4117, 4118, 4119, 4120]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4117 import modulo_4117
from module_4118 import power_4118
from module_4119 import min_4119
from module_4120 import max_4120

def test_modulo_4117():
    assert modulo_4117(10, 3) == 1

def test_power_4118():
    assert power_4118(2, 8) == 256

def test_min_4119():
    assert min_4119(3, 7) == 3

def test_max_4120():
    assert max_4120(3, 7) == 7
