"""Tests for test module 2272 — covers src modules [9085, 9086, 9087, 9088]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9085 import modulo_9085
from module_9086 import power_9086
from module_9087 import min_9087
from module_9088 import max_9088

def test_modulo_9085():
    assert modulo_9085(10, 3) == 1

def test_power_9086():
    assert power_9086(2, 8) == 256

def test_min_9087():
    assert min_9087(3, 7) == 3

def test_max_9088():
    assert max_9088(3, 7) == 7
