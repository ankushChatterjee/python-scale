"""Tests for test module 1152 — covers src modules [4605, 4606, 4607, 4608]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4605 import modulo_4605
from module_4606 import power_4606
from module_4607 import min_4607
from module_4608 import max_4608

def test_modulo_4605():
    assert modulo_4605(10, 3) == 1

def test_power_4606():
    assert power_4606(2, 8) == 256

def test_min_4607():
    assert min_4607(3, 7) == 3

def test_max_4608():
    assert max_4608(3, 7) == 7
