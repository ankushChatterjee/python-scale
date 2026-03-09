"""Tests for test module 1732 — covers src modules [6925, 6926, 6927, 6928]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6925 import modulo_6925
from module_6926 import power_6926
from module_6927 import min_6927
from module_6928 import max_6928

def test_modulo_6925():
    assert modulo_6925(10, 3) == 1

def test_power_6926():
    assert power_6926(2, 8) == 256

def test_min_6927():
    assert min_6927(3, 7) == 3

def test_max_6928():
    assert max_6928(3, 7) == 7
