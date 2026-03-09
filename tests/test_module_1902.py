"""Tests for test module 1902 — covers src modules [7605, 7606, 7607, 7608]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7605 import modulo_7605
from module_7606 import power_7606
from module_7607 import min_7607
from module_7608 import max_7608

def test_modulo_7605():
    assert modulo_7605(10, 3) == 1

def test_power_7606():
    assert power_7606(2, 8) == 256

def test_min_7607():
    assert min_7607(3, 7) == 3

def test_max_7608():
    assert max_7608(3, 7) == 7
