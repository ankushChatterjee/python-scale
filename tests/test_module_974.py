"""Tests for test module 974 — covers src modules [3893, 3894, 3895, 3896]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3893 import modulo_3893
from module_3894 import power_3894
from module_3895 import min_3895
from module_3896 import max_3896

def test_modulo_3893():
    assert modulo_3893(10, 3) == 1

def test_power_3894():
    assert power_3894(2, 8) == 256

def test_min_3895():
    assert min_3895(3, 7) == 3

def test_max_3896():
    assert max_3896(3, 7) == 7
