"""Tests for test module 2214 — covers src modules [8853, 8854, 8855, 8856]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8853 import modulo_8853
from module_8854 import power_8854
from module_8855 import min_8855
from module_8856 import max_8856

def test_modulo_8853():
    assert modulo_8853(10, 3) == 1

def test_power_8854():
    assert power_8854(2, 8) == 256

def test_min_8855():
    assert min_8855(3, 7) == 3

def test_max_8856():
    assert max_8856(3, 7) == 7
