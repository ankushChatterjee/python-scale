"""Tests for test module 498 — covers src modules [1989, 1990, 1991, 1992]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1989 import modulo_1989
from module_1990 import power_1990
from module_1991 import min_1991
from module_1992 import max_1992

def test_modulo_1989():
    assert modulo_1989(10, 3) == 1

def test_power_1990():
    assert power_1990(2, 8) == 256

def test_min_1991():
    assert min_1991(3, 7) == 3

def test_max_1992():
    assert max_1992(3, 7) == 7
