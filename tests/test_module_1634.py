"""Tests for test module 1634 — covers src modules [6533, 6534, 6535, 6536]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6533 import modulo_6533
from module_6534 import power_6534
from module_6535 import min_6535
from module_6536 import max_6536

def test_modulo_6533():
    assert modulo_6533(10, 3) == 1

def test_power_6534():
    assert power_6534(2, 8) == 256

def test_min_6535():
    assert min_6535(3, 7) == 3

def test_max_6536():
    assert max_6536(3, 7) == 7
