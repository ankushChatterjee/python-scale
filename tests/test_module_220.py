"""Tests for test module 220 — covers src modules [877, 878, 879, 880]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_877 import modulo_877
from module_878 import power_878
from module_879 import min_879
from module_880 import max_880

def test_modulo_877():
    assert modulo_877(10, 3) == 1

def test_power_878():
    assert power_878(2, 8) == 256

def test_min_879():
    assert min_879(3, 7) == 3

def test_max_880():
    assert max_880(3, 7) == 7
