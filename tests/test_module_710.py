"""Tests for test module 710 — covers src modules [2837, 2838, 2839, 2840]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2837 import modulo_2837
from module_2838 import power_2838
from module_2839 import min_2839
from module_2840 import max_2840

def test_modulo_2837():
    assert modulo_2837(10, 3) == 1

def test_power_2838():
    assert power_2838(2, 8) == 256

def test_min_2839():
    assert min_2839(3, 7) == 3

def test_max_2840():
    assert max_2840(3, 7) == 7
