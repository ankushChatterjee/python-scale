"""Tests for test module 2286 — covers src modules [9141, 9142, 9143, 9144]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9141 import modulo_9141
from module_9142 import power_9142
from module_9143 import min_9143
from module_9144 import max_9144

def test_modulo_9141():
    assert modulo_9141(10, 3) == 1

def test_power_9142():
    assert power_9142(2, 8) == 256

def test_min_9143():
    assert min_9143(3, 7) == 3

def test_max_9144():
    assert max_9144(3, 7) == 7
