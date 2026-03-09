"""Tests for test module 1868 — covers src modules [7469, 7470, 7471, 7472]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7469 import modulo_7469
from module_7470 import power_7470
from module_7471 import min_7471
from module_7472 import max_7472

def test_modulo_7469():
    assert modulo_7469(10, 3) == 1

def test_power_7470():
    assert power_7470(2, 8) == 256

def test_min_7471():
    assert min_7471(3, 7) == 3

def test_max_7472():
    assert max_7472(3, 7) == 7
