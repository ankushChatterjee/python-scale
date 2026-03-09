"""Tests for test module 1434 — covers src modules [5733, 5734, 5735, 5736]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5733 import modulo_5733
from module_5734 import power_5734
from module_5735 import min_5735
from module_5736 import max_5736

def test_modulo_5733():
    assert modulo_5733(10, 3) == 1

def test_power_5734():
    assert power_5734(2, 8) == 256

def test_min_5735():
    assert min_5735(3, 7) == 3

def test_max_5736():
    assert max_5736(3, 7) == 7
