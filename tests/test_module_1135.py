"""Tests for test module 1135 — covers src modules [4537, 4538, 4539, 4540]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4537 import add_4537
from module_4538 import subtract_4538
from module_4539 import multiply_4539
from module_4540 import divide_4540

def test_add_4537():
    assert add_4537(2, 3) == 5

def test_subtract_4538():
    assert subtract_4538(10, 4) == 6

def test_multiply_4539():
    assert multiply_4539(3, 7) == 21

def test_divide_4540():
    assert divide_4540(10, 2) == 5.0
