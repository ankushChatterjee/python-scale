"""Tests for test module 980 — covers src modules [3917, 3918, 3919, 3920]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3917 import modulo_3917
from module_3918 import power_3918
from module_3919 import min_3919
from module_3920 import max_3920

def test_modulo_3917():
    assert modulo_3917(10, 3) == 1

def test_power_3918():
    assert power_3918(2, 8) == 256

def test_min_3919():
    assert min_3919(3, 7) == 3

def test_max_3920():
    assert max_3920(3, 7) == 7
