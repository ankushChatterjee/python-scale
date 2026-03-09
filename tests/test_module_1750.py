"""Tests for test module 1750 — covers src modules [6997, 6998, 6999, 7000]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6997 import modulo_6997
from module_6998 import power_6998
from module_6999 import min_6999
from module_7000 import max_7000

def test_modulo_6997():
    assert modulo_6997(10, 3) == 1

def test_power_6998():
    assert power_6998(2, 8) == 256

def test_min_6999():
    assert min_6999(3, 7) == 3

def test_max_7000():
    assert max_7000(3, 7) == 7
