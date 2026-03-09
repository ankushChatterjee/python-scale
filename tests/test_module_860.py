"""Tests for test module 860 — covers src modules [3437, 3438, 3439, 3440]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3437 import modulo_3437
from module_3438 import power_3438
from module_3439 import min_3439
from module_3440 import max_3440

def test_modulo_3437():
    assert modulo_3437(10, 3) == 1

def test_power_3438():
    assert power_3438(2, 8) == 256

def test_min_3439():
    assert min_3439(3, 7) == 3

def test_max_3440():
    assert max_3440(3, 7) == 7
