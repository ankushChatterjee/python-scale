"""Tests for test module 782 — covers src modules [3125, 3126, 3127, 3128]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3125 import modulo_3125
from module_3126 import power_3126
from module_3127 import min_3127
from module_3128 import max_3128

def test_modulo_3125():
    assert modulo_3125(10, 3) == 1

def test_power_3126():
    assert power_3126(2, 8) == 256

def test_min_3127():
    assert min_3127(3, 7) == 3

def test_max_3128():
    assert max_3128(3, 7) == 7
