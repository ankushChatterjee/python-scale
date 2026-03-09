"""Tests for test module 1608 — covers src modules [6429, 6430, 6431, 6432]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6429 import modulo_6429
from module_6430 import power_6430
from module_6431 import min_6431
from module_6432 import max_6432

def test_modulo_6429():
    assert modulo_6429(10, 3) == 1

def test_power_6430():
    assert power_6430(2, 8) == 256

def test_min_6431():
    assert min_6431(3, 7) == 3

def test_max_6432():
    assert max_6432(3, 7) == 7
