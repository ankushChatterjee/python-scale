"""Tests for test module 1362 — covers src modules [5445, 5446, 5447, 5448]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5445 import modulo_5445
from module_5446 import power_5446
from module_5447 import min_5447
from module_5448 import max_5448

def test_modulo_5445():
    assert modulo_5445(10, 3) == 1

def test_power_5446():
    assert power_5446(2, 8) == 256

def test_min_5447():
    assert min_5447(3, 7) == 3

def test_max_5448():
    assert max_5448(3, 7) == 7
