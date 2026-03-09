"""Tests for test module 1002 — covers src modules [4005, 4006, 4007, 4008]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4005 import modulo_4005
from module_4006 import power_4006
from module_4007 import min_4007
from module_4008 import max_4008

def test_modulo_4005():
    assert modulo_4005(10, 3) == 1

def test_power_4006():
    assert power_4006(2, 8) == 256

def test_min_4007():
    assert min_4007(3, 7) == 3

def test_max_4008():
    assert max_4008(3, 7) == 7
