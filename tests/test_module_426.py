"""Tests for test module 426 — covers src modules [1701, 1702, 1703, 1704]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1701 import modulo_1701
from module_1702 import power_1702
from module_1703 import min_1703
from module_1704 import max_1704

def test_modulo_1701():
    assert modulo_1701(10, 3) == 1

def test_power_1702():
    assert power_1702(2, 8) == 256

def test_min_1703():
    assert min_1703(3, 7) == 3

def test_max_1704():
    assert max_1704(3, 7) == 7
