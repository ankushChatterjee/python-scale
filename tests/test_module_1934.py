"""Tests for test module 1934 — covers src modules [7733, 7734, 7735, 7736]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7733 import modulo_7733
from module_7734 import power_7734
from module_7735 import min_7735
from module_7736 import max_7736

def test_modulo_7733():
    assert modulo_7733(10, 3) == 1

def test_power_7734():
    assert power_7734(2, 8) == 256

def test_min_7735():
    assert min_7735(3, 7) == 3

def test_max_7736():
    assert max_7736(3, 7) == 7
