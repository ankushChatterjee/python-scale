"""Tests for test module 1204 — covers src modules [4813, 4814, 4815, 4816]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4813 import modulo_4813
from module_4814 import power_4814
from module_4815 import min_4815
from module_4816 import max_4816

def test_modulo_4813():
    assert modulo_4813(10, 3) == 1

def test_power_4814():
    assert power_4814(2, 8) == 256

def test_min_4815():
    assert min_4815(3, 7) == 3

def test_max_4816():
    assert max_4816(3, 7) == 7
