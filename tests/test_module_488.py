"""Tests for test module 488 — covers src modules [1949, 1950, 1951, 1952]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1949 import modulo_1949
from module_1950 import power_1950
from module_1951 import min_1951
from module_1952 import max_1952

def test_modulo_1949():
    assert modulo_1949(10, 3) == 1

def test_power_1950():
    assert power_1950(2, 8) == 256

def test_min_1951():
    assert min_1951(3, 7) == 3

def test_max_1952():
    assert max_1952(3, 7) == 7
