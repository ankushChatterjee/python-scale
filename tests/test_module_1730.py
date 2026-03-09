"""Tests for test module 1730 — covers src modules [6917, 6918, 6919, 6920]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6917 import modulo_6917
from module_6918 import power_6918
from module_6919 import min_6919
from module_6920 import max_6920

def test_modulo_6917():
    assert modulo_6917(10, 3) == 1

def test_power_6918():
    assert power_6918(2, 8) == 256

def test_min_6919():
    assert min_6919(3, 7) == 3

def test_max_6920():
    assert max_6920(3, 7) == 7
