"""Tests for test module 1352 — covers src modules [5405, 5406, 5407, 5408]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5405 import modulo_5405
from module_5406 import power_5406
from module_5407 import min_5407
from module_5408 import max_5408

def test_modulo_5405():
    assert modulo_5405(10, 3) == 1

def test_power_5406():
    assert power_5406(2, 8) == 256

def test_min_5407():
    assert min_5407(3, 7) == 3

def test_max_5408():
    assert max_5408(3, 7) == 7
