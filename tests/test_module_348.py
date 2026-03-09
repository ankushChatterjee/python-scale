"""Tests for test module 348 — covers src modules [1389, 1390, 1391, 1392]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1389 import modulo_1389
from module_1390 import power_1390
from module_1391 import min_1391
from module_1392 import max_1392

def test_modulo_1389():
    assert modulo_1389(10, 3) == 1

def test_power_1390():
    assert power_1390(2, 8) == 256

def test_min_1391():
    assert min_1391(3, 7) == 3

def test_max_1392():
    assert max_1392(3, 7) == 7
