"""Tests for test module 982 — covers src modules [3925, 3926, 3927, 3928]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3925 import modulo_3925
from module_3926 import power_3926
from module_3927 import min_3927
from module_3928 import max_3928

def test_modulo_3925():
    assert modulo_3925(10, 3) == 1

def test_power_3926():
    assert power_3926(2, 8) == 256

def test_min_3927():
    assert min_3927(3, 7) == 3

def test_max_3928():
    assert max_3928(3, 7) == 7
