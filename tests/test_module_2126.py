"""Tests for test module 2126 — covers src modules [8501, 8502, 8503, 8504]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8501 import modulo_8501
from module_8502 import power_8502
from module_8503 import min_8503
from module_8504 import max_8504

def test_modulo_8501():
    assert modulo_8501(10, 3) == 1

def test_power_8502():
    assert power_8502(2, 8) == 256

def test_min_8503():
    assert min_8503(3, 7) == 3

def test_max_8504():
    assert max_8504(3, 7) == 7
