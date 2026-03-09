"""Tests for test module 2452 — covers src modules [9805, 9806, 9807, 9808]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9805 import modulo_9805
from module_9806 import power_9806
from module_9807 import min_9807
from module_9808 import max_9808

def test_modulo_9805():
    assert modulo_9805(10, 3) == 1

def test_power_9806():
    assert power_9806(2, 8) == 256

def test_min_9807():
    assert min_9807(3, 7) == 3

def test_max_9808():
    assert max_9808(3, 7) == 7
