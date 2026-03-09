"""Tests for test module 2396 — covers src modules [9581, 9582, 9583, 9584]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9581 import modulo_9581
from module_9582 import power_9582
from module_9583 import min_9583
from module_9584 import max_9584

def test_modulo_9581():
    assert modulo_9581(10, 3) == 1

def test_power_9582():
    assert power_9582(2, 8) == 256

def test_min_9583():
    assert min_9583(3, 7) == 3

def test_max_9584():
    assert max_9584(3, 7) == 7
