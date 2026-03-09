"""Tests for test module 352 — covers src modules [1405, 1406, 1407, 1408]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1405 import modulo_1405
from module_1406 import power_1406
from module_1407 import min_1407
from module_1408 import max_1408

def test_modulo_1405():
    assert modulo_1405(10, 3) == 1

def test_power_1406():
    assert power_1406(2, 8) == 256

def test_min_1407():
    assert min_1407(3, 7) == 3

def test_max_1408():
    assert max_1408(3, 7) == 7
