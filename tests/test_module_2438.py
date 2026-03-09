"""Tests for test module 2438 — covers src modules [9749, 9750, 9751, 9752]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9749 import modulo_9749
from module_9750 import power_9750
from module_9751 import min_9751
from module_9752 import max_9752

def test_modulo_9749():
    assert modulo_9749(10, 3) == 1

def test_power_9750():
    assert power_9750(2, 8) == 256

def test_min_9751():
    assert min_9751(3, 7) == 3

def test_max_9752():
    assert max_9752(3, 7) == 7
