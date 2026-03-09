"""Tests for test module 696 — covers src modules [2781, 2782, 2783, 2784]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2781 import modulo_2781
from module_2782 import power_2782
from module_2783 import min_2783
from module_2784 import max_2784

def test_modulo_2781():
    assert modulo_2781(10, 3) == 1

def test_power_2782():
    assert power_2782(2, 8) == 256

def test_min_2783():
    assert min_2783(3, 7) == 3

def test_max_2784():
    assert max_2784(3, 7) == 7
