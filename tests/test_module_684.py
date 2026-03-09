"""Tests for test module 684 — covers src modules [2733, 2734, 2735, 2736]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2733 import modulo_2733
from module_2734 import power_2734
from module_2735 import min_2735
from module_2736 import max_2736

def test_modulo_2733():
    assert modulo_2733(10, 3) == 1

def test_power_2734():
    assert power_2734(2, 8) == 256

def test_min_2735():
    assert min_2735(3, 7) == 3

def test_max_2736():
    assert max_2736(3, 7) == 7
