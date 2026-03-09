"""Tests for test module 1232 — covers src modules [4925, 4926, 4927, 4928]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4925 import modulo_4925
from module_4926 import power_4926
from module_4927 import min_4927
from module_4928 import max_4928

def test_modulo_4925():
    assert modulo_4925(10, 3) == 1

def test_power_4926():
    assert power_4926(2, 8) == 256

def test_min_4927():
    assert min_4927(3, 7) == 3

def test_max_4928():
    assert max_4928(3, 7) == 7
