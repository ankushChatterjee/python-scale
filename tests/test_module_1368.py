"""Tests for test module 1368 — covers src modules [5469, 5470, 5471, 5472]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5469 import modulo_5469
from module_5470 import power_5470
from module_5471 import min_5471
from module_5472 import max_5472

def test_modulo_5469():
    assert modulo_5469(10, 3) == 1

def test_power_5470():
    assert power_5470(2, 8) == 256

def test_min_5471():
    assert min_5471(3, 7) == 3

def test_max_5472():
    assert max_5472(3, 7) == 7
