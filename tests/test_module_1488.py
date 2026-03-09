"""Tests for test module 1488 — covers src modules [5949, 5950, 5951, 5952]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5949 import modulo_5949
from module_5950 import power_5950
from module_5951 import min_5951
from module_5952 import max_5952

def test_modulo_5949():
    assert modulo_5949(10, 3) == 1

def test_power_5950():
    assert power_5950(2, 8) == 256

def test_min_5951():
    assert min_5951(3, 7) == 3

def test_max_5952():
    assert max_5952(3, 7) == 7
