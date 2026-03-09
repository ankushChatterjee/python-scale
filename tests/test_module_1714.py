"""Tests for test module 1714 — covers src modules [6853, 6854, 6855, 6856]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6853 import modulo_6853
from module_6854 import power_6854
from module_6855 import min_6855
from module_6856 import max_6856

def test_modulo_6853():
    assert modulo_6853(10, 3) == 1

def test_power_6854():
    assert power_6854(2, 8) == 256

def test_min_6855():
    assert min_6855(3, 7) == 3

def test_max_6856():
    assert max_6856(3, 7) == 7
