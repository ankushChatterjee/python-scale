"""Tests for test module 1248 — covers src modules [4989, 4990, 4991, 4992]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4989 import modulo_4989
from module_4990 import power_4990
from module_4991 import min_4991
from module_4992 import max_4992

def test_modulo_4989():
    assert modulo_4989(10, 3) == 1

def test_power_4990():
    assert power_4990(2, 8) == 256

def test_min_4991():
    assert min_4991(3, 7) == 3

def test_max_4992():
    assert max_4992(3, 7) == 7
