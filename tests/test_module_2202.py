"""Tests for test module 2202 — covers src modules [8805, 8806, 8807, 8808]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8805 import modulo_8805
from module_8806 import power_8806
from module_8807 import min_8807
from module_8808 import max_8808

def test_modulo_8805():
    assert modulo_8805(10, 3) == 1

def test_power_8806():
    assert power_8806(2, 8) == 256

def test_min_8807():
    assert min_8807(3, 7) == 3

def test_max_8808():
    assert max_8808(3, 7) == 7
