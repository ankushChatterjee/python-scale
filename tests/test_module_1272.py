"""Tests for test module 1272 — covers src modules [5085, 5086, 5087, 5088]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5085 import modulo_5085
from module_5086 import power_5086
from module_5087 import min_5087
from module_5088 import max_5088

def test_modulo_5085():
    assert modulo_5085(10, 3) == 1

def test_power_5086():
    assert power_5086(2, 8) == 256

def test_min_5087():
    assert min_5087(3, 7) == 3

def test_max_5088():
    assert max_5088(3, 7) == 7
