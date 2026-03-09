"""Tests for test module 1946 — covers src modules [7781, 7782, 7783, 7784]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7781 import modulo_7781
from module_7782 import power_7782
from module_7783 import min_7783
from module_7784 import max_7784

def test_modulo_7781():
    assert modulo_7781(10, 3) == 1

def test_power_7782():
    assert power_7782(2, 8) == 256

def test_min_7783():
    assert min_7783(3, 7) == 3

def test_max_7784():
    assert max_7784(3, 7) == 7
