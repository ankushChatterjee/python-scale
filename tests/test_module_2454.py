"""Tests for test module 2454 — covers src modules [9813, 9814, 9815, 9816]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9813 import modulo_9813
from module_9814 import power_9814
from module_9815 import min_9815
from module_9816 import max_9816

def test_modulo_9813():
    assert modulo_9813(10, 3) == 1

def test_power_9814():
    assert power_9814(2, 8) == 256

def test_min_9815():
    assert min_9815(3, 7) == 3

def test_max_9816():
    assert max_9816(3, 7) == 7
