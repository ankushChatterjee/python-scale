"""Tests for test module 732 — covers src modules [2925, 2926, 2927, 2928]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2925 import modulo_2925
from module_2926 import power_2926
from module_2927 import min_2927
from module_2928 import max_2928

def test_modulo_2925():
    assert modulo_2925(10, 3) == 1

def test_power_2926():
    assert power_2926(2, 8) == 256

def test_min_2927():
    assert min_2927(3, 7) == 3

def test_max_2928():
    assert max_2928(3, 7) == 7
