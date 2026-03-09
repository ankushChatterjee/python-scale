"""Tests for test module 738 — covers src modules [2949, 2950, 2951, 2952]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2949 import modulo_2949
from module_2950 import power_2950
from module_2951 import min_2951
from module_2952 import max_2952

def test_modulo_2949():
    assert modulo_2949(10, 3) == 1

def test_power_2950():
    assert power_2950(2, 8) == 256

def test_min_2951():
    assert min_2951(3, 7) == 3

def test_max_2952():
    assert max_2952(3, 7) == 7
