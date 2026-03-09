"""Tests for test module 196 — covers src modules [781, 782, 783, 784]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_781 import modulo_781
from module_782 import power_782
from module_783 import min_783
from module_784 import max_784

def test_modulo_781():
    assert modulo_781(10, 3) == 1

def test_power_782():
    assert power_782(2, 8) == 256

def test_min_783():
    assert min_783(3, 7) == 3

def test_max_784():
    assert max_784(3, 7) == 7
