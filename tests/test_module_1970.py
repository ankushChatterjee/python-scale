"""Tests for test module 1970 — covers src modules [7877, 7878, 7879, 7880]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7877 import modulo_7877
from module_7878 import power_7878
from module_7879 import min_7879
from module_7880 import max_7880

def test_modulo_7877():
    assert modulo_7877(10, 3) == 1

def test_power_7878():
    assert power_7878(2, 8) == 256

def test_min_7879():
    assert min_7879(3, 7) == 3

def test_max_7880():
    assert max_7880(3, 7) == 7
