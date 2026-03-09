"""Tests for test module 388 — covers src modules [1549, 1550, 1551, 1552]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1549 import modulo_1549
from module_1550 import power_1550
from module_1551 import min_1551
from module_1552 import max_1552

def test_modulo_1549():
    assert modulo_1549(10, 3) == 1

def test_power_1550():
    assert power_1550(2, 8) == 256

def test_min_1551():
    assert min_1551(3, 7) == 3

def test_max_1552():
    assert max_1552(3, 7) == 7
