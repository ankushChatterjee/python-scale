"""Tests for test module 954 — covers src modules [3813, 3814, 3815, 3816]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3813 import modulo_3813
from module_3814 import power_3814
from module_3815 import min_3815
from module_3816 import max_3816

def test_modulo_3813():
    assert modulo_3813(10, 3) == 1

def test_power_3814():
    assert power_3814(2, 8) == 256

def test_min_3815():
    assert min_3815(3, 7) == 3

def test_max_3816():
    assert max_3816(3, 7) == 7
