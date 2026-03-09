"""Tests for test module 1466 — covers src modules [5861, 5862, 5863, 5864]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5861 import modulo_5861
from module_5862 import power_5862
from module_5863 import min_5863
from module_5864 import max_5864

def test_modulo_5861():
    assert modulo_5861(10, 3) == 1

def test_power_5862():
    assert power_5862(2, 8) == 256

def test_min_5863():
    assert min_5863(3, 7) == 3

def test_max_5864():
    assert max_5864(3, 7) == 7
