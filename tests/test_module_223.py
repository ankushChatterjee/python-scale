"""Tests for test module 223 — covers src modules [889, 890, 891, 892]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_889 import add_889
from module_890 import subtract_890
from module_891 import multiply_891
from module_892 import divide_892

def test_add_889():
    assert add_889(2, 3) == 5

def test_subtract_890():
    assert subtract_890(10, 4) == 6

def test_multiply_891():
    assert multiply_891(3, 7) == 21

def test_divide_892():
    assert divide_892(10, 2) == 5.0
