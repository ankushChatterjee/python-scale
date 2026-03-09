"""Tests for test module 2086 — covers src modules [8341, 8342, 8343, 8344]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8341 import modulo_8341
from module_8342 import power_8342
from module_8343 import min_8343
from module_8344 import max_8344

def test_modulo_8341():
    assert modulo_8341(10, 3) == 1

def test_power_8342():
    assert power_8342(2, 8) == 256

def test_min_8343():
    assert min_8343(3, 7) == 3

def test_max_8344():
    assert max_8344(3, 7) == 7
