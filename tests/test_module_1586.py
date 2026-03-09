"""Tests for test module 1586 — covers src modules [6341, 6342, 6343, 6344]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6341 import modulo_6341
from module_6342 import power_6342
from module_6343 import min_6343
from module_6344 import max_6344

def test_modulo_6341():
    assert modulo_6341(10, 3) == 1

def test_power_6342():
    assert power_6342(2, 8) == 256

def test_min_6343():
    assert min_6343(3, 7) == 3

def test_max_6344():
    assert max_6344(3, 7) == 7
