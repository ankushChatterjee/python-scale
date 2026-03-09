"""Tests for test module 1140 — covers src modules [4557, 4558, 4559, 4560]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4557 import modulo_4557
from module_4558 import power_4558
from module_4559 import min_4559
from module_4560 import max_4560

def test_modulo_4557():
    assert modulo_4557(10, 3) == 1

def test_power_4558():
    assert power_4558(2, 8) == 256

def test_min_4559():
    assert min_4559(3, 7) == 3

def test_max_4560():
    assert max_4560(3, 7) == 7
