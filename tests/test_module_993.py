"""Tests for test module 993 — covers src modules [3969, 3970, 3971, 3972]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3969 import add_3969
from module_3970 import subtract_3970
from module_3971 import multiply_3971
from module_3972 import divide_3972

def test_add_3969():
    assert add_3969(2, 3) == 5

def test_subtract_3970():
    assert subtract_3970(10, 4) == 6

def test_multiply_3971():
    assert multiply_3971(3, 7) == 21

def test_divide_3972():
    assert divide_3972(10, 2) == 5.0
