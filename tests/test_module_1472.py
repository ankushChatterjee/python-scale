"""Tests for test module 1472 — covers src modules [5885, 5886, 5887, 5888]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5885 import modulo_5885
from module_5886 import power_5886
from module_5887 import min_5887
from module_5888 import max_5888

def test_modulo_5885():
    assert modulo_5885(10, 3) == 1

def test_power_5886():
    assert power_5886(2, 8) == 256

def test_min_5887():
    assert min_5887(3, 7) == 3

def test_max_5888():
    assert max_5888(3, 7) == 7
