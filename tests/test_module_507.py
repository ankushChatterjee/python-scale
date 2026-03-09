"""Tests for test module 507 — covers src modules [2025, 2026, 2027, 2028]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2025 import add_2025
from module_2026 import subtract_2026
from module_2027 import multiply_2027
from module_2028 import divide_2028

def test_add_2025():
    assert add_2025(2, 3) == 5

def test_subtract_2026():
    assert subtract_2026(10, 4) == 6

def test_multiply_2027():
    assert multiply_2027(3, 7) == 21

def test_divide_2028():
    assert divide_2028(10, 2) == 5.0
