"""Tests for test module 960 — covers src modules [3837, 3838, 3839, 3840]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3837 import modulo_3837
from module_3838 import power_3838
from module_3839 import min_3839
from module_3840 import max_3840

def test_modulo_3837():
    assert modulo_3837(10, 3) == 1

def test_power_3838():
    assert power_3838(2, 8) == 256

def test_min_3839():
    assert min_3839(3, 7) == 3

def test_max_3840():
    assert max_3840(3, 7) == 7
