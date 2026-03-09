"""Tests for test module 2032 — covers src modules [8125, 8126, 8127, 8128]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8125 import modulo_8125
from module_8126 import power_8126
from module_8127 import min_8127
from module_8128 import max_8128

def test_modulo_8125():
    assert modulo_8125(10, 3) == 1

def test_power_8126():
    assert power_8126(2, 8) == 256

def test_min_8127():
    assert min_8127(3, 7) == 3

def test_max_8128():
    assert max_8128(3, 7) == 7
