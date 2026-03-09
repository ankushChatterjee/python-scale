"""Tests for test module 2254 — covers src modules [9013, 9014, 9015, 9016]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9013 import modulo_9013
from module_9014 import power_9014
from module_9015 import min_9015
from module_9016 import max_9016

def test_modulo_9013():
    assert modulo_9013(10, 3) == 1

def test_power_9014():
    assert power_9014(2, 8) == 256

def test_min_9015():
    assert min_9015(3, 7) == 3

def test_max_9016():
    assert max_9016(3, 7) == 7
