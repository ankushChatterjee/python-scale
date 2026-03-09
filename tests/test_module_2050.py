"""Tests for test module 2050 — covers src modules [8197, 8198, 8199, 8200]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8197 import modulo_8197
from module_8198 import power_8198
from module_8199 import min_8199
from module_8200 import max_8200

def test_modulo_8197():
    assert modulo_8197(10, 3) == 1

def test_power_8198():
    assert power_8198(2, 8) == 256

def test_min_8199():
    assert min_8199(3, 7) == 3

def test_max_8200():
    assert max_8200(3, 7) == 7
