"""Tests for test module 1752 — covers src modules [7005, 7006, 7007, 7008]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7005 import modulo_7005
from module_7006 import power_7006
from module_7007 import min_7007
from module_7008 import max_7008

def test_modulo_7005():
    assert modulo_7005(10, 3) == 1

def test_power_7006():
    assert power_7006(2, 8) == 256

def test_min_7007():
    assert min_7007(3, 7) == 3

def test_max_7008():
    assert max_7008(3, 7) == 7
