"""Tests for test module 2014 — covers src modules [8053, 8054, 8055, 8056]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8053 import modulo_8053
from module_8054 import power_8054
from module_8055 import min_8055
from module_8056 import max_8056

def test_modulo_8053():
    assert modulo_8053(10, 3) == 1

def test_power_8054():
    assert power_8054(2, 8) == 256

def test_min_8055():
    assert min_8055(3, 7) == 3

def test_max_8056():
    assert max_8056(3, 7) == 7
