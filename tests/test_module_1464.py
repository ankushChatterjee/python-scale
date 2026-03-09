"""Tests for test module 1464 — covers src modules [5853, 5854, 5855, 5856]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5853 import modulo_5853
from module_5854 import power_5854
from module_5855 import min_5855
from module_5856 import max_5856

def test_modulo_5853():
    assert modulo_5853(10, 3) == 1

def test_power_5854():
    assert power_5854(2, 8) == 256

def test_min_5855():
    assert min_5855(3, 7) == 3

def test_max_5856():
    assert max_5856(3, 7) == 7
