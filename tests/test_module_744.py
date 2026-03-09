"""Tests for test module 744 — covers src modules [2973, 2974, 2975, 2976]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2973 import modulo_2973
from module_2974 import power_2974
from module_2975 import min_2975
from module_2976 import max_2976

def test_modulo_2973():
    assert modulo_2973(10, 3) == 1

def test_power_2974():
    assert power_2974(2, 8) == 256

def test_min_2975():
    assert min_2975(3, 7) == 3

def test_max_2976():
    assert max_2976(3, 7) == 7
