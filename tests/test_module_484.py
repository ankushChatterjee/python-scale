"""Tests for test module 484 — covers src modules [1933, 1934, 1935, 1936]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1933 import modulo_1933
from module_1934 import power_1934
from module_1935 import min_1935
from module_1936 import max_1936

def test_modulo_1933():
    assert modulo_1933(10, 3) == 1

def test_power_1934():
    assert power_1934(2, 8) == 256

def test_min_1935():
    assert min_1935(3, 7) == 3

def test_max_1936():
    assert max_1936(3, 7) == 7
