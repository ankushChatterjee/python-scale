"""Tests for test module 2224 — covers src modules [8893, 8894, 8895, 8896]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8893 import modulo_8893
from module_8894 import power_8894
from module_8895 import min_8895
from module_8896 import max_8896

def test_modulo_8893():
    assert modulo_8893(10, 3) == 1

def test_power_8894():
    assert power_8894(2, 8) == 256

def test_min_8895():
    assert min_8895(3, 7) == 3

def test_max_8896():
    assert max_8896(3, 7) == 7
