"""Tests for test module 446 — covers src modules [1781, 1782, 1783, 1784]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1781 import modulo_1781
from module_1782 import power_1782
from module_1783 import min_1783
from module_1784 import max_1784

def test_modulo_1781():
    assert modulo_1781(10, 3) == 1

def test_power_1782():
    assert power_1782(2, 8) == 256

def test_min_1783():
    assert min_1783(3, 7) == 3

def test_max_1784():
    assert max_1784(3, 7) == 7
