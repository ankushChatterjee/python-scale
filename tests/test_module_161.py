"""Tests for module 161."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_161 import add_161, max_161, power_161, divide_161

def test_add_161():
    assert add_161(2, 3) == 5

def test_max_161():
    assert max_161(3, 7) == 7

def test_power_161():
    assert power_161(2, 8) == 256

def test_divide_161():
    assert divide_161(10, 2) == 5.0
