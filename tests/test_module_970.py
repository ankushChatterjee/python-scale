"""Tests for test module 970 — covers src modules [3877, 3878, 3879, 3880]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3877 import modulo_3877
from module_3878 import power_3878
from module_3879 import min_3879
from module_3880 import max_3880

def test_modulo_3877():
    assert modulo_3877(10, 3) == 1

def test_power_3878():
    assert power_3878(2, 8) == 256

def test_min_3879():
    assert min_3879(3, 7) == 3

def test_max_3880():
    assert max_3880(3, 7) == 7
