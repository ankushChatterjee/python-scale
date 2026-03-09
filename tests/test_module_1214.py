"""Tests for test module 1214 — covers src modules [4853, 4854, 4855, 4856]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4853 import modulo_4853
from module_4854 import power_4854
from module_4855 import min_4855
from module_4856 import max_4856

def test_modulo_4853():
    assert modulo_4853(10, 3) == 1

def test_power_4854():
    assert power_4854(2, 8) == 256

def test_min_4855():
    assert min_4855(3, 7) == 3

def test_max_4856():
    assert max_4856(3, 7) == 7
