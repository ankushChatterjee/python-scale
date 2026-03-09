"""Tests for test module 152 — covers src modules [605, 606, 607, 608]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_605 import modulo_605
from module_606 import power_606
from module_607 import min_607
from module_608 import max_608

def test_modulo_605():
    assert modulo_605(10, 3) == 1

def test_power_606():
    assert power_606(2, 8) == 256

def test_min_607():
    assert min_607(3, 7) == 3

def test_max_608():
    assert max_608(3, 7) == 7
