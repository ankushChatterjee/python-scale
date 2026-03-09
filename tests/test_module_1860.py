"""Tests for test module 1860 — covers src modules [7437, 7438, 7439, 7440]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7437 import modulo_7437
from module_7438 import power_7438
from module_7439 import min_7439
from module_7440 import max_7440

def test_modulo_7437():
    assert modulo_7437(10, 3) == 1

def test_power_7438():
    assert power_7438(2, 8) == 256

def test_min_7439():
    assert min_7439(3, 7) == 3

def test_max_7440():
    assert max_7440(3, 7) == 7
