"""Tests for test module 1740 — covers src modules [6957, 6958, 6959, 6960]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6957 import modulo_6957
from module_6958 import power_6958
from module_6959 import min_6959
from module_6960 import max_6960

def test_modulo_6957():
    assert modulo_6957(10, 3) == 1

def test_power_6958():
    assert power_6958(2, 8) == 256

def test_min_6959():
    assert min_6959(3, 7) == 3

def test_max_6960():
    assert max_6960(3, 7) == 7
