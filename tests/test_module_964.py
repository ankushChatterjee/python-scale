"""Tests for test module 964 — covers src modules [3853, 3854, 3855, 3856]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3853 import modulo_3853
from module_3854 import power_3854
from module_3855 import min_3855
from module_3856 import max_3856

def test_modulo_3853():
    assert modulo_3853(10, 3) == 1

def test_power_3854():
    assert power_3854(2, 8) == 256

def test_min_3855():
    assert min_3855(3, 7) == 3

def test_max_3856():
    assert max_3856(3, 7) == 7
