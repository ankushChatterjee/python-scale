"""Tests for test module 1372 — covers src modules [5485, 5486, 5487, 5488]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5485 import modulo_5485
from module_5486 import power_5486
from module_5487 import min_5487
from module_5488 import max_5488

def test_modulo_5485():
    assert modulo_5485(10, 3) == 1

def test_power_5486():
    assert power_5486(2, 8) == 256

def test_min_5487():
    assert min_5487(3, 7) == 3

def test_max_5488():
    assert max_5488(3, 7) == 7
