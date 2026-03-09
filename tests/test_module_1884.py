"""Tests for test module 1884 — covers src modules [7533, 7534, 7535, 7536]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7533 import modulo_7533
from module_7534 import power_7534
from module_7535 import min_7535
from module_7536 import max_7536

def test_modulo_7533():
    assert modulo_7533(10, 3) == 1

def test_power_7534():
    assert power_7534(2, 8) == 256

def test_min_7535():
    assert min_7535(3, 7) == 3

def test_max_7536():
    assert max_7536(3, 7) == 7
