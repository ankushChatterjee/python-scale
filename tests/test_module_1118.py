"""Tests for test module 1118 — covers src modules [4469, 4470, 4471, 4472]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4469 import modulo_4469
from module_4470 import power_4470
from module_4471 import min_4471
from module_4472 import max_4472

def test_modulo_4469():
    assert modulo_4469(10, 3) == 1

def test_power_4470():
    assert power_4470(2, 8) == 256

def test_min_4471():
    assert min_4471(3, 7) == 3

def test_max_4472():
    assert max_4472(3, 7) == 7
