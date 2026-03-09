"""Tests for test module 222 — covers src modules [885, 886, 887, 888]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_885 import modulo_885
from module_886 import power_886
from module_887 import min_887
from module_888 import max_888

def test_modulo_885():
    assert modulo_885(10, 3) == 1

def test_power_886():
    assert power_886(2, 8) == 256

def test_min_887():
    assert min_887(3, 7) == 3

def test_max_888():
    assert max_888(3, 7) == 7
