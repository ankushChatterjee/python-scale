"""Tests for test module 748 — covers src modules [2989, 2990, 2991, 2992]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2989 import modulo_2989
from module_2990 import power_2990
from module_2991 import min_2991
from module_2992 import max_2992

def test_modulo_2989():
    assert modulo_2989(10, 3) == 1

def test_power_2990():
    assert power_2990(2, 8) == 256

def test_min_2991():
    assert min_2991(3, 7) == 3

def test_max_2992():
    assert max_2992(3, 7) == 7
