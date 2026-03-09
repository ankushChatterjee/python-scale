"""Tests for test module 2256 — covers src modules [9021, 9022, 9023, 9024]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9021 import modulo_9021
from module_9022 import power_9022
from module_9023 import min_9023
from module_9024 import max_9024

def test_modulo_9021():
    assert modulo_9021(10, 3) == 1

def test_power_9022():
    assert power_9022(2, 8) == 256

def test_min_9023():
    assert min_9023(3, 7) == 3

def test_max_9024():
    assert max_9024(3, 7) == 7
