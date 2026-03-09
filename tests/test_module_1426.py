"""Tests for test module 1426 — covers src modules [5701, 5702, 5703, 5704]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5701 import modulo_5701
from module_5702 import power_5702
from module_5703 import min_5703
from module_5704 import max_5704

def test_modulo_5701():
    assert modulo_5701(10, 3) == 1

def test_power_5702():
    assert power_5702(2, 8) == 256

def test_min_5703():
    assert min_5703(3, 7) == 3

def test_max_5704():
    assert max_5704(3, 7) == 7
