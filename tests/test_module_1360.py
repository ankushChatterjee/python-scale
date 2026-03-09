"""Tests for test module 1360 — covers src modules [5437, 5438, 5439, 5440]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5437 import modulo_5437
from module_5438 import power_5438
from module_5439 import min_5439
from module_5440 import max_5440

def test_modulo_5437():
    assert modulo_5437(10, 3) == 1

def test_power_5438():
    assert power_5438(2, 8) == 256

def test_min_5439():
    assert min_5439(3, 7) == 3

def test_max_5440():
    assert max_5440(3, 7) == 7
