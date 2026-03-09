"""Tests for test module 610 — covers src modules [2437, 2438, 2439, 2440]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2437 import modulo_2437
from module_2438 import power_2438
from module_2439 import min_2439
from module_2440 import max_2440

def test_modulo_2437():
    assert modulo_2437(10, 3) == 1

def test_power_2438():
    assert power_2438(2, 8) == 256

def test_min_2439():
    assert min_2439(3, 7) == 3

def test_max_2440():
    assert max_2440(3, 7) == 7
