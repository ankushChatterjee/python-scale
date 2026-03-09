"""Tests for test module 916 — covers src modules [3661, 3662, 3663, 3664]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3661 import modulo_3661
from module_3662 import power_3662
from module_3663 import min_3663
from module_3664 import max_3664

def test_modulo_3661():
    assert modulo_3661(10, 3) == 1

def test_power_3662():
    assert power_3662(2, 8) == 256

def test_min_3663():
    assert min_3663(3, 7) == 3

def test_max_3664():
    assert max_3664(3, 7) == 7
