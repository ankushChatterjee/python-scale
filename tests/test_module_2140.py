"""Tests for test module 2140 — covers src modules [8557, 8558, 8559, 8560]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8557 import modulo_8557
from module_8558 import power_8558
from module_8559 import min_8559
from module_8560 import max_8560

def test_modulo_8557():
    assert modulo_8557(10, 3) == 1

def test_power_8558():
    assert power_8558(2, 8) == 256

def test_min_8559():
    assert min_8559(3, 7) == 3

def test_max_8560():
    assert max_8560(3, 7) == 7
