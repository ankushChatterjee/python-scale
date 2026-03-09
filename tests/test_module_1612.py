"""Tests for test module 1612 — covers src modules [6445, 6446, 6447, 6448]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6445 import modulo_6445
from module_6446 import power_6446
from module_6447 import min_6447
from module_6448 import max_6448

def test_modulo_6445():
    assert modulo_6445(10, 3) == 1

def test_power_6446():
    assert power_6446(2, 8) == 256

def test_min_6447():
    assert min_6447(3, 7) == 3

def test_max_6448():
    assert max_6448(3, 7) == 7
