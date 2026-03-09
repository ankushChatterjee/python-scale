"""Tests for test module 1984 — covers src modules [7933, 7934, 7935, 7936]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7933 import modulo_7933
from module_7934 import power_7934
from module_7935 import min_7935
from module_7936 import max_7936

def test_modulo_7933():
    assert modulo_7933(10, 3) == 1

def test_power_7934():
    assert power_7934(2, 8) == 256

def test_min_7935():
    assert min_7935(3, 7) == 3

def test_max_7936():
    assert max_7936(3, 7) == 7
