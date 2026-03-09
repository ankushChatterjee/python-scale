"""Tests for test module 1972 — covers src modules [7885, 7886, 7887, 7888]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7885 import modulo_7885
from module_7886 import power_7886
from module_7887 import min_7887
from module_7888 import max_7888

def test_modulo_7885():
    assert modulo_7885(10, 3) == 1

def test_power_7886():
    assert power_7886(2, 8) == 256

def test_min_7887():
    assert min_7887(3, 7) == 3

def test_max_7888():
    assert max_7888(3, 7) == 7
