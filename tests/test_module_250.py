"""Tests for test module 250 — covers src modules [997, 998, 999, 1000]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_997 import modulo_997
from module_998 import power_998
from module_999 import min_999
from module_1000 import max_1000

def test_modulo_997():
    assert modulo_997(10, 3) == 1

def test_power_998():
    assert power_998(2, 8) == 256

def test_min_999():
    assert min_999(3, 7) == 3

def test_max_1000():
    assert max_1000(3, 7) == 7
