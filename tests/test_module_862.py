"""Tests for test module 862 — covers src modules [3445, 3446, 3447, 3448]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3445 import modulo_3445
from module_3446 import power_3446
from module_3447 import min_3447
from module_3448 import max_3448

def test_modulo_3445():
    assert modulo_3445(10, 3) == 1

def test_power_3446():
    assert power_3446(2, 8) == 256

def test_min_3447():
    assert min_3447(3, 7) == 3

def test_max_3448():
    assert max_3448(3, 7) == 7
