"""Tests for test module 532 — covers src modules [2125, 2126, 2127, 2128]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2125 import modulo_2125
from module_2126 import power_2126
from module_2127 import min_2127
from module_2128 import max_2128

def test_modulo_2125():
    assert modulo_2125(10, 3) == 1

def test_power_2126():
    assert power_2126(2, 8) == 256

def test_min_2127():
    assert min_2127(3, 7) == 3

def test_max_2128():
    assert max_2128(3, 7) == 7
