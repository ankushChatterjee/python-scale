"""Tests for test module 1210 — covers src modules [4837, 4838, 4839, 4840]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4837 import modulo_4837
from module_4838 import power_4838
from module_4839 import min_4839
from module_4840 import max_4840

def test_modulo_4837():
    assert modulo_4837(10, 3) == 1

def test_power_4838():
    assert power_4838(2, 8) == 256

def test_min_4839():
    assert min_4839(3, 7) == 3

def test_max_4840():
    assert max_4840(3, 7) == 7
