"""Tests for test module 2470 — covers src modules [9877, 9878, 9879, 9880]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9877 import modulo_9877
from module_9878 import power_9878
from module_9879 import min_9879
from module_9880 import max_9880

def test_modulo_9877():
    assert modulo_9877(10, 3) == 1

def test_power_9878():
    assert power_9878(2, 8) == 256

def test_min_9879():
    assert min_9879(3, 7) == 3

def test_max_9880():
    assert max_9880(3, 7) == 7
