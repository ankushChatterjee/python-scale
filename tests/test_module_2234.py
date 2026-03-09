"""Tests for test module 2234 — covers src modules [8933, 8934, 8935, 8936]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8933 import modulo_8933
from module_8934 import power_8934
from module_8935 import min_8935
from module_8936 import max_8936

def test_modulo_8933():
    assert modulo_8933(10, 3) == 1

def test_power_8934():
    assert power_8934(2, 8) == 256

def test_min_8935():
    assert min_8935(3, 7) == 3

def test_max_8936():
    assert max_8936(3, 7) == 7
