"""Tests for test module 2098 — covers src modules [8389, 8390, 8391, 8392]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8389 import modulo_8389
from module_8390 import power_8390
from module_8391 import min_8391
from module_8392 import max_8392

def test_modulo_8389():
    assert modulo_8389(10, 3) == 1

def test_power_8390():
    assert power_8390(2, 8) == 256

def test_min_8391():
    assert min_8391(3, 7) == 3

def test_max_8392():
    assert max_8392(3, 7) == 7
