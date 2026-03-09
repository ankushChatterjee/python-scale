"""Tests for test module 2222 — covers src modules [8885, 8886, 8887, 8888]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8885 import modulo_8885
from module_8886 import power_8886
from module_8887 import min_8887
from module_8888 import max_8888

def test_modulo_8885():
    assert modulo_8885(10, 3) == 1

def test_power_8886():
    assert power_8886(2, 8) == 256

def test_min_8887():
    assert min_8887(3, 7) == 3

def test_max_8888():
    assert max_8888(3, 7) == 7
