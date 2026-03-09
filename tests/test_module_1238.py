"""Tests for test module 1238 — covers src modules [4949, 4950, 4951, 4952]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4949 import modulo_4949
from module_4950 import power_4950
from module_4951 import min_4951
from module_4952 import max_4952

def test_modulo_4949():
    assert modulo_4949(10, 3) == 1

def test_power_4950():
    assert power_4950(2, 8) == 256

def test_min_4951():
    assert min_4951(3, 7) == 3

def test_max_4952():
    assert max_4952(3, 7) == 7
