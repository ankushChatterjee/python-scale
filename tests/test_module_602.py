"""Tests for test module 602 — covers src modules [2405, 2406, 2407, 2408]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2405 import modulo_2405
from module_2406 import power_2406
from module_2407 import min_2407
from module_2408 import max_2408

def test_modulo_2405():
    assert modulo_2405(10, 3) == 1

def test_power_2406():
    assert power_2406(2, 8) == 256

def test_min_2407():
    assert min_2407(3, 7) == 3

def test_max_2408():
    assert max_2408(3, 7) == 7
