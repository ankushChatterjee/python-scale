"""Tests for test module 1446 — covers src modules [5781, 5782, 5783, 5784]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5781 import modulo_5781
from module_5782 import power_5782
from module_5783 import min_5783
from module_5784 import max_5784

def test_modulo_5781():
    assert modulo_5781(10, 3) == 1

def test_power_5782():
    assert power_5782(2, 8) == 256

def test_min_5783():
    assert min_5783(3, 7) == 3

def test_max_5784():
    assert max_5784(3, 7) == 7
