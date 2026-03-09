"""Tests for test module 750 — covers src modules [2997, 2998, 2999, 3000]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2997 import modulo_2997
from module_2998 import power_2998
from module_2999 import min_2999
from module_3000 import max_3000

def test_modulo_2997():
    assert modulo_2997(10, 3) == 1

def test_power_2998():
    assert power_2998(2, 8) == 256

def test_min_2999():
    assert min_2999(3, 7) == 3

def test_max_3000():
    assert max_3000(3, 7) == 7
