"""Tests for test module 1384 — covers src modules [5533, 5534, 5535, 5536]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5533 import modulo_5533
from module_5534 import power_5534
from module_5535 import min_5535
from module_5536 import max_5536

def test_modulo_5533():
    assert modulo_5533(10, 3) == 1

def test_power_5534():
    assert power_5534(2, 8) == 256

def test_min_5535():
    assert min_5535(3, 7) == 3

def test_max_5536():
    assert max_5536(3, 7) == 7
