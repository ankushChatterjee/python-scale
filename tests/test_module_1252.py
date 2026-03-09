"""Tests for test module 1252 — covers src modules [5005, 5006, 5007, 5008]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5005 import modulo_5005
from module_5006 import power_5006
from module_5007 import min_5007
from module_5008 import max_5008

def test_modulo_5005():
    assert modulo_5005(10, 3) == 1

def test_power_5006():
    assert power_5006(2, 8) == 256

def test_min_5007():
    assert min_5007(3, 7) == 3

def test_max_5008():
    assert max_5008(3, 7) == 7
