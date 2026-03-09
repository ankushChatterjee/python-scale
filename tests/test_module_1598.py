"""Tests for test module 1598 — covers src modules [6389, 6390, 6391, 6392]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6389 import modulo_6389
from module_6390 import power_6390
from module_6391 import min_6391
from module_6392 import max_6392

def test_modulo_6389():
    assert modulo_6389(10, 3) == 1

def test_power_6390():
    assert power_6390(2, 8) == 256

def test_min_6391():
    assert min_6391(3, 7) == 3

def test_max_6392():
    assert max_6392(3, 7) == 7
