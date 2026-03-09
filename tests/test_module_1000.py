"""Tests for test module 1000 — covers src modules [3997, 3998, 3999, 4000]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3997 import modulo_3997
from module_3998 import power_3998
from module_3999 import min_3999
from module_4000 import max_4000

def test_modulo_3997():
    assert modulo_3997(10, 3) == 1

def test_power_3998():
    assert power_3998(2, 8) == 256

def test_min_3999():
    assert min_3999(3, 7) == 3

def test_max_4000():
    assert max_4000(3, 7) == 7
