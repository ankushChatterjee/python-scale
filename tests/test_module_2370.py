"""Tests for test module 2370 — covers src modules [9477, 9478, 9479, 9480]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9477 import modulo_9477
from module_9478 import power_9478
from module_9479 import min_9479
from module_9480 import max_9480

def test_modulo_9477():
    assert modulo_9477(10, 3) == 1

def test_power_9478():
    assert power_9478(2, 8) == 256

def test_min_9479():
    assert min_9479(3, 7) == 3

def test_max_9480():
    assert max_9480(3, 7) == 7
