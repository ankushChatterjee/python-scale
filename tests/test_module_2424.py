"""Tests for test module 2424 — covers src modules [9693, 9694, 9695, 9696]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9693 import modulo_9693
from module_9694 import power_9694
from module_9695 import min_9695
from module_9696 import max_9696

def test_modulo_9693():
    assert modulo_9693(10, 3) == 1

def test_power_9694():
    assert power_9694(2, 8) == 256

def test_min_9695():
    assert min_9695(3, 7) == 3

def test_max_9696():
    assert max_9696(3, 7) == 7
