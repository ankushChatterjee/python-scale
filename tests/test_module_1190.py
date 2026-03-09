"""Tests for test module 1190 — covers src modules [4757, 4758, 4759, 4760]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4757 import modulo_4757
from module_4758 import power_4758
from module_4759 import min_4759
from module_4760 import max_4760

def test_modulo_4757():
    assert modulo_4757(10, 3) == 1

def test_power_4758():
    assert power_4758(2, 8) == 256

def test_min_4759():
    assert min_4759(3, 7) == 3

def test_max_4760():
    assert max_4760(3, 7) == 7
