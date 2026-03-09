"""Tests for test module 716 — covers src modules [2861, 2862, 2863, 2864]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2861 import modulo_2861
from module_2862 import power_2862
from module_2863 import min_2863
from module_2864 import max_2864

def test_modulo_2861():
    assert modulo_2861(10, 3) == 1

def test_power_2862():
    assert power_2862(2, 8) == 256

def test_min_2863():
    assert min_2863(3, 7) == 3

def test_max_2864():
    assert max_2864(3, 7) == 7
