"""Tests for test module 1926 — covers src modules [7701, 7702, 7703, 7704]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7701 import modulo_7701
from module_7702 import power_7702
from module_7703 import min_7703
from module_7704 import max_7704

def test_modulo_7701():
    assert modulo_7701(10, 3) == 1

def test_power_7702():
    assert power_7702(2, 8) == 256

def test_min_7703():
    assert min_7703(3, 7) == 3

def test_max_7704():
    assert max_7704(3, 7) == 7
