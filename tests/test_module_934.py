"""Tests for test module 934 — covers src modules [3733, 3734, 3735, 3736]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3733 import modulo_3733
from module_3734 import power_3734
from module_3735 import min_3735
from module_3736 import max_3736

def test_modulo_3733():
    assert modulo_3733(10, 3) == 1

def test_power_3734():
    assert power_3734(2, 8) == 256

def test_min_3735():
    assert min_3735(3, 7) == 3

def test_max_3736():
    assert max_3736(3, 7) == 7
