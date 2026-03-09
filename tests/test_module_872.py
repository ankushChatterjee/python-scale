"""Tests for test module 872 — covers src modules [3485, 3486, 3487, 3488]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3485 import modulo_3485
from module_3486 import power_3486
from module_3487 import min_3487
from module_3488 import max_3488

def test_modulo_3485():
    assert modulo_3485(10, 3) == 1

def test_power_3486():
    assert power_3486(2, 8) == 256

def test_min_3487():
    assert min_3487(3, 7) == 3

def test_max_3488():
    assert max_3488(3, 7) == 7
