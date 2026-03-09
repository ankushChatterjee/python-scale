"""Tests for test module 1700 — covers src modules [6797, 6798, 6799, 6800]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6797 import modulo_6797
from module_6798 import power_6798
from module_6799 import min_6799
from module_6800 import max_6800

def test_modulo_6797():
    assert modulo_6797(10, 3) == 1

def test_power_6798():
    assert power_6798(2, 8) == 256

def test_min_6799():
    assert min_6799(3, 7) == 3

def test_max_6800():
    assert max_6800(3, 7) == 7
