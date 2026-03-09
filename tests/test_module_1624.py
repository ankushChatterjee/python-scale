"""Tests for test module 1624 — covers src modules [6493, 6494, 6495, 6496]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6493 import modulo_6493
from module_6494 import power_6494
from module_6495 import min_6495
from module_6496 import max_6496

def test_modulo_6493():
    assert modulo_6493(10, 3) == 1

def test_power_6494():
    assert power_6494(2, 8) == 256

def test_min_6495():
    assert min_6495(3, 7) == 3

def test_max_6496():
    assert max_6496(3, 7) == 7
