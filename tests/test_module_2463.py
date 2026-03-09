"""Tests for test module 2463 — covers src modules [9849, 9850, 9851, 9852]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9849 import add_9849
from module_9850 import subtract_9850
from module_9851 import multiply_9851
from module_9852 import divide_9852

def test_add_9849():
    assert add_9849(2, 3) == 5

def test_subtract_9850():
    assert subtract_9850(10, 4) == 6

def test_multiply_9851():
    assert multiply_9851(3, 7) == 21

def test_divide_9852():
    assert divide_9852(10, 2) == 5.0
