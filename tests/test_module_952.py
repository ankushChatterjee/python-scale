"""Tests for test module 952 — covers src modules [3805, 3806, 3807, 3808]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3805 import modulo_3805
from module_3806 import power_3806
from module_3807 import min_3807
from module_3808 import max_3808

def test_modulo_3805():
    assert modulo_3805(10, 3) == 1

def test_power_3806():
    assert power_3806(2, 8) == 256

def test_min_3807():
    assert min_3807(3, 7) == 3

def test_max_3808():
    assert max_3808(3, 7) == 7
