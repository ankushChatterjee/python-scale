"""Tests for test module 1230 — covers src modules [4917, 4918, 4919, 4920]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4917 import modulo_4917
from module_4918 import power_4918
from module_4919 import min_4919
from module_4920 import max_4920

def test_modulo_4917():
    assert modulo_4917(10, 3) == 1

def test_power_4918():
    assert power_4918(2, 8) == 256

def test_min_4919():
    assert min_4919(3, 7) == 3

def test_max_4920():
    assert max_4920(3, 7) == 7
