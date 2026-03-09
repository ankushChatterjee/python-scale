"""Tests for test module 2446 — covers src modules [9781, 9782, 9783, 9784]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9781 import modulo_9781
from module_9782 import power_9782
from module_9783 import min_9783
from module_9784 import max_9784

def test_modulo_9781():
    assert modulo_9781(10, 3) == 1

def test_power_9782():
    assert power_9782(2, 8) == 256

def test_min_9783():
    assert min_9783(3, 7) == 3

def test_max_9784():
    assert max_9784(3, 7) == 7
