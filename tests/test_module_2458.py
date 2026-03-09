"""Tests for test module 2458 — covers src modules [9829, 9830, 9831, 9832]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9829 import modulo_9829
from module_9830 import power_9830
from module_9831 import min_9831
from module_9832 import max_9832

def test_modulo_9829():
    assert modulo_9829(10, 3) == 1

def test_power_9830():
    assert power_9830(2, 8) == 256

def test_min_9831():
    assert min_9831(3, 7) == 3

def test_max_9832():
    assert max_9832(3, 7) == 7
