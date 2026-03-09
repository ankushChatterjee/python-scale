"""Tests for test module 2264 — covers src modules [9053, 9054, 9055, 9056]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9053 import modulo_9053
from module_9054 import power_9054
from module_9055 import min_9055
from module_9056 import max_9056

def test_modulo_9053():
    assert modulo_9053(10, 3) == 1

def test_power_9054():
    assert power_9054(2, 8) == 256

def test_min_9055():
    assert min_9055(3, 7) == 3

def test_max_9056():
    assert max_9056(3, 7) == 7
