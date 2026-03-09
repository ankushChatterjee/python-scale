"""Tests for test module 500 — covers src modules [1997, 1998, 1999, 2000]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1997 import modulo_1997
from module_1998 import power_1998
from module_1999 import min_1999
from module_2000 import max_2000

def test_modulo_1997():
    assert modulo_1997(10, 3) == 1

def test_power_1998():
    assert power_1998(2, 8) == 256

def test_min_1999():
    assert min_1999(3, 7) == 3

def test_max_2000():
    assert max_2000(3, 7) == 7
