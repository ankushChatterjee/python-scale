"""Tests for test module 1602 — covers src modules [6405, 6406, 6407, 6408]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6405 import modulo_6405
from module_6406 import power_6406
from module_6407 import min_6407
from module_6408 import max_6408

def test_modulo_6405():
    assert modulo_6405(10, 3) == 1

def test_power_6406():
    assert power_6406(2, 8) == 256

def test_min_6407():
    assert min_6407(3, 7) == 3

def test_max_6408():
    assert max_6408(3, 7) == 7
