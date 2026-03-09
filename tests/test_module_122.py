"""Tests for test module 122 — covers src modules [485, 486, 487, 488]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_485 import modulo_485
from module_486 import power_486
from module_487 import min_487
from module_488 import max_488

def test_modulo_485():
    assert modulo_485(10, 3) == 1

def test_power_486():
    assert power_486(2, 8) == 256

def test_min_487():
    assert min_487(3, 7) == 3

def test_max_488():
    assert max_488(3, 7) == 7
