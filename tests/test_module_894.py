"""Tests for test module 894 — covers src modules [3573, 3574, 3575, 3576]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3573 import modulo_3573
from module_3574 import power_3574
from module_3575 import min_3575
from module_3576 import max_3576

def test_modulo_3573():
    assert modulo_3573(10, 3) == 1

def test_power_3574():
    assert power_3574(2, 8) == 256

def test_min_3575():
    assert min_3575(3, 7) == 3

def test_max_3576():
    assert max_3576(3, 7) == 7
