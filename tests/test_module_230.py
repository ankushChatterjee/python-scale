"""Tests for test module 230 — covers src modules [917, 918, 919, 920]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_917 import modulo_917
from module_918 import power_918
from module_919 import min_919
from module_920 import max_920

def test_modulo_917():
    assert modulo_917(10, 3) == 1

def test_power_918():
    assert power_918(2, 8) == 256

def test_min_919():
    assert min_919(3, 7) == 3

def test_max_920():
    assert max_920(3, 7) == 7
