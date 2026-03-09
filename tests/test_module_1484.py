"""Tests for test module 1484 — covers src modules [5933, 5934, 5935, 5936]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5933 import modulo_5933
from module_5934 import power_5934
from module_5935 import min_5935
from module_5936 import max_5936

def test_modulo_5933():
    assert modulo_5933(10, 3) == 1

def test_power_5934():
    assert power_5934(2, 8) == 256

def test_min_5935():
    assert min_5935(3, 7) == 3

def test_max_5936():
    assert max_5936(3, 7) == 7
