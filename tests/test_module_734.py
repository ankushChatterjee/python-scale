"""Tests for test module 734 — covers src modules [2933, 2934, 2935, 2936]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2933 import modulo_2933
from module_2934 import power_2934
from module_2935 import min_2935
from module_2936 import max_2936

def test_modulo_2933():
    assert modulo_2933(10, 3) == 1

def test_power_2934():
    assert power_2934(2, 8) == 256

def test_min_2935():
    assert min_2935(3, 7) == 3

def test_max_2936():
    assert max_2936(3, 7) == 7
