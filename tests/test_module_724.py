"""Tests for test module 724 — covers src modules [2893, 2894, 2895, 2896]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2893 import modulo_2893
from module_2894 import power_2894
from module_2895 import min_2895
from module_2896 import max_2896

def test_modulo_2893():
    assert modulo_2893(10, 3) == 1

def test_power_2894():
    assert power_2894(2, 8) == 256

def test_min_2895():
    assert min_2895(3, 7) == 3

def test_max_2896():
    assert max_2896(3, 7) == 7
