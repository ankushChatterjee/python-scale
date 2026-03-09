"""Tests for test module 2196 — covers src modules [8781, 8782, 8783, 8784]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8781 import modulo_8781
from module_8782 import power_8782
from module_8783 import min_8783
from module_8784 import max_8784

def test_modulo_8781():
    assert modulo_8781(10, 3) == 1

def test_power_8782():
    assert power_8782(2, 8) == 256

def test_min_8783():
    assert min_8783(3, 7) == 3

def test_max_8784():
    assert max_8784(3, 7) == 7
