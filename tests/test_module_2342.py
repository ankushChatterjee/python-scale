"""Tests for test module 2342 — covers src modules [9365, 9366, 9367, 9368]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9365 import modulo_9365
from module_9366 import power_9366
from module_9367 import min_9367
from module_9368 import max_9368

def test_modulo_9365():
    assert modulo_9365(10, 3) == 1

def test_power_9366():
    assert power_9366(2, 8) == 256

def test_min_9367():
    assert min_9367(3, 7) == 3

def test_max_9368():
    assert max_9368(3, 7) == 7
