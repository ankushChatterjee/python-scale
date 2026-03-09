"""Tests for test module 2460 — covers src modules [9837, 9838, 9839, 9840]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9837 import modulo_9837
from module_9838 import power_9838
from module_9839 import min_9839
from module_9840 import max_9840

def test_modulo_9837():
    assert modulo_9837(10, 3) == 1

def test_power_9838():
    assert power_9838(2, 8) == 256

def test_min_9839():
    assert min_9839(3, 7) == 3

def test_max_9840():
    assert max_9840(3, 7) == 7
