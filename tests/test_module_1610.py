"""Tests for test module 1610 — covers src modules [6437, 6438, 6439, 6440]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6437 import modulo_6437
from module_6438 import power_6438
from module_6439 import min_6439
from module_6440 import max_6440

def test_modulo_6437():
    assert modulo_6437(10, 3) == 1

def test_power_6438():
    assert power_6438(2, 8) == 256

def test_min_6439():
    assert min_6439(3, 7) == 3

def test_max_6440():
    assert max_6440(3, 7) == 7
