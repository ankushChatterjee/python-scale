"""Tests for test module 450 — covers src modules [1797, 1798, 1799, 1800]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1797 import modulo_1797
from module_1798 import power_1798
from module_1799 import min_1799
from module_1800 import max_1800

def test_modulo_1797():
    assert modulo_1797(10, 3) == 1

def test_power_1798():
    assert power_1798(2, 8) == 256

def test_min_1799():
    assert min_1799(3, 7) == 3

def test_max_1800():
    assert max_1800(3, 7) == 7
