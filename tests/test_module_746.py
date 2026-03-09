"""Tests for test module 746 — covers src modules [2981, 2982, 2983, 2984]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2981 import modulo_2981
from module_2982 import power_2982
from module_2983 import min_2983
from module_2984 import max_2984

def test_modulo_2981():
    assert modulo_2981(10, 3) == 1

def test_power_2982():
    assert power_2982(2, 8) == 256

def test_min_2983():
    assert min_2983(3, 7) == 3

def test_max_2984():
    assert max_2984(3, 7) == 7
