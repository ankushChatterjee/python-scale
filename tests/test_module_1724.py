"""Tests for test module 1724 — covers src modules [6893, 6894, 6895, 6896]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6893 import modulo_6893
from module_6894 import power_6894
from module_6895 import min_6895
from module_6896 import max_6896

def test_modulo_6893():
    assert modulo_6893(10, 3) == 1

def test_power_6894():
    assert power_6894(2, 8) == 256

def test_min_6895():
    assert min_6895(3, 7) == 3

def test_max_6896():
    assert max_6896(3, 7) == 7
