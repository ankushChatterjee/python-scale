"""Tests for test module 1950 — covers src modules [7797, 7798, 7799, 7800]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7797 import modulo_7797
from module_7798 import power_7798
from module_7799 import min_7799
from module_7800 import max_7800

def test_modulo_7797():
    assert modulo_7797(10, 3) == 1

def test_power_7798():
    assert power_7798(2, 8) == 256

def test_min_7799():
    assert min_7799(3, 7) == 3

def test_max_7800():
    assert max_7800(3, 7) == 7
