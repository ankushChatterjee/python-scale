"""Tests for test module 988 — covers src modules [3949, 3950, 3951, 3952]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3949 import modulo_3949
from module_3950 import power_3950
from module_3951 import min_3951
from module_3952 import max_3952

def test_modulo_3949():
    assert modulo_3949(10, 3) == 1

def test_power_3950():
    assert power_3950(2, 8) == 256

def test_min_3951():
    assert min_3951(3, 7) == 3

def test_max_3952():
    assert max_3952(3, 7) == 7
