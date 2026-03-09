"""Tests for test module 1500 — covers src modules [5997, 5998, 5999, 6000]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5997 import modulo_5997
from module_5998 import power_5998
from module_5999 import min_5999
from module_6000 import max_6000

def test_modulo_5997():
    assert modulo_5997(10, 3) == 1

def test_power_5998():
    assert power_5998(2, 8) == 256

def test_min_5999():
    assert min_5999(3, 7) == 3

def test_max_6000():
    assert max_6000(3, 7) == 7
