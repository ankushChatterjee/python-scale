"""Tests for test module 1722 — covers src modules [6885, 6886, 6887, 6888]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6885 import modulo_6885
from module_6886 import power_6886
from module_6887 import min_6887
from module_6888 import max_6888

def test_modulo_6885():
    assert modulo_6885(10, 3) == 1

def test_power_6886():
    assert power_6886(2, 8) == 256

def test_min_6887():
    assert min_6887(3, 7) == 3

def test_max_6888():
    assert max_6888(3, 7) == 7
