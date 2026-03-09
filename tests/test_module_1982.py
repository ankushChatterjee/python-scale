"""Tests for test module 1982 — covers src modules [7925, 7926, 7927, 7928]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7925 import modulo_7925
from module_7926 import power_7926
from module_7927 import min_7927
from module_7928 import max_7928

def test_modulo_7925():
    assert modulo_7925(10, 3) == 1

def test_power_7926():
    assert power_7926(2, 8) == 256

def test_min_7927():
    assert min_7927(3, 7) == 3

def test_max_7928():
    assert max_7928(3, 7) == 7
