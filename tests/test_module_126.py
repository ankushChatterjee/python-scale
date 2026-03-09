"""Tests for test module 126 — covers src modules [501, 502, 503, 504]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_501 import modulo_501
from module_502 import power_502
from module_503 import min_503
from module_504 import max_504

def test_modulo_501():
    assert modulo_501(10, 3) == 1

def test_power_502():
    assert power_502(2, 8) == 256

def test_min_503():
    assert min_503(3, 7) == 3

def test_max_504():
    assert max_504(3, 7) == 7
