"""Tests for test module 98 — covers src modules [389, 390, 391, 392]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_389 import modulo_389
from module_390 import power_390
from module_391 import min_391
from module_392 import max_392

def test_modulo_389():
    assert modulo_389(10, 3) == 1

def test_power_390():
    assert power_390(2, 8) == 256

def test_min_391():
    assert min_391(3, 7) == 3

def test_max_392():
    assert max_392(3, 7) == 7
