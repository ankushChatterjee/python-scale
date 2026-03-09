"""Tests for test module 2372 — covers src modules [9485, 9486, 9487, 9488]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9485 import modulo_9485
from module_9486 import power_9486
from module_9487 import min_9487
from module_9488 import max_9488

def test_modulo_9485():
    assert modulo_9485(10, 3) == 1

def test_power_9486():
    assert power_9486(2, 8) == 256

def test_min_9487():
    assert min_9487(3, 7) == 3

def test_max_9488():
    assert max_9488(3, 7) == 7
