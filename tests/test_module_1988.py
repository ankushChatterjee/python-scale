"""Tests for test module 1988 — covers src modules [7949, 7950, 7951, 7952]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7949 import modulo_7949
from module_7950 import power_7950
from module_7951 import min_7951
from module_7952 import max_7952

def test_modulo_7949():
    assert modulo_7949(10, 3) == 1

def test_power_7950():
    assert power_7950(2, 8) == 256

def test_min_7951():
    assert min_7951(3, 7) == 3

def test_max_7952():
    assert max_7952(3, 7) == 7
