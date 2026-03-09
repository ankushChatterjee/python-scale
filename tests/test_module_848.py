"""Tests for test module 848 — covers src modules [3389, 3390, 3391, 3392]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3389 import modulo_3389
from module_3390 import power_3390
from module_3391 import min_3391
from module_3392 import max_3392

def test_modulo_3389():
    assert modulo_3389(10, 3) == 1

def test_power_3390():
    assert power_3390(2, 8) == 256

def test_min_3391():
    assert min_3391(3, 7) == 3

def test_max_3392():
    assert max_3392(3, 7) == 7
