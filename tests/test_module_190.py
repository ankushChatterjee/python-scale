"""Tests for module 190."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_190 import power_190, min_190, multiply_190, max_190

def test_power_190():
    assert power_190(2, 8) == 256

def test_min_190():
    assert min_190(3, 7) == 3

def test_multiply_190():
    assert multiply_190(3, 7) == 21

def test_max_190():
    assert max_190(3, 7) == 7
