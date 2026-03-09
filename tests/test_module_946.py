"""Tests for test module 946 — covers src modules [3781, 3782, 3783, 3784]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3781 import modulo_3781
from module_3782 import power_3782
from module_3783 import min_3783
from module_3784 import max_3784

def test_modulo_3781():
    assert modulo_3781(10, 3) == 1

def test_power_3782():
    assert power_3782(2, 8) == 256

def test_min_3783():
    assert min_3783(3, 7) == 3

def test_max_3784():
    assert max_3784(3, 7) == 7
