"""Tests for test module 1166 — covers src modules [4661, 4662, 4663, 4664]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4661 import modulo_4661
from module_4662 import power_4662
from module_4663 import min_4663
from module_4664 import max_4664

def test_modulo_4661():
    assert modulo_4661(10, 3) == 1

def test_power_4662():
    assert power_4662(2, 8) == 256

def test_min_4663():
    assert min_4663(3, 7) == 3

def test_max_4664():
    assert max_4664(3, 7) == 7
