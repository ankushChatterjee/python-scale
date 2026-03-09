"""Tests for test module 464 — covers src modules [1853, 1854, 1855, 1856]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1853 import modulo_1853
from module_1854 import power_1854
from module_1855 import min_1855
from module_1856 import max_1856

def test_modulo_1853():
    assert modulo_1853(10, 3) == 1

def test_power_1854():
    assert power_1854(2, 8) == 256

def test_min_1855():
    assert min_1855(3, 7) == 3

def test_max_1856():
    assert max_1856(3, 7) == 7
