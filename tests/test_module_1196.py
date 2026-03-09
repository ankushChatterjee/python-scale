"""Tests for test module 1196 — covers src modules [4781, 4782, 4783, 4784]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4781 import modulo_4781
from module_4782 import power_4782
from module_4783 import min_4783
from module_4784 import max_4784

def test_modulo_4781():
    assert modulo_4781(10, 3) == 1

def test_power_4782():
    assert power_4782(2, 8) == 256

def test_min_4783():
    assert min_4783(3, 7) == 3

def test_max_4784():
    assert max_4784(3, 7) == 7
