"""Tests for test module 1748 — covers src modules [6989, 6990, 6991, 6992]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6989 import modulo_6989
from module_6990 import power_6990
from module_6991 import min_6991
from module_6992 import max_6992

def test_modulo_6989():
    assert modulo_6989(10, 3) == 1

def test_power_6990():
    assert power_6990(2, 8) == 256

def test_min_6991():
    assert min_6991(3, 7) == 3

def test_max_6992():
    assert max_6992(3, 7) == 7
