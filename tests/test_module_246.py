"""Tests for test module 246 — covers src modules [981, 982, 983, 984]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_981 import modulo_981
from module_982 import power_982
from module_983 import min_983
from module_984 import max_984

def test_modulo_981():
    assert modulo_981(10, 3) == 1

def test_power_982():
    assert power_982(2, 8) == 256

def test_min_983():
    assert min_983(3, 7) == 3

def test_max_984():
    assert max_984(3, 7) == 7
