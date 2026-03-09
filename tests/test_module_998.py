"""Tests for test module 998 — covers src modules [3989, 3990, 3991, 3992]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3989 import modulo_3989
from module_3990 import power_3990
from module_3991 import min_3991
from module_3992 import max_3992

def test_modulo_3989():
    assert modulo_3989(10, 3) == 1

def test_power_3990():
    assert power_3990(2, 8) == 256

def test_min_3991():
    assert min_3991(3, 7) == 3

def test_max_3992():
    assert max_3992(3, 7) == 7
