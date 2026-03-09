"""Tests for test module 2192 — covers src modules [8765, 8766, 8767, 8768]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8765 import modulo_8765
from module_8766 import power_8766
from module_8767 import min_8767
from module_8768 import max_8768

def test_modulo_8765():
    assert modulo_8765(10, 3) == 1

def test_power_8766():
    assert power_8766(2, 8) == 256

def test_min_8767():
    assert min_8767(3, 7) == 3

def test_max_8768():
    assert max_8768(3, 7) == 7
