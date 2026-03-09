"""Tests for test module 1482 — covers src modules [5925, 5926, 5927, 5928]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5925 import modulo_5925
from module_5926 import power_5926
from module_5927 import min_5927
from module_5928 import max_5928

def test_modulo_5925():
    assert modulo_5925(10, 3) == 1

def test_power_5926():
    assert power_5926(2, 8) == 256

def test_min_5927():
    assert min_5927(3, 7) == 3

def test_max_5928():
    assert max_5928(3, 7) == 7
