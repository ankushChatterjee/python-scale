"""Tests for test module 2450 — covers src modules [9797, 9798, 9799, 9800]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9797 import modulo_9797
from module_9798 import power_9798
from module_9799 import min_9799
from module_9800 import max_9800

def test_modulo_9797():
    assert modulo_9797(10, 3) == 1

def test_power_9798():
    assert power_9798(2, 8) == 256

def test_min_9799():
    assert min_9799(3, 7) == 3

def test_max_9800():
    assert max_9800(3, 7) == 7
