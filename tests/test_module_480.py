"""Tests for test module 480 — covers src modules [1917, 1918, 1919, 1920]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1917 import modulo_1917
from module_1918 import power_1918
from module_1919 import min_1919
from module_1920 import max_1920

def test_modulo_1917():
    assert modulo_1917(10, 3) == 1

def test_power_1918():
    assert power_1918(2, 8) == 256

def test_min_1919():
    assert min_1919(3, 7) == 3

def test_max_1920():
    assert max_1920(3, 7) == 7
