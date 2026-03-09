"""Tests for test module 2252 — covers src modules [9005, 9006, 9007, 9008]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9005 import modulo_9005
from module_9006 import power_9006
from module_9007 import min_9007
from module_9008 import max_9008

def test_modulo_9005():
    assert modulo_9005(10, 3) == 1

def test_power_9006():
    assert power_9006(2, 8) == 256

def test_min_9007():
    assert min_9007(3, 7) == 3

def test_max_9008():
    assert max_9008(3, 7) == 7
