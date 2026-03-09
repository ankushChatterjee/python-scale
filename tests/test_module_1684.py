"""Tests for test module 1684 — covers src modules [6733, 6734, 6735, 6736]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6733 import modulo_6733
from module_6734 import power_6734
from module_6735 import min_6735
from module_6736 import max_6736

def test_modulo_6733():
    assert modulo_6733(10, 3) == 1

def test_power_6734():
    assert power_6734(2, 8) == 256

def test_min_6735():
    assert min_6735(3, 7) == 3

def test_max_6736():
    assert max_6736(3, 7) == 7
