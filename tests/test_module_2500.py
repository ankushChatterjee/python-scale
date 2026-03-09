"""Tests for test module 2500 — covers src modules [9997, 9998, 9999, 10000]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9997 import modulo_9997
from module_9998 import power_9998
from module_9999 import min_9999
from module_10000 import max_10000

def test_modulo_9997():
    assert modulo_9997(10, 3) == 1

def test_power_9998():
    assert power_9998(2, 8) == 256

def test_min_9999():
    assert min_9999(3, 7) == 3

def test_max_10000():
    assert max_10000(3, 7) == 7
