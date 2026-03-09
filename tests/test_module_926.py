"""Tests for test module 926 — covers src modules [3701, 3702, 3703, 3704]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3701 import modulo_3701
from module_3702 import power_3702
from module_3703 import min_3703
from module_3704 import max_3704

def test_modulo_3701():
    assert modulo_3701(10, 3) == 1

def test_power_3702():
    assert power_3702(2, 8) == 256

def test_min_3703():
    assert min_3703(3, 7) == 3

def test_max_3704():
    assert max_3704(3, 7) == 7
