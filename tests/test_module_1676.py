"""Tests for test module 1676 — covers src modules [6701, 6702, 6703, 6704]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6701 import modulo_6701
from module_6702 import power_6702
from module_6703 import min_6703
from module_6704 import max_6704

def test_modulo_6701():
    assert modulo_6701(10, 3) == 1

def test_power_6702():
    assert power_6702(2, 8) == 256

def test_min_6703():
    assert min_6703(3, 7) == 3

def test_max_6704():
    assert max_6704(3, 7) == 7
