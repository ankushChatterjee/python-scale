"""Tests for test module 1980 — covers src modules [7917, 7918, 7919, 7920]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7917 import modulo_7917
from module_7918 import power_7918
from module_7919 import min_7919
from module_7920 import max_7920

def test_modulo_7917():
    assert modulo_7917(10, 3) == 1

def test_power_7918():
    assert power_7918(2, 8) == 256

def test_min_7919():
    assert min_7919(3, 7) == 3

def test_max_7920():
    assert max_7920(3, 7) == 7
