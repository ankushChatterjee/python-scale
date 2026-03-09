"""Tests for test module 1388 — covers src modules [5549, 5550, 5551, 5552]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5549 import modulo_5549
from module_5550 import power_5550
from module_5551 import min_5551
from module_5552 import max_5552

def test_modulo_5549():
    assert modulo_5549(10, 3) == 1

def test_power_5550():
    assert power_5550(2, 8) == 256

def test_min_5551():
    assert min_5551(3, 7) == 3

def test_max_5552():
    assert max_5552(3, 7) == 7
