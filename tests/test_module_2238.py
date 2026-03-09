"""Tests for test module 2238 — covers src modules [8949, 8950, 8951, 8952]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8949 import modulo_8949
from module_8950 import power_8950
from module_8951 import min_8951
from module_8952 import max_8952

def test_modulo_8949():
    assert modulo_8949(10, 3) == 1

def test_power_8950():
    assert power_8950(2, 8) == 256

def test_min_8951():
    assert min_8951(3, 7) == 3

def test_max_8952():
    assert max_8952(3, 7) == 7
