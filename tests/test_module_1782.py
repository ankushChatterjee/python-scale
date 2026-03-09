"""Tests for test module 1782 — covers src modules [7125, 7126, 7127, 7128]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7125 import modulo_7125
from module_7126 import power_7126
from module_7127 import min_7127
from module_7128 import max_7128

def test_modulo_7125():
    assert modulo_7125(10, 3) == 1

def test_power_7126():
    assert power_7126(2, 8) == 256

def test_min_7127():
    assert min_7127(3, 7) == 3

def test_max_7128():
    assert max_7128(3, 7) == 7
