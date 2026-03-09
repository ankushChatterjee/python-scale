"""Tests for test module 1696 — covers src modules [6781, 6782, 6783, 6784]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6781 import modulo_6781
from module_6782 import power_6782
from module_6783 import min_6783
from module_6784 import max_6784

def test_modulo_6781():
    assert modulo_6781(10, 3) == 1

def test_power_6782():
    assert power_6782(2, 8) == 256

def test_min_6783():
    assert min_6783(3, 7) == 3

def test_max_6784():
    assert max_6784(3, 7) == 7
