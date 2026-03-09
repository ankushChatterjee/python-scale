"""Tests for test module 232 — covers src modules [925, 926, 927, 928]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_925 import modulo_925
from module_926 import power_926
from module_927 import min_927
from module_928 import max_928

def test_modulo_925():
    assert modulo_925(10, 3) == 1

def test_power_926():
    assert power_926(2, 8) == 256

def test_min_927():
    assert min_927(3, 7) == 3

def test_max_928():
    assert max_928(3, 7) == 7
