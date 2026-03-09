"""Tests for test module 704 — covers src modules [2813, 2814, 2815, 2816]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2813 import modulo_2813
from module_2814 import power_2814
from module_2815 import min_2815
from module_2816 import max_2816

def test_modulo_2813():
    assert modulo_2813(10, 3) == 1

def test_power_2814():
    assert power_2814(2, 8) == 256

def test_min_2815():
    assert min_2815(3, 7) == 3

def test_max_2816():
    assert max_2816(3, 7) == 7
