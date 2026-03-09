"""Tests for test module 842 — covers src modules [3365, 3366, 3367, 3368]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3365 import modulo_3365
from module_3366 import power_3366
from module_3367 import min_3367
from module_3368 import max_3368

def test_modulo_3365():
    assert modulo_3365(10, 3) == 1

def test_power_3366():
    assert power_3366(2, 8) == 256

def test_min_3367():
    assert min_3367(3, 7) == 3

def test_max_3368():
    assert max_3368(3, 7) == 7
