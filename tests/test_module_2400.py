"""Tests for test module 2400 — covers src modules [9597, 9598, 9599, 9600]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9597 import modulo_9597
from module_9598 import power_9598
from module_9599 import min_9599
from module_9600 import max_9600

def test_modulo_9597():
    assert modulo_9597(10, 3) == 1

def test_power_9598():
    assert power_9598(2, 8) == 256

def test_min_9599():
    assert min_9599(3, 7) == 3

def test_max_9600():
    assert max_9600(3, 7) == 7
