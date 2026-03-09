"""Tests for test module 1532 — covers src modules [6125, 6126, 6127, 6128]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6125 import modulo_6125
from module_6126 import power_6126
from module_6127 import min_6127
from module_6128 import max_6128

def test_modulo_6125():
    assert modulo_6125(10, 3) == 1

def test_power_6126():
    assert power_6126(2, 8) == 256

def test_min_6127():
    assert min_6127(3, 7) == 3

def test_max_6128():
    assert max_6128(3, 7) == 7
