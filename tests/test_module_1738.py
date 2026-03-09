"""Tests for test module 1738 — covers src modules [6949, 6950, 6951, 6952]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6949 import modulo_6949
from module_6950 import power_6950
from module_6951 import min_6951
from module_6952 import max_6952

def test_modulo_6949():
    assert modulo_6949(10, 3) == 1

def test_power_6950():
    assert power_6950(2, 8) == 256

def test_min_6951():
    assert min_6951(3, 7) == 3

def test_max_6952():
    assert max_6952(3, 7) == 7
