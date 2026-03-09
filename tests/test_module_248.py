"""Tests for test module 248 — covers src modules [989, 990, 991, 992]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_989 import modulo_989
from module_990 import power_990
from module_991 import min_991
from module_992 import max_992

def test_modulo_989():
    assert modulo_989(10, 3) == 1

def test_power_990():
    assert power_990(2, 8) == 256

def test_min_991():
    assert min_991(3, 7) == 3

def test_max_992():
    assert max_992(3, 7) == 7
