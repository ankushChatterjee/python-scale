"""Tests for test module 902 — covers src modules [3605, 3606, 3607, 3608]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3605 import modulo_3605
from module_3606 import power_3606
from module_3607 import min_3607
from module_3608 import max_3608

def test_modulo_3605():
    assert modulo_3605(10, 3) == 1

def test_power_3606():
    assert power_3606(2, 8) == 256

def test_min_3607():
    assert min_3607(3, 7) == 3

def test_max_3608():
    assert max_3608(3, 7) == 7
