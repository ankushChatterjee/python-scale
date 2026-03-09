"""Tests for test module 204 — covers src modules [813, 814, 815, 816]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_813 import modulo_813
from module_814 import power_814
from module_815 import min_815
from module_816 import max_816

def test_modulo_813():
    assert modulo_813(10, 3) == 1

def test_power_814():
    assert power_814(2, 8) == 256

def test_min_815():
    assert min_815(3, 7) == 3

def test_max_816():
    assert max_816(3, 7) == 7
