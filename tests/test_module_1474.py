"""Tests for test module 1474 — covers src modules [5893, 5894, 5895, 5896]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5893 import modulo_5893
from module_5894 import power_5894
from module_5895 import min_5895
from module_5896 import max_5896

def test_modulo_5893():
    assert modulo_5893(10, 3) == 1

def test_power_5894():
    assert power_5894(2, 8) == 256

def test_min_5895():
    assert min_5895(3, 7) == 3

def test_max_5896():
    assert max_5896(3, 7) == 7
