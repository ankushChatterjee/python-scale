"""Tests for test module 1032 — covers src modules [4125, 4126, 4127, 4128]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4125 import modulo_4125
from module_4126 import power_4126
from module_4127 import min_4127
from module_4128 import max_4128

def test_modulo_4125():
    assert modulo_4125(10, 3) == 1

def test_power_4126():
    assert power_4126(2, 8) == 256

def test_min_4127():
    assert min_4127(3, 7) == 3

def test_max_4128():
    assert max_4128(3, 7) == 7
