"""Tests for test module 1530 — covers src modules [6117, 6118, 6119, 6120]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6117 import modulo_6117
from module_6118 import power_6118
from module_6119 import min_6119
from module_6120 import max_6120

def test_modulo_6117():
    assert modulo_6117(10, 3) == 1

def test_power_6118():
    assert power_6118(2, 8) == 256

def test_min_6119():
    assert min_6119(3, 7) == 3

def test_max_6120():
    assert max_6120(3, 7) == 7
