"""Tests for test module 714 — covers src modules [2853, 2854, 2855, 2856]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2853 import modulo_2853
from module_2854 import power_2854
from module_2855 import min_2855
from module_2856 import max_2856

def test_modulo_2853():
    assert modulo_2853(10, 3) == 1

def test_power_2854():
    assert power_2854(2, 8) == 256

def test_min_2855():
    assert min_2855(3, 7) == 3

def test_max_2856():
    assert max_2856(3, 7) == 7
