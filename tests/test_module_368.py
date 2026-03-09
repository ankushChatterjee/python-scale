"""Tests for test module 368 — covers src modules [1469, 1470, 1471, 1472]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1469 import modulo_1469
from module_1470 import power_1470
from module_1471 import min_1471
from module_1472 import max_1472

def test_modulo_1469():
    assert modulo_1469(10, 3) == 1

def test_power_1470():
    assert power_1470(2, 8) == 256

def test_min_1471():
    assert min_1471(3, 7) == 3

def test_max_1472():
    assert max_1472(3, 7) == 7
