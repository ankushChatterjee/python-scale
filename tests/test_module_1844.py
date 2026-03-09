"""Tests for test module 1844 — covers src modules [7373, 7374, 7375, 7376]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7373 import modulo_7373
from module_7374 import power_7374
from module_7375 import min_7375
from module_7376 import max_7376

def test_modulo_7373():
    assert modulo_7373(10, 3) == 1

def test_power_7374():
    assert power_7374(2, 8) == 256

def test_min_7375():
    assert min_7375(3, 7) == 3

def test_max_7376():
    assert max_7376(3, 7) == 7
