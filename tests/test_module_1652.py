"""Tests for test module 1652 — covers src modules [6605, 6606, 6607, 6608]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6605 import modulo_6605
from module_6606 import power_6606
from module_6607 import min_6607
from module_6608 import max_6608

def test_modulo_6605():
    assert modulo_6605(10, 3) == 1

def test_power_6606():
    assert power_6606(2, 8) == 256

def test_min_6607():
    assert min_6607(3, 7) == 3

def test_max_6608():
    assert max_6608(3, 7) == 7
