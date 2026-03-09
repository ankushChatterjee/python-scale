"""Tests for test module 1102 — covers src modules [4405, 4406, 4407, 4408]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4405 import modulo_4405
from module_4406 import power_4406
from module_4407 import min_4407
from module_4408 import max_4408

def test_modulo_4405():
    assert modulo_4405(10, 3) == 1

def test_power_4406():
    assert power_4406(2, 8) == 256

def test_min_4407():
    assert min_4407(3, 7) == 3

def test_max_4408():
    assert max_4408(3, 7) == 7
