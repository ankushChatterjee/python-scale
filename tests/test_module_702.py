"""Tests for test module 702 — covers src modules [2805, 2806, 2807, 2808]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2805 import modulo_2805
from module_2806 import power_2806
from module_2807 import min_2807
from module_2808 import max_2808

def test_modulo_2805():
    assert modulo_2805(10, 3) == 1

def test_power_2806():
    assert power_2806(2, 8) == 256

def test_min_2807():
    assert min_2807(3, 7) == 3

def test_max_2808():
    assert max_2808(3, 7) == 7
