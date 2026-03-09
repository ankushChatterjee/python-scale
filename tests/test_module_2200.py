"""Tests for test module 2200 — covers src modules [8797, 8798, 8799, 8800]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8797 import modulo_8797
from module_8798 import power_8798
from module_8799 import min_8799
from module_8800 import max_8800

def test_modulo_8797():
    assert modulo_8797(10, 3) == 1

def test_power_8798():
    assert power_8798(2, 8) == 256

def test_min_8799():
    assert min_8799(3, 7) == 3

def test_max_8800():
    assert max_8800(3, 7) == 7
