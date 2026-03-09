"""Tests for test module 1848 — covers src modules [7389, 7390, 7391, 7392]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7389 import modulo_7389
from module_7390 import power_7390
from module_7391 import min_7391
from module_7392 import max_7392

def test_modulo_7389():
    assert modulo_7389(10, 3) == 1

def test_power_7390():
    assert power_7390(2, 8) == 256

def test_min_7391():
    assert min_7391(3, 7) == 3

def test_max_7392():
    assert max_7392(3, 7) == 7
