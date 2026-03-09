"""Tests for test module 460 — covers src modules [1837, 1838, 1839, 1840]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1837 import modulo_1837
from module_1838 import power_1838
from module_1839 import min_1839
from module_1840 import max_1840

def test_modulo_1837():
    assert modulo_1837(10, 3) == 1

def test_power_1838():
    assert power_1838(2, 8) == 256

def test_min_1839():
    assert min_1839(3, 7) == 3

def test_max_1840():
    assert max_1840(3, 7) == 7
