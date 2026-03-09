"""Tests for test module 2110 — covers src modules [8437, 8438, 8439, 8440]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8437 import modulo_8437
from module_8438 import power_8438
from module_8439 import min_8439
from module_8440 import max_8440

def test_modulo_8437():
    assert modulo_8437(10, 3) == 1

def test_power_8438():
    assert power_8438(2, 8) == 256

def test_min_8439():
    assert min_8439(3, 7) == 3

def test_max_8440():
    assert max_8440(3, 7) == 7
