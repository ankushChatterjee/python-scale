"""Tests for test module 1502 — covers src modules [6005, 6006, 6007, 6008]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6005 import modulo_6005
from module_6006 import power_6006
from module_6007 import min_6007
from module_6008 import max_6008

def test_modulo_6005():
    assert modulo_6005(10, 3) == 1

def test_power_6006():
    assert power_6006(2, 8) == 256

def test_min_6007():
    assert min_6007(3, 7) == 3

def test_max_6008():
    assert max_6008(3, 7) == 7
