"""Tests for test module 1098 — covers src modules [4389, 4390, 4391, 4392]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4389 import modulo_4389
from module_4390 import power_4390
from module_4391 import min_4391
from module_4392 import max_4392

def test_modulo_4389():
    assert modulo_4389(10, 3) == 1

def test_power_4390():
    assert power_4390(2, 8) == 256

def test_min_4391():
    assert min_4391(3, 7) == 3

def test_max_4392():
    assert max_4392(3, 7) == 7
