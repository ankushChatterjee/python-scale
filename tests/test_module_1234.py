"""Tests for test module 1234 — covers src modules [4933, 4934, 4935, 4936]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4933 import modulo_4933
from module_4934 import power_4934
from module_4935 import min_4935
from module_4936 import max_4936

def test_modulo_4933():
    assert modulo_4933(10, 3) == 1

def test_power_4934():
    assert power_4934(2, 8) == 256

def test_min_4935():
    assert min_4935(3, 7) == 3

def test_max_4936():
    assert max_4936(3, 7) == 7
