"""Tests for test module 1746 — covers src modules [6981, 6982, 6983, 6984]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6981 import modulo_6981
from module_6982 import power_6982
from module_6983 import min_6983
from module_6984 import max_6984

def test_modulo_6981():
    assert modulo_6981(10, 3) == 1

def test_power_6982():
    assert power_6982(2, 8) == 256

def test_min_6983():
    assert min_6983(3, 7) == 3

def test_max_6984():
    assert max_6984(3, 7) == 7
