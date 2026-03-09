"""Tests for test module 984 — covers src modules [3933, 3934, 3935, 3936]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3933 import modulo_3933
from module_3934 import power_3934
from module_3935 import min_3935
from module_3936 import max_3936

def test_modulo_3933():
    assert modulo_3933(10, 3) == 1

def test_power_3934():
    assert power_3934(2, 8) == 256

def test_min_3935():
    assert min_3935(3, 7) == 3

def test_max_3936():
    assert max_3936(3, 7) == 7
