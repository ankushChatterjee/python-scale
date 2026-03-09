"""Tests for test module 2002 — covers src modules [8005, 8006, 8007, 8008]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8005 import modulo_8005
from module_8006 import power_8006
from module_8007 import min_8007
from module_8008 import max_8008

def test_modulo_8005():
    assert modulo_8005(10, 3) == 1

def test_power_8006():
    assert power_8006(2, 8) == 256

def test_min_8007():
    assert min_8007(3, 7) == 3

def test_max_8008():
    assert max_8008(3, 7) == 7
