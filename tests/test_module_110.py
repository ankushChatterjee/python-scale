"""Tests for test module 110 — covers src modules [437, 438, 439, 440]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_437 import modulo_437
from module_438 import power_438
from module_439 import min_439
from module_440 import max_440

def test_modulo_437():
    assert modulo_437(10, 3) == 1

def test_power_438():
    assert power_438(2, 8) == 256

def test_min_439():
    assert min_439(3, 7) == 3

def test_max_440():
    assert max_440(3, 7) == 7
