"""Tests for test module 1720 — covers src modules [6877, 6878, 6879, 6880]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6877 import modulo_6877
from module_6878 import power_6878
from module_6879 import min_6879
from module_6880 import max_6880

def test_modulo_6877():
    assert modulo_6877(10, 3) == 1

def test_power_6878():
    assert power_6878(2, 8) == 256

def test_min_6879():
    assert min_6879(3, 7) == 3

def test_max_6880():
    assert max_6880(3, 7) == 7
