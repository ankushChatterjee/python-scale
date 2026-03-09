"""Tests for test module 214 — covers src modules [853, 854, 855, 856]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_853 import modulo_853
from module_854 import power_854
from module_855 import min_855
from module_856 import max_856

def test_modulo_853():
    assert modulo_853(10, 3) == 1

def test_power_854():
    assert power_854(2, 8) == 256

def test_min_855():
    assert min_855(3, 7) == 3

def test_max_856():
    assert max_856(3, 7) == 7
