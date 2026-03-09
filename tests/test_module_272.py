"""Tests for test module 272 — covers src modules [1085, 1086, 1087, 1088]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1085 import modulo_1085
from module_1086 import power_1086
from module_1087 import min_1087
from module_1088 import max_1088

def test_modulo_1085():
    assert modulo_1085(10, 3) == 1

def test_power_1086():
    assert power_1086(2, 8) == 256

def test_min_1087():
    assert min_1087(3, 7) == 3

def test_max_1088():
    assert max_1088(3, 7) == 7
