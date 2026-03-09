"""Tests for test module 2464 — covers src modules [9853, 9854, 9855, 9856]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9853 import modulo_9853
from module_9854 import power_9854
from module_9855 import min_9855
from module_9856 import max_9856

def test_modulo_9853():
    assert modulo_9853(10, 3) == 1

def test_power_9854():
    assert power_9854(2, 8) == 256

def test_min_9855():
    assert min_9855(3, 7) == 3

def test_max_9856():
    assert max_9856(3, 7) == 7
