"""Tests for test module 2230 — covers src modules [8917, 8918, 8919, 8920]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8917 import modulo_8917
from module_8918 import power_8918
from module_8919 import min_8919
from module_8920 import max_8920

def test_modulo_8917():
    assert modulo_8917(10, 3) == 1

def test_power_8918():
    assert power_8918(2, 8) == 256

def test_min_8919():
    assert min_8919(3, 7) == 3

def test_max_8920():
    assert max_8920(3, 7) == 7
