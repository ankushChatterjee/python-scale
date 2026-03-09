"""Tests for test module 620 — covers src modules [2477, 2478, 2479, 2480]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2477 import modulo_2477
from module_2478 import power_2478
from module_2479 import min_2479
from module_2480 import max_2480

def test_modulo_2477():
    assert modulo_2477(10, 3) == 1

def test_power_2478():
    assert power_2478(2, 8) == 256

def test_min_2479():
    assert min_2479(3, 7) == 3

def test_max_2480():
    assert max_2480(3, 7) == 7
