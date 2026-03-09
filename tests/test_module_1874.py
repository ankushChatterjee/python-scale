"""Tests for test module 1874 — covers src modules [7493, 7494, 7495, 7496]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7493 import modulo_7493
from module_7494 import power_7494
from module_7495 import min_7495
from module_7496 import max_7496

def test_modulo_7493():
    assert modulo_7493(10, 3) == 1

def test_power_7494():
    assert power_7494(2, 8) == 256

def test_min_7495():
    assert min_7495(3, 7) == 3

def test_max_7496():
    assert max_7496(3, 7) == 7
