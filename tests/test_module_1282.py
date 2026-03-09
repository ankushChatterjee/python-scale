"""Tests for test module 1282 — covers src modules [5125, 5126, 5127, 5128]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5125 import modulo_5125
from module_5126 import power_5126
from module_5127 import min_5127
from module_5128 import max_5128

def test_modulo_5125():
    assert modulo_5125(10, 3) == 1

def test_power_5126():
    assert power_5126(2, 8) == 256

def test_min_5127():
    assert min_5127(3, 7) == 3

def test_max_5128():
    assert max_5128(3, 7) == 7
