"""Tests for test module 1144 — covers src modules [4573, 4574, 4575, 4576]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4573 import modulo_4573
from module_4574 import power_4574
from module_4575 import min_4575
from module_4576 import max_4576

def test_modulo_4573():
    assert modulo_4573(10, 3) == 1

def test_power_4574():
    assert power_4574(2, 8) == 256

def test_min_4575():
    assert min_4575(3, 7) == 3

def test_max_4576():
    assert max_4576(3, 7) == 7
