"""Tests for test module 2000 — covers src modules [7997, 7998, 7999, 8000]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7997 import modulo_7997
from module_7998 import power_7998
from module_7999 import min_7999
from module_8000 import max_8000

def test_modulo_7997():
    assert modulo_7997(10, 3) == 1

def test_power_7998():
    assert power_7998(2, 8) == 256

def test_min_7999():
    assert min_7999(3, 7) == 3

def test_max_8000():
    assert max_8000(3, 7) == 7
