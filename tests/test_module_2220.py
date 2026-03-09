"""Tests for test module 2220 — covers src modules [8877, 8878, 8879, 8880]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8877 import modulo_8877
from module_8878 import power_8878
from module_8879 import min_8879
from module_8880 import max_8880

def test_modulo_8877():
    assert modulo_8877(10, 3) == 1

def test_power_8878():
    assert power_8878(2, 8) == 256

def test_min_8879():
    assert min_8879(3, 7) == 3

def test_max_8880():
    assert max_8880(3, 7) == 7
