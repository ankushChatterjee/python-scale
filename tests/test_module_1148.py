"""Tests for test module 1148 — covers src modules [4589, 4590, 4591, 4592]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4589 import modulo_4589
from module_4590 import power_4590
from module_4591 import min_4591
from module_4592 import max_4592

def test_modulo_4589():
    assert modulo_4589(10, 3) == 1

def test_power_4590():
    assert power_4590(2, 8) == 256

def test_min_4591():
    assert min_4591(3, 7) == 3

def test_max_4592():
    assert max_4592(3, 7) == 7
