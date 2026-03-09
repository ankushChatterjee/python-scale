"""Tests for test module 2488 — covers src modules [9949, 9950, 9951, 9952]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9949 import modulo_9949
from module_9950 import power_9950
from module_9951 import min_9951
from module_9952 import max_9952

def test_modulo_9949():
    assert modulo_9949(10, 3) == 1

def test_power_9950():
    assert power_9950(2, 8) == 256

def test_min_9951():
    assert min_9951(3, 7) == 3

def test_max_9952():
    assert max_9952(3, 7) == 7
