"""Tests for test module 1108 — covers src modules [4429, 4430, 4431, 4432]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4429 import modulo_4429
from module_4430 import power_4430
from module_4431 import min_4431
from module_4432 import max_4432

def test_modulo_4429():
    assert modulo_4429(10, 3) == 1

def test_power_4430():
    assert power_4430(2, 8) == 256

def test_min_4431():
    assert min_4431(3, 7) == 3

def test_max_4432():
    assert max_4432(3, 7) == 7
