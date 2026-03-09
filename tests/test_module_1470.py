"""Tests for test module 1470 — covers src modules [5877, 5878, 5879, 5880]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5877 import modulo_5877
from module_5878 import power_5878
from module_5879 import min_5879
from module_5880 import max_5880

def test_modulo_5877():
    assert modulo_5877(10, 3) == 1

def test_power_5878():
    assert power_5878(2, 8) == 256

def test_min_5879():
    assert min_5879(3, 7) == 3

def test_max_5880():
    assert max_5880(3, 7) == 7
