"""Tests for test module 1702 — covers src modules [6805, 6806, 6807, 6808]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6805 import modulo_6805
from module_6806 import power_6806
from module_6807 import min_6807
from module_6808 import max_6808

def test_modulo_6805():
    assert modulo_6805(10, 3) == 1

def test_power_6806():
    assert power_6806(2, 8) == 256

def test_min_6807():
    assert min_6807(3, 7) == 3

def test_max_6808():
    assert max_6808(3, 7) == 7
