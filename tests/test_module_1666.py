"""Tests for test module 1666 — covers src modules [6661, 6662, 6663, 6664]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6661 import modulo_6661
from module_6662 import power_6662
from module_6663 import min_6663
from module_6664 import max_6664

def test_modulo_6661():
    assert modulo_6661(10, 3) == 1

def test_power_6662():
    assert power_6662(2, 8) == 256

def test_min_6663():
    assert min_6663(3, 7) == 3

def test_max_6664():
    assert max_6664(3, 7) == 7
