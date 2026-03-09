"""Tests for test module 1996 — covers src modules [7981, 7982, 7983, 7984]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7981 import modulo_7981
from module_7982 import power_7982
from module_7983 import min_7983
from module_7984 import max_7984

def test_modulo_7981():
    assert modulo_7981(10, 3) == 1

def test_power_7982():
    assert power_7982(2, 8) == 256

def test_min_7983():
    assert min_7983(3, 7) == 3

def test_max_7984():
    assert max_7984(3, 7) == 7
