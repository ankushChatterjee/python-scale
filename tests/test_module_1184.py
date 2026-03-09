"""Tests for test module 1184 — covers src modules [4733, 4734, 4735, 4736]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4733 import modulo_4733
from module_4734 import power_4734
from module_4735 import min_4735
from module_4736 import max_4736

def test_modulo_4733():
    assert modulo_4733(10, 3) == 1

def test_power_4734():
    assert power_4734(2, 8) == 256

def test_min_4735():
    assert min_4735(3, 7) == 3

def test_max_4736():
    assert max_4736(3, 7) == 7
