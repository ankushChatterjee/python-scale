"""Tests for test module 166 — covers src modules [661, 662, 663, 664]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_661 import modulo_661
from module_662 import power_662
from module_663 import min_663
from module_664 import max_664

def test_modulo_661():
    assert modulo_661(10, 3) == 1

def test_power_662():
    assert power_662(2, 8) == 256

def test_min_663():
    assert min_663(3, 7) == 3

def test_max_664():
    assert max_664(3, 7) == 7
