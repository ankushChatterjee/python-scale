"""Tests for test module 664 — covers src modules [2653, 2654, 2655, 2656]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2653 import modulo_2653
from module_2654 import power_2654
from module_2655 import min_2655
from module_2656 import max_2656

def test_modulo_2653():
    assert modulo_2653(10, 3) == 1

def test_power_2654():
    assert power_2654(2, 8) == 256

def test_min_2655():
    assert min_2655(3, 7) == 3

def test_max_2656():
    assert max_2656(3, 7) == 7
