"""Tests for test module 2484 — covers src modules [9933, 9934, 9935, 9936]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9933 import modulo_9933
from module_9934 import power_9934
from module_9935 import min_9935
from module_9936 import max_9936

def test_modulo_9933():
    assert modulo_9933(10, 3) == 1

def test_power_9934():
    assert power_9934(2, 8) == 256

def test_min_9935():
    assert min_9935(3, 7) == 3

def test_max_9936():
    assert max_9936(3, 7) == 7
