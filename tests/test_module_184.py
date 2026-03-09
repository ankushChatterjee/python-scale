"""Tests for test module 184 — covers src modules [733, 734, 735, 736]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_733 import modulo_733
from module_734 import power_734
from module_735 import min_735
from module_736 import max_736

def test_modulo_733():
    assert modulo_733(10, 3) == 1

def test_power_734():
    assert power_734(2, 8) == 256

def test_min_735():
    assert min_735(3, 7) == 3

def test_max_736():
    assert max_736(3, 7) == 7
