"""Tests for module 112."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_112 import power_112, multiply_112, add_112, min_112

def test_power_112():
    assert power_112(2, 8) == 256

def test_multiply_112():
    assert multiply_112(3, 7) == 21

def test_add_112():
    assert add_112(2, 3) == 5

def test_min_112():
    assert min_112(3, 7) == 3
