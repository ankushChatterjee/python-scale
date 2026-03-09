"""Tests for test module 720 — covers src modules [2877, 2878, 2879, 2880]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2877 import modulo_2877
from module_2878 import power_2878
from module_2879 import min_2879
from module_2880 import max_2880

def test_modulo_2877():
    assert modulo_2877(10, 3) == 1

def test_power_2878():
    assert power_2878(2, 8) == 256

def test_min_2879():
    assert min_2879(3, 7) == 3

def test_max_2880():
    assert max_2880(3, 7) == 7
