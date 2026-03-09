"""Tests for test module 2366 — covers src modules [9461, 9462, 9463, 9464]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9461 import modulo_9461
from module_9462 import power_9462
from module_9463 import min_9463
from module_9464 import max_9464

def test_modulo_9461():
    assert modulo_9461(10, 3) == 1

def test_power_9462():
    assert power_9462(2, 8) == 256

def test_min_9463():
    assert min_9463(3, 7) == 3

def test_max_9464():
    assert max_9464(3, 7) == 7
