"""Tests for test module 176 — covers src modules [701, 702, 703, 704]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_701 import modulo_701
from module_702 import power_702
from module_703 import min_703
from module_704 import max_704

def test_modulo_701():
    assert modulo_701(10, 3) == 1

def test_power_702():
    assert power_702(2, 8) == 256

def test_min_703():
    assert min_703(3, 7) == 3

def test_max_704():
    assert max_704(3, 7) == 7
