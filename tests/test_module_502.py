"""Tests for test module 502 — covers src modules [2005, 2006, 2007, 2008]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2005 import modulo_2005
from module_2006 import power_2006
from module_2007 import min_2007
from module_2008 import max_2008

def test_modulo_2005():
    assert modulo_2005(10, 3) == 1

def test_power_2006():
    assert power_2006(2, 8) == 256

def test_min_2007():
    assert min_2007(3, 7) == 3

def test_max_2008():
    assert max_2008(3, 7) == 7
