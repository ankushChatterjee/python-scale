"""Tests for test module 1998 — covers src modules [7989, 7990, 7991, 7992]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7989 import modulo_7989
from module_7990 import power_7990
from module_7991 import min_7991
from module_7992 import max_7992

def test_modulo_7989():
    assert modulo_7989(10, 3) == 1

def test_power_7990():
    assert power_7990(2, 8) == 256

def test_min_7991():
    assert min_7991(3, 7) == 3

def test_max_7992():
    assert max_7992(3, 7) == 7
