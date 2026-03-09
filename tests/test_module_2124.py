"""Tests for test module 2124 — covers src modules [8493, 8494, 8495, 8496]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8493 import modulo_8493
from module_8494 import power_8494
from module_8495 import min_8495
from module_8496 import max_8496

def test_modulo_8493():
    assert modulo_8493(10, 3) == 1

def test_power_8494():
    assert power_8494(2, 8) == 256

def test_min_8495():
    assert min_8495(3, 7) == 3

def test_max_8496():
    assert max_8496(3, 7) == 7
