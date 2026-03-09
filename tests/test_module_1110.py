"""Tests for test module 1110 — covers src modules [4437, 4438, 4439, 4440]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4437 import modulo_4437
from module_4438 import power_4438
from module_4439 import min_4439
from module_4440 import max_4440

def test_modulo_4437():
    assert modulo_4437(10, 3) == 1

def test_power_4438():
    assert power_4438(2, 8) == 256

def test_min_4439():
    assert min_4439(3, 7) == 3

def test_max_4440():
    assert max_4440(3, 7) == 7
