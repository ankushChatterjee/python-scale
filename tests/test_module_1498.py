"""Tests for test module 1498 — covers src modules [5989, 5990, 5991, 5992]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5989 import modulo_5989
from module_5990 import power_5990
from module_5991 import min_5991
from module_5992 import max_5992

def test_modulo_5989():
    assert modulo_5989(10, 3) == 1

def test_power_5990():
    assert power_5990(2, 8) == 256

def test_min_5991():
    assert min_5991(3, 7) == 3

def test_max_5992():
    assert max_5992(3, 7) == 7
