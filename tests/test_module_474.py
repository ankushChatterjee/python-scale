"""Tests for test module 474 — covers src modules [1893, 1894, 1895, 1896]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1893 import modulo_1893
from module_1894 import power_1894
from module_1895 import min_1895
from module_1896 import max_1896

def test_modulo_1893():
    assert modulo_1893(10, 3) == 1

def test_power_1894():
    assert power_1894(2, 8) == 256

def test_min_1895():
    assert min_1895(3, 7) == 3

def test_max_1896():
    assert max_1896(3, 7) == 7
