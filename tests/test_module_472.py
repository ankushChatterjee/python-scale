"""Tests for test module 472 — covers src modules [1885, 1886, 1887, 1888]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1885 import modulo_1885
from module_1886 import power_1886
from module_1887 import min_1887
from module_1888 import max_1888

def test_modulo_1885():
    assert modulo_1885(10, 3) == 1

def test_power_1886():
    assert power_1886(2, 8) == 256

def test_min_1887():
    assert min_1887(3, 7) == 3

def test_max_1888():
    assert max_1888(3, 7) == 7
