"""Tests for test module 1974 — covers src modules [7893, 7894, 7895, 7896]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7893 import modulo_7893
from module_7894 import power_7894
from module_7895 import min_7895
from module_7896 import max_7896

def test_modulo_7893():
    assert modulo_7893(10, 3) == 1

def test_power_7894():
    assert power_7894(2, 8) == 256

def test_min_7895():
    assert min_7895(3, 7) == 3

def test_max_7896():
    assert max_7896(3, 7) == 7
