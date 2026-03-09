"""Tests for test module 1960 — covers src modules [7837, 7838, 7839, 7840]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7837 import modulo_7837
from module_7838 import power_7838
from module_7839 import min_7839
from module_7840 import max_7840

def test_modulo_7837():
    assert modulo_7837(10, 3) == 1

def test_power_7838():
    assert power_7838(2, 8) == 256

def test_min_7839():
    assert min_7839(3, 7) == 3

def test_max_7840():
    assert max_7840(3, 7) == 7
