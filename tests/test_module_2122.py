"""Tests for test module 2122 — covers src modules [8485, 8486, 8487, 8488]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8485 import modulo_8485
from module_8486 import power_8486
from module_8487 import min_8487
from module_8488 import max_8488

def test_modulo_8485():
    assert modulo_8485(10, 3) == 1

def test_power_8486():
    assert power_8486(2, 8) == 256

def test_min_8487():
    assert min_8487(3, 7) == 3

def test_max_8488():
    assert max_8488(3, 7) == 7
