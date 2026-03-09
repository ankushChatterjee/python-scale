"""Tests for test module 578 — covers src modules [2309, 2310, 2311, 2312]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2309 import modulo_2309
from module_2310 import power_2310
from module_2311 import min_2311
from module_2312 import max_2312

def test_modulo_2309():
    assert modulo_2309(10, 3) == 1

def test_power_2310():
    assert power_2310(2, 8) == 256

def test_min_2311():
    assert min_2311(3, 7) == 3

def test_max_2312():
    assert max_2312(3, 7) == 7
