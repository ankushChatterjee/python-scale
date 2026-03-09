"""Tests for test module 2494 — covers src modules [9973, 9974, 9975, 9976]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9973 import modulo_9973
from module_9974 import power_9974
from module_9975 import min_9975
from module_9976 import max_9976

def test_modulo_9973():
    assert modulo_9973(10, 3) == 1

def test_power_9974():
    assert power_9974(2, 8) == 256

def test_min_9975():
    assert min_9975(3, 7) == 3

def test_max_9976():
    assert max_9976(3, 7) == 7
