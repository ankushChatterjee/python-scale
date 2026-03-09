"""Tests for test module 234 — covers src modules [933, 934, 935, 936]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_933 import modulo_933
from module_934 import power_934
from module_935 import min_935
from module_936 import max_936

def test_modulo_933():
    assert modulo_933(10, 3) == 1

def test_power_934():
    assert power_934(2, 8) == 256

def test_min_935():
    assert min_935(3, 7) == 3

def test_max_936():
    assert max_936(3, 7) == 7
