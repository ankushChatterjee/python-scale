"""Tests for test module 1872 — covers src modules [7485, 7486, 7487, 7488]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7485 import modulo_7485
from module_7486 import power_7486
from module_7487 import min_7487
from module_7488 import max_7488

def test_modulo_7485():
    assert modulo_7485(10, 3) == 1

def test_power_7486():
    assert power_7486(2, 8) == 256

def test_min_7487():
    assert min_7487(3, 7) == 3

def test_max_7488():
    assert max_7488(3, 7) == 7
