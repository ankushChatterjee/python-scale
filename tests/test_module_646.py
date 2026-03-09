"""Tests for test module 646 — covers src modules [2581, 2582, 2583, 2584]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2581 import modulo_2581
from module_2582 import power_2582
from module_2583 import min_2583
from module_2584 import max_2584

def test_modulo_2581():
    assert modulo_2581(10, 3) == 1

def test_power_2582():
    assert power_2582(2, 8) == 256

def test_min_2583():
    assert min_2583(3, 7) == 3

def test_max_2584():
    assert max_2584(3, 7) == 7
