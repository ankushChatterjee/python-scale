"""Tests for test module 594 — covers src modules [2373, 2374, 2375, 2376]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2373 import modulo_2373
from module_2374 import power_2374
from module_2375 import min_2375
from module_2376 import max_2376

def test_modulo_2373():
    assert modulo_2373(10, 3) == 1

def test_power_2374():
    assert power_2374(2, 8) == 256

def test_min_2375():
    assert min_2375(3, 7) == 3

def test_max_2376():
    assert max_2376(3, 7) == 7
