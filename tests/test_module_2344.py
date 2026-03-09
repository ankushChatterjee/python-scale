"""Tests for test module 2344 — covers src modules [9373, 9374, 9375, 9376]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9373 import modulo_9373
from module_9374 import power_9374
from module_9375 import min_9375
from module_9376 import max_9376

def test_modulo_9373():
    assert modulo_9373(10, 3) == 1

def test_power_9374():
    assert power_9374(2, 8) == 256

def test_min_9375():
    assert min_9375(3, 7) == 3

def test_max_9376():
    assert max_9376(3, 7) == 7
