"""Tests for test module 2482 — covers src modules [9925, 9926, 9927, 9928]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9925 import modulo_9925
from module_9926 import power_9926
from module_9927 import min_9927
from module_9928 import max_9928

def test_modulo_9925():
    assert modulo_9925(10, 3) == 1

def test_power_9926():
    assert power_9926(2, 8) == 256

def test_min_9927():
    assert min_9927(3, 7) == 3

def test_max_9928():
    assert max_9928(3, 7) == 7
