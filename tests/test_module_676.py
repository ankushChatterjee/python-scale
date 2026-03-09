"""Tests for test module 676 — covers src modules [2701, 2702, 2703, 2704]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2701 import modulo_2701
from module_2702 import power_2702
from module_2703 import min_2703
from module_2704 import max_2704

def test_modulo_2701():
    assert modulo_2701(10, 3) == 1

def test_power_2702():
    assert power_2702(2, 8) == 256

def test_min_2703():
    assert min_2703(3, 7) == 3

def test_max_2704():
    assert max_2704(3, 7) == 7
