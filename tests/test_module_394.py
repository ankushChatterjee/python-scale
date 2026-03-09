"""Tests for test module 394 — covers src modules [1573, 1574, 1575, 1576]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1573 import modulo_1573
from module_1574 import power_1574
from module_1575 import min_1575
from module_1576 import max_1576

def test_modulo_1573():
    assert modulo_1573(10, 3) == 1

def test_power_1574():
    assert power_1574(2, 8) == 256

def test_min_1575():
    assert min_1575(3, 7) == 3

def test_max_1576():
    assert max_1576(3, 7) == 7
