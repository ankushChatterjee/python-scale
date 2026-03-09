"""Tests for test module 2184 — covers src modules [8733, 8734, 8735, 8736]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8733 import modulo_8733
from module_8734 import power_8734
from module_8735 import min_8735
from module_8736 import max_8736

def test_modulo_8733():
    assert modulo_8733(10, 3) == 1

def test_power_8734():
    assert power_8734(2, 8) == 256

def test_min_8735():
    assert min_8735(3, 7) == 3

def test_max_8736():
    assert max_8736(3, 7) == 7
