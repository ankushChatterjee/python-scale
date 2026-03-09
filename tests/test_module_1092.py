"""Tests for test module 1092 — covers src modules [4365, 4366, 4367, 4368]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4365 import modulo_4365
from module_4366 import power_4366
from module_4367 import min_4367
from module_4368 import max_4368

def test_modulo_4365():
    assert modulo_4365(10, 3) == 1

def test_power_4366():
    assert power_4366(2, 8) == 256

def test_min_4367():
    assert min_4367(3, 7) == 3

def test_max_4368():
    assert max_4368(3, 7) == 7
