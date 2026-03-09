"""Tests for test module 1222 — covers src modules [4885, 4886, 4887, 4888]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4885 import modulo_4885
from module_4886 import power_4886
from module_4887 import min_4887
from module_4888 import max_4888

def test_modulo_4885():
    assert modulo_4885(10, 3) == 1

def test_power_4886():
    assert power_4886(2, 8) == 256

def test_min_4887():
    assert min_4887(3, 7) == 3

def test_max_4888():
    assert max_4888(3, 7) == 7
