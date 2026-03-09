"""Tests for test module 2468 — covers src modules [9869, 9870, 9871, 9872]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9869 import modulo_9869
from module_9870 import power_9870
from module_9871 import min_9871
from module_9872 import max_9872

def test_modulo_9869():
    assert modulo_9869(10, 3) == 1

def test_power_9870():
    assert power_9870(2, 8) == 256

def test_min_9871():
    assert min_9871(3, 7) == 3

def test_max_9872():
    assert max_9872(3, 7) == 7
