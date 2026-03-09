"""Tests for test module 224 — covers src modules [893, 894, 895, 896]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_893 import modulo_893
from module_894 import power_894
from module_895 import min_895
from module_896 import max_896

def test_modulo_893():
    assert modulo_893(10, 3) == 1

def test_power_894():
    assert power_894(2, 8) == 256

def test_min_895():
    assert min_895(3, 7) == 3

def test_max_896():
    assert max_896(3, 7) == 7
