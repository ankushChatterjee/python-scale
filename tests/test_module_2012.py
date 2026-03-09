"""Tests for test module 2012 — covers src modules [8045, 8046, 8047, 8048]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8045 import modulo_8045
from module_8046 import power_8046
from module_8047 import min_8047
from module_8048 import max_8048

def test_modulo_8045():
    assert modulo_8045(10, 3) == 1

def test_power_8046():
    assert power_8046(2, 8) == 256

def test_min_8047():
    assert min_8047(3, 7) == 3

def test_max_8048():
    assert max_8048(3, 7) == 7
