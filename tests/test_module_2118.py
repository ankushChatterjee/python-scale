"""Tests for test module 2118 — covers src modules [8469, 8470, 8471, 8472]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8469 import modulo_8469
from module_8470 import power_8470
from module_8471 import min_8471
from module_8472 import max_8472

def test_modulo_8469():
    assert modulo_8469(10, 3) == 1

def test_power_8470():
    assert power_8470(2, 8) == 256

def test_min_8471():
    assert min_8471(3, 7) == 3

def test_max_8472():
    assert max_8472(3, 7) == 7
