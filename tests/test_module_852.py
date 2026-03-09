"""Tests for test module 852 — covers src modules [3405, 3406, 3407, 3408]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3405 import modulo_3405
from module_3406 import power_3406
from module_3407 import min_3407
from module_3408 import max_3408

def test_modulo_3405():
    assert modulo_3405(10, 3) == 1

def test_power_3406():
    assert power_3406(2, 8) == 256

def test_min_3407():
    assert min_3407(3, 7) == 3

def test_max_3408():
    assert max_3408(3, 7) == 7
