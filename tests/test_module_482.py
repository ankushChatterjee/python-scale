"""Tests for test module 482 — covers src modules [1925, 1926, 1927, 1928]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1925 import modulo_1925
from module_1926 import power_1926
from module_1927 import min_1927
from module_1928 import max_1928

def test_modulo_1925():
    assert modulo_1925(10, 3) == 1

def test_power_1926():
    assert power_1926(2, 8) == 256

def test_min_1927():
    assert min_1927(3, 7) == 3

def test_max_1928():
    assert max_1928(3, 7) == 7
