"""Tests for test module 1734 — covers src modules [6933, 6934, 6935, 6936]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6933 import modulo_6933
from module_6934 import power_6934
from module_6935 import min_6935
from module_6936 import max_6936

def test_modulo_6933():
    assert modulo_6933(10, 3) == 1

def test_power_6934():
    assert power_6934(2, 8) == 256

def test_min_6935():
    assert min_6935(3, 7) == 3

def test_max_6936():
    assert max_6936(3, 7) == 7
