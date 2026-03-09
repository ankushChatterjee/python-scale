"""Tests for test module 2248 — covers src modules [8989, 8990, 8991, 8992]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8989 import modulo_8989
from module_8990 import power_8990
from module_8991 import min_8991
from module_8992 import max_8992

def test_modulo_8989():
    assert modulo_8989(10, 3) == 1

def test_power_8990():
    assert power_8990(2, 8) == 256

def test_min_8991():
    assert min_8991(3, 7) == 3

def test_max_8992():
    assert max_8992(3, 7) == 7
