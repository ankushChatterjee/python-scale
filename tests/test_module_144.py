"""Tests for test module 144 — covers src modules [573, 574, 575, 576]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_573 import modulo_573
from module_574 import power_574
from module_575 import min_575
from module_576 import max_576

def test_modulo_573():
    assert modulo_573(10, 3) == 1

def test_power_574():
    assert power_574(2, 8) == 256

def test_min_575():
    assert min_575(3, 7) == 3

def test_max_576():
    assert max_576(3, 7) == 7
