"""Tests for test module 2232 — covers src modules [8925, 8926, 8927, 8928]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8925 import modulo_8925
from module_8926 import power_8926
from module_8927 import min_8927
from module_8928 import max_8928

def test_modulo_8925():
    assert modulo_8925(10, 3) == 1

def test_power_8926():
    assert power_8926(2, 8) == 256

def test_min_8927():
    assert min_8927(3, 7) == 3

def test_max_8928():
    assert max_8928(3, 7) == 7
