"""Tests for test module 2434 — covers src modules [9733, 9734, 9735, 9736]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9733 import modulo_9733
from module_9734 import power_9734
from module_9735 import min_9735
from module_9736 import max_9736

def test_modulo_9733():
    assert modulo_9733(10, 3) == 1

def test_power_9734():
    assert power_9734(2, 8) == 256

def test_min_9735():
    assert min_9735(3, 7) == 3

def test_max_9736():
    assert max_9736(3, 7) == 7
