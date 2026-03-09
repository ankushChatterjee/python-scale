"""Tests for test module 624 — covers src modules [2493, 2494, 2495, 2496]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2493 import modulo_2493
from module_2494 import power_2494
from module_2495 import min_2495
from module_2496 import max_2496

def test_modulo_2493():
    assert modulo_2493(10, 3) == 1

def test_power_2494():
    assert power_2494(2, 8) == 256

def test_min_2495():
    assert min_2495(3, 7) == 3

def test_max_2496():
    assert max_2496(3, 7) == 7
