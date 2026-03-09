"""Tests for test module 2282 — covers src modules [9125, 9126, 9127, 9128]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9125 import modulo_9125
from module_9126 import power_9126
from module_9127 import min_9127
from module_9128 import max_9128

def test_modulo_9125():
    assert modulo_9125(10, 3) == 1

def test_power_9126():
    assert power_9126(2, 8) == 256

def test_min_9127():
    assert min_9127(3, 7) == 3

def test_max_9128():
    assert max_9128(3, 7) == 7
