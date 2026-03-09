"""Tests for test module 2144 — covers src modules [8573, 8574, 8575, 8576]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8573 import modulo_8573
from module_8574 import power_8574
from module_8575 import min_8575
from module_8576 import max_8576

def test_modulo_8573():
    assert modulo_8573(10, 3) == 1

def test_power_8574():
    assert power_8574(2, 8) == 256

def test_min_8575():
    assert min_8575(3, 7) == 3

def test_max_8576():
    assert max_8576(3, 7) == 7
