"""Tests for test module 118 — covers src modules [469, 470, 471, 472]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_469 import modulo_469
from module_470 import power_470
from module_471 import min_471
from module_472 import max_472

def test_modulo_469():
    assert modulo_469(10, 3) == 1

def test_power_470():
    assert power_470(2, 8) == 256

def test_min_471():
    assert min_471(3, 7) == 3

def test_max_472():
    assert max_472(3, 7) == 7
