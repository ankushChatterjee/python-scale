"""Tests for test module 452 — covers src modules [1805, 1806, 1807, 1808]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1805 import modulo_1805
from module_1806 import power_1806
from module_1807 import min_1807
from module_1808 import max_1808

def test_modulo_1805():
    assert modulo_1805(10, 3) == 1

def test_power_1806():
    assert power_1806(2, 8) == 256

def test_min_1807():
    assert min_1807(3, 7) == 3

def test_max_1808():
    assert max_1808(3, 7) == 7
