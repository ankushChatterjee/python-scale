"""Tests for test module 772 — covers src modules [3085, 3086, 3087, 3088]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3085 import modulo_3085
from module_3086 import power_3086
from module_3087 import min_3087
from module_3088 import max_3088

def test_modulo_3085():
    assert modulo_3085(10, 3) == 1

def test_power_3086():
    assert power_3086(2, 8) == 256

def test_min_3087():
    assert min_3087(3, 7) == 3

def test_max_3088():
    assert max_3088(3, 7) == 7
