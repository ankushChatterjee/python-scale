"""Tests for test module 1758 — covers src modules [7029, 7030, 7031, 7032]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7029 import modulo_7029
from module_7030 import power_7030
from module_7031 import min_7031
from module_7032 import max_7032

def test_modulo_7029():
    assert modulo_7029(10, 3) == 1

def test_power_7030():
    assert power_7030(2, 8) == 256

def test_min_7031():
    assert min_7031(3, 7) == 3

def test_max_7032():
    assert max_7032(3, 7) == 7
