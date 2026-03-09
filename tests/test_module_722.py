"""Tests for test module 722 — covers src modules [2885, 2886, 2887, 2888]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2885 import modulo_2885
from module_2886 import power_2886
from module_2887 import min_2887
from module_2888 import max_2888

def test_modulo_2885():
    assert modulo_2885(10, 3) == 1

def test_power_2886():
    assert power_2886(2, 8) == 256

def test_min_2887():
    assert min_2887(3, 7) == 3

def test_max_2888():
    assert max_2888(3, 7) == 7
