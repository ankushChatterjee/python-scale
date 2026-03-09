"""Tests for test module 2426 — covers src modules [9701, 9702, 9703, 9704]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9701 import modulo_9701
from module_9702 import power_9702
from module_9703 import min_9703
from module_9704 import max_9704

def test_modulo_9701():
    assert modulo_9701(10, 3) == 1

def test_power_9702():
    assert power_9702(2, 8) == 256

def test_min_9703():
    assert min_9703(3, 7) == 3

def test_max_9704():
    assert max_9704(3, 7) == 7
