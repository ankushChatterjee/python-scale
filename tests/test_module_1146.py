"""Tests for test module 1146 — covers src modules [4581, 4582, 4583, 4584]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4581 import modulo_4581
from module_4582 import power_4582
from module_4583 import min_4583
from module_4584 import max_4584

def test_modulo_4581():
    assert modulo_4581(10, 3) == 1

def test_power_4582():
    assert power_4582(2, 8) == 256

def test_min_4583():
    assert min_4583(3, 7) == 3

def test_max_4584():
    assert max_4584(3, 7) == 7
