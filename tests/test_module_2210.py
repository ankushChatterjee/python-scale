"""Tests for test module 2210 — covers src modules [8837, 8838, 8839, 8840]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8837 import modulo_8837
from module_8838 import power_8838
from module_8839 import min_8839
from module_8840 import max_8840

def test_modulo_8837():
    assert modulo_8837(10, 3) == 1

def test_power_8838():
    assert power_8838(2, 8) == 256

def test_min_8839():
    assert min_8839(3, 7) == 3

def test_max_8840():
    assert max_8840(3, 7) == 7
