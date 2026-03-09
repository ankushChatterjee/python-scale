"""Tests for test module 1754 — covers src modules [7013, 7014, 7015, 7016]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7013 import modulo_7013
from module_7014 import power_7014
from module_7015 import min_7015
from module_7016 import max_7016

def test_modulo_7013():
    assert modulo_7013(10, 3) == 1

def test_power_7014():
    assert power_7014(2, 8) == 256

def test_min_7015():
    assert min_7015(3, 7) == 3

def test_max_7016():
    assert max_7016(3, 7) == 7
