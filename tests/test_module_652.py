"""Tests for test module 652 — covers src modules [2605, 2606, 2607, 2608]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2605 import modulo_2605
from module_2606 import power_2606
from module_2607 import min_2607
from module_2608 import max_2608

def test_modulo_2605():
    assert modulo_2605(10, 3) == 1

def test_power_2606():
    assert power_2606(2, 8) == 256

def test_min_2607():
    assert min_2607(3, 7) == 3

def test_max_2608():
    assert max_2608(3, 7) == 7
