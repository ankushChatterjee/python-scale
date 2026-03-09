"""Tests for test module 874 — covers src modules [3493, 3494, 3495, 3496]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3493 import modulo_3493
from module_3494 import power_3494
from module_3495 import min_3495
from module_3496 import max_3496

def test_modulo_3493():
    assert modulo_3493(10, 3) == 1

def test_power_3494():
    assert power_3494(2, 8) == 256

def test_min_3495():
    assert min_3495(3, 7) == 3

def test_max_3496():
    assert max_3496(3, 7) == 7
