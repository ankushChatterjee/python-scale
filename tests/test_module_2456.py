"""Tests for test module 2456 — covers src modules [9821, 9822, 9823, 9824]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9821 import modulo_9821
from module_9822 import power_9822
from module_9823 import min_9823
from module_9824 import max_9824

def test_modulo_9821():
    assert modulo_9821(10, 3) == 1

def test_power_9822():
    assert power_9822(2, 8) == 256

def test_min_9823():
    assert min_9823(3, 7) == 3

def test_max_9824():
    assert max_9824(3, 7) == 7
