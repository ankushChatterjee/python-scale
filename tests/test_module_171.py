"""Tests for test module 171 — covers src modules [681, 682, 683, 684]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_681 import add_681
from module_682 import subtract_682
from module_683 import multiply_683
from module_684 import divide_684

def test_add_681():
    assert add_681(2, 3) == 5

def test_subtract_682():
    assert subtract_682(10, 4) == 6

def test_multiply_683():
    assert multiply_683(3, 7) == 21

def test_divide_684():
    assert divide_684(10, 2) == 5.0
