"""Tests for test module 2336 — covers src modules [9341, 9342, 9343, 9344]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9341 import modulo_9341
from module_9342 import power_9342
from module_9343 import min_9343
from module_9344 import max_9344

def test_modulo_9341():
    assert modulo_9341(10, 3) == 1

def test_power_9342():
    assert power_9342(2, 8) == 256

def test_min_9343():
    assert min_9343(3, 7) == 3

def test_max_9344():
    assert max_9344(3, 7) == 7
