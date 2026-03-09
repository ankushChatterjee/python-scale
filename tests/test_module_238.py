"""Tests for test module 238 — covers src modules [949, 950, 951, 952]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_949 import modulo_949
from module_950 import power_950
from module_951 import min_951
from module_952 import max_952

def test_modulo_949():
    assert modulo_949(10, 3) == 1

def test_power_950():
    assert power_950(2, 8) == 256

def test_min_951():
    assert min_951(3, 7) == 3

def test_max_952():
    assert max_952(3, 7) == 7
