"""Tests for test module 730 — covers src modules [2917, 2918, 2919, 2920]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2917 import modulo_2917
from module_2918 import power_2918
from module_2919 import min_2919
from module_2920 import max_2920

def test_modulo_2917():
    assert modulo_2917(10, 3) == 1

def test_power_2918():
    assert power_2918(2, 8) == 256

def test_min_2919():
    assert min_2919(3, 7) == 3

def test_max_2920():
    assert max_2920(3, 7) == 7
