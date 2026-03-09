"""Tests for test module 1394 — covers src modules [5573, 5574, 5575, 5576]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5573 import modulo_5573
from module_5574 import power_5574
from module_5575 import min_5575
from module_5576 import max_5576

def test_modulo_5573():
    assert modulo_5573(10, 3) == 1

def test_power_5574():
    assert power_5574(2, 8) == 256

def test_min_5575():
    assert min_5575(3, 7) == 3

def test_max_5576():
    assert max_5576(3, 7) == 7
