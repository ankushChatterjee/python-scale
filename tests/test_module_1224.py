"""Tests for test module 1224 — covers src modules [4893, 4894, 4895, 4896]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4893 import modulo_4893
from module_4894 import power_4894
from module_4895 import min_4895
from module_4896 import max_4896

def test_modulo_4893():
    assert modulo_4893(10, 3) == 1

def test_power_4894():
    assert power_4894(2, 8) == 256

def test_min_4895():
    assert min_4895(3, 7) == 3

def test_max_4896():
    assert max_4896(3, 7) == 7
