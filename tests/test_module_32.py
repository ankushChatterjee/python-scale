"""Tests for test module 32 — covers src modules [125, 126, 127, 128]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_125 import modulo_125
from module_126 import power_126
from module_127 import min_127
from module_128 import max_128

def test_modulo_125():
    assert modulo_125(10, 3) == 1

def test_power_126():
    assert power_126(2, 8) == 256

def test_min_127():
    assert min_127(3, 7) == 3

def test_max_128():
    assert max_128(3, 7) == 7
