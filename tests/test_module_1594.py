"""Tests for test module 1594 — covers src modules [6373, 6374, 6375, 6376]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6373 import modulo_6373
from module_6374 import power_6374
from module_6375 import min_6375
from module_6376 import max_6376

def test_modulo_6373():
    assert modulo_6373(10, 3) == 1

def test_power_6374():
    assert power_6374(2, 8) == 256

def test_min_6375():
    assert min_6375(3, 7) == 3

def test_max_6376():
    assert max_6376(3, 7) == 7
