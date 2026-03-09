"""Tests for test module 134 — covers src modules [533, 534, 535, 536]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_533 import modulo_533
from module_534 import power_534
from module_535 import min_535
from module_536 import max_536

def test_modulo_533():
    assert modulo_533(10, 3) == 1

def test_power_534():
    assert power_534(2, 8) == 256

def test_min_535():
    assert min_535(3, 7) == 3

def test_max_536():
    assert max_536(3, 7) == 7
