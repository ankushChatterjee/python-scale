"""Tests for test module 700 — covers src modules [2797, 2798, 2799, 2800]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2797 import modulo_2797
from module_2798 import power_2798
from module_2799 import min_2799
from module_2800 import max_2800

def test_modulo_2797():
    assert modulo_2797(10, 3) == 1

def test_power_2798():
    assert power_2798(2, 8) == 256

def test_min_2799():
    assert min_2799(3, 7) == 3

def test_max_2800():
    assert max_2800(3, 7) == 7
