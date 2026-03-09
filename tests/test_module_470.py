"""Tests for test module 470 — covers src modules [1877, 1878, 1879, 1880]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1877 import modulo_1877
from module_1878 import power_1878
from module_1879 import min_1879
from module_1880 import max_1880

def test_modulo_1877():
    assert modulo_1877(10, 3) == 1

def test_power_1878():
    assert power_1878(2, 8) == 256

def test_min_1879():
    assert min_1879(3, 7) == 3

def test_max_1880():
    assert max_1880(3, 7) == 7
