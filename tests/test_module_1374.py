"""Tests for test module 1374 — covers src modules [5493, 5494, 5495, 5496]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5493 import modulo_5493
from module_5494 import power_5494
from module_5495 import min_5495
from module_5496 import max_5496

def test_modulo_5493():
    assert modulo_5493(10, 3) == 1

def test_power_5494():
    assert power_5494(2, 8) == 256

def test_min_5495():
    assert min_5495(3, 7) == 3

def test_max_5496():
    assert max_5496(3, 7) == 7
