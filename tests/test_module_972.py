"""Tests for test module 972 — covers src modules [3885, 3886, 3887, 3888]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3885 import modulo_3885
from module_3886 import power_3886
from module_3887 import min_3887
from module_3888 import max_3888

def test_modulo_3885():
    assert modulo_3885(10, 3) == 1

def test_power_3886():
    assert power_3886(2, 8) == 256

def test_min_3887():
    assert min_3887(3, 7) == 3

def test_max_3888():
    assert max_3888(3, 7) == 7
